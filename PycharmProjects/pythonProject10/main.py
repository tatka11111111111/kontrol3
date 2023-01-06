# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочкам
#def card_hide(card):
#     return '*' * len(card[:-4]) + card[-4:]
#
# Напишите функцию, которая проверяет: является ли слово палиндромом
s = input("enter a word: ")
reverse = s[::-1]


def palindrom(s):
    while True:
        if s[::1] == reverse:
            print(s, "is palindrome ")
            break
        if s != reverse:
            print(s, "not a palindrome !")
            continue


print(palindrom(s))