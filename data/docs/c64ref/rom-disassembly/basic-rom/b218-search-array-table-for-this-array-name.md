---
title: SEARCH ARRAY TABLE FOR THIS ARRAY NAME
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
- 005f-lowtr
- b218-search-array-table-for-this-array-name
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $B218
  address_end: $B243
  symbol: search-array-table-for-this-array-name
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B218**: (A,X) = START OF ARRAY TABLE'
---

# $B218 — SEARCH ARRAY TABLE FOR THIS ARRAY NAME

## Disassemblatura
```assembly
.B218  A6 2F    LDX $2F   ; (A,X) = START OF ARRAY TABLE
.B21A  A5 30    LDA $30
.B21C  86 5F    STX $5F   ; USE LOWTR FOR RUNNING POINTER
.B21E  85 60    STA $60
.B220  C5 32    CMP $32   ; DID WE REACH THE END OF ARRAYS YET?
.B222  D0 04    BNE $B228   ; NO, KEEP SEARCHING
.B224  E4 31    CPX $31
.B226  F0 39    BEQ $B261   ; YES, THIS IS A NEW ARRAY NAME
.B228  A0 00    LDY #$00   ; POINT AT 1ST CHAR OF ARRAY NAME
.B22A  B1 5F    LDA ($5F),Y   ; GET 1ST CHAR OF NAME
.B22C  C8       INY   ; POINT AT 2ND CHAR
.B22D  C5 45    CMP $45   ; 1ST CHAR SAME?
.B22F  D0 06    BNE $B237   ; NO, MOVE TO NEXT ARRAY
.B231  A5 46    LDA $46   ; YES, TRY 2ND CHAR
.B233  D1 5F    CMP ($5F),Y   ; SAME?
.B235  F0 16    BEQ $B24D   ; YES, ARRAY FOUND
.B237  C8       INY   ; POINT AT OFFSET TO NEXT ARRAY
.B238  B1 5F    LDA ($5F),Y   ; ADD OFFSET TO RUNNING POINTER
.B23A  18       CLC
.B23B  65 5F    ADC $5F
.B23D  AA       TAX
.B23E  C8       INY
.B23F  B1 5F    LDA ($5F),Y
.B241  65 60    ADC $60
.B243  90 D7    BCC $B21C   ; ...ALWAYS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B218**: (A,X) = START OF ARRAY TABLE
- **$B21C**: USE LOWTR FOR RUNNING POINTER
- **$B220**: DID WE REACH THE END OF ARRAYS YET?
- **$B222**: NO, KEEP SEARCHING
- **$B226**: YES, THIS IS A NEW ARRAY NAME
- **$B228**: POINT AT 1ST CHAR OF ARRAY NAME
- **$B22A**: GET 1ST CHAR OF NAME
- **$B22C**: POINT AT 2ND CHAR
- **$B22D**: 1ST CHAR SAME?
- **$B22F**: NO, MOVE TO NEXT ARRAY
- **$B231**: YES, TRY 2ND CHAR
- **$B233**: SAME?
- **$B235**: YES, ARRAY FOUND
- **$B237**: POINT AT OFFSET TO NEXT ARRAY
- **$B238**: ADD OFFSET TO RUNNING POINTER
- **$B243**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*