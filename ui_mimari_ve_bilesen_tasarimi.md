# MediAI — Web Arayüzü Mimarisi ve Bileşen Tasarımı

**Sorumlu:** Cansude Sayın
**Tarih:** 28 Nisan 2026
**Proje:** Akıllı Teşhis ve Tedavi Sistemi — Siber Şifacılar

---

## İçindekiler

1. [Genel Mimari](#1-genel-mimari)
2. [Framework Değerlendirmesi](#2-framework-değerlendirmesi)
3. [Bileşenler ve Sorumluluklar](#3-bileşenler-ve-sorumluluklar)
4. [Bileşen Diyagramı](#4-bileşen-diyagramı)
5. [Veri Akış Şeması](#5-veri-akış-şeması)
6. [Bileşenler Arası Etkileşimler](#6-bileşenler-arası-etkileşimler)

---

## 1. Genel Mimari

MediAI web arayüzü, **çok sayfalı (Multi-Page Application)** mimarisi üzerine kurulmuştur. Her sayfa bağımsız bir HTML dosyası olarak tasarlanmış, ortak `style.css` dosyası ile tutarlı görünüm sağlanmıştır.

```
┌─────────────────────────────────────────────────────┐
│                   KULLANICI (Doktor)                 │
└─────────────────────┬───────────────────────────────┘
                      │ HTTP
┌─────────────────────▼───────────────────────────────┐
│              FRONTEND (HTML/CSS/JS)                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐             │
│  │  Login   │ │Dashboard │ │ Görüntü  │  ...        │
│  │  Sayfası │ │          │ │ Analizi  │             │
│  └──────────┘ └──────────┘ └──────────┘             │
│              style.css (Ortak CSS)                   │
└─────────────────────┬───────────────────────────────┘
                      │ fetch() / AJAX
┌─────────────────────▼───────────────────────────────┐
│           BACKEND API (Flask — app.py)               │
│  POST /hastalar  │  POST /analiz  │  GET /sonuc      │
└──────┬───────────┴────────┬───────┴──────────┬───────┘
       │                    │                   │
┌──────▼──────┐    ┌────────▼──────┐   ┌───────▼──────┐
│   MySQL     │    │  Ön İşleme   │   │  CNN Modeli  │
│  Veritabanı │    │  (Selim)     │   │  (Enes)      │
└─────────────┘    └───────────────┘   └──────────────┘
```

---

## 2. Framework Değerlendirmesi

Arayüz geliştirmede kullanılabilecek framework'ler değerlendirilmiştir.

### React

| | |
|---|---|
| **Avantaj** | Bileşen tabanlı yapı, geniş ekosistem, yüksek performans |
| **Avantaj** | Sanal DOM sayesinde hızlı UI güncellemeleri |
| **Avantaj** | En yaygın kullanılan frontend kütüphanesi |
| **Dezavantaj** | Öğrenme eğrisi yüksek |
| **Dezavantaj** | Ek yapılandırma gerektirir (Webpack, Babel) |

### Angular

| | |
|---|---|
| **Avantaj** | Tam kapsamlı framework, TypeScript desteği |
| **Avantaj** | Kurumsal projeler için güçlü yapı |
| **Dezavantaj** | Öğrenmesi en zor framework |
| **Dezavantaj** | Küçük projeler için fazla karmaşık |

### Vue.js

| | |
|---|---|
| **Avantaj** | Öğrenmesi kolay, hafif yapı |
| **Avantaj** | Mevcut HTML projelerine kolayca entegre edilir |
| **Dezavantaj** | React ve Angular'a göre daha küçük ekosistem |

### Mevcut Yaklaşım: Vanilla HTML/CSS/JS

| | |
|---|---|
| **Avantaj** | Herhangi bir kurulum gerektirmez, hızlı prototipleme |
| **Avantaj** | Flask ile doğrudan entegrasyon kolaylığı |
| **Dezavantaj** | Büyük projelerde kod tekrarı artar |

### Sonuç

Projenin mevcut aşamasında **Vanilla HTML/CSS/JS** tercih edilmiştir. İlerleyen versiyonda **React** kullanımı önerilmektedir — Flask API ile sorunsuz entegre olur ve bileşen yapısı mevcut sayfalarla birebir örtüşmektedir.

---

## 3. Bileşenler ve Sorumluluklar

### 3.1. Login Bileşeni (`mediAI_login_responsive.html`)

**Sorumluluk:** Kullanıcı kimlik doğrulama

| Özellik | Detay |
|---|---|
| Girdi | E-posta, şifre, uzmanlık alanı |
| Çıktı | Oturum açma → Dashboard yönlendirme |
| API | Henüz bağlı değil (JWT planlandı) |
| Güvenlik | TLS, KVKK uyumlu |

### 3.2. Dashboard Bileşeni (`mediAI_dashboard_responsive.html`)

**Sorumluluk:** Sistem genelinde özet bilgi gösterimi

| Özellik | Detay |
|---|---|
| Girdi | API'den metrik verileri |
| Çıktı | Analiz sayısı, bekleyen teşhis, doğruluk oranı, aktif hasta |
| Alt Bileşenler | Metrik kartları, haftalık grafik, aktivite akışı, sistem durumu |
| API | `GET /api/v1/analiz/sonuc` |

### 3.3. Görüntü Analizi Bileşeni (`mediAI_image_analysis_responsive.html`)

**Sorumluluk:** Tıbbi görüntü yükleme ve AI analizi başlatma

| Özellik | Detay |
|---|---|
| Girdi | DICOM/JPG/PNG görüntü dosyası, hasta ID |
| Çıktı | Analiz başlatma bildirimi, analiz ID |
| Alt Bileşenler | DICOM viewer, araç çubuğu, dosya yükleme alanı, AI sonuç paneli |
| API | `POST /api/v1/analiz/baslat` |

### 3.4. Teşhis Sonuçları Bileşeni (`mediAI_diagnosis_responsive.html`)

**Sorumluluk:** AI teşhis sonuçlarını görüntüleme ve doktor onayı

| Özellik | Detay |
|---|---|
| Girdi | analiz_id (URL parametresi) |
| Çıktı | Teşhis, risk skoru, bulgular, doktor notu |
| Alt Bileşenler | Birincil teşhis kartı, güven metresi, bulgular listesi, ayırıcı tanı tablosu |
| API | `GET /api/v1/analiz/sonuc/<analiz_id>` (sayfa açılınca otomatik) |

### 3.5. Tedavi Planı Bileşeni (`mediAI_treatment_responsive.html`)

**Sorumluluk:** Kişiselleştirilmiş tedavi sürecini yönetme

| Özellik | Detay |
|---|---|
| Girdi | analiz_id |
| Çıktı | Tedavi adımları, ilaç listesi, randevular |
| Alt Bileşenler | Faz stepper, adım listesi, ilaç tablosu, konsültasyon ekibi |
| API | `GET /api/v1/tedavi/plan/<analiz_id>` |

### 3.6. Hasta Profili Bileşeni (`mediAI_patient_responsive.html`)

**Sorumluluk:** Hasta demografik ve klinik bilgilerini yönetme

| Özellik | Detay |
|---|---|
| Girdi | hasta_id |
| Çıktı | Demografik bilgiler, yaşamsal bulgular, lab sonuçları |
| Alt Bileşenler | Profil kartı, vital grid, görüntüleme geçmişi, lab tablosu |
| API | `GET /api/v1/hastalar/<hasta_id>`, `POST /api/v1/hastalar` |

---

## 4. Bileşen Diyagramı

```
┌─────────────────────────────────────────────────────────────┐
│                        MediAI Sistemi                        │
│                                                             │
│  ┌─────────────┐                                            │
│  │    Login    │──────────────────────────────────────────┐ │
│  │  Bileşeni  │                                          │ │
│  └─────────────┘                                          │ │
│                                                           ▼ │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  Ortak Bileşenler                    │   │
│  │  ┌──────────────┐        ┌─────────────────────┐    │   │
│  │  │   Sidebar    │        │      Topbar          │    │   │
│  │  │  Navigasyon  │        │  (Başlık + Arama)   │    │   │
│  │  └──────┬───────┘        └─────────────────────┘    │   │
│  └─────────│───────────────────────────────────────────┘   │
│            │                                               │
│    ┌───────▼────────────────────────────────────────┐      │
│    │              Sayfa Bileşenleri                  │      │
│    │                                                 │      │
│    │  ┌───────────┐  ┌───────────┐  ┌───────────┐  │      │
│    │  │ Dashboard │  │ Görüntü  │  │  Teşhis   │  │      │
│    │  │           │  │ Analizi  │  │ Sonuçları │  │      │
│    │  │ ┌───────┐ │  │ ┌───────┐│  │ ┌───────┐ │  │      │
│    │  │ │Metrik │ │  │ │DICOM  ││  │ │Teşhis │ │  │      │
│    │  │ │Kartlar│ │  │ │Viewer ││  │ │Kartı  │ │  │      │
│    │  │ └───────┘ │  │ └───────┘│  │ └───────┘ │  │      │
│    │  │ ┌───────┐ │  │ ┌───────┐│  │ ┌───────┐ │  │      │
│    │  │ │Grafik │ │  │ │Upload ││  │ │Güven  │ │  │      │
│    │  │ │       │ │  │ │Panel  ││  │ │Metresi│ │  │      │
│    │  │ └───────┘ │  │ └───────┘│  │ └───────┘ │  │      │
│    │  └───────────┘  └───────────┘  └───────────┘  │      │
│    │                                                 │      │
│    │  ┌───────────┐  ┌───────────┐                  │      │
│    │  │  Tedavi   │  │  Hasta   │                  │      │
│    │  │   Planı   │  │ Profili  │                  │      │
│    │  │ ┌───────┐ │  │ ┌───────┐│                  │      │
│    │  │ │Stepper│ │  │ │Profil ││                  │      │
│    │  │ └───────┘ │  │ │Kartı  ││                  │      │
│    │  │ ┌───────┐ │  │ └───────┘│                  │      │
│    │  │ │İlaçlar│ │  │ ┌───────┐│                  │      │
│    │  │ └───────┘ │  │ │Lab    ││                  │      │
│    │  └───────────┘  │ │Sonuç  ││                  │      │
│    │                 │ └───────┘│                  │      │
│    │                 └───────────┘                  │      │
│    └─────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Veri Akış Şeması

### 5.1. Görüntü Analizi Veri Akışı

```
Doktor
  │
  │ 1. Görüntü seçer
  ▼
Görüntü Analizi Sayfası
  │
  │ 2. fetch(POST /api/v1/analiz/baslat)
  │    {hasta_id, goruntu_turu, dosya_adi}
  ▼
Flask API (app.py)
  │
  │ 3. Görüntüyü ön işleme modülüne gönderir
  ▼
Selim'in Ön İşleme Modülü (data_preprocessing.py)
  │    - Resize: 224x224
  │    - Normalize: 0-1
  │    - Gürültü temizleme
  ▼
Enes'in CNN Modeli (ai_model.py)
  │    - model.predict(temiz_goruntu)
  │    - Risk skoru üretir
  ▼
Ali'nin MySQL Veritabanı
  │    - Diagnoses tablosuna yazar
  ▼
Flask API
  │
  │ 4. {analiz_id: 5001, durum: "İşleniyor"} döner
  ▼
Görüntü Analizi Sayfası
  │
  │ 5. Yönlendirme: Teşhis Sonuçları sayfasına geçer
  ▼
Teşhis Sonuçları Sayfası
  │
  │ 6. fetch(GET /api/v1/analiz/sonuc/5001)
  ▼
Flask API → MySQL → Sonuç
  │
  │ 7. {tehsis, risk_skoru, ai_aciklamasi} döner
  ▼
Teşhis Sonuçları Sayfası → Ekrana basılır
```

### 5.2. Hasta Kayıt Veri Akışı

```
Doktor
  │
  │ 1. "Profili Düzenle" butonuna basar
  ▼
Modal Form Açılır
  │
  │ 2. Hasta bilgilerini doldurur
  │    {yas, cinsiyet, gecmis, diyabet}
  ▼
fetch(POST /api/v1/hastalar)
  │
  ▼
Flask API — Validation
  │    - Zorunlu alanlar kontrol edilir
  │    - Yaş doğrulanır (0-150)
  │    - Cinsiyet doğrulanır
  ▼
Ali'nin MySQL Veritabanı
  │    - Patients tablosuna yazar
  ▼
Flask API
  │
  │ 3. {mesaj: "Başarılı", hasta_id: "1001"} döner
  ▼
Modal → Başarı mesajı gösterir
```

---

## 6. Bileşenler Arası Etkileşimler

| Kaynak Bileşen | Hedef Bileşen | Tetikleyici | Aktarılan Veri |
|---|---|---|---|
| Login | Dashboard | "Giriş Yap" butonu | — |
| Dashboard | Görüntü Analizi | Sidebar linki | — |
| Görüntü Analizi | Teşhis Sonuçları | "Teşhis Oluştur" butonu | analiz_id |
| Teşhis Sonuçları | Tedavi Planı | Sidebar linki | analiz_id |
| Tedavi Planı | Hasta Profili | Sidebar linki | hasta_id |
| Hasta Profili | Flask API | "Profili Düzenle" | hasta bilgileri (JSON) |
| Görüntü Analizi | Flask API | "Analiz Başlat" | goruntu + hasta_id |
| Teşhis Sonuçları | Flask API | Sayfa yüklenince | analiz_id |
