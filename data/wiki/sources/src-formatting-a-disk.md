---
id: src-formatting-a-disk
type: source
title: 'Source Summary: base:formatting_a_disk [Codebase64 wiki]'
aliases:
- base:formatting_a_disk [Codebase64 wiki]
- formatting_a_disk.md
tags:
- raster interrupts
- assembly
- basic
- memory management
sources:
- path: data/docs/codebase_c64_org/base/formatting_a_disk.md
  sha256: 8d400361846ea6b815606f97381e5faf5b558638d1bfbaefbba58b78c7ca7718
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:formatting_a_disk [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/formatting_a_disk.md`
**SHA256**: `8d400361846ea6b815606f97381e5faf5b558638d1bfbaefbba58b78c7ca7718`

## Summary



# base:formatting_a_disk [Codebase64 wiki]

****** Formatting a disk ******

As pointed out elsewhere, the CBMDOS formats disks well. To activate it we send a command via the command channel as follows:

OPEN 15, 8, 15, “N0:DISKNAME,ID”: CLOSE 15

And that's it if You're doing it from Basic. However from inside a program possibly running IRQ, Memory Configurations and even possibly run from a cartridge (meaning KERNAL is bypassed during start up) we can do it as follows:

```
        //-------...
