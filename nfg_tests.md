## Rock Paper Scissors (`matrix_rps`)
- Tuple is in the form of `(Player 0, Player 1)`

| P0 \ P1 | Action 0 (Rock) | Action 1 (Paper) | Action 2 (Scissors) |
|---|---:|---:|---:|
| **Action 0 (Rock)** | (0, 0) | (1, -1) | (-1, 1) |
| **Action 1 (Paper)** | (-1, 1) | (0, 0) | (1, -1) |
| **Action 2 (Scissors)** | (1, -1) | (-1, 1) | (0, 0) |

---

## Prisoner's Dilemma (`matrix_pd`)
- Tuple is in the form of `(Player 0, Player 1)`

| P0 \ P1 | Action 0 (Cooperate) | Action 1 (Defect) |
|---|---:|---:|
| **Action 0 (Cooperate)** | (5, 5) | (10, 0) |
| **Action 1 (Defect)** | (0, 10) | (1, 1) |

---

## 3-Player Matching Pennies
- Tuple is in the form of `(Player 0, Player 1, Player 2)`

| Case | Player 0 | Player 1 | Player 2 | Payoffs |
|---|---:|---:|---:|---|
| 1 | 0 | 0 | 0 | (1, 1, -1) |
| 2 | 0 | 0 | 1 | (-1, 1, 1) |
| 3 | 0 | 1 | 0 | (-1, -1, -1) |
| 4 | 0 | 1 | 1 | (1, -1, 1) |
| 5 | 1 | 0 | 0 | (1, -1, 1) |
| 6 | 1 | 0 | 1 | (-1, -1, -1) |
| 7 | 1 | 1 | 0 | (-1, 1, 1) |
| 8 | 1 | 1 | 1 | (1, 1, -1) |
