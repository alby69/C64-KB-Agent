---
id: src-interrupts
type: source
title: 'Source Summary: Interrupts and timing'
aliases:
- Interrupts and timing
- interrupts.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/interrupts.md
  sha256: 1542d71fc0fec73ad7a635ef8650d94108351853442ce38d4ac2edf199aa3960
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Interrupts and timing

**Raw Source File**: `data/docs/codebase_c64_org/base/interrupts.md`
**SHA256**: `1542d71fc0fec73ad7a635ef8650d94108351853442ce38d4ac2edf199aa3960`

## Summary



# Interrupts and timing

base:interrupts

                ### Table of Contents

# Interrupts and timing

Interrupts can be trigged by the CIA chips and the VIC chip, and they are mostly used to trig specific pieces of code at regular intervals. In demo and game coding, timing is often crucial, and programmers may need to use cycle exact timing to achieve things like stable rasterbars. However, timing is not only about setting up interrupts. It can also be achieved through delay loops and simp...
