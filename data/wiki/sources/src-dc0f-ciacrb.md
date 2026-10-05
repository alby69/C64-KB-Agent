---
id: src-dc0f-ciacrb
type: source
title: 'Source Summary: Control Register B'
aliases:
- Control Register B
- dc0f-ciacrb.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dc0f-ciacrb.md
  sha256: d7f99ab18d0982b4f70406cfc964bd72298893591dd697ebf280024d56d19fcc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Control Register B

**Raw Source File**: `data/docs/c64ref/io-map/cia/dc0f-ciacrb.md`
**SHA256**: `d7f99ab18d0982b4f70406cfc964bd72298893591dd697ebf280024d56d19fcc`

## Summary



# CIACRB — Control Register B ($DC0F)

## Panoramica
Il registro o area di memoria CIACRB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0F` (`56335` decimale)
- **Range**: `$DC0F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Set Alarm/TOD-Clock: 1 = Alarm,
       0 = Clock
6-5  Timer B Mode Select:
       00 = Count System 02 Clock Pulses
       01 = Count Positive CNT Transiti...
