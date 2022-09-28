# Bibloteket

Kör main.py för att köra programmet.

- [ ]  Böcker
- [ ]  CD-Skivor
- [ ]  Filmer
- [ ]  Lägga till valfria medie typer (Sist av allt?).
  
Bok:
- En titel
- En författare
- Antal sidnummer
- Ett inköpspris
- Ett inköpsår

Film:
- En titel
- En regissör
- En längd
- Ett inköpspris
- Ett inköpsår

CD-Skiva:
- En titel
- Artist
- Antal spår
- En längd
- Ett inköpspris

# Information
All media är värt 100% av inköpsvärdet under inköpsåret, därefter faller värdet med 10% per år jämfört med föregående år.

När en bok är 50 år gammal så upphör värdeminskningen och ökar istället i värde med 8% varje år.

CD-Skivans värde beror inte på hur gammal skivan är utan på hur många andra skivor det finns med samma titel och artist. Värdet ska räknas ut som "Inköpgspris/Antal liknande skivor".
Avrundas till närmaste hela krona.

Films värde beror också på slitningsgraden vid inköp. Ett värde på 10 innebär att vara är i mycket gott skick och då är värdet 100% av inköpspris. 1:a betyder att den är sliten och det är 10% av inköpspriset. 

För att räkna ut värdet av en film så räknar man först ut hur mycket filmen tappat i värde pga ålder. Därefter tar man det värdet multiplicerat med 0.X där X är förslitningsgraden.

# Input / Output
- [ ] Vilken media man vill registrera.
- [ ] Printa ut medias innehål.
- [ ] Printa ut ALL medias innehåll.
- [ ] Kunna söka på specifik titel.
- [ ] Avsluta program förfrågan. 
(Spara all inmatning i en fil.)