---
title: write character and wait for key
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
- e5ca-tastatureingabe
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E5CA
  address_end: $E5CA
  symbol: write-character-and-wait-for-key
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E5CA**: output character'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E5CA**: Zeichen auf Bildschirm ausgeben'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E5CA**: output to screen'
---

# $E5CA — write character and wait for key

## Disassemblatura
```assembly
.E5CA  20 16 E7 JSR $E716   ; output character
```


## Commenti

### Original Disassembly (—)
- **$E5CA**: output character

### Commodore-64-intern-Buch (Commodore)
- **$E5CA**: Zeichen auf Bildschirm ausgeben
- **$E5CD**: Anzahl der
- **$E5CF**: gedrückten
- **$E5D1**: Tasten
- **$E5D4**: keine Taste gedrückt ?, dann warten
- **$E5D6**: Interrupt verhindern
- **$E5D7**: Cursor in Blink-Phase ?
- **$E5D9**: nein
- **$E5DB**: Zeichen unter dem Cursor
- **$E5DD**: Farbe unter dem Cursor
- **$E5E0**: Cursor nicht
- **$E5E2**: in Blinkphase
- **$E5E4**: Zeichen und Farbe setzen
- **$E5E7**: Zeichen aus Tastaturpuffer holen
- **$E5EA**: Kode für
- **$E5EC**: 'SHIFT RUN' ?
- **$E5EE**: 9 Zeichen
- **$E5F0**: Interrupt verhindern
- **$E5F1**: Zeichenzahl merken
- **$E5F3**: 'LOAD (cr) RUN (cr)'
- **$E5F6**: in Tastaturpuffer holen
- **$E5F9**: nächstes Zeichen
- **$E5FA**: schon alle ?
- **$E5FC**: und auswerten
- **$E5FE**: 'CR'
- **$E600**: nein ?, dann zurück zur Warteschleife
- **$E602**: Länge der Bildschirmzeile
- **$E604**: CR-Flag setzen
- **$E606**: Zeichen vom Bildschirm holen
- **$E608**: Leerzeichen
- **$E60A**: am Ende
- **$E60C**: der
- **$E60D**: Zeile
- **$E60F**: eliminieren
- **$E610**: Position als Index merken
- **$E612**: Cursorspalte
- **$E614**: gleich Null
- **$E617**: Cursorposition auf Null
- **$E619**: Hochkommaflag löschen
- **$E61B**: wenn Cursorzeile schon durch
- **$E61D**: scrollen verschwunden, dann zu $E63A
- **$E61F**: Cursorzeile
- **$E621**: Adresse für Startzeile setzen
- **$E624**: Fehler bei Eingabe ?,
- **$E626**: dann nochmal lesen
- **$E628**: letzte Spalte
- **$E62A**: in Spaltenzeiger bringen
- **$E62C**: mit Index vergleichen
- **$E62E**: wenn kleiner, dann Zeile auswerten
- **$E630**: wenn größer oder gleich, dann keine Eingabe

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E5CA**: output to screen
- **$E5CD**: read NDX, number of characters in keyboard queue
- **$E5CF**: BLNSW, cursor blink enable
- **$E5D1**: AUTODN, auto scroll down flag
- **$E5D4**: loop till key is pressed
- **$E5D6**: disable interrupt
- **$E5D7**: BLNON, last cursor blink (on/off)
- **$E5DB**: GDBLN, character under cursor
- **$E5DD**: GDCOL, background color under cursor
- **$E5E2**: clear BLNON
- **$E5E4**: print to screen
- **$E5E7**: Get character from keyboard buffer
- **$E5EA**: test if <shift/RUN> is pressed
- **$E5EC**: nope
- **$E5EE**: transfer 'LOAD <CR> RUN <CR>' to keyboard buffer
- **$E5F1**: store #9 in NDX, characters in buffer
- **$E5F3**: 'LOAD <CR> RUN <CR>' message in ROM
- **$E5F6**: store in keyboard buffer
- **$E5FA**: all nine characters
- **$E5FC**: always jump
- **$E5FE**: carriage return pressed?
- **$E600**: nope, go to start
- **$E602**: get LNMX, screen line length
- **$E604**: CRSV, flag input/get from keyboard
- **$E606**: PNT, screen address
- **$E608**: space?
- **$E60A**: nope
- **$E60D**: next
- **$E610**: store in INDX, end of logical line for input
- **$E614**: AUTODN
- **$E617**: PNTR, cursor column
- **$E619**: QTSW, reset quotes mode
- **$E61B**: LXSP, cursor X/Y position
- **$E61F**: TBLX, cursor line number
- **$E621**: retreat cursor
- **$E624**: LXSP
- **$E62A**: PNTR
- **$E62C**: INDX

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*