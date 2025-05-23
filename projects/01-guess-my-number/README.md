# Project 01: Guess My Number Game

A simple command-line game where the computer tries to guess the number you are thinking of between 1 and 99.

## How it works

- Think of a number between **1** and **99** (inclusive) and do **not** enter it into the system.
- The program will guess a number and display it.
- You respond:
  - `k` if your number is **smaller** than the guess ("k" stands for "koochaktar").
  - `b` if your number is **bigger** than the guess ("b" stands for "bozorgtar").
  - `d` if the guess is **correct** ("d" stands for "dorost").
- The computer narrows down the guesses based on your hints until it finds your number.

## Example

40

Enter k or b or d: b

75

Enter k or b or d: k

54

Enter k or b or d: d

hooooo!! my guess is True!


## How to run

```bash
python guess_my_number.py
Notes
Only use lower-case characters k, b, or d as your responses.
Each round, the computer should eventually guess the exact number you thought of.
Improvements
You can further improve the game by using a binary search algorithm instead of random choice for more efficiency.
