# Exercise 20: Kabaddi World Cup Team Formation

Given:
- Each Kabaddi player can participate in at most 5 World Cup tournaments.
- But to be eligible for new teams, each must not have played more than 2 tournaments yet.
- Each team requires exactly 3 players.

## Task

Given the number of players (`n`) and how many times each has already played in the World Cup, calculate **how many fully eligible 3-player teams** can be formed.

## Input

First line: An integer `n` (number of players).  
Second line: `n` integers separated by space — the number of times each player has participated.

## Output

A single integer: the maximum number of 3-player teams possible.

## Example

**Input**
6

5 0 4 2 1 0

**Output**
1


**Explanation:**  
Only players with 0, 2, 1, 0 can join; that's 4 people, so only 1 team.

## How to Run

```bash
python kabaddi_worldcup_teams.py
