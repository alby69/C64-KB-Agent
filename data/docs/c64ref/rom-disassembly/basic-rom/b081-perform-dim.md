---
title: perform DIM
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b081-basic-befehl-dim
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B081
  address_end: $B08A
  symbol: perform-dim
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B081**: copy "DIM" flag to X'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B081**: nächstes Zeichen'
---

# $B081 — perform DIM

## Disassemblatura
```assembly
.B081  AA       TAX   ; copy "DIM" flag to X
.B082  20 90 B0 JSR $B090   ; search for variable
.B085  20 79 00 JSR $0079   ; scan memory
.B088  D0 F4    BNE $B07E   ; scan for "," and loop if not null
.B08A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B081**: copy "DIM" flag to X
- **$B082**: search for variable
- **$B085**: scan memory
- **$B088**: scan for "," and loop if not null

### Commodore-64-intern-Buch (Commodore)
- **$B081**: nächstes Zeichen
- **$B082**: Variable dimensionieren
- **$B085**: CHRGOT letztes Zeichen holen
- **$B088**: nicht Ende: zur nächsten Var.
- **$B08A**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*