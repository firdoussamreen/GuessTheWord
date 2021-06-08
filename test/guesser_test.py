import unittest
from functools import partial
from src.guesser import scramble, score_for_guess as original_score_for_guess, pick_random_word

score_for_guess = partial(original_score_for_guess, is_spelling_correct = lambda word: True)

class GuesserTest(unittest.TestCase):  
  def test_canary(self):
    self.assertTrue(True)

  def test_scramble_apple(self):
    self.assertNotEqual("apple", scramble("apple"))

  def test_scramble_matter(self):
    self.assertNotEqual("matter", scramble("matter"))

  def test_scramble_apple_twice(self):
    apple_scrambled_once = scramble("apple")
    
    apple_scrambled_twice = scramble(apple_scrambled_once)

    self.assertNotEqual(apple_scrambled_once, apple_scrambled_twice)

  def test_scramble_empty_string(self):
    self.assertEqual('', scramble(''))

  def test_scramble_mixed_case(self):
    mixed_case_apple_scrambled = scramble("ApPle")

    self.assertTrue(mixed_case_apple_scrambled.islower())

  def test_scrambled_word_same_characters_as_original(self):
    self.assertEqual(sorted("matter"), sorted(scramble("matter")))
  
  def test_score_for_letter_guess(self):
    self.assertEqual(1, score_for_guess('a', 'apple'))

  def test_score_for_monk_in_monkey(self):
    self.assertEqual(7, score_for_guess('monk', 'monkey'))

  def test_score_for_ape_in_apple(self):
    self.assertEqual(4, score_for_guess('ape', 'apple'))

  def test_score_for_word_with_no_vowel(self):
    self.assertEqual(4, score_for_guess('by', 'bayou'))

  def test_score_for_guess_with_letters_not_in_word(self):
    self.assertEqual(0, score_for_guess('bye', 'bayou'))

  def test_score_for_guess_with_repeat_letters(self):
    self.assertEqual(0, score_for_guess('rear', 'relate'))
 
  def test_score_for_word_with_incorrect_spelling(self):
    self.assertEqual(0, original_score_for_guess('app','apple', is_spelling_correct = lambda word: False))
  
  def test_score_for_another_word_with_incorrect_spelling(self):
    self.assertEqual(0, original_score_for_guess('ape','apple', is_spelling_correct = lambda word: False))

  def test_score_for_word_with_correct_spelling_but_runtime_error(self):
    def is_spelling_correct(word):
      raise RuntimeError("Error retrieving data")

    self.assertRaisesRegex(RuntimeError, "Error retrieving data", original_score_for_guess, "apple", "apple", is_spelling_correct)

  def test_pick_random_word_from_list(self):
    words = ['apple', 'monkey', 'cake', 'program', 'school']

    self.assertTrue(pick_random_word(words) in words)

  def test_pick_second_word_different_word(self):
    words = ['apple', 'monkey', 'cake', 'program', 'school']
    first_word = pick_random_word(words)

    second_word = pick_random_word(words)
    for trials in range(10):
      second_word = pick_random_word(words)
      if second_word != first_word:
        break
    if trials == 10:
      return self.fail()

    self.assertNotEqual(first_word, second_word)

  def test_pick_random_word_from_empty_list(self):
    words = []
    self.assertEqual('', pick_random_word(words))

if __name__ == '__main__':
    unittest.main()