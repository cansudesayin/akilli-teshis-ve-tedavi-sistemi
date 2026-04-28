import tensorflow as tf
from tensorflow.keras import layers, models

def create_medical_diagnosis_model():
    """
    Siber Şifacılar Projesi - Temel Hastalık Teşhis Modeli
    Geliştirici: Enes Zukra (Hafta 4 Görevi)
    """
    # CNN Model Mimarisi Oluşturma
    model = models.Sequential([
        # İlk Evrişim Katmanı: Görüntü özelliklerini yakalar
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((2, 2)),

        # İkinci Evrişim Katmanı: Daha derin özellikler için
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),

        # Üçüncü Evrişim Katmanı
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),

        # Sınıflandırma Katmanları
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5), # Overfitting'i önlemek için
        layers.Dense(1, activation='sigmoid') # İkili Sınıflandırma sonucu
    ])

    # Modelin derlenmesi (Kayıp fonksiyonu ve Optimizasyon)
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    return model

if __name__ == "__main__":
    # Test ve Özet Gösterimi
    model = create_medical_diagnosis_model()
    model.summary()
    print("\n✅ Temel Teşhis Modeli Başarıyla Oluşturuldu ve Doğrulandı.")
