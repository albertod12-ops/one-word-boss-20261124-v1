"""Satu kata untuk kompetisi make.fun "One Word for the Boss" (v1).

Pemikiran sendiri, murni, ditulis sebelum melihat lapangan: bos itu
seperti camar -- datang tiba-tiba dari entah mana, membuat banyak suara,
mengotori segalanya, lalu pergi begitu saja, meninggalkan kita yang
membersihkan kekacauannya. Satu kata, tanpa penjelasan: katanya sendiri
sudah membawa seluruh lelucon -- pola manajer camar yang dikenal semua
orang kantor.
"""

import os

TEXT = "Seagull"
assert 1 <= len(TEXT) <= 30 and " " not in TEXT and TEXT.strip() == TEXT
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.umask(0o022)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
