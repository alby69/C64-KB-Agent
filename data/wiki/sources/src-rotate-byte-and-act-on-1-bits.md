---
id: src-rotate-byte-and-act-on-1-bits
type: source
title: 'Source Summary: Rotate byte and perform an action on each bit set to 1'
aliases:
- Rotate byte and perform an action on each bit set to 1
- rotate_byte_and_act_on_1-bits.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/rotate_byte_and_act_on_1-bits.md
  sha256: 275345ccb95fa7e56c753e20180feced7b711c958d6d701e460f1dad90eef574
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Rotate byte and perform an action on each bit set to 1

**Raw Source File**: `data/docs/codebase_c64_org/base/rotate_byte_and_act_on_1-bits.md`
**SHA256**: `275345ccb95fa7e56c753e20180feced7b711c958d6d701e460f1dad90eef574`

## Summary



# Rotate byte and perform an action on each bit set to 1

# Rotate byte and perform an action on each bit set to 1

Invented by Hoogo. Written by Frantic.

Sometimes you've got a byte value and for each bit you want to perform some action if the bit is set to 1 and do nothing, or something else, if the bit is set to 0. Hoogo came up with [a nice way of doing that on CSDb](http://csdb.dk/forums/?roomid=11&topicid=115488#115562) which doesn't clobber any registers except for the status register....
