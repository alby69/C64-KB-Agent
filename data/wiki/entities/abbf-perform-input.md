---
id: abbf-perform-input
type: entity
title: perform INPUT
aliases:
- perform INPUT
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/abbf-perform-input.md
  sha256: 635034daac850527f9cdc89c3fcffabc97fe980361b89fed8c39a38c78b19261
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-abbf-perform-input
---

# perform INPUT



# $ABBF — perform INPUT

## Disassemblatura
```assembly
.ABBF  C9 22    CMP #$22   ; compare next byte with open quote
.ABC1  D0 0B    BNE $ABCE   ; if no prompt string just do INPUT
.ABC3  20 BD AE JSR $AEBD   ; print "..." string
.ABC6  A9 3B    LDA #$3B   ; load A with ";"
.ABC8  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.ABCB  20 21 AB JSR $AB21   ; print string from utility pointer done with prompt, now get data
.ABCE  20 A6 B3 JSR $B3A6   ; check not Direct, back here if ok
.ABD1  A9 2C    LDA #$2C   ; set ","
.ABD3  8D FF 01 STA $01FF   ; save to start of buffer - 1
.ABD6  20 F9 AB JSR $ABF9   ; print "? " and get BASIC input
.ABD9  A5 13    LDA $13   ; get current I/O channel
.ABDB  F0 0D    BEQ $ABEA   ; branch if default I/O channel
.ABDD  20 B7 FF JSR $FFB7   ; read I/O status word
.ABE0  29 02    AND #$02   ; mask no DSR/timeout
.ABE2  F0 06    BEQ $ABEA   ; branch if not error
.ABE4  20 B5 AB JSR $ABB5   ; close input and output channels
.ABE7  4C F8 A8 JMP $A8F8   ; perform DATA
.ABEA  AD 00 02 LDA $0200   ; get first byte in input buffer
.ABED  D0 1E    BNE $AC0D   ; branch if not null else ..
.ABEF  A5 13    LDA $13   ; get current I/O channel
.ABF1  D0 E3    BNE $ABD6   ; if not default channel go get BASIC input
.ABF3  20 06 A9 JSR $A906   ; scan for next BASIC statement ([:] or [EOL])
.ABF6  4C FB A8 JMP $A8FB   ; add Y to the BASIC execute pointer and return
```


## Commenti

### Original Disassembly (—)
- **$ABBF**: compare next byte with open quote
- **$ABC1**: if no prompt string just do INPUT
- **$ABC3**: print "..." string
- **$ABC6**: load A with ";"
- **$ABC8**: scan for CHR$(A), else do syntax error then warm start
- **$ABCB**: print string from utility pointer done with prompt, now get data
- **$ABCE**: check not Direct, back here if ok
- **$ABD1**: set ","
- **$ABD3**: save to start of buffer - 1
- **$ABD6**: print "? " and get BASIC input
- **$ABD9**: get current I/O channel
- **$ABDB**: branch if default I/O channel
- **$ABDD**: read I/O status word
- **$ABE0**: mask no DSR/timeout
- **$ABE2**: branch if not error
- **$ABE4**: close input and output channels
- **$ABE7**: perform DATA
- **$ABEA**: get first byte in input buffer
- **$ABED**: branch if not null else ..
- **$ABEF**: get current I/O channel
- **$ABF1**: if not default channel go get BASIC input
- **$ABF3**: scan for next BASIC statement ([:] or [EOL])
- **$ABF6**: add Y to the BASIC execute pointer and return

### Commodore-64-intern-Buch (Commodore)
- **$ABBF**: '"' Hochkomma?
- **$ABC1**: nein: $ABDE
- **$ABC3**: Dialogstring holen
- **$ABC6**: ';' Semikolon
- **$ABC8**: prüft auf Code
- **$ABCB**: String ausgeben
- **$ABCE**: prüft auf Direkt-Modus
- **$ABD1**: ',' Komma
- **$ABD3**: an Pufferstart
- **$ABD6**: Fragezeichen ausgeben
- **$ABD9**: Nummer des Eingabegeräts
- **$ABDB**: Tastatur? ja: $ABEA
- **$ABDD**: Status holen
- **$ABE0**: Bit 1 isolieren (Tineout R.)
- **$ABE2**: Time-out?
- **$ABE4**: ja: CLRCH,Tastatur aktivieren
- **$ABE7**: nächstes Statement ausführen
- **$ABEA**: erstes Zeichen holen
- **$ABED**: Ende?
- **$ABEF**: ja: Eingabegerät
- **$ABF1**: nicht Tastatur: $ABD6
- **$ABF3**: Offset (Statement) suchen
- **$ABF6**: Programmzeiger auf Statement
- **$ABF9**: Eingabegerät holen
- **$ABFB**: nicht Tastatur: $AC03
- **$ABFD**: '?' ausgeben
- **$AC00**: ' ' Leerzeichen ausgeben
- **$AC03**: Eingabezeile holen

### Marko Mäkelä (Marko Mäkelä)
- **$ABBF**: quote mark
- **$ABC6**: semi-colon
- **$ABD1**: comma
- **$ABE7**: do DATA

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$ABBF**: CHECK FOR OPTIONAL PROMPT STRING
- **$ABC1**: NO, PRINT "?" PROMPT
- **$ABC3**: MAKE A PRINTABLE STRING OUT OF IT
- **$ABC6**: MUST HAVE ; NOW
- **$ABCB**: PRINT THE STRING
- **$ABCE**: ILLEGAL IF IN DIRECT MODE
- **$ABD1**: PRIME THE BUFFER
- **$ABD6**: NO STRING, PRINT "?"

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-abbf-perform-input]]
