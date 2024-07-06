# filter()i function in python is a built in function that allows to filter elements in list,tuple,set

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


def is_greater_5(num):
    return num > 5


new_number_even = filter(is_even, numbers)
print(list(new_number_even))

new_number_5 = filter(is_greater_5, numbers)

print(list(new_number_5))

def double_number(numb):
    return numb * 2

twice = map(double_number,numbers)
print(list(twice))

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']


def filter_vowels(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letters in vowels

result = filter_vowels('e')
print(result)

filtered_words = filter(filter_vowels,letters)
print(list(filtered_words))
