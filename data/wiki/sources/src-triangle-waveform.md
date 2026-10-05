---
id: src-triangle-waveform
type: source
title: 'Source Summary: Examination of SID triangle waveform'
aliases:
- Examination of SID triangle waveform
- triangle_waveform.md
tags:
- sprite programming
- assembly
- sound generation
- memory management
sources:
- path: data/docs/codebase_c64_org/base/triangle_waveform.md
  sha256: 88b569c2aec3915eca69df77ec73a6df0785b7f8daea3dd4681ba4b46dcf48f2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Examination of SID triangle waveform

**Raw Source File**: `data/docs/codebase_c64_org/base/triangle_waveform.md`
**SHA256**: `88b569c2aec3915eca69df77ec73a6df0785b7f8daea3dd4681ba4b46dcf48f2`

## Summary




# Examination of SID triangle waveform

### Table of Contents

# Examination of SID triangle waveform

## Data recorded on the triangle waveform ($10)

The data are recorded using a REU. The recording is done like this:

        ;* Program 1 *
	;Turn off screen and sprites
	...
	;Set frequency of voice 3
	LDA #<freq
	LDX #>freq
	STA $D40E
	STX $D40F
	;Reset waveform
	LDA #$08	;Set test bit
	STA $D412
	;Setup REU to sample register $D41B for $10000 cycles
	...
	;Start recording
	LDA #$10	;Wave...
