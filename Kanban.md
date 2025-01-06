# Tetris Pelin Kanban Taulu

## Backlog (To Do)

| ID  | Tehtävä                    | Status   | Kuvaus                                                                                  |
|-----|-----------------------------|----------|----------------------------------------------------------------------------------------|
| 6   | Kokeile ääniefektejä        | Backlog  | Lisää ja testaa ääniefektit, kuten liikkeille ja rivien poistolle.                     |
| 7   | Lisää pisteiden laskenta    | Backlog  | Lisää pisteytysjärjestelmä, joka laskee pisteet poistettujen rivien määrän mukaan.     |
| 8   | Lisää tasojen eteneminen    | Backlog  | Lisää tason nousu, joka lisää pelin nopeutta tietyn pistemäärän jälkeen.               |
| 10  | Lisää taustamusiikki        | Backlog  | Lisää taustamusiikki, joka soi pelin aikana.                                           |
| 11  | Testaa pelin mekaniikat     | Backlog  | Testaa Tetriminojen liikkuminen, pyöräyttäminen ja pisteiden laskenta.                 |
| 12  | Testaa pelin toiminnallisuus| Backlog  | Testaa eri tasot ja pisteytyksen toimivuus.                                            |
| 13  | Testaa pelin Käyttöliittymä | Backlog  | Varmista, että kaikki käyttöliittymän elementit näkyvät oikein.                        |
| 19  | Haamupalikan on/off togglaus| Backlog  | Haamupalikan käyttö tulisi olla vapaaehtoista, sillä se helpottaa peliä paljon. Palikan voisi togglata joko sidebarista tai gameover-näkymästä.       |




## In Progress (Työn alla)

| ID  | Tehtävä                    | Status      | Kuvaus                                                                               |
|-----|----------------------------|-------------|--------------------------------------------------------------------------------------|
| 15  | Parantele pelin ulkonäköä  | In Progress | Taustan, tetriminoiden ja muiden elementtien ulkonäön parantelu                      |
|     |                            |             |                                                                                      |

## Done (Valmiit tehtävät)

| ID  | Tehtävä                    | Status     | Kuvaus                                                                                |
|-----|----------------------------|------------|---------------------------------------------------------------------------------------|
| 3   | Asenna Pygame              | Done       | Asenna Pygame-kirjasto ja varmista, että se toimii oikein kehitysympäristössä.        |
| 1   | Suunnittele käyttöliittymä | Done       | Luo pelin käyttöliittymän rakenne, mukaan lukien peliruudukko, pisteet ja painikkeet. |
| 2   | Kuva layoutista            | Done       | Tee layout-kuva peliruudusta, pisteiden laskurista ja muista elementeistä.            |
| 4   | Kokeile piirtoa            | Done       | Testaa peliruudukon ja Tetrimino-palikoiden piirtäminen ruudukolle.                   |
| 5   | Tee näppäimistön luku      | Done       | Varmista, että nuolinäppäimet toimivat Tetriminojen liikkeiden ja pyöritysten ohjaukseen. |
| 16  | Haamutetriminopalikka      | Done       | Palikan pudotessa täytyy alhaalla näkyä palikan muoto siinä kohdalla, mihin se putoaisi.      |
| 14  | Tetriminoiden logiikka     | Done       | Tetriminoiden täytyy jäädä osuessa, generoida ylhäältä aina uuden ja poistaa täydet rivit   |
| 9   | Lisää pelin lopetus        | Done       | Lisää logiikka pelin päättymiselle, kun peliruudukko täyttyy eikä uusia palikoita voi sijoittaa. |
| 17  | Tee Game over -näkymä      | Done       | Pelin loppuessa täytyy tulla Game over -ikkuna, josta pelin voi lopettaa tai aloittaa. |
| 18  | Sivupalkin lisäys          | Done       | Sivupalkki peliin, johon voi lisätä suunnitelman mukaisesti UI-elementtejä.           |
|     |                            |            |                                                                                       |

## Projektin aikataulu

- **28.10.2024**: Aiheen valinta ja projektin sääntöjen selvittely. Siivosin oman GitHubini, loin uuden repositorion ja valitsin projektin aiheen. Esimerkki-ideoiden perusteella päätin toteuttaa Tetris-pelin Pythonin Pygame-kirjastolla. *(n. 4 tuntia)*

- **31.10.2024**: Markdown-dokumentin laadinta projektin dokumentointia varten. Dokumenttiin lisättiin vaatimusmäärittely, projektin tehtävälista backlog-tauluna sekä aikataulu, johon pidän kirjaa omasta ajankäytöstäni. *(n. 4 tuntia)*

- **7.11.2024**: Kanban-taulukon ja projektin aikataulun erotus omaan dokumenttiin. Viilasin myös projektin dokumentaatiota sekä kanban-taulua mm. lisäten dokumentointiin asennusohjeen ja tauluun pelin testausvaiheita. Python ja pygame olivat jo asennettuna, joten siirsin taskin valmiiksi ja lisäsin työn alle seuraavaksi suoritettavat tehtävät. Opiskelin myös vähän tekoälyä hyödyntäen, miltä tetris-peli sekä sen koodi pygamella suunnilleen näyttäisi. Loin myös kansion tuleville pelitiedostoille sekä pygame venv-kansion. *(n. 4 tuntia)*

- **11.11.2024**: Suunnittelin ja toteutin layout-kuvan pelin päänäkymälle powerpointilla. Lisäsin kuvan sekä projektin dokumentaatioon, että omaan kansioonsa repositoriossa. *(n. 3 tuntia)*

- **14.11.2024**: Toteutin ensimmäisen version pelistä. päätin tähän mennessä jakaa pelin koodin kolmeen tiedostoon. Yksi pelin main loopille, yksi funktioille ja yksi tetriminoluokalle.
Pelissä on tällä hetkellä tetriminot, pelin ruudukko sekä vähän alkuperäistä piirustusta muistuttava taustaväri. Tetriminoita voi liikutella ja pyöritellä, tosin peli ei koskaan lopu, vaan palikoiden täyttyessä ylös asti peliä ei voi enää pelata, koska palikat ovat päällekäin. Tetriminoiden logiikassa saattaa olla korjaamisen varaa. Pelissä on nyt 5 fps tahti, joka ei muutu. Rivien poisto toimii. Lisään seuraavalla kerralla toiminnon, jolla space-napilla saa palikan suoraan alas, kun se jäi tekemättä tällä kertaa. *(n. 4 tuntia)*

- **16.11.2024**: Parantelin vähän pelin toiminnallisuutta. Lisäsin haamupalikan sinne, mihin palikka on laskeutumassa ja parantelin vähän törmäyslogiikkaa. Lisäsin hard drop -funktion spacebar -nappiin niin kuin viimeksi mainitsin. Lisäsin myös logiikan pelin loppumiselle sekä jonkinlaisen version game over-näkymästä pelin häviämisen yhteydessä. Erotin pelin loppumiseen liittyvän koodin omaan tiedostoonsa, jotta main.py pysyisi edes jossain määrin kompaktina. *(n. 3 tuntia)*

- **8.12.2024**: Kokeilin tehdä sivupalkkia, johon saisi pisteet, seuraavan palikan jne. Ei onnistunut tällä kertaa, joten päädyin vain siistimään vähän koodia siirtämällä koodin kaikki constant-muuttujat omaan tiedostoonsa. (*n. 2 tuntia)*

- **6.1.2025**: siirsin main.py gameloopin määrittelyn tiedostoon functions.py. Lisäsin sivupalkin, johon lisään seuraavalla kerralla tarvittavat UI elementit. Pelin logiikkaa täytyi aika paljon muutella, jotta palkin sai lisättyä rikkomatta pelin toimintaa. (*n. 3 tuntia)
