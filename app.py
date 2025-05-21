from flask import Flask, render_templates, request, jsonify
import numpy as np
import connect4

app = Flask(__name__)

@app.route("/")
def index():
    return render_templates("index.html")

@app.route("/game")
def game():
    return render_templates("game.html")

@app.route("/move", methods=["POST"])
def move():
    try:
        data = request.get_json()
        board = np.array(data["board"])
        difficulty = data.get("difficulty", "MED").upper()
        algorithm = data.get("algorithm", "minimax")

        if difficulty == "EASY":
            depth = 2
        elif difficulty == "MED":
            depth = 4
        elif difficulty == "HARD":
            depth = 7
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400

        if algorithm == "minimax":
            col, _ = connect4.minimax(board, depth=depth, maximisingPlayer=True)
        elif algorithm == "minimax2":
            col, _ = connect4.minimax2(board, depth=depth,  maximisingPlayer=True)
        elif algorithm == "alpha_beta":
            col, _ = connect4.minimax_with_alpha_beta(board, depth=depth, alpha=-1e9, beta=1e9, maximisingPlayer=True)
        elif algorithm == "alpha_beta2":
            col, _ = connect4.minimax2_with_alph_beta(board, depth=depth, alpha=-1e9, beta=1e9, maximisingPlayer=True)
        elif algorithm == "hurestic":
            col = connect4.hurestic(board, connect4.AI)
        elif algorithm == "hurestic2":
            col  = connect4.hurestic2(board, connect4.AI)
        else:
            return jsonify({"error": "Invalid algorithm selected"}), 400

        return jsonify({"column": int(col)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
