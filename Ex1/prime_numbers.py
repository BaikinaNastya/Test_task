def prime_numbers(low, high):
    """
    Функция вывода простых чисел в диапазоне от low до high.
    """
    if not(isinstance(high, int)) or high < 1 or not(isinstance(low, int)) or low < 1:
        print("Введите натуральные числа.")
        return []

    num_to_remove = [1]
    for i in range(2, high+1):
        if i in num_to_remove:
            pass
        else:
            for j in range(i*2, high+1, i):
                num_to_remove.append(j)

    num_to_remove = set(num_to_remove)
    arr_of_primes = [num for num in range(low, high+1) if num not in num_to_remove]

    return arr_of_primes


if __name__ == "__main__":
    print("Функция вывода простых чисел в диапазоне от low до high.")
    try:
        low = int(input("\nВведите нижнюю границу low: "))
        high = int(input("Введите верхнюю границу high: "))
        print("\nВывод простых чисел: ")
        print(prime_numbers(low, high))
    except:
        print("\nВведите натуральные числа.")
    finally:
        input("\nНажмите Enter для выхода из программы...")