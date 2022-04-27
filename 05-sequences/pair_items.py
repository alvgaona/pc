# https://www.codewars.com/kata/61055e2cb02dcb003da50cd5
"""
Write a function with the following properties:

- takes two lists
- returns a list of all possibilities to pair as many elements as possible from both lists while keeping the order of the elements
- output format is a list of lists of tuples, or a list with an empty list, if no pairs are possible
- inner lists can be of any order (see tests)

Hints

If both input lists are of equal length, then every item of one list will be paired with an item of the other list 
(see first example) -> results in only one sublist. If both input lists are of different length and not empty,
then every item of the shorter list will be paired, but not every item of the larger list -> results in more than one
sublist, because there are more then one possibilities to omit items from the larger list.

Example 1

Pair elements of ['c', 'o', 'd', 'e'] with elements of ['w', 'a', 'r', 's']

Expected Result:

[[('c', 'w'), ('o', 'a'), ('d', 'r'), ('e', 's')]]
"""


def pair_elements(array_one, two_array):
    result = []

    for first, second in zip(array_one, two_array):
        result.append((first, second))

    return result


print(pair_elements(['c', 'o', 'd', 'e'], ['w', 'a', 'r', 's']))
