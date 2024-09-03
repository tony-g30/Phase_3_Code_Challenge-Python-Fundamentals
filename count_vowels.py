#function that returns the count of vowels (a, e, i, o, u) in the input string.


def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

result = count_vowels('TONY')
print(result)