---
id: src-use-shy-as-sty-x-or-shx-as-stx-y
type: source
title: 'Source Summary: Store X Indexed by Y and Vice-Versa With SHX/SHY'
aliases:
- Store X Indexed by Y and Vice-Versa With SHX/SHY
- use_shy_as_sty_x_or_shx_as_stx_y.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/use_shy_as_sty_x_or_shx_as_stx_y.md
  sha256: 3f28cfb6e36459e06299167cbfa36991c12a0beeadea125f48e2995b66f17e58
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Store X Indexed by Y and Vice-Versa With SHX/SHY

**Raw Source File**: `data/docs/codebase_c64_org/base/use_shy_as_sty_x_or_shx_as_stx_y.md`
**SHA256**: `3f28cfb6e36459e06299167cbfa36991c12a0beeadea125f48e2995b66f17e58`

## Summary



# Store X Indexed by Y and Vice-Versa With SHX/SHY

# Store X Indexed by Y and Vice-Versa With SHX/SHY

The 6510 doesn't have a stx abs,y or sty abs,x. So instead you would normally do something like this:

//store X indexed by Y:
txa
sta address,y
//store Y indexed by X:
tya
sta address,x

Which each take 7 cycles. But instead you can do this, which only takes 5:

//store X indexed by Y:
shx address,y
//store Y indexed by X:
shy address,x

However, there's a little catch. The value is and'ed ...
