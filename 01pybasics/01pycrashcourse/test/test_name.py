import sys
import os
sys.path.insert(0, os.path.dirname(os.getcwd()))

from mod.name import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('albert', 'einstein')
    assert formatted_name == 'Albert Einstein'

def test_first_middle_last_name():
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
