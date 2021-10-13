from typing import List


def is_prime(n):
    """
    Verifica daca numarul este prim.
    :param n: numar natural.
    :return: True - daca este prim, False - da nu este prim.
    """
    if n < 2:
        return 0
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d = d + 1
    if d == 2:
        return True
    return False


def get_longest_all_primes(lst: List[int]) -> List[int]:
    """
    1.Determina cea mai lunga subsecventa cu o proprietatea ca toate numerele sunt patrate perfecte.
    :param lst: lista de numere citita.
    :return:Lista cu cea mai lunga subsecventa proprietatea ca toate numerele sunt patrate perfecte.
    """
    max_length = 0
    length = 0
    temp_list = []
    final_list = []
    for i in range(len(lst)):
        if is_prime(lst[i]) is True:
            temp_list.append(lst[i])
            length = length + 1
        elif length > max_length:
            max_length = length
            final_list = temp_list[:]
            length = 0
            temp_list.clear()
        else:
            temp_list.clear()
    if length > max_length:
        final_list = temp_list[:]
    return final_list


def test_get_longest_all_primes():
    assert get_longest_all_primes([10, 5, 5, 7, 11, 13, 17, 23, 20, 5, 7, 11, 13, 17, 23, 23]) == [5, 5, 7, 11, 13, 17,
                                                                                                   23]
    assert get_longest_all_primes([10]) == []
    assert get_longest_all_primes([10, 2, 3]) == [2, 3]
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([10, 17, 3, 5, 21, 2, 3, 5, 7]) == [2, 3, 5, 7]
    assert get_longest_all_primes([10, 5, 7, 24, 2, 3]) == [5, 7]
    assert get_longest_all_primes([10, 1, 20]) == []


def prime_digits(n):
    """
    Verifica daca toate cifrele numarului sunt numere prime.
    :param n: numarul pe acre trebuie verificat.
    :return: 1 - daca toate cifrele sunt prime , 0 - daca nu toate cifrele sunt prime.
    """
    lst = []
    while n:
        lst.append(n % 10)
        n = n // 10
    for i in range(len(lst)):
        if is_prime(lst[i]) == False:
            return False
    return True


def get_longest_prime_digits(lst: List[int]) -> List[int]:
    """
    13.Determina cea mai lunga subsecventa cu o proprietatea ca toate numerele sunt formate din cifre prime.
    :param lst: lista de numere
    :return: Lista cu cea mai lunga subsecventa cu proprietatea ca toate cifrele numarului sunt numere prime.
    """
    length = 0
    max_length = 0
    temp_list = []
    final_list = []
    for i in range(len(lst)):
        if prime_digits(lst[i]) == True:
            temp_list.append(lst[i])
            length = length + 1
        elif length > max_length:
            max_length = length
            length = 0
            final_list = temp_list[:]
            temp_list.clear()
        else:
            temp_list.clear()
    if length > max_length:
        final_list = temp_list[:]
    return final_list


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([]) == []
    assert get_longest_prime_digits([1, 2, 3]) == [2, 3]
    assert get_longest_prime_digits([10, 2, 37, 21, 2, 35, 37, 100]) == [2, 35, 37]
    assert get_longest_prime_digits([1]) == []
    assert get_longest_prime_digits([2]) == [2]
    assert get_longest_prime_digits([2, 39, 5, 37, ]) == [5, 37]
    assert get_longest_prime_digits([213, 25, 23, 27, 22, 21, 213, 25, 5, 7, 333, 5555, 203]) == [25, 5, 7, 333, 5555]
    assert get_longest_prime_digits([2, 2, 2, 2, 17, 7, 11, 10, 2, 2, 2, 2, 17, 7, 31, 100]) == [2, 2, 2, 2]


def get_longest_all_not_prime(lst: List[int]) -> List[int]:
    """
        7. Cea mai lunga secventa cu proprietatea ca toate numerele sunt neprime.
        :param lst: lista de numere
        :return: Lista cu cea mai lunga subsecventa cu proprietatea ca toate numerele sunt neprime.
        """
    length = 0
    max_length = 0
    temp_list = []
    final_list = []
    for i in range(len(lst)):
        if is_prime(lst[i]) == False:
            temp_list.append(lst[i])
            length = length + 1
        elif length > max_length:
            max_length = length
            length = 0
            final_list = temp_list[:]
            temp_list.clear()
        else:
            temp_list.clear()
    if length > max_length:
        final_list = temp_list[:]
    return final_list


def test_get_longest_all_not_prime(lst: List[int]):
    assert test_get_longest_all_not_prime([2, 3, 7]) == []
    assert test_get_longest_all_not_prime([1]) == []
    assert test_get_longest_all_not_prime([10, 20, 30, 40, 1]) == [10, 20, 30, 40]
    assert test_get_longest_all_not_prime([14, 15, 16, 18, 2, 1, 10, 20, 30, 40]) == [1, 10, 20, 30, 40]
    assert test_get_longest_all_not_prime([2, 2, 1, 2, 3]) == [2, 2]
    assert test_get_longest_all_not_prime([]) == []
    assert test_get_longest_all_not_prime([1, 10, 15, 17, 222, 420, 48]) == [1, 10, 15]
    assert test_get_longest_all_not_prime([70, 210, 49, 88, 110]) == [70, 210, 49, 88, 110]
    assert test_get_longest_all_not_prime([2, 4, 10, 8, 90, 1, 4, 2]) == [2, 3, 10, 8, 90, 1, 4]


def read_list() -> List[int]:
    lst = input("Introduceti numerele:")
    lst = lst.split(' ')
    converted_list = []
    for i in range(len(lst)):
        converted_list.append(int(lst[i]))
    return converted_list


def main():
    lst = []
    while True:
        print("1.Introduceti numerele separate printr-un spatiu.")
        print("2.Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt numere prime.")
        print("3.Determina cea mai lunga subsecventa cu proprietatea ca toate cifrele numarului sunt numere prime. ")
        print("4.Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt neprime")
        print("5.Exit.")
        optiune = input("Alegeti optiunea: ")
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(get_longest_all_primes(lst))
        elif optiune == '3':
            print(get_longest_prime_digits(lst))
        elif optiune == '4':
            print(get_longest_all_not_prime(lst))
        elif optiune == '5':
            break
        else:
            print("Optiune invalida")


if __name__ == "__main__":
    test_get_longest_all_primes()
    test_get_longest_prime_digits()
    main()
