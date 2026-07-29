---
title: copy string from descriptor to utility pointer
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
- b67a-string-in-reserv-bereich
- b688-move-string-with-length-a-pointer-in-xy
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B67A
  address_end: $B6A2
  symbol: copy-string-from-descriptor-to-utility-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B67A**: clear index'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B67A**: Zähler auf Null'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B67A — copy string from descriptor to utility pointer

## Disassemblatura
```assembly
.B67A  A0 00    LDY #$00   ; clear index
.B67C  B1 6F    LDA ($6F),Y   ; get string length
.B67E  48       PHA   ; save it
.B67F  C8       INY   ; increment index
.B680  B1 6F    LDA ($6F),Y   ; get string pointer low byte
.B682  AA       TAX   ; copy to X
.B683  C8       INY   ; increment index
.B684  B1 6F    LDA ($6F),Y   ; get string pointer high byte
.B686  A8       TAY   ; copy to Y
.B687  68       PLA   ; get length back
.B688  86 22    STX $22   ; save string pointer low byte
.B68A  84 23    STY $23   ; save string pointer high byte store string from pointer to utility pointer
.B68C  A8       TAY   ; copy length as index
.B68D  F0 0A    BEQ $B699   ; branch if null string
.B68F  48       PHA   ; save length
.B690  88       DEY   ; decrement length/index
.B691  B1 22    LDA ($22),Y   ; get byte from string
.B693  91 35    STA ($35),Y   ; save byte to destination
.B695  98       TYA   ; copy length/index
.B696  D0 F8    BNE $B690   ; loop if not all done yet
.B698  68       PLA   ; restore length
.B699  18       CLC   ; clear carry for add
.B69A  65 35    ADC $35   ; add string utility ptr low byte
.B69C  85 35    STA $35   ; save string utility ptr low byte
.B69E  90 02    BCC $B6A2   ; branch if no rollover
.B6A0  E6 36    INC $36   ; increment string utility ptr high byte
.B6A2  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B67A**: clear index
- **$B67C**: get string length
- **$B67E**: save it
- **$B67F**: increment index
- **$B680**: get string pointer low byte
- **$B682**: copy to X
- **$B683**: increment index
- **$B684**: get string pointer high byte
- **$B686**: copy to Y
- **$B687**: get length back
- **$B688**: save string pointer low byte
- **$B68A**: save string pointer high byte store string from pointer to utility pointer
- **$B68C**: copy length as index
- **$B68D**: branch if null string
- **$B68F**: save length
- **$B690**: decrement length/index
- **$B691**: get byte from string
- **$B693**: save byte to destination
- **$B695**: copy length/index
- **$B696**: loop if not all done yet
- **$B698**: restore length
- **$B699**: clear carry for add
- **$B69A**: add string utility ptr low byte
- **$B69C**: save string utility ptr low byte
- **$B69E**: branch if no rollover
- **$B6A0**: increment string utility ptr high byte

### Commodore-64-intern-Buch (Commodore)
- **$B67A**: Zähler auf Null
- **$B67C**: Stringlänge holen
- **$B67E**: und merken
- **$B67F**: Zähler erhöhen
- **$B680**: LOW-Byte der Stringadresse
- **$B682**: ins X-Reg
- **$B683**: Zähler erhöhen
- **$B684**: HIGH-Byte der Stringadresse
- **$B686**: ins Y-Reg und
- **$B687**: Stack
- **$B688**: Zeiger auf
- **$B68A**: String speichern
- **$B68C**: Länge null ?
- **$B68D**: dann fertig
- **$B68F**: wieder in Stack
- **$B690**: Zähler erniedrigen
- **$B691**: String
- **$B693**: in den
- **$B695**: Stringbereich
- **$B696**: übertragen
- **$B698**: Den
- **$B699**: Zeiger
- **$B69A**: um
- **$B69C**: die
- **$B69E**: Stringlänge
- **$B6A0**: erhöhen
- **$B6A2**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*