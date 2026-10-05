---
id: src-e2e0-constants-and-series-for-sincosn
type: source
title: 'Source Summary: constants and series for SIN/COS(n)'
aliases:
- constants and series for SIN/COS(n)
- e2e0-constants-and-series-for-sincosn.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e2e0-constants-and-series-for-sincosn.md
  sha256: 18c988719a9552dfb141274a09a85b2d6360a432d56d911ada0e3dfe43f8b740
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: constants and series for SIN/COS(n)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e2e0-constants-and-series-for-sincosn.md`
**SHA256**: `18c988719a9552dfb141274a09a85b2d6360a432d56d911ada0e3dfe43f8b740`

## Summary



# $E2E0 — constants and series for SIN/COS(n)

## Disassemblatura
```assembly
.E2E0  81 49 0F DA A2   ; 1.570796371, pi/2, as floating number
.E2E5  83 49 0F DA A2   ; 6.28319, 2*pi, as floating number
.E2EA  7F 00 00 00 00   ; 0.25
.E2EF  05   ; series counter
.E2F0  84 E6 1A 2D 1B   ; -14.3813907
.E2F5  86 28 07 FB F8   ; 42.0077971
.E2FA  87 99 68 89 01   ; -76.7041703
.E2FF  87 23 35 DF E1   ; 81.6052237
.E304  86 A5 5D E7 28   ; -41.3147021
.E309  83 49 0F DA A2   ; 6.28318531   2*pi
```
...
