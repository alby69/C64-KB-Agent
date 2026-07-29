---
title: evaluate string
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
- b6a3-stringverwaltung-frestr
- b6db-descriptorstack-entfernen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B6A3
  address_end: $B6EB
  symbol: evaluate-string
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B6A3**: check if source is string, else do type mismatch pop
      string off ...'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B6A3**: prüft auf Stringvariable'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B6A3 — evaluate string

## Disassemblatura
```assembly
.B6A3  20 8F AD JSR $AD8F   ; check if source is string, else do type mismatch pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.B6A6  A5 64    LDA $64   ; get descriptor pointer low byte
.B6A8  A4 65    LDY $65   ; get descriptor pointer high byte pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.B6AA  85 22    STA $22   ; save string pointer low byte
.B6AC  84 23    STY $23   ; save string pointer high byte
.B6AE  20 DB B6 JSR $B6DB   ; clean descriptor stack, YA = pointer
.B6B1  08       PHP   ; save status flags
.B6B2  A0 00    LDY #$00   ; clear index
.B6B4  B1 22    LDA ($22),Y   ; get length from string descriptor
.B6B6  48       PHA   ; put on stack
.B6B7  C8       INY   ; increment index
.B6B8  B1 22    LDA ($22),Y   ; get string pointer low byte from descriptor
.B6BA  AA       TAX   ; copy to X
.B6BB  C8       INY   ; increment index
.B6BC  B1 22    LDA ($22),Y   ; get string pointer high byte from descriptor
.B6BE  A8       TAY   ; copy to Y
.B6BF  68       PLA   ; get string length back
.B6C0  28       PLP   ; restore status
.B6C1  D0 13    BNE $B6D6   ; branch if pointer <> last_sl,last_sh
.B6C3  C4 34    CPY $34   ; compare with bottom of string space high byte
.B6C5  D0 0F    BNE $B6D6   ; branch if <>
.B6C7  E4 33    CPX $33   ; else compare with bottom of string space low byte
.B6C9  D0 0B    BNE $B6D6   ; branch if <>
.B6CB  48       PHA   ; save string length
.B6CC  18       CLC   ; clear carry for add
.B6CD  65 33    ADC $33   ; add bottom of string space low byte
.B6CF  85 33    STA $33   ; set bottom of string space low byte
.B6D1  90 02    BCC $B6D5   ; skip increment if no overflow
.B6D3  E6 34    INC $34   ; increment bottom of string space high byte
.B6D5  68       PLA   ; restore string length
.B6D6  86 22    STX $22   ; save string pointer low byte
.B6D8  84 23    STY $23   ; save string pointer high byte
.B6DA  60       RTS   ; clean descriptor stack, YA = pointer checks if AY is on the descriptor stack, if so does a stack discard
.B6DB  C4 18    CPY $18   ; compare high byte with current descriptor stack item pointer high byte
.B6DD  D0 0C    BNE $B6EB   ; exit if <>
.B6DF  C5 17    CMP $17   ; compare low byte with current descriptor stack item pointer low byte
.B6E1  D0 08    BNE $B6EB   ; exit if <>
.B6E3  85 16    STA $16   ; set descriptor stack pointer
.B6E5  E9 03    SBC #$03   ; update last string pointer low byte
.B6E7  85 17    STA $17   ; save current descriptor stack item pointer low byte
.B6E9  A0 00    LDY #$00   ; clear high byte
.B6EB  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B6A3**: check if source is string, else do type mismatch pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$B6A6**: get descriptor pointer low byte
- **$B6A8**: get descriptor pointer high byte pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$B6AA**: save string pointer low byte
- **$B6AC**: save string pointer high byte
- **$B6AE**: clean descriptor stack, YA = pointer
- **$B6B1**: save status flags
- **$B6B2**: clear index
- **$B6B4**: get length from string descriptor
- **$B6B6**: put on stack
- **$B6B7**: increment index
- **$B6B8**: get string pointer low byte from descriptor
- **$B6BA**: copy to X
- **$B6BB**: increment index
- **$B6BC**: get string pointer high byte from descriptor
- **$B6BE**: copy to Y
- **$B6BF**: get string length back
- **$B6C0**: restore status
- **$B6C1**: branch if pointer <> last_sl,last_sh
- **$B6C3**: compare with bottom of string space high byte
- **$B6C5**: branch if <>
- **$B6C7**: else compare with bottom of string space low byte
- **$B6C9**: branch if <>
- **$B6CB**: save string length
- **$B6CC**: clear carry for add
- **$B6CD**: add bottom of string space low byte
- **$B6CF**: set bottom of string space low byte
- **$B6D1**: skip increment if no overflow
- **$B6D3**: increment bottom of string space high byte
- **$B6D5**: restore string length
- **$B6D6**: save string pointer low byte
- **$B6D8**: save string pointer high byte
- **$B6DA**: clean descriptor stack, YA = pointer checks if AY is on the descriptor stack, if so does a stack discard
- **$B6DB**: compare high byte with current descriptor stack item pointer high byte
- **$B6DD**: exit if <>
- **$B6DF**: compare low byte with current descriptor stack item pointer low byte
- **$B6E1**: exit if <>
- **$B6E3**: set descriptor stack pointer
- **$B6E5**: update last string pointer low byte
- **$B6E7**: save current descriptor stack item pointer low byte
- **$B6E9**: clear high byte

### Commodore-64-intern-Buch (Commodore)
- **$B6A3**: prüft auf Stringvariable
- **$B6A6**: Zeiger auf
- **$B6A8**: Stringdescriptor
- **$B6AA**: nach
- **$B6AC**: $22 und $23 bringen
- **$B6AE**: Descriptor vom Stringstack
- **$B6B1**: Statusregister retten
- **$B6B2**: Zähler auf Null
- **$B6B4**: Stringlänge holen
- **$B6B6**: und in Stack schieben
- **$B6B7**: Zähler erhöhen
- **$B6B8**: LOW-Byte der Anfangsadresse
- **$B6BA**: ins X-Reg schieben
- **$B6BB**: Zähler erhöhen
- **$B6BC**: HIGH-Byte der Anfangsadresse
- **$B6BE**: ins Y-Reg schieben
- **$B6BF**: Stringlänge wieder aus Stack
- **$B6C0**: Statusreg. wieder aus Stack
- **$B6C1**: Neustring=Altstring nein? RTS
- **$B6C3**: Stringadresse identisch mit
- **$B6C5**: Zeiger auf Stringende?
- **$B6C7**: nein, dann
- **$B6C9**: zu $B6D6
- **$B6CB**: String-Anfangszeiger
- **$B6CC**: auf Länge
- **$B6CD**: des
- **$B6CF**: Strings
- **$B6D1**: hinaufsetzen
- **$B6D3**: Stringlänge
- **$B6D5**: holen
- **$B6D6**: LOW-Byte der Startadresse
- **$B6D8**: HIGH-Byte der Startadresse
- **$B6DA**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*