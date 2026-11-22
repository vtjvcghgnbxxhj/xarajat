"""Xarajat - oddiy xarajatlar daftari (buyruq satri dasturi).

Ishlatish:
    python xarajat.py add 15000 "Tushlik"
    python xarajat.py list
    python xarajat.py total
"""

import json
import sys
from datetime import date
from pathlib import Path

FILE = Path("xarajatlar.json")


def load():
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return []


def save(items):
    FILE.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")


def add(amount, note):
    items = load()
    items.append({"sana": str(date.today()), "summa": amount, "izoh": note})
    save(items)
    print(f"Qo'shildi: {amount} so'm - {note}")


def show():
    items = load()
    if not items:
        print("Hali xarajat yo'q.")
        return
    for i, x in enumerate(items, 1):
        print(f"{i}. {x['sana']}  {x['summa']} so'm  {x['izoh']}")


def total():
    print(f"Jami: {sum(x['summa'] for x in load())} so'm")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
    elif args[0] == "add" and len(args) >= 3:
        try:
            add(int(args[1]), " ".join(args[2:]))
        except ValueError:
            print("Summa son bo'lishi kerak. Masalan: add 15000 Tushlik")
    elif args[0] == "list":
        show()
    elif args[0] == "total":
        total()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
