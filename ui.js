
// --- AUTH GUARD ---
(function() {
    var path = window.location.pathname;
    if (path && path.indexOf('login') === -1 && path.indexOf('index.html') === -1 && !path.endsWith('/')) {
        if(localStorage.getItem('isLoggedIn') !== 'true') {
            window.location.href = 'mediAI_login_v2.html';
        }
    }
})();

window.logoutSystem = function(event) {
    if(event) event.preventDefault();
    localStorage.removeItem('isLoggedIn');
    window.location.href = 'mediAI_login_v2.html';
};
// ------------------

document.addEventListener('DOMContentLoaded', function() {
  var t = document.createElement('div');
  t.id = 'global-toast';
  document.body.appendChild(t);
});

function showGlobalToast(msg, type) {
  var t = document.getElementById('global-toast');
  if(!t) return;
  t.innerHTML = (type === 'success' ? '✅ ' : '') + msg;
  t.className = type ? 'show ' + type : 'show';
  setTimeout(function(){ t.className = t.className.replace('show', '').trim(); }, 3500);
}

window.simBtn = function(event, msg, redirect) {
  if (event) event.preventDefault();
  var btn = event.currentTarget || event.target;
  if(btn.dataset.loading) return;
  btn.dataset.loading = 'true';
  
  var orig = btn.innerHTML;
  btn.style.width = btn.offsetWidth + 'px'; 
  btn.innerHTML = '<span class="spinner-btn"></span>';
  btn.style.opacity = '0.85';
  btn.style.pointerEvents = 'none';
  btn.style.justifyContent = 'center';

  setTimeout(function() {
    btn.innerHTML = orig;
    btn.style.width = '';
    btn.style.opacity = '1';
    btn.style.pointerEvents = 'auto';
    delete btn.dataset.loading;
    showGlobalToast(msg, 'success');
    if (redirect) setTimeout(function(){ window.location.href = redirect; }, 1500);
  }, 1200);
}

// Gerçek Fonksiyonlar (Sahte uyarilar yerine)
window.downloadFile = function(event, filename, content) {
    if(event) event.preventDefault();
    var btn = event.currentTarget || event.target;
    
    // Spinner baslat
    var orig = btn.innerHTML;
    btn.style.width = btn.offsetWidth + 'px'; 
    btn.innerHTML = '<span class="spinner-btn"></span>';
    btn.style.opacity = '0.85';
    btn.style.pointerEvents = 'none';
    btn.style.justifyContent = 'center';

    setTimeout(function() {
        // Dosyayi indir
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(content));
        element.setAttribute('download', filename);
        element.style.display = 'none';
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);

        // Butonu eski haline getir
        btn.innerHTML = orig;
        btn.style.width = '';
        btn.style.opacity = '1';
        btn.style.pointerEvents = 'auto';
        showGlobalToast('Dosya indirildi: ' + filename, 'success');
    }, 800);
};

window.printPage = function(event) {
    if(event) event.preventDefault();
    showGlobalToast('Yazdırma hazırlanıyor...', 'success');
    setTimeout(function() {
        window.print();
    }, 500);
};

window.saveStateAndRedirect = function(event, key, value, msg, redirect) {
    if(event) event.preventDefault();
    var btn = event.currentTarget || event.target;
    var orig = btn.innerHTML;
    btn.style.width = btn.offsetWidth + 'px'; 
    btn.innerHTML = '<span class="spinner-btn"></span>';
    btn.style.opacity = '0.85';
    btn.style.pointerEvents = 'none';
    btn.style.justifyContent = 'center';

    setTimeout(function() {
        localStorage.setItem(key, value);
        showGlobalToast(msg, 'success');
        if(redirect) {
            setTimeout(function() { window.location.href = redirect; }, 1000);
        } else {
            btn.innerHTML = orig;
            btn.style.width = '';
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
        }
    }, 600);
};


// --- Geri Kalan Tüm Gerçek Fonksiyonlar ---
window.copyToClipboard = function(event) {
    if(event) event.preventDefault();
    var dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = "Hasta Teşhis Raporu: Şüpheli Nodül (8.2mm, %87 Risk). Detaylı analiz sisteme kaydedildi.";
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
    showGlobalToast("Rapor panoya kopyalandı.", "success");
};

window.printRapor = function(event) {
    if(event) event.preventDefault();
    showGlobalToast("Yazdırma hazırlanıyor...", "success");
    setTimeout(function() { window.print(); }, 500);
};

window.printProfil = function(event) {
    if(event) event.preventDefault();
    showGlobalToast("Profil yazdırmaya hazırlanıyor...", "success");
    setTimeout(function() { window.print(); }, 500);
};

window.downloadPDF = function(event) {
    if(event) event.preventDefault();
    // Use the existing downloadFile function
    if(typeof window.downloadFile === 'function') {
        window.downloadFile(null, 'Teshis_Raporu.pdf', '%PDF-1.4\n%DUMMY_PDF_CONTENT\nTeşhis Raporu PDF formatında oluşturuldu.');
    } else {
        showGlobalToast("PDF oluşturuldu ve indirildi.", "success");
    }
};

window.exportCSV = function(event) {
    if(event) event.preventDefault();
    var csvContent = "Hasta Adı,Yas,Cinsiyet,Kan Grubu,Alerjiler\nAhmet Yıldız,48,Erkek,A Rh(+),Penisilin";
    if(typeof window.downloadFile === 'function') {
        window.downloadFile(null, 'Hasta_Verileri.csv', csvContent);
    }
};

window.exportJSON = function(event) {
    if(event) event.preventDefault();
    var jsonContent = '{"hasta": {"ad": "Ahmet Yıldız", "yas": 48, "cinsiyet": "Erkek", "kan_grubu": "A Rh(+)", "alerjiler": ["Penisilin"]}}';
    if(typeof window.downloadFile === 'function') {
        window.downloadFile(null, 'Hasta_Verileri.json', jsonContent);
    }
};
// ------------------------------------------
