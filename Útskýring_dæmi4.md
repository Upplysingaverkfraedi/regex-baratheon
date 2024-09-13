## Regluleg segðir fyrir timataka.py

### Regluleg segð til að skoða URL-slóðina
Reglulega segðin sem við notum til að skoða URL: `pattern = re.compile(
    r'<tr[^>]*>\s*<td[^>]*>(\d+)</td>\s*<td[^>]*>(3845)</td>\s*<td[^>]*>Finnur Björnsson</td>\s*<td[^>]*>(\d{4})</td>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(\d{2}:\d{2}:\d{2})</td>\s*<td[^>]*>(\+\d{2}:\d{2})</td>\s*<td[^>]*>(\d{2}:\d{2}:\d{2})</td>',
    re.DOTALL
)`.
* `https://timataka\.net\`:
    * Passar nákvæmlega við linkinn "https://timataka.net/".
    * Ath. að við notum bakstrik (`\`) á undan punkti (`.`) til að sleppa honum og tryggja að hann passi við bókstaflega punkt (`.`) í URL-inu.
* `.+/urslit/:`
    * `.`: Passar við hvaða staf sem er (tákn fyrir einn staf).
    * `+`: Passar við einn eða fleiri stafi af hvaða gerð sem er.
    * Saman `. + /urslit/` tryggir að það sé einhver texti á undan "/urslit/".
* `\?race=\d+&cat=\w+`:
    * `\?`: Passar við spurningamerki (`?`), sem er notað í URL fyrir fyrirspurn.
    * `race=\d+`: Passar við "race=" fylgt eftir af einni eða fleiri tölustöfum (`\d+`).
    * `&cat=\w+`: Passar við "&cat=" fylgt eftir af einum eða fleiri bók- eða tölustöfum (`\w+`), þar sem `\w` táknar hvaða staf eða tölustaf sem er.
* `(&age=\d+)?`:
    * `(&age=\d+)?`: Passar við valfrjálsan hluta sem byrjar á "&age=" og fylgt er eftir með einum eða fleiri tölustöfum (`\d+`). Spurningamerkið ? gerir þetta að valfrjálsu samsvörun.

### Regluleg segð til að vinna úr HTML-gögnum
Reglulega sem við notuðum til að vinna úr HTML-gögnum er: `pattern = re.compile(
    r'<tr[^>]*>\s*<td[^>]*>(\d+)</td>\s*<td[^>]*>(3845)</td>\s*<td[^>]*>Finnur Björnsson</td>\s*<td[^>]*>(\d{4})</td>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(\d{2}:\d{2}:\d{2})</td>\s*<td[^>]*>(\+\d{2}:\d{2})</td>\s*<td[^>]*>(\d{2}:\d{2}:\d{2})</td>',
    re.DOTALL
)
`
* `<tr[^>]*>`:
    * Passar við hvaða `<tr>` tag sem er.
    * `[^>]*`: Passar við hvaða staf sem er nema >, svo það tekur inn hvaða eiginleika sem er innan `<tr>` tagsins (t.d. <tr class="row">).
* `\s*`:
    * Passar við hvaða bil sem er (hvít bil, nýjar línur o.s.frv.).
    * Notað til að tryggja að bilið í HTML hafi ekki áhrif á samsvörunina.
* `<td[^>]*>(\d+)</td>`:
    * Passar við `<td>` tag með tölustaf innan þess.
    * (`\d+`): Grípur röðina (`Rank`) með einum eða fleiri tölustöfum, sem verður `match.group(1)`.
* `<td[^>]*>(3845)</td>`:
    * Passar við annað `<td>` tag með keppnisnúmerið "3845" (sérstakt fyrir "Finnur Björnsson").
    * `(3845)`: Nákvæm samsvörun við keppnisnúmerið.
* `<td[^>]*>Finnur Björnsson</td>`:
    * Passar við þriðja `<td>` tagið með nafninu "Finnur Björnsson".
* `<td[^>]*>(\d{4})</td>`:
    * Passar við fjórða `<td>` tagið með fæðingarárinu.
    * `(\d{4})`: Grípur fjóra tölustafi sem tákna árið (Year), sem verður `match.group(3)`.
* `<td[^>]*>(.*?)</td>`:
    * Passar við `<td>` tag sem inniheldur nafn klúbbsins.
    * `(.*?)`: Grípur hvaða texta sem er innan `<td>` tagsins, þar til það finnur næsta loka tag. Þetta verður `match.group(4)`.
* `<td[^>]*>(\d{2}:\d{2}:\d{2})</td>`:
    * Passar við `<td>` tag með keppnistímanum.
    * `(\d{2}:\d{2}:\d{2})`: Grípur tímamynstur "hh:mm
", sem verður `match.group(5)`.
* `<td[^>]*>(\+\d{2}:\d{2})</td>`:
    * Passar við `<td>` tag með muninum "Behind".
    * `(\+\d{2}:\d{2})`: Grípur mynstur "+mm
", sem verður `match.group(6)`.
* `<td[^>]*>(\d{2}:\d{2}:\d{2})</td>`:
    * Passar við síðasta `<td>` tag með chip-tímanum.
    * `(\d{2}:\d{2}:\d{2})`: Grípur tímamynstur "hh:mm
", sem verður `match.group(7)`.