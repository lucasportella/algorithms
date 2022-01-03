# corta o indice pela metade e
# itera somente a metade, vai
# comparando os valores do íncide
# (indice mínimo e indice máximo) até
# chegar na métade, o número de
# letras ser ímpar é irrelevante
# pois o loop para antes do caractere
#  do meio e ele não precisa ser
# verificado para descobrir se é
# palíndromo ou não


def is_palindrome_iterative(word):
    if not word:
        return False

    # good performance
    mid = len(word) // 2
    for c in range(0, mid):
        if word[c] != word[(len(word) - 1 - c)]:
            return False
    return True

    # mid performance
    # word2 = ''
    # for c in range((len(word) -1), -1, -1):
    #     word2 += word[c]
    # if word == word2:
    #     return True
    # return False

    # worst performance, prob cause have to calculate len of word many times
    # word2 = ''
    # for c in range((len(word))):
    #     word2 += word[len(word) -1 -c]
    # if word == word2:
    #     return True
    # return False
