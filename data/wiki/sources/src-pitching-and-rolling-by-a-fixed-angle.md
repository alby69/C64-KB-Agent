---
id: src-pitching-and-rolling-by-a-fixed-angle
type: source
title: 'Source Summary: Pitching and rolling by a fixed angle'
aliases:
- Pitching and rolling by a fixed angle
- pitching_and_rolling_by_a_fixed_angle.md
tags:
- assembly
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/pitching_and_rolling_by_a_fixed_angle.md
  sha256: 2dface272ae5e5b532af0175a84fd1c2c459c4b7dbcf1f211ef71cc9477b0531
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Pitching and rolling by a fixed angle

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/pitching_and_rolling_by_a_fixed_angle.md`
**SHA256**: `2dface272ae5e5b532af0175a84fd1c2c459c4b7dbcf1f211ef71cc9477b0531`

## Summary



# Pitching and rolling by a fixed angle

## How other ships manage to pitch and roll in space

We can pitch and roll our ship by varying amounts, as shown by the dashboard's DC and RL indicators, but enemy ships don't have such a luxury - it turns out they can only orientate themselves at a fixed speed. Specifically, they can only pitch or roll by a fixed amount each iteration of the main loop - by an angle of 1/16 radians, or 3.6 degrees.

For example, here's a video showing the space station...
