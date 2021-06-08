from random import sample
from response_from_service import is_spelling_correct
import random

def scramble(word):
  return ''.join(sample(word, len(word))).lower()

def score_for_guess(guess, word, is_spelling_correct):
  if any(filter(lambda letter: guess.count(letter) > word.count(letter), guess)):
    return 0

  if not is_spelling_correct(guess):
    return 0

  return sum(1 if letter in 'aeiou' else 2 for letter in guess)

def pick_random_word(words):
  if not words:
    return ''
    
  return random.choice(words)