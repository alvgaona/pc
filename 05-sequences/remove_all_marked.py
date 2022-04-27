# https://www.codewars.com/kata/563089b9b7be03472d00002b
"""
Define a function that removes from a given array of integers all the values contained in a second array.

Example:

Examples:

Input -> [1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]
Output -> [2, 2, 4]
"""

#for i in range(0,len(one_array)):
#    print(one_array[i])

#for index, value in enumerate(one_array):
#        print(index)
#        print(value)


def remove_all_marked(array_one, array_two):
    result = []

    for value in array_one:
        if not (value in array_two):
            result.append(value)

        #for subvalue in array_two:
        #    if value != subvalue:
        #        result.append(value)
        #        break

    return result


print(remove_all_marked([1, 2, 3, 4, 4, 4], [4, 8]))
