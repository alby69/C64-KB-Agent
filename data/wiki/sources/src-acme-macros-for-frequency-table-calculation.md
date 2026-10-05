---
id: src-acme-macros-for-frequency-table-calculation
type: source
title: 'Source Summary: ACME-macros for frequency table calculation'
aliases:
- ACME-macros for frequency table calculation
- acme-macros_for_frequency_table_calculation.md
tags:
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/acme-macros_for_frequency_table_calculation.md
  sha256: 65e570bd89b1c0ef8c1d016d57519a997c91a7599b40ba21c1dc24e5eefe05bf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ACME-macros for frequency table calculation

**Raw Source File**: `data/docs/codebase_c64_org/base/acme-macros_for_frequency_table_calculation.md`
**SHA256**: `65e570bd89b1c0ef8c1d016d57519a997c91a7599b40ba21c1dc24e5eefe05bf`

## Summary



# ACME-macros for frequency table calculation

base:acme-macros_for_frequency_table_calculation

                # ACME-macros for frequency table calculation

As a multiple-time convict of music player coding on the C64 I wanted to be able to optimize the position of the frequency table in memory, so that no page boundary crossings emerge from accessing the tables.

Then I heard about the (440 vs. 432) Hz mystery, tried it out and had a better feeling in my guts running on 432Hz. Thus I start...
