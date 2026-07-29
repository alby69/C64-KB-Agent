---
title: get value from line continued
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
- afa7-funktionsberechnung
- afb1-ersten-parameter
- afd1-numerische-funktion-auswerten
- rts
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AFA7
  address_end: $AFE3
  symbol: get-value-from-line-continued
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AFA7**: *2 (2 bytes per function address)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AFA7**: Funktionscode mal 2'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AFA7**: DOUBLE TOKEN TO GET INDEX'
---

# $AFA7 — get value from line continued

## Disassemblatura
```assembly
.AFA7  0A       ASL   ; *2 (2 bytes per function address)
.AFA8  48       PHA   ; save function offset
.AFA9  AA       TAX   ; copy function offset
.AFAA  20 73 00 JSR $0073   ; increment and scan memory
.AFAD  E0 8F    CPX #$8F   ; compare function offset to CHR$ token offset+1
.AFAF  90 20    BCC $AFD1   ; branch if < LEFT$ (can not be =) get value from line .. continued was LEFT$, RIGHT$ or MID$ so..
.AFB1  20 FA AE JSR $AEFA   ; scan for "(", else do syntax error then warm start
.AFB4  20 9E AD JSR $AD9E   ; evaluate, should be string, expression
.AFB7  20 FD AE JSR $AEFD   ; scan for ",", else do syntax error then warm start
.AFBA  20 8F AD JSR $AD8F   ; check if source is string, else do type mismatch
.AFBD  68       PLA   ; restore function offset
.AFBE  AA       TAX   ; copy it
.AFBF  A5 65    LDA $65   ; get descriptor pointer high byte
.AFC1  48       PHA   ; push string pointer high byte
.AFC2  A5 64    LDA $64   ; get descriptor pointer low byte
.AFC4  48       PHA   ; push string pointer low byte
.AFC5  8A       TXA   ; restore function offset
.AFC6  48       PHA   ; save function offset
.AFC7  20 9E B7 JSR $B79E   ; get byte parameter
.AFCA  68       PLA   ; restore function offset
.AFCB  A8       TAY   ; copy function offset
.AFCC  8A       TXA   ; copy byte parameter to A
.AFCD  48       PHA   ; push byte parameter
.AFCE  4C D6 AF JMP $AFD6   ; go call function get value from line .. continued was SGN() to CHR$() so..
.AFD1  20 F1 AE JSR $AEF1   ; evaluate expression within parentheses
.AFD4  68       PLA   ; restore function offset
.AFD5  A8       TAY   ; copy to index
.AFD6  B9 EA 9F LDA $9FEA,Y   ; get function jump vector low byte
.AFD9  85 55    STA $55   ; save functions jump vector low byte
.AFDB  B9 EB 9F LDA $9FEB,Y   ; get function jump vector high byte
.AFDE  85 56    STA $56   ; save functions jump vector high byte
.AFE0  20 54 00 JSR $0054   ; do function call
.AFE3  4C 8D AD JMP $AD8D   ; check if source is numeric and RTS, else do type mismatch string functions avoid this by dumping the return address
```


## Commenti

### Original Disassembly (—)
- **$AFA7**: *2 (2 bytes per function address)
- **$AFA8**: save function offset
- **$AFA9**: copy function offset
- **$AFAA**: increment and scan memory
- **$AFAD**: compare function offset to CHR$ token offset+1
- **$AFAF**: branch if < LEFT$ (can not be =) get value from line .. continued was LEFT$, RIGHT$ or MID$ so..
- **$AFB1**: scan for "(", else do syntax error then warm start
- **$AFB4**: evaluate, should be string, expression
- **$AFB7**: scan for ",", else do syntax error then warm start
- **$AFBA**: check if source is string, else do type mismatch
- **$AFBD**: restore function offset
- **$AFBE**: copy it
- **$AFBF**: get descriptor pointer high byte
- **$AFC1**: push string pointer high byte
- **$AFC2**: get descriptor pointer low byte
- **$AFC4**: push string pointer low byte
- **$AFC5**: restore function offset
- **$AFC6**: save function offset
- **$AFC7**: get byte parameter
- **$AFCA**: restore function offset
- **$AFCB**: copy function offset
- **$AFCC**: copy byte parameter to A
- **$AFCD**: push byte parameter
- **$AFCE**: go call function get value from line .. continued was SGN() to CHR$() so..
- **$AFD1**: evaluate expression within parentheses
- **$AFD4**: restore function offset
- **$AFD5**: copy to index
- **$AFD6**: get function jump vector low byte
- **$AFD9**: save functions jump vector low byte
- **$AFDB**: get function jump vector high byte
- **$AFDE**: save functions jump vector high byte
- **$AFE0**: do function call
- **$AFE3**: check if source is numeric and RTS, else do type mismatch string functions avoid this by dumping the return address

### Commodore-64-intern-Buch (Commodore)
- **$AFA7**: Funktionscode mal 2
- **$AFA8**: auf den Stapel retten
- **$AFA9**: und ins X-Register
- **$AFAA**: CHRGET nächstes Zeichen
- **$AFAD**: numerische Funktion?
- **$AFAF**: ja: $AFD1

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AFA7**: DOUBLE TOKEN TO GET INDEX
- **$AFAD**: LEFT$, RIGHT$, AND MID$
- **$AFAF**: NOT ONE OF THE STRING FUNCTIONS
- **$AFB1**: STRING FUNCTION, NEED "("
- **$AFB4**: EVALUATE EXPRESSION FOR STRING
- **$AFB7**: REQUIRE A COMMA
- **$AFBA**: MAKE SURE EXPRESSION IS A STRING
- **$AFBE**: RETRIEVE ROUTINE POINTER
- **$AFBF**: STACK ADDRESS OF STRING
- **$AFC6**: STACK DOUBLED TOKEN
- **$AFC7**: CONVERT NEXT EXPRESSION TO BYTE IN X-REG
- **$AFCA**: GET DOUBLED TOKEN OFF STACK
- **$AFCB**: USE AS INDEX TO BRANCH
- **$AFCC**: VALUE OF SECOND PARAMETER
- **$AFCD**: PUSH 2ND PARAM
- **$AFCE**: JOIN UNARY FUNCTIONS
- **$AFD1**: REQUIRE "(EXPRESSION)"
- **$AFD5**: INDEX INTO FUNCTION ADDRESS TABLE
- **$AFD9**: PREPARE TO JSR TO ADDRESS
- **$AFE0**: DOES NOT RETURN FOR CHR$, LEFT$, RIGHT$, OR MID$
- **$AFE3**: REQUIRE NUMERIC RESULT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*