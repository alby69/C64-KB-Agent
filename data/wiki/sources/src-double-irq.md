---
id: src-double-irq
type: source
title: 'Source Summary: Double IRQ stable interrupt'
aliases:
- Double IRQ stable interrupt
- double_irq.md
tags:
- raster interrupts
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/double_irq.md
  sha256: 8b99e413043da68ceb242ee1be54f371e93de8543ba1e286001eab798e71d91e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Double IRQ stable interrupt

**Raw Source File**: `data/docs/codebase_c64_org/base/double_irq.md`
**SHA256**: `8b99e413043da68ceb242ee1be54f371e93de8543ba1e286001eab798e71d91e`

## Summary




# Double IRQ stable interrupt

base:double_irq

                # Double IRQ stable interrupt

Sourcecode by Fungus

```
         *= $2000    ;Assemble to $2000
 
         sei         ;Disable IRQ's
         lda #$7f    ;Disable CIA IRQ's
         sta $dc0d
         sta $dd0d
         lda #$35    ;Bank out kernal and basic
         sta $01     ;$e000-$ffff
 
         lda #<irq1  ;Install RASTER IRQ
         ldx #>irq1  ;into Hardware
         sta $fffe   ;Interrupt Vector
         stx $ffff
 ...
