---
title: do newline
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
- e87c-go-to-next-line
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $E87C
  address_end: $E88E
  symbol: do-newline
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E87C**: shift >> input cursor row'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E87C**: LXSP, cursor X-Y position'
---

# $E87C — do newline

## Disassemblatura
```assembly
.E87C  46 C9    LSR $C9   ; shift >> input cursor row
.E87E  A6 D6    LDX $D6   ; get the cursor row
.E880  E8       INX   ; increment the row
.E881  E0 19    CPX #$19   ; compare it with last row + 1
.E883  D0 03    BNE $E888   ; if not last row + 1 skip the screen scroll
.E885  20 EA E8 JSR $E8EA   ; else scroll the screen
.E888  B5 D9    LDA $D9,X   ; get start of line X pointer high byte
.E88A  10 F4    BPL $E880   ; loop if not start of logical line
.E88C  86 D6    STX $D6   ; save the cursor row
.E88E  4C 6C E5 JMP $E56C   ; set the screen pointers for cursor row, column and return
```


## Commenti

### Original Disassembly (—)
- **$E87C**: shift >> input cursor row
- **$E87E**: get the cursor row
- **$E880**: increment the row
- **$E881**: compare it with last row + 1
- **$E883**: if not last row + 1 skip the screen scroll
- **$E885**: else scroll the screen
- **$E888**: get start of line X pointer high byte
- **$E88A**: loop if not start of logical line
- **$E88C**: save the cursor row
- **$E88E**: set the screen pointers for cursor row, column and return

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E87C**: LXSP, cursor X-Y position
- **$E87E**: TBLX, current line number
- **$E880**: next line
- **$E881**: 26th line
- **$E883**: nope, scroll is not needed
- **$E885**: scroll down
- **$E888**: test LTDB1, screen line link table if first of two
- **$E88A**: yes, jump down another line
- **$E88C**: store in TBLX
- **$E88E**: set screen pointers

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*