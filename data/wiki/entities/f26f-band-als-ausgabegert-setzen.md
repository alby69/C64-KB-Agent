---
id: f26f-band-als-ausgabegert-setzen
type: entity
title: Band als Ausgabegerät setzen
aliases:
- Band als Ausgabegerät setzen
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f26f-band-als-ausgabegert-setzen.md
  sha256: 5ea531ee22583b129b55e5f01d81f3328692d69a46389b17d67624e2d8ca4111
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f26f-band-als-ausgabegert-setzen
---

# Band als Ausgabegerät setzen



# $F26F — Band als Ausgabegerät setzen

## Disassemblatura
```assembly
.F26F  A6 B9    LDX $B9   ; Sekundäradresse laden
.F271  E0 60    CPX #$60   ; mit 'Null' vergleichen
.F273  F0 EA    BEQ $F25F   ; Bandfile zum Lesen, 'NOT OUTPUT FILE'
.F275  85 9A    STA $9A   ; Nummer des Ausgabegeräts setzen
.F277  18       CLC   ; Carry =0 (ok Kennzeichen)
.F278  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F26F**: Sekundäradresse laden
- **$F271**: mit 'Null' vergleichen
- **$F273**: Bandfile zum Lesen, 'NOT OUTPUT FILE'
- **$F275**: Nummer des Ausgabegeräts setzen
- **$F277**: Carry =0 (ok Kennzeichen)
- **$F278**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f26f-band-als-ausgabegert-setzen]]
