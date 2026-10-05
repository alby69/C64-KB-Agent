---
id: src-a560-get-statement-into-buffer
type: source
title: 'Source Summary: get statement into buffer'
aliases:
- get statement into buffer
- a560-get-statement-into-buffer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a560-get-statement-into-buffer.md
  sha256: eab94972fa4715c1f40d3145c45f53d7ced4590e1787b779eff8d167d5214088
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get statement into buffer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a560-get-statement-into-buffer.md`
**SHA256**: `eab94972fa4715c1f40d3145c45f53d7ced4590e1787b779eff8d167d5214088`

## Summary



# $A560 — get statement into buffer

## Disassemblatura
```assembly
.A560  A2 00    LDX #$00
.A562  20 12 E1 JSR $E112
.A565  C9 0D    CMP #$0D
.A567  F0 0D    BEQ $A576
.A569  9D 00 02 STA $0200,X
.A56C  E8       INX
.A56D  E0 59    CPX #$59
.A56F  90 F1    BCC $A562
.A571  A2 17    LDX #$17   ; error number
.A573  4C 37 A4 JMP $A437
.A576  4C CA AA JMP $AACA   ; goto end of line
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A560**: Zeiger setzen
- **$A562**: ein Zeichen ho...
