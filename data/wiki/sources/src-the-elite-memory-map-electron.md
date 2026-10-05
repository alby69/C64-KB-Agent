---
id: src-the-elite-memory-map-electron
type: source
title: 'Source Summary: Acorn Electron Elite memory map'
aliases:
- Acorn Electron Elite memory map
- the_elite_memory_map_electron.md
tags:
- basic
- assembly
- memory management
- graphics
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/the_elite_memory_map_electron.md
  sha256: d9566c20eb7e578aaf31928ced78a5b78805be356d7f7f95aa77af6bbac16967
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Acorn Electron Elite memory map

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/the_elite_memory_map_electron.md`
**SHA256**: `d9566c20eb7e578aaf31928ced78a5b78805be356d7f7f95aa77af6bbac16967`

## Summary



# Acorn Electron Elite memory map

## Memory usage in the smallest and most basic version of Elite

Memory might be tight in the [BBC Micro cassette version of Elite](https://elite.bbcelite.com/the_elite_memory_map.html), but things get really problematic in the Electron version. The Electron has the same 32K of user RAM as the BBC, but it's missing one vital feature that the BBC versions use to reduce screen memory, and which can't be implemented on the Electron.

The BBC versions reprogram t...
