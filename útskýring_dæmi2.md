## Regluleg segð fyrir email
Reglulega segðin sem að við notuðum fyrir email er: `\b[A-Za-z0-9.]+@(?!.*\.\.)[A-Za-z0-9.-]+\.[A-Za-z]{2,3}\b`

- `\b` í byrjun skilgreinir orðamörkin þannig að tölvupóstfangið er ekki hluti af lengri streng.
- `[A-Za-z0-9.]` þar á eftir merkir að allt fyrir fyrri hluti netfangsins má innihalda alla bókstafi, stóra: `A-Z` og litla: `a-z`, alla tölustafi frá 0-9:`0-9` og `.`
- `+` þar á eftir það sé a.m.k. eitt eða fleiri af táknunnum í hornklofanum á undan
- `@` þá kemur "@" 
- `(?!.*\.\.)` þetta passar að það komi ekki tvöfaldur punktur neins staðar fyrir eftir núverandi stöðu í strengnum
    - `(?! mynstur)` er negative lookahead og þýðir að eitthvað mynstur sem er skilgreint inni í sviganum má ekki koma fram seinna í strengnum.
    - `.` táknar hvaða staf sem er og `*` táknar "0 eða fleiri skipti", þ.e. mynstrið má hvorki koma strax eða eftir einnhverja stafi
    - `\.\.` merkir tvöfaldan punkt eða ..
- `[A-Za-z0-9.-]+` þar á eftir þýðir að næsti hluti netfangsins má innihalda alla bókstafi, stóra: `A-Z` og litla: `a-z`, alla tölustafi frá 0-9:`0-9`, `.` og .`-`
- `+` þar á eftir það sé a.m.k. eitt eða fleiri af táknunnum í hornklofanum á undan
- þar á eftir kemur punktur táknaður með `\.`
- `[A-Za-z]{2,3}`:  fyrir aftan punktinn mega vera hvaða bókstafir sem er stórir: `A-Z` og litlir: `a-z` og fjöldi þeirra má vera 2 eða 3: `{2,3}`
- `\b` í lokin til að skilgreina orðamörkin

## Kóði
Við settum þessa segð inn í skránna regex_email.py og notuðum `re.findall(email_regex, full_text)` til þess að leita af netföngum í textanum sem að uppfylla skilyrði segðarinnar.