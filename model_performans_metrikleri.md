# 📊 Model Performans Metrikleri ve Değerlendirme Planı

Bu doküman, **Siber Şifacılar - Akıllı Teşhis ve Tedavi Sistemi** kapsamında geliştirilen çok modlu yapay zeka (CNN tabanlı) modelinin doğruluğunu, güvenilirliğini ve klinik ortamdaki geçerliliğini ölçmek için kullanılacak standartları belirler. Tıbbi görüntü analizi süreçlerinde karşılaşılabilecek riskler göz önünde bulundurularak spesifik eşikler ve izleme prosedürleri tanımlanmıştır.

---

## 1. Kullanılacak Performans Metrikleri ve Anlamları

Sistemin başarısı sadece genel doğrulukla değil, klinik risk profillerine göre dengelenmiş aşağıdaki metriklerle ölçülmektedir:

* **Doğruluk (Accuracy):** Modelin toplamda ne kadar doğru karar verdiğinin ölçüsüdür (*Doğru Teşhis Edilenler / Tüm Görüntüler*). Modelimizin temel performansını izlemek için kullanılır ancak dengesiz tıbbi veri setlerinde tek başına yeterli değildir.
* **Duyarlılık (Recall / Sensitivity):** Gerçekte **hasta olan** vakaların ne kadarının model tarafından doğru tespit edildiğidir.
    * *Klinik Önemi:* Projemizdeki **en kritik metriktir**. Malign Melanom veya Proliferatif DR gibi durumlarda bir hastaya yanlışlıkla "sağlıklı" demek (False Negative), hastanın tedavisini geciktireceğinden ölümcül risk taşır. Duyarlılığın maksimize edilmesi hedeflenmektedir.
* **Kesinlik (Precision):** Modelin **hasta dediği** vakaların gerçekte ne kadarının hasta olduğunun ölçüsüdür.
    * *Klinik Önemi:* Sağlıklı bir bireye kanser teşhisi koymak (False Positive), hastada gereksiz biyopsi, radyasyon, psikolojik stres ve poliklinik yoğunluğuna neden olur. Duyarlılık kadar hayati olmasa da operasyonel verimlilik için yüksek tutulmalıdır.
* **F1 Skoru (F1-Score):** Kesinlik ve Duyarlılık metriklerinin harmonik ortalamasıdır. Özellikle APTOS 2019 (Diyabetik Retinopati) ve ISIC 2019 veri setlerindeki gibi "Sağlıklı" vakaların "Hasta" vakalardan sayıca çok daha fazla olduğu (Class Imbalance) durumlarda modelin gerçek başarısını gösterir.
* **AUC-ROC (Area Under the Receiver Operating Characteristic Curve):** Modelin farklı sınıflandırma eşik değerlerinde (threshold) sağlıklı ve hasta dokuyu birbirinden ne kadar iyi ayırt edebildiğini gösterir. 1.0'a yaklaşması mükemmel ayrım anlamına gelir.

---

## 2. Farklı Hastalıklar ve Veri Setleri İçin Ölçüm Stratejisi

Modelin performansı, farklı modaliteler ve veri setleri üzerinde spesifik amaçlara göre ölçülecektir:

### A. Dermatoloji (Malign Melanom ve Bazal Hücreli Karsinom)
* **Veri Seti:** ISIC 2019 & HAM10000
* **Sınıflandırma Türü:** İkili (Binary) Sınıflandırma (Kanserli / Benign)
* **Ölçüm Stratejisi:** "Evre 0" aşamasında mikro değişimlerin tespiti hedeflendiğinden, sistemin karar eşiği (threshold) düşürülerek (örn: 0.35) **Duyarlılık (Recall)** metriğine ağırlık verilir. Kanser riski taşıyan en ufak anomali işaretlenmeli ve `Teşhis Sonuçları` ekranında doktora "Şüpheli Lezyon" badge'i ile gösterilmelidir.

### B. Oftalmoloji (Diyabetik Retinopati - DR)
* **Veri Seti:** APTOS 2019
* **Sınıflandırma Türü:** Çok Sınıflı (Multi-class) Evrelendirme (0: Sağlıklı, 1: Hafif, 2: Orta, 3: Şiddetli, 4: Proliferatif)
* **Ölçüm Stratejisi:** Sadece hastalığın varlığı değil, evresi de teşhis edildiğinden **Makro F1 Skoru** kullanılacaktır. Özellikle Evre 3 ve Evre 4 arasındaki geçişlerin doğru tespit edilip edilmediği Karmaşıklık Matrisi (Confusion Matrix) üzerinden özel olarak izlenecektir.

### C. Dermatoloji (Sedef & Akne) ve Oftalmoloji (YBMD)
* **Ölçüm Stratejisi:** Psoriasis alanı (PASI skoru) ve OCT taramalarındaki sıvı birikimi hesaplamalarında, sınıflandırmadan ziyade "Alan/Piksel Doğruluğu" önemlidir. Bu nedenle hedef bölgenin gerçek boyutu ile modelin tahmin ettiği alan arasındaki örtüşmeyi ölçen **IoU (Intersection over Union) / Jaccard Endeksi** kullanılacaktır.

---

## 3. Kabul Edilebilir Performans Eşikleri

Klinik denemelerde uzman doktor kararlarıyla eşdeğer performans hedefine ulaşmak için sistemin karşılaması gereken asgari eşikler şu şekildedir:

* **Genel Klinik Hedef (Accuracy):** Min. **%95.0** (Şu anki durum: %92.00 - Veri artırma ve ek eğitim ile hedefe ulaşılacaktır)[cite: 1].
* **Kritik Hastalıklar Duyarlılık (Recall - Melanom):** Min. **%90.0** (Şu anki durum: %92.31 - Eşik düşürme stratejisi başarılı, bu seviye korunmalıdır)[cite: 1].
* **Operasyonel Kesinlik (Precision):** Min. **%95.0** (Şu anki durum: %96.15 - Gereksiz doktor konsültasyonlarını önlemek adına başarıyla sağlandı)[cite: 1].

---

## 4. Performans İzleme ve Değerlendirme Planı

Modelin canlıya alınması (Deployment) sonrasında performansı statik kalmamalı, sürekli izlenmelidir:

1.  **Aktif Öğrenme (Active Learning) Döngüsü:** UI üzerinden doktorlara sunulan "Teşhisi Onayla" veya "Reddet / Düzenle" butonlarından elde edilen veriler loglanacaktır. Doktor tarafından düzeltilen teşhisler (EHR ve Görsel verisi ile birlikte), modelin bir sonraki iterasyonunda yeniden eğitim (retraining) verisi olarak sisteme geri beslenecektir.
2.  **API Monitörizasyonu:** `GET /api/v1/analiz/sonuc/<analiz_id>` uç noktasından dönen AI güven skorları (Confidence Scores) loglanacak. Eğer model sürekli olarak düşük güven skorları (< %60) üretmeye başlarsa (Data Drift ihtimali), sistem admin paneline otomatik uyarı düşecektir.
3.  **Periyodik Testler:** Her ayın sonunda, modele o ay içinde sisteme eklenen anonimleştirilmiş 100 yeni klinik vaka verilerek kör test (blind test) yapılacak ve metriklerin hedef eşiklerin altına düşüp düşmediği kontrol edilecektir.

---

## 5. Model Performans Test Sonuçları (v1.0 - 6. Hafta)

Projenin 6. haftasında gerçekleştirilen test senaryolarında, CNN modelinin elde ettiği performans sonuçları ve klinik bulgular aşağıda raporlanmıştır[cite: 1].

**Genel Performans Tablosu:**
| Senaryo | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Temel Sınıflandırma | %92.00 | %96.15 | %89.29 | %92.59 |[cite: 1]
| Melanom Tespiti | %92.00 | %97.30 | %92.31 | %94.74 |[cite: 1]
| Diyabetik Retinopati | %92.00 | %95.00 | %91.94 | %93.44 |[cite: 1]
| **Ortalama** | **%92.00** | **%96.15** | **%91.18** | **%93.59** |[cite: 1]

**Önemli Bulgular:**
* Melanom senaryosunda Recall hedefi olan %90'ın üzerine çıkılmış (%92.31), yanlış negatifi minimize etmek amacıyla karar eşiği 0.50'den 0.35'e düşürme stratejisi başarıyla uygulanmıştır[cite: 1].
* Ortalama Precision %96.15 ile sağlıklı bireylere yanlış teşhis koyma oranı oldukça düşük tutulmuştur[cite: 1].
* Projenin klinik hedefi olan %95 doğruluğa ulaşmak için veri artırma (data augmentation) ve ek eğitim önerilmektedir[cite: 1].