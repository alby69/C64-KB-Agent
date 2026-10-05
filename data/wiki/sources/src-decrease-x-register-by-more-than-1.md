---
id: src-decrease-x-register-by-more-than-1
type: source
title: 'Source Summary: Decreasing the X register by more than 1'
aliases:
- Decreasing the X register by more than 1
- decrease_x_register_by_more_than_1.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/decrease_x_register_by_more_than_1.md
  sha256: 112a0c320c14d21a32e58c17a8eeb6d43276e5ffd309a93c0f1a333524ad704b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Decreasing the X register by more than 1

**Raw Source File**: `data/docs/codebase_c64_org/base/decrease_x_register_by_more_than_1.md`
**SHA256**: `112a0c320c14d21a32e58c17a8eeb6d43276e5ffd309a93c0f1a333524ad704b`

## Summary



# Decreasing the X register by more than 1

### Table of Contents

# Decreasing the X register by more than 1

Written by FTC/HT.

Sometimes you need/want to decrease the X register by more than one. That is often done by the following piece of code:

	txa
	sec
	sbc #$xx ;where xx is (obviously) the value to decrease by..
	tax

This procedure takes 8 cycles (and 5 bytes in mem). If the value of the carry flag is always known at this point in the code, the SEC instruction can be removed and the...
