---
id: src-cartridge-detection
type: source
title: 'Source Summary: 0. Versions used'
aliases:
- 0. Versions used
- cartridge_detection.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/cartridge_detection.md
  sha256: af6903064158e8b327d7b07b3528901a48f8825a946823991ddc376e35390336
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 0. Versions used

**Raw Source File**: `data/docs/codebase_c64_org/base/cartridge_detection.md`
**SHA256**: `af6903064158e8b327d7b07b3528901a48f8825a946823991ddc376e35390336`

## Summary




# 0. Versions used

### Table of Contents

# 0. Versions used

Article written by AlexC. Feel free to add contents!

- Vice 1.22
- C64C Pal
- Action Replay MK VI

# 1. Detecting cartridges

Most cartridges (including RR if active) can be detected by writing to range DE00-DEFF and checking if value written there will be persistent. This allows to detect: Action Replay MK VI, Final Cartridge III and Retro Replay. This method will fail against Trilogic Expert.

start:	lda $de10
	ldx #$0a
	ldy #$...
