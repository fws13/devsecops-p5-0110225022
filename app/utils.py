def truncate(text, limit=50):
    """Potong teks panjang untuk ringkasan."""
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."

import subprocess


def run_cmd(cmd):
    # KODE RENTAN UNTUK DEMO QUALITY GATE, JANGAN DI-MERGE
    return subprocess.call(cmd, shell=True)
