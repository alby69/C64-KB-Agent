---
id: src-8bit-atan2-8-bit-angle
type: source
title: 'Source Summary: 8-bit atan2'
aliases:
- 8-bit atan2
- 8bit_atan2_8-bit_angle.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8bit_atan2_8-bit_angle.md
  sha256: fd0218032143e6ff49194cc040b962f1add87c5c4a3b8385dd0d1ae94445d696
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 8-bit atan2

**Raw Source File**: `data/docs/codebase_c64_org/base/8bit_atan2_8-bit_angle.md`
**SHA256**: `fd0218032143e6ff49194cc040b962f1add87c5c4a3b8385dd0d1ae94445d696`

## Summary



# 8-bit atan2

base:8bit_atan2_8-bit_angle

                # 8-bit atan2

might be more precise to add a clc adc #$01 after each eor #$ff, you have to modify all the preceding bcs *+4/ bcc *+4 to *+7 to get the branches correct. also you can omit the clc where bcs is used. adding a SEC before all sbc's might increase the accuracy even further. :) /Oswald

;; Calculate the angle, in a 256-degree circle, between two points.
;; The trick is to use logarithmic division to get the y/x ratio and
;;...
