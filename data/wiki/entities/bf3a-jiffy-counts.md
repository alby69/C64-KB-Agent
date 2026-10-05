---
id: bf3a-jiffy-counts
type: entity
title: jiffy counts
aliases:
- jiffy counts
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bf3a-jiffy-counts.md
  sha256: 66a870c4d683395d8a94f656acd6bd18ea80c3558d48cb2036ab233b7c12d8e5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bf3a-jiffy-counts
---

# jiffy counts



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

## References
- Source: [[src-bf3a-jiffy-counts]]
