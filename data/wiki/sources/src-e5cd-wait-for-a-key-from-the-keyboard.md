---
id: src-e5cd-wait-for-a-key-from-the-keyboard
type: source
title: 'Source Summary: wait for a key from the keyboard'
aliases:
- wait for a key from the keyboard
- e5cd-wait-for-a-key-from-the-keyboard.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e5cd-wait-for-a-key-from-the-keyboard.md
  sha256: c087b023c8bf0d1014ada9dd5c4150833cb34660cecaf8b243b76373218f7f31
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: wait for a key from the keyboard

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e5cd-wait-for-a-key-from-the-keyboard.md`
**SHA256**: `c087b023c8bf0d1014ada9dd5c4150833cb34660cecaf8b243b76373218f7f31`

## Summary



# $E5CD — wait for a key from the keyboard

## Disassemblatura
```assembly
.E5CD  A5 C6    LDA $C6   ; get the keyboard buffer index
.E5CF  85 CC    STA $CC   ; cursor enable, $00 = flash cursor, $xx = no flash
.E5D1  8D 92 02 STA $0292   ; screen scrolling flag, $00 = scroll, $xx = no scroll this disables both the cursor flash and the screen scroll while there are characters in the keyboard buffer
.E5D4  F0 F7    BEQ $E5CD   ; loop if the buffer is empty
.E5D6  78       SEI   ; disable the in...
