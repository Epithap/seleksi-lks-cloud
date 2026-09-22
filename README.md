# Starter Kit - Soal Praktik AWS

Isi folder ini:

- `app/app.py` - Aplikasi Flask (materi 10)
- `app/requirements.txt` - dependency Python
- `app/Dockerfile` - untuk containerize aplikasi
- `.github/workflows/deploy.yml` - workflow GitHub Actions build & push image ke **GitHub Container Registry (GHCR)** (materi 9)
- `scripts/verify_1_7.sh` - script verifikasi otomatis materi 1-7, dijalankan di AWS CloudShell
- `scripts/verify_9_10.sh` - panduan verifikasi manual materi 9-10, dijalankan di AWS CloudShell

Detail lengkap soal, konsep, requirement teknis, dan cara verifikasi ada di dokumen
"Soal Praktik AWS - Deployment Aplikasi Web Scalable.docx".

Cara membangun infrastrukturnya (security group, IAM role, launch template, ALB, ASG,
CloudWatch, dst) sengaja TIDAK disediakan sebagai command siap pakai — itu bagian dari
yang harus dikerjakan/diuji dari peserta, sesuai spesifikasi di bab **Detail Service**
dan **Appendix** pada dokumen soal.

## Sebelum mulai, siswa WAJIB mengganti:

1. `PREFIX` di semua nama resource AWS (EC2, ASG, ALB, RDS, S3 bucket, alarm, SNS topic)
  dengan identitas masing-masing, contoh: `budi`, `anisa123`, dst.
2. `PREFIX` di bagian atas `scripts/verify_1_7.sh`.
3. `GHCR_OWNER`, `PREFIX`, `ALB_NAME` di bagian atas `scripts/verify_9_10.sh`.

## Catatan penting

- **Default VPC**: seluruh resource dibuat di Default VPC bawaan akun, tidak perlu membuat VPC/subnet baru.
- **IAM Role**: EC2 perlu IAM Role (instance profile) supaya bisa upload log ke S3 tanpa menyimpan access key di instance.
- **GHCR**: setelah image pertama kali berhasil di-push oleh GitHub Actions, package GHCR defaultnya **private**. Siswa wajib membuka:
  `GitHub profile -> Packages -> (nama package) -> Package settings -> Change visibility -> Public`
  supaya EC2 bisa melakukan `docker pull` tanpa perlu login/token.

Penamaan yang konsisten penting karena script `verify_1_7.sh` mencari resource berdasarkan prefix tersebut.
