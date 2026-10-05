---
id: src-cbm64rs2func
type: source
title: 'Source Summary: Commodore 64 RS232 functions'
aliases:
- Commodore 64 RS232 functions
- cbm64rs2func.md
tags:
- general
sources:
- path: data/docs/sta_c64_org/cbm64rs2func.md
  sha256: 42d4ce58a35815386a374ceb51d342b5cf1f5a5a42c09a7f036a84588f6289c2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 RS232 functions

**Raw Source File**: `data/docs/sta_c64_org/cbm64rs2func.md`
**SHA256**: `42d4ce58a35815386a374ceb51d342b5cf1f5a5a42c09a7f036a84588f6289c2`

## Summary



# Commodore 64 RS232 functions

| **Address** | Function | 
|---|---|
| $EF4A | Compute number of   data bits, according to memory address $0293. Input: – Output: X = Number of data bits. Used registers: A, X. | 
| $EFE1 | Define RS232 as default output. Input: A = 2. Output: – Used registers: A. | 
| $F017 | Write byte, from RS232 output cache at   memory address $009E, to RS232. Input: – Output: – Used registers: A, Y. | 
| $F04D | Define RS232 as default input. Input: A = 2. Output: – Used ...
