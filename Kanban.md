# Tetris Pelin Kanban Taulu

## Backlog (To Do)

| ID  | Tehtävä                    | Status   | Kuvaus                                                                                  |
|-----|-----------------------------|----------|----------------------------------------------------------------------------------------|
| 6   | Kokeile ääniefektejä        | Backlog  | Lisää ja testaa ääniefektit, kuten liikkeille ja rivien poistolle.                     |
| 7   | Lisää pisteiden laskenta    | Backlog  | Lisää pisteytysjärjestelmä, joka laskee pisteet poistettujen rivien määrän mukaan.     |
| 8   | Lisää tasojen eteneminen    | Backlog  | Lisää tason nousu, joka lisää pelin nopeutta tietyn pistemäärän jälkeen.               |
| 9   | Lisää pelin lopetus         | Backlog  | Lisää logiikka pelin päättymiselle, kun peliruudukko täyttyy eikä uusia palikoita voi sijoittaa. |
| 10  | Lisää taustamusiikki        | Backlog  | Lisää taustamusiikki, joka soi pelin aikana.                                           |
| 11  | Testaa pelin mekaniikat     | Backlog  | Testaa Tetriminojen liikkuminen, pyöräyttäminen ja pisteiden laskenta.                 |
| 12  | Testaa pelin toiminnallisuus| Backlog  | Testaa eri tasot ja pisteytyksen toimivuus.                                            |
| 13  | Testaa pelin Käyttöliittymä | Backlog  | Varmista, että kaikki käyttöliittymän elementit näkyvät oikein.                        |



## In Progress (Työn alla)

| ID  | Tehtävä                    | Status      | Kuvaus                                                                              |
|-----|----------------------------|-------------|--------------------------------------------------------------------------------------|
| 15  | Parantele pelin ulkonäköä  | In Progress | Taustan, tetriminoiden ja muiden elementtien ulkonäön parantelu                      |
| 14  | Tetriminoiden logiikka     | In Progress | Tetriminoiden täytyy jäädä osuessa, generoida ylhäältä aina uuden ja poistaa täydet rivit   |
|     |                            |             |                                                                                      |

## Done (Valmiit tehtävät)

| ID  | Tehtävä                    | Status     | Kuvaus                                                                                |
|-----|----------------------------|------------|---------------------------------------------------------------------------------------|
| 3   | Asenna Pygame              | Done       | Asenna Pygame-kirjasto ja varmista, että se toimii oikein kehitysympäristössä.        |
| 1   | Suunnittele käyttöliittymä | Done       | Luo pelin käyttöliittymän rakenne, mukaan lukien peliruudukko, pisteet ja painikkeet.|
| 2   | Kuva layoutista            | Done       | Tee layout-kuva peliruudusta, pisteiden laskurista ja muista elementeistä.           |
| 4   | Kokeile piirtoa            | Done       | Testaa peliruudukon ja Tetrimino-palikoiden piirtäminen ruudukolle.                  |
| 5   | Tee näppäimistön luku      | Done       | Varmista, että nuolinäppäimet toimivat Tetriminojen liikkeiden ja pyöritysten ohjaukseen. |
|     |                            |            |                                                                                       |

## Projektin aikataulu

- **28.10.2024**: Aiheen valinta ja projektin sääntöjen selvittely. Siivosin oman GitHubini, loin uuden repositorion ja valitsin projektin aiheen. Esimerkki-ideoiden perusteella päätin toteuttaa Tetris-pelin Pythonin Pygame-kirjastolla. *(n. 4 tuntia)*

- **31.10.2024**: Markdown-dokumentin laadinta projektin dokumentointia varten. Dokumenttiin lisättiin vaatimusmäärittely, projektin tehtävälista backlog-tauluna sekä aikataulu, johon pidän kirjaa omasta ajankäytöstäni. *(n. 4 tuntia)*

- **7.11.2024**: Kanban-taulukon ja projektin aikataulun erotus omaan dokumenttiin. Viilasin myös projektin dokumentaatiota sekä kanban-taulua mm. lisäten dokumentointiin asennusohjeen ja tauluun pelin testausvaiheita. Python ja pygame olivat jo asennettuna, joten siirsin taskin valmiiksi ja lisäsin työn alle seuraavaksi suoritettavat tehtävät. Opiskelin myös vähän tekoälyä hyödyntäen, miltä tetris-peli sekä sen koodi pygamella suunnilleen näyttäisi. Loin myös kansion tuleville pelitiedostoille sekä pygame venv-kansion. *(n. 4 tuntia)*
- **11.11.2024**: Suunnittelin ja toteutin layout-kuvan pelin päänäkymälle powerpointilla. Lisäsin kuvan sekä projektin dokumentaatioon, että omaan kansioonsa repositoriossa. *(n. 3 tuntia)*
- **14.11.2024**: Toteutin ensimmäisen version pelistä. päätin tähän mennessä jakaa pelin koodin kolmeen tiedostoon. Yksi pelin main loopille, yksi funktioille ja yksi tetriminoluokalle.
Pelissä on tällä hetkellä tetriminot, pelin ruudukko sekä vähän alkuperäistä piirustusta muistuttava taustaväri. Tetriminoita voi liikutella ja pyöritellä, tosin peli ei koskaan lopu, vaan palikoiden täyttyessä ylös asti peliä ei voi enää pelata, koska palikat ovat päällekäin. Tetriminoiden logiikassa saattaa olla korjaamisen varaa. Pelissä on nyt 5 fps tahti, joka ei muutu. Rivien poisto toimii. Lisään seuraavalla kerralla toiminnon, jolla space-napilla saa palikan suoraan alas, kun se jäi tekemättä tällä kertaa. *(n. 4 tuntia)*