import socket

from flask import Flask, jsonify

app = Flask(__name__)


# TODO: Baca DB_HOST, DB_USER, DB_PASS, dan DB_NAME dari environment variable.
# Tujuannya agar credential database tidak disimpan langsung di source code.


def get_db_connection():
    # TODO: Buat koneksi ke database menggunakan konfigurasi di atas.
    # Koneksi ini diperlukan oleh endpoint utama untuk menyimpan dan membaca visit.
    raise NotImplementedError("Implementasikan koneksi database")


def init_db():
    # TODO: Buat tabel visits jika tabel tersebut belum tersedia.
    # Fungsi ini biasanya dipanggil sekali saat aplikasi mulai berjalan.
    pass


init_db()


@app.route("/health")
def health():
    """Endpoint untuk health check dari ALB Target Group."""
    return jsonify(status="ok"), 200


@app.route("/")
def index():
    hostname = socket.gethostname()

    # TODO: Simpan satu kunjungan ke database dan hitung total kunjungan.
    # Hasil hitungan nantinya dikembalikan sebagai total_visits.
    visit_count = None

    return jsonify(
        message="Halo dari Flask Training App!",
        served_by=hostname,
        total_visits=visit_count,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)