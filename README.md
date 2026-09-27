# objev-polsko-kurz

Denní kurz polského zlotého (PLN) podle ČNB pro orientační cenu v Kč
v poptávkovém formuláři webu Objev Polsko.

- `kurz.json` — `kurz` = Kč za 1 PLN, `datum` = den vyhlášení kurzu ČNB.
- Aktualizuje ho GitHub Action `Kurz ČNB` ve všední dny ve 14:00 UTC,
  lze ji spustit i ručně (Actions → Kurz ČNB → Run workflow).
- Zdroj: https://api.cnb.cz/cnbapi/exrates/daily
