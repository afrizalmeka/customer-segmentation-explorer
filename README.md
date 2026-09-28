# Customer Segmentation Explorer

Mini Project Sesi 15 (Python Programming for AI - Batch 8) - Project 3 dari 5 opsi. Mengelompokkan pelanggan berdasarkan pendapatan tahunan dan spending score memakai K-Means, dengan slider jumlah cluster (K) yang mengubah visualisasi secara **real-time**.

Cocok untuk peserta dengan latar belakang: marketing, retail, atau yang suka eksplorasi visual. Tanpa LLM - output sangat visual dan mudah dipresentasikan.

## Status

Aplikasi ini **sudah 100% jadi** dan siap dijalankan langsung. Cocok dipakai sebagai referensi belajar: baca `app.py` untuk lihat bagaimana K-Means (Sesi 11) digabung dengan Streamlit (Sesi 14) untuk visualisasi real-time.

Efek "real-time" didapat gratis dari cara kerja Streamlit: setiap kali slider digeser, seluruh skrip dijalankan ulang dari atas, termasuk baris `KMeans(n_clusters=k, ...)` - jadi model otomatis dilatih ulang dengan K terbaru tanpa kode tambahan.

## Struktur Folder

```
customer-segmentation-explorer/
├── app.py                  # Streamlit - dashboard (skeleton, ada TODO)
├── mall_customers.csv      # Dataset asli dari Sesi 11
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalasi

Gunakan virtual environment agar paket project ini tidak bentrok dengan paket Python lain yang sudah terpasang di sistem kamu (mis. error `command not found: streamlit` atau `ImportError` pada scipy/sklearn biasanya disebabkan oleh instalasi global yang tercampur):

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Menjalankan

Setelah semua TODO diisi:

```bash
source .venv/bin/activate      # jika belum aktif
streamlit run app.py
```

## Troubleshooting

- **`zsh: command not found: streamlit`** — venv belum diaktifkan, atau instalasi sebelumnya masuk ke `~/Library/Python/...` yang tidak ada di PATH. Aktifkan venv (`source .venv/bin/activate`) lalu jalankan lagi, atau jalankan sementara dengan `python3 -m streamlit run app.py`.
- **`ImportError` dari `scipy/sparse/linalg/_propack/...`** — biasanya wheel scipy yang ter-install rusak/tidak cocok dengan arsitektur CPU (Apple Silicon vs Intel). Perbaiki dengan menginstal ulang di dalam venv:
  ```bash
  pip uninstall -y scipy numpy
  pip install --no-cache-dir numpy scipy
  ```
- Pastikan `python3 -c "import platform; print(platform.machine())"` dan `uname -m` menunjukkan arsitektur yang sama. Jika berbeda, Python kamu berjalan dalam mode emulasi (Rosetta) — install ulang Python versi native untuk arsitektur mesin kamu.

## Konteks

Bagian dari Sesi 15 - Mini Project: Connecting the Dots, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan Sesi 6 (SQLite), Sesi 11 (K-Means Clustering), dan Sesi 14 (Streamlit deployment).
