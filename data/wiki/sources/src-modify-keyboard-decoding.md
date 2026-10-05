---
id: src-modify-keyboard-decoding
type: source
title: 'Source Summary: Modify Keyboard Decoding'
aliases:
- Modify Keyboard Decoding
- modify_keyboard_decoding.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/modify_keyboard_decoding.md
  sha256: 65ba9d75e7bbfe6aca22bb9ba6a216f1e1adfdb0b652dbc15d35eca096ac4d63
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Modify Keyboard Decoding

**Raw Source File**: `data/docs/codebase_c64_org/base/modify_keyboard_decoding.md`
**SHA256**: `65ba9d75e7bbfe6aca22bb9ba6a216f1e1adfdb0b652dbc15d35eca096ac4d63`

## Summary



# Modify Keyboard Decoding

# Modify Keyboard Decoding

The Kernal calls a routine for checking the keyboard in the interrupt routine. The mapping of keyboard code to PETSCII character is done via tables, which are stored in ROM at addresses $EB81 for unshifted keys, $EBC2 for shifted keys, $EC03 for keys pressed together with the CBM key, and $EC78 for keys pressed together with the control key.

The tables are in ROM, but their selection based on the currently pressed Shift/CBM/Ctrl keys is ...
