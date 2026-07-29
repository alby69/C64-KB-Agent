---
title: get value from line .. continued
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
- aead-get-value-from-line-continued
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $AEAD
  address_end: $AEBB
  symbol: get-value-from-line-continued
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AEAD**: compare with "."'
---

# $AEAD — get value from line .. continued

## Disassemblatura
```assembly
.AEAD  C9 2E    CMP #$2E   ; compare with "."
.AEAF  F0 DE    BEQ $AE8F   ; if so get FAC1 from string and return, e.g. was .123 wasn't .123 so ...
.AEB1  C9 AB    CMP #$AB   ; compare with token for -
.AEB3  F0 58    BEQ $AF0D   ; branch if - token, do set-up for functions wasn't -123 so ...
.AEB5  C9 AA    CMP #$AA   ; compare with token for +
.AEB7  F0 D1    BEQ $AE8A   ; branch if + token, +1 = 1 so ignore leading + it wasn't any sort of number so ...
.AEB9  C9 22    CMP #$22   ; compare with "
.AEBB  D0 0F    BNE $AECC   ; branch if not open quote was open quote so get the enclosed string
```


## Commenti

### Original Disassembly (—)
- **$AEAD**: compare with "."
- **$AEAF**: if so get FAC1 from string and return, e.g. was .123 wasn't .123 so ...
- **$AEB1**: compare with token for -
- **$AEB3**: branch if - token, do set-up for functions wasn't -123 so ...
- **$AEB5**: compare with token for +
- **$AEB7**: branch if + token, +1 = 1 so ignore leading + it wasn't any sort of number so ...
- **$AEB9**: compare with "
- **$AEBB**: branch if not open quote was open quote so get the enclosed string

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*