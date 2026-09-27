"""Stáhne denní kurz PLN z ČNB a uloží ho do kurz.json.

kurz = počet Kč za 1 PLN, datum = den, pro který ČNB kurz vyhlásila.
Soubor se přepíše jen tehdy, když se kurz nebo datum změní.
"""
import json
import urllib.request
from pathlib import Path

URL = "https://api.cnb.cz/cnbapi/exrates/daily?lang=EN"
SOUBOR = Path(__file__).resolve().parent.parent / "kurz.json"


def main() -> None:
    with urllib.request.urlopen(URL, timeout=30) as odpoved:
        data = json.load(odpoved)

    pln = next(r for r in data["rates"] if r["currencyCode"] == "PLN")
    novy = {
        "mena": "PLN",
        "kurz": round(pln["rate"] / pln["amount"], 4),
        "datum": pln["validFor"],
        "zdroj": "ČNB",
    }

    if SOUBOR.exists():
        stary = json.loads(SOUBOR.read_text(encoding="utf-8"))
        if stary.get("kurz") == novy["kurz"] and stary.get("datum") == novy["datum"]:
            print("Kurz se nezměnil:", novy)
            return

    SOUBOR.write_text(json.dumps(novy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Uložen nový kurz:", novy)


if __name__ == "__main__":
    main()
