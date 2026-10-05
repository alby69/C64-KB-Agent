---
id: src-vicii-memory-organizing
type: source
title: 'Source Summary: The VIC banks'
aliases:
- The VIC banks
- vicii_memory_organizing.md
tags:
- sprite programming
- basic
- graphics
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/vicii_memory_organizing.md
  sha256: 17ff8ae7f451f69790cff0cac756e725b3d68a6561d8693c5e0b81c04ff0c848
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: The VIC banks

**Raw Source File**: `data/docs/codebase_c64_org/base/vicii_memory_organizing.md`
**SHA256**: `17ff8ae7f451f69790cff0cac756e725b3d68a6561d8693c5e0b81c04ff0c848`

## Summary




# The VIC banks

### Table of Contents

# The VIC banks

By Oswald/Resource.

The first important thing is that the VICII can only adress 16k ram at once. This means that the 64k memory is divided into four 16k VIC banks. $DD00's lowmost 2 bits controls that which bank is seen by the VIC:

$DD00 = %xxxxxx11 -> bank0: $0000-$3fff
$DD00 = %xxxxxx10 -> bank1: $4000-$7fff
$DD00 = %xxxxxx01 -> bank2: $8000-$bfff
$DD00 = %xxxxxx00 -> bank3: $c000-$ffff

$DD00 should be handled with care when also l...
