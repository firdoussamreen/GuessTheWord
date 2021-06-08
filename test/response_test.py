import unittest
from unittest.mock import patch
from functools import partial
from src.response_from_service import get_response, parse_text, is_spelling_correct

class ResponseTest(unittest.TestCase): 
  def test_response_from_service_returns_text(self):
    self.assertNotEqual(None, get_response('apple'))

  def test_parse_text_true_returns_true(self):
    self.assertTrue(parse_text('true'))

  def test_parse_text_false_returns_false(self):
    self.assertFalse(parse_text('false'))

  def test_parse_text_something_else_raises_exception(self):
    self.assertRaisesRegex(RuntimeError, "Text is not a boolean", parse_text, 'something_else')

  def test_is_spelling_correct_returns_true_for_right(self):
    with patch('src.response_from_service.get_response', return_value = 'true') as mock:
      self.assertTrue(is_spelling_correct('right'))

  def test_is_spelling_correct_returns_false_for_rigth(self):
    with patch('src.response_from_service.get_response', return_value = 'false') as mock:
      self.assertFalse(is_spelling_correct('rigth'))

  def test_is_spelling_correct_returns_false_for_haha(self):
    with patch('src.response_from_service.get_response', return_value = 'false') as mock:
      self.assertFalse(is_spelling_correct('haha'))

  def test_is_spelling_correct_returns_exception(self):
    with patch('src.response_from_service.get_response', side_effect = Exception('Error')) as mock:
      self.assertRaisesRegex(Exception, 'Error', is_spelling_correct, 'word')

  def test_integration_is_spelling_correct_returns_true_for_correct(self):
    self.assertTrue(is_spelling_correct('correct'))

if __name__ == '__main__':
    unittest.main()