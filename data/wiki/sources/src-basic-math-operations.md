---
id: src-basic-math-operations
type: source
title: 'Source Summary: Addition'
aliases:
- Addition
- basic_math_operations.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/basic_math_operations.md
  sha256: 08928dde6447d53c1921037193766d4046143e548c4daac2fc8650d1b4012491
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Addition

**Raw Source File**: `data/docs/codebase_c64_org/base/basic_math_operations.md`
**SHA256**: `08928dde6447d53c1921037193766d4046143e548c4daac2fc8650d1b4012491`

## Summary



# Addition

### Table of Contents

# Addition

## basic method

The addition of two numbers is very simple, because our CPU provides a command for it: ADC. This command adds the content of the accu to the value addressed by the ADC-command. Furthermore it adds the Carryflag (one or zero) to the result and stores it in the accu. To put it short:

ADC value:	accu = accu + value + carryflag

After that the carryflag will be set if there was an overflow in the addition, or cleared otherwise.

## t...
