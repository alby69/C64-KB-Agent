---
title: Jiffy Clock HML
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $00A0
  address_end: $00A2
  symbol: TIME
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 24 hour clock in 1/60th seconds
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesen Speicherzellen wird die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Real-Time Jiffy Clock (approx) 1/60 Sec
  - name: Memory Map
    author: Jim Butterfield
    description: Jiffy Clock HML
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: These three locations are updated 60 times a second, and serve as
      a
  - name: Reference
    author: Joe Forster / STA
    description: 'Values: $000000-$4F19FF, 0-518399 (on PAL machines).'
  - name: 64'er Magazin
    author: 64'er
    description: Das Basic der Commodore-Computer kennt neben der Variablen ST (siehe
  - name: 64map
    author: —
    description: Real-time jiffy Clock (Updated by IRQ Interrupt approx. every 1/60
      of Second)...
---

# TIME — Jiffy Clock HML ($00A0)

## Panoramica
Il registro o area di memoria TIME è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A0` (`160` decimale)
- **Range**: `$00A0`-`$00A2`
- **Dimensione**: `3 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
24 hour clock in 1/60th seconds

### Commodore-64-intern-Buch (Commodore)
In diesen Speicherzellen wird die
Uhrzeit über die Interruptroutine
erhöht.

### C64 Programmer's Reference Guide (Commodore)
Real-Time Jiffy Clock (approx) 1/60 Sec

### Memory Map (Jim Butterfield)
Jiffy Clock HML

### Mapping the Commodore 64 (Sheldon Leemon)
These three locations are updated 60 times a second, and serve as a
software clock which counts the number of jiffies (sixtieths of a
second) that have elapsed since the computer was turned on.

The value of location 162 ($00A2) is increased every jiffy (0.1667
second), 161 ($00A1) is updated every 256 jiffies (4.2267 seconds), and
160 ($00A0) changes every 65536 jiffies (or every 18.2044 minutes).
After 24 hours, these locations are set back to 0.

The jiffy clock is used by the BASIC reserved variables TI and TI$.
These are not ordinary variables that are stored in the RAM variable
area, but are functions that call the Kernal routines RDTIM (63197,
$F6DD), and SETTIM (63204, $F6E4).  Assigning the value of TI or TI$
to another variable reads these locations, while assigning a given
value to TI$ alters these locations.

To illustrate the relationship between these locations and TI$, try
the following program.  The program sets the jiffy clock to 23 hours,
50 minutes.  After the program has been running for one minute, all
these locations will be reset to 0.

    100 TI$="235900"
    110 PRINT TI$,PEEK(160),PEEK(161),PEEK(162)
    120 GOTO 110

Since updating is done by the IRQ interrupt that reads the keyboard,
anything which affects the operation of that interrupt routine will
also interfere with this clock.  A typical example is tape I/O
operations, which steal the IRQ vector for their own use, and restore
it afterwards.  Obviously, user routines which redirect the IRQ and do
not send it back to the normal routine will upset software clock
operation as well.

### Reference (Joe Forster / STA)
Values: $000000-$4F19FF, 0-518399 (on PAL machines).

### 64'er Magazin (64'er)
Das Basic der Commodore-Computer kennt neben der Variablen ST (siehe
Speicherzelle 144) noch zwei weitere »reservierte« Variable, nämlich TI und
TI$. Beide bieten eine interne Uhr, welche aus dem Inhalt der Speicherzellen
160 bis 162 abgeleitet wird. Diese drei Zellen funktionieren wie der
Kilometerzähler eines Autos, halt nur mit drei Stellen.

Die hinterste Stelle ist die Zelle 162. Ihr Inhalt wird beim Einschalten des
Computers auf 0 gesetzt, dann aber 60mal in der Sekunde um 1 erhöht. Das
erfolgt durch die automatische Interrupt-Routine, welche auch die STOP-Taste
abfragt und noch andere Hausaufgaben 60mal in der Sekunde ausführt. Da i60 =
0,01667 ist, zählt also dle Zelle 162 in 0,01667 Sekunden um 1 weiter. Sie kann
wie alle Speicherzellen maximal nur die Zahl 255 enthalten, danach kommt wieder
eine 0. Das heißt aber, daß sie nach 256 * 0,01667 = 4,267 Sekunden einmal
durchgelaufen ist.

Nach jedem Durchlauf wird die davorliegende Speicherzelle 161 um 1 erhöht. Sie
zählt also in 4,267 Sekunden um 1 weiter und ist nach 256 * 4.067 = 1 092,26
Sekunden oder besser nach 18,2044 Minuten einmal durchgelaufen. Nach dem
Kilometerzähler-Prinzip wird nach jedem Durchlauf von 161 der Inhalt der
davorliegenden Zelle 160 um 1 erhöht.

Die Zelle 160 zählt also in 18,2044 Minuten um 1 weiter und ist nach 256 * 18,
2044 = 4660,34 Minuten, das sind 77.67 Stunden, einmal durchgelaufen.

Diese Stundenzahl wird allerdings niemals erreicht, da das Betriebssystem nach
Erreichen des Wertes für 24 Stunden alle drei Zellen wieder auf 0 zurücksetzt.
Wir werden das gleich nachprüfen.

Zuerst aber wollen wir uns den dreizelligen Zähler anschauen:

    10 PRINT PEEK(160);PEEK(161);PEEK(162)
    20 GOTO 10

Nach RUN sehen wir den Inhalt der drei Zellen sich entsprechend der oben
angegebenen Zeiten verändern. Die Zahlen sind nicht vorherbestimmbar, denn der
Zähler ist ja nach dem Einschalten des Computers schon losgelaufen. Er kann
aber auf 0 gesetzt werden durch Einfügen der Zeile 5:

    5 POKE 160,0:POKE 161,0: POKE 162,0

Jetzt beginnt der Zähler immer ab 0. Ich habe gerade gesagt, daß der Zähler auf
0 gesetzt wird, wenn er 24 Stunden lang gelaufen ist. Der Inhalt in den drei
Speicherzellen, der 24 Stunden entspricht, ist nach der oben angegebenen
Umrechnungsart 79-26-0. Diesen Wert, oder besser noch ein Wert kurz davor, in
die Zellen 160 bis 162 gePOKEt, zeigt uns den Nullsetzvorgang. Ersetzen Sie
bitte die obige Zeile 5 durch eine neue Zeile:

    5 POKE 160,79:POKE 161,25:POKE 162,0

Nach vier Sekunden Laufzeit schalten alle drei Zellen in der Tat auf 0 zurück.

Die Umsetzung der Zahlen aus 160 bis 162 in die Variablen TI und TI$ sowie
deren Wirkungsweise entnehmen Sie bitte dem Texteinschub Nr. 16 »Die eingebaute
Uhr«.

Abschließend muß eines noch warnend erwähnt werden. Alle Operationen, welche
den Interrupt-Vektor verwenden beziehungsweise verändern, stören oder verzögern
die normale Interrupt-Routine, die ja den Zähler weiterstellt. So zählt der
Zähler nicht gleichmäßig und die daraus abgeleitete Uhr geht nicht mehr
richtig. Ein Beispiel dafür sind alle Ein- und Ausgaben über die Datasette,
welche über einen Interrupt laufen.

### 64map (—)
Real-time jiffy Clock (Updated by IRQ Interrupt approx. every 1/60 of Second); Update Routine: UDTIMK ($F69B)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*