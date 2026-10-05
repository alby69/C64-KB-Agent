---
id: src-printing-decimal-numbers
type: source
title: 'Source Summary: Printing decimal numbers'
aliases:
- Printing decimal numbers
- printing_decimal_numbers.md
tags:
- assembly
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/printing_decimal_numbers.md
  sha256: b5a7fddc6693b40a875829d18d8fcd756870c502f7541b8904d2b76fb758894b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Printing decimal numbers

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/printing_decimal_numbers.md`
**SHA256**: `b5a7fddc6693b40a875829d18d8fcd756870c502f7541b8904d2b76fb758894b`

## Summary



# Printing decimal numbers

## How to print big decimal numbers with decimal points and padding

Elite prints out a lot of numbers, all of them in decimal (hexadecimal and binary numbers are used internally, but we never see them displayed). The [BPRNT](https://elite.bbcelite.com/cassette/main/subroutine/bprnt.html) routine can print out numbers from 0.1 to 4,294,967,295 (32 set bits), though as the highest figure in the game is the cash pot and that stores the cash amount * 10, the highest fi...
