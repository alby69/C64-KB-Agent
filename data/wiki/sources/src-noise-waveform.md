---
id: src-noise-waveform
type: source
title: 'Source Summary: Examination of SID noise waveform'
aliases:
- Examination of SID noise waveform
- noise_waveform.md
tags:
- sprite programming
- basic
- assembly
- sound generation
- memory management
sources:
- path: data/docs/codebase_c64_org/base/noise_waveform.md
  sha256: 6d9225ea0254b931bdb0d1a5e96d7455d3a09aa9f728f2a897c08bf3c55b1d8f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Examination of SID noise waveform

**Raw Source File**: `data/docs/codebase_c64_org/base/noise_waveform.md`
**SHA256**: `6d9225ea0254b931bdb0d1a5e96d7455d3a09aa9f728f2a897c08bf3c55b1d8f`

## Summary




# Examination of SID noise waveform

### Table of Contents

# Examination of SID noise waveform

## Sampling the waveform

The waveforms of the SID in the c64 and c128 can be examined, because the SID provides a 8-bit output register of the waveform of voice 3 in register $1b.

The exact waveform can also be examined from the “start” of the waveform, because the test-bit (bit 3 in register $12 for voice 3) can be used to reset the random-waveform.

To examine the data, we want to be able to s...
