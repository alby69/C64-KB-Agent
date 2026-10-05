---
id: src-e118-open-channel-for-output-with-error-check
type: source
title: 'Source Summary: open channel for output with error check'
aliases:
- open channel for output with error check
- e118-open-channel-for-output-with-error-check.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e118-open-channel-for-output-with-error-check.md
  sha256: 8396420d77d9a212a29547129dc22a5b6f1dd48476522ae48618b6159cc7fb59
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: open channel for output with error check

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e118-open-channel-for-output-with-error-check.md`
**SHA256**: `8396420d77d9a212a29547129dc22a5b6f1dd48476522ae48618b6159cc7fb59`

## Summary



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

### Magnus Nyman (Mag...
