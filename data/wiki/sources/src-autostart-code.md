---
id: src-autostart-code
type: source
title: 'Source Summary: Autostart Code'
aliases:
- Autostart Code
- autostart_code.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/autostart_code.md
  sha256: f970e8aef86c9fa03011d8e2418b4213fa6c067a84ae2492663ebcfa3a7bad21
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Autostart Code

**Raw Source File**: `data/docs/codebase_c64_org/base/autostart_code.md`
**SHA256**: `f970e8aef86c9fa03011d8e2418b4213fa6c067a84ae2492663ebcfa3a7bad21`

## Summary



# Autostart Code

# Autostart Code

Although this document concentrates on hardware, there is one thing that you must know about the firmware to get complete control over your computer. As the Commodore 64 always switches the ROMs on upon -RESET, you cannot relocate the RESET vector by writing something in RAM. Instead, you have to use the Autostart code that will be recognized by the KERNAL ROM. If the memory places from $8004 through $8008 contain the PETSCII string 'CBM80' (C3 C2 CD 38 30),...
