# Smarthome
Projektin ideana oli tehdä selain näkymä jolta voi hallita kodin laitteita sekä valoja (demossa käytetään vain pienjännite laitteita, kuten tuuletin sekä 5V dc moottori).

## Demot

[Demo soittolista youtubessa](https://www.youtube.com/playlist?list=PL872ra4gWyJHHP2PqL7meYm0NWhReBfDC)

Videot yksitellen
- [laite hallinta](https://youtu.be/u2J_YK_Ac5w)
- [Ledi nauha](https://youtu.be/TL8Gj2XcA3o)
- [Päivittäinen lämpötila kuvaaja](https://youtu.be/YQpg1T2HOT8)
- [Selain puhelimella](https://youtu.be/HR2bNJK3FMk)
- [Käyttäjä laite oikeus](https://youtu.be/bDn4-d62BpU)
- [Uuden rakennuksen luominen](https://youtu.be/RRGJO__1rMQ)


## Ohjelmat
- [Verkkosivu (Front)](website/src) sisältää kaikki tehdyt react komponentit.
- [Verkkosivu (Back)](api/env) sisältää react ohjelman, joka yhdistää frontendin tietokantaan sekä laitteisiin.
- [Laitteiden lähettämä data](backend/env) Sisältää pienen mqtt ohjelman joka laittaa lämpötila sensorien dataa tietokantaan. Ei ole vielä laitettu flask ohjelmaan.
- [Laitteet](devices) jonka alta löytyy pohja ledi valoille sekä releille.
- [Demo laitteet](devices/DemoDevices) sisältää demossa käytettyjen laitteiden ohjelmat.
  - [Demo outlets](devices/DemoDevices/SH_Demo_Outlets) joutui lisäämään keittiön sekä molempien makuuhuoneiden releet yhteen laittesseesn, sillä ESP32 loppuivat kesken
- [MySQL storedprocedure](DataBase/procedures) tietokantaan tehdyt sql komennot.







