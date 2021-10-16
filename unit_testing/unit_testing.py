from collections import Counter
import re

class CountError(Exception):
    pass

def count_letter_frequency(content, letter):
    frequency =  Counter(re.findall(r"\w", content))[letter]
    if not frequency: raise CountError('Letter cannot be found in the content.')
    else: return frequency


