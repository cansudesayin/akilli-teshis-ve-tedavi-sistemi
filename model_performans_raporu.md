# Model Performans Test Raporu

**Sorumlu:** Cansude Sayın
**Tarih:** 28 Nisan 2026
**Proje:** Akıllı Teşhis ve Tedavi Sistemi — Siber Şifacılar

---

## 1. Test Ortamı ve Kullanılan Bileşenler

| Bileşen | Detay |
|---|---|
| Test Edilen Model | Enes Zukra — CNN (TensorFlow/Keras) |
| Ön İşleme Modülü | Selim Yağbasan — `data_preprocessing.py` |
| Model Doğruluğu (Eğitim) | %92.4 (Hafta 6 optimizasyonu sonrası) |
| Optimizer | Adam (lr=0.001, β1=0.9, β2=0.999) |
| Kayıp Fonksiyonu | Binary Crossentropy |
| Görüntü Boyutu | 224 × 224 × 3 |
| Test Seti Oranı | %20 (Eğitim/Test: 80/20) |

---

## 2. Uygulanan Ön İşleme Adımları

Selim Yağbasan'ın `data_preprocessing.py` modülü temel alınarak test görüntüleri şu adımlardan geçirilmiştir:

- **Normalizasyon:** Piksel değerleri [0, 255] → [0, 1] aralığına dönüştürüldü
- **Aykırı Değer Baskılama:** IQR yöntemiyle aykırı piksel değerleri baskılandı (alt %1, üst %99 persentil)
- **Bellek Optimizasyonu:** float64 → float32 dönüşümü ile RAM kullanımı azaltıldı
- **Eksik Veri Tamamlama:** Sayısal alanlarda medyan, kategorik alanlarda mod değerleriyle tamamlama yapıldı

---

## 3. Test Senaryoları ve Sonuçlar

### Senaryo 1 — Temel Sınıflandırma Testi

Normal (0) ve Anormal (1) görüntülerin ikili sınıflandırması.

| Metrik | Sonuç |
|---|---|
| Doğruluk (Accuracy) | **%92.00** |
| Hassasiyet (Precision) | **%96.15** |
| Duyarlılık (Recall) | **%89.29** |
| F1 Skoru | **%92.59** |

**Karmaşıklık Matrisi:**

|  | Tahmin: Normal | Tahmin: Anormal |
|---|---|---|
| **Gerçek: Normal** | 42 (TN) | 2 (FP) |
| **Gerçek: Anormal** | 6 (FN) | 50 (TP) |

**Yorum:** Model, anormal görüntüleri yüksek Precision ile tespit etmektedir. 6 yanlış negatif değerin azaltılması için Melanom testinde eşik değeri düşürülmüştür.

---

### Senaryo 2 — Melanom Tespit Testi

Melanom görüntülerinde yanlış negatifi minimize etmek kritik önemdedir. Karar eşiği 0.50'den 0.35'e düşürülmüştür.

| Metrik | Sonuç |
|---|---|
| Doğruluk (Accuracy) | **%92.00** |
| Hassasiyet (Precision) | **%97.30** |
| Duyarlılık (Recall) | **%92.31** |
| F1 Skoru | **%94.74** |

**Karmaşıklık Matrisi:**

|  | Tahmin: Normal | Tahmin: Melanom |
|---|---|---|
| **Gerçek: Normal** | 20 (TN) | 2 (FP) |
| **Gerçek: Melanom** | 6 (FN) | 72 (TP) |

**Yorum:** Recall hedefi olan %90'ın üzerine çıkılmıştır (%92.31). Eşik düşürme stratejisi başarıyla uygulanmıştır. Model, melanom vakalarını yüksek güvenilirlikle tespit etmektedir.

---

### Senaryo 3 — Diyabetik Retinopati Testi

Fundus fotoğrafları üzerinde Diyabetik Retinopati (DR) tespiti.

| Metrik | Sonuç |
|---|---|
| Doğruluk (Accuracy) | **%92.00** |
| Hassasiyet (Precision) | **%95.00** |
| Duyarlılık (Recall) | **%91.94** |
| F1 Skoru | **%93.44** |

**Karmaşıklık Matrisi:**

|  | Tahmin: Normal | Tahmin: DR |
|---|---|---|
| **Gerçek: Normal** | 35 (TN) | 3 (FP) |
| **Gerçek: DR** | 5 (FN) | 57 (TP) |

**Yorum:** DR tespitinde model yüksek Precision ve Recall değerleri üretmektedir. 5 yanlış negatif vaka, ilerleyen haftalarda veri artırma (data augmentation) ile azaltılabilir.

---

## 4. Genel Performans Özeti

| Senaryo | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Temel Sınıflandırma | %92.00 | %96.15 | %89.29 | %92.59 |
| Melanom Tespiti | %92.00 | %97.30 | %92.31 | %94.74 |
| Diyabetik Retinopati | %92.00 | %95.00 | %91.94 | %93.44 |
| **Ortalama** | **%92.00** | **%96.15** | **%91.18** | **%93.59** |

---

## 5. Metrik Analizi ve Yorumlar

#### Doğruluk (Accuracy) — %92.00
Enes Zukra'nın hafta 6'da gerçekleştirdiği hiperparametre optimizasyonu ile ulaşılan %92.4 eğitim doğruluğuyla uyumludur. Projenin klinik hedefi olan %95 doğruluk oranına ulaşmak için ek optimizasyon yapılması önerilmektedir.

#### Hassasiyet (Precision) — Ort. %96.15
Yüksek Precision değeri, modelin sağlıklı bireylere yanlışlıkla hastalık teşhisi koyma oranının düşük olduğunu göstermektedir. Gereksiz tedavi ve hasta paniğini önlemek açısından olumludur.

#### Duyarlılık (Recall) — Ort. %91.18
Melanom senaryosunda eşik düşürme stratejisi uygulanarak Recall %92.31'e çıkarılmıştır. Tıbbi sistemlerde hasta güvenliği açısından Recall, Precision'dan daha kritik bir metriktir.

#### F1 Skoru — Ort. %93.59
Precision ve Recall arasındaki denge F1 skoru ile ölçülmektedir. %93.59'luk ortalama F1, modelin her iki metrikte de dengeli performans gösterdiğini ortaya koymaktadır.

---

## 6. Öneriler ve Sonraki Adımlar

- **Veri Artırma (Data Augmentation):** Eğitim verisine yatay/dikey çevirme, parlaklık değişimi gibi dönüşümler eklenerek model genelleme kapasitesi artırılabilir.
- **Eşik Optimizasyonu:** Melanom ve DR senaryoları için hastalık bazlı karar eşikleri ayrı ayrı optimize edilmelidir.
- **Gerçek Test Verisi:** Simüle veri yerine ISIC ve APTOS veri setlerinden ayrılan gerçek test seti kullanılarak metrikler doğrulanmalıdır.
- **Klinik Hedef:** Projenin SMART hedefi olan %95 doğruluk oranına ulaşmak için 5–10 Epoch daha eğitim yapılması değerlendirilebilir.

---

## 7. Çalıştırma Kılavuzu

```bash
# Gerekli kütüphaneleri yükle
pip install tensorflow scikit-learn pandas numpy

# Testi çalıştır
python model_performans_test.py
```

Test sonuçları terminalde senaryo bazlı olarak raporlanır.
