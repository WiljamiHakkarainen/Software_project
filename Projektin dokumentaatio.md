# Projektin Dokumentaatio

# Tetris-Pelin Vaatimusmäärittely

## 1. Johdanto
Tämä vaatimusmäärittely kuvaa Tetris-pelin vaatimukset ja toiminnallisuudet. Tavoitteena on toteuttaa Pythonin pygame-kirjastolla perinteinen Tetris-peli, jossa on lisätty ääniefektejä ja pisteiden laskenta.

## 2. Toiminnalliset vaatimukset

### 2.1 Pelin perustoiminnot
- **Pelin aloitus**: Pelin on aloitettava aloitusnäytöllä, josta pelaaja voi aloittaa uuden pelin tai lopettaa.
- **Tetriminojen liike**: Pelaajan on voitava ohjata palikoita näppäimistön nuolinäppäimillä:
  - Vasemmalle ja oikealle siirtyminen.
  - Alas pudottaminen nopeammin.
  - Pyöräytys myötä- tai vastapäivään.
- **Palikoiden putoaminen**: Tetrimino-palikat putoavat automaattisesti peliruudukkoon.
- **Rivien poisto**: Kun yksi tai useampi vaakarivi täyttyy kokonaan, se poistetaan, ja pelaaja saa pisteitä.
- **Pelin päättyminen**: Peli päättyy, kun Tetrimino-palikoita ei voida sijoittaa ruudukkoon (pelikenttä täyttyy).

### 2.2 Pisteytys ja tasot
- **Pisteiden laskenta**: Pelaaja saa pisteitä seuraavasti:
  - Yksittäisen rivin poistaminen = 100 pistettä.
  - Kaksi riviä kerralla = 300 pistettä.
  - Kolme riviä kerralla = 500 pistettä.
  - Neljä riviä (Tetris) kerralla = 800 pistettä.
- **Tason nousu**: Pelin nopeus kasvaa pelaajan edetessä tasoilla, jotka vaihtuvat tietyn pistemäärän jälkeen.

### 2.3 Ääniefektit
- **Ääniefektit**: Pelissä tulee olla ääniefektit ainakin seuraaviin toimintoihin:
  - Tetriminojen siirtäminen ja pyöräyttäminen.
  - Rivin poistaminen.
  - Pelin päättyminen.
- **Taustamusiikki**: Pelissä soi taustamusiikki, joka alkaa automaattisesti pelin alkaessa ja jatkuu, kunnes peli päättyy tai pelaaja lopettaa sen.

### 2.4 Käyttöliittymä
- **Pelikenttä**: Peliruudukon tulee olla 10 ruutua leveä ja 20 ruutua korkea.
- **Pisteiden näyttö**: Näyttää pelaajan pistemäärän.
- **Tason ja nopeuden näyttö**: Näyttää nykyisen tason ja pelinopeuden.
- **Toiminnot**:
  - Aloitusnäyttö.
  - Pausen ja Restartin painikkeet tai näppäinohjaus.

## 3. Ei-toiminnalliset vaatimukset

### 3.1 Suorituskyky
- Pelin on pysyttävä sujuvana (vähintään 30 FPS) tavallisella tietokoneella.

### 3.2 Yhteensopivuus
- **Alustat**: Peli toimii Windows- ja macOS-käyttöjärjestelmissä.
- **Python-versio**: Peli käyttää Pygamea ja on yhteensopiva vähintään Python 3.8 -version kanssa.

### 3.3 Käytettävyys
- **Ohjeet ja käyttöliittymä**: Pelin käyttöliittymän tulee olla selkeä ja helposti ymmärrettävä. Käyttöohjeet näytetään aloitusnäytössä.
- **Näppäinohjaus**: Pelin tärkeimmät toiminnot ohjataan nuolinäppäimillä, jotta käyttäjän on helppo pelata ilman monimutkaisia komentoja.

### 3.4 Jatkokehitysmahdollisuudet
- Pelin laajennusvaihtoehdot:
  - **Pelitilan valinta**: Mahdollisuus valita vaikeusaste tai pelata eri pelitiloja (esim. ajastettu tai loputon tila).
  - **Pelaajan tulostaulukko**: Näytä parhaat tulokset.
  - **Uudet ääniefektit ja musiikki**: Lisää uusia ääniä ja taustamusiikkeja eri pelitiloihin.

## 4. Testausvaatimukset
- **Yksikkötestaus**: Testaa Tetriminojen liikkuminen, pyöräyttäminen ja pisteiden laskenta.
- **Toiminnallisuuden testaus**: Testaa eri tasot ja pisteytyksen toimivuus.
- **Käyttöliittymän testaus**: Varmista, että kaikki käyttöliittymän elementit näkyvät oikein.



## Backlog
| ID  | Tehtävä                    | Status   | Kuvaus                                                                                  |
|-----|-----------------------------|----------|----------------------------------------------------------------------------------------|
| 1   | Suunnittele käyttöliittymä  | backlog  | Luo pelin käyttöliittymän rakenne, mukaan lukien peliruudukko, pisteet ja painikkeet.  |
| 2   | Kuva layoutista             | Backlog  | Tee layout-kuva peliruudusta, pisteiden laskurista ja muista elementeistä.             |
| 3   | Asenna Pygame               | Backlog  | Asenna Pygame-kirjasto ja varmista, että se toimii oikein kehitysympäristössä.         |
| 4   | Kokeile piirtoa             | Backlog  | Testaa peliruudukon ja Tetrimino-palikoiden piirtäminen ruudukolle.                    |
| 5   | Testaa näppäimistön luku    | Backlog  | Varmista, että nuolinäppäimet toimivat Tetriminojen liikkeiden ja pyöritysten ohjaukseen. |
| 6   | Kokeile ääniefektejä        | Backlog  | Lisää ja testaa ääniefektit, kuten liikkeille ja rivien poistolle.                     |
| 7   | Lisää pisteiden laskenta    | Backlog  | Lisää pisteytysjärjestelmä, joka laskee pisteet poistettujen rivien määrän mukaan.     |
| 8   | Lisää tasojen eteneminen    | Backlog  | Lisää tason nousu, joka lisää pelin nopeutta tietyn pistemäärän jälkeen.               |
| 9   | Lisää pelin lopetus         | Backlog  | Lisää logiikka pelin päättymiselle, kun peliruudukko täyttyy eikä uusia palikoita voi sijoittaa. |
| 10  | Lisää taustamusiikki        | Backlog  | Lisää taustamusiikki, joka soi pelin aikana.                                           |




## Kanban Taulun status-kuvaukset

- **Backlog**: Kaikki tehtävät, jotka odottavat tekemistä.
- **TODO**: Tehtävät, jotka ovat työn alla.
- **Done**: Valmiit tehtävät.

### Leiska (Layout) Kuva
Kesken


## Projektin aikataulu

- **28.10.2024**: Aiheen valinta ja projektin sääntöjen selvittely. Siivosin oman GitHubini, loin uuden repositorion ja valitsin projektin aiheen. Esimerkki-ideoiden perusteella päätin toteuttaa Tetris-pelin Pythonin Pygame-kirjastolla. *(4h)*

- **31.10.2024**: Markdown-dokumentin laadinta projektin dokumentointia varten. Dokumenttiin lisättiin vaatimusmäärittely, projektin tehtävälista backlog-tauluna sekä aikataulu, johon pidän kirjaa omasta ajankäytöstäni. *(4h)*


