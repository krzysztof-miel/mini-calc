# Python Mini Project: `mini_calc`

Prosty, instruktażowy projekt w Pythonie z testami w `pytest`.

## Funkcjonalność
Pakiet `mini_calc` udostępnia kilka prostych funkcji:
- `add(a, b)` — dodawanie
- `sub(a, b)` — odejmowanie
- `mean(numbers)` — średnia arytmetyczna
- `is_prime(n)` — sprawdzanie pierwszości liczby
- Prosty interfejs CLI: `mini-calc`

---

## Jak uruchomić lokalnie

### 1) Wymagania
- Python 3.9+ (sprawdzisz: `python --version` lub `python3 --version`)

### 2) Klonowanie / pobranie projektu
- Opcja A – pobierz ZIP i rozpakuj.
- Opcja B – sklonuj repozytorium z GitHuba (po utworzeniu, patrz sekcja „Publikacja na GitHub”).

### 3) Stworzenie wirtualnego środowiska (zalecane)

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux (bash/zsh):
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4) Instalacja projektu (tryb deweloperski) i zależności testowych
```bash
pip install -U pip
pip install -e ".[dev]"
```

> Jeśli nie chcesz używać `pyproject.toml`, możesz też:
> ```bash
> pip install -r requirements.txt
> ```

### 5) Uruchomienie testów
```bash
pytest -q
```

### 6) Uruchomienie CLI
Po zainstalowaniu (krok 4) dostępna jest komenda:
```bash
mini-calc add 2 3
mini-calc sub 10 4
mini-calc mean 1 2 3 4 5
mini-calc prime 17
```

---

## Publikacja na GitHub (szybka ścieżka)

1. Zaloguj się na GitHub i utwórz nowe, **puste** repozytorium (bez inicjalizacji README).
2. W terminalu w katalogu projektu:
   ```bash
   git init -b main
   git add .
   git commit -m "Init mini_calc with pytest"
   git remote add origin https://github.com/<twoja_nazwa>/<twoje_repo>.git
   git push -u origin main
   ```
3. (Opcjonalnie) Włącz GitHub Actions dla testów — dodaj workflow w `.github/workflows/tests.yml` (przykład w komentarzu na końcu README).

---

## Struktura projektu
```
python-mini-project/
├─ src/
│  └─ mini_calc/
│     ├─ __init__.py
│     ├─ core.py
│     └─ cli.py
├─ tests/
│  └─ test_core.py
├─ pyproject.toml
├─ requirements.txt
├─ pytest.ini
├─ .gitignore
└─ README.md
```

---

<!-- Przykładowy workflow GitHub Actions (opcjonalnie)
Utwórz plik .github/workflows/tests.yml o treści:

name: tests
on:
  push:
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: pytest -q
-->
