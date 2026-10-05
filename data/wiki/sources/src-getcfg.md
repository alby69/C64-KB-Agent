---
id: src-getcfg
type: source
title: 'Source Summary: GETCFG'
aliases:
- GETCFG
- getcfg.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/getcfg.md
  sha256: 078c6a34ae1f33f0f08af906eb48f21192b8001b62a61fa567e347133649bbfe
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: GETCFG

**Raw Source File**: `data/docs/c64ref/kernal-api/getcfg.md`
**SHA256**: `078c6a34ae1f33f0f08af906eb48f21192b8001b62a61fa567e347133649bbfe`

## Summary




# GETCFG —  ($FF6B)

## Panoramica
La routine KERNAL `GETCFG` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF6B`
- **Chiamata**: `JSR GETCFG` o `SYS 65387`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine translates a bank number (0-15) into the
ponding MMU register setting to configure the system
at bank. Call the routine with .X holding the bank num-
pon return, the accumulator will hold the correspond...
