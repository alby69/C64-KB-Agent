---
title: initialise VIC and screen editor
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ff81-betriebssystem-routinen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FF81
  address_end: $FF81
  symbol: initialise-vic-and-screen-editor
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF81**: initialise VIC and screen editor'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FF81**: Video-Reset'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FF81**: initialise screen and keyboard'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FF81**: CINT, init screen editor'
---

# $FF81 — initialise VIC and screen editor

## Disassemblatura
```assembly
.FF81  4C 5B FF JMP $FF5B   ; initialise VIC and screen editor
```


## Commenti

### Original Disassembly (—)
- **$FF81**: initialise VIC and screen editor

### Commodore-64-intern-Buch (Commodore)
- **$FF81**: Video-Reset
- **$FF84**: CIAs initialisieren
- **$FF87**: RAM löschen bzw. testen
- **$FF8A**: I/O initialisieren
- **$FF8D**: I/O Vektoren initialisieren
- **$FF90**: Status setzen
- **$FF93**: Sekundäradresse nach LISTEN senden
- **$FF96**: Sekundäradresse nach TALK senden
- **$FF99**: RAM-Ende setzen/holen
- **$FF9C**: RAM-Anfang setzen/holen
- **$FF9F**: Tastatur abfragen
- **$FFA2**: Time-out-Flag für IEC-Bus setzen
- **$FFA5**: Eingabe vom IEC-Bus
- **$FFA8**: Ausgabe vom IEC-Bus
- **$FFAB**: UNTALK senden
- **$FFAE**: UNLISTEN senden
- **$FFB1**: LISTEN senden
- **$FFB4**: TALK senden
- **$FFB7**: Status holen
- **$FFBA**: Fileparameter setzen
- **$FFBD**: Filenamenparameter setzen
- **$FFC0**: $F34A OPEN
- **$FFC3**: $F291 CLOSE
- **$FFC6**: $F20E CHKIN Eingabeg. setzen
- **$FFC9**: $F250 CKOUT Ausgabegerät set.
- **$FFCC**: $F333 CLRCH Ein-Ausgabe zurücksetzen
- **$FFCF**: $F157 BASIN Eingabe eines Zeichens
- **$FFD2**: $F1CA BSOUT Ausgabe eines Zeichens
- **$FFD5**: LOAD
- **$FFD8**: SAVE
- **$FFDB**: Time setzen
- **$FFDE**: Time holen
- **$FFE1**: $F6ED STOP-Taste abfragen
- **$FFE4**: $F13E GET
- **$FFE7**: $F32F CLALL
- **$FFEA**: Time erhöhen
- **$FFED**: SCREEN Anzahl Zeilen und Spalten holen
- **$FFF0**: Cursor setzen / Cursorposition holen
- **$FFF3**: Startadresse des I/O-Bausteins holen

### Marko Mäkelä (Marko Mäkelä)
- **$FF81**: initialise screen and keyboard
- **$FF84**: initialise I/O devices
- **$FF87**: initialise memory pointers
- **$FF8A**: restore I/O vectors
- **$FF8D**: set I/O vectors from XY
- **$FF90**: control kernal messages
- **$FF93**: read secondary address after listen
- **$FF96**: read secondary address after talk
- **$FF99**: read/set top of memory
- **$FF9C**: read/set bottom of memory
- **$FF9F**: scan keyboard
- **$FFA2**: set timeout for serial bus
- **$FFA5**: input on serial bus
- **$FFA8**: output byte on serial bus
- **$FFAB**: send untalk on serial bus
- **$FFAE**: send unlisten on serial bus
- **$FFB1**: send listen on serial bus
- **$FFB4**: send talk on serial bus
- **$FFB7**: read I/O status word
- **$FFBA**: set file parameters
- **$FFBD**: set filename parameters
- **$FFC0**: (F34A) open a file
- **$FFC3**: (F291) close a file
- **$FFC6**: (F20E) set input device
- **$FFC9**: (F250) set output device
- **$FFCC**: (F333) restore I/O devices to default
- **$FFCF**: (F157) input char on current device
- **$FFD2**: (F1CA) output char on current device
- **$FFD5**: load ram from device
- **$FFD8**: save ram to device
- **$FFDB**: set real time clock
- **$FFDE**: read real time clock
- **$FFE1**: (F6ED) check stop key
- **$FFE4**: (F13E) get a character
- **$FFE7**: (F32F) close all channels and files
- **$FFEA**: increment real time clock
- **$FFED**: read organisation of screen into XY
- **$FFF0**: read/set XY cursor position
- **$FFF3**: read base address of I/O devices

### Magnus Nyman (Magnus Nyman)
- **$FF81**: CINT, init screen editor
- **$FF84**: IOINT, init input/output
- **$FF87**: RAMTAS, init RAM, tape screen
- **$FF8A**: RESTOR, restore default I/O vector
- **$FF8D**: VECTOR, read/set I/O vector
- **$FF90**: SETMSG, control KERNAL messages
- **$FF93**: SECOND, send SA after LISTEN
- **$FF96**: TKSA, send SA after TALK
- **$FF99**: MEMTOP, read/set top of memory
- **$FF9C**: MEMBOT, read/set bottom of memory
- **$FF9F**: SCNKEY, scan keyboard
- **$FFA2**: SETTMO, set IEEE timeout
- **$FFA5**: ACPTR, input byte from serial bus
- **$FFA8**: CIOUT, output byte to serial bus
- **$FFAB**: UNTALK, command serial bus UNTALK
- **$FFAE**: UNLSN, command serial bus UNLSN
- **$FFB1**: LISTEN, command serial bus LISTEN
- **$FFB4**: TALK, command serial bus TALK
- **$FFB7**: READST, read I/O status word
- **$FFBA**: SETLFS, set logical file parameters
- **$FFBD**: SETNAM, set filename
- **$FFC0**: OPEN, open file
- **$FFC3**: CLOSE, close file
- **$FFC6**: CHKIN, prepare channel for input
- **$FFC9**: CHKOUT, prepare channel for output
- **$FFCC**: CLRCHN, close all I/O
- **$FFCF**: CHRIN, input byte from channel
- **$FFD2**: CHROUT, output byte to channel
- **$FFD5**: LOAD, load from serial device
- **$FFD8**: SAVE, save to serial device
- **$FFDB**: SETTIM, set realtime clock
- **$FFDE**: RDTIM, read realtime clock
- **$FFE1**: STOP, check <STOP> key
- **$FFE4**: GETIN, get input from keyboard
- **$FFE7**: CLALL, close all files and channels
- **$FFEA**: UDTIM, increment realtime clock
- **$FFED**: SCREEN, return screen organisation
- **$FFF0**: PLOT, read/set cursor X/Y position
- **$FFF3**: IOBASE, return IOBASE address

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*