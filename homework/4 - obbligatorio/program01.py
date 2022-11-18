#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Obiettivo dello homework è leggere alcune stringhe contenute in una serie di
file e generare una nuova stringa a partire da tutte le stringhe lette.
Le stringhe da leggere sono contenute in diversi file, collegati fra loro a
formare una catena chiusa. Infatti, la prima stringa di ogni file è il nome di
un altro file che appartiene alla catena: partendo da un qualsiasi file e
seguendo la catena, si ritorna sempre nel file di partenza.

Esempio: il contenuto di "A.txt" inizia con "B.txt", il file "B.txt", inizia
con "C.txt" e il file "C.txt" inizia con "A.txt", formando la catena
"A.txt"-"B.txt"-"C.txt".

Oltre alla stringa con il nome del file successivo, ogni file contiene anche
altre stringhe separate da spazi, tabulazioni o caratteri di a capo. La
funzione deve leggere tutte le stringhe presenti nei file della catena e
costruire la stringa che si ottiene concatenando i caratteri con la più alta
frequenza in ogni posizione. Ovvero, nella stringa da costruire, alla
posizione p ci sarà il carattere che ha frequenza massima nella posizione p di
ogni stringa letta dai file. Nel caso in cui ci fossero più caratteri con
la stessa frequenza, si consideri l'ordine alfabetico.
La stringa da costruire ha lunghezza pari alla
lunghezza massima delle stringhe lette dai file.

Quindi, si deve scrivere una funzione che prende in ingresso una stringa A 
che rappresenta il nome di un file e restituisce una stringa.
La funzione deve costruire la stringa secondo le indicazioni illustrate sopra
e ritornare le stringa così costruita.

Esempio: se il contenuto dei tre file A.txt, B.txt e C.txt nella directory
test01 è il seguente

test01/A.txt          test01/B.txt          test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt          test01/A.txt
house                 home                  kite                                                                       
garden                park                  hello                                                                       
kitchen               affair                portrait                                                                     
balloon                                     angel                                                                                                                                               
                                            surfing                                                               

la funzione most_frequent_chars("test01/A.txt") dovrà restituire la stringa
"hareennt".
'''


def leggi_parole_files_v2(startFilename: str) -> dict:
    words = {}
    c = True
    filename = startFilename
    while c:
        file_words = leggi_parole_file(filename)
        if file_words[0] == startFilename:
            c = False
        filename = file_words[0]
        for word in file_words:
            if not word.endswith(".txt"):
                words[word] = words.get(word, 0) + 1
    return words


def leggi_parole_file(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().split()


def genera_lettera(diz: dict[str, int]):
    max_freq = max(diz, key=diz.get)    # type: ignore
    # necessario in commento sul type solo perchè
    # un'estensione fa un warning altrimenti
    return min(key for key in diz if diz[key] == diz[max_freq])


def genera_parola_v4(words_dict: dict[str, int]) -> str:
    words = list(words_dict.keys())
    max_len = len(max(words, key=len))
    characters: list[dict[str, int]] = [{} for _ in range(max_len)]
    for word in words:
        for i in range(len(word)):
            letter = word[i]
            characters[i][letter] = characters[i].get(
                letter, 0) + 1 * words_dict[word]
    # Ho lasciato il codice commentato perchè la forma in una linea sola
    # mi è stata suggerita da un'estensione di Visual Studio Code e per correttezza
    # lascio quello scritto a mano
    """
    parola = ""
    for i in range(max_len):
        parola += genera_lettera(characters[i])
    return parola
    """
    return "".join(genera_lettera(diz) for diz in characters)


def most_frequent_chars(filename: str) -> str:
    # SCRIVI QUI LA TUA SOLUZIONE
    parole = leggi_parole_files_v2(startFilename=filename)
    return genera_parola_v4(parole)


if __name__ == "__main__":
    import time
    import os

    tests = (
        ('test02/bullfight.txt', 'poternusakesness'),
        ('test03/woodchuck.txt', 'aanreeaseesable'),
        ('test04/pampers.txt', 'ceeelieessseds'),
        ('test05/avocados.txt', 'sereeieeesssssncy'),
        ('test06/strums.txt', 'sereeeeesssssssynssm'),
        ('test07/sinew.txt', 'すひびずじぞぜぃけそみきおょぇどべしこしこれれあねきゞ゜ぷ'),
        ('test08/boilings.txt', '🚏🏞😨♣☢🐸‼🗻🌚🥷🍯🎽♾🗽🍄⚔🫓😠🍈🪀🏞➡🍼👩😻📿🌁🕌👾🤓😚®❇💒🦪👒💂☪🥡🥕'),
        ('test09/meddles.txt', 'ᛢᚦᛝᛡᚤᚬᚬᛍᚸᛘᚣᚢᛜᛥᚳᛜᛖᛄᚢᛊᚬᛟᛈᛅᛞᚹᛯᚼᛁᚺ'),
        ('test10/aileron.txt',
         'ᛠᚣᚻᛝᚧᛜ᛭くᚻᛝᚭᛈᚺᛦᚩᛞᛏᚽᛪᚢᚰᚯひᛃだᚯᚨろᚷᚦᛕᚸᛯᛄᛩᛂᚲᛆᛏᚰᛨぼゆᛇᛮᛚᚯᛓやᚼかᚯᚨᛦ᛫ᚩᚲᛋᚽ👘♒ぜ🕋ゔ🕣📬💊☺🦌'),
        ('test11/metonymies.txt',
         'ᛃᚬᛝᚸᛈᚦᚱᛦᛢᛮᚼᛋᚯᛤᚳᛈᛓᚿᛊᚬᛈᚯᛎᚦᛅᛮᚧᚬᛦᚲᚮᚶᛑきᛓᛔᛮぞᛘᚼᛤᚩᛮᚼᛋᛛᛡᚱᛌᛑᚩᛪきᛤᛃᛅᛞᛏᛣᚤᚻᚦᚢᚩᛨᛐᛘゔᚷᚴᚧᚺᛖᛑᛨᛈがᛃᛥᚽᛚᚣᛋᚾᚳᚩごばᚩᚰぐがたᚨᚼᚩᛉ゜ᛅᚬᚲぅしᛪᚵᚨぎᛝᛡᛀごでᛟᚸゖそぇが🏟🃏じゔᚫぴ💌🔸😖ᛆᛪᚯ᛫ᚤᛑᚺᚾᛒᛦにぼ゙ぞゃせねねな'),
        ('test12/incipience.txt',
         'sereeeeeesssssssりᚷᛈᚳᚽᚿᚪᛙᛪᛄᚩᚿᛨᚧᚮめわᛂᛆᛘᛤᛤᛜᛉᛈᚣのぽᚳᛅᚺᛊᛛᚪᚶᚡᛘᚷᚥᛑ᛬ᛋᚥᚩᚮᛏᛅᛎᚯᚱᚽしᚻᛔᚳᛇᚪᛅᚲᚪᛨᛒゐᚨᚰᚽᚩᚿつげᛊつᚢだᛇᚺᛯᚮりᚬᚴᚹよょぬおᚱᛮᛏᚹᛑᚮっᛋ🛢ᚲᛢ📲ぃᚭᛡゐぴ🆖🫒⏰👹🍹ᛅ⏏◀🛄👍🌽🔥🎅🆙🦒🦟🔤🚓😗😕ᛦᛃᛮᛈᛂ'),
    )
    tot_time = time.time()
    for n_test, (file, word) in enumerate(tests, start=1):
        print(f"n test:\t\t{n_test}")
        start_time = time.time()
        x = leggi_parole_files_v2(startFilename=file)
        print(f"t. lettura:\t{time.time() - start_time}s")
        start_time = time.time()
        parola = genera_parola_v4(x)
        print(f"n. parole:\t{len(x)}")
        if parola != word:
            print("\033[91m")
            print(f"parola:\t\t'{parola}'")
            print(f"expected:\t'{word}'")
        else:
            print("\033[92m")
            print(f"parola:\t\t'{parola}'")
            print("\033[0m")
        size = os.get_terminal_size()
        print(
            f"t. gen. parola:\t{time.time() - start_time}s",
            end="\n\n"+"="*size.columns+"\n\n")
    print(f'total time:\t{time.time() - tot_time}s')


# funzioni create durante la progettazione ma sostituite da quelle precedenti


def genera_parola_v1(words: list[str]) -> str:
    # prima versione, troppo lenta

    if not words:
        return ""
    lettere = [word[0] for word in words]
    lettere_cp = lettere[:]
    lettere.sort(key=lambda letter: [-lettere_cp.count(letter), letter])
    return lettere[0] + genera_parola_v1([word[1:] for word in words if word[1:]])


def genera_parola_v2(words: list[str]) -> str:
    if not words:
        return ""

    characters = {}
    for l in words:
        characters[l[0]] = characters.get(l[0], 0) + 1

    character = genera_lettera(characters)
    return character + genera_parola_v2([word[1:] for word in words if word[1:]])


def genera_parola_v3(words: list[str]) -> str:
    # implementazione non ricorsiva ma praticamente uguale (almeno l'idea sarebbe questa) alla v2
    max_len = len(max(words, key=len))
    parola = ""
    for i in range(max_len):
        characters = {}
        for word in words:
            if len(word) > i:
                characters[word[i]] = characters.get(word[i], 0) + 1
        parola += genera_lettera(characters)
    return parola


def genera_parola_v3_dict(words_dict: dict[str, int]) -> str:
    words = list(words_dict.keys())
    max_len = len(max(words, key=len))
    parola = ""
    character_list = []
    for i in range(max_len):
        characters = {}
        for word in words:
            if len(word) > i:
                characters[word[i]] = characters.get(
                    word[i], 0) + 1 * words_dict[word]
        parola += genera_lettera(characters)
        character_list.append(characters)
    return parola


def leggi_parole_files(startFilename: str, filename=None, isfirst: bool = True) -> list:
    if filename is None:
        filename = startFilename
    # se vero allora sono tornato all'inizio della catena
    if not isfirst and (filename == startFilename):
        return []
    x = leggi_parole_file(filename)
    return x[1:] + leggi_parole_files(startFilename, x[0], False)
