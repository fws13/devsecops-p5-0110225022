# Notes API (devsecops-p5-NIM)

## 1. Nama & Fungsi Aplikasi
**Notes API** adalah REST API sederhana untuk mengelola catatan mahasiswa
(membuat, melihat, menghapus, dan meringkas catatan).

## 2. Bahasa & Framework
- Python 3.11
- Flask (web framework)
- Pytest (unit testing)
- Bandit (SAST)

## 3. Cara Menjalankan
    pip install -r requirements.txt
    python -m app.main
Aplikasi berjalan di http://127.0.0.1:5000

Menjalankan test:
    python -m pytest tests/ -v

Contoh endpoint: `GET /notes`, `POST /notes`, `GET /notes/<id>`,
`DELETE /notes/<id>`, `GET /summaries`.

## 4. Overview Pipeline CI/CD
Workflow `.github/workflows/devsecops.yml` terpicu pada push dan pull request
ke branch `main`:
1. **build**: install dependencies dan menjalankan unit test (pytest).
2. **sast-scan** (needs: build): memindai kode dengan Bandit.
   **Quality Gate**: pipeline gagal bila ditemukan isu severity HIGH.
   Laporan JSON diunggah sebagai artifact.
