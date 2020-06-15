# Connect 4

https://en.wikipedia.org/wiki/Connect_Four

Projekt został wykonany na laboratoria z języków symbolicznych.
## Opis Zadania
○ Okno wyświetlające siatkę 7 kolumn x 6 wierszy, przycisk nad każdą kolumną,
informację “Tura gracza 1” lub “Tura gracza 2”
Gracze na zmianę wrzucają monety do wybranych przez siebie kolumn.
○ Gracze wybierają kolumnę klikając przycisk nad nią.
○ Wygrywa gracz który pierwszy ustawi cztery monety w linii (poziomo, pionowo
lub po skosie).
○ Gdy gra się kończy, wyświetlane jest okienko z napisem “Wygrał gracz 1” lub
“Wygrał gracz 2”, zależnie kto wygrał grę. Możliwe jest zresetowanie planszy
bez zamykania głównego okna.
○ Reprezentacja reguł gry ma być realizowana poprzez hierarchię klas. Klasa
bazowa definiuje między innymi funkcję wirtualną ktoWygral() nadpisywaną w
klasach pochodnych. Realizowane powinny być przynajmniej dwa zestawy reguł,
jako dwie klasy pochodne.
Testy
1. Wykonanie po dwa ruchy przez każdego z graczy - monety spadają na dół pola
gry lub zatrzymują się na już wrzuconym żetonie.
2. Ułożenie pionowej linii monet przez jednego gracza - oczekiwana informacja o
jego wygranej.
3. Ułożenie poziomej linii monet przez drugiego gracza - oczekiwana informacja o
jego wygranej.
4. Ułożenie skośnej linii przez dowolnego gracza - oczekiwana informacja o
jego wygranej.
5. Zapełnienie pola gry tak, że żaden gracz nie ułożył linii - oczekiwana informacja
o remisie.

## Author
Radioaktyv
