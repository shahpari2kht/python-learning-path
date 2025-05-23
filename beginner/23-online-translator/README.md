# Exercise 23: Online Translator

Receives a dictionary and a sentence, and translates the sentence using the given dictionary.

## Input

- The first line is an integer `n` (number of dictionary entries).
- The next `n` lines contain two words: the word and its translation.
- The last line contains a sentence to be translated.

## Output

- The translated sentence with the given mappings; words not found in the dictionary remain unchanged.

## Example

**Input:**
5

hello salam

goodbye khodafez

say goftan

we ma

you shoma

we say goodbye to you tonight

**Output:**
ma goftan khodafez to shoma tonight


## How to Run

```bash
python online_translator.py
