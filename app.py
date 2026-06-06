from flask import Flask, request, jsonify
from flask_cors import CORS # Cansude'nin eklediği CORS desteği
import mysql.connector
from datetime import datetime

app = Flask(__name__)
CORS(app) # Arayüzlerin API'ye erişebilmesi için şart!

# ==============================================================================
# VERİTABANI BAĞLANTISI (Edanur'un MySQL Şemasına Göre)
# ==============================================================================
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Burayı kendi kullanıcı adınla güncelle
        password="sifre",    # Burayı kendi şifrenle güncelle
        database="mediai_db" # Edanur'un raporundaki veritabanı adı
    )

# ==============================================================================
# 1. KAPI: YENİ HASTA KAYDI (POST)
# ==============================================================================
@app.route('/api/v1/hastalar', methods=['POST'])
def hasta_kayit():
    gelen_veri = request.json
    
    # Cansude'nin istediği veri doğrulama (Validation)
    yas = gelen_veri.get('yas')
    cinsiyet = gelen_veri.get('cinsiyet')
    
    if not yas or not cinsiyet:
        return jsonify({
            "hata": True, 
            "mesaj": "Eksik zorunlu alanlar: yas, cinsiyet",
            "zaman": datetime.now().isoformat()
        }), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Edanur'un 'Patients' tablosuna kayıt (Parametrik - Güvenli Sorgu)
        sql = "INSERT INTO Patients (age, gender, medical_history, diabetes) VALUES (%s, %s, %s, %s)"
        values = (yas, cinsiyet, gelen_veri.get('gecmis', ''), gelen_veri.get('diyabet', False))
        
        cursor.execute(sql, values)
        conn.commit()
        
        h_id = cursor.lastrowid # Veritabanından gelen gerçek ID

        cursor.close()
        conn.close()

        return jsonify({
            "hata": False,
            "mesaj": "Hasta başarıyla MySQL veritabanına kaydedildi.",
            "hasta_id": str(h_id),
            "zaman": datetime.now().isoformat()
        }), 201
    except Exception as e:
        return jsonify({"hata": True, "mesaj": f"DB Hatası: {str(e)}"}), 500

# ==============================================================================
# 2. KAPI: ANALİZ BAŞLATMA (POST)
# ==============================================================================
@app.route('/api/v1/analiz/baslat', methods=['POST'])
def analiz_baslat():
    gelen_veri = request.json
    hasta_id = gelen_veri.get('hasta_id')
    
    # [SELİM & ENES İÇİN]: Burası ileride AI modeline bağlanacak
    return jsonify({
        "hata": False,
        "mesaj": f"{hasta_id} ID'li hasta için analiz başlatıldı.",
        "analiz_durumu": "İşleniyor",
        "analiz_id": 5001,
        "zaman": datetime.now().isoformat()
    }), 202

# ==============================================================================
# 3. KAPI: TEŞHİS SONUCUNU GETİR (GET)
# ==============================================================================
@app.route('/api/v1/analiz/sonuc/<int:analiz_id>', methods=['GET'])
def sonuc_getir(analiz_id):
    # Cansude'nin istediği standart sonuç formatı
    return jsonify({
        "hata": False,
        "analiz_id": analiz_id,
        "tehsis": "Malign Melanom (Cilt Kanseri)",
        "risk_skoru": 88.5,
        "ai_aciklamasi": "Lezyon sınırlarında asimetri tespit edildi.",
        "zaman": datetime.now().isoformat()
    }), 200

# Cansude'nin eklediği 404 Hata Yönetimi
@app.errorhandler(404)
def sayfa_bulunamadi(e):
    return jsonify({"hata": True, "mesaj": "Geçersiz endpoint adresi!"}), 404

if __name__ == '__main__':
    print("============================================================")
    print("  Siber Şifacılar — MediAI API Sunucusu Başlatılıyor...")
    print("============================================================")
    app.run(debug=True, port=5000)