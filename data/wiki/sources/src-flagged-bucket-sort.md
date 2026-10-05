---
id: src-flagged-bucket-sort
type: source
title: 'Source Summary: Flagged Bucket Sort'
aliases:
- Flagged Bucket Sort
- flagged_bucket_sort.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/flagged_bucket_sort.md
  sha256: f4bb93f97fd4471981850be10bd898c58277f4a11efbf262080e7a6d16763e9a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Flagged Bucket Sort

**Raw Source File**: `data/docs/codebase_c64_org/base/flagged_bucket_sort.md`
**SHA256**: `f4bb93f97fd4471981850be10bd898c58277f4a11efbf262080e7a6d16763e9a`

## Summary



# Flagged Bucket Sort

# Flagged Bucket Sort

By Christopher Jam.

The following was a run at a fast worst case perfect sort, as may be useful for a bullet hell shooter or other application with fast moving sprites.

The general idea is to maintain a list of 220 buckets, one for each y-position at which a sprite may be visible, and to skip over unused buckets by having a small (27 byte) table of flags.

For any non-zero flag byte, a lookup table used to quickly determine the index of the least...
