import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def verify_and_load_medical_data(image_path, target_size=(224, 224)):
    """
    Siber Şifacılar Projesi - Hafta 2: Tıbbi Görüntü Yükleme ve Ön Kontrol Sistemi
    Geliştirici: Enes Zukra
    
    Bu fonksiyon, yüklenen X-Ray/MRI görüntülerinin sisteme uygunluğunu denetler
    		...ve CNN modeline girmeden önceki ilk hazırlık aşamasını gerçekleştirir.
    """
    print(f"🔄 [Hafta 2] Görüntü Kontrol Ediliyor: {image_path}")
    
    # 1. Dosya varlık kontrolü
    if not os.path.exists(image_path):
        print("❌ HATA: Belirtilen yolda tıbbi görüntü bulunamadı!")
        return None
        
    try:
        # 2. Görüntüyü hedef boyutta yükleme (Hafta 4'teki CNN girişi için 224x224)
        img = load_img(image_path, target_size=target_size)
        
        # 3. Görüntüyü Diziye (Array) Çevirme
        img_array = img_to_array(img)
        
        # 4. Piksel Değerlerini Normalize Etme (0-255 arasından 0-1 arasına)
        img_array_normalized = img_array / 255.0
        
        # 5. Boyut Genişletme (Batch Dimension Ekleme)
        final_data = np.expand_dims(img_array_normalized, axis=0)
        
        print("✅ Görüntü Başarıyla Doğrulandı ve Model Girişine Hazır Hale Getirildi.")
        print(f"📊 Veri Boyutu (Shape): {final_data.shape} -> (Batch, Yükseklik, Genişlik, Kanal)")
        
        return final_data
        
    except Exception as e:
        print(f"❌ Görüntü işlenirken bir hata oluştu: {str(e)}")
        return None

if __name__ == "__main__":
    print("=== Siber Şifacılar - Hafta 2 Veri Giriş Testi ===")
    # Bu kısım test amaçlıdır, simüle edilmiş bir dosya yolu kontrol edilir
    sample_image = "test_xray_image.png"
    verify_and_load_medical_data(sample_image)
