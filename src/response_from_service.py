import requests

def get_response(word):
  url = ''.join(["http://agilec.cs.uh.edu/spell?check=", word])
  return requests.get(url).text

def parse_text(text):
  if text not in ['true', 'false']:
    raise RuntimeError("Text is not a boolean")

  return text == 'true'

def is_spelling_correct(word):
  return parse_text(get_response(word))