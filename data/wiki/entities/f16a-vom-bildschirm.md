---
id: f16a-vom-bildschirm
type: entity
title: vom Bildschirm
aliases:
- vom Bildschirm
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f16a-vom-bildschirm.md
  sha256: c33d91492c7708a7014a99ff6bbaa8bcc8b15ae254f9d85f5a0b22c4be1e9161
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f16a-vom-bildschirm
---

# vom Bildschirm



# $F16A — vom Bildschirm

## Disassemblatura
```assembly
.F16A  85 D0    STA $D0   ; Flag auf Eingabe von Bild- schimrstelle
.F16C  A5 D5    LDA $D5   ; Cursorzeile laden
.F16E  85 C8    STA $C8   ; als Pointer für Ende der Zeile speichern
.F170  4C 32 E6 JMP $E632   ; zu Eingabe vom Bildschirm
.F173  B0 38    BCS $F1AD   ; verzweige zu Eingabe vom IEC-Bus
.F175  C9 02    CMP #$02   ; Eingabe von RS-232 ?
.F177  F0 3F    BEQ $F1B8   ; ja, so verzweige
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F16A**: Flag auf Eingabe von Bild- schimrstelle
- **$F16C**: Cursorzeile laden
- **$F16E**: als Pointer für Ende der Zeile speichern
- **$F170**: zu Eingabe vom Bildschirm
- **$F173**: verzweige zu Eingabe vom IEC-Bus
- **$F175**: Eingabe von RS-232 ?
- **$F177**: ja, so verzweige

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f16a-vom-bildschirm]]
