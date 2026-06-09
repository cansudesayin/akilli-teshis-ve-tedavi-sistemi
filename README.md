# akilli-teshis-ve-tedavi-sistemi
Makine öğrenimi algoritmaları kullanarak tıbbi görüntüleri analiz eden, hastalıkları erken teşhis eden ve kişiselleştirilmiş tedavi önerileri sunan bir sistem geliştirilmesi.

# MediAI — Akıllı Teşhis ve Tedavi Sistemi

Makine öğrenimi algoritmaları kullanarak tıbbi görüntüleri analiz eden, hastalıkları erken teşhis eden ve kişiselleştirilmiş tedavi önerileri sunan klinik karar destek sistemi.

## Hakkında

MediAI, dermatoloji (Malign Melanom) ve oftalmoloji (Diyabetik Retinopati) alanlarındaki tıbbi görüntüleri hastanın EHR verileriyle birleştirerek analiz eden yapay zeka tabanlı bir web uygulamasıdır. Sistem, doktorlara açıklanabilir teşhis kanıtları ve kişiselleştirilmiş tedavi takvimi sunar.

## Özellikler

- DICOM görüntü yükleme ve AI destekli analiz
- CNN modeli ile %92.4 doğruluk oranı
- ICD-10 kodlu teşhis ve ayırıcı tanı
- Kişiselleştirilmiş tedavi planı ve faz takibi
- Hasta profili ve EHR entegrasyonu
- Swagger UI API dokümantasyonu
- Dark Mode desteği

## Teknolojiler

- **Backend:** Python, Flask
- **AI/ML:** TensorFlow, Keras (CNN), OpenCV
- **Veritabanı:** MySQL
- **Frontend:** HTML5, CSS3, JavaScript
- **Güvenlik:** 256-bit TLS, RBAC, MFA

## Kurulum

```bash
git clone https://github.com/cansudesayin/akilli-teshis-ve-tedavi-sistemi
cd akilli-teshis-ve-tedavi-sistemi
pip install -r requirements.txt
python app.py
```

Uygulama `http://localhost:5000` adresinde çalışır.

## Demo

https://cansudesayin.github.io/akilli-teshis-ve-tedavi-sistemi/

> Statik ön yüz demosu — backend ve veritabanı bağlı değildir.

## Ekip — Siber Şifacılar

| İsim | Rol |
|---|---|
| Cansude Sayın | Proje Yöneticisi, API & Arayüz |
| Ali İstanbullu | Backend, MySQL, Deploy |
| Enes Zukra | ML Model, CNN |
| Selim Yağbasan | Veri İşleme |
| Edanur Yasak | Veritabanı, Swagger |

## Lisans

Fırat Üniversitesi — Yazılım Mühendisliği Temelleri Dersi — 2026
