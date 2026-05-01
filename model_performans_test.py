"""
Akıllı Teşhis ve Tedavi Sistemi
Model Performans Test Modülü

Sorumlu : Cansude Sayın
Tarih   : 28 Nisan 2026
Görev   : Model Performans Testlerini Gerçekleştirme (Hafta 5-6)

Bu modül, Enes Zukra'nın geliştirdiği CNN modelinin
Selim Yağbasan'ın hazırladığı ön işleme pipeline'ı
kullanılarak farklı senaryolarda test edilmesini sağlar.
"""

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
import tensorflow as tf
from tensorflow.keras import layers, models

# ==============================================================================
# ENES'İN MODELİ — model.py dosyasından import edilecek
# Şimdilik modeli burada yeniden tanımlıyoruz
# [ENES İÇİN NOT]: model ağırlıkları kaydedildiğinde aşağıdaki satırı aç:
# model = tf.keras.models.load_model('mediAI_model.h5')
# ==============================================================================
def create_medical_diagnosis_model():
    """
    Enes Zukra tarafından geliştirilen CNN modeli.
    Hafta 6'da %92.4 accuracy ile optimize edilmiştir.
    """
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=0.001,
            beta_1=0.9,
            beta_2=0.999
        ),
        loss='binary_crossentropy',
        metrics=['accuracy',
                 tf.keras.metrics.Precision(name='precision'),
                 tf.keras.metrics.Recall(name='recall')]
    )
    return model


# ==============================================================================
# SELİM'İN ÖN İŞLEME FONKSİYONU — data_preprocessing.py'den import edilecek
# [SELİM İÇİN NOT]: Bu satırı aktif et:
# from data_preprocessing import ehr_veri_temizle, optimize_memory
# ==============================================================================
def goruntu_on_isle(goruntu_dizisi):
    """
    Selim Yağbasan'ın ön işleme modülü baz alınarak
    görüntü verilerini modele hazır hale getirir.

    İşlemler:
    - 224x224 boyutuna yeniden ölçekleme
    - [0, 1] aralığına normalizasyon
    - Aykırı piksel değerlerinin baskılanması
    """
    # Normalizasyon (0-255 → 0-1)
    goruntu_dizisi = goruntu_dizisi.astype('float32') / 255.0

    # Aykırı değer baskılama (Selim'in IQR yöntemiyle uyumlu)
    alt_sinir = np.percentile(goruntu_dizisi, 1)
    ust_sinir = np.percentile(goruntu_dizisi, 99)
    goruntu_dizisi = np.clip(goruntu_dizisi, alt_sinir, ust_sinir)

    return goruntu_dizisi


# ==============================================================================
# SENARYO 1: NORMAL / ANORMAL SINIFLANDIRMA TESTİ
# ==============================================================================
def senaryo_1_temel_siniflandirma(model, test_boyutu=100):
    """
    Temel ikili sınıflandırma testi.
    Normal (0) ve Anormal (1) görüntüleri doğru sınıflandırıyor mu?

    Returns:
        dict: Accuracy, Precision, Recall, F1 sonuçları
    """
    print("\n" + "="*60)
    print("SENARYO 1: Temel Sınıflandırma Testi")
    print("="*60)

    # [NOT]: Gerçek test veri seti yüklendiğinde bu kısım değişecek:
    # test_goruntuleri = np.load('test_data/test_images.npy')
    # gercek_etiketler = np.load('test_data/test_labels.npy')

    # Simüle edilmiş test verisi (model ağırlıkları geldiğinde kaldırılacak)
    np.random.seed(42)
    test_goruntuleri = np.random.rand(test_boyutu, 224, 224, 3)
    gercek_etiketler = np.random.randint(0, 2, test_boyutu)

    # Ön işleme uygula
    test_goruntuleri = goruntu_on_isle(test_goruntuleri)

    # Model tahmini
    tahminler_ham = model.predict(test_goruntuleri, verbose=0)
    tahminler = (tahminler_ham > 0.5).astype(int).flatten()

    # Metrikler
    acc  = accuracy_score(gercek_etiketler, tahminler)
    prec = precision_score(gercek_etiketler, tahminler, zero_division=0)
    rec  = recall_score(gercek_etiketler, tahminler, zero_division=0)
    f1   = f1_score(gercek_etiketler, tahminler, zero_division=0)
    cm   = confusion_matrix(gercek_etiketler, tahminler)

    print(f"  Doğruluk  (Accuracy)  : %{acc*100:.2f}")
    print(f"  Hassasiyet (Precision): %{prec*100:.2f}")
    print(f"  Duyarlılık (Recall)   : %{rec*100:.2f}")
    print(f"  F1 Skoru              : %{f1*100:.2f}")
    print(f"\n  Karmaşıklık Matrisi:")
    print(f"  {cm}")

    return {"senaryo": "Temel Sınıflandırma",
            "accuracy": acc, "precision": prec,
            "recall": rec, "f1": f1, "confusion_matrix": cm.tolist()}


# ==============================================================================
# SENARYO 2: MELANOM TESPİT TESTİ (Yüksek Riskli)
# ==============================================================================
def senaryo_2_melanom_tespiti(model, test_boyutu=100):
    """
    Melanom görüntülerinde yüksek Recall kritik önemdedir.
    Yanlış negatif (hasta kişiye 'sağlıklı' demek) kabul edilemez.

    Hedef: Recall > %90
    """
    print("\n" + "="*60)
    print("SENARYO 2: Melanom Tespit Testi (Yüksek Öncelikli)")
    print("="*60)

    # Melanom ağırlıklı simüle veri (%70 pozitif)
    np.random.seed(7)
    test_goruntuleri = np.random.rand(test_boyutu, 224, 224, 3)
    gercek_etiketler = np.random.choice([0, 1], test_boyutu, p=[0.3, 0.7])

    test_goruntuleri = goruntu_on_isle(test_goruntuleri)
    tahminler_ham = model.predict(test_goruntuleri, verbose=0)

    # Melanom tespitinde eşik düşürülür: 0.5 → 0.35
    # Yanlış negatifi minimize etmek için
    esik = 0.35
    tahminler = (tahminler_ham > esik).astype(int).flatten()

    acc  = accuracy_score(gercek_etiketler, tahminler)
    prec = precision_score(gercek_etiketler, tahminler, zero_division=0)
    rec  = recall_score(gercek_etiketler, tahminler, zero_division=0)
    f1   = f1_score(gercek_etiketler, tahminler, zero_division=0)
    cm   = confusion_matrix(gercek_etiketler, tahminler)

    print(f"  Karar Eşiği           : {esik}")
    print(f"  Doğruluk  (Accuracy)  : %{acc*100:.2f}")
    print(f"  Hassasiyet (Precision): %{prec*100:.2f}")
    print(f"  Duyarlılık (Recall)   : %{rec*100:.2f}")
    print(f"  F1 Skoru              : %{f1*100:.2f}")
    print(f"\n  Karmaşıklık Matrisi:")
    print(f"  {cm}")

    hedef = "✅ BAŞARILI" if rec >= 0.90 else "⚠️ GELİŞTİRİLMELİ"
    print(f"\n  Recall Hedefi (>%90): {hedef}")

    return {"senaryo": "Melanom Tespiti",
            "esik": esik, "accuracy": acc,
            "precision": prec, "recall": rec,
            "f1": f1, "confusion_matrix": cm.tolist()}


# ==============================================================================
# SENARYO 3: DİYABETİK RETİNOPATİ TESTİ
# ==============================================================================
def senaryo_3_diyabetik_retinopati(model, test_boyutu=100):
    """
    Diyabetik Retinopati evrelendirme testi.
    0: Sağlıklı, 1: DR tespit edildi
    """
    print("\n" + "="*60)
    print("SENARYO 3: Diyabetik Retinopati Testi")
    print("="*60)

    np.random.seed(21)
    test_goruntuleri = np.random.rand(test_boyutu, 224, 224, 3)
    gercek_etiketler = np.random.choice([0, 1], test_boyutu, p=[0.4, 0.6])

    test_goruntuleri = goruntu_on_isle(test_goruntuleri)
    tahminler_ham = model.predict(test_goruntuleri, verbose=0)
    tahminler = (tahminler_ham > 0.5).astype(int).flatten()

    acc  = accuracy_score(gercek_etiketler, tahminler)
    prec = precision_score(gercek_etiketler, tahminler, zero_division=0)
    rec  = recall_score(gercek_etiketler, tahminler, zero_division=0)
    f1   = f1_score(gercek_etiketler, tahminler, zero_division=0)
    cm   = confusion_matrix(gercek_etiketler, tahminler)

    print(f"  Doğruluk  (Accuracy)  : %{acc*100:.2f}")
    print(f"  Hassasiyet (Precision): %{prec*100:.2f}")
    print(f"  Duyarlılık (Recall)   : %{rec*100:.2f}")
    print(f"  F1 Skoru              : %{f1*100:.2f}")
    print(f"\n  Karmaşıklık Matrisi:")
    print(f"  {cm}")

    return {"senaryo": "Diyabetik Retinopati",
            "accuracy": acc, "precision": prec,
            "recall": rec, "f1": f1,
            "confusion_matrix": cm.tolist()}


# ==============================================================================
# SONUÇLARI RAPORLA
# ==============================================================================
def sonuclari_raporla(tum_sonuclar):
    """
    Tüm senaryo sonuçlarını özetler ve karşılaştırır.
    """
    print("\n" + "="*60)
    print("GENEL PERFORMANS ÖZET RAPORU")
    print("="*60)
    print(f"{'Senaryo':<30} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
    print("-"*60)
    for s in tum_sonuclar:
        print(
            f"{s['senaryo']:<30}"
            f"{s['accuracy']*100:>9.2f}%"
            f"{s['precision']*100:>9.2f}%"
            f"{s['recall']*100:>9.2f}%"
            f"{s['f1']*100:>9.2f}%"
        )
    print("="*60)

    # Ortalama metrikler
    ort_acc  = np.mean([s['accuracy']  for s in tum_sonuclar])
    ort_prec = np.mean([s['precision'] for s in tum_sonuclar])
    ort_rec  = np.mean([s['recall']    for s in tum_sonuclar])
    ort_f1   = np.mean([s['f1']        for s in tum_sonuclar])

    print(f"\n  Ortalama Accuracy  : %{ort_acc*100:.2f}")
    print(f"  Ortalama Precision : %{ort_prec*100:.2f}")
    print(f"  Ortalama Recall    : %{ort_rec*100:.2f}")
    print(f"  Ortalama F1        : %{ort_f1*100:.2f}")


# ==============================================================================
# ANA ÇALIŞTIRICI
# ==============================================================================
if __name__ == "__main__":
    print("="*60)
    print("  MediAI — Model Performans Test Modülü")
    print("  Sorumlu: Cansude Sayın | 28 Nisan 2026")
    print("="*60)

    # Modeli yükle
    print("\n  Model yükleniyor...")
    model = create_medical_diagnosis_model()
    print("  Model hazır.")

    # Testleri çalıştır
    sonuclar = []
    sonuclar.append(senaryo_1_temel_siniflandirma(model))
    sonuclar.append(senaryo_2_melanom_tespiti(model))
    sonuclar.append(senaryo_3_diyabetik_retinopati(model))

    # Özet rapor
    sonuclari_raporla(sonuclar)

    print("\n✅ Tüm testler tamamlandı.")
    print("   Detaylı rapor: model_performans_raporu.md")
