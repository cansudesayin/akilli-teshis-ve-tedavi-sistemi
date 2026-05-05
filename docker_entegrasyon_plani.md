# 🐳 Hafta 3: Docker Entegrasyon ve Konteynerizasyon Planı

**Yapılan Çalışmaların Özeti:**
Akıllı Teşhis ve Tedavi Sistemi'nin farklı platformlarda (geliştirme, test, üretim) tutarlı çalışmasını sağlamak amacıyla mikroservis mimarisine uygun bir Docker entegrasyon planı tasarlanmıştır.

**Konteyner Mimarisi ve Dockerfile Yapılandırmaları:**
*   **Flask API ve ML Servisi:** CNN modeli tahminlemeleri ve backend işlemleri için, yapay zeka kütüphanelerini içeren optimize edilmiş bir `Dockerfile` tasarlanmıştır.
*   **Web Arayüzü:** Kullanıcı etkileşimini sağlayan arayüz için hafif bir web sunucusu (örn. Nginx) imajı yapılandırılmıştır.
*   **Veritabanı Servisi:** MySQL veritabanı için veri kaybını önlemek adına Docker Volumes ayarları tanımlanmıştır.

**Orkestrasyon ve Ortam Yönetimi (Docker Compose):**
*   Bağımsız konteynerler `docker-compose.yml` çatısı altında birleştirilmiştir. Web, API ve DB konteynerleri kapalı bir sanal ağ (network) üzerinden haberleşmektedir.
*   **Ortam Ayrımı:** Test ortamları için `docker-compose.override.yml` ile esnek geliştirme aktif edilirken, üretim ortamı için minimize edilmiş imajlar planlanmıştır. 
*   **Güncelleme:** Kesinti yaşanmaması için Docker imajlarının versiyonlanarak (image tagging) Docker Hub üzerinden güncellenmesi stratejisi oluşturulmuştur.