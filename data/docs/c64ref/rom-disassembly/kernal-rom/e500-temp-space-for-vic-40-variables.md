---
title: ; TEMP SPACE FOR VIC-40 VARIABLES *
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0022-index
- 0055-size
- 00b1-temp
- 00cc-blnsw
- 00cd-blnct
- 00cf-blnon
- 00d1-pnt
- 00d3-pntr
- 00d5-lnmx
- 00d6-tblx
- 00d9-ldtb1
- 0286-color
- 0288-hibase
- 0289-xmax
- 028b-kount
- 028c-delay
- 028f-keylog
- 0291-mode
- adc
- bcc
- bcs
- bmi
- bne
- bpl
- cint
- clc
- clear
- cpx
- cursor
- dex
- e500-basis-adresse-des-cias-holen
- e505-spalten
- e50a-c1
- e518-bildschirm-reset
- e544-bildschirm-lschen
- e566-cursor-home
- e56c-bildschirmzeiger-setzen
- inx
- iny
- iobase
- jmp
- jsr
- lda
- ldx
- ldy
- memory
- ora
- plot
- return
- rts
- screen
- sta
- stx
- sty
- tax
- tay
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E500
  address_end: $E58E
  symbol: temp-space-for-vic-40-variables
  sources:
  - name: Original Disassembly
    author: Commodore
    description: '- **$E500**: IOBASE LDX #<D1PRA'
  - name: Original Disassembly
    author: —
    description: '- **$E500**: get the I/O base address low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E500**: Adresse'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E500**: low  DC00'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E500**: set (X/Y) to $dc00'
---

# $E500 — ; TEMP SPACE FOR VIC-40 VARIABLES *

## Disassemblatura
```assembly
.E500  A2 00    LDX #$00   ; IOBASE LDX #<D1PRA
.E502  A0 DC    LDY #$DC   ; LDY    #>D1PRA
.E504  60       RTS   ; RTS ; ;RETURN MAX ROWS,COLS OF SCREEN ;
.E505  A2 28    LDX #$28   ; SCRORG LDX #LLEN
.E507  A0 19    LDY #$19   ; LDY    #NLINES
.E509  60       RTS   ; RTS ; ;READ/PLOT CURSOR POSITION ;
.E50A  B0 07    BCS $E513   ; PLOT   BCS PLOT10
.E50C  86 D6    STX $D6   ; STX    TBLX
.E50E  84 D3    STY $D3   ; STY    PNTR
.E510  20 6C E5 JSR $E56C   ; JSR    STUPT
.E513  A6 D6    LDX $D6   ; PLOT10 LDX TBLX
.E515  A4 D3    LDY $D3   ; LDY    PNTR
.E517  60       RTS   ; RTS ;INITIALIZE I/O ; CINT ; ; ESTABLISH SCREEN MEMORY ;
.E518  20 A0 E5 JSR $E5A0   ; JSR PANIC       ;SET UP VIC ;
.E51B  A9 00    LDA #$00   ; LDA #0          ;MAKE SURE WE'RE IN PET MODE
.E51D  8D 91 02 STA $0291   ; STA MODE
.E520  85 CF    STA $CF   ; STA BLNON       ;WE DONT HAVE A GOOD CHAR FROM THE SCREEN YET
.E522  A9 48    LDA #$48   ; LDA #<SHFLOG    ;SET SHIFT LOGIC INDIRECTS
.E524  8D 8F 02 STA $028F   ; STA KEYLOG
.E527  A9 EB    LDA #$EB   ; LDA #>SHFLOG
.E529  8D 90 02 STA $0290   ; STA KEYLOG+1
.E52C  A9 0A    LDA #$0A   ; LDA #10
.E52E  8D 89 02 STA $0289   ; STA XMAX        ;MAXIMUM TYPE AHEAD BUFFER SIZE
.E531  8D 8C 02 STA $028C   ; STA DELAY
.E534  A9 0E    LDA #$0E   ; LDA #$E         ;INIT COLOR TO LIGHT BLUE<<<<<<<<<<
.E536  8D 86 02 STA $0286   ; STA COLOR
.E539  A9 04    LDA #$04   ; LDA #4
.E53B  8D 8B 02 STA $028B   ; STA KOUNT       ;DELAY BETWEEN KEY REPEATS
.E53E  A9 0C    LDA #$0C   ; LDA #$C
.E540  85 CD    STA $CD   ; STA BLNCT
.E542  85 CC    STA $CC   ; STA BLNSW
.E544  AD 88 02 LDA $0288   ; CLSR LDA HIBASE ;FILL HI BYTE PTR TABLE
.E547  09 80    ORA #$80   ; ORA #$80
.E549  A8       TAY   ; TAY
.E54A  A9 00    LDA #$00   ; LDA #0
.E54C  AA       TAX   ; TAX
.E54D  94 D9    STY $D9,X   ; LPS1 STY LDTB1,X
.E54F  18       CLC   ; CLC
.E550  69 28    ADC #$28   ; ADC #LLEN
.E552  90 01    BCC $E555   ; BCC LPS2
.E554  C8       INY   ; INY             ;CARRY BUMP HI BYTE
.E555  E8       INX   ; LPS2 INX
.E556  E0 1A    CPX #$1A   ; CPX #NLINES+1   ;DONE # OF LINES?
.E558  D0 F3    BNE $E54D   ; BNE LPS1        ;NO...
.E55A  A9 FF    LDA #$FF   ; LDA #$FF        ;TAG END OF LINE TABLE
.E55C  95 D9    STA $D9,X   ; STA LDTB1,X
.E55E  A2 18    LDX #$18   ; LDX #NLINES-1   ;CLEAR FROM THE BOTTOM LINE UP
.E560  20 FF E9 JSR $E9FF   ; CLEAR1 JSR CLRLN       ;SEE SCROLL ROUTINES
.E563  CA       DEX   ; DEX
.E564  10 FA    BPL $E560   ; BPL CLEAR1 ;HOME FUNCTION ;
.E566  A0 00    LDY #$00   ; NXTD   LDY #0
.E568  84 D3    STY $D3   ; STY    PNTR            ;LEFT COLUMN
.E56A  84 D6    STY $D6   ; STY    TBLX            ;TOP LINE ; ;MOVE CURSOR TO TBLX,PNTR ; STUPT
.E56C  A6 D6    LDX $D6   ; LDX TBLX        ;GET CURENT LINE INDEX
.E56E  A5 D3    LDA $D3   ; LDA PNTR        ;GET CHARACTER POINTER
.E570  B4 D9    LDY $D9,X   ; FNDSTR LDY LDTB1,X     ;FIND BEGINING OF LINE
.E572  30 08    BMI $E57C   ; BMI STOK        ;BRANCH IF START FOUND
.E574  18       CLC   ; CLC
.E575  69 28    ADC #$28   ; ADC #LLEN       ;ADJUST POINTER
.E577  85 D3    STA $D3   ; STA PNTR
.E579  CA       DEX   ; DEX
.E57A  10 F4    BPL $E570   ; BPL FNDSTR ;
.E57C  20 F0 E9 JSR $E9F0   ; STOK   JSR SETPNT      ;SET UP PNT INDIRECT 901227-03********** ;
.E57F  A9 27    LDA #$27   ; LDA #LLEN-1
.E581  E8       INX   ; INX
.E582  B4 D9    LDY $D9,X   ; FNDEND LDY LDTB1,X
.E584  30 06    BMI $E58C   ; BMI STDONE
.E586  18       CLC   ; CLC
.E587  69 28    ADC #$28   ; ADC #LLEN
.E589  E8       INX   ; INX
.E58A  10 F6    BPL $E582   ; BPL FNDEND STDONE
.E58C  85 D5    STA $D5   ; STA LNMX
.E58E  4C 24 EA JMP $EA24   ; JMP SCOLOR      ;MAKE COLOR POINTER FOLLOW 901227-03**********
```


## Commenti

### Original Disassembly (Commodore)
- **$E500**: IOBASE LDX #<D1PRA
- **$E502**: LDY    #>D1PRA
- **$E504**: RTS ; ;RETURN MAX ROWS,COLS OF SCREEN ;
- **$E505**: SCRORG LDX #LLEN
- **$E507**: LDY    #NLINES
- **$E509**: RTS ; ;READ/PLOT CURSOR POSITION ;
- **$E50A**: PLOT   BCS PLOT10
- **$E50C**: STX    TBLX
- **$E50E**: STY    PNTR
- **$E510**: JSR    STUPT
- **$E513**: PLOT10 LDX TBLX
- **$E515**: LDY    PNTR
- **$E517**: RTS ;INITIALIZE I/O ; CINT ; ; ESTABLISH SCREEN MEMORY ;
- **$E518**: JSR PANIC       ;SET UP VIC ;
- **$E51B**: LDA #0          ;MAKE SURE WE'RE IN PET MODE
- **$E51D**: STA MODE
- **$E520**: STA BLNON       ;WE DONT HAVE A GOOD CHAR FROM THE SCREEN YET
- **$E522**: LDA #<SHFLOG    ;SET SHIFT LOGIC INDIRECTS
- **$E524**: STA KEYLOG
- **$E527**: LDA #>SHFLOG
- **$E529**: STA KEYLOG+1
- **$E52C**: LDA #10
- **$E52E**: STA XMAX        ;MAXIMUM TYPE AHEAD BUFFER SIZE
- **$E531**: STA DELAY
- **$E534**: LDA #$E         ;INIT COLOR TO LIGHT BLUE<<<<<<<<<<
- **$E536**: STA COLOR
- **$E539**: LDA #4
- **$E53B**: STA KOUNT       ;DELAY BETWEEN KEY REPEATS
- **$E53E**: LDA #$C
- **$E540**: STA BLNCT
- **$E542**: STA BLNSW
- **$E544**: CLSR LDA HIBASE ;FILL HI BYTE PTR TABLE
- **$E547**: ORA #$80
- **$E549**: TAY
- **$E54A**: LDA #0
- **$E54C**: TAX
- **$E54D**: LPS1 STY LDTB1,X
- **$E54F**: CLC
- **$E550**: ADC #LLEN
- **$E552**: BCC LPS2
- **$E554**: INY             ;CARRY BUMP HI BYTE
- **$E555**: LPS2 INX
- **$E556**: CPX #NLINES+1   ;DONE # OF LINES?
- **$E558**: BNE LPS1        ;NO...
- **$E55A**: LDA #$FF        ;TAG END OF LINE TABLE
- **$E55C**: STA LDTB1,X
- **$E55E**: LDX #NLINES-1   ;CLEAR FROM THE BOTTOM LINE UP
- **$E560**: CLEAR1 JSR CLRLN       ;SEE SCROLL ROUTINES
- **$E563**: DEX
- **$E564**: BPL CLEAR1 ;HOME FUNCTION ;
- **$E566**: NXTD   LDY #0
- **$E568**: STY    PNTR            ;LEFT COLUMN
- **$E56A**: STY    TBLX            ;TOP LINE ; ;MOVE CURSOR TO TBLX,PNTR ; STUPT
- **$E56C**: LDX TBLX        ;GET CURENT LINE INDEX
- **$E56E**: LDA PNTR        ;GET CHARACTER POINTER
- **$E570**: FNDSTR LDY LDTB1,X     ;FIND BEGINING OF LINE
- **$E572**: BMI STOK        ;BRANCH IF START FOUND
- **$E574**: CLC
- **$E575**: ADC #LLEN       ;ADJUST POINTER
- **$E577**: STA PNTR
- **$E579**: DEX
- **$E57A**: BPL FNDSTR ;
- **$E57C**: STOK   JSR SETPNT      ;SET UP PNT INDIRECT 901227-03********** ;
- **$E57F**: LDA #LLEN-1
- **$E581**: INX
- **$E582**: FNDEND LDY LDTB1,X
- **$E584**: BMI STDONE
- **$E586**: CLC
- **$E587**: ADC #LLEN
- **$E589**: INX
- **$E58A**: BPL FNDEND STDONE
- **$E58C**: STA LNMX
- **$E58E**: JMP SCOLOR      ;MAKE COLOR POINTER FOLLOW 901227-03**********

### Original Disassembly (—)
- **$E500**: get the I/O base address low byte
- **$E502**: get the I/O base address high byte

### Commodore-64-intern-Buch (Commodore)
- **$E500**: Adresse
- **$E502**: $DC00
- **$E504**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E500**: low  DC00
- **$E502**: high DC00

### Magnus Nyman (Magnus Nyman)
- **$E500**: set (X/Y) to $dc00

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*