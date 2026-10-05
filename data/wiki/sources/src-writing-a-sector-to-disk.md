---
id: src-writing-a-sector-to-disk
type: source
title: 'Source Summary: Writing a sector to disk'
aliases:
- Writing a sector to disk
- writing_a_sector_to_disk.md
tags:
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/writing_a_sector_to_disk.md
  sha256: a6374424e336b9bd8756617f2eb2f49d84adc1869bc1f664b8f2ce3105287149
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Writing a sector to disk

**Raw Source File**: `data/docs/codebase_c64_org/base/writing_a_sector_to_disk.md`
**SHA256**: `a6374424e336b9bd8756617f2eb2f49d84adc1869bc1f664b8f2ce3105287149`

## Summary




# Writing a sector to disk

# Writing a sector to disk

For writing a sector to disk, the Commodore DOS offers the block write command. Due to heavy bugs in the B-W command, Commodore has sacrificed one of the user commands as a bugfix replacement. So instead of B-W you simply use U2.

The format of this DOS command is: “U2 <channel> <drive> <track> <sector>”

The drive parameter is only used for dual disk drives, so for all common C64/C128/C16 drives this parameter will always be 0.

Paramet...
