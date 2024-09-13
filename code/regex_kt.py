import argparse
import re

def parse_arguments():
    """
    Lesa inn argument frá skipanalínu
    :return: (ArgumentParser) parser með argumentunum
    """

    parser = argparse.ArgumentParser(description='Leita að kennitölum einstaklinga eða fyrirtækja.')
    parser.add_argument('--file', required=True,
                        help='Slóð að inntaksskrá með kennitölum.')
    parser.add_argument('--einstaklingar', action='store_true',
                        help='Leita að kennitölum einstaklinga.')
    parser.add_argument('--fyrirtaeki', action='store_true',
                        help='Leita að kennitölum fyrirtækja.')
    return parser.parse_args()


def lesa_skra(file_path):
    """
    Lesa inntaksskrá og skila lista af línum
    :param file_path: (str) Slóð að skrá
    :return:          (list) Listi af línum
    """

    with open(file_path, 'r') as file:
        return file.readlines()


def prenta_nidurstodur(kennitolur):
    """
    Prentar út niðurstöður í console
    :param kennitolur: (list) Listi af kennitölum
    :return:           None
    """

    if kennitolur:
        print("Fundnar kennitölur:")
        for kt in kennitolur:
            print(kt)
    else:
        print("Engar kennitölur fundust.")


def finna_kennitolur(text, leit_af_einstaklingum, leit_af_fyrirtaekjum):
    """
    Leita að kennitölum í texta með reglulegum segðum
    :param text:                    (list) Listi af línum
    :param leit_af_einstaklingum:   (bool) Leita að kennitölum einstaklinga
    :param leit_af_fyrirtaekjum:    (bool) Leita að kennitölum fyrirtækja
    :return:                        (list) Listi af kennitölum
    """

    kennitolur = []
    # skilgreina reglulega segð fyrir einstaklinga 
    mynstur_einstaklingar = r'\b(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])(\d{2})-([2-9][0-9])(\d{1})([890])\b'
    # Skilgreina reglulega segð fyrir fyrirtæki 
    mynstur_fyrirtaeki = r'\b[4-9]\d{5}-\d{4}\b'
    
    if leit_af_einstaklingum:
        for lina in text:
            # Finn allar kennitölur einstaklinga í línunni
            for kt in re.findall(mynstur_einstaklingar, lina):
                #skipti hópunum niður til þess að prenta þá alla saman
                dagur = kt[0]
                manudur = kt[1]
                ar = kt[2]
                fyrsti_hluti = kt[3]
                mid_hluti = kt[4]
                lokastafur = kt[5]
                
                # Sameina hópana til að fá kennitölu á forminu ddmmáá-xxxx
                kennitala = f"{dagur}{manudur}{ar}-{fyrsti_hluti}{mid_hluti}{lokastafur}"
                kennitolur.append(kennitala)

    if leit_af_fyrirtaekjum:
        for lina in text:
            # Finn allar kennitölur fyrirtækja í línunni og bæti þeim við listann
            kennitolur.extend(re.findall(mynstur_fyrirtaeki, lina))

    return kennitolur


def main():
    """
    Keyrslufall sem les inn skrá, leitar að kennitölum og prentar niðurstöður.
    :return: None
    """

    args = parse_arguments()

    # Athuga hvort valkostir séu valdir; ef ekkert er valið, hætta og sýna villu
    if not args.einstaklingar and not args.fyrirtaeki:
        print("Þú verður að velja annað hvort --einstaklingar eða --fyrirtaeki eða bæði.")
        return

    text = lesa_skra(args.file)
    kennitolur = finna_kennitolur(text, args.einstaklingar, args.fyrirtaeki)

    prenta_nidurstodur(kennitolur)


if __name__ == "__main__":
    main()
