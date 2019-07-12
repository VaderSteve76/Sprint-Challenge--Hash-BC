#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    if length <= 1:
        return None

    ht = HashTable(16)

    for i in range(length):  # check for element in hashtable
        key_exist = hash_table_retrieve(ht, weights[i])
        # is same elem. and each  = to elem + elem
        if (key_exist == 0 or key_exist) and
        (limit - weights[i] == weights[i]):
            return (i, key_exist)
        hash_table_insert(ht, weights[i], i)

    keys = []  # placeholder

    for i in range(length):   # looking for key, adding limit
        key_value = hash_table_retrieve(ht, weights[i])
        if key_value:
            keys.append(weights[i])
            keys.append(limit - weights[i])
            break

    indexes = [weights.index(keys[0]), weights.index(keys[1])]
    indexes.sort(reverse=True)

    return (indexes[0], indexes[1])


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
