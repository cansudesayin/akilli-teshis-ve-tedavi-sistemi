from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)
app.secret_key = 'mediai-dev-secret-2026'

# ==============================================================================
# MOCK MOD — MySQL olmadan çalışabilmek için
# ==============================================================================
MOCK_MODE = True  # False yapıp aşağıdaki bağlantı bilgilerini doldurarak gerçek DB kullanabilirsiniz

def get_db_connection():
    if MOCK_MODE:
        return None
    import mysql.connector
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sifre",
        database="mediai_db"
    )

# ==============================================================================
# MOCK VERİ
# ==============================================================================
MOCK_PATIENTS = [
    {"hasta_id": "P-9821", "yas": 45, "cinsiyet": "Kadın", "diyabet": True, "tip": "Dermatoloji", "oncelik": "Yüksek"},
    {"hasta_id": "P-9825", "yas": 62, "cinsiyet": "Erkek", "diyabet": False, "tip": "Oftalmoloji", "oncelik": "Normal"},
    {"hasta_id": "P-9829", "yas": 38, "cinsiyet": "Kadın", "diyabet": False, "tip": "Dermatoloji", "oncelik": "Normal"},
]

MOCK_ANALIZ_SONUCU = {
    "hata": False,
    "analiz_id": 5001,
    "teshis": "Malign Melanom Şüphesi (Cilt Kanseri)",
    "risk_skoru": 87.0,
    "evre": "Evre II",
    "icd_kodu": "C43.9",
    "ai_aciklamasi": "Lezyon sınırlarında asimetri tespit edildi. ABCD kriterlerine göre yüksek risk skoru.",
    "bulgular": [
        {"bulgu": "Asimetri Tespiti", "guven": 92, "konum": "Sol üst kadran", "boyut": "8.2mm"},
        {"bulgu": "Kenar Düzensizliği", "guven": 88, "konum": "Merkezi bölge", "boyut": "4.5mm"},
    ],
    "diferansiyel": [
        {"teshis": "Bazal Hücreli Karsinom", "oran": 12},
        {"teshis": "Seborrheic Keratosis", "oran": 8},
        {"teshis": "Displastik Nevüs", "oran": 5},
    ],
    "zaman": datetime.now().isoformat()
}

MOCK_TEDAVI = {
    "hasta_id": "P-9821",
    "teshis": "Malignant Melanoma",
    "evre": "Stage II",
    "protokol": "Active Protocol",
    "baslangic": "12 Ekim 2026",
    "sure": "12 Hafta",
    "uyum_skoru": "98.4%",
    "ilac": "Nivolumab",
    "dozaj": "240mg",
    "uygulama": "IV Infusion",
    "sikluk": "Her 2 haftada bir",
    "sonraki_randevu": "26 Ekim 2026",
}

# ==============================================================================
# SAYFA ROUTE'LARI
# ==============================================================================

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email', '')
    sifre = request.form.get('sifre', '')
    uzmanlik = request.form.get('uzmanlik', 'dermatoloji')
    
    # Mock doğrulama — gerçek projede DB sorgusu
    if email and sifre:
        session['doktor'] = {'email': email, 'uzmanlik': uzmanlik, 'ad': 'Dr. Selim Yağbasan'}
        return redirect(url_for('dashboard'))
    
    return render_template('login.html', hata="Geçersiz e-posta veya şifre.")

@app.route('/dashboard')
def dashboard():
    if 'doktor' not in session and not MOCK_MODE:
        return redirect(url_for('login'))
    doktor = session.get('doktor', {'ad': 'Dr. Selim Yağbasan', 'uzmanlik': 'dermatoloji'})
    return render_template('dashboard.html', doktor=doktor, hastalar=MOCK_PATIENTS)

@app.route('/analiz')
def analiz():
    if 'doktor' not in session and not MOCK_MODE:
        return redirect(url_for('login'))
    doktor = session.get('doktor', {'ad': 'Dr. Selim Yağbasan', 'uzmanlik': 'dermatoloji'})
    return render_template('analiz.html', doktor=doktor)

@app.route('/teshis')
def teshis():
    if 'doktor' not in session and not MOCK_MODE:
        return redirect(url_for('login'))
    doktor = session.get('doktor', {'ad': 'Dr. Selim Yağbasan', 'uzmanlik': 'dermatoloji'})
    hasta_id = request.args.get('hasta_id', 'P-9821')
    return render_template('teshis.html', doktor=doktor, sonuc=MOCK_ANALIZ_SONUCU, hasta_id=hasta_id)

@app.route('/tedavi')
def tedavi():
    if 'doktor' not in session and not MOCK_MODE:
        return redirect(url_for('login'))
    doktor = session.get('doktor', {'ad': 'Dr. Selim Yağbasan', 'uzmanlik': 'dermatoloji'})
    hasta_id = request.args.get('hasta_id', 'P-9821')
    return render_template('tedavi.html', doktor=doktor, tedavi=MOCK_TEDAVI, hasta_id=hasta_id)

@app.route('/cikis')
def cikis():
    session.clear()
    return redirect(url_for('login'))

# ==============================================================================
# API ENDPOINT'LERİ
# ==============================================================================

@app.route('/api/v1/hastalar', methods=['POST'])
def hasta_kayit():
    gelen_veri = request.json
    yas = gelen_veri.get('yas')
    cinsiyet = gelen_veri.get('cinsiyet')
    
    if not yas or not cinsiyet:
        return jsonify({
            "hata": True,
            "mesaj": "Eksik zorunlu alanlar: yas, cinsiyet",
            "zaman": datetime.now().isoformat()
        }), 400

    if MOCK_MODE:
        return jsonify({
            "hata": False,
            "mesaj": "Hasta başarıyla kaydedildi. (Mock Mod)",
            "hasta_id": "P-" + str(len(MOCK_PATIENTS) + 9830),
            "zaman": datetime.now().isoformat()
        }), 201

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO Patients (age, gender, medical_history, diabetes) VALUES (%s, %s, %s, %s)"
        values = (yas, cinsiyet, gelen_veri.get('gecmis', ''), gelen_veri.get('diyabet', False))
        cursor.execute(sql, values)
        conn.commit()
        h_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return jsonify({
            "hata": False,
            "mesaj": "Hasta başarıyla MySQL veritabanına kaydedildi.",
            "hasta_id": str(h_id),
            "zaman": datetime.now().isoformat()
        }), 201
    except Exception as e:
        return jsonify({"hata": True, "mesaj": f"DB Hatası: {str(e)}"}), 500

@app.route('/api/v1/analiz/baslat', methods=['POST'])
def analiz_baslat():
    gelen_veri = request.json or {}
    hasta_id = gelen_veri.get('hasta_id', 'BILINMIYOR')
    return jsonify({
        "hata": False,
        "mesaj": f"{hasta_id} ID'li hasta için analiz başlatıldı.",
        "analiz_durumu": "İşleniyor",
        "analiz_id": 5001,
        "zaman": datetime.now().isoformat()
    }), 202

@app.route('/api/v1/analiz/sonuc/<int:analiz_id>', methods=['GET'])
def sonuc_getir(analiz_id):
    return jsonify({
        "hata": False,
        "analiz_id": analiz_id,
        **MOCK_ANALIZ_SONUCU
    }), 200

@app.route('/api/v1/hastalar', methods=['GET'])
def hasta_listesi():
    return jsonify({
        "hata": False,
        "hastalar": MOCK_PATIENTS,
        "toplam": len(MOCK_PATIENTS)
    }), 200

@app.errorhandler(404)
def sayfa_bulunamadi(e):
    return jsonify({"hata": True, "mesaj": "Geçersiz endpoint adresi!"}), 404

if __name__ == '__main__':
    print("=" * 60)
    print("  Siber Şifacılar — MediAI Sistemi Başlatılıyor...")
    print(f"  Mock Mod: {'AKTİF' if MOCK_MODE else 'KAPALI (MySQL gerekli)'}")
    print("  URL: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)