# Akıllı Teşhis ve Tedavi Sistemi - API Tasarımı ve Endpoint Raporu
**Sorumlu:** Ali İstanbullu
**Tarih:** 22 Mart 2026
**Faz:** 3. Hafta - Sistem Tasarımı

Bu doküman, Siber Şifacılar projesinin Frontend (Doktor Web Arayüzü) ile Backend (Yapay Zeka Modeli ve Veritabanı) arasındaki veri iletişimini sağlayacak olan API uç noktalarını (Endpoint'leri) tanımlar. Sistem RESTful mimari standartlarına göre tasarlanmıştır.

**Temel URL (Base URL):** `https://api.sibersifacilar.com/v1`

---

## 1. Hasta ve EHR (Elektronik Sağlık Kayıtları) Yönetimi

Bu kapılar, Edanur'un kuracağı veritabanındaki hasta bilgilerini yönetmek için kullanılacaktır.

### 1.1. Yeni Hasta Kaydı
* **Endpoint:** `POST /api/hastalar`
* **Ne İş Yapar:** Doktorun sisteme yeni bir hasta (EHR verileriyle birlikte) eklemesini sağlar.
* **Cansude'nin (Frontend) Göndereceği Veri (Request):**
  ```json
  {
    "ad_soyad": "Ahmet Yılmaz",
    "yas": 45,
    "cinsiyet": "Erkek",
    "genetik_yatkinlik": true,
    "kan_degerleri": {"hba1c": 6.5, "seker": 110}
  }

  Sistemin Vereceği Cevap (Response): 201 Created (Başarılı) ve oluşturulan hastanın ID'si.

1.2. Hasta Geçmişini Görüntüleme
Endpoint: GET /api/hastalar/{hasta_id}

Ne İş Yapar: Spesifik bir hastanın geçmiş analizlerini, reçetelerini ve demografik bilgilerini getirir.

2. Yapay Zeka (AI) Görüntü Analizi ve Teşhis
Sistemin kalbi olan yapay zeka entegrasyonu bu kapılar üzerinden sağlanacaktır.

2.1. Cilt veya Göz Görüntüsü Yükleme ve Analiz Başlatma
Endpoint: POST /api/analiz/baslat

Ne İş Yapar: Doktorun yüklediği fotoğrafı (Dermoskopik, Fundus veya OCT) ve hasta ID'sini alarak Python/TensorFlow modeline analiz etmesi için gönderir.

Cansude'nin (Frontend) Göndereceği Veri (Request):

JSON
{
  "hasta_id": "1001",
  "goruntu_turu": "OCT", 
  "goruntu_dosyasi": "(Base64 Formatında Görsel Verisi veya Multipart File)"
}
Sistemin Vereceği Cevap (Response): 202 Accepted (Analiz başladı, işleniyor...)

2.2. Teşhis Sonucunu Alma (Klinik Karar Destek)
Endpoint: GET /api/analiz/sonuc/{analiz_id}

Ne İş Yapar: Yapay zeka modelinin görüntü üzerinde yaptığı teşhisi, risk skorunu ve ısı haritasını (lezyon bölgesini) UI'a döndürür.

Sistemin Vereceği Cevap (Response):

JSON
{
  "analiz_id": "5005",
  "tehsis": "Diyabetik Retinopati",
  "evre": "Orta",
  "risk_skoru": 85.4,
  "isi_haritasi_url": "/medya/analiz/heatmap_5005.png",
  "ai_aciklamasi": "Retina alt bölgede 3 adet mikroanevrizma tespit edilmiştir."
}

Gemini şunu dedi:
Harika! Yepyeni ve tertemiz odandasın. Sol üstte dal seçici butonda ali-api-tasarimi yazdığını görebiliyorum. İlk adımı başarıyla geçtik!

Şimdi asıl görevimiz olan API raporunu oluşturup bu odaya kaydetme adımına geçiyoruz. Lütfen şu adımları sırasıyla yap:

Ekranda, dosyaların hemen üstünde sağa doğru duran "Add file" butonuna tıkla ve açılan menüden "Create new file" (Yeni dosya oluştur) seçeneğini seç.

Karşına çıkan ekranda en üstte dosya adını yazacağın yere tam olarak şunu yaz: api_tasarim_raporu.md

Hemen altındaki kocaman boşluğa (Edit new file), senin için hazırladığım aşağıdaki metnin tamamını kopyalayıp yapıştır:

Markdown
# Akıllı Teşhis ve Tedavi Sistemi - API Tasarımı ve Endpoint Raporu
**Sorumlu:** Ali İstanbullu
**Tarih:** 22 Mart 2026
**Faz:** 3. Hafta - Sistem Tasarımı

Bu doküman, Siber Şifacılar projesinin Frontend (Doktor Web Arayüzü) ile Backend (Yapay Zeka Modeli ve Veritabanı) arasındaki veri iletişimini sağlayacak olan API uç noktalarını (Endpoint'leri) tanımlar. Sistem RESTful mimari standartlarına göre tasarlanmıştır.

**Temel URL (Base URL):** `https://api.sibersifacilar.com/v1`

---

## 1. Hasta ve EHR (Elektronik Sağlık Kayıtları) Yönetimi

Bu kapılar, Edanur'un kuracağı veritabanındaki hasta bilgilerini yönetmek için kullanılacaktır.

### 1.1. Yeni Hasta Kaydı
* **Endpoint:** `POST /api/hastalar`
* **Ne İş Yapar:** Doktorun sisteme yeni bir hasta (EHR verileriyle birlikte) eklemesini sağlar.
* **Cansude'nin (Frontend) Göndereceği Veri (Request):**
  ```json
  {
    "ad_soyad": "Ahmet Yılmaz",
    "yas": 45,
    "cinsiyet": "Erkek",
    "genetik_yatkinlik": true,
    "kan_degerleri": {"hba1c": 6.5, "seker": 110}
  }
Sistemin Vereceği Cevap (Response): 201 Created (Başarılı) ve oluşturulan hastanın ID'si.

1.2. Hasta Geçmişini Görüntüleme
Endpoint: GET /api/hastalar/{hasta_id}

Ne İş Yapar: Spesifik bir hastanın geçmiş analizlerini, reçetelerini ve demografik bilgilerini getirir.

2. Yapay Zeka (AI) Görüntü Analizi ve Teşhis
Sistemin kalbi olan yapay zeka entegrasyonu bu kapılar üzerinden sağlanacaktır.

2.1. Cilt veya Göz Görüntüsü Yükleme ve Analiz Başlatma
Endpoint: POST /api/analiz/baslat

Ne İş Yapar: Doktorun yüklediği fotoğrafı (Dermoskopik, Fundus veya OCT) ve hasta ID'sini alarak Python/TensorFlow modeline analiz etmesi için gönderir.

Cansude'nin (Frontend) Göndereceği Veri (Request):

JSON
{
  "hasta_id": "1001",
  "goruntu_turu": "OCT", 
  "goruntu_dosyasi": "(Base64 Formatında Görsel Verisi veya Multipart File)"
}
Sistemin Vereceği Cevap (Response): 202 Accepted (Analiz başladı, işleniyor...)

2.2. Teşhis Sonucunu Alma (Klinik Karar Destek)
Endpoint: GET /api/analiz/sonuc/{analiz_id}

Ne İş Yapar: Yapay zeka modelinin görüntü üzerinde yaptığı teşhisi, risk skorunu ve ısı haritasını (lezyon bölgesini) UI'a döndürür.

Sistemin Vereceği Cevap (Response):

JSON
{
  "analiz_id": "5005",
  "tehsis": "Diyabetik Retinopati",
  "evre": "Orta",
  "risk_skoru": 85.4,
  "isi_haritasi_url": "/medya/analiz/heatmap_5005.png",
  "ai_aciklamasi": "Retina alt bölgede 3 adet mikroanevrizma tespit edilmiştir."
}
3. Dinamik Tedavi ve Optimizasyon
Projenin yenilikçi "tedavi planlama" kısmını yönetecek uç noktalardır.

3.1. Kişiselleştirilmiş Tedavi Önerisi Alma
Endpoint: GET /api/tedavi/plan/{analiz_id}

Ne İş Yapar: Yapılan son analize göre sisteme entegre algoritmaların doktora dinamik bir tedavi planı (Örn: İlaç rotasyonu veya iğne zamanlaması) sunmasını sağlar.

Sistemin Vereceği Cevap (Response):

JSON
{
  "onerilen_tedavi": "Anti-VEGF Enjeksiyonu",
  "zamanlama_protokolu": "Treat-and-Extend",
  "sonraki_randevu_hedefi": "8 Hafta Sonra",
  "alternatif_ilaclar": ["İlaç A", "İlaç B"]
}
