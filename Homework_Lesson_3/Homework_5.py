import random
def get_jokes(num, repeat=True):
    my_joke = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if not repeat:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return 'was repeat'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(num):
                my_joke.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')

    else:
        for i in range(num):
            ran_nouns = random.choice(nouns)
            ran_adverbs = random.choice(adverbs)
            ran_adjectives = random.choice(adjectives)
            my_joke.append(f'{ran_nouns} {ran_adverbs} {ran_adjectives}')
    return print(my_joke)

get_jokes(5, True)