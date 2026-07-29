---
title: ; THIS IS A PATCH FOR INPUT LOGIC 901227-03*
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0001-r6510
- 0022-index
- 0068-bits
- 0090-status
- 0099-dfltn
- 009a-dflto
- 00a0-time
- 00ac-sal
- 00ad-sah
- 00ae-eal
- 00af-eah
- 00c0-cas1
- 00c6-ndx
- 00c7-rvs
- 00c8-indx
- 00c9-lsxp
- 00ca-lstp
- 00cc-blnsw
- 00cd-blnct
- 00ce-gdbln
- 00cf-blnon
- 00d0-crsw
- 00d1-pnt
- 00d3-pntr
- 00d4-qtsw
- 00d5-lnmx
- 00d6-tblx
- 00d7-data
- 00d8-insrt
- 00d9-ldtb1
- 00f3-user
- 0277-keyd
- 0286-color
- 0287-gdcol
- 0288-hibase
- 028c-delay
- 0292-autodn
- 02a5-lintmp
- ab45-print
- adc
- asl
- b983-registers
- bcc
- bcs
- beq
- bit
- bmi
- bne
- bpl
- bvs
- check
- clc
- clear
- cli
- cmp
- cpx
- cpy
- cursor
- dec
- dex
- dey
- e591-this-is-a-patch-for-input-logic-901227-03
- e599-orphan-bytes
- e59a-set-io-defaults
- e5a0-initialisieren
- e5b4-holen
- e5ca-tastatureingabe
- e5cd-wait-for-a-key-from-the-keyboard
- e632-holen
- e63a-get-character-from-current-screen-line
- e684-auf-hochkomma-testen
- e691-ausgeben
- e6a8-return-from-output-to-the-screen
- e6b6-neu-berechnen
- e6ed-retreat-cursor
- e701-zeile
- e716-ausgabe-auf-bildschirm
- e7d4-zeichen-grer-127
- e87c-go-to-next-line
- e891-output-carriage-return
- e8a1-check-line-decrement
- e8b3-check-line-increment
- e8cb-prft-auf-farbcodes
- e8da-tabelle-der-farb-kodes
- e8ea-bildschirm-scrollen
- e965-fortsetzungszeile
- e9c8-zeile-nach-oben-schieben
- e9e0-scrollzeile-berechnen
- e9f0-zeile-x
- e9ff-bildschirmzeile-x-lschen
- ea12-orphan-byte
- ea13-print-to-screen
- ea1c-bildschirm-setzen
- ea24-zeiger-auf-farb-ram-berechnen
- ea31-interrupt-routine
- ece7-load
- ecec-run
- eor
- f5ed-save
- fce2-reset
- ffea-increment-real-time-clock
- inc
- input
- inx
- iny
- jmp
- jsr
- lda
- ldx
- ldy
- lsr
- nop
- ora
- pha
- php
- pla
- plp
- return
- rti
- rts
- sbc
- scnkey
- screen
- sec
- sei
- setup
- sta
- stop
- store
- stx
- sty
- tax
- tay
- txa
- tya
- update
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $E591
  address_end: $EA86
  symbol: this-is-a-patch-for-input-logic-901227-03
  sources:
  - name: Original Disassembly
    author: Commodore
    description: '- **$E591**: FINPUT CPX LSXP        ;CHECK IF ON SAME LINE'
---

# $E591 — ; THIS IS A PATCH FOR INPUT LOGIC 901227-03*

## Disassemblatura
```assembly
.E591  E4 C9    CPX $C9   ; FINPUT CPX LSXP        ;CHECK IF ON SAME LINE
.E593  F0 03    BEQ $E598   ; BEQ FINPUX      ;YES..RETURN TO SEND
.E595  4C ED E6 JMP $E6ED   ; JMP FINDST      ;CHECK IF WE WRAPPED DOWN...
.E598  60       RTS   ; FINPUX RTS
.E599  EA       NOP   ; NOP             ;KEEP THE SPACE THE SAME... ;PANIC NMI ENTRY ;
.E59A  20 A0 E5 JSR $E5A0   ; VPAN   JSR PANIC       ;FIX VIC SCREEN
.E59D  4C 66 E5 JMP $E566   ; JMP    NXTD            ;HOME CURSOR
.E5A0  A9 03    LDA #$03   ; PANIC  LDA #3          ;RESET DEFAULT I/O
.E5A2  85 9A    STA $9A   ; STA    DFLTO
.E5A4  A9 00    LDA #$00   ; LDA    #0
.E5A6  85 99    STA $99   ; STA    DFLTN ;INIT VIC ;
.E5A8  A2 2F    LDX #$2F   ; INITV  LDX #47         ;LOAD ALL VIC REGS ***
.E5AA  BD B8 EC LDA $ECB8,X   ; PX4    LDA TVIC-1,X
.E5AD  9D FF CF STA $CFFF,X   ; STA VICREG-1,X
.E5B0  CA       DEX   ; DEX
.E5B1  D0 F7    BNE $E5AA   ; BNE    PX4
.E5B3  60       RTS   ; RTS ; ;REMOVE CHARACTER FROM QUEUE ;
.E5B4  AC 77 02 LDY $0277   ; LP2    LDY KEYD
.E5B7  A2 00    LDX #$00   ; LDX    #0
.E5B9  BD 78 02 LDA $0278,X   ; LP1    LDA KEYD+1,X
.E5BC  9D 77 02 STA $0277,X   ; STA    KEYD,X
.E5BF  E8       INX   ; INX
.E5C0  E4 C6    CPX $C6   ; CPX    NDX
.E5C2  D0 F5    BNE $E5B9   ; BNE    LP1
.E5C4  C6 C6    DEC $C6   ; DEC    NDX
.E5C6  98       TYA   ; TYA
.E5C7  58       CLI   ; CLI
.E5C8  18       CLC   ; CLC                    ;GOOD RETURN
.E5C9  60       RTS   ; RTS ;
.E5CA  20 16 E7 JSR $E716   ; LOOP4  JSR PRT LOOP3
.E5CD  A5 C6    LDA $C6   ; LDA    NDX
.E5CF  85 CC    STA $CC   ; STA    BLNSW
.E5D1  8D 92 02 STA $0292   ; STA    AUTODN          ;TURN ON AUTO SCROLL DOWN
.E5D4  F0 F7    BEQ $E5CD   ; BEQ    LOOP3
.E5D6  78       SEI   ; SEI
.E5D7  A5 CF    LDA $CF   ; LDA    BLNON
.E5D9  F0 0C    BEQ $E5E7   ; BEQ    LP21
.E5DB  A5 CE    LDA $CE   ; LDA    GDBLN
.E5DD  AE 87 02 LDX $0287   ; LDX    GDCOL           ;RESTORE ORIGINAL COLOR
.E5E0  A0 00    LDY #$00   ; LDY    #0
.E5E2  84 CF    STY $CF   ; STY    BLNON
.E5E4  20 13 EA JSR $EA13   ; JSR    DSPP
.E5E7  20 B4 E5 JSR $E5B4   ; LP21   JSR LP2
.E5EA  C9 83    CMP #$83   ; CMP    #$83            ;RUN KEY?
.E5EC  D0 10    BNE $E5FE   ; BNE LP22
.E5EE  A2 09    LDX #$09   ; LDX #9
.E5F0  78       SEI   ; SEI
.E5F1  86 C6    STX $C6   ; STX NDX
.E5F3  BD E6 EC LDA $ECE6,X   ; LP23   LDA RUNTB-1,X
.E5F6  9D 76 02 STA $0276,X   ; STA KEYD-1,X
.E5F9  CA       DEX   ; DEX
.E5FA  D0 F7    BNE $E5F3   ; BNE LP23
.E5FC  F0 CF    BEQ $E5CD   ; BEQ LOOP3
.E5FE  C9 0D    CMP #$0D   ; LP22   CMP #$D
.E600  D0 C8    BNE $E5CA   ; BNE    LOOP4
.E602  A4 D5    LDY $D5   ; LDY    LNMX
.E604  84 D0    STY $D0   ; STY    CRSW
.E606  B1 D1    LDA ($D1),Y   ; CLP5   LDA (PNT)Y
.E608  C9 20    CMP #$20   ; CMP    #'
.E60A  D0 03    BNE $E60F   ; BNE    CLP6
.E60C  88       DEY   ; DEY
.E60D  D0 F7    BNE $E606   ; BNE    CLP5
.E60F  C8       INY   ; CLP6   INY
.E610  84 C8    STY $C8   ; STY    INDX
.E612  A0 00    LDY #$00   ; LDY    #0
.E614  8C 92 02 STY $0292   ; STY AUTODN      ;TURN OFF AUTO SCROLL DOWN
.E617  84 D3    STY $D3   ; STY    PNTR
.E619  84 D4    STY $D4   ; STY    QTSW
.E61B  A5 C9    LDA $C9   ; LDA    LSXP
.E61D  30 1B    BMI $E63A   ; BMI    LOP5
.E61F  A6 D6    LDX $D6   ; LDX TBLX
.E621  20 ED E6 JSR $E6ED   ; JSR FINDST      ;FIND 1ST PHYSICAL LINE
.E624  E4 C9    CPX $C9   ; CPX LSXP
.E626  D0 12    BNE $E63A   ; BNE    LOP5
.E628  A5 CA    LDA $CA   ; LDA    LSTP
.E62A  85 D3    STA $D3   ; STA    PNTR
.E62C  C5 C8    CMP $C8   ; CMP    INDX
.E62E  90 0A    BCC $E63A   ; BCC    LOP5
.E630  B0 2B    BCS $E65D   ; BCS    CLP2 ;INPUT A LINE UNTIL CARRIAGE RETURN ;
.E632  98       TYA   ; LOOP5  TYA
.E633  48       PHA   ; PHA
.E634  8A       TXA   ; TXA
.E635  48       PHA   ; PHA
.E636  A5 D0    LDA $D0   ; LDA    CRSW
.E638  F0 93    BEQ $E5CD   ; BEQ    LOOP3
.E63A  A4 D3    LDY $D3   ; LOP5   LDY PNTR
.E63C  B1 D1    LDA ($D1),Y   ; LDA    (PNT)Y NOTONE
.E63E  85 D7    STA $D7   ; STA    DATA
.E640  29 3F    AND #$3F   ; LOP51  AND #$3F
.E642  06 D7    ASL $D7   ; ASL    DATA
.E644  24 D7    BIT $D7   ; BIT    DATA
.E646  10 02    BPL $E64A   ; BPL    LOP54
.E648  09 80    ORA #$80   ; ORA    #$80
.E64A  90 04    BCC $E650   ; LOP54  BCC LOP52
.E64C  A6 D4    LDX $D4   ; LDX    QTSW
.E64E  D0 04    BNE $E654   ; BNE    LOP53
.E650  70 02    BVS $E654   ; LOP52  BVS LOP53
.E652  09 40    ORA #$40   ; ORA    #$40
.E654  E6 D3    INC $D3   ; LOP53  INC PNTR
.E656  20 84 E6 JSR $E684   ; JSR    QTSWC
.E659  C4 C8    CPY $C8   ; CPY    INDX
.E65B  D0 17    BNE $E674   ; BNE    CLP1
.E65D  A9 00    LDA #$00   ; CLP2   LDA #0
.E65F  85 D0    STA $D0   ; STA    CRSW
.E661  A9 0D    LDA #$0D   ; LDA    #$D
.E663  A6 99    LDX $99   ; LDX    DFLTN           ;FIX GETS FROM SCREEN
.E665  E0 03    CPX #$03   ; CPX    #3              ;IS IT THE SCREEN?
.E667  F0 06    BEQ $E66F   ; BEQ    CLP2A
.E669  A6 9A    LDX $9A   ; LDX    DFLTO
.E66B  E0 03    CPX #$03   ; CPX    #3
.E66D  F0 03    BEQ $E672   ; BEQ    CLP21
.E66F  20 16 E7 JSR $E716   ; CLP2A  JSR PRT
.E672  A9 0D    LDA #$0D   ; CLP21  LDA #$D
.E674  85 D7    STA $D7   ; CLP1   STA DATA
.E676  68       PLA   ; PLA
.E677  AA       TAX   ; TAX
.E678  68       PLA   ; PLA
.E679  A8       TAY   ; TAY
.E67A  A5 D7    LDA $D7   ; LDA    DATA
.E67C  C9 DE    CMP #$DE   ; CMP    #$DE            ;IS IT <PI> ?
.E67E  D0 02    BNE $E682   ; BNE    CLP7
.E680  A9 FF    LDA #$FF   ; LDA    #$FF
.E682  18       CLC   ; CLP7   CLC
.E683  60       RTS   ; RTS
.E684  C9 22    CMP #$22   ; QTSWC  CMP #$22
.E686  D0 08    BNE $E690   ; BNE    QTSWL
.E688  A5 D4    LDA $D4   ; LDA    QTSW
.E68A  49 01    EOR #$01   ; EOR    #$1
.E68C  85 D4    STA $D4   ; STA    QTSW
.E68E  A9 22    LDA #$22   ; LDA    #$22
.E690  60       RTS   ; QTSWL  RTS
.E691  09 40    ORA #$40   ; NXT33  ORA #$40
.E693  A6 C7    LDX $C7   ; NXT3   LDX RVS
.E695  F0 02    BEQ $E699   ; BEQ    NVS
.E697  09 80    ORA #$80   ; NC3    ORA #$80
.E699  A6 D8    LDX $D8   ; NVS    LDX INSRT
.E69B  F0 02    BEQ $E69F   ; BEQ    NVS1
.E69D  C6 D8    DEC $D8   ; DEC    INSRT
.E69F  AE 86 02 LDX $0286   ; NVS1   LDX COLOR PUT COLOR ON SCREEN
.E6A2  20 13 EA JSR $EA13   ; JSR    DSPP
.E6A5  20 B6 E6 JSR $E6B6   ; JSR WLOGIC      ;CHECK FOR WRAPAROUND
.E6A8  68       PLA   ; LOOP2  PLA
.E6A9  A8       TAY   ; TAY
.E6AA  A5 D8    LDA $D8   ; LDA    INSRT
.E6AC  F0 02    BEQ $E6B0   ; BEQ    LOP2
.E6AE  46 D4    LSR $D4   ; LSR    QTSW
.E6B0  68       PLA   ; LOP2   PLA
.E6B1  AA       TAX   ; TAX
.E6B2  68       PLA   ; PLA
.E6B3  18       CLC   ; CLC                    ;GOOD RETURN
.E6B4  58       CLI   ; CLI
.E6B5  60       RTS   ; RTS WLOGIC
.E6B6  20 B3 E8 JSR $E8B3   ; JSR CHKDWN      ;MAYBE WE SHOULD WE INCREMENT TBLX
.E6B9  E6 D3    INC $D3   ; INC PNTR        ;BUMP CHARCTER POINTER
.E6BB  A5 D5    LDA $D5   ; LDA LNMX        ;
.E6BD  C5 D3    CMP $D3   ; CMP PNTR        ;IF LNMX IS LESS THAN PNTR
.E6BF  B0 3F    BCS $E700   ; BCS WLGRTS      ;BRANCH IF LNMX>=PNTR
.E6C1  C9 4F    CMP #$4F   ; CMP #MAXCHR-1   ;PAST MAX CHARACTERS
.E6C3  F0 32    BEQ $E6F7   ; BEQ WLOG10      ;BRANCH IF SO
.E6C5  AD 92 02 LDA $0292   ; LDA AUTODN      ;SHOULD WE AUTO SCROLL DOWN?
.E6C8  F0 03    BEQ $E6CD   ; BEQ WLOG20      ;BRANCH IF NOT
.E6CA  4C 67 E9 JMP $E967   ; JMP    BMT1            ;ELSE DECIDE WHICH WAY TO SCROLL WLOG20
.E6CD  A6 D6    LDX $D6   ; LDX TBLX        ;SEE IF WE SHOULD SCROLL DOWN
.E6CF  E0 19    CPX #$19   ; CPX #NLINES
.E6D1  90 07    BCC $E6DA   ; BCC WLOG30      ;BRANCH IF NOT
.E6D3  20 EA E8 JSR $E8EA   ; JSR SCROL       ;ELSE DO THE SCROL UP
.E6D6  C6 D6    DEC $D6   ; DEC TBLX        ;AND ADJUST CURENT LINE#
.E6D8  A6 D6    LDX $D6   ; LDX TBLX
.E6DA  16 D9    ASL $D9,X   ; WLOG30 ASL LDTB1,X     ;WRAP THE LINE
.E6DC  56 D9    LSR $D9,X   ; LSR LDTB1,X
.E6DE  E8       INX   ; INX             ;INDEX TO NEXT LLINE
.E6DF  B5 D9    LDA $D9,X   ; LDA LDTB1,X     ;GET HIGH ORDER BYTE OF ADDRESS
.E6E1  09 80    ORA #$80   ; ORA #$80        ;MAKE IT A NON-CONTINUATION LINE
.E6E3  95 D9    STA $D9,X   ; STA LDTB1,X     ;AND PUT IT BACK
.E6E5  CA       DEX   ; DEX             ;GET BACK TO CURRENT LINE
.E6E6  A5 D5    LDA $D5   ; LDA LNMX        ;CONTINUE THE BYTES TAKEN OUT
.E6E8  18       CLC   ; CLC
.E6E9  69 28    ADC #$28   ; ADC #LLEN
.E6EB  85 D5    STA $D5   ; STA LNMX FINDST
.E6ED  B5 D9    LDA $D9,X   ; LDA LDTB1,X     ;IS THIS THE FIRST LINE?
.E6EF  30 03    BMI $E6F4   ; BMI FINX        ;BRANCH IF SO
.E6F1  CA       DEX   ; DEX             ;ELSE BACKUP 1
.E6F2  D0 F9    BNE $E6ED   ; BNE FINDST FINX
.E6F4  4C F0 E9 JMP $E9F0   ; JMP SETPNT      ;MAKE SURE PNT IS RIGHT
.E6F7  C6 D6    DEC $D6   ; WLOG10 DEC TBLX
.E6F9  20 7C E8 JSR $E87C   ; JSR NXLN
.E6FC  A9 00    LDA #$00   ; LDA #0
.E6FE  85 D3    STA $D3   ; STA PNTR        ;POINT TO FIRST BYTE
.E700  60       RTS   ; WLGRTS RTS
.E701  A6 D6    LDX $D6   ; BKLN   LDX TBLX
.E703  D0 06    BNE $E70B   ; BNE BKLN1
.E705  86 D3    STX $D3   ; STX PNTR
.E707  68       PLA   ; PLA
.E708  68       PLA   ; PLA
.E709  D0 9D    BNE $E6A8   ; BNE LOOP2 ;
.E70B  CA       DEX   ; BKLN1  DEX
.E70C  86 D6    STX $D6   ; STX TBLX
.E70E  20 6C E5 JSR $E56C   ; JSR STUPT
.E711  A4 D5    LDY $D5   ; LDY LNMX
.E713  84 D3    STY $D3   ; STY PNTR
.E715  60       RTS   ; RTS ;PRINT ROUTINE ;
.E716  48       PHA   ; PRT    PHA
.E717  85 D7    STA $D7   ; STA    DATA
.E719  8A       TXA   ; TXA
.E71A  48       PHA   ; PHA
.E71B  98       TYA   ; TYA
.E71C  48       PHA   ; PHA
.E71D  A9 00    LDA #$00   ; LDA    #0
.E71F  85 D0    STA $D0   ; STA    CRSW
.E721  A4 D3    LDY $D3   ; LDY    PNTR
.E723  A5 D7    LDA $D7   ; LDA    DATA
.E725  10 03    BPL $E72A   ; BPL    *+5
.E727  4C D4 E7 JMP $E7D4   ; JMP    NXTX
.E72A  C9 0D    CMP #$0D   ; CMP    #$D
.E72C  D0 03    BNE $E731   ; BNE    NJT1
.E72E  4C 91 E8 JMP $E891   ; JMP    NXT1
.E731  C9 20    CMP #$20   ; NJT1   CMP #'
.E733  90 10    BCC $E745   ; BCC    NTCN
.E735  C9 60    CMP #$60   ; CMP    #$60            ;LOWER CASE?
.E737  90 04    BCC $E73D   ; BCC    NJT8            ;NO...
.E739  29 DF    AND #$DF   ; AND    #$DF            ;YES...MAKE SCREEN LOWER
.E73B  D0 02    BNE $E73F   ; BNE    NJT9            ;ALWAYS
.E73D  29 3F    AND #$3F   ; NJT8   AND #$3F
.E73F  20 84 E6 JSR $E684   ; NJT9   JSR QTSWC
.E742  4C 93 E6 JMP $E693   ; JMP    NXT3
.E745  A6 D8    LDX $D8   ; NTCN   LDX INSRT
.E747  F0 03    BEQ $E74C   ; BEQ    CNC3X
.E749  4C 97 E6 JMP $E697   ; JMP    NC3
.E74C  C9 14    CMP #$14   ; CNC3X  CMP #$14
.E74E  D0 2E    BNE $E77E   ; BNE    NTCN1
.E750  98       TYA   ; TYA
.E751  D0 06    BNE $E759   ; BNE    BAK1UP
.E753  20 01 E7 JSR $E701   ; JSR BKLN
.E756  4C 73 E7 JMP $E773   ; JMP BK2
.E759  20 A1 E8 JSR $E8A1   ; BAK1UP JSR CHKBAK      ;SHOULD WE DEC TBLX
.E75C  88       DEY   ; DEY
.E75D  84 D3    STY $D3   ; STY    PNTR
.E75F  20 24 EA JSR $EA24   ; BK1    JSR SCOLOR      ;FIX COLOR PTRS
.E762  C8       INY   ; BK15   INY
.E763  B1 D1    LDA ($D1),Y   ; LDA    (PNT)Y
.E765  88       DEY   ; DEY
.E766  91 D1    STA ($D1),Y   ; STA    (PNT)Y
.E768  C8       INY   ; INY
.E769  B1 F3    LDA ($F3),Y   ; LDA    (USER)Y
.E76B  88       DEY   ; DEY
.E76C  91 F3    STA ($F3),Y   ; STA    (USER)Y
.E76E  C8       INY   ; INY
.E76F  C4 D5    CPY $D5   ; CPY    LNMX
.E771  D0 EF    BNE $E762   ; BNE    BK15
.E773  A9 20    LDA #$20   ; BK2    LDA #'
.E775  91 D1    STA ($D1),Y   ; STA    (PNT)Y
.E777  AD 86 02 LDA $0286   ; LDA    COLOR
.E77A  91 F3    STA ($F3),Y   ; STA    (USER)Y
.E77C  10 4D    BPL $E7CB   ; BPL    JPL3
.E77E  A6 D4    LDX $D4   ; NTCN1  LDX QTSW
.E780  F0 03    BEQ $E785   ; BEQ    NC3W
.E782  4C 97 E6 JMP $E697   ; CNC3   JMP NC3
.E785  C9 12    CMP #$12   ; NC3W   CMP #$12
.E787  D0 02    BNE $E78B   ; BNE    NC1
.E789  85 C7    STA $C7   ; STA    RVS
.E78B  C9 13    CMP #$13   ; NC1    CMP #$13
.E78D  D0 03    BNE $E792   ; BNE    NC2
.E78F  20 66 E5 JSR $E566   ; JSR    NXTD
.E792  C9 1D    CMP #$1D   ; NC2    CMP #$1D
.E794  D0 17    BNE $E7AD   ; BNE    NCX2
.E796  C8       INY   ; INY
.E797  20 B3 E8 JSR $E8B3   ; JSR CHKDWN
.E79A  84 D3    STY $D3   ; STY    PNTR
.E79C  88       DEY   ; DEY
.E79D  C4 D5    CPY $D5   ; CPY    LNMX
.E79F  90 09    BCC $E7AA   ; BCC    NCZ2
.E7A1  C6 D6    DEC $D6   ; DEC TBLX
.E7A3  20 7C E8 JSR $E87C   ; JSR    NXLN
.E7A6  A0 00    LDY #$00   ; LDY    #0
.E7A8  84 D3    STY $D3   ; JPL4   STY PNTR
.E7AA  4C A8 E6 JMP $E6A8   ; NCZ2   JMP LOOP2
.E7AD  C9 11    CMP #$11   ; NCX2   CMP #$11
.E7AF  D0 1D    BNE $E7CE   ; BNE    COLR1
.E7B1  18       CLC   ; CLC
.E7B2  98       TYA   ; TYA
.E7B3  69 28    ADC #$28   ; ADC    #LLEN
.E7B5  A8       TAY   ; TAY
.E7B6  E6 D6    INC $D6   ; INC TBLX
.E7B8  C5 D5    CMP $D5   ; CMP    LNMX
.E7BA  90 EC    BCC $E7A8   ; BCC    JPL4
.E7BC  F0 EA    BEQ $E7A8   ; BEQ    JPL4
.E7BE  C6 D6    DEC $D6   ; DEC TBLX
.E7C0  E9 28    SBC #$28   ; CURS10 SBC #LLEN
.E7C2  90 04    BCC $E7C8   ; BCC GOTDWN
.E7C4  85 D3    STA $D3   ; STA PNTR
.E7C6  D0 F8    BNE $E7C0   ; BNE CURS10
.E7C8  20 7C E8 JSR $E87C   ; GOTDWN JSR NXLN
.E7CB  4C A8 E6 JMP $E6A8   ; JPL3   JMP LOOP2
.E7CE  20 CB E8 JSR $E8CB   ; COLR1  JSR CHKCOL      ;CHECK FOR A COLOR
.E7D1  4C 44 EC JMP $EC44   ; JMP LOWER       ;WAS JMP LOOP2 ;CHECK COLOR ; ;SHIFTED KEYS ; NXTX KEEPIT
.E7D4  29 7F    AND #$7F   ; AND    #$7F
.E7D6  C9 7F    CMP #$7F   ; CMP    #$7F
.E7D8  D0 02    BNE $E7DC   ; BNE    NXTX1
.E7DA  A9 5E    LDA #$5E   ; LDA    #$5E NXTX1 NXTXA
.E7DC  C9 20    CMP #$20   ; CMP #$20        ;IS IT A FUNCTION KEY
.E7DE  90 03    BCC $E7E3   ; BCC    UHUH
.E7E0  4C 91 E6 JMP $E691   ; JMP    NXT33 UHUH
.E7E3  C9 0D    CMP #$0D   ; CMP    #$D
.E7E5  D0 03    BNE $E7EA   ; BNE    UP5
.E7E7  4C 91 E8 JMP $E891   ; JMP    NXT1
.E7EA  A6 D4    LDX $D4   ; UP5    LDX  QTSW
.E7EC  D0 3F    BNE $E82D   ; BNE    UP6
.E7EE  C9 14    CMP #$14   ; CMP    #$14
.E7F0  D0 37    BNE $E829   ; BNE    UP9
.E7F2  A4 D5    LDY $D5   ; LDY    LNMX
.E7F4  B1 D1    LDA ($D1),Y   ; LDA    (PNT)Y
.E7F6  C9 20    CMP #$20   ; CMP    #'
.E7F8  D0 04    BNE $E7FE   ; BNE    INS3
.E7FA  C4 D3    CPY $D3   ; CPY    PNTR
.E7FC  D0 07    BNE $E805   ; BNE    INS1
.E7FE  C0 4F    CPY #$4F   ; INS3   CPY #MAXCHR-1
.E800  F0 24    BEQ $E826   ; BEQ    INSEXT          ;EXIT IF LINE TOO LONG
.E802  20 65 E9 JSR $E965   ; JSR    NEWLIN          ;SCROLL DOWN 1
.E805  A4 D5    LDY $D5   ; INS1   LDY LNMX
.E807  20 24 EA JSR $EA24   ; JSR    SCOLOR
.E80A  88       DEY   ; INS2   DEY
.E80B  B1 D1    LDA ($D1),Y   ; LDA    (PNT)Y
.E80D  C8       INY   ; INY
.E80E  91 D1    STA ($D1),Y   ; STA    (PNT)Y
.E810  88       DEY   ; DEY
.E811  B1 F3    LDA ($F3),Y   ; LDA    (USER)Y
.E813  C8       INY   ; INY
.E814  91 F3    STA ($F3),Y   ; STA    (USER)Y
.E816  88       DEY   ; DEY
.E817  C4 D3    CPY $D3   ; CPY    PNTR
.E819  D0 EF    BNE $E80A   ; BNE    INS2
.E81B  A9 20    LDA #$20   ; LDA    #$20
.E81D  91 D1    STA ($D1),Y   ; STA    (PNT)Y
.E81F  AD 86 02 LDA $0286   ; LDA    COLOR
.E822  91 F3    STA ($F3),Y   ; STA    (USER)Y
.E824  E6 D8    INC $D8   ; INC    INSRT
.E826  4C A8 E6 JMP $E6A8   ; INSEXT JMP LOOP2
.E829  A6 D8    LDX $D8   ; UP9    LDX INSRT
.E82B  F0 05    BEQ $E832   ; BEQ    UP2
.E82D  09 40    ORA #$40   ; UP6    ORA #$40
.E82F  4C 97 E6 JMP $E697   ; JMP    NC3
.E832  C9 11    CMP #$11   ; UP2    CMP #$11
.E834  D0 16    BNE $E84C   ; BNE    NXT2
.E836  A6 D6    LDX $D6   ; LDX    TBLX
.E838  F0 37    BEQ $E871   ; BEQ JPL2
.E83A  C6 D6    DEC $D6   ; DEC TBLX
.E83C  A5 D3    LDA $D3   ; LDA PNTR
.E83E  38       SEC   ; SEC
.E83F  E9 28    SBC #$28   ; SBC #LLEN
.E841  90 04    BCC $E847   ; BCC UPALIN
.E843  85 D3    STA $D3   ; STA PNTR
.E845  10 2A    BPL $E871   ; BPL JPL2
.E847  20 6C E5 JSR $E56C   ; UPALIN JSR STUPT
.E84A  D0 25    BNE $E871   ; BNE    JPL2
.E84C  C9 12    CMP #$12   ; NXT2   CMP #$12
.E84E  D0 04    BNE $E854   ; BNE    NXT6
.E850  A9 00    LDA #$00   ; LDA    #0
.E852  85 C7    STA $C7   ; STA    RVS
.E854  C9 1D    CMP #$1D   ; NXT6   CMP #$1D
.E856  D0 12    BNE $E86A   ; BNE    NXT61
.E858  98       TYA   ; TYA
.E859  F0 09    BEQ $E864   ; BEQ    BAKBAK
.E85B  20 A1 E8 JSR $E8A1   ; JSR    CHKBAK
.E85E  88       DEY   ; DEY
.E85F  84 D3    STY $D3   ; STY    PNTR
.E861  4C A8 E6 JMP $E6A8   ; JMP LOOP2
.E864  20 01 E7 JSR $E701   ; BAKBAK JSR BKLN
.E867  4C A8 E6 JMP $E6A8   ; JMP    LOOP2
.E86A  C9 13    CMP #$13   ; NXT61  CMP #$13
.E86C  D0 06    BNE $E874   ; BNE    SCCL
.E86E  20 44 E5 JSR $E544   ; JSR    CLSR
.E871  4C A8 E6 JMP $E6A8   ; JPL2   JMP LOOP2 SCCL
.E874  09 80    ORA #$80   ; ORA    #$80            ;MAKE IT UPPER CASE
.E876  20 CB E8 JSR $E8CB   ; JSR    CHKCOL          ;TRY FOR COLOR
.E879  4C 4F EC JMP $EC4F   ; JMP UPPER       ;WAS JMP LOOP2 ;
.E87C  46 C9    LSR $C9   ; NXLN   LSR LSXP
.E87E  A6 D6    LDX $D6   ; LDX    TBLX
.E880  E8       INX   ; NXLN2  INX
.E881  E0 19    CPX #$19   ; CPX    #NLINES         ;OFF BOTTOM?
.E883  D0 03    BNE $E888   ; BNE    NXLN1           ;NO...
.E885  20 EA E8 JSR $E8EA   ; JSR    SCROL           ;YES...SCROLL
.E888  B5 D9    LDA $D9,X   ; NXLN1  LDA LDTB1,X     ;DOUBLE LINE?
.E88A  10 F4    BPL $E880   ; BPL    NXLN2           ;YES...SCROLL AGAIN
.E88C  86 D6    STX $D6   ; STX    TBLX
.E88E  4C 6C E5 JMP $E56C   ; JMP    STUPT NXT1
.E891  A2 00    LDX #$00   ; LDX    #0
.E893  86 D8    STX $D8   ; STX    INSRT
.E895  86 C7    STX $C7   ; STX    RVS
.E897  86 D4    STX $D4   ; STX    QTSW
.E899  86 D3    STX $D3   ; STX    PNTR
.E89B  20 7C E8 JSR $E87C   ; JSR    NXLN
.E89E  4C A8 E6 JMP $E6A8   ; JPL5   JMP LOOP2 ; ; ; CHECK FOR A DECREMENT TBLX ;
.E8A1  A2 02    LDX #$02   ; CHKBAK LDX #NWRAP
.E8A3  A9 00    LDA #$00   ; LDA #0
.E8A5  C5 D3    CMP $D3   ; CHKLUP CMP PNTR
.E8A7  F0 07    BEQ $E8B0   ; BEQ BACK
.E8A9  18       CLC   ; CLC
.E8AA  69 28    ADC #$28   ; ADC #LLEN
.E8AC  CA       DEX   ; DEX
.E8AD  D0 F6    BNE $E8A5   ; BNE CHKLUP
.E8AF  60       RTS   ; RTS ;
.E8B0  C6 D6    DEC $D6   ; BACK   DEC TBLX
.E8B2  60       RTS   ; RTS ; ; CHECK FOR INCREMENT TBLX ;
.E8B3  A2 02    LDX #$02   ; CHKDWN LDX #NWRAP
.E8B5  A9 27    LDA #$27   ; LDA #LLEN-1
.E8B7  C5 D3    CMP $D3   ; DWNCHK CMP PNTR
.E8B9  F0 07    BEQ $E8C2   ; BEQ DNLINE
.E8BB  18       CLC   ; CLC
.E8BC  69 28    ADC #$28   ; ADC #LLEN
.E8BE  CA       DEX   ; DEX
.E8BF  D0 F6    BNE $E8B7   ; BNE DWNCHK
.E8C1  60       RTS   ; RTS ;
.E8C2  A6 D6    LDX $D6   ; DNLINE LDX TBLX
.E8C4  E0 19    CPX #$19   ; CPX #NLINES
.E8C6  F0 02    BEQ $E8CA   ; BEQ DWNBYE
.E8C8  E6 D6    INC $D6   ; INC TBLX ;
.E8CA  60       RTS   ; DWNBYE RTS CHKCOL
.E8CB  A2 0F    LDX #$0F   ; LDX #15         ;THERE'S 15 COLORS
.E8CD  DD DA E8 CMP $E8DA,X   ; CHK1A  CMP COLTAB,X
.E8D0  F0 04    BEQ $E8D6   ; BEQ CHK1B
.E8D2  CA       DEX   ; DEX
.E8D3  10 F8    BPL $E8CD   ; BPL CHK1A
.E8D5  60       RTS   ; RTS ; CHK1B
.E8D6  8E 86 02 STX $0286   ; STX COLOR       ;CHANGE THE COLOR
.E8D9  60       RTS   ; RTS COLTAB ;BLK,WHT,RED,CYAN,MAGENTA,GRN,BLUE,YELLOW
.E8DA  90 05 1C 9F 9C 1E 1F 9E   ; .BYT   $90,$05,$1C,$9F,$9C,$1E,$1F,$9E
.E8E2  81 95 96 97 98 99 9A 9B   ; .BYT   $81,$95,$96,$97,$98,$99,$9A,$9B .END ;.LIB CONKAT (JAPAN CONVERSION TABLES) .LIB   EDITOR.2 ;SCREEN SCROLL ROUTINE ;
.E8EA  A5 AC    LDA $AC   ; SCROL  LDA SAL
.E8EC  48       PHA   ; PHA
.E8ED  A5 AD    LDA $AD   ; LDA    SAH
.E8EF  48       PHA   ; PHA
.E8F0  A5 AE    LDA $AE   ; LDA    EAL
.E8F2  48       PHA   ; PHA
.E8F3  A5 AF    LDA $AF   ; LDA    EAH
.E8F5  48       PHA   ; PHA ; ;   S C R O L L   U P ;
.E8F6  A2 FF    LDX #$FF   ; SCRO0  LDX #$FF
.E8F8  C6 D6    DEC $D6   ; DEC TBLX
.E8FA  C6 C9    DEC $C9   ; DEC LSXP
.E8FC  CE A5 02 DEC $02A5   ; DEC LINTMP
.E8FF  E8       INX   ; SCR10  INX             ;GOTO NEXT LINE
.E900  20 F0 E9 JSR $E9F0   ; JSR SETPNT      ;POINT TO 'TO' LINE
.E903  E0 18    CPX #$18   ; CPX #NLINES-1   ;DONE?
.E905  B0 0C    BCS $E913   ; BCS SCR41       ;BRANCH IF SO ;
.E907  BD F1 EC LDA $ECF1,X   ; LDA LDTB2+1,X   ;SETUP FROM PNTR
.E90A  85 AC    STA $AC   ; STA SAL
.E90C  B5 DA    LDA $DA,X   ; LDA LDTB1+1,X
.E90E  20 C8 E9 JSR $E9C8   ; JSR SCRLIN      ;SCROLL THIS LINE UP1
.E911  30 EC    BMI $E8FF   ; BMI SCR10 ; SCR41
.E913  20 FF E9 JSR $E9FF   ; JSR CLRLN ;
.E916  A2 00    LDX #$00   ; LDX    #0              ;SCROLL HI BYTE POINTERS
.E918  B5 D9    LDA $D9,X   ; SCRL5  LDA LDTB1,X
.E91A  29 7F    AND #$7F   ; AND    #$7F
.E91C  B4 DA    LDY $DA,X   ; LDY    LDTB1+1,X
.E91E  10 02    BPL $E922   ; BPL    SCRL3
.E920  09 80    ORA #$80   ; ORA    #$80
.E922  95 D9    STA $D9,X   ; SCRL3  STA LDTB1,X
.E924  E8       INX   ; INX
.E925  E0 18    CPX #$18   ; CPX    #NLINES-1
.E927  D0 EF    BNE $E918   ; BNE    SCRL5 ;
.E929  A5 F1    LDA $F1   ; LDA    LDTB1+NLINES-1
.E92B  09 80    ORA #$80   ; ORA    #$80
.E92D  85 F1    STA $F1   ; STA    LDTB1+NLINES-1
.E92F  A5 D9    LDA $D9   ; LDA    LDTB1           ;DOUBLE LINE?
.E931  10 C3    BPL $E8F6   ; BPL    SCRO0           ;YES...SCROLL AGAIN ;
.E933  E6 D6    INC $D6   ; INC TBLX
.E935  EE A5 02 INC $02A5   ; INC LINTMP
.E938  A9 7F    LDA #$7F   ; LDA #$7F        ;CHECK FOR CONTROL KEY
.E93A  8D 00 DC STA $DC00   ; STA COLM        ;DROP LINE 2 ON PORT B
.E93D  AD 01 DC LDA $DC01   ; LDA ROWS
.E940  C9 FB    CMP #$FB   ; CMP #$FB        ;SLOW SCROLL KEY?(CONTROL)
.E942  08       PHP   ; PHP             ;SAVE STATUS. RESTORE PORT B
.E943  A9 7F    LDA #$7F   ; LDA #$7F        ;FOR STOP KEY CHECK
.E945  8D 00 DC STA $DC00   ; STA COLM
.E948  28       PLP   ; PLP
.E949  D0 0B    BNE $E956   ; BNE    MLP42 ;
.E94B  A0 00    LDY #$00   ; LDY    #0
.E94D  EA       NOP   ; MLP4   NOP             ;DELAY
.E94E  CA       DEX   ; DEX
.E94F  D0 FC    BNE $E94D   ; BNE    MLP4
.E951  88       DEY   ; DEY
.E952  D0 F9    BNE $E94D   ; BNE    MLP4
.E954  84 C6    STY $C6   ; STY    NDX             ;CLEAR KEY QUEUE BUFFER ;
.E956  A6 D6    LDX $D6   ; MLP42  LDX TBLX ;
.E958  68       PLA   ; PULIND PLA             ;RESTORE OLD INDIRECTS
.E959  85 AF    STA $AF   ; STA    EAH
.E95B  68       PLA   ; PLA
.E95C  85 AE    STA $AE   ; STA    EAL
.E95E  68       PLA   ; PLA
.E95F  85 AD    STA $AD   ; STA    SAH
.E961  68       PLA   ; PLA
.E962  85 AC    STA $AC   ; STA    SAL
.E964  60       RTS   ; RTS NEWLIN
.E965  A6 D6    LDX $D6   ; LDX TBLX
.E967  E8       INX   ; BMT1   INX ; CPX #NLINES ;EXCEDED THE NUMBER OF LINES ??? ; BEQ BMT2 ;VIC-40 CODE
.E968  B5 D9    LDA $D9,X   ; LDA LDTB1,X     ;FIND LAST DISPLAY LINE OF THIS LINE
.E96A  10 FB    BPL $E967   ; BPL BMT1        ;TABLE END MARK=>$FF WILL ABORT...ALSO
.E96C  8E A5 02 STX $02A5   ; BMT2   STX LINTMP      ;FOUND IT ;GENERATE A NEW LINE
.E96F  E0 18    CPX #$18   ; CPX    #NLINES-1       ;IS ONE LINE FROM BOTTOM?
.E971  F0 0E    BEQ $E981   ; BEQ    NEWLX           ;YES...JUST CLEAR LAST
.E973  90 0C    BCC $E981   ; BCC    NEWLX           ;<NLINES...INSERT LINE
.E975  20 EA E8 JSR $E8EA   ; JSR SCROL       ;SCROLL EVERYTHING
.E978  AE A5 02 LDX $02A5   ; LDX LINTMP
.E97B  CA       DEX   ; DEX
.E97C  C6 D6    DEC $D6   ; DEC TBLX
.E97E  4C DA E6 JMP $E6DA   ; JMP WLOG30
.E981  A5 AC    LDA $AC   ; NEWLX  LDA SAL
.E983  48       PHA   ; PHA
.E984  A5 AD    LDA $AD   ; LDA    SAH
.E986  48       PHA   ; PHA
.E987  A5 AE    LDA $AE   ; LDA    EAL
.E989  48       PHA   ; PHA
.E98A  A5 AF    LDA $AF   ; LDA    EAH
.E98C  48       PHA   ; PHA
.E98D  A2 19    LDX #$19   ; LDX #NLINES
.E98F  CA       DEX   ; SCD10  DEX
.E990  20 F0 E9 JSR $E9F0   ; JSR SETPNT      ;SET UP TO ADDR
.E993  EC A5 02 CPX $02A5   ; CPX LINTMP
.E996  90 0E    BCC $E9A6   ; BCC SCR40
.E998  F0 0C    BEQ $E9A6   ; BEQ SCR40       ;BRANCH IF FINISHED
.E99A  BD EF EC LDA $ECEF,X   ; LDA LDTB2-1,X   ;SET FROM ADDR
.E99D  85 AC    STA $AC   ; STA SAL
.E99F  B5 D8    LDA $D8,X   ; LDA LDTB1-1,X
.E9A1  20 C8 E9 JSR $E9C8   ; JSR SCRLIN      ;SCROLL THIS LINE DOWN
.E9A4  30 E9    BMI $E98F   ; BMI SCD10 SCR40
.E9A6  20 FF E9 JSR $E9FF   ; JSR CLRLN
.E9A9  A2 17    LDX #$17   ; LDX #NLINES-2 SCRD21
.E9AB  EC A5 02 CPX $02A5   ; CPX LINTMP      ;DONE?
.E9AE  90 0F    BCC $E9BF   ; BCC SCRD22      ;BRANCH IF SO
.E9B0  B5 DA    LDA $DA,X   ; LDA LDTB1+1,X
.E9B2  29 7F    AND #$7F   ; AND #$7F
.E9B4  B4 D9    LDY $D9,X   ; LDY LDTB1,X     ;WAS IT CONTINUED
.E9B6  10 02    BPL $E9BA   ; BPL SCRD19      ;BRANCH IF SO
.E9B8  09 80    ORA #$80   ; ORA #$80
.E9BA  95 DA    STA $DA,X   ; SCRD19 STA LDTB1+1,X
.E9BC  CA       DEX   ; DEX
.E9BD  D0 EC    BNE $E9AB   ; BNE SCRD21 SCRD22
.E9BF  AE A5 02 LDX $02A5   ; LDX LINTMP
.E9C2  20 DA E6 JSR $E6DA   ; JSR WLOG30 ;
.E9C5  4C 58 E9 JMP $E958   ; JMP PULIND      ;GO PUL OLD INDIRECTS AND RETURN ; ; SCROLL LINE FROM SAL TO PNT ; AND COLORS FROM EAL TO USER ; SCRLIN
.E9C8  29 03    AND #$03   ; AND #$03        ;CLEAR ANY GARBAGE STUFF
.E9CA  0D 88 02 ORA $0288   ; ORA HIBASE      ;PUT IN HIORDER BITS
.E9CD  85 AD    STA $AD   ; STA SAL+1
.E9CF  20 E0 E9 JSR $E9E0   ; JSR TOFROM      ;COLOR TO & FROM ADDRS
.E9D2  A0 27    LDY #$27   ; LDY #LLEN-1 SCD20
.E9D4  B1 AC    LDA ($AC),Y   ; LDA (SAL)Y
.E9D6  91 D1    STA ($D1),Y   ; STA (PNT)Y
.E9D8  B1 AE    LDA ($AE),Y   ; LDA (EAL)Y
.E9DA  91 F3    STA ($F3),Y   ; STA (USER)Y
.E9DC  88       DEY   ; DEY
.E9DD  10 F5    BPL $E9D4   ; BPL SCD20
.E9DF  60       RTS   ; RTS ; ; DO COLOR TO AND FROM ADDRESSES ; FROM CHARACTER TO AND FROM ADRS ; TOFROM
.E9E0  20 24 EA JSR $EA24   ; JSR SCOLOR
.E9E3  A5 AC    LDA $AC   ; LDA SAL         ;CHARACTER FROM
.E9E5  85 AE    STA $AE   ; STA EAL         ;MAKE COLOR FROM
.E9E7  A5 AD    LDA $AD   ; LDA SAL+1
.E9E9  29 03    AND #$03   ; AND #$03
.E9EB  09 D8    ORA #$D8   ; ORA #>VICCOL
.E9ED  85 AF    STA $AF   ; STA EAL+1
.E9EF  60       RTS   ; RTS ; ; SET UP PNT AND Y ; FROM .X ;
.E9F0  BD F0 EC LDA $ECF0,X   ; SETPNT LDA LDTB2,X
.E9F3  85 D1    STA $D1   ; STA PNT
.E9F5  B5 D9    LDA $D9,X   ; LDA LDTB1,X
.E9F7  29 03    AND #$03   ; AND #$03
.E9F9  0D 88 02 ORA $0288   ; ORA HIBASE
.E9FC  85 D2    STA $D2   ; STA PNT+1
.E9FE  60       RTS   ; RTS ; ; CLEAR THE LINE POINTED TO BY .X ;
.E9FF  A0 27    LDY #$27   ; CLRLN  LDY #LLEN-1
.EA01  20 F0 E9 JSR $E9F0   ; JSR SETPNT
.EA04  20 24 EA JSR $EA24   ; JSR SCOLOR
.EA07  20 DA E4 JSR $E4DA   ; CLR10  JSR CPATCH      ;REVERSED ORDER FROM 901227-02
.EA0A  A9 20    LDA #$20   ; LDA #$20        ;STORE A SPACE
.EA0C  91 D1    STA ($D1),Y   ; STA (PNT)Y     ;TO DISPLAY
.EA0E  88       DEY   ; DEY
.EA0F  10 F6    BPL $EA07   ; BPL CLR10
.EA11  60       RTS   ; RTS
.EA12  EA       NOP   ; NOP ; ;PUT A CHAR ON THE SCREEN ;
.EA13  A8       TAY   ; DSPP   TAY             ;SAVE CHAR
.EA14  A9 02    LDA #$02   ; LDA    #2
.EA16  85 CD    STA $CD   ; STA    BLNCT           ;BLINK CURSOR
.EA18  20 24 EA JSR $EA24   ; JSR    SCOLOR          ;SET COLOR PTR
.EA1B  98       TYA   ; TYA                    ;RESTORE COLOR
.EA1C  A4 D3    LDY $D3   ; DSPP2  LDY PNTR        ;GET COLUMN
.EA1E  91 D1    STA ($D1),Y   ; STA    (PNT)Y          ;CHAR TO SCREEN
.EA20  8A       TXA   ; TXA
.EA21  91 F3    STA ($F3),Y   ; STA    (USER)Y         ;COLOR TO SCREEN
.EA23  60       RTS   ; RTS
.EA24  A5 D1    LDA $D1   ; SCOLOR LDA PNT         ;GENERATE COLOR PTR
.EA26  85 F3    STA $F3   ; STA    USER
.EA28  A5 D2    LDA $D2   ; LDA    PNT+1
.EA2A  29 03    AND #$03   ; AND    #$03
.EA2C  09 D8    ORA #$D8   ; ORA    #>VICCOL        ;VIC COLOR RAM
.EA2E  85 F4    STA $F4   ; STA    USER+1
.EA30  60       RTS   ; RTS
.EA31  20 EA FF JSR $FFEA   ; KEY    JSR $FFEA       ;UPDATE JIFFY CLOCK
.EA34  A5 CC    LDA $CC   ; LDA BLNSW       ;BLINKING CRSR ?
.EA36  D0 29    BNE $EA61   ; BNE KEY4        ;NO
.EA38  C6 CD    DEC $CD   ; DEC BLNCT       ;TIME TO BLINK ?
.EA3A  D0 25    BNE $EA61   ; BNE KEY4        ;NO
.EA3C  A9 14    LDA #$14   ; LDA #20         ;RESET BLINK COUNTER
.EA3E  85 CD    STA $CD   ; REPDO  STA BLNCT
.EA40  A4 D3    LDY $D3   ; LDY PNTR        ;CURSOR POSITION
.EA42  46 CF    LSR $CF   ; LSR BLNON       ;CARRY SET IF ORIGINAL CHAR
.EA44  AE 87 02 LDX $0287   ; LDX GDCOL       ;GET CHAR ORIGINAL COLOR
.EA47  B1 D1    LDA ($D1),Y   ; LDA (PNT)Y      ;GET CHARACTER
.EA49  B0 11    BCS $EA5C   ; BCS KEY5        ;BRANCH IF NOT NEEDED ;
.EA4B  E6 CF    INC $CF   ; INC BLNON       ;SET TO 1
.EA4D  85 CE    STA $CE   ; STA GDBLN       ;SAVE ORIGINAL CHAR
.EA4F  20 24 EA JSR $EA24   ; JSR SCOLOR
.EA52  B1 F3    LDA ($F3),Y   ; LDA (USER)Y     ;GET ORIGINAL COLOR
.EA54  8D 87 02 STA $0287   ; STA GDCOL       ;SAVE IT
.EA57  AE 86 02 LDX $0286   ; LDX COLOR       ;BLINK IN THIS COLOR
.EA5A  A5 CE    LDA $CE   ; LDA GDBLN       ;WITH ORIGINAL CHARACTER ;
.EA5C  49 80    EOR #$80   ; KEY5   EOR #$80        ;BLINK IT
.EA5E  20 1C EA JSR $EA1C   ; JSR DSPP2       ;DISPLAY IT ;
.EA61  A5 01    LDA $01   ; KEY4   LDA R6510       ;GET CASSETTE SWITCHES
.EA63  29 10    AND #$10   ; AND #$10        ;IS SWITCH DOWN ?
.EA65  F0 0A    BEQ $EA71   ; BEQ KEY3        ;BRANCH IF SO ;
.EA67  A0 00    LDY #$00   ; LDY    #0
.EA69  84 C0    STY $C0   ; STY CAS1        ;CASSETTE OFF SWITCH ;
.EA6B  A5 01    LDA $01   ; LDA R6510
.EA6D  09 20    ORA #$20   ; ORA #$20
.EA6F  D0 08    BNE $EA79   ; BNE KL24        ;BRANCH IF MOTOR IS OFF ;
.EA71  A5 C0    LDA $C0   ; KEY3   LDA CAS1
.EA73  D0 06    BNE $EA7B   ; BNE KL2 ;
.EA75  A5 01    LDA $01   ; LDA R6510
.EA77  29 1F    AND #$1F   ; AND #%011111    ;TURN MOTOR ON ; KL24
.EA79  85 01    STA $01   ; STA R6510 ;
.EA7B  20 87 EA JSR $EA87   ; KL2    JSR SCNKEY      ;SCAN KEYBOARD ;
.EA7E  AD 0D DC LDA $DC0D   ; KPREND LDA D1ICR       ;CLEAR INTERUPT FLAGS
.EA81  68       PLA   ; PLA             ;RESTORE REGISTERS
.EA82  A8       TAY   ; TAY
.EA83  68       PLA   ; PLA
.EA84  AA       TAX   ; TAX
.EA85  68       PLA   ; PLA
.EA86  40       RTI   ; RTI             ;EXIT FROM IRQ ROUTINES
```


## Commenti

### Original Disassembly (Commodore)
- **$E591**: FINPUT CPX LSXP        ;CHECK IF ON SAME LINE
- **$E593**: BEQ FINPUX      ;YES..RETURN TO SEND
- **$E595**: JMP FINDST      ;CHECK IF WE WRAPPED DOWN...
- **$E598**: FINPUX RTS
- **$E599**: NOP             ;KEEP THE SPACE THE SAME... ;PANIC NMI ENTRY ;
- **$E59A**: VPAN   JSR PANIC       ;FIX VIC SCREEN
- **$E59D**: JMP    NXTD            ;HOME CURSOR
- **$E5A0**: PANIC  LDA #3          ;RESET DEFAULT I/O
- **$E5A2**: STA    DFLTO
- **$E5A4**: LDA    #0
- **$E5A6**: STA    DFLTN ;INIT VIC ;
- **$E5A8**: INITV  LDX #47         ;LOAD ALL VIC REGS ***
- **$E5AA**: PX4    LDA TVIC-1,X
- **$E5AD**: STA VICREG-1,X
- **$E5B0**: DEX
- **$E5B1**: BNE    PX4
- **$E5B3**: RTS ; ;REMOVE CHARACTER FROM QUEUE ;
- **$E5B4**: LP2    LDY KEYD
- **$E5B7**: LDX    #0
- **$E5B9**: LP1    LDA KEYD+1,X
- **$E5BC**: STA    KEYD,X
- **$E5BF**: INX
- **$E5C0**: CPX    NDX
- **$E5C2**: BNE    LP1
- **$E5C4**: DEC    NDX
- **$E5C6**: TYA
- **$E5C7**: CLI
- **$E5C8**: CLC                    ;GOOD RETURN
- **$E5C9**: RTS ;
- **$E5CA**: LOOP4  JSR PRT LOOP3
- **$E5CD**: LDA    NDX
- **$E5CF**: STA    BLNSW
- **$E5D1**: STA    AUTODN          ;TURN ON AUTO SCROLL DOWN
- **$E5D4**: BEQ    LOOP3
- **$E5D6**: SEI
- **$E5D7**: LDA    BLNON
- **$E5D9**: BEQ    LP21
- **$E5DB**: LDA    GDBLN
- **$E5DD**: LDX    GDCOL           ;RESTORE ORIGINAL COLOR
- **$E5E0**: LDY    #0
- **$E5E2**: STY    BLNON
- **$E5E4**: JSR    DSPP
- **$E5E7**: LP21   JSR LP2
- **$E5EA**: CMP    #$83            ;RUN KEY?
- **$E5EC**: BNE LP22
- **$E5EE**: LDX #9
- **$E5F0**: SEI
- **$E5F1**: STX NDX
- **$E5F3**: LP23   LDA RUNTB-1,X
- **$E5F6**: STA KEYD-1,X
- **$E5F9**: DEX
- **$E5FA**: BNE LP23
- **$E5FC**: BEQ LOOP3
- **$E5FE**: LP22   CMP #$D
- **$E600**: BNE    LOOP4
- **$E602**: LDY    LNMX
- **$E604**: STY    CRSW
- **$E606**: CLP5   LDA (PNT)Y
- **$E608**: CMP    #'
- **$E60A**: BNE    CLP6
- **$E60C**: DEY
- **$E60D**: BNE    CLP5
- **$E60F**: CLP6   INY
- **$E610**: STY    INDX
- **$E612**: LDY    #0
- **$E614**: STY AUTODN      ;TURN OFF AUTO SCROLL DOWN
- **$E617**: STY    PNTR
- **$E619**: STY    QTSW
- **$E61B**: LDA    LSXP
- **$E61D**: BMI    LOP5
- **$E61F**: LDX TBLX
- **$E621**: JSR FINDST      ;FIND 1ST PHYSICAL LINE
- **$E624**: CPX LSXP
- **$E626**: BNE    LOP5
- **$E628**: LDA    LSTP
- **$E62A**: STA    PNTR
- **$E62C**: CMP    INDX
- **$E62E**: BCC    LOP5
- **$E630**: BCS    CLP2 ;INPUT A LINE UNTIL CARRIAGE RETURN ;
- **$E632**: LOOP5  TYA
- **$E633**: PHA
- **$E634**: TXA
- **$E635**: PHA
- **$E636**: LDA    CRSW
- **$E638**: BEQ    LOOP3
- **$E63A**: LOP5   LDY PNTR
- **$E63C**: LDA    (PNT)Y NOTONE
- **$E63E**: STA    DATA
- **$E640**: LOP51  AND #$3F
- **$E642**: ASL    DATA
- **$E644**: BIT    DATA
- **$E646**: BPL    LOP54
- **$E648**: ORA    #$80
- **$E64A**: LOP54  BCC LOP52
- **$E64C**: LDX    QTSW
- **$E64E**: BNE    LOP53
- **$E650**: LOP52  BVS LOP53
- **$E652**: ORA    #$40
- **$E654**: LOP53  INC PNTR
- **$E656**: JSR    QTSWC
- **$E659**: CPY    INDX
- **$E65B**: BNE    CLP1
- **$E65D**: CLP2   LDA #0
- **$E65F**: STA    CRSW
- **$E661**: LDA    #$D
- **$E663**: LDX    DFLTN           ;FIX GETS FROM SCREEN
- **$E665**: CPX    #3              ;IS IT THE SCREEN?
- **$E667**: BEQ    CLP2A
- **$E669**: LDX    DFLTO
- **$E66B**: CPX    #3
- **$E66D**: BEQ    CLP21
- **$E66F**: CLP2A  JSR PRT
- **$E672**: CLP21  LDA #$D
- **$E674**: CLP1   STA DATA
- **$E676**: PLA
- **$E677**: TAX
- **$E678**: PLA
- **$E679**: TAY
- **$E67A**: LDA    DATA
- **$E67C**: CMP    #$DE            ;IS IT <PI> ?
- **$E67E**: BNE    CLP7
- **$E680**: LDA    #$FF
- **$E682**: CLP7   CLC
- **$E683**: RTS
- **$E684**: QTSWC  CMP #$22
- **$E686**: BNE    QTSWL
- **$E688**: LDA    QTSW
- **$E68A**: EOR    #$1
- **$E68C**: STA    QTSW
- **$E68E**: LDA    #$22
- **$E690**: QTSWL  RTS
- **$E691**: NXT33  ORA #$40
- **$E693**: NXT3   LDX RVS
- **$E695**: BEQ    NVS
- **$E697**: NC3    ORA #$80
- **$E699**: NVS    LDX INSRT
- **$E69B**: BEQ    NVS1
- **$E69D**: DEC    INSRT
- **$E69F**: NVS1   LDX COLOR PUT COLOR ON SCREEN
- **$E6A2**: JSR    DSPP
- **$E6A5**: JSR WLOGIC      ;CHECK FOR WRAPAROUND
- **$E6A8**: LOOP2  PLA
- **$E6A9**: TAY
- **$E6AA**: LDA    INSRT
- **$E6AC**: BEQ    LOP2
- **$E6AE**: LSR    QTSW
- **$E6B0**: LOP2   PLA
- **$E6B1**: TAX
- **$E6B2**: PLA
- **$E6B3**: CLC                    ;GOOD RETURN
- **$E6B4**: CLI
- **$E6B5**: RTS WLOGIC
- **$E6B6**: JSR CHKDWN      ;MAYBE WE SHOULD WE INCREMENT TBLX
- **$E6B9**: INC PNTR        ;BUMP CHARCTER POINTER
- **$E6BB**: LDA LNMX        ;
- **$E6BD**: CMP PNTR        ;IF LNMX IS LESS THAN PNTR
- **$E6BF**: BCS WLGRTS      ;BRANCH IF LNMX>=PNTR
- **$E6C1**: CMP #MAXCHR-1   ;PAST MAX CHARACTERS
- **$E6C3**: BEQ WLOG10      ;BRANCH IF SO
- **$E6C5**: LDA AUTODN      ;SHOULD WE AUTO SCROLL DOWN?
- **$E6C8**: BEQ WLOG20      ;BRANCH IF NOT
- **$E6CA**: JMP    BMT1            ;ELSE DECIDE WHICH WAY TO SCROLL WLOG20
- **$E6CD**: LDX TBLX        ;SEE IF WE SHOULD SCROLL DOWN
- **$E6CF**: CPX #NLINES
- **$E6D1**: BCC WLOG30      ;BRANCH IF NOT
- **$E6D3**: JSR SCROL       ;ELSE DO THE SCROL UP
- **$E6D6**: DEC TBLX        ;AND ADJUST CURENT LINE#
- **$E6D8**: LDX TBLX
- **$E6DA**: WLOG30 ASL LDTB1,X     ;WRAP THE LINE
- **$E6DC**: LSR LDTB1,X
- **$E6DE**: INX             ;INDEX TO NEXT LLINE
- **$E6DF**: LDA LDTB1,X     ;GET HIGH ORDER BYTE OF ADDRESS
- **$E6E1**: ORA #$80        ;MAKE IT A NON-CONTINUATION LINE
- **$E6E3**: STA LDTB1,X     ;AND PUT IT BACK
- **$E6E5**: DEX             ;GET BACK TO CURRENT LINE
- **$E6E6**: LDA LNMX        ;CONTINUE THE BYTES TAKEN OUT
- **$E6E8**: CLC
- **$E6E9**: ADC #LLEN
- **$E6EB**: STA LNMX FINDST
- **$E6ED**: LDA LDTB1,X     ;IS THIS THE FIRST LINE?
- **$E6EF**: BMI FINX        ;BRANCH IF SO
- **$E6F1**: DEX             ;ELSE BACKUP 1
- **$E6F2**: BNE FINDST FINX
- **$E6F4**: JMP SETPNT      ;MAKE SURE PNT IS RIGHT
- **$E6F7**: WLOG10 DEC TBLX
- **$E6F9**: JSR NXLN
- **$E6FC**: LDA #0
- **$E6FE**: STA PNTR        ;POINT TO FIRST BYTE
- **$E700**: WLGRTS RTS
- **$E701**: BKLN   LDX TBLX
- **$E703**: BNE BKLN1
- **$E705**: STX PNTR
- **$E707**: PLA
- **$E708**: PLA
- **$E709**: BNE LOOP2 ;
- **$E70B**: BKLN1  DEX
- **$E70C**: STX TBLX
- **$E70E**: JSR STUPT
- **$E711**: LDY LNMX
- **$E713**: STY PNTR
- **$E715**: RTS ;PRINT ROUTINE ;
- **$E716**: PRT    PHA
- **$E717**: STA    DATA
- **$E719**: TXA
- **$E71A**: PHA
- **$E71B**: TYA
- **$E71C**: PHA
- **$E71D**: LDA    #0
- **$E71F**: STA    CRSW
- **$E721**: LDY    PNTR
- **$E723**: LDA    DATA
- **$E725**: BPL    *+5
- **$E727**: JMP    NXTX
- **$E72A**: CMP    #$D
- **$E72C**: BNE    NJT1
- **$E72E**: JMP    NXT1
- **$E731**: NJT1   CMP #'
- **$E733**: BCC    NTCN
- **$E735**: CMP    #$60            ;LOWER CASE?
- **$E737**: BCC    NJT8            ;NO...
- **$E739**: AND    #$DF            ;YES...MAKE SCREEN LOWER
- **$E73B**: BNE    NJT9            ;ALWAYS
- **$E73D**: NJT8   AND #$3F
- **$E73F**: NJT9   JSR QTSWC
- **$E742**: JMP    NXT3
- **$E745**: NTCN   LDX INSRT
- **$E747**: BEQ    CNC3X
- **$E749**: JMP    NC3
- **$E74C**: CNC3X  CMP #$14
- **$E74E**: BNE    NTCN1
- **$E750**: TYA
- **$E751**: BNE    BAK1UP
- **$E753**: JSR BKLN
- **$E756**: JMP BK2
- **$E759**: BAK1UP JSR CHKBAK      ;SHOULD WE DEC TBLX
- **$E75C**: DEY
- **$E75D**: STY    PNTR
- **$E75F**: BK1    JSR SCOLOR      ;FIX COLOR PTRS
- **$E762**: BK15   INY
- **$E763**: LDA    (PNT)Y
- **$E765**: DEY
- **$E766**: STA    (PNT)Y
- **$E768**: INY
- **$E769**: LDA    (USER)Y
- **$E76B**: DEY
- **$E76C**: STA    (USER)Y
- **$E76E**: INY
- **$E76F**: CPY    LNMX
- **$E771**: BNE    BK15
- **$E773**: BK2    LDA #'
- **$E775**: STA    (PNT)Y
- **$E777**: LDA    COLOR
- **$E77A**: STA    (USER)Y
- **$E77C**: BPL    JPL3
- **$E77E**: NTCN1  LDX QTSW
- **$E780**: BEQ    NC3W
- **$E782**: CNC3   JMP NC3
- **$E785**: NC3W   CMP #$12
- **$E787**: BNE    NC1
- **$E789**: STA    RVS
- **$E78B**: NC1    CMP #$13
- **$E78D**: BNE    NC2
- **$E78F**: JSR    NXTD
- **$E792**: NC2    CMP #$1D
- **$E794**: BNE    NCX2
- **$E796**: INY
- **$E797**: JSR CHKDWN
- **$E79A**: STY    PNTR
- **$E79C**: DEY
- **$E79D**: CPY    LNMX
- **$E79F**: BCC    NCZ2
- **$E7A1**: DEC TBLX
- **$E7A3**: JSR    NXLN
- **$E7A6**: LDY    #0
- **$E7A8**: JPL4   STY PNTR
- **$E7AA**: NCZ2   JMP LOOP2
- **$E7AD**: NCX2   CMP #$11
- **$E7AF**: BNE    COLR1
- **$E7B1**: CLC
- **$E7B2**: TYA
- **$E7B3**: ADC    #LLEN
- **$E7B5**: TAY
- **$E7B6**: INC TBLX
- **$E7B8**: CMP    LNMX
- **$E7BA**: BCC    JPL4
- **$E7BC**: BEQ    JPL4
- **$E7BE**: DEC TBLX
- **$E7C0**: CURS10 SBC #LLEN
- **$E7C2**: BCC GOTDWN
- **$E7C4**: STA PNTR
- **$E7C6**: BNE CURS10
- **$E7C8**: GOTDWN JSR NXLN
- **$E7CB**: JPL3   JMP LOOP2
- **$E7CE**: COLR1  JSR CHKCOL      ;CHECK FOR A COLOR
- **$E7D1**: JMP LOWER       ;WAS JMP LOOP2 ;CHECK COLOR ; ;SHIFTED KEYS ; NXTX KEEPIT
- **$E7D4**: AND    #$7F
- **$E7D6**: CMP    #$7F
- **$E7D8**: BNE    NXTX1
- **$E7DA**: LDA    #$5E NXTX1 NXTXA
- **$E7DC**: CMP #$20        ;IS IT A FUNCTION KEY
- **$E7DE**: BCC    UHUH
- **$E7E0**: JMP    NXT33 UHUH
- **$E7E3**: CMP    #$D
- **$E7E5**: BNE    UP5
- **$E7E7**: JMP    NXT1
- **$E7EA**: UP5    LDX  QTSW
- **$E7EC**: BNE    UP6
- **$E7EE**: CMP    #$14
- **$E7F0**: BNE    UP9
- **$E7F2**: LDY    LNMX
- **$E7F4**: LDA    (PNT)Y
- **$E7F6**: CMP    #'
- **$E7F8**: BNE    INS3
- **$E7FA**: CPY    PNTR
- **$E7FC**: BNE    INS1
- **$E7FE**: INS3   CPY #MAXCHR-1
- **$E800**: BEQ    INSEXT          ;EXIT IF LINE TOO LONG
- **$E802**: JSR    NEWLIN          ;SCROLL DOWN 1
- **$E805**: INS1   LDY LNMX
- **$E807**: JSR    SCOLOR
- **$E80A**: INS2   DEY
- **$E80B**: LDA    (PNT)Y
- **$E80D**: INY
- **$E80E**: STA    (PNT)Y
- **$E810**: DEY
- **$E811**: LDA    (USER)Y
- **$E813**: INY
- **$E814**: STA    (USER)Y
- **$E816**: DEY
- **$E817**: CPY    PNTR
- **$E819**: BNE    INS2
- **$E81B**: LDA    #$20
- **$E81D**: STA    (PNT)Y
- **$E81F**: LDA    COLOR
- **$E822**: STA    (USER)Y
- **$E824**: INC    INSRT
- **$E826**: INSEXT JMP LOOP2
- **$E829**: UP9    LDX INSRT
- **$E82B**: BEQ    UP2
- **$E82D**: UP6    ORA #$40
- **$E82F**: JMP    NC3
- **$E832**: UP2    CMP #$11
- **$E834**: BNE    NXT2
- **$E836**: LDX    TBLX
- **$E838**: BEQ JPL2
- **$E83A**: DEC TBLX
- **$E83C**: LDA PNTR
- **$E83E**: SEC
- **$E83F**: SBC #LLEN
- **$E841**: BCC UPALIN
- **$E843**: STA PNTR
- **$E845**: BPL JPL2
- **$E847**: UPALIN JSR STUPT
- **$E84A**: BNE    JPL2
- **$E84C**: NXT2   CMP #$12
- **$E84E**: BNE    NXT6
- **$E850**: LDA    #0
- **$E852**: STA    RVS
- **$E854**: NXT6   CMP #$1D
- **$E856**: BNE    NXT61
- **$E858**: TYA
- **$E859**: BEQ    BAKBAK
- **$E85B**: JSR    CHKBAK
- **$E85E**: DEY
- **$E85F**: STY    PNTR
- **$E861**: JMP LOOP2
- **$E864**: BAKBAK JSR BKLN
- **$E867**: JMP    LOOP2
- **$E86A**: NXT61  CMP #$13
- **$E86C**: BNE    SCCL
- **$E86E**: JSR    CLSR
- **$E871**: JPL2   JMP LOOP2 SCCL
- **$E874**: ORA    #$80            ;MAKE IT UPPER CASE
- **$E876**: JSR    CHKCOL          ;TRY FOR COLOR
- **$E879**: JMP UPPER       ;WAS JMP LOOP2 ;
- **$E87C**: NXLN   LSR LSXP
- **$E87E**: LDX    TBLX
- **$E880**: NXLN2  INX
- **$E881**: CPX    #NLINES         ;OFF BOTTOM?
- **$E883**: BNE    NXLN1           ;NO...
- **$E885**: JSR    SCROL           ;YES...SCROLL
- **$E888**: NXLN1  LDA LDTB1,X     ;DOUBLE LINE?
- **$E88A**: BPL    NXLN2           ;YES...SCROLL AGAIN
- **$E88C**: STX    TBLX
- **$E88E**: JMP    STUPT NXT1
- **$E891**: LDX    #0
- **$E893**: STX    INSRT
- **$E895**: STX    RVS
- **$E897**: STX    QTSW
- **$E899**: STX    PNTR
- **$E89B**: JSR    NXLN
- **$E89E**: JPL5   JMP LOOP2 ; ; ; CHECK FOR A DECREMENT TBLX ;
- **$E8A1**: CHKBAK LDX #NWRAP
- **$E8A3**: LDA #0
- **$E8A5**: CHKLUP CMP PNTR
- **$E8A7**: BEQ BACK
- **$E8A9**: CLC
- **$E8AA**: ADC #LLEN
- **$E8AC**: DEX
- **$E8AD**: BNE CHKLUP
- **$E8AF**: RTS ;
- **$E8B0**: BACK   DEC TBLX
- **$E8B2**: RTS ; ; CHECK FOR INCREMENT TBLX ;
- **$E8B3**: CHKDWN LDX #NWRAP
- **$E8B5**: LDA #LLEN-1
- **$E8B7**: DWNCHK CMP PNTR
- **$E8B9**: BEQ DNLINE
- **$E8BB**: CLC
- **$E8BC**: ADC #LLEN
- **$E8BE**: DEX
- **$E8BF**: BNE DWNCHK
- **$E8C1**: RTS ;
- **$E8C2**: DNLINE LDX TBLX
- **$E8C4**: CPX #NLINES
- **$E8C6**: BEQ DWNBYE
- **$E8C8**: INC TBLX ;
- **$E8CA**: DWNBYE RTS CHKCOL
- **$E8CB**: LDX #15         ;THERE'S 15 COLORS
- **$E8CD**: CHK1A  CMP COLTAB,X
- **$E8D0**: BEQ CHK1B
- **$E8D2**: DEX
- **$E8D3**: BPL CHK1A
- **$E8D5**: RTS ; CHK1B
- **$E8D6**: STX COLOR       ;CHANGE THE COLOR
- **$E8D9**: RTS COLTAB ;BLK,WHT,RED,CYAN,MAGENTA,GRN,BLUE,YELLOW
- **$E8DA**: .BYT   $90,$05,$1C,$9F,$9C,$1E,$1F,$9E
- **$E8E2**: .BYT   $81,$95,$96,$97,$98,$99,$9A,$9B .END ;.LIB CONKAT (JAPAN CONVERSION TABLES) .LIB   EDITOR.2 ;SCREEN SCROLL ROUTINE ;
- **$E8EA**: SCROL  LDA SAL
- **$E8EC**: PHA
- **$E8ED**: LDA    SAH
- **$E8EF**: PHA
- **$E8F0**: LDA    EAL
- **$E8F2**: PHA
- **$E8F3**: LDA    EAH
- **$E8F5**: PHA ; ;   S C R O L L   U P ;
- **$E8F6**: SCRO0  LDX #$FF
- **$E8F8**: DEC TBLX
- **$E8FA**: DEC LSXP
- **$E8FC**: DEC LINTMP
- **$E8FF**: SCR10  INX             ;GOTO NEXT LINE
- **$E900**: JSR SETPNT      ;POINT TO 'TO' LINE
- **$E903**: CPX #NLINES-1   ;DONE?
- **$E905**: BCS SCR41       ;BRANCH IF SO ;
- **$E907**: LDA LDTB2+1,X   ;SETUP FROM PNTR
- **$E90A**: STA SAL
- **$E90C**: LDA LDTB1+1,X
- **$E90E**: JSR SCRLIN      ;SCROLL THIS LINE UP1
- **$E911**: BMI SCR10 ; SCR41
- **$E913**: JSR CLRLN ;
- **$E916**: LDX    #0              ;SCROLL HI BYTE POINTERS
- **$E918**: SCRL5  LDA LDTB1,X
- **$E91A**: AND    #$7F
- **$E91C**: LDY    LDTB1+1,X
- **$E91E**: BPL    SCRL3
- **$E920**: ORA    #$80
- **$E922**: SCRL3  STA LDTB1,X
- **$E924**: INX
- **$E925**: CPX    #NLINES-1
- **$E927**: BNE    SCRL5 ;
- **$E929**: LDA    LDTB1+NLINES-1
- **$E92B**: ORA    #$80
- **$E92D**: STA    LDTB1+NLINES-1
- **$E92F**: LDA    LDTB1           ;DOUBLE LINE?
- **$E931**: BPL    SCRO0           ;YES...SCROLL AGAIN ;
- **$E933**: INC TBLX
- **$E935**: INC LINTMP
- **$E938**: LDA #$7F        ;CHECK FOR CONTROL KEY
- **$E93A**: STA COLM        ;DROP LINE 2 ON PORT B
- **$E93D**: LDA ROWS
- **$E940**: CMP #$FB        ;SLOW SCROLL KEY?(CONTROL)
- **$E942**: PHP             ;SAVE STATUS. RESTORE PORT B
- **$E943**: LDA #$7F        ;FOR STOP KEY CHECK
- **$E945**: STA COLM
- **$E948**: PLP
- **$E949**: BNE    MLP42 ;
- **$E94B**: LDY    #0
- **$E94D**: MLP4   NOP             ;DELAY
- **$E94E**: DEX
- **$E94F**: BNE    MLP4
- **$E951**: DEY
- **$E952**: BNE    MLP4
- **$E954**: STY    NDX             ;CLEAR KEY QUEUE BUFFER ;
- **$E956**: MLP42  LDX TBLX ;
- **$E958**: PULIND PLA             ;RESTORE OLD INDIRECTS
- **$E959**: STA    EAH
- **$E95B**: PLA
- **$E95C**: STA    EAL
- **$E95E**: PLA
- **$E95F**: STA    SAH
- **$E961**: PLA
- **$E962**: STA    SAL
- **$E964**: RTS NEWLIN
- **$E965**: LDX TBLX
- **$E967**: BMT1   INX ; CPX #NLINES ;EXCEDED THE NUMBER OF LINES ??? ; BEQ BMT2 ;VIC-40 CODE
- **$E968**: LDA LDTB1,X     ;FIND LAST DISPLAY LINE OF THIS LINE
- **$E96A**: BPL BMT1        ;TABLE END MARK=>$FF WILL ABORT...ALSO
- **$E96C**: BMT2   STX LINTMP      ;FOUND IT ;GENERATE A NEW LINE
- **$E96F**: CPX    #NLINES-1       ;IS ONE LINE FROM BOTTOM?
- **$E971**: BEQ    NEWLX           ;YES...JUST CLEAR LAST
- **$E973**: BCC    NEWLX           ;<NLINES...INSERT LINE
- **$E975**: JSR SCROL       ;SCROLL EVERYTHING
- **$E978**: LDX LINTMP
- **$E97B**: DEX
- **$E97C**: DEC TBLX
- **$E97E**: JMP WLOG30
- **$E981**: NEWLX  LDA SAL
- **$E983**: PHA
- **$E984**: LDA    SAH
- **$E986**: PHA
- **$E987**: LDA    EAL
- **$E989**: PHA
- **$E98A**: LDA    EAH
- **$E98C**: PHA
- **$E98D**: LDX #NLINES
- **$E98F**: SCD10  DEX
- **$E990**: JSR SETPNT      ;SET UP TO ADDR
- **$E993**: CPX LINTMP
- **$E996**: BCC SCR40
- **$E998**: BEQ SCR40       ;BRANCH IF FINISHED
- **$E99A**: LDA LDTB2-1,X   ;SET FROM ADDR
- **$E99D**: STA SAL
- **$E99F**: LDA LDTB1-1,X
- **$E9A1**: JSR SCRLIN      ;SCROLL THIS LINE DOWN
- **$E9A4**: BMI SCD10 SCR40
- **$E9A6**: JSR CLRLN
- **$E9A9**: LDX #NLINES-2 SCRD21
- **$E9AB**: CPX LINTMP      ;DONE?
- **$E9AE**: BCC SCRD22      ;BRANCH IF SO
- **$E9B0**: LDA LDTB1+1,X
- **$E9B2**: AND #$7F
- **$E9B4**: LDY LDTB1,X     ;WAS IT CONTINUED
- **$E9B6**: BPL SCRD19      ;BRANCH IF SO
- **$E9B8**: ORA #$80
- **$E9BA**: SCRD19 STA LDTB1+1,X
- **$E9BC**: DEX
- **$E9BD**: BNE SCRD21 SCRD22
- **$E9BF**: LDX LINTMP
- **$E9C2**: JSR WLOG30 ;
- **$E9C5**: JMP PULIND      ;GO PUL OLD INDIRECTS AND RETURN ; ; SCROLL LINE FROM SAL TO PNT ; AND COLORS FROM EAL TO USER ; SCRLIN
- **$E9C8**: AND #$03        ;CLEAR ANY GARBAGE STUFF
- **$E9CA**: ORA HIBASE      ;PUT IN HIORDER BITS
- **$E9CD**: STA SAL+1
- **$E9CF**: JSR TOFROM      ;COLOR TO & FROM ADDRS
- **$E9D2**: LDY #LLEN-1 SCD20
- **$E9D4**: LDA (SAL)Y
- **$E9D6**: STA (PNT)Y
- **$E9D8**: LDA (EAL)Y
- **$E9DA**: STA (USER)Y
- **$E9DC**: DEY
- **$E9DD**: BPL SCD20
- **$E9DF**: RTS ; ; DO COLOR TO AND FROM ADDRESSES ; FROM CHARACTER TO AND FROM ADRS ; TOFROM
- **$E9E0**: JSR SCOLOR
- **$E9E3**: LDA SAL         ;CHARACTER FROM
- **$E9E5**: STA EAL         ;MAKE COLOR FROM
- **$E9E7**: LDA SAL+1
- **$E9E9**: AND #$03
- **$E9EB**: ORA #>VICCOL
- **$E9ED**: STA EAL+1
- **$E9EF**: RTS ; ; SET UP PNT AND Y ; FROM .X ;
- **$E9F0**: SETPNT LDA LDTB2,X
- **$E9F3**: STA PNT
- **$E9F5**: LDA LDTB1,X
- **$E9F7**: AND #$03
- **$E9F9**: ORA HIBASE
- **$E9FC**: STA PNT+1
- **$E9FE**: RTS ; ; CLEAR THE LINE POINTED TO BY .X ;
- **$E9FF**: CLRLN  LDY #LLEN-1
- **$EA01**: JSR SETPNT
- **$EA04**: JSR SCOLOR
- **$EA07**: CLR10  JSR CPATCH      ;REVERSED ORDER FROM 901227-02
- **$EA0A**: LDA #$20        ;STORE A SPACE
- **$EA0C**: STA (PNT)Y     ;TO DISPLAY
- **$EA0E**: DEY
- **$EA0F**: BPL CLR10
- **$EA11**: RTS
- **$EA12**: NOP ; ;PUT A CHAR ON THE SCREEN ;
- **$EA13**: DSPP   TAY             ;SAVE CHAR
- **$EA14**: LDA    #2
- **$EA16**: STA    BLNCT           ;BLINK CURSOR
- **$EA18**: JSR    SCOLOR          ;SET COLOR PTR
- **$EA1B**: TYA                    ;RESTORE COLOR
- **$EA1C**: DSPP2  LDY PNTR        ;GET COLUMN
- **$EA1E**: STA    (PNT)Y          ;CHAR TO SCREEN
- **$EA20**: TXA
- **$EA21**: STA    (USER)Y         ;COLOR TO SCREEN
- **$EA23**: RTS
- **$EA24**: SCOLOR LDA PNT         ;GENERATE COLOR PTR
- **$EA26**: STA    USER
- **$EA28**: LDA    PNT+1
- **$EA2A**: AND    #$03
- **$EA2C**: ORA    #>VICCOL        ;VIC COLOR RAM
- **$EA2E**: STA    USER+1
- **$EA30**: RTS
- **$EA31**: KEY    JSR $FFEA       ;UPDATE JIFFY CLOCK
- **$EA34**: LDA BLNSW       ;BLINKING CRSR ?
- **$EA36**: BNE KEY4        ;NO
- **$EA38**: DEC BLNCT       ;TIME TO BLINK ?
- **$EA3A**: BNE KEY4        ;NO
- **$EA3C**: LDA #20         ;RESET BLINK COUNTER
- **$EA3E**: REPDO  STA BLNCT
- **$EA40**: LDY PNTR        ;CURSOR POSITION
- **$EA42**: LSR BLNON       ;CARRY SET IF ORIGINAL CHAR
- **$EA44**: LDX GDCOL       ;GET CHAR ORIGINAL COLOR
- **$EA47**: LDA (PNT)Y      ;GET CHARACTER
- **$EA49**: BCS KEY5        ;BRANCH IF NOT NEEDED ;
- **$EA4B**: INC BLNON       ;SET TO 1
- **$EA4D**: STA GDBLN       ;SAVE ORIGINAL CHAR
- **$EA4F**: JSR SCOLOR
- **$EA52**: LDA (USER)Y     ;GET ORIGINAL COLOR
- **$EA54**: STA GDCOL       ;SAVE IT
- **$EA57**: LDX COLOR       ;BLINK IN THIS COLOR
- **$EA5A**: LDA GDBLN       ;WITH ORIGINAL CHARACTER ;
- **$EA5C**: KEY5   EOR #$80        ;BLINK IT
- **$EA5E**: JSR DSPP2       ;DISPLAY IT ;
- **$EA61**: KEY4   LDA R6510       ;GET CASSETTE SWITCHES
- **$EA63**: AND #$10        ;IS SWITCH DOWN ?
- **$EA65**: BEQ KEY3        ;BRANCH IF SO ;
- **$EA67**: LDY    #0
- **$EA69**: STY CAS1        ;CASSETTE OFF SWITCH ;
- **$EA6B**: LDA R6510
- **$EA6D**: ORA #$20
- **$EA6F**: BNE KL24        ;BRANCH IF MOTOR IS OFF ;
- **$EA71**: KEY3   LDA CAS1
- **$EA73**: BNE KL2 ;
- **$EA75**: LDA R6510
- **$EA77**: AND #%011111    ;TURN MOTOR ON ; KL24
- **$EA79**: STA R6510 ;
- **$EA7B**: KL2    JSR SCNKEY      ;SCAN KEYBOARD ;
- **$EA7E**: KPREND LDA D1ICR       ;CLEAR INTERUPT FLAGS
- **$EA81**: PLA             ;RESTORE REGISTERS
- **$EA82**: TAY
- **$EA83**: PLA
- **$EA84**: TAX
- **$EA85**: PLA
- **$EA86**: RTI             ;EXIT FROM IRQ ROUTINES

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*