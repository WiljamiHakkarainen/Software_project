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

### 3.5. Testausvaatimukset
- **Yksikkötestaus**: Testaa Tetriminojen liikkuminen, pyöräyttäminen ja pisteiden laskenta.
- **Toiminnallisuuden testaus**: Testaa eri tasot ja pisteytyksen toimivuus.
- **Käyttöliittymän testaus**: Varmista, että kaikki käyttöliittymän elementit näkyvät oikein.

## 4. Asennusohjeet

Pelin asentaminen edellyttää, että tietokoneella on Python 3.8 tai uudempi asennettuna.

###  1: Asenna Python
Jos Python ei ole vielä asennettu, lataa se https://www.python.org/downloads/ ja asenna se.

### 2: Asenna Pygame
Pygame on Pythonin kirjasto, joka mahdollistaa pelin kehittämisen. Asenna se syöttämällä terminaalin komento: pip install pygame

### 3: Hae Tetris-pelin lähdekoodi Githubista

Pelin lähdekoodin saa täältä : https://github.com/WiljamiHakkarainen/Software_project

### 4: kopioi koodit kansioon ja aja pelin main-tiedosto terminaalissa

Syötä terminaaliin esimerkiksi: 
1. cd tetris_game
2. python main.py



## Aluksi suunniteltu pelinäkymä
![GAME UI Sketch](images/Tetris_UI.jpg)


