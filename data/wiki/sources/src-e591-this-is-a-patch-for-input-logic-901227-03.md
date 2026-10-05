---
id: src-e591-this-is-a-patch-for-input-logic-901227-03
type: source
title: 'Source Summary: ; THIS IS A PATCH FOR INPUT LOGIC 901227-03*'
aliases:
- ; THIS IS A PATCH FOR INPUT LOGIC 901227-03*
- e591-this-is-a-patch-for-input-logic-901227-03.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e591-this-is-a-patch-for-input-logic-901227-03.md
  sha256: 2c11eb9f4b1172f6f33c2eb9b7fc088b5ffe78fbec9103c25c657d49d259699e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ; THIS IS A PATCH FOR INPUT LOGIC 901227-03*

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e591-this-is-a-patch-for-input-logic-901227-03.md`
**SHA256**: `2c11eb9f4b1172f6f33c2eb9b7fc088b5ffe78fbec9103c25c657d49d259699e`

## Summary



# $E591 — ; THIS IS A PATCH FOR INPUT LOGIC 901227-03*

## Disassemblatura
```assembly
.E591  E4 C9    CPX $C9   ; FINPUT CPX LSXP        ;CHECK IF ON SAME LINE
.E593  F0 03    BEQ $E598   ; BEQ FINPUX      ;YES..RETURN TO SEND
.E595  4C ED E6 JMP $E6ED   ; JMP FINDST      ;CHECK IF WE WRAPPED DOWN...
.E598  60       RTS   ; FINPUX RTS
.E599  EA       NOP   ; NOP             ;KEEP THE SPACE THE SAME... ;PANIC NMI ENTRY ;
.E59A  20 A0 E5 JSR $E5A0   ; VPAN   JSR PANIC       ;FIX VIC SCREEN
.E59...
