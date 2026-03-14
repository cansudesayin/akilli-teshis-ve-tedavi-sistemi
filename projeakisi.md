# Akıllı Teşhis ve Tedavi Sistemi
## Proje Akışı ve Haftalık İlerleme

Bu dosya, **Siber Şifacılar** takımının haftalık proje ilerlemesini ve görev dağılımlarını içerir.

---

## 1. Hafta (5–12 Mart)

### 🎯 Proje Tanımı ve Hedef Belirleme

#### 🏥 Cilt ve Göz Hastalıkları İçin Çok Modlu Klinik Karar Destek Sistemi

💡 Bu proje, dermatoloji ve oftalmoloji alanlarındaki tıbbi görüntüleri hastanın klinik geçmişiyle birleştirerek analiz eden yapay zeka tabanlı bir yazılım sistemidir. Sistem sadece hastalıkları sınıflandırmakla kalmaz; aynı zamanda hekimlere açıklanabilir teşhis kanıtları sunar ve hastaya özel, dinamik bir tedavi planı oluşturarak sağlık süreçlerini optimize eder.

---

### 📌 1. Projenin Kapsamı

Projenin sınırları ve içerdiği modüller şunlardır:

- 📥 **Girdi:** Yüksek çözünürlüklü tıbbi görüntüler ve hastanın EHR (Elektronik Sağlık Kayıtları — yaş, cinsiyet, kan değerleri, genetik yatkınlık vb.) verileri.
- ⚙️ **İşlem:** Derin Öğrenme ve Takviyeli Öğrenme (tedavi optimizasyonu) algoritmaları kullanılarak çok modlu veri analizi.
- 📤 **Çıktı:** Erken teşhis uyarısı, risk skorlaması, lezyon/ödem haritalaması (ısı haritaları) ve kişiselleştirilmiş tedavi takvimi/dozaj önerisi.
- ⚠️ **Sınırlandırmalar:** Sistem nihai kararı veren bir doktor değildir. Tıbbi Cihaz Yazılımı olarak hekimin karar verme sürecini hızlandıran ve doğrulayan bir asistandır.

---

### 🔬 2. Teşhisi İyileştirilecek Hastalıklar

Sistem, teşhis sürecinde insan gözünün kaçırabileceği mikro-değişimleri tespit etmeye odaklanır.

#### 🧑‍⚕️ Dermatoloji (Cilt)

- 🦠 **Malign Melanom & Bazal Hücreli Karsinom:** Dermoskopik görüntülerdeki asimetri, sınır düzensizliği, renk çeşitliliği ve çap (ABCD kuralı) özelliklerini piksel bazında analiz ederek kanserli lezyonları henüz "ben" görünümündeyken "Evre 0" aşamasında tespit eder.
- 🔴 **Psoriasis (Sedef) & Akne:** Lezyonların yayılım alanını ve şiddetini otomatik olarak hesaplayarak (PASI skoru) standart ve objektif bir şiddet derecelendirmesi yapar.

#### 👁️ Oftalmoloji (Göz)

- 🩸 **Diyabetik Retinopati (DR):** Fundus fotoğraflarındaki mikroanevrizmaları (kılcal damar kanamaları) ve eksudaları (yağ/protein birikintileri) saniyeler içinde tespit ederek hastalığın evresini (Hafif, Orta, Şiddetli, Proliferatif) belirler.
- 👀 **Yaşa Bağlı Makula Dejenerasyonu (Sarı Nokta):** OCT (Optik Koherens Tomografi) taramalarında retina katmanları arasındaki sıvı birikimini ve doku incelmesini milimetrik olarak ölçer.

---

### 🚀 3. Optimize Edilecek Tedavi Süreçleri

Projenin en yenilikçi yönü, teşhis sonrası süreçleri iyileştirmesidir.

- ⏱️ **Dinamik Tedavi Zamanlaması (Göz):** Göz hastalıklarında (DR ve YBMD) uygulanan Anti-VEGF göz içi iğnelerinin zamanlamasını optimize eder. Sistem, retina altı sıvının tekrar ne zaman birikeceğini öngörerek ("Treat-and-Extend" protokolü) hastanın 4 hafta yerine belki de 8 haftada bir iğne olmasını sağlar. Bu, hastanın konforunu artırır ve gereksiz maliyetleri önler.
- 💊 **Kişiselleştirilmiş İlaç Rotasyonu (Cilt):** Sedef veya şiddetli akne gibi kronik durumlarda sistem, hastanın yaşını ve lezyonun geçmiş görüntülere göre iyileşme hızını (zaman serisi analizi) değerlendirir. Tedaviye yanıt alınamıyorsa, biyolojik ajanların veya topikal kremlerin etken maddelerinin/dozajlarının ne zaman değiştirilmesi gerektiğini doktora önerir.
- 🔪 **Cerrahi Sınır Tahmini (Cilt Kanserleri):** Melanom teşhis edildiğinde, tümörün derinlik (Breslow kalınlığı) tahminini yaparak cerraha minimum sağlıklı doku marjını önerir. Bu, estetik kaybı ve nüks riskini aynı anda minimize eder.

---

### 🎯 4. Somut Proje Hedefleri (SMART Goals)

- 🏥 **Klinik Hedef:** Melanom ve Diyabetik Retinopati için erken teşhis doğruluğunu %95'in üzerine çıkararak klinik denemelerde uzman doktor kararlarıyla eşdeğer veya daha üstün performans göstermek.
- 📈 **Operasyonel Hedef:** Bir poliklinikte rutin görüntü inceleme ve raporlama süresini hasta başına ortalama %60 oranında azaltarak doktorların daha fazla hastaya, daha kaliteli zaman ayırmasını sağlamak.

---


### 🖼️ 5. Veri Seti Araştırması ve Erişim Planı

👤 **Sorumlu:** Ali İstanbullu
📅 **Tarih:** 6 Mart 2026

Proje kapsam belgesinde belirtilen teşhis ve tedavi optimizasyonu hedefleri doğrultusunda, model eğitiminde kullanılacak uygun veri setleri ve bu verilere erişim adımları aşağıda planlanmıştır. Sistem "Çok Modlu" (Görüntü + EHR) çalışacağı için, meta veri (yaş, cinsiyet, bölgesel analiz) içeren veri setlerine öncelik verilmiştir.

#### 🧑‍⚕️ Dermatoloji (Cilt Hastalıkları) Veri Setleri

Projedeki Malign Melanom, Bazal Hücreli Karsinom, Sedef ve Akne teşhisleri için dermoskopik ve klinik görüntüler kullanılacaktır.

**🦠 ISIC 2019 & HAM10000** (Melanom ve Karsinom için)
- 📦 **İçerik:** 25.000'den fazla dermoskopik görüntü. Hastaların yaş, cinsiyet ve lezyon bölgesi (EHR verisi) CSV formatında görsellerle eşleştirilmiştir.
- 🔓 **Durum:** Açık Kaynaklı (Kaggle / ISIC Arşivi)
- ✅ **Proje Uyumu:** ABCD kuralı analizi ve "Evre 0" tespiti hedeflerine tam uygundur.

**🔴 Dermnet** (Sedef ve Akne için)
- 📦 **İçerik:** 23 farklı cilt hastalığı kategorisinde toplanmış binlerce klinik cilt fotoğrafı.
- 🔓 **Durum:** Açık Kaynaklı (Kaggle)
- ✅ **Proje Uyumu:** Lezyon yayılım alanı ve PASI skoru hesaplamaları için kullanılacaktır.

#### 👁️ Oftalmoloji (Göz Hastalıkları) Veri Setleri

Diyabetik Retinopati için Fundus fotoğrafları, Yaşa Bağlı Makula Dejenerasyonu (YBMD) için ise OCT taramaları kullanılacaktır.

**🩸 APTOS 2019 Körlük Tespiti** (Diyabetik Retinopati)
- 📦 **İçerik:** 3.662 yüksek çözünürlüklü retina fundus fotoğrafı. Görüntüler uzmanlar tarafından 0 (Sağlıklı) ile 4 (Proliferatif DR) arasında derecelendirilmiştir.
- 🔓 **Durum:** Açık Kaynaklı (Kaggle)
- ✅ **Proje Uyumu:** Mikroanevrizma ve eksuda tespiti ile DR evrelendirmesi hedefini doğrudan karşılar.

**👀 Retinal OCT Görüntüleri — Kermany ve ark.** (YBMD / Sarı Nokta)
- 📦 **İçerik:** 84.495 Optik Koherens Tomografi (OCT) taraması.
- 🔓 **Durum:** Açık Kaynaklı (Kaggle / Mendeley Data)
- ✅ **Proje Uyumu:** Retina katmanları arasındaki sıvı birikiminin tespiti ve Anti-VEGF iğne zamanlamasının ("Treat-and-Extend") optimize edilmesi için kullanılacaktır.

#### ⚙️ Veri Erişimi ve Entegrasyon Planı

- ⬇️ **Veri Çekme:** Veri setleri çok büyük (GB'larca) olduğu için manuel indirme yapılmayacaktır. Python ortamında Kaggle API kullanılarak veriler doğrudan geliştirme sunucusuna otomatik çekilecektir.
- 🧹 **Veri Ön İşleme:** Görüntü boyutları (örn. 224×224 piksel) standardize edilecek ve gürültü azaltma (noise reduction) filtreleri uygulanacaktır.
- 🗄️ **Veritabanı (SQL) Entegrasyonu:** Hastaların EHR verileri (yaş, cinsiyet, diyabet geçmişi) ilişkisel SQL veritabanına aktarılacak; görüntülerin dosya yolları bu demografik tablolarla eşleştirilecektir.

---

### Haftalık Görev Dağılımı

- **Cansude Sayın** (Scrum Master / Yönetici): GitHub reposu oluşturuldu. Ekip üyeleri eklendi. Proje akış dokümanı oluşturuldu.
- **Selim Yağbasan** (Yazılım Mühendisi): Proje kapsamının belirlenmesi
- **Enes Zukra** (Yazılım Mühendisi): [Bu hafta yaptığı işler]
- **Edanur Yasak** (Yazılım Mühendisi): [Bu hafta yaptığı işler]
- **Ali İstanbullu** (Yazılım Mühendisi): Proje için uygun cilt ve göz hastalığı veri setleri (Kaggle üzerinden) araştırılıp erişim planı raporlandı.

---

## 2. Hafta

---

#  Sistem Güvenliği ve Risk Analizi Planı

Bu belge, **Cilt ve Göz Hastalıkları İçin Çok Modlu Klinik Karar Destek Sistemi** projesinin altyapısında, veri işleme süreçlerinde ve yapay zeka modelinde karşılaşılabilecek olası güvenlik zafiyetlerini ve bu zafiyetlerin nasıl giderileceğini tanımlar.

Proje, hassas Elektronik Sağlık Kayıtları (EHR) ve tıbbi görüntüler işlediği için **KVKK** ve **HIPAA** standartlarına tam uyum hedeflenmektedir.

---

## 1. Sistem ve Veri Risk Analizi (Zafiyet Tespiti)

Sistemin barındırdığı potansiyel tehlikeler dört ana kategoride incelenmiştir:

### A. Veri Gizliliği ve Sızıntı Riskleri
* **Zafiyet:** MySQL veritabanındaki hasta kimlik bilgilerinin (ad, TC, iletişim) ve tıbbi geçmişin şifrelenmeden tutulması ihtimali.
* **Risk (Yüksek):** Veritabanına yetkisiz erişim durumunda hastaların en mahrem sağlık verilerinin çalınması ve KVKK ihlali.

### B. Altyapı ve Ağ (Docker/Sunucu) Zafiyetleri
* **Zafiyet:** Docker container'larının varsayılan `root` yetkileriyle çalıştırılması ve dış dünyaya açık gereksiz portlar (API uç noktaları).
* **Risk (Kritik):** Kötü niyetli bir yazılımın container'dan sızarak tüm ana sunucuyu (Host) ele geçirmesi.

### C. Yapay Zeka Modeli Güvenlik Riskleri
* **Zafiyet:** Modele dışarıdan manipüle edilmiş (Adversarial Attack) noise (gürültü) içeren sahte görüntülerin yüklenmesi.
* **Risk (Orta/Yüksek):** Modelin kasıtlı olarak manipüle edilip yanlış teşhis (örn. kanserli hücreye sağlıklı raporu) vermesinin sağlanması.

### D. Erişim ve Kimlik Yönetimi Riskleri
* **Zafiyet:** Doktorların ve sistem yöneticilerinin zayıf parolalar kullanması veya sisteme girişlerde Multi-Factor Authentication (MFA) bulunmaması.
* **Risk (Yüksek):** Çalınan bir doktor hesabı üzerinden sisteme sahte veri girilmesi veya hasta verilerinin dışarı sızdırılması.

---

## 2. Güvenlik Planı ve Zafiyet Giderme Stratejileri

Risk analizindeki bulguları bertaraf etmek için uygulanacak teknik ve operasyonel adımlar şunlardır:

###  Veri Güvenliği (KVKK/HIPAA Uyumluluğu)
* **Pseudonymization:** Görüntü ve EHR verileri model eğitimine veya analize girmeden önce hasta kimliklerinden (PII - Personally Identifiable Information) arındırılacaktır.
* **Encryption (Şifreleme):** * *Data at Rest:* MySQL veritabanındaki veriler AES-256 standardı ile şifrelenecektir.
  * *Data in Transit:* Sistem içi ve dışı tüm iletişim (Frontend - Backend - Veritabanı) TLS 1.3 / HTTPS protokolleri üzerinden yapılacaktır.

###  Altyapı ve Uygulama Güvenliği
* **Container İzolasyonu:** Docker container'ları kesinlikle `root` yetkisiyle çalıştırılmayacak, "Least Privilege" prensibi uygulanacaktır.
* **Network Segmentation (VPC):** Veritabanı (MySQL) internete tamamen kapalı bir özel ağda (Private Subnet) tutulacak, sadece uygulamanın çalıştığı Backend sunucusu ile iletişim kurabilecektir.
* **Vulnerability Scanning:** Python kütüphanelerindeki bilinen zafiyetler (CVE) düzenli olarak taranacaktır.

###  Kimlik ve Erişim Yönetimi (IAM)
* **Role-Based Access Control (RBAC):** Sistemde "Super Admin", "Uzman Doktor", "Asistan" gibi net rol ayrımları yapılacaktır.
* **Multi-Factor Authentication (MFA):** Sisteme giriş yapacak tüm sağlık personeli için SMS veya Authenticator uygulaması zorunlu tutulacaktır.

---

## 3. Zaman Çizelgesi ve Sorumluluklar


| Faz | Uygulanacak Güvenlik Önlemi | Sorumlu Kişi | Hedef Süre |
| :--- | :--- | :--- | :--- |
| **Faz 1** | Veritabanı şifrelemesi (AES-256) ve HTTPS (SSL/TLS) sertifikalarının kurulması. | **Cansude Sayın** & **Ali İstanbullu** | 1. - 2. Hafta |
| **Faz 1** | Multi-Factor Authentication (MFA) ve Role-Based Access Control (RBAC) kodlaması. | **Enes Zukra** | 2. - 3. Hafta |
| **Faz 2** | Docker container güvenlik sıkılaştırması (Least Privilege) ve Network Segmentation. | **Cansude Sayın** | 3. Hafta |
| **Faz 2** | Veri setlerindeki (görüntü/EHR) kişisel bilgilerin analize girmeden önce Pseudonymization işlemi. | **Ali İstanbullu** | 4. Hafta |
| **Faz 3** | Yapay zeka modeline gelen girdilerin doğrulanması ve Adversarial Attack savunması. | **Edanur Yasak** | 5. Hafta |
| **Faz 4** | Tüm sistemin Penetration Test (PenTest) sürecinden geçirilmesi ve KVKK raporunun hazırlanması. | **Tüm Ekip** | 6. Hafta |

