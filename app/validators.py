def validate_note(data):
    """Validasi input catatan. Mengembalikan (valid, pesan_error)."""
    if not data:
        return False, "Data tidak boleh kosong"
    title = data.get("title", "").strip()
    content = data.get("content", "").strip()
    if not title:
        return False, "Judul wajib diisi"
    if len(title) > 100:
        return False, "Judul maksimal 100 karakter"
    if not content:
        return False, "Isi catatan wajib diisi"
    return True, ""
