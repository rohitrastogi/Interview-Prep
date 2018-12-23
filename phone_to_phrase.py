KEYPAD = {
    1: ['y', 'z'],
    2: ['a', 'w'],
    3: ['b', 'c'],
    4: ['e', 'f', 'g'],
    5: ['h', 'i', 'j'],
    6: ['k', 'l', 'm'],
    7: ['n', 'o', 'p'],
    8: ['r', 's'],
    9: ['q', 'x', 'd'],
    0: ['t', 'u', 'v']
}

def preprocess_number(phone_number):
    split_phone_number = phone_number.split('-')
    if split_phone_number[0] == '1' and split_phone_number[1] == '800':
        return list(map(int, ''.join(split_phone_number[-2:])))
    return list(map(int, ''.join(split_phone_number)))


def solve(words, phone_number):
    res = []
    digits = preprocess_number(phone_number)
    possible_words = filter_dictionary(digits[0], words)
    for word in possible_words:
        recur(words, word, 1, digits, 1, [], res)
    return list(map(lambda l: ' '.join(l), res))

def recur(words, curr_word, word_index, digits, digit_index, sol, res):
    if digit_index == len(digits) and len(curr_word) == word_index:
        res.append(sol + [curr_word])
        return

    digit = digits[digit_index]
    chars = KEYPAD[digit]
    if len(curr_word) == word_index:
        sol.append(curr_word)
        possible_words = filter_dictionary(digits[digit_index], words)
        for word in possible_words:
            recur(words, word, 1, digits, digit_index + 1, sol, res)

    elif curr_word[word_index] in chars:
        recur(words, curr_word, word_index + 1, digits, digit_index + 1, sol, res)
    

def filter_dictionary(digit, words):
    res = []
    chars = KEYPAD[digit]
    for word in words:
        if word[0] in chars:
            res.append(word)
    return res

#TEST preprocess_number:
# print(preprocess_number('1-630-631-9924'))
# print(preprocess_number('1-800-123-4567'))

#Test filter_dictionary:
#print(filter_dictionary(5, ['happy', 'crappy', 'shop', 'jeans']))

#1-800-hat-shop
#1-800-520-9578
words = ['shop', 'hat', 'attack', 'gus', 'to', 'shon']
print(solve(words, '1-800-520-8577'))