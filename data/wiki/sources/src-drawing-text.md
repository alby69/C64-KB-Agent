---
id: src-drawing-text
type: source
title: 'Source Summary: Drawing text'
aliases:
- Drawing text
- drawing_text.md
tags:
- memory management
- assembly
- graphics
- basic
- input handling
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/drawing_text.md
  sha256: 1e7afdea8b9609fc1d3a047210f885fbc204facf10e1532e3caed4630ac16348
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Drawing text

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/drawing_text.md`
**SHA256**: `1e7afdea8b9609fc1d3a047210f885fbc204facf10e1532e3caed4630ac16348`

## Summary



# Drawing text

## How Elite draws text on-screen by poking character bitmaps directly into screen memory

There is a lot of text in Elite, so much so that it needs to be compressed (see the deep dive on [printing text tokens](https://elite.bbcelite.com/printing_text_tokens.html) for details). But how does this text make it onto the screen, as in this wordy example from the [Constrictor mission](https://elite.bbcelite.com/the_constrictor_mission.html) briefing?

![The first briefing screen for...
