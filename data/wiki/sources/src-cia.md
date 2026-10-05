---
id: src-cia
type: source
title: 'Source Summary: CIA (6526) Programming'
aliases:
- CIA (6526) Programming
- cia.md
tags:
- raster interrupts
- memory management
- input handling
sources:
- path: data/docs/codebase_c64_org/base/cia.md
  sha256: e8d2b730b6c90a450c38523b5a6569ad2ee43ac10c24a8b54af30ea0e2222238
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CIA (6526) Programming

**Raw Source File**: `data/docs/codebase_c64_org/base/cia.md`
**SHA256**: `e8d2b730b6c90a450c38523b5a6569ad2ee43ac10c24a8b54af30ea0e2222238`

## Summary



# CIA (6526) Programming

base:cia

                ### Table of Contents

# CIA (6526) Programming

A lot of stuff is controlled by the CIA chips, such as keyboard/joystick reading, serial IO, timer interrupts, VIC bank switching and… You name it!

## Interrupts

There are many kinds of interrupts on the C64. The CIA generates Timer interrupts, which can be set to be trigged at specific timed intervals. Other kinds of interrupts, such as raster interrupts are trigged by the VIC chip. Informat...
