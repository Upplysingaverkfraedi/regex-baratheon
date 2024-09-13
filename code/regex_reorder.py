import argparse
import os
import re


def parse_arguments():
    """
    Lesa inn argument frá skipanalínu
    :return: (ArgumentParser) parser með argumentunum
    """

    parser = argparse.ArgumentParser(description="""Endurraða csv-skrá sem hefur röðunina: 
    1) eiginnafn millinafn kenninafn, 2) heimilisfang, 3) símanúmer.    
    Úttaksskráin verður endurröðuð í tsv röð:
    1) heimilisfang, 2) símanúmer, 3) kenninafn, eigninnafn millinafn.
    """)
    parser.add_argument('--infile', required=True,
                        help='Slóð að inntaksskrá með upplýsingum.')
    parser.add_argument('--outfile', required=True,
                        help='Slóð að úttaksskrá með endurröðuðum upplýsingum.')
    return parser.parse_args()


def lesa_skra(file_path):
    """
    Lesa inntaksskrá og skila lista af línum
    :param file_path: (str) Slóð að skrá
    :return:          (list) Listi af línum
    """

    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def endurraða_skra(linur):
    """"
    Tekur línur á formattinu Jón Jónsson, Litla-Saurbæ, 816 Ölfusi, 555-1234
Guðrún Helgadóttir, Fiskislóð 15, 101 Reykjavík, 510-7000
Jón Oddur Guðmundsson, Úthlíð 6, 450 Patreksfirði, 897-1234
og skilar endurröðuðum línum á formattinu Litla-Saurbæ	816 Ölfusi	555-1234	Jónsson, Jón
Fiskislóð 15	101 Reykjavík	510-7000	Helgadóttir, Guðrún
Úthlíð 6	450 Patreksfirði	897-1234	Guðmundsson, Jón Oddur. Þannig Orðunum er enduraðað
Kommur fara út nema á milli eftirnafns og fornafns og bil myndast.



    substitution = r'\3\t\4\t\5\t\2\t\1'

    """
    result = []
    pattern = r'([^,]+)\s([^,]+),\s([^,]+),\s([^,]+),\s(.+)'  # reges pattern notað til að bera kennsl á og hópa saman miðað við formattið
    substitution = r'\3\t\4\t\5\t\2, \1'  # Skiptimunstrið skilgreint til þess að enduraða orðunum, kommum skipt út fyrir bil

    for lina in linur:  # ítra yfir hverja línu i input listanum
        if re.match(pattern, lina):  # athuga hvort línurnar passi við regex patternið
            newline = re.sub(pattern, substitution, lina)  # enduraða línunum eftir substitution-inu
            result.append(newline)  # bæta enduraðaðri línunni við útkomu listann

    return result


def skrifa_nidurstodur(output_file, linur):
    """
    Skrifar niðurstöður í úttaksskrá
    :param output_file: (str) Slóð að úttaksskrá
    :param linur:       (list) Listi af línum
    :return:            None
    """

    with open(output_file, 'w') as file:
        file.write('\n'.join(linur))


def main():
    """
    Keyrslufall sem les inn skrá, endurraðar henni og skrifar niðurstöður í nýja skrá.
    :return: None
    """

    args = parse_arguments()

    # Athuga hvort skráar endingar séu réttar
    if not args.infile.endswith('.csv'):
        print('Inntaksskrá þarf að vera csv skrá.')
        return
    if not args.outfile.endswith('.tsv'):
        print('Úttaksskrá þarf að vera tsv skrá.')
        return
    # Athuga hvort inntaksskrá sé til
    if not os.path.exists(args.infile):
        print('Inntaksskrá fannst ekki.')
        return

    # Lesa línur úr skránni
    linur = lesa_skra(args.infile)

    # Endurraða hverri línu í skránni
    linur = endurraða_skra(linur)

    # Skrifa niðurstöðurnar í nýja skrá
    skrifa_nidurstodur(args.outfile, linur)


if __name__ == "_main_":
    main()
