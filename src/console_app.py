from guesser import scramble, score_for_guess, pick_random_word
from response_from_service import get_response, parse_text, is_spelling_correct
import random, os

current_path = os.path.dirname(__file__)
word_file_path = os.path.join(current_path, '../words.txt')

word_file = open(word_file_path, "r")
word_list = word_file.readlines()

random_word = pick_random_word(word_list)
random_word = random_word.rstrip("\n")

random_word_scrambled = scramble(random_word)
present_scrambled_word = ''.join(["\nScrambled word: ", random_word_scrambled])

while True:
    print(present_scrambled_word)

    print('Enter a guess for the word: ', end = '')
    word_guess = input()

    score_as_string = str(score_for_guess(word_guess, random_word, is_spelling_correct))
    present_score = ''.join(["Score for guess: ", score_as_string])
    print(present_score)

    if word_guess == random_word:
        print("\nCongratulations, you guessed the correct word!")
        break