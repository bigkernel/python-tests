#!/usr/bin/env python

'''The default value is evaluated only once.
This makes a difference when the default is a mutable object such as a list,
dictionary, or instances of most classes.
'''
def func0(v, L = None):
    if L is None:
        L = []
    L.append(v)
    return L

def func1(v, L = []):
    L.append(v)
    return L

def parrot(voltage, state = 'a stiff', action = 'voom', type='Norwegin Blue'):
    print("-- This parrot wouldn't", action, end = ' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# tuple type of the @arguments
# dictionary type of the @keywords
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any?", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

# Documentation Strings
def document_func():
    '''Do nothing, But document it!
    No, Really, it doesn't do anything.'''
    pass

def annotation_func(param0:str, param1:int) ->str:
    print("Annotations: ", annotation_func.__annotations__)
    return param0 + " <> " + param1

def main():
    print(func0(1))
    print(func0(2))
    print(func0(3))
    print(func1(1))
    print(func1(2))
    print(func1(3))

    parrot(100)
    parrot(voltage = 1000)
    parrot(voltage = 1000, action = 'VOOOOOM')
    parrot(action = 'VOM', voltage = 10000)
    parrot('a million', 'bereft of life', 'jump')
    parrot('a thousand', state = 'pushing up the daisies')

    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very very runny, sir.",
               shopkeeper = "Michael Palin",
               client = "John Cleese",
               sketch = "Cheese Shop Sketch")

# Unpacking arguments list
    d = {"voltage": "four million", "state": "belledin' demised", "action":"VooM"}
    parrot(**d)

    print(document_func.__doc__)

    print(annotation_func("1", "2"))

if __name__ == '__main__':
    main()
