# Pong Game

A classic 2D Pong game built with Python and Pygame, featuring two game modes, sound effects, and an AI opponent.

## Features

- **Player vs Player** — two players on the same keyboard
- **Player vs Computer** — face an AI opponent that tracks the ball
- Score tracking — first to 5 points wins
- Ball accelerates by 5% on every paddle hit
- 3-second reset delay after each point
- Sound effects for hits and scoring
- Win screen with restart or quit option

## Controls

| Action | Player 1 (Left) | Player 2 / You (Right) |
|---|---|---|
| Move Up | `W` | `↑` |
| Move Down | `S` | `↓` |
| Restart (win screen) | `R` | `R` |
| Quit | `ESC` | `ESC` |

> In **Player vs Computer** mode, you control the right paddle with the arrow keys. The AI controls the left paddle.

## Requirements

- Python 3.x
- Pygame

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
cd src
python main.py
```

## Project Structure

```
pong-game/
├── src/
│   ├── main.py       # Game loop, menu, scoring, win screen
│   ├── ball.py       # Ball movement, collision, speed scaling
│   ├── paddle.py     # Paddle movement and bounds checking
│   ├── hit.wav       # Sound played on paddle hit
│   └── score.wav     # Sound played on scoring
└── requirements.txt
```
