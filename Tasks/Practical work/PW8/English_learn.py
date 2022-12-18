import operator
import pymorphy2
import translate


def get_english_phrasebook(file_name: str, phrasebook: str) -> None:
    with open(file_name, "r", encoding='utf-8') as file:
        list = file.read().split()
        write_dict_to_file(phrasebook, get_sorted_dict(normalize_words_list(list)))


def normalize_words_list(words_list: list) -> list:
    for i in range(0, len(words_list)):
        letter_list: list = [a for a in words_list[i] if a.isalpha()]
        word: str = "".join(letter_list)
        words_list[i] = get_normal_form(word)
    return words_list


def get_normal_form(word: str) -> str:
    morph = pymorphy2.MorphAnalyzer()
    return morph.parse(word)[0].normal_form


def get_sorted_dict(words: list) -> dict:
    words_in_dict = {}
    for word in words:
        words_in_dict[word] = str(words.count(word))
    if '' in words_in_dict:
        words_in_dict.pop('')
    return dict(sorted(words_in_dict.items(), key=operator.itemgetter(1), reverse=True))


def write_dict_to_file(file_name: str, dictionary_of_words: dict) -> None:
    en_translator = translate.Translator(from_lang='ru', to_lang='en')

    with open(file_name, encoding='utf-8', mode='w') as file:
        for word in dictionary_of_words:
            file.write(f'{word} | {en_translator.translate(word)} | {dictionary_of_words[word]}\n')


get_english_phrasebook('text.txt', 'phrasebook.txt')