## Útskýring á reglulegri segð fyrir kennitölu einstaklinga:

Reglulega segðin fyrir kennitölu einstaklinga er: `\b(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])(\d{2})-([2-9][0-9])(\d{1})([890])\b`

skilyrðin fyrir kennitölu einstaklinga eru:
- fyrstu tveir tölustafirnir eru á bilinu 01-31:  
    Reglulega segðin `0[1-9]|[12][0-9]|3[01]`: ef að 1. talan er 0 getur 2. talan verið 1-9, ef að 1. talan er 1 eða 2 getur 2. talan verið 0-9, og ef að 1. talan er 3 getur seinni talan verið 0-1
- næstu tveir eru á bilinu 01-12  
    Regluklega segðin `0[1-9]|1[0-2]`: ef að fyrri talan er 0 getur seinni verið á bilinu 1-9, en ef að hún er 1 getur seinni verið 1 eða tveir.
- síðustu tveir geta verið hvaða tölustafir sem er:  
    Reglulega segðin `\d{2}`: hvaða tveir tölustafir á bilinu 0-9
- tölustafir 7 og 8 er tala frá og með 20  
    Reglulega segðin `[2-9][0-9]`: fyrri stafurinn getur verið á bilinu 2-9 og seinni á bilinu 0-9
- tölustafur 9 er hvaða tölustafur sem er á bilinu 0-9
    Reglulega segðin `\d{1}`  
- Síðasti stafurinn getur verið 8, 9 eða 0
    Reglulega segðin `[890]`  

Síðan settum við hverja reglulegu segð inn í sviga og settum segðina saman með bandstriki eftir fyrstu 6 tölustafina eins og kennitölurnar voru settar upp í textaskránni sem að við notuðum. settum `\b` fyrir framan og aftan segðina til að skilgreina orðamörkin


## Útskýring á reglulegri segð fyrir kennitölu fyrirtækja

Reglulega segðin sem að við notuðum fyrir kennitölur fyrirtækja er: `\b[4-9]\d{5}-\d{4}\b`

Fyrir kennitölur fyrirtækja er reglulega segðin töluvert einfaldari þar sem að þau fá úthlutað kennitölu þar sem að eina skilyrðið er að fyrsti stafurinn er 4 eða hærri.
Til þess að passa að fyrsti stafurinn yrði ekki minni en 4 byrjaði reglulega segðin á `[4-9]` sem passar við hvaða staf á bilinu 4-9
þar á eftir koma 5 tölustafir á bilinu 0-9 með reglulegu segðinni `d{5}`
Svo táknum við bandstrik þar sem að kennitölurnar eru skrifaðar þannig í textanum sem unnið var með
í lokin koma svo aftur 4 handahófskenndar tölur á bilinu 0-9 með reglulegu segðinni `\d{4}`
Við settum þetta allt saman og `\b` fyrir framan og aftan til þessað skilgreina orðamörkin.

## Kóði Útskýring
Kóðinn er í regex_kt.py skránni. Þar skilgreindum reglulegu segðina fyrir einstaklinga og fyrirtæki og nota svo re.findall(mynstur_einstaklingar, lina) til þess að leita af öllum kennitölum einstaklings, eða fyrirtækja í hverri línu sem að passa við reglulegu segðina. Þar sem að reglulega segðin hjá kennitölum einstaklinnga var skipt niður í búta setti ég þá ala saman í streng til þess að kennitalan prentist á réttu formi.
