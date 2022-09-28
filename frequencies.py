"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if not isinstance(item, str):
            item = str(item)
        if item not in frequencies:
            frequencies[f'{item}'] = 1
        else:
            frequencies[f'{item}'] += 1
    return frequencies

print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))
#{ 'a': 2, 'b': 3, 'c': 1 }
print(frequencies([100, 'Hello', '100', '100', 100]))
#{ '100': 4, 'Hello': 1 }
