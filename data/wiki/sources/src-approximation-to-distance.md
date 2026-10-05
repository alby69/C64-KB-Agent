---
id: src-approximation-to-distance
type: source
title: 'Source Summary: Approximation to distance'
aliases:
- Approximation to distance
- approximation_to_distance.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/approximation_to_distance.md
  sha256: d33171ae7d903b064e03a11c14c4435544ccb14298a56b10a96c4f4aab70eeec
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Approximation to distance

**Raw Source File**: `data/docs/codebase_c64_org/base/approximation_to_distance.md`
**SHA256**: `d33171ae7d903b064e03a11c14c4435544ccb14298a56b10a96c4f4aab70eeec`

## Summary



# Approximation to distance

base:approximation_to_distance

                # Approximation to distance

Classic distance formula is d= SQR( (x2-x1)^2 + (y2-y1)^2)) and it is well known that if you are comparing the magnitude of two distances you can avoid doing the square root operation as the square of the distances sort in the same order. However, to avoid the square root and the multiplication is the intent of this approximation.

The following approximation is based on a combination of l...
