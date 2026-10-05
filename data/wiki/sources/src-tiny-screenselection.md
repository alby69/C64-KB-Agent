---
id: src-tiny-screenselection
type: source
title: 'Source Summary: base:tiny_screenselection [Codebase64 wiki]'
aliases:
- base:tiny_screenselection [Codebase64 wiki]
- tiny_screenselection.md
tags:
- raster interrupts
- assembly
- basic
- input handling
sources:
- path: data/docs/codebase_c64_org/base/tiny_screenselection.md
  sha256: 9a7a8a7267b47c77165dca1320475add37319cf25824099dc453b1d933677b4b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:tiny_screenselection [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/tiny_screenselection.md`
**SHA256**: `9a7a8a7267b47c77165dca1320475add37319cf25824099dc453b1d933677b4b`

## Summary




# base:tiny_screenselection [Codebase64 wiki]

base:tiny_screenselection

                
Source of a small tool that allows to edit several screens at basic-prompt.

Tried to keep it small.

load it, NEW and SYS 828

F1/F7 select between 26 screens which are all stored in georam. (you start at screen 'C')

F5/F3 are copy/paste for screen.

Code in tapebuffer.

Enjoy if you can :) /enthusi


```
 
!to "geoutil"
bankblk  = $dfff ;00-31($1f) / 16kb
bankpag  = $dffe ;00-63      /256b
bankadr  =...
