---
id: src-dispatch-on-a-byte
type: source
title: 'Source Summary: Dispatching on a Byte'
aliases:
- Dispatching on a Byte
- dispatch_on_a_byte.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/dispatch_on_a_byte.md
  sha256: f810012147c27bfedfc5f7a302d4d69e2d8456d5528ab7b694a9c315eab25ed5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Dispatching on a Byte

**Raw Source File**: `data/docs/codebase_c64_org/base/dispatch_on_a_byte.md`
**SHA256**: `f810012147c27bfedfc5f7a302d4d69e2d8456d5528ab7b694a9c315eab25ed5`

## Summary



# Dispatching on a Byte

base:dispatch_on_a_byte

                ### Table of Contents

# Dispatching on a Byte

*by White Flame and Krill*

The need to dispatch to one of many possible routines based on the value of a byte comes up regularly if you're doing complex data-oriented routines like decompression or scripting, and most often needs to be as fast as possible.

All but the Stack Dispatch routine use self-modification, which will run 1 cycle faster and 1 byte leaner if the dispatch rou...
