---
id: src-generating-approximate-sines-in-assembly
type: source
title: 'Source Summary: Generating Sine Tables from Parabolas'
aliases:
- Generating Sine Tables from Parabolas
- generating_approximate_sines_in_assembly.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/generating_approximate_sines_in_assembly.md
  sha256: e323cea61616fee33af6cc873a1e3ccb71ca6432753213a188160a7facd0511e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Generating Sine Tables from Parabolas

**Raw Source File**: `data/docs/codebase_c64_org/base/generating_approximate_sines_in_assembly.md`
**SHA256**: `e323cea61616fee33af6cc873a1e3ccb71ca6432753213a188160a7facd0511e`

## Summary



# Generating Sine Tables from Parabolas

### Table of Contents

# Generating Sine Tables from Parabolas

by White Flame

It's been a long-standing tradition in games & demos that sine waves can be approximated by parabolas (see the graph at the bottom). They're a little boxier, and deviate to an error of about 6%, but generally work for doing quick and dirty trig.

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:sine-parabolas2.png)


Parabolas are easy to generate, as they can repre...
