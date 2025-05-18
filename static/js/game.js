const startScreen = document.getElementById("start-screen");
const startBtn = document.getElementById("start-btn");
const playersInfo = document.getElementById("players-info");

const playerImg = document.getElementById("player-img");
const aiImg = document.getElementById("ai-img");
const playerNameText = document.getElementById("player-name");
const aiNameText = document.getElementById("ai-name");

const playerSelect = document.getElementById("player-select");
const aiSelect = document.getElementById("ai-select");

function capitalize(name) {
   return name.charAt(0).toUpperCase() + name.slice(1);
}

const step1 = document.getElementById("step-1");
const step2 = document.getElementById("step-2");
const nextBtn = document.getElementById("next-btn");

nextBtn.addEventListener("click", () => {
   const selectedAlgorithm = document.getElementById("algorithm-select").value;
   const selectedDifficulty = document.getElementById("difficulty").value;

   step1.classList.add("hidden");
   step2.classList.remove("hidden");
});

startBtn.addEventListener("click", () => {
   const selectedHuman = playerSelect.value;
   const selectedAI = aiSelect.value;

   const humanName = capitalize(selectedHuman.split(".")[0]);
   const aiName = capitalize(selectedAI.split(".")[0]);

   playerImg.src = `/static/images/${selectedHuman}`;
   aiImg.src = `/static/images/${selectedAI}`;
   playerNameText.textContent = `You: ${humanName}`;
   aiNameText.textContent = aiName;

   startScreen.classList.add("hidden");
   playersInfo.classList.remove("hidden");
});

const moveList = document.getElementById("move-list");
const finalResult = document.getElementById("final-result");

let moveCounter = 1;

function logMove(player, row, col) {
   const item = document.createElement("li");
   item.textContent = `${moveCounter++}. ${player} played at [Row ${row + 1}, Col ${col + 1}]`;
   moveList.appendChild(item);
}

window.addEventListener("DOMContentLoaded", () => {
   const ROWS = 6,
      COLS = 7;
   let board = Array.from({
      length: ROWS
   }, () => Array(COLS).fill(0));
   let gameOver = false;

   const boardDiv = document.getElementById("board");

   function renderBoard() {
      boardDiv.innerHTML = "";
      for (let r = ROWS - 1; r >= 0; r--) {
         for (let c = 0; c < COLS; c++) {
            const cell = document.createElement("div");
            cell.classList.add("cell");
            if (board[r][c] === 1) cell.classList.add("player1");
            else if (board[r][c] === 2) cell.classList.add("player2");
            cell.dataset.row = r;
            cell.dataset.col = c;
            boardDiv.appendChild(cell);
         }
      }
   }

   function nextRow(col) {
      for (let r = 0; r < ROWS; r++) {
         if (board[r][col] === 0) return r;
      }
      return null;
   }

   function checkWin(player) {
      const directions = [
         [1, 0],
         [0, 1],
         [1, 1],
         [1, -1]
      ];
      for (let r = 0; r < ROWS; r++) {
         for (let c = 0; c < COLS; c++) {
            if (board[r][c] !== player) continue;
            for (let [dr, dc] of directions) {
               let count = 1;
               for (let i = 1; i < 4; i++) {
                  const nr = r + dr * i,
                     nc = c + dc * i;
                  if (nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS || board[nr][nc] !== player) break;
                  count++;
               }
               if (count === 4) return true;
            }
         }
      }
      return false;
   }

   function checkDraw() {
      return board.every(row => row.every(cell => cell !== 0));
   }

   const messages = {
      win: [{
            text: "أنا هنا بين الكتيبة! 🔥",
            sound: "إنت عايز تبوظ اخلاقي.mp3"
         },
         {
            text: "إنت عايز تنبط أخلاقي؟ 😂",
            sound: "إنت عايز تبوظ اخلاقي.mp3"
         }
      ],
      lose: [{
            text: "اضرب ... 💥",
            sound: "اضررب.mp3+"
         },
         {
            text: "مستحيل مستحيل!! 😭",
            sound: "مستحيل مستحيل.mp3"
         }
      ],
      draw: [{
            text: "بهجت صابر: مش وقته 😅",
            sound: "بهجت صابر مش وقته.mp3"
         },
         {
            text: "سبحااااانه ",
            sound: "سبحااااانه بهجت صابر.mp3"
         }
      ]
   };

   function endGame(type) {
      gameOver = true;
      const options = messages[type];
      const chosen = options[Math.floor(Math.random() * options.length)];
      const audio = new Audio(`/static/sounds/${chosen.sound}`);

      audio.onended = () => {
         alert(chosen.text);
         location.reload();
      };

      setTimeout(() => {
         if (!audio.ended) {
            alert(chosen.text);
            location.reload();
         }
      }, 7000);

      audio.play().catch(() => {
         alert(chosen.text);
         location.reload();
      });
   }

   let musicStarted = false;
   boardDiv.addEventListener("click", async (e) => {
      if (!musicStarted) {
         const bgMusic = document.getElementById("bg-music");
         bgMusic.play().catch(() => {});
         musicStarted = true;
      }

      if (gameOver || !e.target.classList.contains("cell")) return;
      const col = +e.target.dataset.col;
      const row = nextRow(col);
      if (row === null) return;

      board[row][col] = 1;
      renderBoard();

      if (checkWin(1)) return endGame("win");
      if (checkDraw()) return endGame("draw");

const difficulty = document.getElementById("difficulty").value;
const algorithm = document.getElementById("algorithm-select").value;

const response = await fetch("/move", {
   method: "POST",
   headers: {
      "Content-Type": "application/json"
   },
   body: JSON.stringify({
      board,
      difficulty,
      algorithm
   }),
});


      const data = await response.json();
      const aiCol = data.column;
      const aiRow = nextRow(aiCol);
      if (aiRow !== null) {
         board[aiRow][aiCol] = 2;
         renderBoard();
      }

      if (checkWin(2)) return endGame("lose");
      if (checkDraw()) return endGame("draw");
   });

   renderBoard();
});