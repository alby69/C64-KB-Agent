---
id: src-populating-several-related-arrays-from-a-single-macro
type: source
title: 'Source Summary: base:populating_several_related_arrays_from_a_single_macro
  [Codebase64 wiki]'
aliases:
- base:populating_several_related_arrays_from_a_single_macro [Codebase64 wiki]
- populating_several_related_arrays_from_a_single_macro.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/populating_several_related_arrays_from_a_single_macro.md
  sha256: 5fdd65505ebf964adcabea69ac3376ff99886c687d9a5d29b3603e7b36dd3627
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:populating_several_related_arrays_from_a_single_macro [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/populating_several_related_arrays_from_a_single_macro.md`
**SHA256**: `5fdd65505ebf964adcabea69ac3376ff99886c687d9a5d29b3603e7b36dd3627`

## Summary



# base:populating_several_related_arrays_from_a_single_macro [Codebase64 wiki]

Often, you have set of data, you need to put in several arrays. For example, in a demo, for each effect you could have init address (2 bytes), run address (2 bytes), and number of frames to run.

One easy way to group these together is by using segments.

First, add segments to your config file, as usual:

```
SEGMENTS
{
	INITLO: load=RAM1, type=ro;
	...
}
```
Secondly, add labels at the beginning of each segment. ...
