# MediAI — API Teknik Dokümantasyonu

**Sorumlu:** Cansude Sayın
**Tarih:** 6 Nisan 2026
**Proje:** Akıllı Teşhis ve Tedavi Sistemi — Siber Şifacılar

---

## İçindekiler

1. [Genel Bilgiler](#1-genel-bilgiler)
2. [Kurulum ve Çalıştırma](#2-kurulum-ve-çalıştırma)
3. [Endpoint Referansı](#3-endpoint-referansı)
4. [Hata Kodları](#4-hata-kodları)
5. [Entegrasyon Kontrol Listesi](#5-entegrasyon-kontrol-listesi)

---

## 1. Genel Bilgiler

Bu API, MediAI sisteminin Frontend (HTML arayüzleri) ile Backend (veritabanı ve yapay zeka modeli) arasındaki veri iletişimini sağlar.

| Özellik | Değer |
|---|---|
| Framework | Python Flask |
| Mimari | RESTful |
| Yerel Adres | `http://localhost:5000` |
| Veri Formatı | JSON |
| Port | 5000 |
| CORS | Aktif (geliştirme modunda) |

---

## 2. Kurulum ve Çalıştırma

#### Gerekli Kütüphaneler

```bash
pip install flask flask-cors
```

#### Sunucuyu Başlatma

```bash
python app.py
```

Sunucu başarıyla çalışınca terminalde şu çıktı görünür:

```
============================================================
  Siber Şifacılar — MediAI API Sunucusu Başlatılıyor...
============================================================
  Adres : http://localhost:5000
  Mod   : Geliştirme (Debug)
============================================================
```

#### Test Etme

Sunucu çalışırken tarayıcıya şunu yaz:

```
http://localhost:5000/api/v1/analiz/sonuc/5001
```

Başarılı yanıt geliyorsa API çalışıyor demektir.

---

## 3. Endpoint Referansı

### 3.1. Yeni Hasta Kaydı

```
POST /api/v1/hastalar
```

**Ne İş Yapar:** Doktorun arayüzden girdiği hasta bilgilerini alır ve sisteme kaydeder.

**Gönderilecek Veri (Request Body):**

```json
{
  "yas": 45,
  "cinsiyet": "Erkek",
  "gecmis": "Hipertansiyon, Tip 2 Diyabet",
  "diyabet": true
}
```

| Alan | Tür | Zorunlu | Açıklama |
|---|---|---|---|
| `yas` | integer | Evet | 0–150 arası |
| `cinsiyet` | string | Evet | "Erkek" veya "Kadın" |
| `gecmis` | string | Hayır | Geçmiş hastalıklar |
| `diyabet` | boolean | Hayır | Diyabet durumu |

**Başarılı Yanıt (201 Created):**

```json
{
  "hata": false,
  "mesaj": "Hasta başarıyla sisteme kaydedildi.",
  "hasta_id": "1001",
  "zaman": "2026-04-06T10:30:00"
}
```

**Frontend Entegrasyonu:** Hasta Profili sayfasındaki "Profili Düzenle" modalından tetiklenir.

---

### 3.2. Hasta Bilgisi Görüntüleme

```
GET /api/v1/hastalar/<hasta_id>
```

**Ne İş Yapar:** Belirtilen ID'ye ait hastanın tüm bilgilerini döndürür.

**Örnek İstek:**

```
GET /api/v1/hastalar/1001
```

**Başarılı Yanıt (200 OK):**

```json
{
  "hata": false,
  "hasta_id": 1001,
  "yas": 48,
  "cinsiyet": "Erkek",
  "gecmis": "Hipertansiyon, Tip 2 Diyabet",
  "diyabet": true,
  "kan_grubu": "A Rh+",
  "kayit_tarihi": "2026-01-03",
  "zaman": "2026-04-06T10:30:00"
}
```

---

### 3.3. Görüntü Analizi Başlatma

```
POST /api/v1/analiz/baslat
```

**Ne İş Yapar:** Doktorun yüklediği tıbbi görüntüyü alır ve yapay zeka analizini başlatır.

**Gönderilecek Veri (Request Body):**

```json
{
  "hasta_id": "1001",
  "goruntu_turu": "dermoskopi",
  "dosya_adi": "cilt_lesyon.jpg"
}
```

| Alan | Tür | Zorunlu | Kabul Edilen Değerler |
|---|---|---|---|
| `hasta_id` | string | Evet | Sistemdeki geçerli hasta ID |
| `goruntu_turu` | string | Evet | dermoskopi, fundus, oct, xray, ct, mri |
| `dosya_adi` | string | Hayır | Yüklenen dosyanın adı |

**Başarılı Yanıt (202 Accepted):**

```json
{
  "hata": false,
  "mesaj": "1001 numaralı hasta için yapay zeka analizi başlatıldı.",
  "analiz_durumu": "İşleniyor",
  "analiz_id": 5001,
  "zaman": "2026-04-06T10:31:00"
}
```

**Frontend Entegrasyonu:** Görüntü Analizi sayfasındaki "Yapay Zeka Analizini Başlat" butonundan tetiklenir.

---

### 3.4. Teşhis Sonucunu Görüntüleme

```
GET /api/v1/analiz/sonuc/<analiz_id>
```

**Ne İş Yapar:** Yapay zeka modelinin ürettiği teşhis sonucunu, risk skorunu ve açıklamayı döndürür.

**Örnek İstek:**

```
GET /api/v1/analiz/sonuc/5001
```

**Başarılı Yanıt (200 OK):**

```json
{
  "hata": false,
  "analiz_id": 5001,
  "hasta_id": 1001,
  "tehsis": "Malign Melanom (Cilt Kanseri)",
  "evre": "Evre 1",
  "risk_skoru": 88.5,
  "ai_aciklamasi": "Lezyon sınırlarında asimetri tespit edildi. Biyopsi önerilir.",
  "isi_haritasi_url": "/medya/analiz/heatmap_5001.png",
  "analiz_tarihi": "2026-04-06T10:32:00",
  "zaman": "2026-04-06T10:32:00"
}
```

**Frontend Entegrasyonu:** Teşhis Sonuçları sayfası açıldığında otomatik olarak çağrılır.

---

### 3.5. Tedavi Planı

```
GET /api/v1/tedavi/plan/<analiz_id>
```

**Ne İş Yapar:** Yapılan analize göre kişiselleştirilmiş tedavi önerisini döndürür.

**Örnek İstek:**

```
GET /api/v1/tedavi/plan/5001
```

**Başarılı Yanıt (200 OK):**

```json
{
  "hata": false,
  "analiz_id": 5001,
  "onerilen_tedavi": "Geniş Eksizyon (Cerrahi Çıkarma)",
  "zamanlama_protokolu": "Acil — 2 hafta içinde",
  "sonraki_randevu_hedefi": "2 Hafta Sonra",
  "alternatif_tedaviler": ["Mohs Cerrahisi", "İmmünoterapi"],
  "notlar": "Sentinel lenf nodu biyopsisi değerlendirilmelidir.",
  "zaman": "2026-04-06T10:33:00"
}
```

---

## 4. Hata Kodları

| HTTP Kodu | Anlamı | Örnek Durum |
|---|---|---|
| `200 OK` | Başarılı | Veri başarıyla getirildi |
| `201 Created` | Oluşturuldu | Hasta kaydı başarıyla oluşturuldu |
| `202 Accepted` | İşleme Alındı | Analiz kuyruğa eklendi |
| `400 Bad Request` | Hatalı İstek | Eksik veya geçersiz alan |
| `404 Not Found` | Bulunamadı | Geçersiz endpoint |
| `405 Method Not Allowed` | Yanlış Metod | GET yerine POST gönderildi |
| `415 Unsupported Media Type` | Yanlış Format | JSON yerine form verisi gönderildi |
| `500 Internal Server Error` | Sunucu Hatası | Beklenmeyen bir hata |

**Hata Yanıtı Örneği:**

```json
{
  "hata": true,
  "mesaj": "Eksik zorunlu alanlar: yas, cinsiyet",
  "zaman": "2026-04-06T10:30:00"
}
```

---

## 5. Entegrasyon Kontrol Listesi

Aşağıdaki kontroller yapılmış ve doğrulanmıştır:

#### Frontend — API Bağlantıları

- [x] Hasta Profili sayfası → `POST /api/v1/hastalar` bağlantısı kuruldu
- [x] Görüntü Analizi sayfası → `POST /api/v1/analiz/baslat` bağlantısı kuruldu
- [x] Teşhis Sonuçları sayfası → `GET /api/v1/analiz/sonuc` otomatik çağrısı kuruldu
- [x] Demo Mod — Flask sunucusu kapalıyken sayfalar sahte veriyle çalışmaya devam ediyor

#### API — Eksik Giderme

- [x] CORS desteği eklendi (HTML sayfaları API'ye istek atabilir)
- [x] Gelen veri doğrulama (validation) eklendi
- [x] Hata yönetimi (try/except, standart hata yanıtları) eklendi
- [x] Standart yanıt formatı oluşturuldu (`hata`, `mesaj`, `zaman` alanları)
- [x] 5. endpoint eklendi: `GET /api/v1/tedavi/plan/<analiz_id>`
- [x] `GET /api/v1/hastalar/<hasta_id>` endpoint'i eklendi

#### Bekleyen Entegrasyonlar (İlerleyen Haftalar)

- [ ] MySQL veritabanı bağlantısı — `Ali İstanbullu` (5. Hafta görevi)
- [ ] Görüntü ön işleme modülü entegrasyonu — `Selim Yağbasan` (5. ve 6. Hafta görevi)
- [ ] CNN model entegrasyonu (`model.predict()`) — `Enes Zukra` (5. ve 6. Hafta görevi)
- [ ] Gerçek görüntü dosyası yükleme (multipart/form-data)
- [ ] JWT ile kimlik doğrulama (token bazlı güvenlik)

---

## 6. Dokümantasyon Aracı Seçimi

### Değerlendirilen Araçlar

#### Swagger (OpenAPI)

| | |
|---|---|
| **Avantaj** | Otomatik interaktif arayüz oluşturur, kod yorumlarından dokümantasyon üretir, geniş ekosistem |
| **Avantaj** | Flask ile `flask-swagger-ui` kütüphanesi üzerinden kolayca entegre edilir |
| **Avantaj** | Endpoint'leri tarayıcıdan test etmeye olanak tanır |
| **Dezavantaj** | Kurulum ve yapılandırma zaman alır |
| **Dezavantaj** | YAML/JSON şema yazımı karmaşık olabilir |

#### Postman

| | |
|---|---|
| **Avantaj** | Kullanımı kolay, görsel arayüz |
| **Avantaj** | Koleksiyon paylaşımı ile ekip içi test kolaylaşır |
| **Avantaj** | Otomatik test senaryoları yazılabilir |
| **Dezavantaj** | Ücretsiz sürümde takım özellikleri kısıtlı |
| **Dezavantaj** | Kod tabanıyla senkronizasyon manuel yapılmalı |

#### Redoc

| | |
|---|---|
| **Avantaj** | Şık ve okunabilir dokümantasyon sayfası üretir |
| **Avantaj** | OpenAPI şemasından otomatik render eder |
| **Dezavantaj** | Interaktif test özelliği yoktur |

### Seçilen Araç: Swagger (OpenAPI) + Postman

Proje için **ikili yaklaşım** benimsenmiştir:

- **Swagger** → Resmi teknik dokümantasyon ve endpoint referansı için
- **Postman** → Ekip içi test ve geliştirme aşamasında hızlı doğrulama için

---

## 7. Dokümantasyonu Güncel Tutma ve Sürüm Kontrolü

#### Sürüm Numaralandırma

API sürümleri URL üzerinden yönetilmektedir:

```
/api/v1/hastalar   → Mevcut sürüm
/api/v2/hastalar   → İlerleyen sürüm (geriye dönük uyumluluk korunur)
```

#### Güncelleme Kuralları

- Yeni endpoint eklendiğinde `api_teknik_dokumantasyon.md` aynı commit içinde güncellenir
- Her endpoint değişikliği Pull Request açıklamasında belirtilir
- Kırıcı değişiklikler (breaking changes) yeni sürüm numarasıyla yayınlanır

#### Sürüm Geçmişi

| Sürüm | Tarih | Değişiklik |
|---|---|---|
| v1.0 | 6 Nisan 2026 | İlk 3 endpoint (hasta kayıt, analiz başlat, sonuç getir) |
| v1.1 | 25 Nisan 2026 | CORS, validation, 2 yeni endpoint, hata yönetimi eklendi |

---

## 8. Dokümantasyon Otomatikleştirme Stratejisi

#### Flask-Swagger Entegrasyonu

`app.py` içindeki her endpoint'e OpenAPI şema yorumları eklenerek Swagger dokümantasyonu otomatik üretilir:

```python
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
```

Sunucu çalıştığında `http://localhost:5000/api/docs` adresinden interaktif dokümantasyona erişilir.

#### Otomatik Güncelleme Akışı

```
Kod değişikliği
      ↓
app.py'e yorum satırı eklenir
      ↓
swagger.json otomatik güncellenir
      ↓
Pull Request açılır
      ↓
api_teknik_dokumantasyon.md güncellenir
      ↓
Main branch'e merge edilir
```

#### Postman Koleksiyonu

Tüm endpoint'ler Postman koleksiyonu olarak `mediAI_api.postman_collection.json` dosyasına aktarılmış ve repoya eklenmiştir. Ekip üyeleri bu dosyayı Postman'e import ederek tüm endpoint'leri hazır test ortamıyla kullanabilir.

