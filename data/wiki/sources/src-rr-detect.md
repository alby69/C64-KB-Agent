---
id: src-rr-detect
type: source
title: 'Source Summary: Detect Retro Replay hardware'
aliases:
- Detect Retro Replay hardware
- rr_detect.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/rr_detect.md
  sha256: 2b5ce6158e572974e736cd3e3f3521591a60e6f4d445f7bfbf2987c79279c584
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Detect Retro Replay hardware

**Raw Source File**: `data/docs/codebase_c64_org/base/rr_detect.md`
**SHA256**: `2b5ce6158e572974e736cd3e3f3521591a60e6f4d445f7bfbf2987c79279c584`

## Summary



# Detect Retro Replay hardware

base:rr_detect

                # Detect Retro Replay hardware

By FMan.

This is a straight-forward detection routine to find out if a Retro Replay is active on the system. It works by writing different bytes to the same address in the $8000-$9FFF range. If there is no cart, all of the writes will go to normal RAM and the latest byte will be the one read back. Otherwise some of them go to different RR RAM banks. Successful readback of both bytes written to the ...
