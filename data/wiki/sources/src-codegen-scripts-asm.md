---
id: src-codegen-scripts-asm
type: source
title: 'Source Summary: base:codegen-scripts.asm [Codebase64 wiki]'
aliases:
- base:codegen-scripts.asm [Codebase64 wiki]
- codegen-scripts_asm.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/codegen-scripts_asm.md
  sha256: f47f60024b49837402c594f32fe28039ed281b029a7f7518989af8d9fccaf112
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:codegen-scripts.asm [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/codegen-scripts_asm.md`
**SHA256**: `f47f60024b49837402c594f32fe28039ed281b029a7f7518989af8d9fccaf112`

## Summary




# base:codegen-scripts.asm [Codebase64 wiki]

base:codegen-scripts.asm

                ```
//general helper scripts..
//gets hi-byte of 16 bit arguments
.function _16bit_nextArgument(arg) {
	.if (arg.getType() == AT_IMMEDIATE) .return CmdArgument(arg.getType(), >arg.getValue())
	.if (arg.getType() == AT_IZEROPAGEY || arg.getType() == AT_IZEROPAGEX) .return arg
	.return CmdArgument(arg.getType(), arg.getValue()+1)
}
//move byte
.pseudocommand mb src;tar {
	lda src
	.if (tar.getType() == AT_IN...
