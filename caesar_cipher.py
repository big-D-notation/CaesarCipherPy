ALPHABETS = {
    'EN' : 'abcdefghijklmnopqrstuvwxyz',
    'UA' : 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя',
}


def encode(text: str, key: int, lang: str) -> str:
    '''
        Функція шифрування тексту шифром Цезаря
        Викликає функцію shift() для зміщення по алфавіту на key символів

        :param text: текст для шифрування
        :param key:  ключ шифрування
        :param lang: мова вхідного тексту. 
                    'EN' - англійська, 'UA' - українська
                    
        :return: зашифрований текст
    '''
    return shift(text, key, lang)


def decode(text: str, key: int, lang: str) -> str:
    '''
        Функція шифрування тексту шифром Цезаря
        Викликає функцію shift() для зміщення по алфавіту на -key символів

        :param text: текст для дешифрування
        :param key:  ключ шифрування
        :param lang: мова вхідного тексту. 
                    'EN' - англійська, 'UA' - українська
                    
        :return: дешифрований текст
    '''
     
    return shift(text, -key, lang)

def shift(text: str, key: int, lang: str) -> str:
    '''
        Функція, що зсуває текст по алфавіту на key символів

        :param text: текст для дешифрування
        :param key:  ключ шифрування
        :param lang: мова вхідного тексту. 
                    'EN' - англійська, 'UA' - українська
                    
        :return: зміщений на key символів текст        
    '''
    
    res = []

    if not lang in ALPHABETS:
        raise ValueError(f'Unsuported language {lang}')

    lang_alph = ALPHABETS[lang]

    for symbol in text:        
        if symbol.isalpha():
            is_upper = symbol.isupper()
            new_symbol_index = (
                lang_alph.find(symbol.lower()) + key) % len(lang_alph
            )
            new_symbol = lang_alph[new_symbol_index]
            res.append(new_symbol.upper() if is_upper else new_symbol)
        else:
            res.append(symbol)

    return ''.join(res)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Caesar cipher encoder and decoding script'
    )

    parser.add_argument('--text', required=True, help='text to encode/decode')
    parser.add_argument('--key', type=int, required=True, help='text to encode/decode')
    parser.add_argument('--lang', required=True, choices=['EN', 'UA'], help='input text language')
    parser.add_argument('--encode', action='store_true', help='encode text')
    parser.add_argument('--decode', action='store_true', help='decode text')

    args = parser.parse_args()

    if args.encode:
        print(encode(args.text, args.key, args.lang))
    elif args.decode: 
        print(decode(args.text, args.key, args.lang))

if __name__ == '__main__':
    main()
