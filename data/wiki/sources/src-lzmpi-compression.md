---
id: src-lzmpi-compression
type: source
title: 'Source Summary: LZMPi Compression'
aliases:
- LZMPi Compression
- lzmpi_compression.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/lzmpi_compression.md
  sha256: b4fa2e846a8432484364762d98de601e444d0bb8b4bf12503e44871bdbecaf50
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LZMPi Compression

**Raw Source File**: `data/docs/codebase_c64_org/base/lzmpi_compression.md`
**SHA256**: `b4fa2e846a8432484364762d98de601e444d0bb8b4bf12503e44871bdbecaf50`

## Summary



# LZMPi Compression

### Table of Contents

# LZMPi Compression

## The compression algorithm

The compressor uses quite a lot of C++ and STL mostly because STL has well optimised sorted associative containers and it makes the core algorithm easier to understand because there is less code to read through. Even so, when compiled in release mode this algorithm uses less memory and executes a little quicker than some other comparable LZ based algorithms written in C. The algorithm inserts previou...
