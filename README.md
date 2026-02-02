# 🧙‍♂️ Connect 4 — Harry Potter Edition (AI Course Project)


> This repository is an **AI course project**: a Harry-Potter-themed Connect Four web game with an intelligent opponent.

---

## ✨ Features

- 🎮 **Web game** (Flask) with an interactive 6×7 Connect Four board.
- 🧠 Multiple AI options:
  - **Minimax**
  - **Minimax v2** (alternative evaluation)
  - **Minimax + Alpha–Beta pruning**
  - **Minimax v2 + Alpha–Beta pruning**
  - **Heuristic** / **Heuristic v2** (fast greedy)
- 🎚️ Difficulty levels mapped to search depth:
  - **Easy** → depth **2**
  - **Medium** → depth **4**
  - **Hard** → depth **7**
- ⚡ Harry Potter vibe:
  - Intro video + music
  - HP font and themed assets

---

## 🧩 Tech Stack

- **Python 3**
- **Flask** (backend / routes)
- **NumPy** (board representation & computation)
- **HTML/CSS/JS** (frontend)

---

## 🚀 Getting Started

### 1) Clone the project
```bash
git clone <YOUR_REPO_URL>
cd An-Intelligent-Connect-Four-Player-main
```

### 2) Create a virtual environment (recommended)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate
```

### 3) Install dependencies
If you have a `requirements.txt`:
```bash
pip install -r requirements.txt
```

Otherwise install directly:
```bash
pip install flask numpy
```

### 4) Run the app
```bash
python app.py
```

Then open:
- `http://127.0.0.1:5000/`

---

## ✅ Important Note (Quick Fix)

If the app fails immediately with an import error, ensure `app.py` uses **render_template** (Flask’s correct function name):

Replace:
```python
from flask import Flask, render_templates, request, jsonify
...
return render_templates("index.html")
```

With:
```python
from flask import Flask, render_template, request, jsonify
...
return render_template("index.html")
```

---

## 🎯 How to Play

1. Start from the landing page `/` then click **Start Game**.
2. Choose:
   - **Algorithm**
   - **Difficulty**
   - Your character & AI opponent
3. Click any column to drop your piece.
4. The AI responds using the selected algorithm.

Board encoding:
- `0` → empty
- `1` → human player
- `2` → AI

---

## 🤖 AI Details (High Level)

The AI lives in `connect4.py` and supports:

- **Minimax**: explores the game tree up to a chosen depth and picks the move that maximizes the AI score.
- **Alpha–Beta Pruning**: speeds up minimax by skipping branches that cannot affect the final decision.
- **Two evaluation strategies**:
  - `score_position()` (classic window scoring + center preference)
  - `future_chance_score()` (counts future chances / open windows)

---

## 🔌 API Endpoint (for the AI move)

The frontend calls:
- `POST /move`

Payload:
```json
{
  "board": [[0,0,0,0,0,0,0], ...],
  "difficulty": "MED",
  "algorithm": "alpha_beta"
}
```

Response:
```json
{ "column": 3 }
```

Supported algorithm values:
- `minimax`
- `minimax2`
- `alpha_beta`
- `alpha_beta2`
- `hurestic`
- `hurestic2`

---

## 📁 Project Structure

```
.
├─ app.py                 # Flask app (routes + AI selection)
├─ connect4.py            # Game logic + AI algorithms
├─ templates/
│  ├─ index.html          # Intro page (video + start)
│  └─ game.html           # Game UI & settings
└─ static/
   ├─ css/                # Styles (Harry Potter theme)
   ├─ js/                 # Frontend logic
   ├─ images/             # Characters, icons, backgrounds
   ├─ sounds/             # Music & effects
   └─ video/              # Intro video
```

---

## 📌 Credits / Academic Use

This project is made for **educational purposes** as part of an AI course.  
