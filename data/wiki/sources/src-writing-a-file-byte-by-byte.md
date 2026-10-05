---
id: src-writing-a-file-byte-by-byte
type: source
title: 'Source Summary: Writing to a file byte-by-byte'
aliases:
- Writing to a file byte-by-byte
- writing_a_file_byte-by-byte.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/writing_a_file_byte-by-byte.md
  sha256: f6b9aa1c442dcc818150ee0a803dd43b08decc425146bf2f8321337f4d2260fb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Writing to a file byte-by-byte

**Raw Source File**: `data/docs/codebase_c64_org/base/writing_a_file_byte-by-byte.md`
**SHA256**: `f6b9aa1c442dcc818150ee0a803dd43b08decc425146bf2f8321337f4d2260fb`

## Summary




# Writing to a file byte-by-byte

base:writing_a_file_byte-by-byte

                # Writing to a file byte-by-byte

BASIC code:

10 FS=8192:FE=16384
20 OPEN 2,8,2,"JUST A FILENAME,P,W"
30 IF ST<>0 THEN GOTO 70
40 A=PEEK(FS):FS=FS+1
50 PRINT#2,CHR$(A);
60 IF FE>FS THEN GOTO 30
70 CLOSE 2

Assembler code:

```
file_start = $2000    ; example addresses
file_end   = $4000
        LDA #fname_end-fname
        LDX #<fname
        LDY #>fname
        JSR $FFBD     ; call SETNAM
        LDA #$02   ...
