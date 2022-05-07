def num_translate_adv(keyz=None):
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
    if keyz.istitle():
     keyz = keyz.lower()
     print(numbers.get(keyz).title())
    else:
        print(numbers.get(keyz))
num_translate_adv('Ten')