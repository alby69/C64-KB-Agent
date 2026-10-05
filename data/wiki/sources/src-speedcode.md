---
id: src-speedcode
type: source
title: 'Source Summary: Speedcode a.k.a. Loop Unrolling'
aliases:
- Speedcode a.k.a. Loop Unrolling
- speedcode.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/speedcode.md
  sha256: 8b3ac8400aafce2abee700090b973034f7a622d25e80d68bd8af5cb6cf73c15a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Speedcode a.k.a. Loop Unrolling

**Raw Source File**: `data/docs/codebase_c64_org/base/speedcode.md`
**SHA256**: `8b3ac8400aafce2abee700090b973034f7a622d25e80d68bd8af5cb6cf73c15a`

## Summary



# Speedcode a.k.a. Loop Unrolling

### Table of Contents

# Speedcode a.k.a. Loop Unrolling

Written by Cruzer/CML

## Intro

One of the earliest optimization tricks invented was loop unrolling, aka. speedcode. It was probably first done to get the most rastersplits on the same line, and then later utilized to break DYCP records, etc. The idea is that instead of a loop, you “unroll” the inner part of the loop that actually does something, and thereby strip away the administrative costs of the ...
