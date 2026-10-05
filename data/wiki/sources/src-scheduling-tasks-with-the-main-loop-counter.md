---
id: src-scheduling-tasks-with-the-main-loop-counter
type: source
title: 'Source Summary: Scheduling tasks with the main loop counter'
aliases:
- Scheduling tasks with the main loop counter
- scheduling_tasks_with_the_main_loop_counter.md
tags:
- basic
- assembly
- memory management
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/scheduling_tasks_with_the_main_loop_counter.md
  sha256: ec62716ee31478067c3f99d5ee5de82962af80fe7f701f569648f9289876a984
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Scheduling tasks with the main loop counter

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/scheduling_tasks_with_the_main_loop_counter.md`
**SHA256**: `ec62716ee31478067c3f99d5ee5de82962af80fe7f701f569648f9289876a984`

## Summary



# Scheduling tasks with the main loop counter

## How the main loop counter controls what we do and when we do it

Elite's program flow is based around a main loop that starts iterating as soon as you get past the title screen. At its simplest - when docked - the main loop does little more than listening for function key presses and calling the relevant routines for cargo, equipment, charts and so on, but out in space in the midst of a frenetic battle for survival, things get an awful lot busi...
