---
id: src-afb1-ersten-parameter
type: source
title: 'Source Summary: ersten Parameter'
aliases:
- ersten Parameter
- afb1-ersten-parameter.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/afb1-ersten-parameter.md
  sha256: 9bba5e36728e521d69f99cf898ae148410bd0516326a716cd68b87e354c3d9a9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ersten Parameter

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/afb1-ersten-parameter.md`
**SHA256**: `9bba5e36728e521d69f99cf898ae148410bd0516326a716cd68b87e354c3d9a9`

## Summary



# $AFB1 — ersten Parameter

## Disassemblatura
```assembly
.AFB1  20 FA AE JSR $AEFA   ; prüft auf Klammer auf
.AFB4  20 9E AD JSR $AD9E   ; FRMEVL holen beliebigen Term
.AFB7  20 FD AE JSR $AEFD   ; prüft auf Komma
.AFBA  20 8F AD JSR $AD8F   ; prüft auf String
.AFBD  68       PLA   ; Funktionstoken left$, r$, m$
.AFBE  AA       TAX   ; Akku nach X holen
.AFBF  A5 65    LDA $65   ; Adresse des
.AFC1  48       PHA   ; Stringdescriptors
.AFC2  A5 64    LDA $64   ; holen und auf den Stapel
.AFC4...
