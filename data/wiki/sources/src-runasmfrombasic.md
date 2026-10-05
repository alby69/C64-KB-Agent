---
id: src-runasmfrombasic
type: source
title: 'Source Summary: base:runasmfrombasic [Codebase64 wiki]'
aliases:
- base:runasmfrombasic [Codebase64 wiki]
- runasmfrombasic.md
tags:
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/runasmfrombasic.md
  sha256: 37b82cd7a464d5702b1c3d0a5a29546ae9f6160cfca6cd5dcc3443cda27597ad
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:runasmfrombasic [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/runasmfrombasic.md`
**SHA256**: `37b82cd7a464d5702b1c3d0a5a29546ae9f6160cfca6cd5dcc3443cda27597ad`

## Summary




# base:runasmfrombasic [Codebase64 wiki]

### Table of Contents

## Running an Assembler program from BASIC using SYS

A Basic program can call Assembler code using the SYS command. See the [description of the SYS Basic command](https://www.c64-wiki.com/wiki/SYS). Before calling the specified address, SYS “loads” the accumulator, the X and the Y index register, and the status register with the bytes stored at addresses 780–783/$030C–$030F: From BASIC, one can set up parameters and data here, ...
