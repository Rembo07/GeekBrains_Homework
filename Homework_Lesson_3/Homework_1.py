def num_translate(key=None):
    numbers = { 'zero':'ноль',
                'one':'один',
                'two':'два',
                'three':'три',
                'four':'четыре',
                'five':'пять',
                'six':'шесть',
                'seven':'семь',
                'eight':'восемь',
                'nine':'девять',
                'ten':'десять'
    }
    print(numbers.get(key))
num_translate('h')
