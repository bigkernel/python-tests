#!/usr/bin/env python

## LIST mutable sequence
## Here are all of methods of list object.
## list.append(x): Add an item to the end of the list.
##      list.append(object)
## list.extend(L): Extend the list by appeding all the items in the given list.
##      list.extend(iterable)
## list.insert(i, x): Insert an item x at a given position i.
##      list.insert(index, object)
## list.remove(x): Remove the first item from the list whose value is x.
##                It is an error(ValueError) if there is not such item.
##      list.remove(value)
## list.pop([i]): Remove the item at the given position and return it.
##                If no index is specified, removes and returns the last item.
##                if list is empty or index out of range, raises IndexError.
##      list.pop([index])
## list.index(): Return the index in the list of the first item whose value is x
##               It is an error(ValueError) if there is no such item.
##      list.index(value[, start[, stop]])
## list.count(x): Return the number of item x apprears in the list.
##      list.count(value)
## list.sort(cmp = None, key = None, reverse = False):
##              Sort the items of the list in place.
##      cmp(x, y) : -1 least equal
##                  0  equal
##                  1  great equal

## Using List as Stacks
stack = [0, 1, 2]

stack.append(3)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

## Using List as Queues
queue = [0, 1, 2]

queue.append(3)
print(queue)

queue.pop(0)
print(queue)

queue.pop(0)
print(queue)

## List Comprehensions
from math import pi
pilist = [str(round(pi, i)) for i in range(5)]
print(pilist)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix_roll= [[row[i] for row in matrix] for i in range(4)]
print(matrix_roll)
