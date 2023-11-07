def roman_numerals_to_int(roman_numeral):
    """
    Функция перевода числа из римской нотации в десятичную целочисленную нотацию.
    """
    result = 0
    roman_letters = ("I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M")
    arab_nubmbers = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
    roman_numeral = roman_numeral.upper()
    
    if len(roman_numeral) == 0:
        print("Получена пустая строка.")
        return None

    i = 0
    while True:
        if i >= len(roman_numeral):
            break

        num = 0
        step = 0
        roman_num_exist_error = "{0} не является римской цифрой.".format(roman_numeral)

        try:
            # проверка пары рядомстоящих символов
            if i+1 < len(roman_numeral):
                substr = "".join([roman_numeral[i], roman_numeral[i+1]])
                
                if substr in roman_letters:
                    num += arab_nubmbers[roman_letters.index(substr)]
                    step = 2
                    # меньшая цифра, стоящая перед большей, должна быть только одна
                    if roman_numeral[i] == roman_numeral[i-1]:
                        print(roman_num_exist_error)
                        return None
                    # индекс числа, которое идет после большего, должен быть не меньше, чем индес наименьшего из пары
                    elif roman_letters.index(roman_numeral[i+2]) >= roman_letters.index(roman_numeral[i]):
                        print(roman_num_exist_error)
                        return None
                    i += step
                    result += num
                    continue  

            # проверка отдельного символа
            if roman_numeral[i] in roman_letters:
                num += arab_nubmbers[roman_letters.index(roman_numeral[i])]
                step = 1
                cur_index = i
                
                # цикл для проверки ближайших цифр
                for count in range(1, 5):
                    if roman_numeral[cur_index+1] in roman_letters:
                        # индекс последующей цифры должен быть меньше текущего
                        if roman_letters.index(roman_numeral[cur_index+1]) > roman_letters.index(roman_numeral[i]):
                            print(roman_num_exist_error)
                            return None
                        # если цифра изменилась, выходим из цикла
                        elif (roman_numeral[cur_index+1] != roman_numeral[cur_index]) & (count > 1):
                            break
                        # цифры V, L, D не могут встречаться более одного раза
                        elif (roman_numeral[cur_index+1] in ["V", "L", "D"]) & (count >= 2):
                            print(roman_num_exist_error)
                            return None
                        # остальные цифры не могут встречаться более 3-х раз подряд
                        elif (roman_numeral[cur_index+1] == roman_numeral[cur_index]) & (count == 4):
                            print(roman_num_exist_error)
                            return None
                        else:
                            cur_index += 1
                    else:
                        print("Встречен посторонний символ.")
                        return None
                
                result += num
                i += step
            
            else:
                print("Встречен посторонний символ.")
                return None

        except IndexError:
            result += num
            i += step
        except ValueError:
            print("Встречен посторонний символ.")
            return None

    return result 


if __name__ == "__main__":
    print("Функция перевода числа из римской нотации в десятичную целочисленную нотацию.")
    roman_numeral = input("\nВведите римское число: ")
    result = roman_numerals_to_int(roman_numeral)
    if result:
        print("Десятичное число: {0}".format(result))
    input("\nНажмите Enter для выхода из программы...")
