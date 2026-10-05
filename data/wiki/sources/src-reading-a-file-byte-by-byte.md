---
id: src-reading-a-file-byte-by-byte
type: source
title: 'Source Summary: Reading from a file byte-by-byte'
aliases:
- Reading from a file byte-by-byte
- reading_a_file_byte-by-byte.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/reading_a_file_byte-by-byte.md
  sha256: 1df8f42c2d0646f3f803ecdf51d07814f38475a118982976a9746712e28fa9f5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Reading from a file byte-by-byte

**Raw Source File**: `data/docs/codebase_c64_org/base/reading_a_file_byte-by-byte.md`
**SHA256**: `1df8f42c2d0646f3f803ecdf51d07814f38475a118982976a9746712e28fa9f5`

## Summary



# Reading from a file byte-by-byte

base:reading_a_file_byte-by-byte

                # Reading from a file byte-by-byte

BASIC code:

10 LA=8192
20 OPEN 2,8,2,"JUST A FILENAME"
30 IF ST<>0 THEN GOTO 60
40 GET#2,A$:IF A$="" THEN A$=CHR$(0)
50 POKE LA,ASC(A$):LA=LA+1:GOTO 30
60 CLOSE 2

Assembler code:

```
load_address = $2000  ; just an example
        LDA #fname_end-fname
        LDX #<fname
        LDY #>fname
        JSR $FFBD     ; call SETNAM
        LDA #$02      ; file number 2
       ...
