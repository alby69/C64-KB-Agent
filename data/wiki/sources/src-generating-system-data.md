---
id: src-generating-system-data
type: source
title: 'Source Summary: Generating system data'
aliases:
- Generating system data
- generating_system_data.md
tags:
- basic
- assembly
- memory management
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/generating_system_data.md
  sha256: 2dfb8d8b8951406729be71fa9a3c346b0fdc25333cd1206584414d9c242d9e57
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Generating system data

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/generating_system_data.md`
**SHA256**: `2dfb8d8b8951406729be71fa9a3c346b0fdc25333cd1206584414d9c242d9e57`

## Summary



# Generating system data

## The algorithms behind the procedural generation of system data

The Data on System screen is, under the hood, a work of mathematical art. Every bit of data on that screen is procedurally generated from the system seeds, specifically from parts of s0_hi, s1_hi and s1_lo. This enables the game to produce system data like the following, all from three 16-bit numbers:

![The Data on System screen for Lave in the BBC Micro cassette version of Elite](https://elite.bbceli...
