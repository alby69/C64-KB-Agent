---
id: src-classic-hard-restart-and-about-adsr-in-generally
type: source
title: 'Source Summary: ADSR Discussion Notes'
aliases:
- ADSR Discussion Notes
- classic_hard-restart_and_about_adsr_in_generally.md
tags:
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/classic_hard-restart_and_about_adsr_in_generally.md
  sha256: 4305836aeb80fee26ae5fd566297fa53fe482a6477b699465f2819dd79e4e6b3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ADSR Discussion Notes

**Raw Source File**: `data/docs/codebase_c64_org/base/classic_hard-restart_and_about_adsr_in_generally.md`
**SHA256**: `4305836aeb80fee26ae5fd566297fa53fe482a6477b699465f2819dd79e4e6b3`

## Summary



# ADSR Discussion Notes

### Table of Contents

# ADSR Discussion Notes

By mixer with contributions from many.

Few notes about what has been discussed about SID envelopes lately at CSDB and at IRC. Errors are all mine, and this being a Wiki, you can fix them. :) This text could use some generic bits about ADSR and code-examples.

# What is ADSR-Bug?

SID volume-envelope aka. ADSR has a 15-bit LFSR that acts as a prescaler to ENV counter. This LFSR determines the rate at which ENV counter is ...
