import re

def text_stat(filename):
    """
    Функция вывода статистики текста из файла.
    """
    result = {}

    is_text_file = False
    for ext in [".txt", ".csv", ".log"]:
        if filename.endswith(ext): 
            is_text_file = True
            break
    if not is_text_file:
        result["error"] = "Файл не является текстовым."
        return result

    try:
        with open(filename, "r") as file:
            ru_letters = [chr(code) for arr in [range(ord("а"), ord("я") + 1), (ord("ё"),)] for code in arr]
            en_letters = [chr(code) for code in range(ord("a"), ord("z") + 1)]
            
            letter_statistics = {letter:[0,0] for list in [ru_letters, en_letters] for letter in list}

            char_counter = 0
            paragraph_counter = 0
            word_counter = 0
            bilingual_word_counter = 0

            while True:
                paragraph = file.readline()
                if paragraph:
                    paragraph = paragraph.rstrip()

                    paragraph_counter += 1
                    char_counter += len(paragraph)

                    paragraph = [re.sub(r"[^\w]", "", word) for word in paragraph.split()]
                    paragraph = [word.lower() for word in paragraph if word]
                    word_counter += len(paragraph)

                    for word in paragraph:
                        for char in word:
                            if char in ru_letters + en_letters:
                                letter_statistics[char][0] += 1
                        for char in set(word):
                            if char in ru_letters + en_letters:
                                letter_statistics[char][1] += 1
                        if bool(set(word) & set(ru_letters)) & bool(set(word) & set(en_letters)):
                            bilingual_word_counter += 1

                else:
                    break
            
            for char in ru_letters + en_letters:
                letter_statistics[char][0] /= char_counter
                letter_statistics[char][1] /= word_counter
                result[char] = round(letter_statistics[char][0], 4), round(letter_statistics[char][1], 4)

            result["paragraph_amount"] = paragraph_counter
            result["word_amount"] = word_counter
            result["bilingual_word_amount"] = bilingual_word_counter
    

    except FileNotFoundError:
        result.clear()
        result["error"] = "Файл не найден."
    except ZeroDivisionError:
        result.clear()
        result["error"] = "Количество слов или символов в файле равно нулю."
    except PermissionError:
        result.clear()
        result["error"] = "Недостаточно прав доступа."
    except OSError:
        result.clear()
        result["error"] = "Ошибка системы."
    except:
        result.clear()
        result["error"] = "Ошибка при работе с файлом."
    
    return result


if __name__ == "__main__":
    print("Функция вывода статистики текста из файла.")
    path = input("\nВведите путь до файла: ")
    print("\nВывод статистики: ")
    result = text_stat(path)
    for item in result.items():
        print("{0}: {1}".format(item[0], item[1]))
    input("\nНажмите Enter для выхода из программы...")