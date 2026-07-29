---
title: 'do error #X then warm start, the error message vector is initialised to point
  here'
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a43a-fehlermeldung-ausgeben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A43A
  address_end: $A467
  symbol: do-error-x-then-warm-start-the-error-message-vector-is-initialised-to-point-here
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A43A**: copy error number'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A43A**: Fehlernummer im X-Register'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A465**: low  A369'
---

# $A43A — do error #X then warm start, the error message vector is initialised to point here

## Disassemblatura
```assembly
.A43A  8A       TXA   ; copy error number
.A43B  0A       ASL   ; *2
.A43C  AA       TAX   ; copy to index
.A43D  BD 26 A3 LDA $A326,X   ; get error message pointer low byte
.A440  85 22    STA $22   ; save it
.A442  BD 27 A3 LDA $A327,X   ; get error message pointer high byte
.A445  85 23    STA $23   ; save it
.A447  20 CC FF JSR $FFCC   ; close input and output channels
.A44A  A9 00    LDA #$00   ; clear A
.A44C  85 13    STA $13   ; clear current I/O channel, flag default
.A44E  20 D7 AA JSR $AAD7   ; print CR/LF
.A451  20 45 AB JSR $AB45   ; print "?"
.A454  A0 00    LDY #$00   ; clear index
.A456  B1 22    LDA ($22),Y   ; get byte from message
.A458  48       PHA   ; save status
.A459  29 7F    AND #$7F   ; mask 0xxx xxxx, clear b7
.A45B  20 47 AB JSR $AB47   ; output character
.A45E  C8       INY   ; increment index
.A45F  68       PLA   ; restore status
.A460  10 F4    BPL $A456   ; loop if character was not end marker
.A462  20 7A A6 JSR $A67A   ; flush BASIC stack and clear continue pointer
.A465  A9 69    LDA #$69   ; set " ERROR" pointer low byte
.A467  A0 A3    LDY #$A3   ; set " ERROR" pointer high byte
```


## Commenti

### Original Disassembly (—)
- **$A43A**: copy error number
- **$A43B**: *2
- **$A43C**: copy to index
- **$A43D**: get error message pointer low byte
- **$A440**: save it
- **$A442**: get error message pointer high byte
- **$A445**: save it
- **$A447**: close input and output channels
- **$A44A**: clear A
- **$A44C**: clear current I/O channel, flag default
- **$A44E**: print CR/LF
- **$A451**: print "?"
- **$A454**: clear index
- **$A456**: get byte from message
- **$A458**: save status
- **$A459**: mask 0xxx xxxx, clear b7
- **$A45B**: output character
- **$A45E**: increment index
- **$A45F**: restore status
- **$A460**: loop if character was not end marker
- **$A462**: flush BASIC stack and clear continue pointer
- **$A465**: set " ERROR" pointer low byte
- **$A467**: set " ERROR" pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$A43A**: Fehlernummer im X-Register
- **$A43B**: Akku * 2
- **$A43C**: Akku als Zeiger nach X
- **$A43D**: und Adresse der
- **$A440**: Fehlernummer aus Tabelle
- **$A442**: holen und
- **$A445**: abspeichern
- **$A447**: I/O Kanäle zurücksetzen
- **$A44A**: und Eingabekanal auf
- **$A44C**: Tastatur setzen
- **$A44E**: (CR) und (LF) ausgeben
- **$A451**: '?' ausgeben
- **$A454**: Zeiger setzen
- **$A456**: Fehlermeldungstext holen
- **$A458**: Akku retten
- **$A459**: Bit 7 löschen und
- **$A45B**: Fehlermeldung ausgeben
- **$A45E**: Zähler vermindern
- **$A45F**: Akku zurückholen
- **$A460**: Fertig? Nein, dann weiter
- **$A462**: BASIC-Zeiger initialisieren
- **$A465**: Zeiger A/Y auf Error-
- **$A467**: meldung stellen
- **$A469**: String ausgeben
- **$A46C**: Auf Programmodus
- **$A46E**: (prog/direkt) prüfen
- **$A46F**: Direkt: dann ausgeben
- **$A471**: 'in Zeilennummer' ausgeben
- **$A474**: Zeiger auf Ready-Modus
- **$A476**: setzen und
- **$A478**: String ausgeben
- **$A47B**: Wert für Direktmodus laden
- **$A47D**: und Flag setzen

### Marko Mäkelä (Marko Mäkelä)
- **$A465**: low  A369
- **$A467**: high A369
- **$A474**: low A376
- **$A476**: low A376
- **$A480**: normally A483

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*