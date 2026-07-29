---
title: write the tape header
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
- 0200-buf
- f76a-band-schreiben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F76A
  address_end: $F7CF
  symbol: write-the-tape-header
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F76A**: save header type'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F76A**: Header-Typ speichern'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F76A — write the tape header

## Disassemblatura
```assembly
.F76A  85 9E    STA $9E   ; save header type
.F76C  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F76F  90 5E    BCC $F7CF   ; if < $0200 just exit ??
.F771  A5 C2    LDA $C2   ; get I/O start address high byte
.F773  48       PHA   ; save it
.F774  A5 C1    LDA $C1   ; get I/O start address low byte
.F776  48       PHA   ; save it
.F777  A5 AF    LDA $AF   ; get tape end address high byte
.F779  48       PHA   ; save it
.F77A  A5 AE    LDA $AE   ; get tape end address low byte
.F77C  48       PHA   ; save it
.F77D  A0 BF    LDY #$BF   ; index to header end
.F77F  A9 20    LDA #$20   ; clear byte, [SPACE]
.F781  91 B2    STA ($B2),Y   ; clear header byte
.F783  88       DEY   ; decrement index
.F784  D0 FB    BNE $F781   ; loop if more to do
.F786  A5 9E    LDA $9E   ; get the header type back
.F788  91 B2    STA ($B2),Y   ; write it to header
.F78A  C8       INY   ; increment the index
.F78B  A5 C1    LDA $C1   ; get the I/O start address low byte
.F78D  91 B2    STA ($B2),Y   ; write it to header
.F78F  C8       INY   ; increment the index
.F790  A5 C2    LDA $C2   ; get the I/O start address high byte
.F792  91 B2    STA ($B2),Y   ; write it to header
.F794  C8       INY   ; increment the index
.F795  A5 AE    LDA $AE   ; get the tape end address low byte
.F797  91 B2    STA ($B2),Y   ; write it to header
.F799  C8       INY   ; increment the index
.F79A  A5 AF    LDA $AF   ; get the tape end address high byte
.F79C  91 B2    STA ($B2),Y   ; write it to header
.F79E  C8       INY   ; increment the index
.F79F  84 9F    STY $9F   ; save the index
.F7A1  A0 00    LDY #$00   ; clear Y
.F7A3  84 9E    STY $9E   ; clear the name index
.F7A5  A4 9E    LDY $9E   ; get name index
.F7A7  C4 B7    CPY $B7   ; compare with file name length
.F7A9  F0 0C    BEQ $F7B7   ; if all done exit the loop
.F7AB  B1 BB    LDA ($BB),Y   ; get file name byte
.F7AD  A4 9F    LDY $9F   ; get buffer index
.F7AF  91 B2    STA ($B2),Y   ; save file name byte to buffer
.F7B1  E6 9E    INC $9E   ; increment file name index
.F7B3  E6 9F    INC $9F   ; increment tape buffer index
.F7B5  D0 EE    BNE $F7A5   ; loop, branch always
.F7B7  20 D7 F7 JSR $F7D7   ; set tape buffer start and end pointers
.F7BA  A9 69    LDA #$69   ; set write lead cycle count
.F7BC  85 AB    STA $AB   ; save write lead cycle count
.F7BE  20 6B F8 JSR $F86B   ; do tape write, no cycle count set
.F7C1  A8       TAY
.F7C2  68       PLA   ; pull tape end address low byte
.F7C3  85 AE    STA $AE   ; restore it
.F7C5  68       PLA   ; pull tape end address high byte
.F7C6  85 AF    STA $AF   ; restore it
.F7C8  68       PLA   ; pull I/O start addresses low byte
.F7C9  85 C1    STA $C1   ; restore it
.F7CB  68       PLA   ; pull I/O start addresses high byte
.F7CC  85 C2    STA $C2   ; restore it
.F7CE  98       TYA
.F7CF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F76A**: save header type
- **$F76C**: get tape buffer start pointer in XY
- **$F76F**: if < $0200 just exit ??
- **$F771**: get I/O start address high byte
- **$F773**: save it
- **$F774**: get I/O start address low byte
- **$F776**: save it
- **$F777**: get tape end address high byte
- **$F779**: save it
- **$F77A**: get tape end address low byte
- **$F77C**: save it
- **$F77D**: index to header end
- **$F77F**: clear byte, [SPACE]
- **$F781**: clear header byte
- **$F783**: decrement index
- **$F784**: loop if more to do
- **$F786**: get the header type back
- **$F788**: write it to header
- **$F78A**: increment the index
- **$F78B**: get the I/O start address low byte
- **$F78D**: write it to header
- **$F78F**: increment the index
- **$F790**: get the I/O start address high byte
- **$F792**: write it to header
- **$F794**: increment the index
- **$F795**: get the tape end address low byte
- **$F797**: write it to header
- **$F799**: increment the index
- **$F79A**: get the tape end address high byte
- **$F79C**: write it to header
- **$F79E**: increment the index
- **$F79F**: save the index
- **$F7A1**: clear Y
- **$F7A3**: clear the name index
- **$F7A5**: get name index
- **$F7A7**: compare with file name length
- **$F7A9**: if all done exit the loop
- **$F7AB**: get file name byte
- **$F7AD**: get buffer index
- **$F7AF**: save file name byte to buffer
- **$F7B1**: increment file name index
- **$F7B3**: increment tape buffer index
- **$F7B5**: loop, branch always
- **$F7B7**: set tape buffer start and end pointers
- **$F7BA**: set write lead cycle count
- **$F7BC**: save write lead cycle count
- **$F7BE**: do tape write, no cycle count set
- **$F7C2**: pull tape end address low byte
- **$F7C3**: restore it
- **$F7C5**: pull tape end address high byte
- **$F7C6**: restore it
- **$F7C8**: pull I/O start addresses low byte
- **$F7C9**: restore it
- **$F7CB**: pull I/O start addresses high byte
- **$F7CC**: restore it

### Commodore-64-intern-Buch (Commodore)
- **$F76A**: Header-Typ speichern
- **$F76C**: Bandpufferadresse holen
- **$F76F**: verzweige falls Adresse ungültig
- **$F771**: Startadresse
- **$F773**: laden
- **$F774**: und in
- **$F776**: Stack schreiben
- **$F777**: Endadresse
- **$F779**: laden
- **$F77A**: und in
- **$F77C**: Stack schreiben
- **$F77D**: Pufferlänge für Schleife holen
- **$F77F**: Code für ' ' laden
- **$F781**: und speichern
- **$F783**: Zähler verringern
- **$F784**: verzweige falls Puffer noch nicht alles gelöscht
- **$F786**: gespeicherten Header-Typ holen
- **$F788**: und in Puffer schreiben
- **$F78A**: Zähler erhöhen
- **$F78B**: Startadresse LOW holen
- **$F78D**: und in Puffer schreiben
- **$F78F**: Zähler erhöhen
- **$F790**: Startadesse HIGH holen
- **$F792**: und in Puffer schreiben
- **$F794**: Zähler erhöhen
- **$F795**: Endadresse LOW holen
- **$F797**: und in Puffer schreiben
- **$F799**: Zähler erhöhen
- **$F79A**: Endadresse HIGH holen
- **$F79C**: und in Puffer schreiben
- **$F79E**: Zähler erhöhen
- **$F79F**: Zähler speichern
- **$F7A1**: Zähler für Filenamen auf Null setzen
- **$F7A3**: und speichern
- **$F7A5**: Zähler holen
- **$F7A7**: und mit Länge des Filenamens vergleichen
- **$F7A9**: verzweige falls alle Buchsta- ben geholt
- **$F7AB**: Filenamen holen
- **$F7AD**: Pufferzeiger laden
- **$F7AF**: und Zeichen in Puffer schrei- ben
- **$F7B1**: Zähler für Filenamen erhöhen
- **$F7B3**: Zeiger auf Bandpuffer erhöhen
- **$F7B5**: unbedingter Sprung
- **$F7B7**: Start- und Endadresse auf Bandpuffer holen
- **$F7BC**: Checksumme für Header bzw. Datenblock = $69
- **$F7BE**: Block auf Band schreiben
- **$F7C1**: Akku retten
- **$F7C2**: Endadresse
- **$F7C3**: vom Stack
- **$F7C5**: holen und
- **$F7C6**: in $AE/SAF speichern
- **$F7C8**: Startadresse
- **$F7C9**: vom Stack
- **$F7CB**: holen und
- **$F7CC**: in $C1/C2 speichern
- **$F7CE**: Akku wiederholen
- **$F7CF**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*