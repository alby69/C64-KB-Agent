---
id: src-b02e-string-comparison
type: source
title: 'Source Summary: STRING COMPARISON'
aliases:
- STRING COMPARISON
- b02e-string-comparison.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b02e-string-comparison.md
  sha256: 0fa1cc4a87672b7fba882dc4a3ad73efeb8b3d34dd0a8528e6c3111ab3fb7750
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STRING COMPARISON

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b02e-string-comparison.md`
**SHA256**: `0fa1cc4a87672b7fba882dc4a3ad73efeb8b3d34dd0a8528e6c3111ab3fb7750`

## Summary



# $B02E — STRING COMPARISON

## Disassemblatura
```assembly
.B02E  A9 00    LDA #$00   ; SET RESULT TYPE TO NUMERIC
.B030  85 0D    STA $0D
.B032  C6 4D    DEC $4D   ; MAKE CPRTYP 0000<=>0
.B034  20 A6 B6 JSR $B6A6
.B037  85 61    STA $61   ; STRING LENGTH
.B039  86 62    STX $62
.B03B  84 63    STY $63
.B03D  A5 6C    LDA $6C
.B03F  A4 6D    LDY $6D
.B041  20 AA B6 JSR $B6AA
.B044  86 6C    STX $6C
.B046  84 6D    STY $6D
.B048  AA       TAX   ; LEN (ARG) STRING
.B049  38       SEC
.B04A  E5 ...
