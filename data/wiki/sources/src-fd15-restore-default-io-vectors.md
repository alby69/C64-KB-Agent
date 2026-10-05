---
id: src-fd15-restore-default-io-vectors
type: source
title: 'Source Summary: restore default I/O vectors'
aliases:
- restore default I/O vectors
- fd15-restore-default-io-vectors.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd15-restore-default-io-vectors.md
  sha256: ad9e3559d62ce75beb3ab16aa633549959929073010a0ba4937a9a5b7930f465
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: restore default I/O vectors

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fd15-restore-default-io-vectors.md`
**SHA256**: `ad9e3559d62ce75beb3ab16aa633549959929073010a0ba4937a9a5b7930f465`

## Summary



# $FD15 — restore default I/O vectors

## Disassemblatura
```assembly
.FD15  A2 30    LDX #$30   ; pointer to vector table low byte
.FD17  A0 FD    LDY #$FD   ; pointer to vector table high byte
.FD19  18       CLC   ; flag set vectors
```


## Commenti

### Original Disassembly (—)
- **$FD15**: pointer to vector table low byte
- **$FD17**: pointer to vector table high byte
- **$FD19**: flag set vectors

### Commodore-64-intern-Buch (Commodore)
- **$FD15**: LOW- und HIGH-Byte des
- **$FD17**: ...
