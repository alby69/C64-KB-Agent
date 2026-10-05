---
id: src-technical-information
type: source
title: 'Source Summary: Technical information for Teletext Elite'
aliases:
- Technical information for Teletext Elite
- technical_information.md
tags:
- basic
- assembly
- raster interrupts
- graphics
sources:
- path: data/docs/elite_bbcelite_com/hacks/teletext_elite/technical_information.md
  sha256: fcae22ce3f9067a2febe7b50089a097e99b8514fb9dc891c7edfadfc2182ca51
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Technical information for Teletext Elite

**Raw Source File**: `data/docs/elite_bbcelite_com/hacks/teletext_elite/technical_information.md`
**SHA256**: `fcae22ce3f9067a2febe7b50089a097e99b8514fb9dc891c7edfadfc2182ca51`

## Summary



# Technical information for Teletext Elite

## Details of how Elite was converted to use teletext

![Teletext Elite rear space view](https://elite.bbcelite.com/images/teletext_elite/station_view.png) 

Under the hood, Teletext Elite is identical to the disc version of BBC Micro Elite, but instead of setting up a mode 4/5 split-screen mode and poking pixels into screen memory, we stay in mode 7 and poke sixels and text characters into screen memory.

To make this process easier, we can scale fr...
