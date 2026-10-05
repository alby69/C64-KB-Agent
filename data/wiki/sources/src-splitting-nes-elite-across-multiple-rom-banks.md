---
id: src-splitting-nes-elite-across-multiple-rom-banks
type: source
title: 'Source Summary: Splitting NES Elite across multiple ROM banks'
aliases:
- Splitting NES Elite across multiple ROM banks
- splitting_nes_elite_across_multiple_rom_banks.md
tags:
- basic
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/splitting_nes_elite_across_multiple_rom_banks.md
  sha256: 082efd59956f5087088f6a3309bad6be08d0297dc0aa8e9f62b0b223647a5d2b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Splitting NES Elite across multiple ROM banks

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/splitting_nes_elite_across_multiple_rom_banks.md`
**SHA256**: `082efd59956f5087088f6a3309bad6be08d0297dc0aa8e9f62b0b223647a5d2b`

## Summary



# Splitting NES Elite across multiple ROM banks

## Details of the MMC1 controller and the 128K game ROM

The NES was originally designed to take cartridge ROMs containing up to 32K of program code (called PRG-ROM) and 8K of pattern data (called CHR-ROM). This standard setup maps the program code into CPU memory from $8000 to $FFFF and the character patterns into PPU memory from $0000 to $1FFF, with the 2K of on-board WRAM completing the picture from $0000 to $07FF.

This memory structure is e...
