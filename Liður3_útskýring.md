## 3. Endurraða skrá

Markmið dæmisins er að endurraða línum með hjálp reglulega segða. Reglulegar segðir eru
notaðar til að leita að, breyta eða staðfesta texta. Þær eru byggðar á mynstrum sem saman-
standa af táknum sem tákna sérstakar tegundir texta eða aðgerðir. Eru þær mikið nýttar í
gagngagreiningu og textaúrvinnslu. Í þessu dæmi verður textinn úr skjali
nafn_heimilisfang_simanumer.csv breytt eftir fyrirmælum. En stendur til að breyta uppröðuninni
á línunni. Í stað þess að röðin sé nafn, heimilisfang, póstnúmer og símanúmer. Verður hún
heimilisfang, póstnúmer, símanúmer, kenninafn og að lokin eiginafn og millinafn. en einnig viljum
við taka kommu út og setja `\t` inn í staðinn (nema á eftir kenniafni).

Upprunalegu línurnar líta svona út:

Jón Jónsson, Litla-Saurbæ, 816 Ölfusi, 555-1234
Guðrún Helgadóttir, Fiskislóð 15, 101 Reykjavík, 510-7000
Jón Oddur Guðmundsson, Úthlíð 6, 450 Patreksfirði, 897-1234

Reglulega segðin sem notað er:

`([^,]+)\s([^,]+),\s([^,]+),\s([^,]+),\s(.+)`

Reglulega segðin hér er notuð til að finna og hópa saman upplýsingarnar í hverri línu fyrir sig.

Brjótum þetta niður:

`([^,]+)` = táknar fyrsta hópinn. `[^,]` þýðir hvað sem er nema komma hérna er ss komman tekin af. Hornklofarnir `[]` lýsa hvað má koma fram í þessum hóp. `+` merkir að það þarf að vera eitt eða fleiri af þessum táknum. Eða
einn eða fleiri stafir hér sem eru ekki komma. Svigarnir `()` afmarka hópinn til að hægt sé að vísa til þeirra
seinna. `\s` = táknar bil. Síðan birtast hóparnir eins koll ap kolli. Í lokinn kemur seinasti hópurinn = `(.+)`
en hann tekur það sem eftir er á línunni, sem er hér símanúmer.
Reglulega segðin skiptir textanum í hópa eftir:
1. eiginnafn og millinafn ef á við
2. kenninafn
3. Heimilisfang
4. póstnúmer
5. símanúmer

Næst kemur substitution sem er notað til að breyta uppsetningu tecxtans út frá því sem reglulega segðin hefur greint út.

substitution = `r'\3\t\4\t\5\t\2, \1'`

Hér merkir hvert \tala tiltekin hóp sem var afmarkaður í reglulegu segðinni að ofan.
`\t` setur inn bil.
Hér prentast því út heimilisfang -bil- póstnr. -bil- símanr. -bil- kenninafn, eignnafn

Ath. komman sem birtist í úrtakinu á eftir kenninafni kemur fyrir tilstilli hennar úr
substitution setningunni. Þannig ég þurfti að bæta henni við hér til að hún birtist. Því
að í reglulegu segðinni að ofan eru kommurnar aðeins til staðar til að setja textann upp
á skipulagðan hátt en `([^,]+)` sér til þess að komman sé ekki tekin með í úttakið. Substitution
notar aðeins ,,fangaða" hópa og þar eru engar kommur nema það sé tekið fram.

Hér fyrir neðan má sjá þetta útfært í python kóða. Restin af kóðanum má finna inni á skráni: regex_reorder.py

`def endurraða_skra(linur)`
    """"
    Tekur línur á formattinu Jón Jónsson, Litla-Saurbæ, 816 Ölfusi, 555-1234
    Guðrún Helgadóttir, Fiskislóð 15,  101 Reykjavík, 510-7000
    Jón Oddur Guðmundsson, Úthlíð 6, 450 Patreksfirði, 897-1234
    og skilar endurröðuðum línum á formattinu Litla-Saurbæ	816 Ölfusi	555-1234	      Jónsson, Jón
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

    return result ```

Niðurstaðan birtist úr skjalinu heimilisfang_simanumer_nafn.tsv

Litla-Saurbæ	816 Ölfusi	555-1234	Jónsson, Jón
Fiskislóð 15	101 Reykjavík	510-7000	Helgadóttir, Guðrún
Úthlíð 6	450 Patreksfirði	897-1234	Guðmundsson, Jón Oddur
regex_reorder.py