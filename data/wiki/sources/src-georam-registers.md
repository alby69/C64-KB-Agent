---
id: src-georam-registers
type: source
title: 'Source Summary: geoRAM Register Description'
aliases:
- geoRAM Register Description
- georam_registers.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/georam_registers.md
  sha256: 960b07c9b22dbe6d1303b550099094db9f64a8f9b7d36cf510324a90693db020
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: geoRAM Register Description

**Raw Source File**: `data/docs/codebase_c64_org/base/georam_registers.md`
**SHA256**: `960b07c9b22dbe6d1303b550099094db9f64a8f9b7d36cf510324a90693db020`

## Summary



# geoRAM Register Description

base:georam_registers

                # geoRAM Register Description

by White Flame

The geoRAM is a banked memory system. It uses the registers at $dffe and $dfff to determine what part of the geoRAM memory should be visible in the banked window at $de00-$deff.

$dfff - block selection, each block is 16KB
$dffe - select a 256-byte page within the block (0-63)

Since there are only 64 256-byte pages that fit in 16k, the value in $dffe ranges from 0 to 63. The nu...
