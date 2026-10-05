---
id: src-a579-crunch-basic-tokens-vector
type: source
title: 'Source Summary: crunch BASIC tokens vector'
aliases:
- crunch BASIC tokens vector
- a579-crunch-basic-tokens-vector.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a579-crunch-basic-tokens-vector.md
  sha256: 457b605cb9911e1d85759499ced261156c9b80b606f10607a9b1d9ac6191c139
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: crunch BASIC tokens vector

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a579-crunch-basic-tokens-vector.md`
**SHA256**: `457b605cb9911e1d85759499ced261156c9b80b606f10607a9b1d9ac6191c139`

## Summary



# $A579 — crunch BASIC tokens vector

## Disassemblatura
```assembly
.A579  6C 04 03 JMP ($0304)   ; do crunch BASIC tokens
```


## Commenti

### Original Disassembly (—)
- **$A579**: do crunch BASIC tokens

### Commodore-64-intern-Buch (Commodore)
- **$A579**: JMP $A57C
- **$A57C**: Zeiger setzen, erstes Zeichen
- **$A57E**: Wert für codierte Zeile
- **$A580**: Flag für Hochkomma
- **$A582**: Zeichen aus Puffer holen
- **$A585**: kein BASIC-Code ? kleiner 128
- **$A587**: Code für Pi ?
- **$...
