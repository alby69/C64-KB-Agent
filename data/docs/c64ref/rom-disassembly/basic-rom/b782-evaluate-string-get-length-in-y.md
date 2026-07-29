---
title: evaluate string, get length in Y
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
- b782-stringparameter-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B782
  address_end: $B78A
  symbol: evaluate-string-get-length-in-y
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B782**: evaluate string'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B782**: FRESTR, String holen, Länge in A'
---

# $B782 — evaluate string, get length in Y

## Disassemblatura
```assembly
.B782  20 A3 B6 JSR $B6A3   ; evaluate string
.B785  A2 00    LDX #$00   ; set data type = numeric
.B787  86 0D    STX $0D   ; clear data type flag, $FF = string, $00 = numeric
.B789  A8       TAY   ; copy length to Y
.B78A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B782**: evaluate string
- **$B785**: set data type = numeric
- **$B787**: clear data type flag, $FF = string, $00 = numeric
- **$B789**: copy length to Y

### Commodore-64-intern-Buch (Commodore)
- **$B782**: FRESTR, String holen, Länge in A
- **$B785**: Typeflag
- **$B787**: auf numerisch setzen
- **$B789**: Länge in Y
- **$B78A**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*