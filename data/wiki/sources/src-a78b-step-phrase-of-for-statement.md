---
id: src-a78b-step-phrase-of-for-statement
type: source
title: 'Source Summary: "STEP" PHRASE OF "FOR" STATEMENT'
aliases:
- '"STEP" PHRASE OF "FOR" STATEMENT'
- a78b-step-phrase-of-for-statement.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a78b-step-phrase-of-for-statement.md
  sha256: 21582ff0742bce936009f0af57f48af455fda9ddf940b24d976f7ccf14af3f49
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: "STEP" PHRASE OF "FOR" STATEMENT

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a78b-step-phrase-of-for-statement.md`
**SHA256**: `21582ff0742bce936009f0af57f48af455fda9ddf940b24d976f7ccf14af3f49`

## Summary



# $A78B — "STEP" PHRASE OF "FOR" STATEMENT

## Disassemblatura
```assembly
.A78B  A9 BC    LDA #$BC   ; STEP DEFAULT=1
.A78D  A0 B9    LDY #$B9
.A78F  20 A2 BB JSR $BBA2
.A792  20 79 00 JSR $0079
.A795  C9 A9    CMP #$A9
.A797  D0 06    BNE $A79F   ; USE DEFAULT VALUE OF 1.0
.A799  20 73 00 JSR $0073   ; STEP SPECIFIED, GET IT
.A79C  20 8A AD JSR $AD8A
.A79F  20 2B BC JSR $BC2B
.A7A2  20 38 AE JSR $AE38
.A7A5  A5 4A    LDA $4A
.A7A7  48       PHA
.A7A8  A5 49    LDA $49
.A7AA  48       PHA
.A7...
