---
id: src-drawing-pixels-in-the-commodore-64-version
type: source
title: 'Source Summary: Drawing pixels in the Commodore 64 version'
aliases:
- Drawing pixels in the Commodore 64 version
- drawing_pixels_in_the_commodore_64_version.md
tags:
- basic
- assembly
- graphics
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/drawing_pixels_in_the_commodore_64_version.md
  sha256: e531e5d11845b04de736666bce625ad82e1b27800239b846a64995dacfa1303a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Drawing pixels in the Commodore 64 version

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/drawing_pixels_in_the_commodore_64_version.md`
**SHA256**: `e531e5d11845b04de736666bce625ad82e1b27800239b846a64995dacfa1303a`

## Summary



# Drawing pixels in the Commodore 64 version

## Updating the bitmap screen in the Commodore 64 version of Elite

Even though the Commodore 64's graphics are driven by a completely different chip to the BBC Micro and Acorn Electron, it turns out that the Commodore's pixel routines are a mash-up of the code from both Acorn platforms. Let's take a look.

The BBC Micro's graphics come courtesy of a 6845 CRTC chip, a custom-built Video ULA and a 6522 System VIA timer, and they look like this:

![A...
