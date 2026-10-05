---
id: src-6510-features
type: source
title: 'Source Summary: 6510 features'
aliases:
- 6510 features
- 6510_features.md
tags:
- sprite programming
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/6510_features.md
  sha256: 430265889caf3aea02b9665d1891dab27302b8f2ba0cd32907a0adc1408fe793
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 6510 features

**Raw Source File**: `data/docs/codebase_c64_org/base/6510_features.md`
**SHA256**: `430265889caf3aea02b9665d1891dab27302b8f2ba0cd32907a0adc1408fe793`

## Summary



# 6510 features

base:6510_features

                # 6510 features

- PHP always pushes the Break (B) flag as a `1' to the stack. Jukka Tapanimäki claimed in C=lehti issue 3/89, on page 27 that the processor makes a logical OR between the status register's bit 4 and the bit 8 of the stack pointer register (which is always 1). He did not give any reasons for this argument, and has refused to clarify it afterwards. Well, this was not the only error in his article…

- Indirect addressing modes ...
