import copy
from typing import List


def is_prime(n):
    if n < 2:
        return 0
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d = d + 1
    if d == 2:
        return 1
    return 0


def get_longest_all_primes(lst: List[int]) -> List[int]:
    max_length = 0
    length = 0
    list = []
    final_list = []
    for i in range(len(lst)):
        if is_prime(lst[i]) == 1:
            list.append(lst[i])
            length = length + 1
        else:
            if length > max_length:
                max_length = length
                final_list = copy.deepcopy(list)
                length = 0
                list.clear()
    if length > max_length:
        final_list = copy.deepcopy(list)
    return final_list


def main():
    lisst = [10, 5, 5, 7, 11, 13, 17, 23, 20, 5, 7, 11, 13, 17, 23]
    new_list = get_longest_all_primes(lisst)
    print(new_list)


if __name__ == "__main__":
    main()
