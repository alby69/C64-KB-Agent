---
id: fb8e-copy-io-start-address-to-buffer-address
type: entity
title: copy I/O start address to buffer address
aliases:
- copy I/O start address to buffer address
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fb8e-copy-io-start-address-to-buffer-address.md
  sha256: e5cf2dca0d530d17ffc302bf1165088725d322ee6cb58cc4ceb054a0fc815c55
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fb8e-copy-io-start-address-to-buffer-address
---

# copy I/O start address to buffer address



# $FB8E — copy I/O start address to buffer address

## Disassemblatura
```assembly
.FB8E  A5 C2    LDA $C2   ; get I/O start address high byte
.FB90  85 AD    STA $AD   ; set buffer address high byte
.FB92  A5 C1    LDA $C1   ; get I/O start address low byte
.FB94  85 AC    STA $AC   ; set buffer address low byte
.FB96  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FB8E**: get I/O start address high byte
- **$FB90**: set buffer address high byte
- **$FB92**: get I/O start address low byte
- **$FB94**: set buffer address low byte

### Commodore-64-intern-Buch (Commodore)
- **$FB8E**: Startadresse
- **$FB90**: $C1/$C2
- **$FB92**: nach $AC/$AD
- **$FB94**: speichern
- **$FB96**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fb8e-copy-io-start-address-to-buffer-address]]
