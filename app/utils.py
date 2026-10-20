def truncate(text, limit=50):
    """Potong teks panjang untuk ringkasan."""
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


