---
id: src-cbm64dtsfunc
type: source
title: 'Source Summary: Commodore 64 datasette functions'
aliases:
- Commodore 64 datasette functions
- cbm64dtsfunc.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/sta_c64_org/cbm64dtsfunc.md
  sha256: d2e8a54fce3cd4876cdbbf8d28953831214d5c3a637d1017664ff71aed1cec7a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 datasette functions

**Raw Source File**: `data/docs/sta_c64_org/cbm64dtsfunc.md`
**SHA256**: `d2e8a54fce3cd4876cdbbf8d28953831214d5c3a637d1017664ff71aed1cec7a`

## Summary



# Commodore 64 datasette functions

| **Address** | Function | 
|---|---|
| $F179 | Read byte from   datasette (data files only). Input: – Output: A = Byte read. Used registers: A, Y. | 
| $F1DD | Write byte to datasette. Input: Carry = 1; A = Byte to write; 0 = End of file. Output: – Used registers: – | 
| $F22A | Define datasette as default input. Input: A = 1. Output: – Used registers: A, X. | 
| $F26F | Define datasette as default output. Input: A = 1. Output: – Used registers: A, X. | 
| ...
