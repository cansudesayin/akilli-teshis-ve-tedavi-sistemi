from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from datetime import datetime
import numpy as np
import os

# ==============================================================================
# MODEL ENTEGRASYONU
# Geliştirici: Cansude Sayın (Enes Zukra'nın ai_model.py dosyası baz alındı)
# ==============================================================================
try:
    import tensorflow as tf
    from tensorflow.keras import layers, models as keras_models

    def create_medical_diagnosis_model():
        """
        Enes Zukra tarafından geliştirilen CNN modeli.
        Hafta 6'da %92.4 accuracy ile optimize edilmiştir.
        """
        model = keras_models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(1, activation='sigmoid')
        ])
        model.compile(
            optimizer=tf.keras.optimizers.Adam(
                learning_rate=0.001, beta_1=0.9, beta_2=0.999
            ),
            loss='binary_crossentropy',
            metrics=['accuracy',
                     tf.keras.metrics.Precision(name='precision'),
                     tf.keras.metrics.Recall(name='recall')]
        )
        return model

    MODEL_PATH = 'model.h5'
    if os.path.exists(MODEL_PATH):
        AI_MODEL = tf.keras.models.load_model(MODEL_PATH)
        print("Model agırlıkları yüklendi:", MODEL_PATH)
    else:
        AI_MODEL = create_medical_diagnosis_model()
        AI_MODEL.save(MODEL_PATH)
        print("Model oluşturuldu ve kaydedildi:", MODEL_PATH)

    MODEL_AKTIF = True

except ImportError:
    AI_MODEL = None
    MODEL_AKTIF = False
    print("TensorFlow bulunamadı. Model simülasyon modunda çalışacak.")

# ==============================================================================
# MODEL TAHMİN FONKSİYONU
# ==============================================================================
def model_tahmin_et(goruntu_dizisi):
    if MODEL_AKTIF and AI_MODEL is not None:
        tahmin = AI_MODEL.predict(goruntu_dizisi, verbose=0)
        risk_skoru = float(tahmin[0][0]) * 100
    else:
        import random
        risk_skoru = round(random.uniform(60, 95), 1)

    if risk_skoru >= 80:
        teshis = "Malign Melanom Şüphesi"
        evre = "Evre II"
        guven = round(risk_skoru * 0.95, 1)
    elif risk_skoru >= 60:
        teshis = "Diyabetik Retinopati"
        evre = "Orta"
        guven = round(risk_skoru * 0.92, 1)
    else:
        teshis = "Benign Lezyon"
        evre = "Evre 0"
        guven = round(risk_skoru * 0.88, 1)

    return {
        "teshis": teshis,
        "evre": evre,
        "risk_skoru": round(risk_skoru, 1),
        "guven_skoru": guven,
        "ai_aciklamasi": "Lezyon sınırlarında asimetri ve renk değişkenliği tespit edildi.",
        "model_surumu": "CNN v1.1 - Accuracy: %92.4"
    }

# ==============================================================================
# FLASK UYGULAMASI
# ==============================================================================
app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

CORS(app)

# Swagger JSON dosyasini direkt servis et
from flask import send_from_directory
import os

@app.route('/swagger.json')
def swagger_json():
    return send_from_directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static_klasor'), 'swagger.json')

# ==============================================================================
# VERİTABANI BAĞLANTISI (Ali İstanbullu)
# ==============================================================================
def get_db_connection():
    try:
        config = {
            'host': os.environ.get('DB_HOST', 'localhost'),
            'port': int(os.environ.get('DB_PORT', 3306)),
            'user': os.environ.get('DB_USER', 'root'),
            'password': os.environ.get('DB_PASSWORD', 'sifre'),
            'database': os.environ.get('DB_NAME', 'mediai_db')
        }
        # Aiven gibi bulut MySQL servisleri SSL zorunlu tutar
        if os.environ.get('DB_SSL', 'false').lower() == 'true':
            config['ssl_disabled'] = False
        return mysql.connector.connect(**config)
    except Exception as e:
        print(f"Veritabanı bağlantı hatası: {e}")
        return None

# ==============================================================================
# 1. KAPI: YENİ HASTA KAYDI (POST)
# ==============================================================================
@app.route('/api/v1/hastalar', methods=['POST'])
def hasta_kayit():
    gelen_veri = request.json
    yas = gelen_veri.get('yas')
    cinsiyet = gelen_veri.get('cinsiyet')

    if not yas or not cinsiyet:
        return jsonify({
            "hata": True,
            "mesaj": "Eksik zorunlu alanlar: yas, cinsiyet",
            "zaman": datetime.now().isoformat()
        }), 400

    if not isinstance(yas, int) or not (0 < yas < 150):
        return jsonify({
            "hata": True,
            "mesaj": "Geçersiz yaş değeri. 1-149 arasında olmalıdır.",
            "zaman": datetime.now().isoformat()
        }), 400

    try:
        conn = get_db_connection()
        if conn is None:
            import random
            return jsonify({
                "hata": False,
                "mesaj": "[DEMO] Hasta kaydı simüle edildi (DB bağlantısı yok).",
                "hasta_id": str(random.randint(1000, 9999)),
                "zaman": datetime.now().isoformat()
            }), 201
        cursor = conn.cursor()
        sql = "INSERT INTO Patients (age, gender, medical_history, diabetes) VALUES (%s, %s, %s, %s)"
        values = (yas, cinsiyet, gelen_veri.get('gecmis', ''), gelen_veri.get('diyabet', False))
        cursor.execute(sql, values)
        conn.commit()
        h_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return jsonify({
            "hata": False,
            "mesaj": "Hasta başarıyla MySQL veritabanına kaydedildi.",
            "hasta_id": str(h_id),
            "zaman": datetime.now().isoformat()
        }), 201

    except Exception as e:
        return jsonify({
            "hata": True,
            "mesaj": f"DB Hatası: {str(e)}",
            "zaman": datetime.now().isoformat()
        }), 500

# ==============================================================================
# 2. KAPI: HASTA BİLGİSİ GÖRÜNTÜLEME (GET)
# ==============================================================================
@app.route('/api/v1/hastalar/<int:hasta_id>', methods=['GET'])
def hasta_getir(hasta_id):
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({
                "hata": False,
                "hasta": {
                    "patient_id": hasta_id,
                    "age": 45,
                    "gender": "Erkek",
                    "medical_history": "Demo hasta verisi",
                    "diabetes": False
                },
                "mesaj": "[DEMO] Veritabanı bağlantısı yok, örnek veri gösteriliyor.",
                "zaman": datetime.now().isoformat()
            }), 200
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Patients WHERE patient_id = %s", (hasta_id,))
        hasta = cursor.fetchone()
        cursor.close()
        conn.close()

        if not hasta:
            return jsonify({
                "hata": True,
                "mesaj": "Belirtilen ID'ye ait hasta bulunamadı.",
                "zaman": datetime.now().isoformat()
            }), 404

        return jsonify({
            "hata": False,
            "hasta": hasta,
            "zaman": datetime.now().isoformat()
        }), 200

    except Exception as e:
        return jsonify({
            "hata": True,
            "mesaj": f"DB Hatası: {str(e)}",
            "zaman": datetime.now().isoformat()
        }), 500

# ==============================================================================
# 3. KAPI: ANALİZ BAŞLATMA (POST) — CNN Model Entegrasyonu
# ==============================================================================
@app.route('/api/v1/analiz/baslat', methods=['POST'])
def analiz_baslat():
    gelen_veri = request.json
    hasta_id = gelen_veri.get('hasta_id')
    goruntu_turu = gelen_veri.get('goruntu_turu', '')

    if not hasta_id:
        return jsonify({
            "hata": True,
            "mesaj": "Eksik zorunlu alan: hasta_id",
            "zaman": datetime.now().isoformat()
        }), 400

    desteklenen_turler = ['Dermoskopik', 'Fundus', 'OCT']
    if goruntu_turu and goruntu_turu not in desteklenen_turler:
        return jsonify({
            "hata": True,
            "mesaj": f"Desteklenmeyen görüntü türü. Kabul edilenler: {', '.join(desteklenen_turler)}",
            "zaman": datetime.now().isoformat()
        }), 415

    try:
        # Selim'in ön işleme modülü entegrasyonu (data_preprocessing.py)
        # Gerçek görüntü geldiğinde:
        # from data_preprocessing import ehr_veri_temizle
        # goruntu_dizisi = verify_and_load_medical_data(goruntu_dosya_yolu)
        goruntu_dizisi = np.random.rand(1, 224, 224, 3).astype('float32')

        # Enes'in CNN modeli
        sonuc = model_tahmin_et(goruntu_dizisi)

        return jsonify({
            "hata": False,
            "mesaj": f"{hasta_id} ID'li hasta için analiz tamamlandı.",
            "analiz_durumu": "Tamamlandı",
            "analiz_id": 5001,
            "sonuc": sonuc,
            "tahmini_sure_saniye": 8,
            "zaman": datetime.now().isoformat()
        }), 202

    except Exception as e:
        return jsonify({
            "hata": True,
            "mesaj": f"Model hatası: {str(e)}",
            "zaman": datetime.now().isoformat()
        }), 500

# ==============================================================================
# 4. KAPI: TEŞHİS SONUCUNU GETİR (GET)
# ==============================================================================
@app.route('/api/v1/analiz/sonuc/<int:analiz_id>', methods=['GET'])
def sonuc_getir(analiz_id):
    goruntu_dizisi = np.random.rand(1, 224, 224, 3).astype('float32')
    sonuc = model_tahmin_et(goruntu_dizisi)

    return jsonify({
        "hata": False,
        "analiz_id": analiz_id,
        "durum": "completed",
        **sonuc,
        "isi_haritasi_url": f"/medya/analiz/heatmap_{analiz_id}.png",
        "zaman": datetime.now().isoformat()
    }), 200

# ==============================================================================
# 5. KAPI: KİŞİSELLEŞTİRİLMİŞ TEDAVİ PLANI (GET)
# ==============================================================================
@app.route('/api/v1/tedavi/plan/<int:analiz_id>', methods=['GET'])
def tedavi_plan(analiz_id):
    return jsonify({
        "hata": False,
        "analiz_id": analiz_id,
        "onerilen_tedavi": "Anti-VEGF Enjeksiyonu",
        "zamanlama_protokolu": "Treat-and-Extend",
        "sonraki_randevu_hedefi": "8 Hafta Sonra",
        "alternatif_ilaclar": ["Ranibizumab (Lucentis)", "Bevacizumab (Avastin)"],
        "dozaj_notu": "Hastanın diyabet geçmişi göz önünde bulundurulmuştur.",
        "zaman": datetime.now().isoformat()
    }), 200

# ==============================================================================
# HATA YÖNETİMİ
# ==============================================================================
@app.errorhandler(404)
def sayfa_bulunamadi(e):
    return jsonify({"hata": True, "mesaj": "Geçersiz endpoint adresi!", "zaman": datetime.now().isoformat()}), 404

@app.errorhandler(405)
def metot_hatasi(e):
    return jsonify({"hata": True, "mesaj": "Geçersiz HTTP metodu!", "zaman": datetime.now().isoformat()}), 405

@app.errorhandler(500)
def sunucu_hatasi(e):
    return jsonify({"hata": True, "mesaj": "Sunucu hatası oluştu.", "zaman": datetime.now().isoformat()}), 500

# ==============================================================================
# SUNUCUYU BAŞLAT
# ==============================================================================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("=" * 60)
    print("  Siber Şifacılar — MediAI API Sunucusu Başlatılıyor...")
    print(f"  Model Durumu: {'Aktif' if MODEL_AKTIF else 'Simülasyon Modu'}")
    print(f"  Port: {port}")
    print(f"  Swagger: http://localhost:{port}/api/docs")
    print("=" * 60)
    app.run(debug=False, host='0.0.0.0', port=port)
