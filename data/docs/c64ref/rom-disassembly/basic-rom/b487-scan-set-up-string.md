---
title: scan, set up string
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
- b487-string-holen-zeiger-in-ay
- b4ca-descriptorstapel-bringen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B487
  address_end: $B4F3
  symbol: scan-set-up-string
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B487**: set terminator to "'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B487**: ''"''-Code'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B487**: quote mark'
---

# $B487 — scan, set up string

## Disassemblatura
```assembly
.B487  A2 22    LDX #$22   ; set terminator to "
.B489  86 07    STX $07   ; set search character, terminator 1
.B48B  86 08    STX $08   ; set terminator 2 print search or alternate terminated string to utility pointer source is AY
.B48D  85 6F    STA $6F   ; store string start low byte
.B48F  84 70    STY $70   ; store string start high byte
.B491  85 62    STA $62   ; save string pointer low byte
.B493  84 63    STY $63   ; save string pointer high byte
.B495  A0 FF    LDY #$FF   ; set length to -1
.B497  C8       INY   ; increment length
.B498  B1 6F    LDA ($6F),Y   ; get byte from string
.B49A  F0 0C    BEQ $B4A8   ; exit loop if null byte [EOS]
.B49C  C5 07    CMP $07   ; compare with search character, terminator 1
.B49E  F0 04    BEQ $B4A4   ; branch if terminator
.B4A0  C5 08    CMP $08   ; compare with terminator 2
.B4A2  D0 F3    BNE $B497   ; loop if not terminator 2
.B4A4  C9 22    CMP #$22   ; compare with "
.B4A6  F0 01    BEQ $B4A9   ; branch if " (carry set if = !)
.B4A8  18       CLC   ; clear carry for add (only if [EOL] terminated string)
.B4A9  84 61    STY $61   ; save length in FAC1 exponent
.B4AB  98       TYA   ; copy length to A
.B4AC  65 6F    ADC $6F   ; add string start low byte
.B4AE  85 71    STA $71   ; save string end low byte
.B4B0  A6 70    LDX $70   ; get string start high byte
.B4B2  90 01    BCC $B4B5   ; branch if no low byte overflow
.B4B4  E8       INX   ; else increment high byte
.B4B5  86 72    STX $72   ; save string end high byte
.B4B7  A5 70    LDA $70   ; get string start high byte
.B4B9  F0 04    BEQ $B4BF   ; branch if in utility area
.B4BB  C9 02    CMP #$02   ; compare with input buffer memory high byte
.B4BD  D0 0B    BNE $B4CA   ; branch if not in input buffer memory string in input buffer or utility area, move to string memory
.B4BF  98       TYA   ; copy length to A
.B4C0  20 75 B4 JSR $B475   ; copy descriptor pointer and make string space A bytes long
.B4C3  A6 6F    LDX $6F   ; get string start low byte
.B4C5  A4 70    LDY $70   ; get string start high byte
.B4C7  20 88 B6 JSR $B688   ; store string A bytes long from XY to utility pointer check for space on descriptor stack then ... put string address and length on descriptor stack and update stack pointers
.B4CA  A6 16    LDX $16   ; get the descriptor stack pointer
.B4CC  E0 22    CPX #$22   ; compare it with the maximum + 1
.B4CE  D0 05    BNE $B4D5   ; if there is space on the string stack continue else do string too complex error
.B4D0  A2 19    LDX #$19   ; error $19, string too complex error
.B4D2  4C 37 A4 JMP $A437   ; do error #X then warm start put string address and length on descriptor stack and update stack pointers
.B4D5  A5 61    LDA $61   ; get the string length
.B4D7  95 00    STA $00,X   ; put it on the string stack
.B4D9  A5 62    LDA $62   ; get the string pointer low byte
.B4DB  95 01    STA $01,X   ; put it on the string stack
.B4DD  A5 63    LDA $63   ; get the string pointer high byte
.B4DF  95 02    STA $02,X   ; put it on the string stack
.B4E1  A0 00    LDY #$00   ; clear Y
.B4E3  86 64    STX $64   ; save the string descriptor pointer low byte
.B4E5  84 65    STY $65   ; save the string descriptor pointer high byte, always $00
.B4E7  84 70    STY $70   ; clear FAC1 rounding byte
.B4E9  88       DEY   ; Y = $FF
.B4EA  84 0D    STY $0D   ; save the data type flag, $FF = string
.B4EC  86 17    STX $17   ; save the current descriptor stack item pointer low byte
.B4EE  E8       INX   ; update the stack pointer
.B4EF  E8       INX   ; update the stack pointer
.B4F0  E8       INX   ; update the stack pointer
.B4F1  86 16    STX $16   ; save the new descriptor stack pointer
.B4F3  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B487**: set terminator to "
- **$B489**: set search character, terminator 1
- **$B48B**: set terminator 2 print search or alternate terminated string to utility pointer source is AY
- **$B48D**: store string start low byte
- **$B48F**: store string start high byte
- **$B491**: save string pointer low byte
- **$B493**: save string pointer high byte
- **$B495**: set length to -1
- **$B497**: increment length
- **$B498**: get byte from string
- **$B49A**: exit loop if null byte [EOS]
- **$B49C**: compare with search character, terminator 1
- **$B49E**: branch if terminator
- **$B4A0**: compare with terminator 2
- **$B4A2**: loop if not terminator 2
- **$B4A4**: compare with "
- **$B4A6**: branch if " (carry set if = !)
- **$B4A8**: clear carry for add (only if [EOL] terminated string)
- **$B4A9**: save length in FAC1 exponent
- **$B4AB**: copy length to A
- **$B4AC**: add string start low byte
- **$B4AE**: save string end low byte
- **$B4B0**: get string start high byte
- **$B4B2**: branch if no low byte overflow
- **$B4B4**: else increment high byte
- **$B4B5**: save string end high byte
- **$B4B7**: get string start high byte
- **$B4B9**: branch if in utility area
- **$B4BB**: compare with input buffer memory high byte
- **$B4BD**: branch if not in input buffer memory string in input buffer or utility area, move to string memory
- **$B4BF**: copy length to A
- **$B4C0**: copy descriptor pointer and make string space A bytes long
- **$B4C3**: get string start low byte
- **$B4C5**: get string start high byte
- **$B4C7**: store string A bytes long from XY to utility pointer check for space on descriptor stack then ... put string address and length on descriptor stack and update stack pointers
- **$B4CA**: get the descriptor stack pointer
- **$B4CC**: compare it with the maximum + 1
- **$B4CE**: if there is space on the string stack continue else do string too complex error
- **$B4D0**: error $19, string too complex error
- **$B4D2**: do error #X then warm start put string address and length on descriptor stack and update stack pointers
- **$B4D5**: get the string length
- **$B4D7**: put it on the string stack
- **$B4D9**: get the string pointer low byte
- **$B4DB**: put it on the string stack
- **$B4DD**: get the string pointer high byte
- **$B4DF**: put it on the string stack
- **$B4E1**: clear Y
- **$B4E3**: save the string descriptor pointer low byte
- **$B4E5**: save the string descriptor pointer high byte, always $00
- **$B4E7**: clear FAC1 rounding byte
- **$B4E9**: Y = $FF
- **$B4EA**: save the data type flag, $FF = string
- **$B4EC**: save the current descriptor stack item pointer low byte
- **$B4EE**: update the stack pointer
- **$B4EF**: update the stack pointer
- **$B4F0**: update the stack pointer
- **$B4F1**: save the new descriptor stack pointer

### Commodore-64-intern-Buch (Commodore)
- **$B487**: '"'-Code
- **$B489**: nach Suchzeichen
- **$B48B**: und Hochkommaflag
- **$B48D**: Startadresse des Strings
- **$B48F**: nach $6F/70
- **$B491**: und $62/63
- **$B493**: speichern
- **$B495**: Zeiger setzen
- **$B497**: Zeiger erhöhen
- **$B498**: nächstes Zeichen des Strings
- **$B49A**: Endekennzeichen?
- **$B49C**: Suchzeichen?
- **$B49E**: ja: $B4A4
- **$B4A0**: = Zeichen in Hochkommaflag
- **$B4A2**: nein: $B497
- **$B4A4**: '"'-Code?
- **$B4A6**: ja: $B4A9
- **$B4A8**: Carry löschen (Addition)
- **$B4A9**: Länge des Str. speichern und
- **$B4AB**: in Akku holen
- **$B4AC**: und zur Startadresse addieren
- **$B4AE**: ergibt Endadresse LOW + 1
- **$B4B0**: Übertrag
- **$B4B2**: Addition umgehen
- **$B4B4**: Übertrag addieren
- **$B4B5**: Endadresse HIGH + 1
- **$B4B7**: Startadresse HIGH
- **$B4B9**: null?
- **$B4BB**: zwei?
- **$B4BD**: nein: $B4CA
- **$B4BF**: Länge in Akku
- **$B4C0**: Stringzeiger berechnen
- **$B4C3**: LOW- und HIGH-Byte der
- **$B4C5**: Startadresse holen
- **$B4C7**: String in Bereich kopieren

### Marko Mäkelä (Marko Mäkelä)
- **$B487**: quote mark
- **$B4A4**: quote mark

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*