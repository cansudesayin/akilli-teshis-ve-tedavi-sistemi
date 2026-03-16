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


### 📊 2. Gereksinim Toplama ve Analizi

👤 **Sorumlu: Enes Zukra
📅 Tarih: 7 Mart 2026 

Proje kapsamında sistemin temel gereksinimleri analiz edilmiştir.

#### Fonksiyonel Gereksinimler
- Doktorların hastaya ait cilt veya göz görüntülerini sisteme yükleyebilmesi
- Yapay zeka modelinin görüntüleri analiz ederek hastalık tespiti yapması
- Sistem tarafından risk skorunun ve teşhis sonucunun gösterilmesi
- Hastaya ait temel bilgilerin sistemde saklanması

#### Kullanıcı Gereksinimleri
- Doktorların sistemi kolay kullanabilmesi
- Analiz sonuçlarının anlaşılır şekilde gösterilmesi
- Sistem performansının hızlı olması

---
**3. Teknoloji Araştırması ve Seçimi**

**Sorumlu:** Edanur Yasak
**Tarih:** 10 Mart 2026

Bu projede dermatoloji ve oftalmoloji alanlarında görüntü analizi yaparak hastalık teşhisi ve tedavi önerisi sunan bir sistem geliştirilmesi hedeflenmektedir. Bu nedenle görüntü işleme, makine öğrenimi ve veri analitiği alanlarında güçlü araçlar tercih edilmiştir.

---

# 1. Programlama Dili

## Python

Projenin ana programlama dili olarak **Python** seçilmiştir.

### Gerekçeler

* Yapay zekâ ve veri bilimi projelerinde en yaygın kullanılan dildir.
* Geniş makine öğrenimi ve görüntü işleme kütüphane desteğine sahiptir.
* Akademik projeler ve araştırmalarda standart haline gelmiştir.
* Veri analizi ve model geliştirme süreçlerini hızlandırır.

Python sayesinde veri işleme, model eğitimi ve sistem entegrasyonu tek bir dil üzerinden gerçekleştirilebilecektir.

---

# 2. Makine Öğrenimi ve Derin Öğrenme Kütüphaneleri

## TensorFlow

Projede derin öğrenme modellerinin geliştirilmesi için **TensorFlow** kullanılacaktır.

### Gerekçeler

* Büyük veri ile çalışmaya uygun ölçeklenebilir mimariye sahiptir.
* Görüntü sınıflandırma ve tıbbi görüntü analizi için güçlü araçlar sunar.
* GPU desteği sayesinde model eğitimi hızlanır.
* Endüstride ve akademide yaygın şekilde kullanılmaktadır.

---

## Keras

Model geliştirme sürecini kolaylaştırmak amacıyla **Keras** kullanılacaktır.

### Gerekçeler

* TensorFlow üzerinde çalışan yüksek seviyeli bir derin öğrenme API’sidir.
* Daha az kod ile model geliştirmeyi sağlar.
* Convolutional Neural Network (CNN) gibi mimarilerin hızlı şekilde oluşturulmasına imkan tanır.

Bu sayede dermatolojik görüntüler ve retina görüntüleri üzerinde sınıflandırma modelleri geliştirilebilecektir.

---

# 3. Görüntü İşleme Teknolojileri

## OpenCV

Tıbbi görüntülerin işlenmesi için **OpenCV** kullanılacaktır.

### Gerekçeler

* Görüntü ön işleme işlemleri için güçlü fonksiyonlar sunar.
* Gürültü azaltma, kontrast ayarlama ve görüntü kırpma işlemleri yapılabilir.
* Makine öğrenmesi modellerine daha temiz veri sağlanmasını sağlar.

Bu aşama model doğruluğunu artırmak için kritik öneme sahiptir.

---

# 4. Veri Analitiği Kütüphaneleri

## Pandas

Veri analizi için **Pandas** kullanılacaktır.

### Kullanım Alanları

* Hastalara ait demografik verilerin analizi
* CSV formatındaki veri setlerinin işlenmesi
* Görüntü meta verilerinin düzenlenmesi

---

## NumPy

Sayısal işlemler için **NumPy** kullanılacaktır.

### Gerekçeler

* Matris ve vektör işlemlerini hızlı şekilde gerçekleştirebilir.
* Makine öğrenmesi algoritmalarının temel matematik altyapısını sağlar.

---

# 5. Geliştirme Ortamı

## Visual Studio Code

Yazılım geliştirme ortamı olarak **Visual Studio Code** kullanılacaktır.

### Gerekçeler

* Python desteği güçlüdür.
* Eklenti sistemi sayesinde veri bilimi araçları kolayca entegre edilebilir.
* Hızlı ve hafif bir geliştirme ortamıdır.

---

# 6. Veritabanı Yönetim Sistemi

## MySQL

Hasta bilgileri ve meta verilerin saklanması için **MySQL** kullanılacaktır.

### Kullanım Amaçları

* Hasta demografik verilerinin saklanması
* Klinik kayıtların tutulması
* Görüntü dosyalarının veritabanındaki hasta bilgileriyle eşleştirilmesi

---

# 7. Konteyner Teknolojisi

## Docker

Uygulamanın farklı ortamlarda sorunsuz çalışması için **Docker** kullanılacaktır.

### Gerekçeler

* Geliştirme ortamının taşınabilir olmasını sağlar
* Tüm bağımlılıkların tek bir konteyner içinde çalışmasını sağlar
* Ekip üyelerinin aynı ortamda geliştirme yapmasına imkan tanır

---

# Genel Teknoloji Mimarisi

Projede kullanılacak temel teknoloji stack’i aşağıdaki gibidir:

| Katman            | Teknoloji          |
| ----------------- | ------------------ |
| Programlama dili  | Python             |
| Makine öğrenimi   | TensorFlow + Keras |
| Görüntü işleme    | OpenCV             |
| Veri analizi      | Pandas + NumPy     |
| Geliştirme ortamı | Visual Studio Code |
| Veritabanı        | MySQL              |
| Ortam yönetimi    | Docker             |

---

 **4. Geliştirme Ortamı Kurulumu**

 **Sorumlu:** Cansude Sayın 
 **Tarih:** 7 Mart 2026

Proje geliştirme sürecinde kullanılacak yazılım araçları ve kütüphaneler araştırılmış ve geliştirme ortamı kurulmuştur. Bu kapsamda aşağıdaki teknolojiler bilgisayara kurulmuş ve çalışır durumda test edilmiştir.

### Kurulan Araçlar ve Teknolojiler:

- **Python** – Projenin ana programlama dili olarak kurulmuştur.
- **TensorFlow** – Derin öğrenme modellerinin geliştirilmesi için kurulmuştur.
- **Keras** – TensorFlow tabanlı model geliştirme için kullanıma hazırlanmıştır.
- **Visual Studio Code** – Python geliştirme ortamı olarak kurulmuştur.
- **MySQL** – Hastalara ait klinik verilerin saklanacağı veritabanı sistemi kurulmuştur.
- **Docker** – Uygulamaların izole bir ortamda çalıştırılması ve geliştirme ortamının taşınabilir hale getirilmesi amacıyla kurulmuştur.

### Kurulum Sonrası Testler:

- Python ortamında TensorFlow kütüphanesi başarıyla import edilmiştir.
- MySQL veritabanı servisi çalışır durumda test edilmiştir.
- Docker servisinin çalıştığı doğrulanmıştır.
- Geliştirme ortamı proje geliştirme için hazır hale getirilmiştir.


### 5. Veri Seti Araştırması ve Erişim Planı

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
- **Enes Zukra** (Yazılım Mühendisi): [Proje için temel sistem gereksinimleri analiz edildi ve belirlendi.]
- **Edanur Yasak** (Yazılım Mühendisi): [Proje için teknoloji araştırması ve seçimi yapıldı.]
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


-------------------------------



#   Sistem Güvenlik Açığı Analizi ve Risk Değerlendirmesi

👤 **Sorumlu:** Enes Zukra
📅 **Tarih:** 16 Mart 2026

Gereksinim analizi aşamasında belirlenen sistem özellikleri (hasta verilerinin saklanması, tıbbi görüntülerin yüklenmesi ve yapay zeka analizi) doğrultusunda olası güvenlik açıkları tespit edilmiş, riskleri değerlendirilmiş ve Siber Şifacılar ekibinin sonraki adımları için bir eylem planı oluşturulmuştur.

#### 🔍 1. Olası Güvenlik Açıkları
- **Yetkisiz Erişim ve Kimlik Avı:** Doktor hesaplarının ele geçirilmesi sonucu sisteme ve hasta verilerine yetkisiz kişilerin erişimi.
- **Veri İhlali (Sızıntı):** Görüntülerin veya elektronik sağlık kayıtlarının (EHR) sisteme yüklenmesi veya veritabanında saklanması sırasında çalınması.
- **Yapay Zeka Manipülasyonu (Adversarial Attacks):** Kötü niyetli kişilerin sisteme yüklenen görüntüleri manipüle ederek modelin yanlış teşhis (örn. risk skorunun kasıtlı değiştirilmesi) yapmasına neden olması.
- **API ve Veritabanı Zafiyetleri:** Sistemin arka planında (backend) oluşabilecek SQL Injection, XSS veya API uç nokta ihlalleri.

#### ⚠️ 2. Risk Değerlendirmesi
- **Hasta Mahremiyeti İhlali (Kritik Risk):** Hassas sağlık verilerinin açığa çıkması, ciddi yasal (KVKK/GDPR ihlali) ve etik sorunlara yol açar.
- **Hatalı Teşhis ve Hasta Güvenliği (Kritik Risk):** Modelin veya veritabanındaki verilerin manipüle edilmesi, doktorun yanlış yönlendirilmesine ve hastanın zarar görmesine neden olabilir.
- **Sistem Kesintisi (Orta Risk):** Sistemin DDoS gibi saldırılarla erişilemez hale gelmesi, poliklinik operasyonlarını yavaşlatır.

#### 🛡️ 3. Eylem Planı (Risk Azaltma Stratejileri)
- **Güçlü Kimlik Doğrulama:** Doktor girişlerinde Rol Tabanlı Erişim Kontrolü (RBAC) ve İki Aşamalı Doğrulama (2FA/MFA) zorunlu kılınacaktır.
- **Uçtan Uca Şifreleme:** Veri iletiminde TLS/SSL protokolleri kullanılacak, durağan hasta verileri (EHR) AES-256 gibi güçlü algoritmalarla veritabanında şifrelenecektir.
- **Veri Anonimleştirme:** Yapay zeka modelinin eğitimi ve analizi sırasında hastaların kişisel kimlik bilgileri (PII) maskelenecek/anonimleştirilecektir.
- **Güvenlik Loglaması (Audit Trails):** Sistemde kimin, ne zaman, hangi veriye eriştiği değiştirilemez şekilde kayıt altına alınarak izlenebilirlik sağlanacaktır.
- **Girdi Doğrulama (Input Validation):** Sisteme yüklenen dosyalar ve API istekleri kötü amaçlı yazılımlara ve manipülasyonlara karşı sıkı bir taramadan geçirilecektir.

-------------------------------


