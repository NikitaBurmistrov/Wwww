import json
import random
from random import choice

file_cit = 'quotes.json'


#Загрузка цитат в json
def Load():
    try:
        with open(file_cit, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

#Сохранение цитат
def Save(quotes):
    with open(file_cit, 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)


#Показ всех цитат
def Show_all(quotes):
    if not quotes:
        print('\nЦитат нет')
        confromed = input(('\nХотите добавить: (Да\Нет) ')).lower()
        if confromed == 'да':
            Add_Quote(quotes)
        else:
            print('Отмена')
    else:
        for i, q in enumerate(quotes,1):
            print(f"\n[{i}] {q['content']} - {q['author']}")

#Показ рандомной цитаты
def Show_Random(quotes):
    quote = random.choice(quotes)
    print(f"\n {quote['content']}\n-{quote['author']}")


#Добавление новой цитаты
def Add_Quote(quotes):
    author = input('Автор: ').strip()
    content = input('Цитата: ').strip()
    if author and content:
        quotes.append({"author":author, "content":content})
        Save(quotes)
        print('\nЦитата добавлена')
    else:
        print('\nОшибка. Цитата не сохранена')


#Удаление цитаты по номеру
def Delete(quotes):
    if not quotes:
        print('Нет цитаты на удаление')

    Show_all(quotes)
    try:
        index = int(input('\n Введите номер цитаты на удаление :) '))
        if 1 <= index <= len(quotes):
            q = quotes[index-1]
            confrim = input(f"удалить: \"{q['content']}\" - {q['author']}? (Да/Нет): ").lower()
            if confrim == 'да':
                del quotes[index - 1]
                Save(quotes)
                print('Цитата удалена')
            else:
                print('Отмена')
        else:
            print('Номер вне диапазона')
    except ValueError:
        print('Введите целое число')


#Удаление всех цитат

def Delete_All(quotes):
    if not quotes:
        print('Список пуст')
    else:
        Show_all(quotes)
        deletes = input('\nВы хотите удалить все цитаты: (Да/Нет) ').lower()
        if deletes == 'да':
            del quotes[:]
            Save(quotes)
            print('\nЦитаты удалены')
        else:
            print('\nОтмена')


#Главное меню
def main():
    quotes = Load()

    while True:
        print("\n===Меню===")
        print('1. Показать все цитаты')
        print('2. Показать случайную цитату')
        print('3. Добавить цитату')
        print('4. Удалить цитату')
        print('5. Удалить все цитаты')
        print('6. Выход')

        option = input('Выбери цифру от 1 до 6 ').strip()

        if option == '1':
            Show_all(quotes)
        elif option == '2':
            Show_Random(quotes)
        elif option == '3':
            Add_Quote(quotes)
        elif option == '4':
            Delete(quotes)
        elif option == '5':
            Delete_All(quotes)
        elif option == '6':
            print('Пока!')
            break

if __name__ == "__main__":
    main()