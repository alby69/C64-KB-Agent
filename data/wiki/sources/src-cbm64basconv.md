---
id: src-cbm64basconv
type: source
title: 'Source Summary: Commodore 64 BASIC data conversion functions'
aliases:
- Commodore 64 BASIC data conversion functions
- cbm64basconv.md
tags:
- basic
- assembly
sources:
- path: data/docs/sta_c64_org/cbm64basconv.md
  sha256: 9ab84eb91998c3fb5257c898738573d0e462d0aec8bef48503e55deb6cb892ea
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 BASIC data conversion functions

**Raw Source File**: `data/docs/sta_c64_org/cbm64basconv.md`
**SHA256**: `9ab84eb91998c3fb5257c898738573d0e462d0aec8bef48503e55deb6cb892ea`

## Summary



# Commodore 64 BASIC data conversion functions

| **Address** | Function | 
|---|---|
| $A96B | Fetch line number from BASIC program and put result to memory addresses $0014-$0015; if first character not a digit then the result is 0; if result is 64000 or above then display "SYNTAX ERROR". (Must call $0073, CHRGET beforehands.) | 
| $A9C4 | Assign value to integer variable; convert FAC to integer and write into variable pointed by memory addresses $0049-$004A. | 
| $A9DA | Assign value to stri...
