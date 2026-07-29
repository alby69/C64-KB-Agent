---
title: RS-232 status
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
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
  address: $0297
  symbol: RSSTAT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 status register
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier werden die Fehlermeldungen der
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'RS-232: 6551 Status Register Image'
  - name: Memory Map
    author: Jim Butterfield
    description: RS-232 status
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The contents of this register indicate the error status of RS-232
      data
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64'er Magazin
    author: 64'er
    description: Genauso wie in der Speicherzelle 144 der Status aller Ein- und Ausgabe-
  - name: 64map
    author: —
    description: RS232 Pseudo 6551 Status Register Image
---

# RSSTAT — RS-232 status ($0297)

## Panoramica
Il registro o area di memoria RSSTAT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0297` (`663` decimale)
- **Range**: `$0297`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 status register

### Commodore-64-intern-Buch (Commodore)
Hier werden die Fehlermeldungen der
RS-232 Schnittstelle angezeigt:

| Bit | Wert  | Bedeutung                        |
|-----|-------|----------------------------------|
|  0  |   1   | Fehler bei Parity-Prüfung        |
|  1  |   2   | Fehler in der Bitfolge           |
|  2  |   4   | Überlauf des Eingabepuffers      |
|  3  |   8   | Eingabepuffer ist leer           |
|  4  |  16   | das CTS-Signal fehlt             |
|  5  |  32   | nicht belegt                     |
|  6  |  64   | Das DSR-Signal fehlt             |
|  7  | 128   | Die Übertragung ist unterbrochen |

### C64 Programmer's Reference Guide (Commodore)
RS-232: 6551 Status Register Image

### Memory Map (Jim Butterfield)
RS-232 status

### Mapping the Commodore 64 (Sheldon Leemon)
The contents of this register indicate the error status of RS-232 data
transmission.  That status can be determined by PEEKing this location
directly, by referencing the BASIC reserved variable ST, or by using
the Kernal READST (65031, $FE07) routine.

Note that if you use ST or Kernal, this location will be set to 0
after it is read.  Therefore, if you need to test more than one bit,
make sure that each test preserves the original value, because you
won't be able to read it again.  The meaning of each bit value is
specified below:

|Bit|Value|                                         |
|---|-----|-----------------------------------------|
| 7 | 128 | 1 = Break Detected                      |
| 6 | 64  | 1 = DTR (Data Set Ready) Signal Missing |
| 5 |     | Unused                                  |
| 4 | 16  | 1 = CTS (Clear to Send) Signal Missing  |
| 3 | 8   | 1 = Receiver Buffer Empty               |
| 2 | 4   | 1 = Receiver Buffer Overrun             |
| 1 | 2   | 1 = Framing Error                       |
| 0 | 1   | 1 = Parity Error                        |

The user is responsible for checking these errors and taking
appropriate action.  If, for example, you find that Bit 0 or 1 is set
when you are sending, indicating a framing or parity error, you should
resend the last byte.  If Bit 2 is set, the GET#2 command is not being
executed quickly enough to empty the buffer (BASIC should be able to
keep up at 300 baud, but not higher).  If Bit 7 is set, you will want
to stop sending, and execute a GET#2 to see what is being sent.

### Reference (Joe Forster / STA)
Bits:

* Bit #0: 1 = Parity error occurred.
* Bit #1: 1 = Frame error, a stop bit with the value of 0, occurred.
* Bit #2: 1 = Input buffer underflow occurred, too much data has arrived but it has not been read from the buffer in time.
* Bit #3: 1 = Input buffer is empty, nothing to read.
* Bit #4: 0 = Sender is Clear To Send; 1 = Sender is not ready to send data to receiver.
* Bit #6: 0 = Receiver reports Data Set Ready; 1 = Receiver is not ready to receive data.
* Bit #7: 1 = Carrier loss, a stop bit and a data byte both with the value of 0, detected.

### 64'er Magazin (64'er)
Genauso wie in der Speicherzelle 144 der Status aller Ein- und Ausgabe-
Operationen angezeigt wird, werden alle Fehler der RS232-Schnittstelle in der
Speicherzelle 663 angezeigt. Die Bedeutung der einzelnen Bits, wenn sie auf 1
gesetzt sind, zeigt Tabelle 14.

Der Status wird nicht automatisch angezeigt, sondern muß vom Programm abgefragt
werden. Abfragen können Sie sowohl durch PEEKen der Speicherzelle 663 als auch
durch Aufrufen der Statusvariablen ST. Die Variable ST, die normalerweise den
Inhalt der Zelle 144 wiedergibt, schaltet nach dem Eröffnen eines RS232-Kanals
durch OPEN 1,2 auf die Speicherzelle 663 um. Jedoch ist Vorsicht geboten, da
durch Aufruf von ST der Inhalt von 663 gelöscht wird.

Es ist ratsam, den Wert von ST erst einer anderen Variablen zuzuordnen, wenn
sie mehrfach verwendet werden soll.

Falls das Status-Register einen Fehler anzeigt, muß das Programm entsprechende
Konsequenzen ziehen. Wenn zum Beispiel Bit 0 oder Bit 1 gesetzt sind, ist es
angebracht, das letzte Daten-Byte noch einmal zu übertragen. Wenn Bit 2 gesetzt
ist, heißt dies, daß der GET #-Befehl den Eingabepufferspeicher nicht schnell
genug entleert. Falls die Übertragungsgeschwindigkeit von 300 Bit/s, die
maximal mit einem Basic-Programm erreichbar ist, nicht ausreicht, muß entweder
der Sender langsamer eingestellt werden, oder Sie schreiben das Programm in
Maschinensprache.

### 64map (—)
RS232 Pseudo 6551 Status Register Image

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*