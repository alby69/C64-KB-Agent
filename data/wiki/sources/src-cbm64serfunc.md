---
id: src-cbm64serfunc
type: source
title: 'Source Summary: Commodore 64 serial bus functions'
aliases:
- Commodore 64 serial bus functions
- cbm64serfunc.md
tags:
- assembly
sources:
- path: data/docs/sta_c64_org/cbm64serfunc.md
  sha256: 28008f73e52a7b345c0ae843cc91ca597189ade04ec9b3b0958c91c484938723
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 serial bus functions

**Raw Source File**: `data/docs/sta_c64_org/cbm64serfunc.md`
**SHA256**: `28008f73e52a7b345c0ae843cc91ca597189ade04ec9b3b0958c91c484938723`

## Summary



# Commodore 64 serial bus functions

| **Address** | Function | 
|---|---|
| $ED09 | Send TALK command   to serial bus. Input: A = Device number. Output: – Used registers: A. | 
| $ED0C | Send LISTEN command to serial bus. Input: A = Device number. Output: – Used registers: A. | 
| $ED40 | Flush serial bus output cache, at memory   address $0095, to serial bus. Input: – Output: – Used registers: A. | 
| $EDB9 | Send LISTEN secondary address to serial   bus. Input: A = Secondary address. Output...
