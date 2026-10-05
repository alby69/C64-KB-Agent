---
id: src-dictionary-compression
type: source
title: 'Source Summary: base:dictionary_compression [Codebase64 wiki]'
aliases:
- base:dictionary_compression [Codebase64 wiki]
- dictionary_compression.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/dictionary_compression.md
  sha256: 446de686e31520c2f75acd9f8ef13b5f3209e2930c515076f6a9e0fd83210ab2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:dictionary_compression [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/dictionary_compression.md`
**SHA256**: `446de686e31520c2f75acd9f8ef13b5f3209e2930c515076f6a9e0fd83210ab2`

## Summary



# base:dictionary_compression [Codebase64 wiki]

Full source and example code is in here: [https://github.com/martinpiper/C64Public/tree/master/DictionaryCompression](https://github.com/martinpiper/C64Public/tree/master/DictionaryCompression)

A variant of literal/copy compression (LZMPiE) that uses an extra common dictionary (hence LZMPiED) calculated from multiple input files, to reduce overall compressed data size.

The build for this tool is also a good demonstration on how to unit test 65...
