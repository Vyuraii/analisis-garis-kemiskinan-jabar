# 📊 Dashboard Analisis Garis Kemiskinan Jawa Barat

Dashboard interaktif berbasis **Streamlit** untuk memvisualisasikan tren dan perbandingan garis kemiskinan per kapita di seluruh Kabupaten/Kota di Provinsi Jawa Barat dari tahun **2004** hingga **2025**.

## ✨ Fitur

- **KPI Cards** — Menampilkan nilai garis kemiskinan tertinggi, rata-rata, dan total data secara dinamis sesuai filter
- **Tren Per Tahun** — Grafik garis interaktif untuk membandingkan tren antar wilayah dari waktu ke waktu
- **Perbandingan Antar Wilayah** — Bar chart horizontal untuk melihat posisi relatif setiap Kabupaten/Kota pada tahun tertentu
- **Filter Dinamis** — Slider rentang tahun dan multiselect Kabupaten/Kota di sidebar
- **Tabel Data Mentah** — Ekspander berisi data lengkap yang bisa disalin atau dianalisis lebih lanjut
- **Desain Dark Mode** — Tema biru navy profesional dengan custom CSS

---

## 🗂️ Struktur Proyek

```
📁 dashboard-kemiskinan-jabar/
├── dashboard.py                          # File utama aplikasi Streamlit
├── bps-od_20003_garis_kemiskinan_...csv  # Dataset BPS Jawa Barat
├── requirements.txt                      # Daftar dependensi Python
└── README.md                             # Dokumentasi ini
```

---

## 🚀 Cara Menjalankan

### 1. Clone repositori

```bash
git clone https://github.com/username/dashboard-kemiskinan-jabar.git
cd dashboard-kemiskinan-jabar
```

### 2. Buat virtual environment (opsional tapi disarankan)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi

```bash
streamlit run dashboard.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`

---

## 📦 Dependensi

| Library | Versi Minimum | Fungsi |
|---|---|---|
| `streamlit` | 1.30.0 | Framework web app |
| `pandas` | 2.0.0 | Pengolahan data |
| `plotly` | 5.18.0 | Visualisasi interaktif |

Buat file `requirements.txt` dengan isi:

```
streamlit>=1.30.0
pandas>=2.0.0
plotly>=5.18.0
```

---

## 📂 Sumber Data

Data bersumber dari **Badan Pusat Statistik (BPS) Jawa Barat** melalui portal Open Data Jabar:

- **Nama dataset:** Garis Kemiskinan Berdasarkan Kabupaten/Kota
- **Kode dataset:** `bps-od_20003`
- **Cakupan:** 27 Kabupaten/Kota di Provinsi Jawa Barat
- **Periode:** 2004 – 2025
- **Satuan:** Rupiah per kapita per bulan

---

## 🖥️ Tampilan Dashboard

| Komponen | Deskripsi |
|---|---|
| Header | Banner judul dengan label Live dan sumber data |
| KPI Cards | 3 kartu metrik utama (tertinggi, rata-rata, total data) |
| Line Chart | Tren garis kemiskinan per tahun per wilayah |
| Bar Chart | Perbandingan antar wilayah pada tahun akhir filter |
| Data Table | Tabel mentah dengan format angka Rupiah |

---

## 🤝 Kontribusi

Kontribusi sangat terbuka! Silakan:

1. Fork repositori ini
2. Buat branch fitur baru (`git checkout -b fitur/nama-fitur`)
3. Commit perubahan (`git commit -m 'Tambah fitur X'`)
4. Push ke branch (`git push origin fitur/nama-fitur`)
5. Buat Pull Request

---

## 📄 Lisensi

Proyek ini menggunakan lisensi **MIT**. Data yang digunakan merupakan data publik dari BPS Jawa Barat.

---

<div align="center">
  Dibuat dengan ❤️ menggunakan Streamlit &nbsp;|&nbsp; Data: BPS Jawa Barat
</div>
