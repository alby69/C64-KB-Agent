---
id: src-stable-raster-with-lightpen
type: source
title: 'Source Summary: Stable Raster with Lightpen'
aliases:
- Stable Raster with Lightpen
- stable_raster_with_lightpen.md
tags:
- sprite programming
- input handling
- basic
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/codebase_c64_org/base/stable_raster_with_lightpen.md
  sha256: ffd7939847d874580dae7834a680d33413ecbc48c7ec884c77394d4bc8274c74
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Stable Raster with Lightpen

**Raw Source File**: `data/docs/codebase_c64_org/base/stable_raster_with_lightpen.md`
**SHA256**: `ffd7939847d874580dae7834a680d33413ecbc48c7ec884c77394d4bc8274c74`

## Summary




# Stable Raster with Lightpen

### Table of Contents

# Stable Raster with Lightpen

I've seen a few references to getting a stable raster by triggering the light pen but couldn't find it in any tutorials. So I was curious about it and have documented here what I've found out.

It turns out to be a mostly useless technique because of the following problems:

- It's wrecked if the user presses space or joystick #1 button
- It can only be used once per frame!

But if you can live with that (for...
