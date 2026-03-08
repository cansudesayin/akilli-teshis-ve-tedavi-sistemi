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

### Hafta İçi Görev Listesi

- 📊 2. Gereksinim Toplama ve Analizi
- 🛠️ 3. Teknoloji Araştırması ve Seçimi
- 💻 4. Geliştirme Ortamı Kurulumu
- 🖼️ 5. Veri Seti İncelemesi ve Ön İşleme

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
**Tarih:** 8 Mart 2026

---

# Akıllı Teşhis ve Tedavi Sistemi

## Veri Analitiği ve Makine Öğrenimi Teknoloji Seçimi

### 1. Programlama Dili

Bu proje için temel geliştirme dili olarak **Python** seçilmiştir.

**Gerekçeler**

* Makine öğrenimi ve veri analitiği alanında en yaygın kullanılan dildir
* Tıbbi görüntü analizi için çok sayıda hazır kütüphane içerir
* Büyük veri setleri ile çalışmayı kolaylaştırır
* Akademik ve araştırma projelerinde standart hale gelmiştir

Projedeki veri ön işleme, model eğitimi ve analiz işlemlerinin tamamı Python tabanlı yürütülecektir.


# 2. Makine Öğrenimi ve Derin Öğrenme Kütüphaneleri

## PyTorch

Model geliştirme için **PyTorch** tercih edilmiştir.

**Neden PyTorch?**

* Derin öğrenme modelleri geliştirmek için esnek bir yapı sunar
* Araştırma projelerinde çok yaygın kullanılır
* Görüntü işleme modelleri için güçlü destek sağlar
* Eğitim sürecini kolayca görselleştirmeye izin verir

Bu kütüphane ile özellikle **Convolutional Neural Network (CNN)** tabanlı görüntü sınıflandırma modelleri geliştirilecektir.

Bu modeller:

* cilt lezyonlarını sınıflandırma
* retina görüntülerini analiz etme
* hastalık evrelerini belirleme

gibi görevleri yerine getirecektir.

# 3. Görüntü İşleme Teknolojileri

## OpenCV

Görüntü ön işleme işlemleri için **OpenCV** kullanılacaktır.

**Kullanım amaçları**

* görüntü boyutlarını standardize etmek
* gürültü azaltma
* kontrast iyileştirme
* lezyon bölgelerini belirginleştirme

Örneğin:

* dermoskopik görüntülerde lezyon sınırlarının daha net çıkarılması
* retina görüntülerinde damar yapılarını vurgulama


# 4. Veri Analitiği Araçları

## Pandas

Hasta verilerinin analizi için **Pandas** kullanılacaktır.

**Kullanım amaçları**

* yaş, cinsiyet gibi demografik verilerin analizi
* veri temizleme
* veri setlerinin düzenlenmesi
* model eğitimine uygun veri tabloları oluşturma


## NumPy

Sayısal işlemler için **NumPy** kullanılacaktır.

Makine öğrenimi algoritmaları büyük ölçüde matris hesaplamalarına dayandığı için NumPy yüksek performans sağlar.


# 5. Model Eğitimi Platformu

## Google Colab

Model eğitimi için **Google Colab** platformu kullanılacaktır.

**Avantajları**

* ücretsiz GPU desteği
* Python ortamı hazır gelir
* büyük veri setleri ile çalışma kolaylığı
* ekip üyeleri ile paylaşım kolaylığı

Bu platform özellikle görüntü verisi üzerinde eğitim yapılırken işlem süresini ciddi şekilde azaltacaktır.


# 6. Veritabanı Teknolojisi

Projedeki EHR verileri için **MySQL** gibi ilişkisel veritabanı sistemleri kullanılacaktır.

Veritabanında şu bilgiler tutulacaktır:

* hasta yaşı
* cinsiyet
* diyabet geçmişi
* görüntü dosya yolu

Bu yapı sayesinde görüntüler ve hasta bilgileri birbiriyle ilişkilendirilebilecektir.


# 7. Sistem Arayüzü (Opsiyonel)

Kullanıcıların sisteme görüntü yükleyebilmesi için basit bir web arayüzü oluşturulacaktır.

Bu amaçla **Flask** kullanılabilir.

Bu arayüz sayesinde kullanıcılar:

* cilt veya göz görüntüsü yükleyebilir
* analiz sonucunu görebilir
* olası hastalık tahminlerini inceleyebilir



# 8. Genel Sistem Akışı

Projenin teknik çalışma akışı şu şekilde planlanmaktadır:

1️⃣ Veri setlerinin **Kaggle API** ile indirilmesi
2️⃣ Görüntülerin **OpenCV ile ön işlenmesi**
3️⃣ Demografik verilerin **Pandas ile düzenlenmesi**
4️⃣ Görüntülerin **PyTorch modelleri ile eğitilmesi**
5️⃣ Tahmin sonuçlarının **SQL veritabanına kaydedilmesi**
6️⃣ Kullanıcıların **Flask arayüzü üzerinden sisteme erişmesi**

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

> İlerleyen haftalarda doldurulacak.
