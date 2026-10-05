---
id: src-reading-a-sector-from-disk
type: source
title: 'Source Summary: Reading a sector from disk'
aliases:
- Reading a sector from disk
- reading_a_sector_from_disk.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/reading_a_sector_from_disk.md
  sha256: 26fc4698711e70990ed7da2e3b8dec90d1b1c2e868fee92be543d142b7692cf3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Reading a sector from disk

**Raw Source File**: `data/docs/codebase_c64_org/base/reading_a_sector_from_disk.md`
**SHA256**: `26fc4698711e70990ed7da2e3b8dec90d1b1c2e868fee92be543d142b7692cf3`

## Summary



# Reading a sector from disk

# Reading a sector from disk

For reading a sector from disk, the Commodore DOS offers the block read command. Due to heavy bugs in the B-R command, Commodore has sacrificed one of the user commands as a bugfix replacement. So instead of B-R you simply use U1.

The format of this DOS command is: “U1 <channel> <drive> <track> <sector>”

The drive parameter is only used for dual disk drives, so for all common C64/C128/C16 drives this parameter will always be 0.

Par...
