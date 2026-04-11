from flask import Flask, request, jsonify

app = Flask(__name__)

# ==============================================================================
# 1. KAPI: YENİ HASTA KAYDI (Frontend -> API -> Veritabanı)
# ==============================================================================
@app.route('/api/v1/hastalar', methods=['POST'])
def hasta_kayit():
    # [CANSUDE İÇİN NOT (UI/UX)]:
    # Cansude, arayüzden "Kaydet" butonuna basıldığında formdaki 'ad', 'soyad', 
    # 'yas' gibi bilgileri JSON formatında bu kapıya (POST) göndereceksin.
    gelen_veri = request.json
    
    # [EDANUR İÇİN NOT (Veritabanı)]: 
    # Edanur, Cansude'nin gönderdiği bu 'gelen_veri'yi alıp, senin tasarladığın 
    # MySQL veritabanındaki "Hastalar" tablosuna tam bu satırda kaydedeceğiz.
    
    # Şimdilik Frontend tasarımı test edilebilsin diye Cansude'ye sahte (dummy) bir cevap dönüyoruz:
    return jsonify({
        "mesaj": "Hasta başarıyla sisteme kaydedildi",
        "hasta_id": "1001"
    }), 201


# ==============================================================================
# 2. KAPI: FOTOĞRAF YÜKLEME VE YAPAY ZEKA ANALİZİ (Frontend -> API -> AI)
# ==============================================================================
@app.route('/api/v1/analiz/baslat', methods=['POST'])
def analiz_baslat():
    # [CANSUDE İÇİN NOT (UI/UX)]: 
    # Doktor fotoğraf seçip "Analiz Et" dediğinde, o fotoğraf dosyasını ve 
    # hastanın ID'sini bu kapıya POST ediyorsun.
    gelen_veri = request.json
    hasta_id = gelen_veri.get('hasta_id')
    
    # [SELİM & ENES İÇİN NOT (Ön İşleme & AI Modeli)]: 
    # Beyler, Cansude'den gelen fotoğrafı önce Selim'in gürültü temizleme fonksiyonuna
    # sokacağız. Çıkan temiz fotoğrafı tam burada Enes'in CNN modeline (model.predict)
    # verip kanser risk skorunu üreteceğiz.
    
    return jsonify({
        "mesaj": f"{hasta_id} numaralı hasta için yapay zeka analizi başlatıldı.",
        "analiz_durumu": "İşleniyor"
    }), 202


# ==============================================================================
# 3. KAPI: TEŞHİS SONUCUNU GÖSTERME (Veritabanı -> API -> Frontend)
# ==============================================================================
@app.route('/api/v1/analiz/sonuc/<int:analiz_id>', methods=['GET'])
def sonuc_getir(analiz_id):
    # [EDANUR İÇİN NOT (Veritabanı)]: 
    # Edanur, arayüz bu kapıyı çaldığında senin veritabanına bağlanıp, bu 'analiz_id'ye 
    # ait risk skorunu, ısı haritasını ve tedavi planını çekecek kodu buraya yazacağız.
    
    # [CANSUDE İÇİN NOT (UI/UX)]: 
    # Cansude, doktor "Sonucu Gör" sayfasına girdiğinde bu kapıya GET isteği atacaksın.
    # Ben sana veritabanından alıp aşağıdaki gibi bir JSON döneceğim. 
    # Sen de HTML/CSS şablonunda 'risk_skoru' ve 'tehsis' verilerini ekrana basacaksın.
    sahte_sonuc = {
        "analiz_id": analiz_id,
        "tehsis": "Malign Melanom (Cilt Kanseri)",
        "evre": "Evre 1",
        "risk_skoru": 88.5,
        "ai_aciklamasi": "Lezyon sınırlarında asimetri tespit edildi."
    }
    
    return jsonify(sahte_sonuc), 200


# ==============================================================================
# SUNUCUYU BAŞLATMA KOMUTU (Terminalde 'python app.py' yazılınca çalışır)
# ==============================================================================
if __name__ == '__main__':
    print("Siber Şifacılar API Sunucusu Başlatılıyor...")
    print("Loglar (Gelen/Giden Veri Trafiği) aşağıda akacaktır:")
    # Debug=True sayesinde koda yeni bir şey eklediğimizde sunucu kendini otomatik yeniler
    app.run(debug=True, port=5000)