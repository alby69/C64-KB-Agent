---
id: src-detecting-sid-type-safe-method
type: source
title: 'Source Summary: Detecting Sid Type - safe method'
aliases:
- Detecting Sid Type - safe method
- detecting_sid_type_-_safe_method.md
tags:
- raster interrupts
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/detecting_sid_type_-_safe_method.md
  sha256: 25344069bded4842e4f20c6626ee06505eb7165cf2c82d70038544c293f3a490
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Detecting Sid Type - safe method

**Raw Source File**: `data/docs/codebase_c64_org/base/detecting_sid_type_-_safe_method.md`
**SHA256**: `25344069bded4842e4f20c6626ee06505eb7165cf2c82d70038544c293f3a490`

## Summary




# Detecting Sid Type - safe method

base:detecting_sid_type_-_safe_method

                # Detecting Sid Type - safe method

This SID detection routine is based on the fact that there is a one cycle delay in the oscillator on 8580 compared to 6581 when turned on.

	;SID DETECTION ROUTINE
	
	;By SounDemon - Based on a tip from Dag Lem.
	;Put together by FTC after SounDemons instructions
	;...and tested by Rambones and Jeff.
	
	; - Don't run this routine on a badline
	
	sei		;No disturbing in...
