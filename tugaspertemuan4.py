KNOWLEDGE_BASE = {

    "K01": {
        "nama": "RAM Rusak / Bermasalah",
        "gejala": {"G01", "G02", "G03", "G04"},
        "solusi": (
            "1. Matikan komputer dan cabut RAM dari slotnya.\n"
            "2. Bersihkan pin RAM dengan penghapus.\n"
            "3. Pasang kembali dengan benar.\n"
            "4. Coba slot lain.\n"
            "5. Ganti RAM jika rusak."
        ),
    },

    "K02": {
        "nama": "Overheat (Prosesor Terlalu Panas)",
        "gejala": {"G05", "G06", "G07", "G08"},
        "solusi": (
            "1. Matikan komputer dan biarkan dingin.\n"
            "2. Bersihkan kipas dan heatsink.\n"
            "3. Ganti thermal paste.\n"
            "4. Pastikan ventilasi baik.\n"
            "5. Tambah kipas jika perlu."
        ),
    },

    "K03": {
        "nama": "Hardisk Corrupt / Bermasalah",
        "gejala": {"G09", "G10", "G11", "G12"},
        "solusi": (
            "1. Jalankan CHKDSK.\n"
            "2. Backup data penting.\n"
            "3. Defragmentasi HDD.\n"
            "4. Periksa bad sector.\n"
            "5. Ganti hardisk jika rusak."
        ),
    },

    "K04": {
        "nama": "VGA / Kartu Grafis Bermasalah",
        "gejala": {"G13", "G14", "G15", "G16"},
        "solusi": (
            "1. Update driver VGA.\n"
            "2. Bersihkan slot VGA.\n"
            "3. Periksa kabel.\n"
            "4. Tes di komputer lain.\n"
            "5. Ganti VGA jika rusak."
        ),
    },

    "K05": {
        "nama": "Power Supply (PSU) Lemah / Rusak",
        "gejala": {"G17", "G18", "G19", "G20"},
        "solusi": (
            "1. Periksa kabel daya.\n"
            "2. Kurangi beban listrik.\n"
            "3. Test PSU.\n"
            "4. Ganti PSU jika bermasalah.\n"
            "5. Gunakan PSU dengan watt sesuai."
        ),
    },

    "K06": {
        "nama": "Motherboard Bermasalah",
        "gejala": {"G21", "G22", "G23", "G24", "G25"},
        "solusi": (
            "1. Periksa kapasitor.\n"
            "2. Reset BIOS.\n"
            "3. Cek konektor motherboard.\n"
            "4. Bawa ke teknisi.\n"
            "5. Ganti motherboard jika rusak."
        ),
    },
}

DAFTAR_GEJALA = {

    # RAM
    "G01": "Komputer sering BSOD",
    "G02": "Komputer restart sendiri",
    "G03": "Bunyi beep saat boot",
    "G04": "Program sering crash",
    # Overheat
    "G05": "Komputer mati sendiri",
    "G06": "Kipas sangat kencang",
    "G07": "CPU sangat panas",
    "G08": "Performa menurun",
    # Hardisk
    "G09": "Booting lama",
    "G10": "Suara klik dari HDD",
    "G11": "File corrupt",
    "G12": "Disk tidak terbaca",
    # VGA
    "G13": "Layar artefak",
    "G14": "Layar blank",
    "G15": "Driver crash",
    "G16": "Resolusi tidak normal",
    # PSU
    "G17": "Tidak bisa menyala",
    "G18": "Sering mati mendadak",
    "G19": "Lampu berkedip",
    "G20": "USB tidak stabil",
    # Motherboard
    "G21": "Tidak ada tampilan",
    "G22": "Port tidak berfungsi",
    "G23": "Tanggal reset",
    "G24": "Gagal masuk BIOS",
    "G25": "Sering gagal POST",
}

SEPARATOR = "=" * 62
THIN_SEP  = "-" * 62


def cetak_header():
    print(SEPARATOR)
    print("   SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER / LAPTOP")
    print("   Metode: Forward Chaining | Knowledge Base Dictionary")
    print(SEPARATOR)
    print()


def cetak_menu_gejala():
    print(THIN_SEP)
    print(f"  {'KODE':<6}  GEJALA")
    print(THIN_SEP)
    for kode, deskripsi in DAFTAR_GEJALA.items():
        print(f"  [{kode}]  {deskripsi}")
    print(THIN_SEP)


def minta_input_gejala():
    print("\n  Masukkan kode gejala yang dialami komputer Anda.")
    print("  Pisahkan dengan koma jika lebih dari satu.")
    print("  Contoh: G01,G05,G13")
    print()

    raw = input("  >> Gejala Anda : ").strip().upper()

    if not raw:
        return set()

    kode_input = {k.strip() for k in raw.split(",")}
    valid      = kode_input & DAFTAR_GEJALA.keys()
    invalid    = kode_input - DAFTAR_GEJALA.keys()

    if invalid:
        print(f"\n Kode tidak dikenali dan diabaikan: {', '.join(sorted(invalid))}")

    return valid


def inferensi(gejala_user: set) -> list:
    hasil = []

    for kode_k, data in KNOWLEDGE_BASE.items():
        gejala_rule  = data["gejala"]
        cocok        = gejala_user & gejala_rule
        jumlah_cocok = len(cocok)

        if jumlah_cocok == 0:
            continue

        skor_persen = (jumlah_cocok / len(gejala_rule)) * 100

        hasil.append({
            "kode"       : kode_k,
            "nama"       : data["nama"],
            "solusi"     : data["solusi"],
            "cocok"      : cocok,
            "jumlah"     : jumlah_cocok,
            "total_rule" : len(gejala_rule),
            "skor"       : skor_persen,
        })

    hasil.sort(key=lambda x: x["skor"], reverse=True)
    return hasil


def tingkat_kepercayaan(skor: float) -> str:
    if skor >= 75:
        return "SANGAT TINGGI"
    elif skor >= 50:
        return "TINGGI"
    elif skor >= 25:
        return "SEDANG"
    else:
        return "RENDAH"


def tampilkan_hasil(hasil: list, gejala_user: set):
    print()
    print(SEPARATOR)
    print("   HASIL DIAGNOSA")
    print(SEPARATOR)

    if not hasil:
        print("\n  [!] Tidak ditemukan kerusakan yang cocok.")
        return

    print()
    print(f"  Gejala yang dimasukkan ({len(gejala_user)} gejala):")
    for g in sorted(gejala_user):
        print(f"    [{g}] {DAFTAR_GEJALA[g]}")

    print()
    print(SEPARATOR)

    for i, item in enumerate(hasil, start=1):
        label_conf = tingkat_kepercayaan(item["skor"])
        print()
        print(f"  DIAGNOSA #{i}  |  Kepercayaan: {item['skor']:.1f}%  ({label_conf})")
        print(THIN_SEP)
        print(f"  Jenis Kerusakan : {item['nama']}")
        print(f"  Gejala Cocok    : {item['jumlah']} dari {item['total_rule']}")
        print(f"  Kode Gejala     : {', '.join(sorted(item['cocok']))}")
        print()
        print("  SOLUSI:")
        for baris in item["solusi"].split("\n"):
            print(f"    {baris}")
        print(THIN_SEP)

    print()
    print(SEPARATOR)


def main():
    while True:
        cetak_header()
        cetak_menu_gejala()

        gejala_user = minta_input_gejala()

        if not gejala_user:
            print("\n  [!] Tidak ada gejala valid.")
        else:
            hasil = inferensi(gejala_user)
            tampilkan_hasil(hasil, gejala_user)

        lagi = input("  Ingin mendiagnosa lagi? (y/n) >> ").strip().lower()
        if lagi != "y":
            print("\n  Terima kasih telah menggunakan Sistem Pakar berikut.")
            print(SEPARATOR)
            break


if __name__ == "__main__":
    main()