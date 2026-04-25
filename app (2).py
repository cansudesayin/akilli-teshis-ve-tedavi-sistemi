from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)

# ==============================================================================
# CORS AYARI — HTML sayfalarının (frontend) bu API'ye istek atabilmesi için
# gereklidir. Geliştirme aşamasında tüm kaynaklara izin verilmektedir.
# Yayına alınırken origins kısıtlanmalıdır.
# ==============================================================================
CORS(app)

# ==============================================================================
# YARDIMCI FONKSİYONLAR
# ==============================================================================

def hata_yaniti(mesaj, kod=400):
    """Standart hata yanıtı üretir."""
    return jsonify({
        "hata": True,
        "mesaj": mesaj,
        "zaman": datetime.now().isoformat()
    }), kod

def basari_yaniti(veri, kod=200):
    """Standart başarı yanıtı üretir."""
    return jsonify({
        "hata": False,
        "zaman": datetime.now().isoformat(),
        **veri
    }), kod

# ==============================================================================
# 1. KAPI: YENİ HASTA KAYDI (Frontend -> API -> Veritabanı)
# POST /api/v1/hastalar
# ==============================================================================
@app.route('/api/v1/hastalar', methods=['POST'])
def hasta_kayit():
    """
    Yeni hasta kaydı oluşturur.

    Beklenen JSON:
    {
        "yas": 45,
        "cinsiyet": "Erkek",
        "gecmis": "Hipertansiyon",
        "diyabet": false
    }

    Başarılı yanıt (201):
    {
        "mesaj": "Hasta başarıyla kaydedildi",
        "hasta_id": "1001"
    }
    """

    # --- Gelen veriyi kontrol et ---
    if not request.is_json:
        return hata_yaniti("İstek JSON formatında olmalıdır.", 415)

    veri = request.get_json()

    if not veri:
        return hata_yaniti("Gönderilen veri boş olamaz.", 400)

    # --- Zorunlu alan kontrolü ---
    zorunlu_alanlar = ['yas', 'cinsiyet']
    eksik = [alan for alan in zorunlu_alanlar if alan not in veri]
    if eksik:
        return hata_yaniti(f"Eksik zorunlu alanlar: {', '.join(eksik)}", 400)

    # --- Yaş doğrulama ---
    try:
        yas = int(veri['yas'])
        if yas < 0 or yas > 150:
            return hata_yaniti("Yaş 0 ile 150 arasında olmalıdır.", 400)
    except (ValueError, TypeError):
        return hata_yaniti("Yaş sayısal bir değer olmalıdır.", 400)

    # --- Cinsiyet doğrulama ---
    gecerli_cinsiyetler = ['Erkek', 'Kadın', 'erkek', 'kadın', 'E', 'K']
    if veri['cinsiyet'] not in gecerli_cinsiyetler:
        return hata_yaniti("Cinsiyet 'Erkek' veya 'Kadın' olmalıdır.", 400)

    # [ALİ İÇİN NOT (Veritabanı Entegrasyonu — 5. Hafta Görevi)]:
    # Burada MySQL bağlantısı kurulacak ve veri Patients tablosuna yazılacak.
    # Örnek:
    #   cursor.execute("INSERT INTO Patients (age, gender, medical_history, diabetes)"
    #                  " VALUES (%s, %s, %s, %s)",
    #                  (yas, veri['cinsiyet'], veri.get('gecmis',''), veri.get('diyabet', False)))
    #   hasta_id = cursor.lastrowid

    return basari_yaniti({
        "mesaj": "Hasta başarıyla sisteme kaydedildi.",
        "hasta_id": "1001"
    }, 201)


# ==============================================================================
# 2. KAPI: HASTA BİLGİSİ GÖRÜNTÜLEME
# GET /api/v1/hastalar/<hasta_id>
# ==============================================================================
@app.route('/api/v1/hastalar/<int:hasta_id>', methods=['GET'])
def hasta_getir(hasta_id):
    """
    Belirtilen hasta ID'sine ait bilgileri döndürür.

    Başarılı yanıt (200):
    {
        "hasta_id": 1001,
        "yas": 48,
        "cinsiyet": "Erkek",
        ...
    }
    """

    if hasta_id <= 0:
        return hata_yaniti("Geçersiz hasta ID.", 400)

    # [ALİ İÇİN NOT (Veritabanı Entegrasyonu — 5. Hafta Görevi)]:
    # cursor.execute("SELECT * FROM Patients WHERE patient_id = %s", (hasta_id,))
    # hasta = cursor.fetchone()
    # if not hasta: return hata_yaniti("Hasta bulunamadı.", 404)

    sahte_hasta = {
        "hasta_id": hasta_id,
        "yas": 48,
        "cinsiyet": "Erkek",
        "gecmis": "Hipertansiyon, Tip 2 Diyabet",
        "diyabet": True,
        "kan_grubu": "A Rh+",
        "kayit_tarihi": "2026-01-03"
    }

    return basari_yaniti(sahte_hasta)


# ==============================================================================
# 3. KAPI: GÖRÜNTÜ YÜKLEME VE YAPAY ZEKA ANALİZİ BAŞLATMA
# POST /api/v1/analiz/baslat
# ==============================================================================
@app.route('/api/v1/analiz/baslat', methods=['POST'])
def analiz_baslat():
    """
    Görüntü analizini başlatır.

    Beklenen JSON:
    {
        "hasta_id": "1001",
        "goruntu_turu": "dermoskopi",
        "dosya_adi": "cilt_lesyon.jpg"
    }

    Başarılı yanıt (202):
    {
        "mesaj": "Analiz başlatıldı",
        "analiz_durumu": "İşleniyor",
        "analiz_id": 5001
    }
    """

    if not request.is_json:
        return hata_yaniti("İstek JSON formatında olmalıdır.", 415)

    veri = request.get_json()

    if not veri:
        return hata_yaniti("Gönderilen veri boş olamaz.", 400)

    # --- Zorunlu alan kontrolü ---
    zorunlu_alanlar = ['hasta_id', 'goruntu_turu']
    eksik = [alan for alan in zorunlu_alanlar if alan not in veri]
    if eksik:
        return hata_yaniti(f"Eksik zorunlu alanlar: {', '.join(eksik)}", 400)

    # --- Görüntü türü doğrulama ---
    gecerli_turler = ['dermoskopi', 'fundus', 'oct', 'xray', 'ct', 'mri']
    if veri['goruntu_turu'].lower() not in gecerli_turler:
        return hata_yaniti(
            f"Geçersiz görüntü türü. Kabul edilenler: {', '.join(gecerli_turler)}", 400)

    hasta_id = veri['hasta_id']

    # [SELİM İÇİN NOT (Veri Ön İşleme — 5. ve 6. Hafta Görevi)]:
    # 1. Görüntü buradan Selim'in ön işleme modülüne gönderilecek:
    #    temiz_goruntu = on_isleme(goruntu_dosyasi)  # resize 224x224, normalize, gürültü temizleme
    #
    # [ENES İÇİN NOT (CNN Modeli — 5. ve 6. Hafta Görevi)]:
    # 2. Selim'in temizlediği görüntü Enes'in CNN modeline verilecek:
    #    sonuc = model.predict(temiz_goruntu)  # Eğitilmiş TensorFlow/Keras modeli
    #
    # [ALİ İÇİN NOT (Veritabanı Entegrasyonu — 5. Hafta Görevi)]:
    # 3. Model çıktısı veritabanına kaydedilecek:
    #    cursor.execute("INSERT INTO Diagnoses (image_id, disease_name, risk_score, stage)"
    #                   " VALUES (%s, %s, %s, %s)", (image_id, tehsis, risk_skoru, evre))

    return basari_yaniti({
        "mesaj": f"{hasta_id} numaralı hasta için yapay zeka analizi başlatıldı.",
        "analiz_durumu": "İşleniyor",
        "analiz_id": 5001
    }, 202)


# ==============================================================================
# 4. KAPI: TEŞHİS SONUCUNU GÖRÜNTÜLEME
# GET /api/v1/analiz/sonuc/<analiz_id>
# ==============================================================================
@app.route('/api/v1/analiz/sonuc/<int:analiz_id>', methods=['GET'])
def sonuc_getir(analiz_id):
    """
    Yapay zeka analiz sonucunu döndürür.

    Başarılı yanıt (200):
    {
        "analiz_id": 5001,
        "tehsis": "Malign Melanom",
        "evre": "Evre 1",
        "risk_skoru": 88.5,
        "ai_aciklamasi": "..."
    }
    """

    if analiz_id <= 0:
        return hata_yaniti("Geçersiz analiz ID.", 400)

    # [ALİ İÇİN NOT (Veritabanı Entegrasyonu — 5. Hafta Görevi)]:
    # cursor.execute("""
    #     SELECT d.*, i.image_type FROM Diagnoses d
    #     JOIN Images i ON d.image_id = i.image_id
    #     WHERE d.diagnosis_id = %s
    # """, (analiz_id,))
    # sonuc = cursor.fetchone()
    # if not sonuc: return hata_yaniti("Analiz sonucu bulunamadı.", 404)

    sahte_sonuc = {
        "analiz_id": analiz_id,
        "hasta_id": 1001,
        "tehsis": "Malign Melanom (Cilt Kanseri)",
        "evre": "Evre 1",
        "risk_skoru": 88.5,
        "ai_aciklamasi": "Lezyon sınırlarında asimetri tespit edildi. Biyopsi önerilir.",
        "isi_haritasi_url": f"/medya/analiz/heatmap_{analiz_id}.png",
        "analiz_tarihi": datetime.now().isoformat()
    }

    return basari_yaniti(sahte_sonuc)


# ==============================================================================
# 5. KAPI: TEDAVİ PLANI
# GET /api/v1/tedavi/plan/<analiz_id>
# ==============================================================================
@app.route('/api/v1/tedavi/plan/<int:analiz_id>', methods=['GET'])
def tedavi_plan(analiz_id):
    """
    Analize göre kişiselleştirilmiş tedavi planı döndürür.

    Başarılı yanıt (200):
    {
        "onerilen_tedavi": "...",
        "zamanlama_protokolu": "...",
        "sonraki_randevu": "..."
    }
    """

    if analiz_id <= 0:
        return hata_yaniti("Geçersiz analiz ID.", 400)

    sahte_plan = {
        "analiz_id": analiz_id,
        "onerilen_tedavi": "Geniş Eksizyon (Cerrahi Çıkarma)",
        "zamanlama_protokolu": "Acil — 2 hafta içinde",
        "sonraki_randevu_hedefi": "2 Hafta Sonra",
        "alternatif_tedaviler": ["Mohs Cerrahisi", "İmmünoterapi"],
        "notlar": "Sentinel lenf nodu biyopsisi değerlendirilmelidir."
    }

    return basari_yaniti(sahte_plan)


# ==============================================================================
# HATA YÖNETİMİ — Tanımlanmamış rotalar ve sunucu hataları
# ==============================================================================
@app.errorhandler(404)
def sayfa_bulunamadi(e):
    return hata_yaniti("Bu endpoint mevcut değil.", 404)

@app.errorhandler(405)
def metod_hatasi(e):
    return hata_yaniti("Bu HTTP metodu bu endpoint için geçerli değil.", 405)

@app.errorhandler(500)
def sunucu_hatasi(e):
    return hata_yaniti("Sunucu hatası oluştu. Lütfen tekrar deneyin.", 500)


# ==============================================================================
# SUNUCUYU BAŞLATMA
# Terminalde: python app.py
# ==============================================================================
if __name__ == '__main__':
    print("=" * 60)
    print("  Siber Şifacılar — MediAI API Sunucusu Başlatılıyor...")
    print("=" * 60)
    print(f"  Adres : http://localhost:5000")
    print(f"  Mod   : Geliştirme (Debug)")
    print("=" * 60)
    app.run(debug=True, port=5000)
