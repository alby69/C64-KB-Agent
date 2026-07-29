---
title: search the stack for FOR or GOSUB activity
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
- a38a-for-next-und-gosub-befehl
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A38A
  address_end: $A3B7
  symbol: search-the-stack-for-for-or-gosub-activity
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A38A**: copy stack pointer'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A38A**: Stapelzeiger in X-Register'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A392**: for block code'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A38F**: "FOR" FRAME HERE?'
---

# $A38A — search the stack for FOR or GOSUB activity

## Disassemblatura
```assembly
.A38A  BA       TSX   ; copy stack pointer
.A38B  E8       INX   ; +1 pass return address
.A38C  E8       INX   ; +2 pass return address
.A38D  E8       INX   ; +3 pass calling routine return address
.A38E  E8       INX   ; +4 pass calling routine return address
.A38F  BD 01 01 LDA $0101,X   ; get the token byte from the stack
.A392  C9 81    CMP #$81   ; is it the FOR token
.A394  D0 21    BNE $A3B7   ; if not FOR token just exit it was the FOR token
.A396  A5 4A    LDA $4A   ; get FOR/NEXT variable pointer high byte
.A398  D0 0A    BNE $A3A4   ; branch if not null
.A39A  BD 02 01 LDA $0102,X   ; get FOR variable pointer low byte
.A39D  85 49    STA $49   ; save FOR/NEXT variable pointer low byte
.A39F  BD 03 01 LDA $0103,X   ; get FOR variable pointer high byte
.A3A2  85 4A    STA $4A   ; save FOR/NEXT variable pointer high byte
.A3A4  DD 03 01 CMP $0103,X   ; compare variable pointer with stacked variable pointer high byte
.A3A7  D0 07    BNE $A3B0   ; branch if no match
.A3A9  A5 49    LDA $49   ; get FOR/NEXT variable pointer low byte
.A3AB  DD 02 01 CMP $0102,X   ; compare variable pointer with stacked variable pointer low byte
.A3AE  F0 07    BEQ $A3B7   ; exit if match found
.A3B0  8A       TXA   ; copy index
.A3B1  18       CLC   ; clear carry for add
.A3B2  69 12    ADC #$12   ; add FOR stack use size
.A3B4  AA       TAX   ; copy back to index
.A3B5  D0 D8    BNE $A38F   ; loop if not at start of stack
.A3B7  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A38A**: copy stack pointer
- **$A38B**: +1 pass return address
- **$A38C**: +2 pass return address
- **$A38D**: +3 pass calling routine return address
- **$A38E**: +4 pass calling routine return address
- **$A38F**: get the token byte from the stack
- **$A392**: is it the FOR token
- **$A394**: if not FOR token just exit it was the FOR token
- **$A396**: get FOR/NEXT variable pointer high byte
- **$A398**: branch if not null
- **$A39A**: get FOR variable pointer low byte
- **$A39D**: save FOR/NEXT variable pointer low byte
- **$A39F**: get FOR variable pointer high byte
- **$A3A2**: save FOR/NEXT variable pointer high byte
- **$A3A4**: compare variable pointer with stacked variable pointer high byte
- **$A3A7**: branch if no match
- **$A3A9**: get FOR/NEXT variable pointer low byte
- **$A3AB**: compare variable pointer with stacked variable pointer low byte
- **$A3AE**: exit if match found
- **$A3B0**: copy index
- **$A3B1**: clear carry for add
- **$A3B2**: add FOR stack use size
- **$A3B4**: copy back to index
- **$A3B5**: loop if not at start of stack

### Commodore-64-intern-Buch (Commodore)
- **$A38A**: Stapelzeiger in X-Register
- **$A38B**: 4 mal erhöhen
- **$A38C**: (nächsten zwei Rücksprung-
- **$A38D**: adressen, Interpreter und
- **$A38E**: Routine, übergehen)
- **$A38F**: nächstes Byte hoten
- **$A392**: Ist es FOR-Code ?
- **$A394**: Nein: dann RTS
- **$A396**: Variablenzeiger holen
- **$A398**: keine Variable (NEXT):$A3A4
- **$A39A**: Variablenzeiger aus
- **$A39D**: Stapel nach $49/4A
- **$A39F**: (Variablenzeiger)
- **$A3A2**: holen
- **$A3A4**: Mit Zeiger im Stapel vergl.
- **$A3A7**: Ungleich: nächste Schleife
- **$A3A9**: Zeiger wieder holen
- **$A3AB**: Mit Zeiger im Stapel vergl.
- **$A3AE**: Gleich: Schleife gefunden,RTS
- **$A3B0**: Suchzeiger in Akku
- **$A3B1**: Carry für Addition löschen
- **$A3B2**: Suchzeiger um 18 erhöhen
- **$A3B4**: und wieder zurück ins X-Rg.
- **$A3B5**: nächste Schleife prüfen
- **$A3B7**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$A392**: for block code

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A38F**: "FOR" FRAME HERE?
- **$A394**: NO
- **$A396**: YES -- "NEXT" WITH NO VARIABLE?
- **$A398**: NO, VARIABLE SPECIFIED
- **$A39A**: YES, SO USE THIS FRAME
- **$A3A4**: IS VARIABLE IN THIS FRAME?
- **$A3A7**: NO
- **$A3A9**: LOOK AT 2ND BYTE TOO
- **$A3AB**: SAME VARIABLE?
- **$A3AE**: YES
- **$A3B0**: NO, SO TRY NEXT FRAME (IF ANY)
- **$A3B1**: 18 BYTES PER FRAME
- **$A3B5**: ...ALWAYS?

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*