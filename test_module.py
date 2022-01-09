
from arithmetic_arranger import arithmetic_arranger
import pytest

def test_problems_more_than_5():
  try:
    arithmetic_arranger(['1200 + 13','23 - 69','2433 + 69','2553 - 69','3223 - 69','3223 - 69','3223 - 69','3223 - 69'],True)
  except:
    print('Error: Too many problems.')
def test_wrong_operator():
  try:
    arithmetic_arranger(['1200 x 13','23 - 69','2433 + 69','2553 - 69','3223 - 69',],True)
  except:
    print("Error: Operator must be '+' or '-'.")
def test_must_contain_digits_only():
  try:
    arithmetic_arranger(['12sada00 + 13','23 - 69','2433 + 69','2553 - 69','3223 - 69',],True)
  except:
    print('Error: Numbers must only contain digits.')
def test_numbers_more_than_4():
  try:
    arithmetic_arranger(['1231200 + 13','23 - 69','2433 + 69','2553 - 69','3223 - 69',],True)
  except:
    print('Error: Numbers cannot be more than four digits.')
if __name__=='__main__':
    unittest.main()
