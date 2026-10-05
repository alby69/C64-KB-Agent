---
id: src-scoring-points
type: source
title: 'Source Summary: Scoring points'
aliases:
- Scoring points
- scoring_points.md
tags:
- raster interrupts
- sprite programming
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scoring_points.md
  sha256: 3798b02c02e332188d80acb648c14570e6441d493f1902c4219df0690ceec9dd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Scoring points

**Raw Source File**: `data/docs/codebase_c64_org/base/scoring_points.md`
**SHA256**: `3798b02c02e332188d80acb648c14570e6441d493f1902c4219df0690ceec9dd`

## Summary



# Scoring points

### Table of Contents

# Scoring points

by Achim

There are three ways to code scoring.

## 1) Decimal mode

This one can be found in many games. You only have to declare a couple of variables for the player's score and switch to decimal mode.

Example for six digits:

sed		//set decimal mode
clc
lda #$50	//50 points scored
adc score1	//ones and tens
sta score1
lda score2	//hundreds and thousands
adc #00
sta score2
lda score3	//ten-thousands and hundred-thousands
adc #00
sta...
