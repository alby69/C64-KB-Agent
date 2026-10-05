---
id: aead-get-value-from-line-continued
type: entity
title: get value from line .. continued
aliases:
- get value from line .. continued
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aead-get-value-from-line-continued.md
  sha256: a701fd2cd9b0d69f888817ff0d2faffdb5d3f9a625cabffac902e2775e6e107c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-aead-get-value-from-line-continued
---

# get value from line .. continued



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

## References
- Source: [[src-aead-get-value-from-line-continued]]
