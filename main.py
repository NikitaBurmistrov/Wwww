from random import choice

import requests
import time

API_URL = "https://zenquotes.io/api/random"
SAVED_FILE = "Цитаты.txt"

def get_quotes(author=None, limit=3):
    response = requests.get(API_URL)

    if response.status_code != 200:
        print("Ошибка при запросе:", response.status_code)
        return []

    data = response.json()
    return data


def save_quotes(quotes):
    with open(SAVED_FILE, "a", encoding='utf-16') as f:
        for quote in quotes:
            line = f"{quote['q']} - {quote['a']}\n"
            f.write(line)


def main():
    print('Философские цитаты')

    author = input('Введите имя автора или оставьте поле пустым: ').strip()
    quotes = get_quotes(author=author)

    if not quotes:
        print('Цитаты не найдены.')
        return

    for i, q in enumerate(quotes, start=1):
        print(f"\n[{i}] {q['q']}\n - {q['a']}")
        time.sleep(0.5)

    choice = input('\nСохранить эти цитаты? (Да/Нет): ').lower()
    if choice == 'да':
        save_quotes(quotes)


if __name__=="__main__":
    main()




