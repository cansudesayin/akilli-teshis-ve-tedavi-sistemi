# MediAI - Akıllı Teşhis ve Tedavi Sistemi Proje Dokümantasyonu

## [cite_start]1. Proje Özeti ve Sunum İçeriği [cite: 1, 5]
[cite_start]**Sorumlu:** Ali İstanbullu (Yazılım Mühendisi) [cite: 3] | [cite_start]**Tarih:** 26 Nisan 2026 [cite: 4]

* [cite_start]**Problem:** Cilt (Malign Melanom) ve göz (Diyabetik Retinopati) hastalıklarının erken teşhisindeki zorluklar ve raporlama süreçlerinin uzunluğu[cite: 7].
* [cite_start]**Çözüm:** Tıbbi görüntüleri (OCT, dermoskopik) ve hasta geçmişini (EHR) saniyeler içinde analiz eden "Çok Modlu Klinik Karar Destek Sistemi"[cite: 8].
* [cite_start]**Teknolojiler:** TensorFlow/Keras ile CNN, OpenCV, Python Flask, MySQL, HTML/CSS/JS[cite: 10, 11, 12, 13, 14].
* [cite_start]**Performans:** Model %85 doğruluk oranına ulaşmış olup, raporlama süresinin hasta başına %60 oranında azaltılması öngörülmektedir[cite: 16].
* [cite_start]**Demo Akışı:** Doktor şifreli giriş yapar, görüntüyü yükler, `POST /api/v1/analiz/baslat` uç noktasına veri gönderilir, CNN modeli Güven Skoru hesaplar ve sonuç MySQL'e kaydedilir[cite: 18, 19, 21, 22, 23].

---

## [cite_start]2. Tıbbi Görüntü Veri Seti ve Ön İşleme Stratejisi [cite: 26, 30]
[cite_start]**Sorumlu:** Selim Yağbasan [cite: 29] | [cite_start]**Tarih:** 5 Mayıs 2026 [cite: 28]

* [cite_start]**Veri Profili:** Röntgen, MR, BT görüntüleri ağırlıklı olarak DICOM, PNG/JPEG ve NIFTI formatlarındadır[cite: 33, 34]. [cite_start]Orijinal çözünürlükler 512x512 ile 4K arasında değişmektedir[cite: 35].
* [cite_start]**Sorunlar:** Tıbbi cihaz artefaktları, sınıf dengesizliği ve aşırı parlak/karanlık çekimler[cite: 38].
* [cite_start]**Yeniden Boyutlandırma:** Donanım optimizasyonu (RAM/VRAM) için görüntüler 224x224 veya 256x256 piksele standardize edilecek ve gereksiz boşluklar kırpılacaktır[cite: 42, 43, 44, 45].
* [cite_start]**Gürültü ve Kontrast:** Doku sınırlarını koruyan filtreler uygulanacak ve detaylar için CLAHE tekniği ile normalizasyon (Min-Max Scaling) kullanılacaktır[cite: 48, 50, 52, 53].
* [cite_start]**Veri Artırma (Data Augmentation):** Model ezberini (Overfitting) önlemek için çevirme ve hafif döndürme işlemleri eklenecektir[cite: 57, 58].

---

## [cite_start]3. Yapay Zeka Model Optimizasyonu ve Performans [cite: 67, 104]
[cite_start]**Belge:** Rapor No: SCH-AI-2024-006 [cite: 67] | [cite_start]Hafta 6 [cite: 106]

* [cite_start]**Optimizasyon Gerekçesi:** 5. Haftada eğitilen temel CNN modelinde %12.7'lik yüksek bir overfitting farkı ve yanlış öğrenme tespit edilmiştir[cite: 76, 81].
* [cite_start]**Yapılan İyileştirmeler:** Modelin tam bağlantılar (Dense) katmanından önce %50 oranında Dropout (p=0.50) eklendi ve Adam Optimizer için Öğrenme Hızı (Learning Rate) 0.01'den 0.001'e düşürüldü[cite: 86, 88].
* [cite_start]**Metrik Değişimleri:** Yapılan müdahalelerle "Test Doğruluğu" %85.0'dan %92.4'e çıkartılmış ve overfitting farkı %2.3'e düşürülerek model kararlılığı artırılmıştır[cite: 93].
* [cite_start]**Modül Optimizasyonları:** Pandas üzerinde "Downcasting" işlemi ile sayısal veriler int32/float32'ye indirilmiş (RAM yükü %50-70 azaltıldı) ve for döngüleri yerine vektörizasyon kullanılarak veri işleme hızı 10-50 kat artırılmıştır[cite: 111, 112, 114, 118, 119].

---

## [cite_start]4. Veritabanı (MySQL) Tasarımı ve SQL Yapısı [cite: 130, 131, 153]

[cite_start]Aşağıda veritabanı şemasını oluşturan temel SQL kurguları yer almaktadır[cite: 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186]:

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
import tensorflow as tf
from tensorflow.keras import layers, models

def create_medical_model():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(1, activation='sigmoid'))
    
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

    hasta_kaydi = {
    "hasta_bilgisi": {"patient_id": 1, "yas": 45, "cinsiyet": "Kadın", "genetik_risk": ["melanom", "diyabet"], "gecmis_hastaliklar": ["akne", "hipertansiyon"]},
    "teshisler": [{"hastalik": "Melanom", "evre": "Evre 1", "risk_skoru": 0.87, "tarih": "2026-03-10"}],
    "tedavi_gecmisi": [
        {"tedavi": "Krem", "etken_madde": "Retinoid", "yanit": "Orta", "sure_gun": 30},
        {"tedavi": "Lazer", "yanit": "İyi", "sure_gun": 10}
    ]
}

def tedavi_oner(hasta_kaydi):
    son_teshis = hasta_kaydi["teshisler"][-1]
    gecmis = hasta_kaydi["tedavi_gecmisi"]
    son_yanit = gecmis[-1]["yanit"]

    if son_teshis["hastalik"] == "Melanom":
        if son_yanit == "Kötü":
            return "Cerrahi müdahale önerilir"
        elif son_yanit == "Orta":
            return "İlaç değişimi önerilir"
        else:
            return "Mevcut tedaviye devam"
    elif son_teshis["hastalik"] == "Diyabetik Retinopati":
        return "Anti-VEGF tedavi planı önerilir"
    
    return "Doktor değerlendirmesi gerekli"
    from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(host="localhost", user="root", password="sifre", database="mediai_db")

@app.route('/api/v1/hastalar', methods=['POST'])
def hasta_kayit():
    gelen_veri = request.json
    yas = gelen_veri.get('yas')
    cinsiyet = gelen_veri.get('cinsiyet')

    if not yas or not cinsiyet:
        return jsonify({"hata": True, "mesaj": "Eksik zorunlu alanlar: yas, cinsiyet"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO Patients (age, gender, medical_history, diabetes) VALUES (%s, %s, %s, %s)"
        values = (yas, cinsiyet, gelen_veri.get('gecmis', ''), gelen_veri.get('diyabet', False))
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"hata": False, "mesaj": "Hasta başarıyla kaydedildi."}), 201
    except Exception as e:
        return jsonify({"hata": True, "mesaj": f"DB Hatası: {str(e)}"}), 500

@app.route('/api/v1/analiz/baslat', methods=['POST'])
def analiz_baslat():
    gelen_veri = request.json
    hasta_id = gelen_veri.get('hasta_id')
    return jsonify({
        "hata": False, 
        "mesaj": f"{hasta_id} ID'li hasta için analiz başlatıldı.", 
        "analiz_durumu": "İşleniyor"
    }), 202

@app.route('/api/v1/analiz/sonuc/', methods=['GET'])
def sonuc_getir(analiz_id):
    return jsonify({
        "hata": False,
        "analiz_id": analiz_id,
        "tehsis": "Malign Melanom (Cilt Kanseri)",
        "risk_skoru": 88.5,
        "ai_aciklamasi": "Lezyon sınırlarında asimetri tespit edildi."
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)