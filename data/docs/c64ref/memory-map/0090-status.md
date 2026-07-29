---
title: Status word ST
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
  address: $0090
  symbol: STATUS
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: I/O operation status byte
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In dieser Speicherzelle, die auch mit
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Kernal I/O Status Word: ST'
  - name: Memory Map
    author: Jim Butterfield
    description: Status word ST
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The Kernal routines which open I/O channels or perform input/output
  - name: Reference
    author: Joe Forster / STA
    description: 'Serial bus bits:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Adresse enthält ein Byte, welches mit der Statusvariablen ST
      von Basic
  - name: 64map
    author: —
    description: Kernal I/O Status Word  ST
---

# STATUS — Status word ST ($0090)

## Panoramica
Il registro o area di memoria STATUS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0090` (`144` decimale)
- **Range**: `$0090`
- **Dimensione**: `1 byte`
- **Permessi**: `R`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
I/O operation status byte

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle, die auch mit
der BASIC-Variable ST identisch ist,
sind die Fehlermeldungen der Datasette
und der Floppy verzeichnet:

| Bit | Datasette        |
|-----|------------------|
| 0   | Unbenutzt        |
| 1   | Unbenutzt        |
| 2   | Kurzer Block     |
| 3   | Langer Block     |
| 4   | Lesefehler       |
| 5   | Prüfsummenfehler |
| 6   | File-Ende        |
| 7   | Band-Ende        |

| Bit | Floppy                   |
|-----|--------------------------|
| 0   | Fehler beim Schreiben    |
| 1   | Fehler beim Lesen        |
| 2   | Unbenutzt                |
| 3   | Unbenutzt                |
| 4   | Unbenutzt                |
| 5   | Unbenutzt                |
| 6   | Daten-Ende               |
| 7   | DEVICE NOT PRESENT ERROR |

### C64 Programmer's Reference Guide (Commodore)
Kernal I/O Status Word: ST

### Memory Map (Jim Butterfield)
Status word ST

### Mapping the Commodore 64 (Sheldon Leemon)
The Kernal routines which open I/O channels or perform input/output
functions check and update this location.  The value here is almost
always the same as that returned to BASIC by use of the reserved
variable ST.  Note that BASIC syntax will not allow an assignment such
as ST=4.  A table of status codes for cassette and serial devices
follows below:

| Bit | Bit Value | Cassette                             |
|-----|-----------|--------------------------------------|
| 2   | 4         | Short Block                          |
| 3   | 8         | Long Block                           |
| 4   | 16        | Unrecoverable error (Read), mismatch |
| 5   | 32        | Checksum error                       |
| 6   | 64        | End of file                          |

| Bit | Bit Value | Serial Devices                       |
|-----|-----------|--------------------------------------|
| 0   | 1         | Time out (Write)                     |
| 1   | 2         | Time out (Read)                      |
| 6   | 64        | EOI (End or Identify)                |
| 7   | 128       | Device not present                   |

Probably the most useful bit to test is Bit 6 (end of file).  When
using the GET statement to read in individual bytes from a file, the
statement IF ST AND 64 will be true if you have got to the end of the
file.

For status codes for the RS-232 device, see the entry for location 663
($0297).

### Reference (Joe Forster / STA)
Serial bus bits:

* Bit #0: Transfer direction during which the timeout occurred; 0 = Input; 1 = Output.
* Bit #1: 1 = Timeout occurred.
* Bit #4: 1 = VERIFY error occurred (only during VERIFY), the file read from the device did not match that in the memory.
* Bit #6: 1 = End of file has been reached.
* Bit #7: 1 = Device is not present.

Datasette bits:

* Bit #2: 1 = Block is too short (shorter than 192 bytes).
* Bit #3: 1 = Block is too long (longer than 192 bytes).
* Bit #4: 1 = Not all bytes read with error during pass 1 could be corrected during pass 2, or a VERIFY error occurred, the file read from the device did not match that in the memory.
* Bit #5: 1 = Checksum error occurred.
* Bit #6: 1 = End of file has been reached (only during reading data files).

### 64'er Magazin (64'er)
Diese Adresse enthält ein Byte, welches mit der Statusvariablen ST von Basic
identisch ist. Diese reservierte Variable ist im Texteinschub Nr. 14 »ST-atus«
näher beschrieben.

Alle Routinen des Betriebssystems, die mit Ein- und Ausgabe zu tun haben,
benutzen diese Speicherzelle zum Abspeichern und Abfragen des Status der Ein-/
Ausgabeoperationen.

Genauer gesagt, alle Ein-/Ausgabeoperationen, die mit der Datasette und mit dem
Floppy-Gerät beziehungsweise dem Drucker zu tun haben, benutzen die Adresse
144. Im Fachjargon sprechen wir vom Kassetten-Port und vom seriellen Port.

Der dritte Anschluß des Computers, nämlich der RS232 oder User-Port, benutzt
für den Status die Speicherzelle 663.

Jedes Bit der Zelle 144 hat eine eigene Bedeutung wie folgt.

| Bit | Wert | Kassette                        |
|-----|------|---------------------------------|
| 2   | 4    | Kurzer Block                    |
| 3   | 8    | Langer Block                    |
| 4   | 16   | Lesefehler (nicht korrigierbar) |
| 5   | 32   | Prüfsummenfehler                |
| 6   | 64   | File-Ende                       |
| 7   | 128  | Band-Ende                       |

| Bit | Wert | Floppy/Drucker                  |
|-----|------|---------------------------------|
| 0   | 1    | Fehler beim Schreiben           |
| 1   | 2    | Fehler beim Lesen               |
| 6   | 64   | Daten-Ende                      |
| 7   | 128  | »Device Not Present«-Fehler     |

Alle nicht aufgeführten Bits sind nicht benutzt.

Diese Speicherzelle beziehungsweise die Statusvariable ST kann recht nützlich
sein. Einige Kochrezepte dafür werden im Texteinschub Nr. 14 behandelt.

### 64map (—)
Kernal I/O Status Word  ST

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*