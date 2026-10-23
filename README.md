# Chess engine & Web GUI

Projekt vývoje vlastní šachové umělé inteligence v Pythonu s podporou více úrovní obtížnosti a rozhraním pro hru.

## O projektu

Cílem projektu je vytvořit funkčního šachového bota s využitím rozhodovacího algoritmu **Minimax** a **Alpha-Beta prořezávání**. Aplikace bude nabízet více obtížností, aby si mohl zahrát každý podle své úrovně. Je propojena s grafickým rozhraním pro hraní v porhlížečí nebo desktopovém GUI.

### Důležité funkce.
**3 úrovně obtížnosti:**
  * **Snadná (cca 500 ELO):** Nízká hloubka prohledávání, bot delá náhodné chyby.
  * **Střední (cca 1200 ELO):** Hloubka 3 tahy, bot dokaáže pracovat s hodnotou jednotlivých figurek a podle ní se rozhoduje. Také dokáže rozeznávat určité pozice.
  * **Těžká (1500+ ELO):** Hloubka 4+ tahy, Alpha-Beta prořezávání, pozicní tabulky.
**Validace pravidel:** Správa stavu hry a správnost tahů pomocí knihovny `python-chess`.
**UCI Rozhraní:** Podpora standardizovaných příkazů (`uci`, `isready`, `position`, `go`) pro komunikaci s GUI.


## Milníky projektu (Milestones)

- [ ] **Milník 1: UCI Rozhraní a základy**
  - Nastavení repozitáře a vývojového prostředí.
  - Implementace základní UCI smyčky pro komunikaci s GUI.
  - Integrace knihovny `python-chess` pro správu stavu hry.
- [ ] **Milník 2: Implementace AI (Minimax)**
  - Rekurzivní algoritmus Minimax.
  - Optimalizace pomocí Alpha-Beta prořezávání.
  - Materiálová a pozicní evaluační funkce (Piece-Square Tables).
- [ ] **Milník 3: Nastavení obtížností**
  - Implementace 3 úrovní (Snadná / Střední / Těžká) pomocí nastavení hloubky a míry chybovosti.
  - Podpora nastavení obtížnosti přes UCI možnosti (`setoption`).
- [ ] **Milník 4: Integrace do GUI & Testování**
  - Otestování bota v aplikaci Cute Chess proti lidskému hráči i jiným botům.
  - Odladění rychlosti reakcí a stabilizace kódu.
  - Dokončení dokumentace k projektu.


## Plán práce (Task List)

### 1. Fáze: Příprava a UCI Protokol
- [ ] Vytvořit strukturu projektu
- [ ] Nainstalovat závislosti (`python-chess`)
- [ ] Napsat UCI parser pro čtení příkazů
- [ ] Propojit skript s aplikací Cute Chess a ověřit správnou komunikaci

### 2. Fáze: Vývoj algoritmu
- [ ] Napsat evaluační funkci (součet hodnot figurek + pozicní tabulky)
- [ ] Implementovat algoritmus Minimax
- [ ] Přidat Alpha-Beta prořezávání pro zvýšení hloubky prohledávání
- [ ] Doplnit logiku pro snadnou obtížnost (chyby / omezení hloubky)

### 3. Fáze: Testování a dokumentace
- [ ] Zkontrolovat správné ukončování hry (mat, pat, remíza)
- [ ] Otestovat reakční dobu bota při hloubce 4–5 tahů
- [ ] Připravit podklady pro prezentaci a vysvětlení algoritmu

## Použité technologie
* **Jazyk:** Python 3.14.4
* **Šachová logika:** `python-chess`
* **Algoritmy:** Minimax, Alpha-Beta Pruning, Piece-Square Tables
* **Komunikační protokol:** UCI (Universal Chess Interface)
* **GUI:** [Cute Chess](https://cutechess.com/)

