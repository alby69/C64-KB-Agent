---
id: src-restor
type: source
title: 'Source Summary: e I/O default vectors'
aliases:
- e I/O default vectors
- restor.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/restor.md
  sha256: 60b4d87c36e0337f41509535d4ce524700ec18c83b7644a14342bca8a787473a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: e I/O default vectors

**Raw Source File**: `data/docs/c64ref/kernal-api/restor.md`
**SHA256**: `60b4d87c36e0337f41509535d4ce524700ec18c83b7644a14342bca8a787473a`

## Summary



# Restor — e I/O default vectors ($FF8A)

## Panoramica
La routine KERNAL `Restor` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF8A`
- **Chiamata**: `JSR Restor` o `SYS 65418`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y

scription**: This routine restores the default values of all system
s used in KERNAL and BASIC routines an...
