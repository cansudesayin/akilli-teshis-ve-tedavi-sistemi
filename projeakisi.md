# Akıllı Teşhis ve Tedavi Sistemi
## Proje Akışı ve Haftalık İlerleme

Bu dosya, **Siber Şifacılar** takımının haftalık proje ilerlemesini ve görev dağılımlarını içerir.

---

## 1. Hafta (5–12 Mart)

###  Proje Tanımı ve Hedef Belirleme

####  Cilt ve Göz Hastalıkları İçin Çok Modlu Klinik Karar Destek Sistemi

 Bu proje, dermatoloji ve oftalmoloji alanlarındaki tıbbi görüntüleri hastanın klinik geçmişiyle birleştirerek analiz eden yapay zeka tabanlı bir yazılım sistemidir. Sistem sadece hastalıkları sınıflandırmakla kalmaz; aynı zamanda hekimlere açıklanabilir teşhis kanıtları sunar ve hastaya özel, dinamik bir tedavi planı oluşturarak sağlık süreçlerini optimize eder.

---

###  1. Projenin Kapsamı

Projenin sınırları ve içerdiği modüller şunlardır:

-  **Girdi:** Yüksek çözünürlüklü tıbbi görüntüler ve hastanın EHR (Elektronik Sağlık Kayıtları — yaş, cinsiyet, kan değerleri, genetik yatkınlık vb.) verileri.
-  **İşlem:** Derin Öğrenme ve Takviyeli Öğrenme (tedavi optimizasyonu) algoritmaları kullanılarak çok modlu veri analizi.
-  **Çıktı:** Erken teşhis uyarısı, risk skorlaması, lezyon/ödem haritalaması (ısı haritaları) ve kişiselleştirilmiş tedavi takvimi/dozaj önerisi.
-  **Sınırlandırmalar:** Sistem nihai kararı veren bir doktor değildir. Tıbbi Cihaz Yazılımı olarak hekimin karar verme sürecini hızlandıran ve doğrulayan bir asistandır.

---

###  2. Teşhisi İyileştirilecek Hastalıklar

Sistem, teşhis sürecinde insan gözünün kaçırabileceği mikro-değişimleri tespit etmeye odaklanır.

####  Dermatoloji (Cilt)

-  **Malign Melanom & Bazal Hücreli Karsinom:** Dermoskopik görüntülerdeki asimetri, sınır düzensizliği, renk çeşitliliği ve çap (ABCD kuralı) özelliklerini piksel bazında analiz ederek kanserli lezyonları henüz "ben" görünümündeyken "Evre 0" aşamasında tespit eder.
-  **Psoriasis (Sedef) & Akne:** Lezyonların yayılım alanını ve şiddetini otomatik olarak hesaplayarak (PASI skoru) standart ve objektif bir şiddet derecelendirmesi yapar.

####  Oftalmoloji (Göz)

-  **Diyabetik Retinopati (DR):** Fundus fotoğraflarındaki mikroanevrizmaları (kılcal damar kanamaları) ve eksudaları (yağ/protein birikintileri) saniyeler içinde tespit ederek hastalığın evresini (Hafif, Orta, Şiddetli, Proliferatif) belirler.
-  **Yaşa Bağlı Makula Dejenerasyonu (Sarı Nokta):** OCT (Optik Koherens Tomografi) taramalarında retina katmanları arasındaki sıvı birikimini ve doku incelmesini milimetrik olarak ölçer.

---

###  3. Optimize Edilecek Tedavi Süreçleri

Projenin en yenilikçi yönü, teşhis sonrası süreçleri iyileştirmesidir.

-  **Dinamik Tedavi Zamanlaması (Göz):** Göz hastalıklarında (DR ve YBMD) uygulanan Anti-VEGF göz içi iğnelerinin zamanlamasını optimize eder. Sistem, retina altı sıvının tekrar ne zaman birikeceğini öngörerek ("Treat-and-Extend" protokolü) hastanın 4 hafta yerine belki de 8 haftada bir iğne olmasını sağlar. Bu, hastanın konforunu artırır ve gereksiz maliyetleri önler.
-  **Kişiselleştirilmiş İlaç Rotasyonu (Cilt):** Sedef veya şiddetli akne gibi kronik durumlarda sistem, hastanın yaşını ve lezyonun geçmiş görüntülere göre iyileşme hızını (zaman serisi analizi) değerlendirir. Tedaviye yanıt alınamıyorsa, biyolojik ajanların veya topikal kremlerin etken maddelerinin/dozajlarının ne zaman değiştirilmesi gerektiğini doktora önerir.
-  **Cerrahi Sınır Tahmini (Cilt Kanserleri):** Melanom teşhis edildiğinde, tümörün derinlik (Breslow kalınlığı) tahminini yaparak cerraha minimum sağlıklı doku marjını önerir. Bu, estetik kaybı ve nüks riskini aynı anda minimize eder.

---

###  4. Somut Proje Hedefleri (SMART Goals)

-  **Klinik Hedef:** Melanom ve Diyabetik Retinopati için erken teşhis doğruluğunu %95'in üzerine çıkararak klinik denemelerde uzman doktor kararlarıyla eşdeğer veya daha üstün performans göstermek.
-  **Operasyonel Hedef:** Bir poliklinikte rutin görüntü inceleme ve raporlama süresini hasta başına ortalama %60 oranında azaltarak doktorların daha fazla hastaya, daha kaliteli zaman ayırmasını sağlamak.

---


###  2. Gereksinim Toplama ve Analizi

 **Sorumlu: Enes Zukra
 Tarih: 7 Mart 2026 

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

 **Sorumlu:** Ali İstanbullu
 **Tarih:** 6 Mart 2026

Proje kapsam belgesinde belirtilen teşhis ve tedavi optimizasyonu hedefleri doğrultusunda, model eğitiminde kullanılacak uygun veri setleri ve bu verilere erişim adımları aşağıda planlanmıştır. Sistem "Çok Modlu" (Görüntü + EHR) çalışacağı için, meta veri (yaş, cinsiyet, bölgesel analiz) içeren veri setlerine öncelik verilmiştir.

####  Dermatoloji (Cilt Hastalıkları) Veri Setleri

Projedeki Malign Melanom, Bazal Hücreli Karsinom, Sedef ve Akne teşhisleri için dermoskopik ve klinik görüntüler kullanılacaktır.

** ISIC 2019 & HAM10000** (Melanom ve Karsinom için)
-  **İçerik:** 25.000'den fazla dermoskopik görüntü. Hastaların yaş, cinsiyet ve lezyon bölgesi (EHR verisi) CSV formatında görsellerle eşleştirilmiştir.
-  **Durum:** Açık Kaynaklı (Kaggle / ISIC Arşivi)
-  **Proje Uyumu:** ABCD kuralı analizi ve "Evre 0" tespiti hedeflerine tam uygundur.

** Dermnet** (Sedef ve Akne için)
-  **İçerik:** 23 farklı cilt hastalığı kategorisinde toplanmış binlerce klinik cilt fotoğrafı.
-  **Durum:** Açık Kaynaklı (Kaggle)
-  **Proje Uyumu:** Lezyon yayılım alanı ve PASI skoru hesaplamaları için kullanılacaktır.

####  Oftalmoloji (Göz Hastalıkları) Veri Setleri

Diyabetik Retinopati için Fundus fotoğrafları, Yaşa Bağlı Makula Dejenerasyonu (YBMD) için ise OCT taramaları kullanılacaktır.

** APTOS 2019 Körlük Tespiti** (Diyabetik Retinopati)
-  **İçerik:** 3.662 yüksek çözünürlüklü retina fundus fotoğrafı. Görüntüler uzmanlar tarafından 0 (Sağlıklı) ile 4 (Proliferatif DR) arasında derecelendirilmiştir.
-  **Durum:** Açık Kaynaklı (Kaggle)
-  **Proje Uyumu:** Mikroanevrizma ve eksuda tespiti ile DR evrelendirmesi hedefini doğrudan karşılar.

** Retinal OCT Görüntüleri — Kermany ve ark.** (YBMD / Sarı Nokta)
-  **İçerik:** 84.495 Optik Koherens Tomografi (OCT) taraması.
-  **Durum:** Açık Kaynaklı (Kaggle / Mendeley Data)
-  **Proje Uyumu:** Retina katmanları arasındaki sıvı birikiminin tespiti ve Anti-VEGF iğne zamanlamasının ("Treat-and-Extend") optimize edilmesi için kullanılacaktır.

####  Veri Erişimi ve Entegrasyon Planı

- ⬇️ **Veri Çekme:** Veri setleri çok büyük (GB'larca) olduğu için manuel indirme yapılmayacaktır. Python ortamında Kaggle API kullanılarak veriler doğrudan geliştirme sunucusuna otomatik çekilecektir.
-  **Veri Ön İşleme:** Görüntü boyutları (örn. 224×224 piksel) standardize edilecek ve gürültü azaltma (noise reduction) filtreleri uygulanacaktır.
-  **Veritabanı (SQL) Entegrasyonu:** Hastaların EHR verileri (yaş, cinsiyet, diyabet geçmişi) ilişkisel SQL veritabanına aktarılacak; görüntülerin dosya yolları bu demografik tablolarla eşleştirilecektir.

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

 **Sorumlu:** Enes Zukra
 **Tarih:** 16 Mart 2026

Gereksinim analizi aşamasında belirlenen sistem özellikleri (hasta verilerinin saklanması, tıbbi görüntülerin yüklenmesi ve yapay zeka analizi) doğrultusunda olası güvenlik açıkları tespit edilmiş, riskleri değerlendirilmiş ve Siber Şifacılar ekibinin sonraki adımları için bir eylem planı oluşturulmuştur.

####  1. Olası Güvenlik Açıkları
- **Yetkisiz Erişim ve Kimlik Avı:** Doktor hesaplarının ele geçirilmesi sonucu sisteme ve hasta verilerine yetkisiz kişilerin erişimi.
- **Veri İhlali (Sızıntı):** Görüntülerin veya elektronik sağlık kayıtlarının (EHR) sisteme yüklenmesi veya veritabanında saklanması sırasında çalınması.
- **Yapay Zeka Manipülasyonu (Adversarial Attacks):** Kötü niyetli kişilerin sisteme yüklenen görüntüleri manipüle ederek modelin yanlış teşhis (örn. risk skorunun kasıtlı değiştirilmesi) yapmasına neden olması.
- **API ve Veritabanı Zafiyetleri:** Sistemin arka planında (backend) oluşabilecek SQL Injection, XSS veya API uç nokta ihlalleri.

####  2. Risk Değerlendirmesi
- **Hasta Mahremiyeti İhlali (Kritik Risk):** Hassas sağlık verilerinin açığa çıkması, ciddi yasal (KVKK/GDPR ihlali) ve etik sorunlara yol açar.
- **Hatalı Teşhis ve Hasta Güvenliği (Kritik Risk):** Modelin veya veritabanındaki verilerin manipüle edilmesi, doktorun yanlış yönlendirilmesine ve hastanın zarar görmesine neden olabilir.
- **Sistem Kesintisi (Orta Risk):** Sistemin DDoS gibi saldırılarla erişilemez hale gelmesi, poliklinik operasyonlarını yavaşlatır.

####  3. Eylem Planı (Risk Azaltma Stratejileri)
- **Güçlü Kimlik Doğrulama:** Doktor girişlerinde Rol Tabanlı Erişim Kontrolü (RBAC) ve İki Aşamalı Doğrulama (2FA/MFA) zorunlu kılınacaktır.
- **Uçtan Uca Şifreleme:** Veri iletiminde TLS/SSL protokolleri kullanılacak, durağan hasta verileri (EHR) AES-256 gibi güçlü algoritmalarla veritabanında şifrelenecektir.
- **Veri Anonimleştirme:** Yapay zeka modelinin eğitimi ve analizi sırasında hastaların kişisel kimlik bilgileri (PII) maskelenecek/anonimleştirilecektir.
- **Güvenlik Loglaması (Audit Trails):** Sistemde kimin, ne zaman, hangi veriye eriştiği değiştirilemez şekilde kayıt altına alınarak izlenebilirlik sağlanacaktır.
- **Girdi Doğrulama (Input Validation):** Sisteme yüklenen dosyalar ve API istekleri kötü amaçlı yazılımlara ve manipülasyonlara karşı sıkı bir taramadan geçirilecektir.




#  Akıllı Teşhis ve Tedavi Sistemi
 **Sorumlu:** Edanur Yasak
 **Tarih:** 28 Mart 2026

## Veritabanı Tasarımı ve İlişkiler

Bu sistemde hem **görüntü verisi** hem de **hasta bilgileri (EHR)** tutulacağı için ilişkisel bir yapı tercih edilmiştir. Bu amaçla **MySQL** kullanılmıştır.

---

# 1️⃣ Temel Varlıklar (Tablolar)

Bu sistem 5 ana tablodan oluşur:

* Hasta (Patients)
* Doktor (Doctors)
* Görüntü (Images)
* Teşhis (Diagnoses)
* Tedavi Planı (Treatments)

---

# 2️⃣ Tablolar ve Alanlar

##  1. Patients (Hastalar)

Hastaya ait temel bilgiler tutulur.

| Alan            | Tür      | Açıklama           |
| --------------- | -------- | ------------------ |
| patient_id      | INT (PK) | Hasta ID           |
| age             | INT      | Yaş                |
| gender          | VARCHAR  | Cinsiyet           |
| medical_history | TEXT     | Geçmiş hastalıklar |
| diabetes        | BOOLEAN  | Diyabet durumu     |

📌 Not: KVKK gereği isim/TC gibi bilgiler tutulmayabilir (anonimleştirme).

---

##  2. Doctors (Doktorlar)

Sistemi kullanan doktorlar.

| Alan           | Tür      | Açıklama                   |
| -------------- | -------- | -------------------------- |
| doctor_id      | INT (PK) | Doktor ID                  |
| name           | VARCHAR  | Doktor adı                 |
| specialization | VARCHAR  | Uzmanlık (dermatoloji vb.) |
| email          | VARCHAR  | Giriş bilgisi              |

---

##  3. Images (Tıbbi Görüntüler)

Modelin analiz ettiği görüntüler.

| Alan        | Tür      | Açıklama              |
| ----------- | -------- | --------------------- |
| image_id    | INT (PK) | Görüntü ID            |
| patient_id  | INT (FK) | Hastaya bağlı         |
| image_path  | VARCHAR  | Dosya yolu            |
| image_type  | VARCHAR  | (cilt / retina / OCT) |
| upload_date | DATETIME | Yüklenme tarihi       |

---

##  4. Diagnoses (Teşhisler)

AI modelinin ürettiği sonuçlar.

| Alan         | Tür      | Açıklama         |
| ------------ | -------- | ---------------- |
| diagnosis_id | INT (PK) | Teşhis ID        |
| image_id     | INT (FK) | Hangi görüntüden |
| disease_name | VARCHAR  | Hastalık adı     |
| risk_score   | FLOAT    | Risk oranı (%)   |
| stage        | VARCHAR  | Hastalık evresi  |
| created_at   | DATETIME | Tarih            |

---

##  5. Treatments (Tedavi Planı)

Kişiye özel öneriler.

| Alan           | Tür      | Açıklama              |
| -------------- | -------- | --------------------- |
| treatment_id   | INT (PK) | Tedavi ID             |
| diagnosis_id   | INT (FK) | Hangi teşhise bağlı   |
| treatment_type | VARCHAR  | İlaç / iğne / cerrahi |
| dosage         | VARCHAR  | Doz bilgisi           |
| schedule       | VARCHAR  | Tedavi sıklığı        |
| notes          | TEXT     | Açıklama              |

---

# 3️⃣ İlişkiler (Relationships)

Bu sistemde ilişkiler şöyle çalışır:

* 1 hasta → birçok görüntü
* 1 görüntü → 1 teşhis
* 1 teşhis → 1 tedavi
* 1 doktor → birçok hasta (opsiyonel eklenebilir)

---

##  İlişki Şeması (Mantık)

```
Patients (1) ──── (N) Images
Images (1) ──── (1) Diagnoses
Diagnoses (1) ──── (1) Treatments
Doctors (1) ──── (N) Patients
```

---

# 4️⃣ SQL Örnek


```sql
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    age INT,
    gender VARCHAR(10),
    medical_history TEXT,
    diabetes BOOLEAN
);

CREATE TABLE Images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    image_path VARCHAR(255),
    image_type VARCHAR(50),
    upload_date DATETIME,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

CREATE TABLE Diagnoses (
    diagnosis_id INT PRIMARY KEY AUTO_INCREMENT,
    image_id INT,
    disease_name VARCHAR(100),
    risk_score FLOAT,
    stage VARCHAR(50),
    created_at DATETIME,
    FOREIGN KEY (image_id) REFERENCES Images(image_id)
);

CREATE TABLE Treatments (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    diagnosis_id INT,
    treatment_type VARCHAR(100),
    dosage VARCHAR(100),
    schedule VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (diagnosis_id) REFERENCES Diagnoses(diagnosis_id)
);
```

---

# 5️⃣ Tasarımın Mantığı

Bu veritabanı tasarımı:

* Çok modlu veri yapısını destekler (görüntü + EHR)
* Veri tekrarını önler (normalize yapı)
* Yapay zeka çıktılarının izlenmesini sağlar
* Tedavi sürecinin zaman içinde takip edilmesine olanak tanır



-------------------------------
## 3. Hafta

* **Ali İstanbullu:** Projenin Frontend ve Backend haberleşmesini sağlayacak API tasarımı yapıldı ve Endpoint'ler belirlendi.
#           Teknoloji Araştırması ve Seçimi (Siber Güvenlik Araçları)

 **Sorumlu:** Cansude Sayın
 **Tarih:** 23 Mart 2026

Geliştirme ortamının kurulmasının ardından, proje kapsamında kullanılacak siber güvenlik araçları araştırılmıştır. Bu araçlar; sistem güvenliğini sağlamak, zafiyetleri tespit etmek ve analiz süreçlerini desteklemek amacıyla incelenmiştir.

#### İncelenen Araç Kategorileri

Siber güvenlik araçları üç ana kategoride değerlendirilmiştir:

- Zafiyet Tarayıcıları (Vulnerability Scanners)
- Sızma Testi Araçları (Pentest Tools)
- Ağ Analiz Araçları (Network Analysis Tools)

---

#### Araç Analizi ve Karşılaştırma

##### Zafiyet Tarayıcıları

- Nessus / OpenVAS  
  Özellik: Sistemlerdeki güvenlik açıklarını otomatik olarak tespit eder.  
  Avantaj: Hızlı ve kapsamlı tarama yapar.  
  Dezavantaj: Yanlış pozitif sonuçlar verebilir.

---

##### Sızma Testi Araçları

- Metasploit  
  Özellik: Güvenlik açıklarını test etmek ve exploit geliştirmek için kullanılır.  
  Avantaj: Güçlü ve modüler yapı  
  Dezavantaj: Öğrenmesi zor olabilir

- Burp Suite  
  Özellik: Web uygulamalarındaki açıkları analiz eder.  
  Avantaj: Web güvenliği için etkilidir  
  Dezavantaj: Ücretsiz versiyonu sınırlıdır

---

##### Ağ Analiz Araçları

- Nmap  
  Özellik: Ağ tarama ve açık port tespiti yapar  
  Avantaj: Hızlı ve güçlü analiz  
  Dezavantaj: Komut satırı bilgisi gerektirir

- Wireshark  
  Özellik: Ağ trafiğini analiz eder  
  Avantaj: Detaylı veri analizi  
  Dezavantaj: Yeni başlayanlar için karmaşık olabilir

---

#### Genel Karşılaştırma

| Araç | Kullanım Alanı | Avantaj | Dezavantaj |
|------|--------------|--------|-----------|
| Nessus / OpenVAS | Zafiyet tarama | Otomatik analiz | Yanlış pozitif |
| Metasploit | Sızma testi | Güçlü exploit sistemi | Karmaşık |
| Burp Suite | Web güvenliği | Detaylı analiz | Ücretli özellikler |
| Nmap | Ağ tarama | Hızlı ve etkili | CLI zor olabilir |
| Wireshark | Trafik analizi | Derin analiz | Öğrenmesi zor |

---

#### Proje İçin Seçilen Araçlar

Siber Şifacılar grubu olarak proje ihtiyaçları doğrultusunda aşağıdaki araçların kullanılması uygun görülmüştür:

- Nmap → Ağ ve sistem keşfi  
- Wireshark → Veri trafiği analizi  
- Metasploit → Güvenlik açıklarının test edilmesi  
- OpenVAS / Nessus → Zafiyet taraması  

---

#### Kullanım Planı

Proje sürecinde araçların kullanım planı aşağıdaki şekilde belirlenmiştir:

1. Geliştirme Aşaması  
   Sistem mimarisi oluşturulurken temel güvenlik kontrolleri yapılacaktır.

2. Test Aşaması  
   Nmap ile sistem taraması yapılacaktır.  
   OpenVAS ile zafiyet analizi gerçekleştirilecektir.

3. Güvenlik Testleri  
   Metasploit ile sızma testleri uygulanacaktır.  
   Wireshark ile ağ trafiği analiz edilecektir.

4. Raporlama  
   Tespit edilen güvenlik açıkları raporlanacaktır.  
   Geliştirilecek sistemde gerekli güvenlik önlemleri alınacaktır.

---
 **Sorumlu:** Cansude Sayın
 **Tarih:** 29 Mart 2026
 
 # MediAI — Arayüz Tasarım Raporu

Tıbbi yapay zeka teşhis sistemine ait kullanıcı arayüzü tasarımları. Sistem; giriş, dashboard, görüntü analizi, teşhis sonuçları, tedavi planı ve hasta profili sayfalarından oluşmaktadır.

---

## İçindekiler

1. [Giriş Ekranı](#1-giriş-ekranı)
2. [Dashboard](#2-dashboard)
3. [Görüntü Analizi](#3-görüntü-analizi)
4. [Teşhis Sonuçları](#4-teşhis-sonuçları)
5. [Tedavi Planı](#5-tedavi-planı)
6. [Hasta Profili](#6-hasta-profili)

---

## 1. Giriş Ekranı

Klinik kimlik doğrulama ekranı. Doktor uzmanlık alanını seçerek (Oftalmoloji, Dermatoloji, Diğer) e-posta/şifre veya kurumsal SSO ile sisteme erişir. 256-bit TLS şifrelemesi ve KVKK uyumluluğu belirtilmiştir.

![Giriş Ekranı]<img width="1887" height="863" alt="image" src="https://github.com/user-attachments/assets/b4b74892-f146-45a2-8da6-faef3a5d9b47" />

**Temel özellikler:**
- Uzmanlık alanı seçimi (kart tabanlı)
- E-posta / Doktor ID ve şifre alanları
- Kurumsal SSO girişi (Active Directory)
- Güvenlik bilgisi (TLS, KVKK)
- Sol panelde sistem istatistikleri (%95.4 doğruluk, %60 raporlama süresi azalması)

---

## 2. Dashboard

Sistemin genel bakış ekranı. Günlük analiz sayısı, bekleyen teşhisler, AI doğruluk oranı ve aktif hasta metrikleri anlık olarak izlenebilir.

![Dashboard]<img width="1913" height="875" alt="image" src="https://github.com/user-attachments/assets/02858e96-a2fa-4869-a520-1660494f54bb" />

**Temel özellikler:**
- 4 metrik kartı: Bugünkü Analizler (24), Bekleyen Teşhis (7), Doğruluk Oranı (%94.2), Aktif Hastalar (142)
- Haftalık analiz dağılımı çubuk grafiği (Akciğer BT / MRI Beyin / X-Ray)
- Son aktivite akışı (5 kayıt)
- Sistem durumu paneli (AI Motoru, DICOM Sunucusu, Görüntü İşleme, Yedekleme)
- Bekleyen analizler listesi (Ahmet Yıldız, Fatma Demir, Mehmet Kaya — öncelik badge'leriyle)
- Tanı dağılımı (Pnömoni %34, Normal %42, Tümör Şüphesi %18, Diğer %6)

---

## 3. Görüntü Analizi

DICOM görüntü görüntüleyici ekranı. Karanlık temelli viewer, kesit navigasyonu ve AI analiz sonuçlarını içerir. Tespit edilen anomali görüntü üzerinde kırmızıyla işaretlenir.

![Görüntü Analizi]<img width="1897" height="877" alt="image" src="https://github.com/user-attachments/assets/0762f793-1a96-4c5c-9dbe-23a6a029b26f" />

**Temel özellikler:**
- Karanlık DICOM viewer (Akciğer BT, kesit 45/120)
- Araç çubuğu: seçim, zoom, ölçüm, anotasyon, W/L kontrolü
- Parlaklık ve kontrast slider'ları
- Anomali işaretleyici (kırmızı, pulse animasyonu)
- Kesit thumbnail şeridi (8 kesit)
- Sağ panel AI bulguları:
  - Şüpheli Nodül — Sağ alt lob, 8.2mm solid — **%87 güven**
  - Küçük İnfiltrasyon — Sol üst lob, periferik — **%62 güven**
- İşlemler: Teşhis Oluştur, Rapor Görüntüle, İkinci Görüş İste

---

## 4. Teşhis Sonuçları

AI tarafından üretilen teşhis bulgularının doktor tarafından incelendiği ve onaylandığı ekran.

### 4.1 Birincil Teşhis ve Bulgular

![Teşhis Sonuçları]<img width="1896" height="875" alt="image" src="https://github.com/user-attachments/assets/689c3d1f-77a6-4d8f-8e45-60b691e0df09" />

**Temel özellikler:**
- Birincil teşhis: **Pulmoner Nodül — Malignite Şüphesi** (ICD-10: R91.1)
- Badge'ler: Pirads 4, Biyopsi Gerekli, Yüksek Öncelik
- AI güven skoru metresi (gradient ölçek, %87)
- Tespit edilen bulgular:
  - Solid Nodül — %87 güven (8.2mm × 7.6mm, SAL, Solid)
  - Periferik İnfiltrasyon — %62 güven (SÜL, GGO, Diffüz)

### 4.2 Ayırıcı Tanı ve Doktor Notu
  
![Teşhis Sonuçları (devam)]<img width="1896" height="762" alt="image" src="https://github.com/user-attachments/assets/a382ca1e-91f2-42ef-8320-1b1c2f463619" />

**Temel özellikler:**
- Ayırıcı tanı tablosu: Primer akciğer kanseri %72, Metastatik lezyon %18, Karsinoid tümör %7, Benign granülom %3
- Doktor notu alanı (düzenlenebilir)
- Teşhis geçmişi zaman çizelgesi (BT Analizi, Görüntü Yüklendi, Önceki BT, İlk Başvuru)
- Önerilen adımlar: PET-CT Tetkiki (Acil), Bronkoskopik Biyopsi, Onkoloji Konsültasyonu, Kontrol BT
- Aksiyonlar: **Teşhisi Onayla** / **Reddet**

---

## 5. Tedavi Planı

Hasta için oluşturulan tedavi sürecinin adım adım izlendiği ekran.

### 5.1 Fazlar ve Adımlar

![Tedavi Planı]<img width="1899" height="876" alt="image" src="https://github.com/user-attachments/assets/55407b4f-a6b7-4179-bc07-170dffd05dfd" />

**Temel özellikler:**
- 5 fazlı stepper: Teşhis (tamamlandı) → Görüntüleme (aktif) → Biyopsi → Tedavi → Takip
- Genel ilerleme %40, Görüntüleme %100
- Konsültasyon ekibi: Dr. Ahmet Yılmaz, Dr. Selin Bozkurt, Dr. Murat Özkan
- Yaklaşan randevular: 02 Nis PET-CT, 05 Nis Bronkoskopi, 10 Nis Onkoloji Konsültasyonu

### 5.2 İlaçlar ve Detay

![Tedavi Planı (devam)]<img width="1893" height="844" alt="image" src="https://github.com/user-attachments/assets/1e7677ed-27c4-4838-a9ca-f21107a1e0b6" />

**Temel özellikler:**
- Sıralı 5 tedavi adımı (durum badge'leriyle: Tamamlandı / Planlandı / Bekliyor)
- Mevcut ilaçlar: Acetylsalicylic Acid 100mg, Ambroxol HCl 30mg, Vitamin D3 1000IU

---

## 6. Hasta Profili

Hastaya ait tüm klinik ve demografik bilgilerin yer aldığı kapsamlı profil ekranı.

### 6.1 Genel Bilgiler ve Yaşamsal Bulgular

![Hasta Profili]<img width="1898" height="878" alt="image" src="https://github.com/user-attachments/assets/02362bc7-6867-41c8-b94e-5957df346b79" />

**Temel özellikler:**
- Profil: Ahmet Yıldız, #P-2041, **Yüksek Risk**
- Kişisel bilgiler: 48 yaş, Erkek, A Rh+, 178cm / 82kg
- Yaşamsal bulgular: Tansiyon 138/88 (Yüksek), Nabız 78bpm (Normal), SpO2 %96 (Sınırda), Ateş 36.8°C (Normal)
- Görüntüleme geçmişi: BT Toraks (Anormal), Akciğer Grafisi (Normal), BT Toraks (Normal), MRI Beyin (Normal)
- Hastalık geçmişi: Hipertansiyon 2018, Tip 2 Diyabet 2021, KOAH 2023, Apendektomi 1998
- Risk faktörleri: Sigara / Aile Öyküsü (Yüksek), Alkol / Meslek (Orta)
- Aktif ilaçlar: Metformin 850mg, Lisinopril 10mg, Budesonid inhaler

### 6.2 Laboratuvar Sonuçları

![Hasta Profili (devam)]<img width="1895" height="512" alt="image" src="https://github.com/user-attachments/assets/ab9b851e-4187-449c-96a1-0f0362b5bd93" />

**Temel özellikler:**
- Laboratuvar sekmeleri: Hemogram / Biyokimya / Tümör Marker
- Hemogram değerleri: WBC 8.2, RBC 4.6, Hemoglobin 13.8g/dL, Hematokrit 41.2%, PLT 310
- **CEA: 8.4 ng/mL ↑** (referans <3.0 — anormal, kırmızıyla vurgulanmış)

---

## Tasarım Sistemi

| Özellik | Değer |
|---|---|
| Kenar çubuğu genişliği | 220px |
| Birincil renk | `#1a5fa8` |
| Hata / Acil | `#e24b4a` |
| Uyarı | `#ba7517` |
| Başarı | `#0f6e56` |
| Kenarlık | `0.5px solid` |
| Kart köşe yarıçapı | `10px` |
| Görüntüleyici arka plan | `#0d0d0d` |

---










#### Sonuç

Yapılan analizler sonucunda, proje için gerekli siber güvenlik araçları belirlenmiş ve kullanım planı oluşturulmuştur. Bu araçlar sayesinde sistemin güvenliği artırılacak ve olası tehditler erken aşamada tespit edilecektir.

---

## 4. Hafta

# API Entegrasyonu ve Temel Uç Noktalarının (Endpoints) Geliştirilmesi

**Sorumlu:** Ali İstanbullu
**Tarih:** 6 Nisan 2026

Projenin 4. haftasında, web arayüzü ile veritabanı ve yapay zeka modelleri arasındaki veri iletişimini sağlayacak merkezi API altyapısı **Python Flask** framework'ü kullanılarak kodlanmıştır.

### 1. Geliştirilen Temel Uç Noktalar (Endpoints)

Sistem RESTful mimari standartlarına uygun olarak tasarlanmış ve aşağıdaki 3 temel kapı (route) `app.py` dosyası üzerinde ayağa kaldırılmıştır:

* **`POST /api/v1/hastalar` (Hasta Kayıt Modülü):**
    * **İşlev:** Frontend'den gelen hasta kimlik ve klinik verilerini (JSON formatında) karşılar.
    * **Durum:** Arayüz testleri için "201 Created" başarılı yanıtı ve dummy (sahte) hasta ID'si döndürecek şekilde ayarlandı. İlerleyen fazlarda doğrudan MySQL veritabanına veri yazacak.

* **`POST /api/v1/analiz/baslat` (Yapay Zeka Tetikleyici):**
    * **İşlev:** Doktorun arayüzden yüklediği DICOM/Görsel dosyalarını ve hasta ID'sini alarak arka plan işlemlerini başlatır.
    * **Durum:** Ön işleme ve CNN modelini tetikleyecek ana kapıdır. Şimdilik sistemin kilitlenmemesi için asenkron bir "İşleniyor (202 Accepted)" yanıtı dönmektedir.

* **`GET /api/v1/analiz/sonuc/<analiz_id>` (Klinik Karar Destek Çıktısı):**
    * **İşlev:** Veritabanında oluşan yapay zeka analiz sonuçlarını (Risk skoru, teşhis, ısı haritası URL'si) Frontend'e servis eder.
    * **Durum:** UI/UX tasarımlarının (Dashboard ve Teşhis ekranları) veri ile test edilebilmesi adına, sahte bir "Malign Melanom" analiz sonucu (JSON) üretecek şekilde kodlandı.

### 2. Mimari ve Entegrasyon Notları

* **Geliştirme Ortamı:** Flask kütüphanesi kullanılarak lokal sunucu (port 5000) yapılandırması tamamlandı ve veri trafiği loglaması aktif edildi.
* **Ekip İletişimi:** Yazılan kod bloklarının içine, UI/UX ve Veritabanı geliştiricisi ekip arkadaşlarımın kendi kodlarını nereye entegre edeceklerini gösteren detaylı dokümantasyon yorumları eklendi.
* **Test:** Endpoint'lerin JSON veri alma ve servis etme süreçleri lokal ortamda test edilip doğrulandıktan sonra proje repozitorisine yüklenerek ana projeyle (main branch) başarıyla birleştirildi (Merge).




## 4. Hafta

### API Entegrasyonu ve Temel Uç Noktalarının (Endpoints) Geliştirilmesi
**Sorumlu:** Ali İstanbullu **Tarih:** 6 Nisan 2026

Projenin 4. haftasında, web arayüzü ile veritabanı ve yapay zeka modelleri arasındaki veri iletişimini sağlayacak merkezi API altyapısı Python Flask framework'ü kullanılarak kodlanmıştır.

#### 1. Geliştirilen Temel Uç Noktalar (Endpoints)
Sistem RESTful mimari standartlarına uygun olarak tasarlanmış ve aşağıdaki 3 temel kapı (route) `app.py` dosyası üzerinde ayağa kaldırılmıştır:
- **POST /api/v1/hastalar (Hasta Kayıt Modülü):**
  - **İşlev:** Frontend'den gelen hasta kimlik ve klinik verilerini (JSON formatında) karşılar.
  - **Durum:** Arayüz testleri için "201 Created" başarılı yanıtı ve dummy (sahte) hasta ID'si döndürecek şekilde ayarlandı. İlerleyen fazlarda doğrudan MySQL veritabanına veri yazacak.
- **POST /api/v1/analiz/baslat (Yapay Zeka Tetikleyici):**
  - **İşlev:** Doktorun arayüzden yüklediği DICOM/Görsel dosyalarını ve hasta ID'sini alarak arka plan işlemlerini başlatır.
  - **Durum:** Ön işleme ve CNN modelini tetikleyecek ana kapıdır. Şimdilik sistemin kilitlenmemesi için asenkron bir "İşleniyor (202 Accepted)" yanıtı dönmektedir.
- **GET /api/v1/analiz/sonuc/<analiz_id> (Klinik Karar Destek Çıktısı):**
  - **İşlev:** Veritabanında oluşan yapay zeka analiz sonuçlarını (Risk skoru, teşhis, ısı haritası URL'si) Frontend'e servis eder.
  - **Durum:** UI/UX tasarımlarının (Dashboard ve Teşhis ekranları) veri ile test edilebilmesi adına, sahte bir "Malign Melanom" analiz sonucu (JSON) üretecek şekilde kodlandı.

#### 2. Mimari ve Entegrasyon Notları
- **Geliştirme Ortamı:** Flask kütüphanesi kullanılarak lokal sunucu (port 5000) yapılandırması tamamlandı ve veri trafiği loglaması aktif edildi.
- **Ekip İletişimi:** Yazılan kod bloklarının içine, UI/UX ve Veritabanı geliştiricisi ekip arkadaşlarımın kendi kodlarını nereye entegre edeceklerini gösteren detaylı dokümantasyon yorumları eklendi.
- **Test:** Endpoint'lerin JSON veri alma ve servis etme süreçleri lokal ortamda test edilip doğrulandıktan sonra proje repozitorisine yüklenerek ana projeyle (main branch) başarıyla birleştirildi (Merge).



-------------------------------------------


###  Temel Hastalık Teşhis Modeli Oluşturulması

**Sorumlu:** Enes Zukra  
**Tarih:** 17 Nisan 2026

Projenin temel fonksiyonu olan hastalık teşhisini gerçekleştirecek yapay zeka modelinin mimarisi tasarlanmış ve ilk prototip model oluşturulmuştur.

####  Teknik Mimari ve Derin Öğrenme Yapısı
- **Model Tipi:** Tıbbi görüntü analizi (cilt lezyonları ve göz fundus fotoğrafları) için endüstri standardı olan **CNN (Convolutional Neural Network)** mimarisi kullanılmıştır.
- **Kullanılan Teknolojiler:** Modelin geliştirilmesi, katmanlarının oluşturulması ve eğitilmesi süreçlerinde **TensorFlow** ve **Keras** kütüphanelerinden yararlanılmıştır.
- **Katman Yapısı:** Görüntüdeki mikro değişimleri yakalayabilmek adına çok katmanlı (Conv2D ve MaxPooling) bir yapı kurgulanmış, aşırı öğrenmeyi (overfitting) önlemek için optimize edilmiştir.

####  Model Performansı ve Validasyon
- Oluşturulan model, eğitim seti dışında bırakılan **Validasyon Veri Seti** üzerinde test edilmiştir.
- Modelin doğruluk (Accuracy) ve kayıp (Loss) değerleri analiz edilerek, klinik karar destek sistemi için gerekli olan temel başarı kriterlerini karşıladığı doğrulanmıştır.
- Elde edilen ilk sonuçlar, sistemin hastalıkları yüksek güven oranıyla sınıflandırabildiğini göstermektedir.

-------------------------------------------

Web Arayüzü için Temel HTML ve CSS Şablonlarının Oluşturulması
Sorumlu: Cansude Sayın
Tarih: 18 Nisan 2026
Projenin 4. haftasında, doktorların kullanacağı web tabanlı kullanıcı arayüzü için temel HTML ve CSS şablonları oluşturulmuştur. Şablonlar; basit, kullanıcı dostu ve responsive (duyarlı) tasarım prensiplerine uygun olarak geliştirilmiştir.
1. Oluşturulan Sayfalar
Sistem toplamda 6 ana sayfadan oluşmaktadır ve her sayfa kendi HTML dosyası olarak hazırlanmıştır:

mediAI_login_responsive.html — Giriş Ekranı
mediAI_dashboard_responsive.html — Dashboard
mediAI_image_analysis_responsive.html — Görüntü Analizi
mediAI_diagnosis_responsive.html — Teşhis Sonuçları
mediAI_treatment_responsive.html — Tedavi Planı
mediAI_patient_responsive.html — Hasta Profili

2. Responsive (Duyarlı) Tasarım
Tüm sayfalar farklı ekran boyutlarına uyum sağlayacak şekilde style.css adlı ortak bir CSS dosyasına bağlanmıştır. Üç kırılma noktası tanımlanmıştır:

1024px altı (Tablet): Sidebar daralır, grid yapılar 2 sütuna iner.
768px altı (Mobil): Sidebar gizlenir, hamburger menü aktif olur, içerik tek sütuna geçer.
480px altı (Küçük Mobil): Tüm içerik tek sütun, gereksiz elemanlar gizlenir.

3. API Bağlantıları
Ali'nin geliştirdiği Flask API uç noktaları arayüze entegre edilmiştir:

Hasta Profili sayfası: "Profili Düzenle" butonuna basıldığında modal form açılır, formdaki hasta bilgileri JSON formatında POST /api/v1/hastalar endpoint'ine gönderilir.
Görüntü Analizi sayfası: Fotoğraf yükleme alanı eklendi. Doktor görüntüyü seçip "Analiz Başlat" butonuna bastığında dosya bilgileri POST /api/v1/analiz/baslat endpoint'ine iletilir.
Teşhis Sonuçları sayfası: Sayfa açıldığında otomatik olarak GET /api/v1/analiz/sonuc/{id} endpoint'i çağrılır ve dönen teşhis, risk skoru ve AI açıklaması ilgili alanlara yazılır.

4. Sayfa Arası Navigasyon
Tüm sayfalardaki sidebar linkleri birbirine bağlanmıştır. "Sisteme Giriş Yap" butonu Dashboard'a, "Teşhis Oluştur" butonu Teşhis Sonuçları sayfasına yönlendirmektedir.
5. Mimari Notlar

Ortak CSS değişkenleri style.css dosyasında tanımlanmış, tüm sayfalar bu dosyayı <link> ile kullanmaktadır.
Flask sunucusu çalışmadığı durumlarda sayfalar Demo Mod ile çalışmaya devam etmekte, sahte verilerle arayüz test edilebilmektedir.
Tüm dosyalar frontend/ klasörü altında düzenlenip proje repozitorisine yüklenerek ana dal (main branch) ile birleştirilmiştir.


