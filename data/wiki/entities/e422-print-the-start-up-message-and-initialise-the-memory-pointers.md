---
id: e422-print-the-start-up-message-and-initialise-the-memory-pointers
type: entity
title: print the start up message and initialise the memory pointers
aliases:
- print the start up message and initialise the memory pointers
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e422-print-the-start-up-message-and-initialise-the-memory-pointers.md
  sha256: 0c8bf7cf77677c20fed585a6ab5f75d4be2a191832b44b22be878d8133565f74
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e422-print-the-start-up-message-and-initialise-the-memory-pointers
---

# print the start up message and initialise the memory pointers



# $E422 — print the start up message and initialise the memory pointers

## Disassemblatura
```assembly
.E422  A5 2B    LDA $2B   ; get the start of memory low byte
.E424  A4 2C    LDY $2C   ; get the start of memory high byte
.E426  20 08 A4 JSR $A408   ; check available memory, do out of memory error if no room
.E429  A9 73    LDA #$73   ; set "**** COMMODORE 64 BASIC V2 ****" pointer low byte
.E42B  A0 E4    LDY #$E4   ; set "**** COMMODORE 64 BASIC V2 ****" pointer high byte
.E42D  20 1E AB JSR $AB1E   ; print a null terminated string
.E430  A5 37    LDA $37   ; get the end of memory low byte
.E432  38       SEC   ; set carry for subtract
.E433  E5 2B    SBC $2B   ; subtract the start of memory low byte
.E435  AA       TAX   ; copy the result to X
.E436  A5 38    LDA $38   ; get the end of memory high byte
.E438  E5 2C    SBC $2C   ; subtract the start of memory high byte
.E43A  20 CD BD JSR $BDCD   ; print XA as unsigned integer
.E43D  A9 60    LDA #$60   ; set " BYTES FREE" pointer low byte
.E43F  A0 E4    LDY #$E4   ; set " BYTES FREE" pointer high byte
.E441  20 1E AB JSR $AB1E   ; print a null terminated string
.E444  4C 44 A6 JMP $A644   ; do NEW, CLEAR, RESTORE and return
```


## Commenti

### Original Disassembly (—)
- **$E422**: get the start of memory low byte
- **$E424**: get the start of memory high byte
- **$E426**: check available memory, do out of memory error if no room
- **$E429**: set "**** COMMODORE 64 BASIC V2 ****" pointer low byte
- **$E42B**: set "**** COMMODORE 64 BASIC V2 ****" pointer high byte
- **$E42D**: print a null terminated string
- **$E430**: get the end of memory low byte
- **$E432**: set carry for subtract
- **$E433**: subtract the start of memory low byte
- **$E435**: copy the result to X
- **$E436**: get the end of memory high byte
- **$E438**: subtract the start of memory high byte
- **$E43A**: print XA as unsigned integer
- **$E43D**: set " BYTES FREE" pointer low byte
- **$E43F**: set " BYTES FREE" pointer high byte
- **$E441**: print a null terminated string
- **$E444**: do NEW, CLEAR, RESTORE and return

### Marko Mäkelä (Marko Mäkelä)
- **$E429**: low  E473
- **$E42B**: high E473
- **$E43D**: low  E460
- **$E43F**: high E460

### Magnus Nyman (Magnus Nyman)
- **$E422**: read TXTTAB, start of BASIC
- **$E426**: check for memory overlap
- **$E429**: $e473, startup message
- **$E42D**: output (A/Y)
- **$E430**: MEMSIZ, highest address in BASIC
- **$E432**: prepare for subtract
- **$E433**: subtract TXTTAB
- **$E435**: move to (X)
- **$E436**: and highbyte
- **$E43A**: output number in (A/X)
- **$E43D**: $e460
- **$E43F**: pointer to 'BASIC BYTES FREE'
- **$E441**: output (A/Y)
- **$E444**: perform NEW

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e422-print-the-start-up-message-and-initialise-the-memory-pointers]]
