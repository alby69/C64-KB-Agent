---
id: src-teletext-elite-technical-information
type: source
title: 'Source Summary: Technical information for Teletext Elite'
aliases:
- Technical information for Teletext Elite
- teletext_elite_technical_information.md
tags:
- assembly
- basic
- graphics
- raster interrupts
sources:
- path: data/docs/elite_bbcelite_com/hacks/teletext_elite_technical_information.md
  sha256: 606b2f30e4bf1103b6c0429931a43b5b52018468ffec5a7cb36523ccf57b595e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Technical information for Teletext Elite

**Raw Source File**: `data/docs/elite_bbcelite_com/hacks/teletext_elite_technical_information.md`
**SHA256**: `606b2f30e4bf1103b6c0429931a43b5b52018468ffec5a7cb36523ccf57b595e`

## Summary



# Technical information for Teletext Elite

## Details of how Elite was converted to use teletext

![Teletext Elite rear space view](https://elite.bbcelite.com/images/teletext_elite/station_view.png) 

Under the hood, Teletext Elite is identical to the disc version of BBC Micro Elite, but instead of setting up a mode 4/5 split-screen mode and poking pixels into screen memory, we stay in mode 7 and poke sixels and text characters into screen memory.

To make this process easier, we can scale fr...
