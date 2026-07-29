---
title: jiffy counts
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bf3a-ti-nach-ti
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BF3A
  address_end: $BF4E
  symbol: jiffy-counts
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BF3A**: -2160000    10s hours'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BF3A**: -2 160 000'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $BF3A — jiffy counts

## Disassemblatura
```assembly
.BF3A  FF DF 0A 80   ; -2160000    10s hours
.BF3E  00 03 4B C0   ; +216000        hours
.BF42  FF FF 73 60   ; -36000    10s mins
.BF46  00 00 0E 10   ; +3600        mins
.BF4A  FF FF FD A8   ; -600    10s secs
.BF4E  00 00 00 3C   ; +60        secs
```


## Commenti

### Original Disassembly (—)
- **$BF3A**: -2160000    10s hours
- **$BF3E**: +216000        hours
- **$BF42**: -36000    10s mins
- **$BF46**: +3600        mins
- **$BF4A**: -600    10s secs
- **$BF4E**: +60        secs

### Commodore-64-intern-Buch (Commodore)
- **$BF3A**: -2 160 000
- **$BF3E**: 216 000
- **$BF42**: -36 000
- **$BF46**: 3 600
- **$BF4A**: - 600
- **$BF4E**: 60

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*