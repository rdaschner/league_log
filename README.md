# league_log - # League Ranker

This project processes football match results and calculates team rankings.

## 📦 Project Structure

- `main.py` – Entry point for CLI and FastAPI.
- `services/league.py` – League logic.
- `models/match.py` – Data model for match results.
- `tests/` – Unit tests.
- `sample_data/matches.txt` – Sample match data.

---

## 🚀 Usage

### 🟦 1. Run as CLI

```bash
python -m league_ranker.main --file sample_data/matches.txt
```

### 🌐 2. Run as FastAPI service

```bash
uvicorn league_ranker.main:app --reload --port 5000 --app-dir src
```

### 🎯 3. Test FastAPI Endpoints

#### `/rank` (JSON Input)

```bash
curl -X POST "http://localhost:5000/rank" \
  -H "Content-Type: application/json" \
  -d '{ "matches": ["Lions 1, FC Awesome 1", "Snakes 2, Lions 1"] }'
```

#### `/rank-file` (File Upload)

```bash
curl -X POST "http://localhost:5000/rank-file" \
  -F "file=@sample_data/matches.txt"
```

---

## ✅ Running Tests

```bash
pytest
```

You should see coverage results like:

```
================= test session starts =================
...
collected 5 items

tests/test_match.py ..                           [ 40%]
tests/test_league.py ...                         [100%]

================== 5 passed in 0.09s ==================
```

Ensure you have `pytest` installed:

```bash
pip install pytest
```

# Actual Test 22/06/2025

tests\test_api.py .                                                                                                                                                           [ 20%]
tests\test_cli.py .                                                                                                                                                           [ 40%]
tests\test_league.py .                                                                                                                                                        [ 60%] 
tests\test_match.py ..                                                                                                                                                        [100%]

================================================================================== tests coverage ================================================================================== 
_________________________________________________________________ coverage: platform win32, python 3.12.8-final-0 __________________________________________________________________ 

Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
src\league_ranker\__init__.py              0      0   100%
src\league_ranker\api.py                  38     18    53%   21-22, 29-48
src\league_ranker\main.py                 19     19     0%   2-24
src\league_ranker\models\match.py         20      0   100%
src\league_ranker\services\league.py      26      1    96%   12
--------------------------------------------------------------------
TOTAL                                    103     38    63%
================================================================================ 5 passed in 2.30s ================================================================================= 