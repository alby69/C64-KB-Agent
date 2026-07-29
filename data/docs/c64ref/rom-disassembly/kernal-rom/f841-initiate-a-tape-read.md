---
title: initiate a tape read
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
- bcs
- f841-block-vom-band-lesen
- f84a-programm-vom-band-laden
- f8dc-clear-saved-irq-address
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F841
  address_end: $F862
  symbol: initiate-a-tape-read
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F841**: clear A'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F841**: Status'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F841 — initiate a tape read

## Disassemblatura
```assembly
.F841  A9 00    LDA #$00   ; clear A
.F843  85 90    STA $90   ; clear serial status byte
.F845  85 93    STA $93   ; clear the load/verify flag
.F847  20 D7 F7 JSR $F7D7   ; set the tape buffer start and end pointers
.F84A  20 17 F8 JSR $F817   ; wait for PLAY
.F84D  B0 1F    BCS $F86E   ; exit if STOP was pressed, uses a further BCS at the target address to reach final target at $F8DC
.F84F  78       SEI   ; disable interrupts
.F850  A9 00    LDA #$00   ; clear A
.F852  85 AA    STA $AA
.F854  85 B4    STA $B4
.F856  85 B0    STA $B0   ; clear tape timing constant min byte
.F858  85 9E    STA $9E   ; clear tape pass 1 error log/char buffer
.F85A  85 9F    STA $9F   ; clear tape pass 2 error log corrected
.F85C  85 9C    STA $9C   ; clear byte received flag
.F85E  A9 90    LDA #$90   ; enable CA1 interrupt ??
.F860  A2 0E    LDX #$0E   ; set index for tape read vector
.F862  D0 11    BNE $F875   ; go do tape read/write, branch always
```


## Commenti

### Original Disassembly (—)
- **$F841**: clear A
- **$F843**: clear serial status byte
- **$F845**: clear the load/verify flag
- **$F847**: set the tape buffer start and end pointers
- **$F84A**: wait for PLAY
- **$F84D**: exit if STOP was pressed, uses a further BCS at the target address to reach final target at $F8DC
- **$F84F**: disable interrupts
- **$F850**: clear A
- **$F856**: clear tape timing constant min byte
- **$F858**: clear tape pass 1 error log/char buffer
- **$F85A**: clear tape pass 2 error log corrected
- **$F85C**: clear byte received flag
- **$F85E**: enable CA1 interrupt ??
- **$F860**: set index for tape read vector
- **$F862**: go do tape read/write, branch always

### Commodore-64-intern-Buch (Commodore)
- **$F841**: Status
- **$F843**: und Verify-Flag
- **$F845**: löschen
- **$F847**: Bandpufferadresse holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*