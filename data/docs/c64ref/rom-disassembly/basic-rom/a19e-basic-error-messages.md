---
title: BASIC error messages
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a19e-error-messages
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $A19E
  address_end: $A320
  symbol: basic-error-messages
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A19E**: 1 too many files'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A19E**: too many files'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A19E**: 1 too many files'
---

# $A19E — BASIC error messages

## Disassemblatura
```assembly
.A19E  54 4F   ; 1 too many files
.A1A0  4F 20 4D 41 4E 59 20 46
.A1A8  49 4C 45 D3 46 49 4C 45   ; 2 file open
.A1B0  20 4F 50 45 CE 46 49 4C   ; 3 file not open
.A1B8  45 20 4E 4F 54 20 4F 50
.A1C0  45 CE 46 49 4C 45 20 4E   ; 4 file not found
.A1C8  4F 54 20 46 4F 55 4E C4   ; 5 device not present
.A1D0  44 45 56 49 43 45 20 4E
.A1D8  4F 54 20 50 52 45 53 45
.A1E0  4E D4 4E 4F 54 20 49 4E   ; 6 not input file
.A1E8  50 55 54 20 46 49 4C C5
.A1F0  4E 4F 54 20 4F 55 54 50   ; 7 not output file
.A1F8  55 54 20 46 49 4C C5 4D
.A200  49 53 53 49 4E 47 20 46   ; 8 missing filename
.A208  49 4C 45 20 4E 41 4D C5
.A210  49 4C 4C 45 47 41 4C 20   ; 9 illegal device number
.A218  44 45 56 49 43 45 20 4E
.A220  55 4D 42 45 D2 4E 45 58   ; 10 next without for
.A228  54 20 57 49 54 48 4F 55
.A230  54 20 46 4F D2 53 59 4E   ; 11 syntax
.A238  54 41 D8 52 45 54 55 52   ; 12 return without gosub
.A240  4E 20 57 49 54 48 4F 55
.A248  54 20 47 4F 53 55 C2 4F   ; 13 out of data
.A250  55 54 20 4F 46 20 44 41
.A258  54 C1 49 4C 4C 45 47 41   ; 14 illegal quantity
.A260  4C 20 51 55 41 4E 54 49
.A268  54 D9 4F 56 45 52 46 4C   ; 15 overflow
.A270  4F D7 4F 55 54 20 4F 46   ; 16 out of memory
.A278  20 4D 45 4D 4F 52 D9 55   ; 17 undef'd statement
.A280  4E 44 45 46 27 44 20 53
.A288  54 41 54 45 4D 45 4E D4
.A290  42 41 44 20 53 55 42 53   ; 18 bad subscript
.A298  43 52 49 50 D4 52 45 44   ; 19 redim'd array
.A2A0  49 4D 27 44 20 41 52 52
.A2A8  41 D9 44 49 56 49 53 49   ; 20 division by zero
.A2B0  4F 4E 20 42 59 20 5A 45
.A2B8  52 CF 49 4C 4C 45 47 41   ; 21 illegal direct
.A2C0  4C 20 44 49 52 45 43 D4
.A2C8  54 59 50 45 20 4D 49 53   ; 22 type mismatch
.A2D0  4D 41 54 43 C8 53 54 52   ; 23 string too long
.A2D8  49 4E 47 20 54 4F 4F 20
.A2E0  4C 4F 4E C7 46 49 4C 45   ; 24 file data
.A2E8  20 44 41 54 C1 46 4F 52   ; 25 formula too complex
.A2F0  4D 55 4C 41 20 54 4F 4F
.A2F8  20 43 4F 4D 50 4C 45 D8
.A300  43 41 4E 27 54 20 43 4F   ; 26 can't continue
.A308  4E 54 49 4E 55 C5 55 4E   ; 27 undef'd function
.A310  44 45 46 27 44 20 46 55
.A318  4E 43 54 49 4F CE 56 45   ; 28 verify
.A320  52 49 46 D9 4C 4F 41 C4   ; 29 load
```


## Commenti

### Original Disassembly (—)
- **$A19E**: 1 too many files
- **$A1A8**: 2 file open
- **$A1B0**: 3 file not open
- **$A1C0**: 4 file not found
- **$A1C8**: 5 device not present
- **$A1E0**: 6 not input file
- **$A1F0**: 7 not output file
- **$A200**: 8 missing filename
- **$A210**: 9 illegal device number
- **$A220**: 10 next without for
- **$A230**: 11 syntax
- **$A238**: 12 return without gosub
- **$A248**: 13 out of data
- **$A258**: 14 illegal quantity
- **$A268**: 15 overflow
- **$A270**: 16 out of memory
- **$A278**: 17 undef'd statement
- **$A290**: 18 bad subscript
- **$A298**: 19 redim'd array
- **$A2A8**: 20 division by zero
- **$A2B8**: 21 illegal direct
- **$A2C8**: 22 type mismatch
- **$A2D0**: 23 string too long
- **$A2E0**: 24 file data
- **$A2E8**: 25 formula too complex
- **$A300**: 26 can't continue
- **$A308**: 27 undef'd function
- **$A318**: 28 verify
- **$A320**: 29 load

### Marko Mäkelä (Marko Mäkelä)
- **$A19E**: too many files
- **$A1AC**: file open
- **$A1B5**: file not open
- **$A1C2**: file not found
- **$A1D0**: device not present
- **$A1E2**: not input file
- **$A1F0**: not output file
- **$A1FF**: missing file name
- **$A210**: illegal device number
- **$A225**: next without for
- **$A235**: syntax
- **$A23B**: return without gosub
- **$A24F**: out of data
- **$A25A**: illegal quantity
- **$A26A**: overflow
- **$A272**: out of memory
- **$A27F**: undef'd statement
- **$A290**: bad subscript
- **$A29D**: redim'd array
- **$A2AA**: division by zero
- **$A2BA**: illegal direct
- **$A2C8**: type mismatch
- **$A2D5**: string to long
- **$A2E4**: file data
- **$A2ED**: formula too complex
- **$A300**: can't continue
- **$A30E**: undef'd function
- **$A31E**: verify
- **$A324**: load

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A19E**: 1 too many files
- **$A1A8**: 2 file open
- **$A1B0**: 3 file not open
- **$A1C0**: 4 file not found
- **$A1C8**: 5 device not present
- **$A1E0**: 6 not input file
- **$A1F0**: 7 not output file
- **$A200**: 8 missing filename
- **$A210**: 9 illegal device number
- **$A220**: 10 next without for
- **$A230**: 11 syntax
- **$A238**: 12 return without gosub
- **$A248**: 13 out of data
- **$A258**: 14 illegal quantity
- **$A268**: 15 overflow
- **$A270**: 16 out of memory
- **$A278**: 17 undef'd statement
- **$A290**: 18 bad subscript
- **$A298**: 19 redim'd array
- **$A2A8**: 20 division by zero
- **$A2B8**: 21 illegal direct
- **$A2C8**: 22 type mismatch
- **$A2D0**: 23 string too long
- **$A2E0**: 24 file data
- **$A2E8**: 25 formula too complex
- **$A300**: 26 can't continue
- **$A308**: 27 undef'd function
- **$A318**: 28 verify
- **$A320**: 29 load
- **$A364**: OK
- **$A368**: ERROR
- **$A370**: IN
- **$A378**: READY.
- **$A380**: BREAK

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*