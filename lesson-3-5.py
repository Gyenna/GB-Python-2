import random


def get_jokes(count_j):
    '''Возвращает n шуток из трех слов'''
    nouns = ['автомобиль', 'лес', 'огонь', 'город']
    adverbs = ['сегодня', 'вчера', 'завтра', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'мягкий']
    joke = []
    for i in range(count_j):
        joke.append(f'{nouns[random.randint(0,3)]} {adverbs[random.randint(0,3)]} {adjectives[random.randint(0,3)]}')
    return joke


count = int(input("Введите желаемое число шуток: \n"))
print(f'Созданные шутки:\n {get_jokes(count)}')
