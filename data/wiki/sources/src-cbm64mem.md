---
id: src-cbm64mem
type: source
title: 'Source Summary: Commodore 64 memory map'
aliases:
- Commodore 64 memory map
- cbm64mem.md
tags:
- graphics
- memory management
- basic
- sprite programming
- input handling
- sound generation
- assembly
- raster interrupts
sources:
- path: data/docs/sta_c64_org/cbm64mem.md
  sha256: 4c66774549e25bb40208dda34bc89d1a83e11ac03f0d6b04d4cea0838886bb98
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 memory map

**Raw Source File**: `data/docs/sta_c64_org/cbm64mem.md`
**SHA256**: `4c66774549e25bb40208dda34bc89d1a83e11ac03f0d6b04d4cea0838886bb98`

## Summary




# Commodore 64 memory map

| **Address (hex, dec)** | Description   | 
|---|---|
| **$0000-$00FF, 0-255 Zero page** |  | 
| $0000 0 | Processor port data direction register. Bits: Bit #x: 0 = Bit #x in processor port can only be read; 1 = Bit #x in processor port can be read and written. Default: $2F, %00101111. | 
| $0001 1 | Processor port. Bits: Bits #0-#2: Configuration for memory areas $A000-$BFFF, $D000-$DFFF and $E000-$FFFF. Values: 
%x00: RAM visible in all three areas. %x01: RAM visi...
