# Exercise 21: Laptop Prices

You are given `n` laptops, each with a price and quality.  
If there exists a pair such that a cheaper laptop has **higher quality** than a more expensive one, print:

happy irsa


Otherwise print:

poor irsa


_All outputs should be in lowercase._

## Input

- First line: integer n (number of laptops)
- Next n lines: two integers per line (price quality)

## Example 1

**Input**
2

1 10

7 3

**Output**
happy irsa


## Example 2

**Input**
4

1 5

7 9

5 6

20 30

**Output**
poor irsa


## How to Run

```bash
python laptop_prices.py
