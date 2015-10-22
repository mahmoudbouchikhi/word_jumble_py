__author__ = 'Cpt-Mahmoud'


def remainder(x, y):
    return x % y


def power(x, y):
    return x ** y


def quotient(x, y):
    return x // y


def makeTitle(text):
    return text.title()


def clean(text):
    return text.strip()


def makeSentence(text):
    return text.capitalize() + "."


def distance(x, y):
    count = 0
    for i, v in enumerate(x):
        if x[i] != y[i]:
            count += 1
    return count


def selectLast(S):
    return S[-1]
