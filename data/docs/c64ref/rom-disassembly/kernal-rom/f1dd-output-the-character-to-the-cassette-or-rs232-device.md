---
title: output the character to the cassette or RS232 device
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f1dd-output-the-character-to-the-cassette-or-rs232-device
- f1e5-ausgabe-auf-band
- f208-rs-232-ausgabe
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $F1DD
  address_end: $F20B
  symbol: output-the-character-to-the-cassette-or-rs232-device
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F1DD**: save the character to the character buffer'
---

# $F1DD — output the character to the cassette or RS232 device

## Disassemblatura
```assembly
.F1DD  85 9E    STA $9E   ; save the character to the character buffer
.F1DF  8A       TXA   ; copy X
.F1E0  48       PHA   ; save X
.F1E1  98       TYA   ; copy Y
.F1E2  48       PHA   ; save Y
.F1E3  90 23    BCC $F208   ; if Cb is clear it must be the RS232 device output the character to the cassette
.F1E5  20 0D F8 JSR $F80D   ; bump the tape pointer
.F1E8  D0 0E    BNE $F1F8   ; if not end save next byte and exit
.F1EA  20 64 F8 JSR $F864   ; initiate tape write
.F1ED  B0 0E    BCS $F1FD   ; exit if error
.F1EF  A9 02    LDA #$02   ; set data block type ??
.F1F1  A0 00    LDY #$00   ; clear index
.F1F3  91 B2    STA ($B2),Y   ; save type to buffer ??
.F1F5  C8       INY   ; increment index
.F1F6  84 A6    STY $A6   ; save tape buffer index
.F1F8  A5 9E    LDA $9E   ; restore character from character buffer
.F1FA  91 B2    STA ($B2),Y   ; save to buffer
.F1FC  18       CLC   ; flag no error
.F1FD  68       PLA   ; pull Y
.F1FE  A8       TAY   ; restore Y
.F1FF  68       PLA   ; pull X
.F200  AA       TAX   ; restore X
.F201  A5 9E    LDA $9E   ; get the character from the character buffer
.F203  90 02    BCC $F207   ; exit if no error
.F205  A9 00    LDA #$00   ; else clear A
.F207  60       RTS   ; output the character to the RS232 device
.F208  20 17 F0 JSR $F017   ; send byte to the RS232 buffer, no setup
.F20B  4C FC F1 JMP $F1FC   ; do no error exit
```


## Commenti

### Original Disassembly (—)
- **$F1DD**: save the character to the character buffer
- **$F1DF**: copy X
- **$F1E0**: save X
- **$F1E1**: copy Y
- **$F1E2**: save Y
- **$F1E3**: if Cb is clear it must be the RS232 device output the character to the cassette
- **$F1E5**: bump the tape pointer
- **$F1E8**: if not end save next byte and exit
- **$F1EA**: initiate tape write
- **$F1ED**: exit if error
- **$F1EF**: set data block type ??
- **$F1F1**: clear index
- **$F1F3**: save type to buffer ??
- **$F1F5**: increment index
- **$F1F6**: save tape buffer index
- **$F1F8**: restore character from character buffer
- **$F1FA**: save to buffer
- **$F1FC**: flag no error
- **$F1FD**: pull Y
- **$F1FE**: restore Y
- **$F1FF**: pull X
- **$F200**: restore X
- **$F201**: get the character from the character buffer
- **$F203**: exit if no error
- **$F205**: else clear A
- **$F207**: output the character to the RS232 device
- **$F208**: send byte to the RS232 buffer, no setup
- **$F20B**: do no error exit

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*