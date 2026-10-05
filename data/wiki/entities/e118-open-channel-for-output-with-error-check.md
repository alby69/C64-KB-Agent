---
id: e118-open-channel-for-output-with-error-check
type: entity
title: open channel for output with error check
aliases:
- open channel for output with error check
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e118-open-channel-for-output-with-error-check.md
  sha256: 8396420d77d9a212a29547129dc22a5b6f1dd48476522ae48618b6159cc7fb59
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e118-open-channel-for-output-with-error-check
---

# open channel for output with error check



# $E118 — open channel for output with error check

## Disassemblatura
```assembly
.E118  20 AD E4 JSR $E4AD   ; open channel for output
.E11B  B0 DC    BCS $E0F9   ; if error go handle BASIC I/O error
.E11D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E118**: open channel for output
- **$E11B**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E118**: Ausgabegerät setzen
- **$E11B**: Fehler ?
- **$E11D**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E118**: open output channel via CHKOUT
- **$E11B**: if carry set, handle I/O error
- **$E11D**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e118-open-channel-for-output-with-error-check]]
