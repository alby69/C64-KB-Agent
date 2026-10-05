---
id: e87c-do-newline
type: entity
title: do newline
aliases:
- do newline
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e87c-do-newline.md
  sha256: b00bdbafae2e7cc0ca5c582c5b8a1d6593782b7a7ab2a02bd1b169d3acd0411f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e87c-do-newline
---

# do newline



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

## References
- Source: [[src-e87c-do-newline]]
