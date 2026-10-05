---
id: src-af84-read-real-time-clock-into-fac1-mantissa-0hml
type: source
title: 'Source Summary: read real time clock into FAC1 mantissa, 0HML'
aliases:
- read real time clock into FAC1 mantissa, 0HML
- af84-read-real-time-clock-into-fac1-mantissa-0hml.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af84-read-real-time-clock-into-fac1-mantissa-0hml.md
  sha256: b901367b27e026356e7465ab57cdd0172abb99a8987412de9811ac41e40e291f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: read real time clock into FAC1 mantissa, 0HML

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/af84-read-real-time-clock-into-fac1-mantissa-0hml.md`
**SHA256**: `b901367b27e026356e7465ab57cdd0172abb99a8987412de9811ac41e40e291f`

## Summary



# $AF84 — read real time clock into FAC1 mantissa, 0HML

## Disassemblatura
```assembly
.AF84  20 DE FF JSR $FFDE   ; read real time clock
.AF87  86 64    STX $64   ; save jiffy clock mid byte as  FAC1 mantissa 3
.AF89  84 63    STY $63   ; save jiffy clock high byte as  FAC1 mantissa 2
.AF8B  85 65    STA $65   ; save jiffy clock low byte as  FAC1 mantissa 4
.AF8D  A0 00    LDY #$00   ; clear Y
.AF8F  84 62    STY $62   ; clear FAC1 mantissa 1
.AF91  60       RTS   ; variable name set-up, var...
