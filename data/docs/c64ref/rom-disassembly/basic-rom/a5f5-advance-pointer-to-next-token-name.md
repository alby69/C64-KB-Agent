---
title: ADVANCE POINTER TO NEXT TOKEN NAME
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
- 007a-txtptr
- a5f5-advance-pointer-to-next-token-name
- input
- store
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $A5F5
  address_end: $A612
  symbol: advance-pointer-to-next-token-name
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A5F5**: GET POINTER TO INPUT LINE IN X-REG'
---

# $A5F5 — ADVANCE POINTER TO NEXT TOKEN NAME

## Disassemblatura
```assembly
.A5F5  A6 7A    LDX $7A   ; GET POINTER TO INPUT LINE IN X-REG
.A5F7  E6 0B    INC $0B   ; BUMP (TOKEN # - $80)
.A5F9  C8       INY   ; NEXT TOKEN ONE BEYOND THAT
.A5FA  B9 9D A0 LDA $A09D,Y   ; YES, AT NEXT NAME.  END OF TABLE?
.A5FD  10 FA    BPL $A5F9
.A5FF  B9 9E A0 LDA $A09E,Y
.A602  D0 B4    BNE $A5B8   ; NO, NOT END OF TABLE
.A604  BD 00 02 LDA $0200,X   ; YES, SO NOT A KEYWORD
.A607  10 BE    BPL $A5C7   ; ...ALWAYS, COPY CHAR AS IS END OF LINE
.A609  99 FD 01 STA $01FD,Y   ; STORE ANOTHER 00 ON END
.A60C  C6 7B    DEC $7B   ; SET TXTPTR = INPUT.BUFFER-1
.A60E  A9 FF    LDA #$FF
.A610  85 7A    STA $7A
.A612  60       RTS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A5F5**: GET POINTER TO INPUT LINE IN X-REG
- **$A5F7**: BUMP (TOKEN # - $80)
- **$A5F9**: NEXT TOKEN ONE BEYOND THAT
- **$A5FA**: YES, AT NEXT NAME.  END OF TABLE?
- **$A602**: NO, NOT END OF TABLE
- **$A604**: YES, SO NOT A KEYWORD
- **$A607**: ...ALWAYS, COPY CHAR AS IS END OF LINE
- **$A609**: STORE ANOTHER 00 ON END
- **$A60C**: SET TXTPTR = INPUT.BUFFER-1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*