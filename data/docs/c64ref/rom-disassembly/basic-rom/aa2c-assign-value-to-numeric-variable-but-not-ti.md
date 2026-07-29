---
title: assign value to numeric variable, but not TI$
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
- aa2c-string
- aa52-and-descriptor-is-a-variable
- aa68-move-descriptor-into-variable
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AA2C
  address_end: $AA7F
  symbol: assign-value-to-numeric-variable-but-not-ti
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AA2C**: index to string pointer high byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AA2C**: Zeiger setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AA64**: low  0061'
---

# $AA2C — assign value to numeric variable, but not TI$

## Disassemblatura
```assembly
.AA2C  A0 02    LDY #$02   ; index to string pointer high byte
.AA2E  B1 64    LDA ($64),Y   ; get string pointer high byte
.AA30  C5 34    CMP $34   ; compare with bottom of string space high byte
.AA32  90 17    BCC $AA4B   ; branch if string pointer high byte is less than bottom of string space high byte
.AA34  D0 07    BNE $AA3D   ; branch if string pointer high byte is greater than bottom of string space high byte else high bytes were equal
.AA36  88       DEY   ; decrement index to string pointer low byte
.AA37  B1 64    LDA ($64),Y   ; get string pointer low byte
.AA39  C5 33    CMP $33   ; compare with bottom of string space low byte
.AA3B  90 0E    BCC $AA4B   ; branch if string pointer low byte is less than bottom of string space low byte
.AA3D  A4 65    LDY $65   ; get descriptor pointer high byte
.AA3F  C4 2E    CPY $2E   ; compare with start of variables high byte
.AA41  90 08    BCC $AA4B   ; branch if less, is on string stack
.AA43  D0 0D    BNE $AA52   ; if greater make space and copy string else high bytes were equal
.AA45  A5 64    LDA $64   ; get descriptor pointer low byte
.AA47  C5 2D    CMP $2D   ; compare with start of variables low byte
.AA49  B0 07    BCS $AA52   ; if greater or equal make space and copy string
.AA4B  A5 64    LDA $64   ; get descriptor pointer low byte
.AA4D  A4 65    LDY $65   ; get descriptor pointer high byte
.AA4F  4C 68 AA JMP $AA68   ; go copy descriptor to variable
.AA52  A0 00    LDY #$00   ; clear index
.AA54  B1 64    LDA ($64),Y   ; get string length
.AA56  20 75 B4 JSR $B475   ; copy descriptor pointer and make string space A bytes long
.AA59  A5 50    LDA $50   ; copy old descriptor pointer low byte
.AA5B  A4 51    LDY $51   ; copy old descriptor pointer high byte
.AA5D  85 6F    STA $6F   ; save old descriptor pointer low byte
.AA5F  84 70    STY $70   ; save old descriptor pointer high byte
.AA61  20 7A B6 JSR $B67A   ; copy string from descriptor to utility pointer
.AA64  A9 61    LDA #$61   ; get descriptor pointer low byte
.AA66  A0 00    LDY #$00   ; get descriptor pointer high byte
.AA68  85 50    STA $50   ; save descriptor pointer low byte
.AA6A  84 51    STY $51   ; save descriptor pointer high byte
.AA6C  20 DB B6 JSR $B6DB   ; clean descriptor stack, YA = pointer
.AA6F  A0 00    LDY #$00   ; clear index
.AA71  B1 50    LDA ($50),Y   ; get string length from new descriptor
.AA73  91 49    STA ($49),Y   ; copy string length to variable
.AA75  C8       INY   ; increment index
.AA76  B1 50    LDA ($50),Y   ; get string pointer low byte from new descriptor
.AA78  91 49    STA ($49),Y   ; copy string pointer low byte to variable
.AA7A  C8       INY   ; increment index
.AA7B  B1 50    LDA ($50),Y   ; get string pointer high byte from new descriptor
.AA7D  91 49    STA ($49),Y   ; copy string pointer high byte to variable
.AA7F  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$AA2C**: index to string pointer high byte
- **$AA2E**: get string pointer high byte
- **$AA30**: compare with bottom of string space high byte
- **$AA32**: branch if string pointer high byte is less than bottom of string space high byte
- **$AA34**: branch if string pointer high byte is greater than bottom of string space high byte else high bytes were equal
- **$AA36**: decrement index to string pointer low byte
- **$AA37**: get string pointer low byte
- **$AA39**: compare with bottom of string space low byte
- **$AA3B**: branch if string pointer low byte is less than bottom of string space low byte
- **$AA3D**: get descriptor pointer high byte
- **$AA3F**: compare with start of variables high byte
- **$AA41**: branch if less, is on string stack
- **$AA43**: if greater make space and copy string else high bytes were equal
- **$AA45**: get descriptor pointer low byte
- **$AA47**: compare with start of variables low byte
- **$AA49**: if greater or equal make space and copy string
- **$AA4B**: get descriptor pointer low byte
- **$AA4D**: get descriptor pointer high byte
- **$AA4F**: go copy descriptor to variable
- **$AA52**: clear index
- **$AA54**: get string length
- **$AA56**: copy descriptor pointer and make string space A bytes long
- **$AA59**: copy old descriptor pointer low byte
- **$AA5B**: copy old descriptor pointer high byte
- **$AA5D**: save old descriptor pointer low byte
- **$AA5F**: save old descriptor pointer high byte
- **$AA61**: copy string from descriptor to utility pointer
- **$AA64**: get descriptor pointer low byte
- **$AA66**: get descriptor pointer high byte
- **$AA68**: save descriptor pointer low byte
- **$AA6A**: save descriptor pointer high byte
- **$AA6C**: clean descriptor stack, YA = pointer
- **$AA6F**: clear index
- **$AA71**: get string length from new descriptor
- **$AA73**: copy string length to variable
- **$AA75**: increment index
- **$AA76**: get string pointer low byte from new descriptor
- **$AA78**: copy string pointer low byte to variable
- **$AA7A**: increment index
- **$AA7B**: get string pointer high byte from new descriptor
- **$AA7D**: copy string pointer high byte to variable

### Commodore-64-intern-Buch (Commodore)
- **$AA2C**: Zeiger setzen
- **$AA2E**: Stringadresse HIGH mit
- **$AA30**: Stringanfangsadr. vergleichen
- **$AA32**: kleiner: String im Programm
- **$AA34**: größer: $AA3D
- **$AA36**: Zeiger vermindern
- **$AA37**: Stringadresse (LOW) holen
- **$AA39**: und vergleichen
- **$AA3B**: kleiner: String im Programm
- **$AA3D**: Zeiger auf Stringdescriptor
- **$AA3F**: mit Variablenstart vergl.
- **$AA41**: kleiner: $AA4B
- **$AA43**: größer: $AA52
- **$AA45**: Stringdiscriptorzeiger (LOW)
- **$AA47**: mit Variablenstart vergl.
- **$AA49**: größer: $AA52
- **$AA4B**: Zeiger in Akku und Y-Reg.
- **$AA4D**: auf Stringdescriptor setzen
- **$AA4F**: bis $AA68 überspringen
- **$AA52**: Zeiger setzen
- **$AA54**: Länge des Strings holen
- **$AA56**: prüft Platz, setzt Stringz.
- **$AA59**: Zeiger auf Stringdescriptor
- **$AA5B**: holen (LOW- und HIGH-Byte)
- **$AA5D**: und
- **$AA5F**: speichern
- **$AA61**: String in Bereich übertragen
- **$AA64**: Werte laden
- **$AA66**: und damit
- **$AA68**: Stringdiscriptor
- **$AA6A**: neu setzen
- **$AA6C**: Descriptor löschen
- **$AA6F**: Zeiger setzen
- **$AA71**: Länge des Descriptors holen
- **$AA73**: und abspeichern
- **$AA75**: Zeiger erhöhen
- **$AA76**: Adresse (LOW) holen
- **$AA78**: und speichern
- **$AA7A**: Zeiger erhöhen
- **$AA7B**: und Adresse (HIGH)
- **$AA7D**: in Variable bringen
- **$AA7F**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$AA64**: low  0061
- **$AA66**: high 0061

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*