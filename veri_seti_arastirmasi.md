Akıllı Teşhis ve Tedavi Sistemi - Veri Seti Araştırması ve Erişim Planı
Sorumlu: Ali İstanbullu
Tarih: 6 Mart 2026

Proje kapsam belgesinde belirtilen teşhis ve tedavi optimizasyonu hedefleri doğrultusunda, model eğitiminde kullanılacak uygun veri setleri ve bu verilere erişim adımları aşağıda planlanmıştır. Sistem "Çok Modlu" (Görüntü + EHR) çalışacağı için, meta veri (yaş, cinsiyet, bölgesel analiz) içeren veri setlerine öncelik verilmiştir.

1. Dermatoloji (Cilt Hastalıkları) Veri Setleri
Projedeki Malign Melanom, Bazal Hücreli Karsinom, Sedef ve Akne teşhisleri için dermoskopik ve klinik görüntüler kullanılacaktır.

ISIC 2019 & HAM10000 (Melanom ve Karsinom İçin):

İçerik: 25.000'den fazla dermoskopik görüntü. Hastaların yaş, cinsiyet ve lezyon bölgesi (EHR verisi) CSV formatında görsellerle eşleştirilmiştir.

Durum: Açık Kaynaklı (Kaggle / ISIC Arşivi).

Proje Uyumu: ABCD kuralı analizi ve "Evre 0" tespiti hedeflerine tam uygundur.

Dermnet (Sedef ve Akne İçin):

İçerik: 23 farklı cilt hastalığı kategorisinde toplanmış binlerce klinik cilt fotoğrafı.

Durum: Açık Kaynaklı (Kaggle).

Proje Uyumu: Lezyon yayılım alanı ve PASI skoru hesaplamaları için kullanılacaktır.

2. Oftalmoloji (Göz Hastalıkları) Veri Setleri
Diyabetik Retinopati için Fundus fotoğrafları, Yaşa Bağlı Makula Dejenerasyonu (YBMD) için ise OCT taramaları kullanılacaktır.

APTOS 2019 Blindness Detection (Diyabetik Retinopati):

İçerik: 3.662 yüksek çözünürlüklü retina fundus fotoğrafı. Görüntüler uzmanlar tarafından 0 (Sağlıklı) ile 4 (Proliferatif DR) arasında derecelendirilmiştir.

Durum: Açık Kaynaklı (Kaggle).

Proje Uyumu: Mikroanevrizma ve eksuda tespiti ile DR evrelendirmesi hedefini doğrudan karşılar.

Retinal OCT Images - Kermany et al. (YBMD / Sarı Nokta):

İçerik: 84.495 X-Ray benzeri Optik Koherens Tomografi (OCT) taraması.

Durum: Açık Kaynaklı (Kaggle / Mendeley Data).

Proje Uyumu: Retina katmanları arasındaki sıvı birikiminin tespit edilmesi ve Anti-VEGF iğne zamanlamasının ("Treat-and-Extend") optimize edilmesi için kullanılacaktır.

3. Veri Erişimi ve Entegrasyon Planı
Veri Çekme (Download): Veri setleri çok büyük (GB'larca) olduğu için manuel indirme yapılmayacaktır. Python ortamında kaggle API kullanılarak veriler doğrudan geliştirme sunucusuna/bilgisayarına otomatik çekilecektir.

Veri Ön İşleme (Preprocessing): Görüntü boyutları (örn: 224x224 piksel) standardize edilecek ve gürültü azaltma (noise reduction) filtreleri uygulanacaktır.

Veritabanı (SQL) Entegrasyonu: Hastaların EHR verileri (yaş, cinsiyet, diyabet geçmişi) ilişkisel SQL veritabanına aktarılacak, görüntülerin dosya yolları (file_path) bu demografik tablolarla eşleştirilecektir.
