---
title: ;  GENERAL KEYBOARD SCAN
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
- 0090-status
- 00a0-time
- 00a5-count
- 00c5-lstx
- 00c6-ndx
- 00c7-rvs
- 00cb-sfdx
- 00d7-data
- 00f5-keytab
- 0277-keyd
- 0289-xmax
- 028a-rptflg
- 028b-kount
- 028c-delay
- 028d-shflag
- 028e-lstshf
- 028f-keylog
- 0291-mode
- asl
- bcc
- bcs
- beq
- bit
- bmi
- bne
- bpl
- bvs
- check
- clear
- cmp
- cpx
- cpy
- dec
- dex
- dey
- ea87-tastaturabfrage
- eadd-process-key-image
- eb48-commodore
- eb64-select-keyboard-table
- eb79-dekodiertabellen
- eb81-ungeshifted
- ebc2-tabelle-2-geshifted
- ec03-tabelle-3-mit-c-taste
- ec44-prft-auf-steuerzeichen
- ec5e-shift-commodore-key-check
- ec78-tabelle-4-mit-ctrl-taste
- ecb9-videocontroller
- ece7-load
- ece7-runstop
- ecec-run
- eor
- f5ed-save
- fce2-reset
- inx
- iny
- jmp
- lda
- ldx
- ldy
- lsr
- ora
- output
- pha
- pla
- return
- rol
- rts
- scnkey
- sec
- setup
- sta
- stop
- stx
- sty
- tax
- tay
- txa
- update
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EA87
  address_end: $ECE7
  symbol: general-keyboard-scan
  sources:
  - name: Original Disassembly
    author: Commodore
    description: '- **$EA87**: SCNKEY LDA #$00'
  - name: Original Disassembly
    author: —
    description: '- **$EA87**: clear A'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EA89**: Shift/CTRL Flag rücksetzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$EAFD**: delete'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EA89**: clear SHFLAG'
---

# $EA87 — ;  GENERAL KEYBOARD SCAN

## Disassemblatura
```assembly
.EA87  A9 00    LDA #$00   ; SCNKEY LDA #$00
.EA89  8D 8D 02 STA $028D   ; STA SHFLAG
.EA8C  A0 40    LDY #$40   ; LDY #64         ;LAST KEY INDEX
.EA8E  84 CB    STY $CB   ; STY SFDX        ;NULL KEY FOUND
.EA90  8D 00 DC STA $DC00   ; STA COLM        ;RAISE ALL LINES
.EA93  AE 01 DC LDX $DC01   ; LDX ROWS        ;CHECK FOR A KEY DOWN
.EA96  E0 FF    CPX #$FF   ; CPX #$FF        ;NO KEYS DOWN?
.EA98  F0 61    BEQ $EAFB   ; BEQ SCNOUT      ;BRANCH IF NONE
.EA9A  A8       TAY   ; TAY             ;.A=0 LDY #0
.EA9B  A9 81    LDA #$81   ; LDA #<MODE1
.EA9D  85 F5    STA $F5   ; STA KEYTAB
.EA9F  A9 EB    LDA #$EB   ; LDA #>MODE1
.EAA1  85 F6    STA $F6   ; STA KEYTAB+1
.EAA3  A9 FE    LDA #$FE   ; LDA #$FE        ;START WITH 1ST COLUMN
.EAA5  8D 00 DC STA $DC00   ; STA COLM
.EAA8  A2 08    LDX #$08   ; SCN20  LDX #8          ;8 ROW KEYBOARD
.EAAA  48       PHA   ; PHA             ;SAVE COLUMN OUTPUT INFO
.EAAB  AD 01 DC LDA $DC01   ; SCN22  LDA ROWS
.EAAE  CD 01 DC CMP $DC01   ; CMP ROWS        ;DEBOUNCE KEYBOARD
.EAB1  D0 F8    BNE $EAAB   ; BNE SCN22
.EAB3  4A       LSR   ; SCN30  LSR A           ;LOOK FOR KEY DOWN
.EAB4  B0 16    BCS $EACC   ; BCS CKIT        ;NONE
.EAB6  48       PHA   ; PHA
.EAB7  B1 F5    LDA ($F5),Y   ; LDA (KEYTAB),Y  ;GET CHAR CODE
.EAB9  C9 05    CMP #$05   ; CMP #$05
.EABB  B0 0C    BCS $EAC9   ; BCS SPCK2       ;IF NOT SPECIAL KEY GO ON
.EABD  C9 03    CMP #$03   ; CMP #$03        ;COULD IT BE A STOP KEY?
.EABF  F0 08    BEQ $EAC9   ; BEQ SPCK2       ;BRANCH IF SO
.EAC1  0D 8D 02 ORA $028D   ; ORA SHFLAG
.EAC4  8D 8D 02 STA $028D   ; STA SHFLAG      ;PUT SHIFT BIT IN FLAG BYTE
.EAC7  10 02    BPL $EACB   ; BPL CKUT SPCK2
.EAC9  84 CB    STY $CB   ; STY SFDX        ;SAVE KEY NUMBER
.EACB  68       PLA   ; CKUT   PLA
.EACC  C8       INY   ; CKIT   INY
.EACD  C0 41    CPY #$41   ; CPY #65
.EACF  B0 0B    BCS $EADC   ; BCS CKIT1       ;BRANCH IF FINISHED
.EAD1  CA       DEX   ; DEX
.EAD2  D0 DF    BNE $EAB3   ; BNE SCN30
.EAD4  38       SEC   ; SEC
.EAD5  68       PLA   ; PLA             ;RELOAD COLUMN INFO
.EAD6  2A       ROL   ; ROL A
.EAD7  8D 00 DC STA $DC00   ; STA COLM        ;NEXT COLUMN ON KEYBOARD
.EADA  D0 CC    BNE $EAA8   ; BNE SCN20       ;ALWAYS BRANCH
.EADC  68       PLA   ; CKIT1  PLA             ;DUMP COLUMN OUTPUT...ALL DONE
.EADD  6C 8F 02 JMP ($028F)   ; JMP (KEYLOG)    ;EVALUATE SHIFT FUNCTIONS
.EAE0  A4 CB    LDY $CB   ; REKEY  LDY SFDX        ;GET KEY INDEX
.EAE2  B1 F5    LDA ($F5),Y   ; LDA (KEYTAB)Y   ;GET CHAR CODE
.EAE4  AA       TAX   ; TAX             ;SAVE THE CHAR
.EAE5  C4 C5    CPY $C5   ; CPY LSTX        ;SAME AS PREV CHAR INDEX?
.EAE7  F0 07    BEQ $EAF0   ; BEQ RPT10       ;YES
.EAE9  A0 10    LDY #$10   ; LDY #$10        ;NO - RESET DELAY BEFORE REPEAT
.EAEB  8C 8C 02 STY $028C   ; STY DELAY
.EAEE  D0 36    BNE $EB26   ; BNE CKIT2       ;ALWAYS
.EAF0  29 7F    AND #$7F   ; RPT10  AND #$7F        ;UNSHIFT IT
.EAF2  2C 8A 02 BIT $028A   ; BIT RPTFLG      ;CHECK FOR REPEAT DISABLE
.EAF5  30 16    BMI $EB0D   ; BMI RPT20       ;YES
.EAF7  70 49    BVS $EB42   ; BVS SCNRTS
.EAF9  C9 7F    CMP #$7F   ; CMP #$7F        ;NO KEYS ?
.EAFB  F0 29    BEQ $EB26   ; SCNOUT BEQ CKIT2       ;YES - GET OUT
.EAFD  C9 14    CMP #$14   ; CMP #$14        ;AN INST/DEL KEY ?
.EAFF  F0 0C    BEQ $EB0D   ; BEQ RPT20       ;YES - REPEAT IT
.EB01  C9 20    CMP #$20   ; CMP #$20        ;A SPACE KEY ?
.EB03  F0 08    BEQ $EB0D   ; BEQ RPT20       ;YES
.EB05  C9 1D    CMP #$1D   ; CMP #$1D        ;A CRSR LEFT/RIGHT ?
.EB07  F0 04    BEQ $EB0D   ; BEQ RPT20       ;YES
.EB09  C9 11    CMP #$11   ; CMP #$11        ;A CRSR UP/DWN ?
.EB0B  D0 35    BNE $EB42   ; BNE SCNRTS      ;NO - EXIT
.EB0D  AC 8C 02 LDY $028C   ; RPT20  LDY DELAY       ;TIME TO REPEAT ?
.EB10  F0 05    BEQ $EB17   ; BEQ RPT40       ;YES
.EB12  CE 8C 02 DEC $028C   ; DEC DELAY
.EB15  D0 2B    BNE $EB42   ; BNE SCNRTS
.EB17  CE 8B 02 DEC $028B   ; RPT40  DEC KOUNT       ;TIME FOR NEXT REPEAT ?
.EB1A  D0 26    BNE $EB42   ; BNE SCNRTS      ;NO
.EB1C  A0 04    LDY #$04   ; LDY #4          ;YES - RESET CTR
.EB1E  8C 8B 02 STY $028B   ; STY KOUNT
.EB21  A4 C6    LDY $C6   ; LDY NDX         ;NO REPEAT IF QUEUE FULL
.EB23  88       DEY   ; DEY
.EB24  10 1C    BPL $EB42   ; BPL SCNRTS CKIT2
.EB26  A4 CB    LDY $CB   ; LDY SFDX        ;GET INDEX OF KEY
.EB28  84 C5    STY $C5   ; STY LSTX        ;SAVE THIS INDEX TO KEY FOUND
.EB2A  AC 8D 02 LDY $028D   ; LDY SHFLAG      ;UPDATE SHIFT STATUS
.EB2D  8C 8E 02 STY $028E   ; STY LSTSHF
.EB30  E0 FF    CPX #$FF   ; CKIT3  CPX #$FF        ;A NULL KEY OR NO KEY ?
.EB32  F0 0E    BEQ $EB42   ; BEQ SCNRTS      ;BRANCH IF SO
.EB34  8A       TXA   ; TXA             ;NEED X AS INDEX SO...
.EB35  A6 C6    LDX $C6   ; LDX NDX         ;GET # OF CHARS IN KEY QUEUE
.EB37  EC 89 02 CPX $0289   ; CPX XMAX        ;IRQ BUFFER FULL ?
.EB3A  B0 06    BCS $EB42   ; BCS SCNRTS      ;YES - NO MORE INSERT PUTQUE
.EB3C  9D 77 02 STA $0277,X   ; STA KEYD,X      ;PUT RAW DATA HERE
.EB3F  E8       INX   ; INX
.EB40  86 C6    STX $C6   ; STX NDX         ;UPDATE KEY QUEUE COUNT
.EB42  A9 7F    LDA #$7F   ; SCNRTS LDA #$7F        ;SETUP PB7 FOR STOP KEY SENSE
.EB44  8D 00 DC STA $DC00   ; STA COLM
.EB47  60       RTS   ; RTS ; ; SHIFT LOGIC ; SHFLOG
.EB48  AD 8D 02 LDA $028D   ; LDA SHFLAG
.EB4B  C9 03    CMP #$03   ; CMP #$03        ;COMMODORE SHIFT COMBINATION?
.EB4D  D0 15    BNE $EB64   ; BNE KEYLG2      ;BRANCH IF NOT
.EB4F  CD 8E 02 CMP $028E   ; CMP LSTSHF      ;DID I DO THIS ALREADY
.EB52  F0 EE    BEQ $EB42   ; BEQ SCNRTS      ;BRANCH IF SO
.EB54  AD 91 02 LDA $0291   ; LDA MODE
.EB57  30 1D    BMI $EB76   ; BMI SHFOUT      ;DONT SHIFT IF ITS MINUS
.EB59  AD 18 D0 LDA $D018   ; SWITCH LDA VICREG+24   ;**********************************:
.EB5C  49 02    EOR #$02   ; EOR #$02        ;TURN ON OTHER CASE
.EB5E  8D 18 D0 STA $D018   ; STA VICREG+24   ;POINT THE VIC THERE
.EB61  4C 76 EB JMP $EB76   ; JMP SHFOUT ; KEYLG2
.EB64  0A       ASL   ; ASL A
.EB65  C9 08    CMP #$08   ; CMP #$08        ;WAS IT A CONTROL KEY
.EB67  90 02    BCC $EB6B   ; BCC NCTRL       ;BRANCH IF NOT
.EB69  A9 06    LDA #$06   ; LDA #6          ;ELSE USE TABLE #4 ; NCTRL NOTKAT
.EB6B  AA       TAX   ; TAX
.EB6C  BD 79 EB LDA $EB79,X   ; LDA KEYCOD,X
.EB6F  85 F5    STA $F5   ; STA KEYTAB
.EB71  BD 7A EB LDA $EB7A,X   ; LDA KEYCOD+1,X
.EB74  85 F6    STA $F6   ; STA KEYTAB+1 SHFOUT
.EB76  4C E0 EA JMP $EAE0   ; JMP REKEY .END .LIB   EDITOR.3 KEYCOD                 ;KEYBOARD MODE 'DISPATCH' .WORD MODE1 .WORD MODE2 .WORD MODE3
.EB79  81 EB C2 EB 03 EC 78 EC   ; .WORD CONTRL    ;CONTROL KEYS ; ; COTTACONNA MODE ; ;.WORD MODE1  ;PET MODE1 ;.WORD MODE2  ;PET MODE2 ;.WORD CCTTA3 ;DUMMY WORD ;.WORD CONTRL ; ; EXTENDED KATAKANA MODE ; ;.WORD CCTTA2 ;KATAKANA CHARACTERS ;.WORD CCTTA3 ;LIMITED GRAPHICS ;.WORD CCTTA3 ;DUMMY ;.WORD CONTRL MODE1 ;DEL,3,5,7,9,+,YEN SIGN,1
.EB81  14 0D 1D 88 85 86 87 11   ; .BYT   $14,$0D,$1D,$88,$85,$86,$87,$11 ;RETURN,W,R,Y,I,P,*,LEFT ARROW
.EB89  33 57 41 34 5A 53 45 01   ; .BYT   $33,$57,$41,$34,$5A,$53,$45,$01 ;RT CRSR,A,D,G,J,L,;,CTRL
.EB91  35 52 44 36 43 46 54 58   ; .BYT   $35,$52,$44,$36,$43,$46,$54,$58 ;F4,4,6,8,0,-,HOME,2
.EB99  37 59 47 38 42 48 55 56   ; .BYT   $37,$59,$47,$38,$42,$48,$55,$56 ;F1,Z,C,B,M,.,R.SHIFTT,SPACE
.EBA1  39 49 4A 30 4D 4B 4F 4E   ; .BYT   $39,$49,$4A,$30,$4D,$4B,$4F,$4E ;F2,S,F,H,K,:,=,COM.KEY
.EBA9  2B 50 4C 2D 2E 3A 40 2C   ; .BYT   $2B,$50,$4C,$2D,$2E,$3A,$40,$2C ;F3,E,T,U,O,@,EXP,Q
.EBB1  5C 2A 3B 13 01 3D 5E 2F   ; .BYT   $5C,$2A,$3B,$13,$01,$3D,$5E,$2F ;CRSR DWN,L.SHIFT,X,V,N,,,/,STOP
.EBB9  31 5F 04 32 20 02 51 03   ; .BYT   $31,$5F,$04,$32,$20,$02,$51,$03
.EBC1  FF   ; .BYT   $FF             ;END OF TABLE NULL MODE2                  ;SHIFT ;INS,%,',),+,YEN,!
.EBC2  94 8D 9D 8C 89 8A 8B 91   ; .BYT   $94,$8D,$9D,$8C,$89,$8A,$8B,$91 ;SRETURN,W,R,Y,I,P,*,SLEFT ARROW
.EBCA  23 D7 C1 24 DA D3 C5 01   ; .BYT   $23,$D7,$C1,$24,$DA,$D3,$C5,$01 ;LF.CRSR,A,D,G,J,L,;,CTRL
.EBD2  25 D2 C4 26 C3 C6 D4 D8   ; .BYT   $25,$D2,$C4,$26,$C3,$C6,$D4,$D8 ;,$,&,(,      ,"
.EBDA  27 D9 C7 28 C2 C8 D5 D6   ; .BYT   $27,$D9,$C7,$28,$C2,$C8,$D5,$D6 ;F5,Z,C,B,M,.,R.SHIFT,SSPACE
.EBE2  29 C9 CA 30 CD CB CF CE   ; .BYT   $29,$C9,$CA,$30,$CD,$CB,$CF,$CE ;F6,S,F,H,K,:,=,SCOM.KEY
.EBEA  DB D0 CC DD 3E 5B BA 3C   ; .BYT   $DB,$D0,$CC,$DD,$3E,$5B,$BA,$3C ;F7,E,T,U,O,@,PI,G
.EBF2  A9 C0 5D 93 01 3D DE 3F   ; .BYT   $A9,$C0,$5D,$93,$01,$3D,$DE,$3F ;CRSR DWN,L.SHIFT,X,V,N,,,/,RUN
.EBFA  21 5F 04 22 A0 02 D1 83   ; .BYT   $21,$5F,$04,$22,$A0,$02,$D1,$83
.EC02  FF   ; .BYT   $FF             ;END OF TABLE NULL ; MODE3                  ;LEFT WINDOW GRAHPICS ;INS,C10,C12,C14,9,+,POUND SIGN,C8
.EC03  94 8D 9D 8C 89 8A 8B 91   ; .BYT   $94,$8D,$9D,$8C,$89,$8A,$8B,$91 ;RETURN,W,R,Y,I,P,*,LFT.ARROW
.EC0B  96 B3 B0 97 AD AE B1 01   ; .BYT   $96,$B3,$B0,$97,$AD,$AE,$B1,$01 ;LF.CRSR,A,D,G,J,L,;,CTRL
.EC13  98 B2 AC 99 BC BB A3 BD   ; .BYT   $98,$B2,$AC,$99,$BC,$BB,$A3,$BD ;F8,C11,C13,C15,0,-,HOME,C9
.EC1B  9A B7 A5 9B BF B4 B8 BE   ; .BYT   $9A,$B7,$A5,$9B,$BF,$B4,$B8,$BE ;F2,Z,C,B,M,.,R.SHIFT,SPACE
.EC23  29 A2 B5 30 A7 A1 B9 AA   ; .BYT   $29,$A2,$B5,$30,$A7,$A1,$B9,$AA ;F4,S,F,H,K,:,=,COM.KEY
.EC2B  A6 AF B6 DC 3E 5B A4 3C   ; .BYT   $A6,$AF,$B6,$DC,$3E,$5B,$A4,$3C ;F6,E,T,U,O,@,PI,Q
.EC33  A8 DF 5D 93 01 3D DE 3F   ; .BYT   $A8,$DF,$5D,$93,$01,$3D,$DE,$3F ;CRSR.UP,L.SHIFT,X,V,N,,,/,STOP
.EC3B  81 5F 04 95 A0 02 AB 83   ; .BYT   $81,$5F,$04,$95,$A0,$02,$AB,$83
.EC43  FF   ; .BYT   $FF             ;END OF TABLE NULL ;CCTTA2 ;WAS CCTTA2 IN JAPANESE VERSION LOWER
.EC44  C9 0E    CMP #$0E   ; CMP #$0E        ;DOES HE WANT LOWER CASE?
.EC46  D0 07    BNE $EC4F   ; BNE UPPER       ;BRANCH IF NOT
.EC48  AD 18 D0 LDA $D018   ; LDA VICREG+24   ;ELSE SET VIC TO POINT TO LOWER CASE
.EC4B  09 02    ORA #$02   ; ORA #$02
.EC4D  D0 09    BNE $EC58   ; BNE ULSET       ;JMP UPPER
.EC4F  C9 8E    CMP #$8E   ; CMP #$8E        ;DOES HE WANT UPPER CASE
.EC51  D0 0B    BNE $EC5E   ; BNE LOCK        ;BRANCH IF NOT
.EC53  AD 18 D0 LDA $D018   ; LDA VICREG+24   ;MAKE SURE VIC POINT TO UPPER/PET SET
.EC56  29 FD    AND #$FD   ; AND #$FF-$02
.EC58  8D 18 D0 STA $D018   ; ULSET  STA VICREG+24
.EC5B  4C A8 E6 JMP $E6A8   ; OUTHRE JMP LOOP2 LOCK
.EC5E  C9 08    CMP #$08   ; CMP #8          ;DOES HE WANT TO LOCK IN THIS MODE?
.EC60  D0 07    BNE $EC69   ; BNE UNLOCK      ;BRANCH IF NOT
.EC62  A9 80    LDA #$80   ; LDA #$80        ;ELSE SET LOCK SWITCH ON
.EC64  0D 91 02 ORA $0291   ; ORA MODE        ;DON'T HURT ANYTHING - JUST IN CASE
.EC67  30 09    BMI $EC72   ; BMI LEXIT UNLOCK
.EC69  C9 09    CMP #$09   ; CMP #9          ;DOES HE WANT TO UNLOCK THE KEYBOARD?
.EC6B  D0 EE    BNE $EC5B   ; BNE OUTHRE      ;BRANCH IF NOT
.EC6D  A9 7F    LDA #$7F   ; LDA #$7F        ;CLEAR THE LOCK SWITCH
.EC6F  2D 91 02 AND $0291   ; AND MODE        ;DONT HURT ANYTHING
.EC72  8D 91 02 STA $0291   ; LEXIT  STA MODE
.EC75  4C A8 E6 JMP $E6A8   ; JMP LOOP2       ;GET OUT ;CCTTA3 ;.BYT $04,$FF,$FF,$FF,$FF,$FF,$E2,$9D ;RUN-K24-K31 ;.BYT $83,$01,$FF,$FF,$FF,$FF,$FF,$91 ;K32-K39.F5 ;.BYT $A0,$FF,$FF,$FF,$FF,$EE,$01,$89 ;CO.KEY,K40-K47.F6 ;.BYT $02,$FF,$FF,$FF,$FF,$E1,$FD,$8A ;K48-K55 ;.BYT $FF,$FF,$FF,$FF,$FF,$B0,$E0,$8B ;K56-K63 ;.BYT $F2,$F4,$F6,$FF,$F0,$ED,$93,$8C ;.BYT $FF ;END OF TABLE NULL CONTRL ;NULL,RED,PURPLE,BLUE,RVS ,NULL,NULL,BLACK
.EC78  FF FF FF FF FF FF FF FF   ; .BYT   $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF ;NULL, W  ,REVERSE, Y  , I  , P  ,NULL,MUSIC
.EC80  1C 17 01 9F 1A 13 05 FF   ; .BYT   $1C,$17,$01,$9F,$1A,$13,$05,$FF
.EC88  9C 12 04 1E 03 06 14 18   ; .BYT   $9C,$12,$04,$1E,$03,$06,$14,$18 ;NULL,CYAN,GREEN,YELLOW,RVS OFF,NULL,NULL,WHITE
.EC90  1F 19 07 9E 02 08 15 16   ; .BYT   $1F,$19,$07,$9E,$02,$08,$15,$16
.EC98  12 09 0A 92 0D 0B 0F 0E   ; .BYT   $12,$09,$0A,$92,$0D,$0B,$0F,$0E
.ECA0  FF 10 0C FF FF 1B 00 FF   ; .BYT   $FF,$10,$0C,$FF,$FF,$1B,$00,$FF
.ECA8  1C FF 1D FF FF 1F 1E FF   ; .BYT   $1C,$FF,$1D,$FF,$FF,$1F,$1E,$FF
.ECB0  90 06 FF 05 FF FF 11 FF   ; .BYT   $90,$06,$FF,$05,$FF,$FF,$11,$FF
.ECB8  FF   ; .BYT   $FF             ;END OF TABLE NULL TVIC .BYT   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ;SPRITES (0-16) .BYT   $1B,0,0,0,0,$08,0,$14,0,0,0,0,0,0,0 ;DATA (17-31)
.ECB9  00 00 00 00 00 00 00 00   ; .BYT   14,6,1,2,3,4,0,1,2,3,4,5,6,7 ;32-46 ;
.ECE7  4C 4F 41 44 0D 52 55 4E   ; RUNTB  .BYT 'LOAD',$D,'RUN',$D ; LINZ0  = VICSCN LINZ1  = LINZ0+LLEN LINZ2  = LINZ1+LLEN LINZ3  = LINZ2+LLEN LINZ4  = LINZ3+LLEN LINZ5  = LINZ4+LLEN LINZ6  = LINZ5+LLEN LINZ7  = LINZ6+LLEN LINZ8  = LINZ7+LLEN LINZ9  = LINZ8+LLEN LINZ10 = LINZ9+LLEN LINZ11 = LINZ10+LLEN LINZ12 = LINZ11+LLEN LINZ13 = LINZ12+LLEN LINZ14 = LINZ13+LLEN LINZ15 = LINZ14+LLEN LINZ16 = LINZ15+LLEN LINZ17 = LINZ16+LLEN LINZ18 = LINZ17+LLEN LINZ19 = LINZ18+LLEN LINZ20 = LINZ19+LLEN LINZ21 = LINZ20+LLEN LINZ22 = LINZ21+LLEN LINZ23 = LINZ22+LLEN LINZ24 = LINZ23+LLEN
```


## Commenti

### Original Disassembly (Commodore)
- **$EA87**: SCNKEY LDA #$00
- **$EA89**: STA SHFLAG
- **$EA8C**: LDY #64         ;LAST KEY INDEX
- **$EA8E**: STY SFDX        ;NULL KEY FOUND
- **$EA90**: STA COLM        ;RAISE ALL LINES
- **$EA93**: LDX ROWS        ;CHECK FOR A KEY DOWN
- **$EA96**: CPX #$FF        ;NO KEYS DOWN?
- **$EA98**: BEQ SCNOUT      ;BRANCH IF NONE
- **$EA9A**: TAY             ;.A=0 LDY #0
- **$EA9B**: LDA #<MODE1
- **$EA9D**: STA KEYTAB
- **$EA9F**: LDA #>MODE1
- **$EAA1**: STA KEYTAB+1
- **$EAA3**: LDA #$FE        ;START WITH 1ST COLUMN
- **$EAA5**: STA COLM
- **$EAA8**: SCN20  LDX #8          ;8 ROW KEYBOARD
- **$EAAA**: PHA             ;SAVE COLUMN OUTPUT INFO
- **$EAAB**: SCN22  LDA ROWS
- **$EAAE**: CMP ROWS        ;DEBOUNCE KEYBOARD
- **$EAB1**: BNE SCN22
- **$EAB3**: SCN30  LSR A           ;LOOK FOR KEY DOWN
- **$EAB4**: BCS CKIT        ;NONE
- **$EAB6**: PHA
- **$EAB7**: LDA (KEYTAB),Y  ;GET CHAR CODE
- **$EAB9**: CMP #$05
- **$EABB**: BCS SPCK2       ;IF NOT SPECIAL KEY GO ON
- **$EABD**: CMP #$03        ;COULD IT BE A STOP KEY?
- **$EABF**: BEQ SPCK2       ;BRANCH IF SO
- **$EAC1**: ORA SHFLAG
- **$EAC4**: STA SHFLAG      ;PUT SHIFT BIT IN FLAG BYTE
- **$EAC7**: BPL CKUT SPCK2
- **$EAC9**: STY SFDX        ;SAVE KEY NUMBER
- **$EACB**: CKUT   PLA
- **$EACC**: CKIT   INY
- **$EACD**: CPY #65
- **$EACF**: BCS CKIT1       ;BRANCH IF FINISHED
- **$EAD1**: DEX
- **$EAD2**: BNE SCN30
- **$EAD4**: SEC
- **$EAD5**: PLA             ;RELOAD COLUMN INFO
- **$EAD6**: ROL A
- **$EAD7**: STA COLM        ;NEXT COLUMN ON KEYBOARD
- **$EADA**: BNE SCN20       ;ALWAYS BRANCH
- **$EADC**: CKIT1  PLA             ;DUMP COLUMN OUTPUT...ALL DONE
- **$EADD**: JMP (KEYLOG)    ;EVALUATE SHIFT FUNCTIONS
- **$EAE0**: REKEY  LDY SFDX        ;GET KEY INDEX
- **$EAE2**: LDA (KEYTAB)Y   ;GET CHAR CODE
- **$EAE4**: TAX             ;SAVE THE CHAR
- **$EAE5**: CPY LSTX        ;SAME AS PREV CHAR INDEX?
- **$EAE7**: BEQ RPT10       ;YES
- **$EAE9**: LDY #$10        ;NO - RESET DELAY BEFORE REPEAT
- **$EAEB**: STY DELAY
- **$EAEE**: BNE CKIT2       ;ALWAYS
- **$EAF0**: RPT10  AND #$7F        ;UNSHIFT IT
- **$EAF2**: BIT RPTFLG      ;CHECK FOR REPEAT DISABLE
- **$EAF5**: BMI RPT20       ;YES
- **$EAF7**: BVS SCNRTS
- **$EAF9**: CMP #$7F        ;NO KEYS ?
- **$EAFB**: SCNOUT BEQ CKIT2       ;YES - GET OUT
- **$EAFD**: CMP #$14        ;AN INST/DEL KEY ?
- **$EAFF**: BEQ RPT20       ;YES - REPEAT IT
- **$EB01**: CMP #$20        ;A SPACE KEY ?
- **$EB03**: BEQ RPT20       ;YES
- **$EB05**: CMP #$1D        ;A CRSR LEFT/RIGHT ?
- **$EB07**: BEQ RPT20       ;YES
- **$EB09**: CMP #$11        ;A CRSR UP/DWN ?
- **$EB0B**: BNE SCNRTS      ;NO - EXIT
- **$EB0D**: RPT20  LDY DELAY       ;TIME TO REPEAT ?
- **$EB10**: BEQ RPT40       ;YES
- **$EB12**: DEC DELAY
- **$EB15**: BNE SCNRTS
- **$EB17**: RPT40  DEC KOUNT       ;TIME FOR NEXT REPEAT ?
- **$EB1A**: BNE SCNRTS      ;NO
- **$EB1C**: LDY #4          ;YES - RESET CTR
- **$EB1E**: STY KOUNT
- **$EB21**: LDY NDX         ;NO REPEAT IF QUEUE FULL
- **$EB23**: DEY
- **$EB24**: BPL SCNRTS CKIT2
- **$EB26**: LDY SFDX        ;GET INDEX OF KEY
- **$EB28**: STY LSTX        ;SAVE THIS INDEX TO KEY FOUND
- **$EB2A**: LDY SHFLAG      ;UPDATE SHIFT STATUS
- **$EB2D**: STY LSTSHF
- **$EB30**: CKIT3  CPX #$FF        ;A NULL KEY OR NO KEY ?
- **$EB32**: BEQ SCNRTS      ;BRANCH IF SO
- **$EB34**: TXA             ;NEED X AS INDEX SO...
- **$EB35**: LDX NDX         ;GET # OF CHARS IN KEY QUEUE
- **$EB37**: CPX XMAX        ;IRQ BUFFER FULL ?
- **$EB3A**: BCS SCNRTS      ;YES - NO MORE INSERT PUTQUE
- **$EB3C**: STA KEYD,X      ;PUT RAW DATA HERE
- **$EB3F**: INX
- **$EB40**: STX NDX         ;UPDATE KEY QUEUE COUNT
- **$EB42**: SCNRTS LDA #$7F        ;SETUP PB7 FOR STOP KEY SENSE
- **$EB44**: STA COLM
- **$EB47**: RTS ; ; SHIFT LOGIC ; SHFLOG
- **$EB48**: LDA SHFLAG
- **$EB4B**: CMP #$03        ;COMMODORE SHIFT COMBINATION?
- **$EB4D**: BNE KEYLG2      ;BRANCH IF NOT
- **$EB4F**: CMP LSTSHF      ;DID I DO THIS ALREADY
- **$EB52**: BEQ SCNRTS      ;BRANCH IF SO
- **$EB54**: LDA MODE
- **$EB57**: BMI SHFOUT      ;DONT SHIFT IF ITS MINUS
- **$EB59**: SWITCH LDA VICREG+24   ;**********************************:
- **$EB5C**: EOR #$02        ;TURN ON OTHER CASE
- **$EB5E**: STA VICREG+24   ;POINT THE VIC THERE
- **$EB61**: JMP SHFOUT ; KEYLG2
- **$EB64**: ASL A
- **$EB65**: CMP #$08        ;WAS IT A CONTROL KEY
- **$EB67**: BCC NCTRL       ;BRANCH IF NOT
- **$EB69**: LDA #6          ;ELSE USE TABLE #4 ; NCTRL NOTKAT
- **$EB6B**: TAX
- **$EB6C**: LDA KEYCOD,X
- **$EB6F**: STA KEYTAB
- **$EB71**: LDA KEYCOD+1,X
- **$EB74**: STA KEYTAB+1 SHFOUT
- **$EB76**: JMP REKEY .END .LIB   EDITOR.3 KEYCOD                 ;KEYBOARD MODE 'DISPATCH' .WORD MODE1 .WORD MODE2 .WORD MODE3
- **$EB79**: .WORD CONTRL    ;CONTROL KEYS ; ; COTTACONNA MODE ; ;.WORD MODE1  ;PET MODE1 ;.WORD MODE2  ;PET MODE2 ;.WORD CCTTA3 ;DUMMY WORD ;.WORD CONTRL ; ; EXTENDED KATAKANA MODE ; ;.WORD CCTTA2 ;KATAKANA CHARACTERS ;.WORD CCTTA3 ;LIMITED GRAPHICS ;.WORD CCTTA3 ;DUMMY ;.WORD CONTRL MODE1 ;DEL,3,5,7,9,+,YEN SIGN,1
- **$EB81**: .BYT   $14,$0D,$1D,$88,$85,$86,$87,$11 ;RETURN,W,R,Y,I,P,*,LEFT ARROW
- **$EB89**: .BYT   $33,$57,$41,$34,$5A,$53,$45,$01 ;RT CRSR,A,D,G,J,L,;,CTRL
- **$EB91**: .BYT   $35,$52,$44,$36,$43,$46,$54,$58 ;F4,4,6,8,0,-,HOME,2
- **$EB99**: .BYT   $37,$59,$47,$38,$42,$48,$55,$56 ;F1,Z,C,B,M,.,R.SHIFTT,SPACE
- **$EBA1**: .BYT   $39,$49,$4A,$30,$4D,$4B,$4F,$4E ;F2,S,F,H,K,:,=,COM.KEY
- **$EBA9**: .BYT   $2B,$50,$4C,$2D,$2E,$3A,$40,$2C ;F3,E,T,U,O,@,EXP,Q
- **$EBB1**: .BYT   $5C,$2A,$3B,$13,$01,$3D,$5E,$2F ;CRSR DWN,L.SHIFT,X,V,N,,,/,STOP
- **$EBB9**: .BYT   $31,$5F,$04,$32,$20,$02,$51,$03
- **$EBC1**: .BYT   $FF             ;END OF TABLE NULL MODE2                  ;SHIFT ;INS,%,',),+,YEN,!
- **$EBC2**: .BYT   $94,$8D,$9D,$8C,$89,$8A,$8B,$91 ;SRETURN,W,R,Y,I,P,*,SLEFT ARROW
- **$EBCA**: .BYT   $23,$D7,$C1,$24,$DA,$D3,$C5,$01 ;LF.CRSR,A,D,G,J,L,;,CTRL
- **$EBD2**: .BYT   $25,$D2,$C4,$26,$C3,$C6,$D4,$D8 ;,$,&,(,      ,"
- **$EBDA**: .BYT   $27,$D9,$C7,$28,$C2,$C8,$D5,$D6 ;F5,Z,C,B,M,.,R.SHIFT,SSPACE
- **$EBE2**: .BYT   $29,$C9,$CA,$30,$CD,$CB,$CF,$CE ;F6,S,F,H,K,:,=,SCOM.KEY
- **$EBEA**: .BYT   $DB,$D0,$CC,$DD,$3E,$5B,$BA,$3C ;F7,E,T,U,O,@,PI,G
- **$EBF2**: .BYT   $A9,$C0,$5D,$93,$01,$3D,$DE,$3F ;CRSR DWN,L.SHIFT,X,V,N,,,/,RUN
- **$EBFA**: .BYT   $21,$5F,$04,$22,$A0,$02,$D1,$83
- **$EC02**: .BYT   $FF             ;END OF TABLE NULL ; MODE3                  ;LEFT WINDOW GRAHPICS ;INS,C10,C12,C14,9,+,POUND SIGN,C8
- **$EC03**: .BYT   $94,$8D,$9D,$8C,$89,$8A,$8B,$91 ;RETURN,W,R,Y,I,P,*,LFT.ARROW
- **$EC0B**: .BYT   $96,$B3,$B0,$97,$AD,$AE,$B1,$01 ;LF.CRSR,A,D,G,J,L,;,CTRL
- **$EC13**: .BYT   $98,$B2,$AC,$99,$BC,$BB,$A3,$BD ;F8,C11,C13,C15,0,-,HOME,C9
- **$EC1B**: .BYT   $9A,$B7,$A5,$9B,$BF,$B4,$B8,$BE ;F2,Z,C,B,M,.,R.SHIFT,SPACE
- **$EC23**: .BYT   $29,$A2,$B5,$30,$A7,$A1,$B9,$AA ;F4,S,F,H,K,:,=,COM.KEY
- **$EC2B**: .BYT   $A6,$AF,$B6,$DC,$3E,$5B,$A4,$3C ;F6,E,T,U,O,@,PI,Q
- **$EC33**: .BYT   $A8,$DF,$5D,$93,$01,$3D,$DE,$3F ;CRSR.UP,L.SHIFT,X,V,N,,,/,STOP
- **$EC3B**: .BYT   $81,$5F,$04,$95,$A0,$02,$AB,$83
- **$EC43**: .BYT   $FF             ;END OF TABLE NULL ;CCTTA2 ;WAS CCTTA2 IN JAPANESE VERSION LOWER
- **$EC44**: CMP #$0E        ;DOES HE WANT LOWER CASE?
- **$EC46**: BNE UPPER       ;BRANCH IF NOT
- **$EC48**: LDA VICREG+24   ;ELSE SET VIC TO POINT TO LOWER CASE
- **$EC4B**: ORA #$02
- **$EC4D**: BNE ULSET       ;JMP UPPER
- **$EC4F**: CMP #$8E        ;DOES HE WANT UPPER CASE
- **$EC51**: BNE LOCK        ;BRANCH IF NOT
- **$EC53**: LDA VICREG+24   ;MAKE SURE VIC POINT TO UPPER/PET SET
- **$EC56**: AND #$FF-$02
- **$EC58**: ULSET  STA VICREG+24
- **$EC5B**: OUTHRE JMP LOOP2 LOCK
- **$EC5E**: CMP #8          ;DOES HE WANT TO LOCK IN THIS MODE?
- **$EC60**: BNE UNLOCK      ;BRANCH IF NOT
- **$EC62**: LDA #$80        ;ELSE SET LOCK SWITCH ON
- **$EC64**: ORA MODE        ;DON'T HURT ANYTHING - JUST IN CASE
- **$EC67**: BMI LEXIT UNLOCK
- **$EC69**: CMP #9          ;DOES HE WANT TO UNLOCK THE KEYBOARD?
- **$EC6B**: BNE OUTHRE      ;BRANCH IF NOT
- **$EC6D**: LDA #$7F        ;CLEAR THE LOCK SWITCH
- **$EC6F**: AND MODE        ;DONT HURT ANYTHING
- **$EC72**: LEXIT  STA MODE
- **$EC75**: JMP LOOP2       ;GET OUT ;CCTTA3 ;.BYT $04,$FF,$FF,$FF,$FF,$FF,$E2,$9D ;RUN-K24-K31 ;.BYT $83,$01,$FF,$FF,$FF,$FF,$FF,$91 ;K32-K39.F5 ;.BYT $A0,$FF,$FF,$FF,$FF,$EE,$01,$89 ;CO.KEY,K40-K47.F6 ;.BYT $02,$FF,$FF,$FF,$FF,$E1,$FD,$8A ;K48-K55 ;.BYT $FF,$FF,$FF,$FF,$FF,$B0,$E0,$8B ;K56-K63 ;.BYT $F2,$F4,$F6,$FF,$F0,$ED,$93,$8C ;.BYT $FF ;END OF TABLE NULL CONTRL ;NULL,RED,PURPLE,BLUE,RVS ,NULL,NULL,BLACK
- **$EC78**: .BYT   $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF ;NULL, W  ,REVERSE, Y  , I  , P  ,NULL,MUSIC
- **$EC80**: .BYT   $1C,$17,$01,$9F,$1A,$13,$05,$FF
- **$EC88**: .BYT   $9C,$12,$04,$1E,$03,$06,$14,$18 ;NULL,CYAN,GREEN,YELLOW,RVS OFF,NULL,NULL,WHITE
- **$EC90**: .BYT   $1F,$19,$07,$9E,$02,$08,$15,$16
- **$EC98**: .BYT   $12,$09,$0A,$92,$0D,$0B,$0F,$0E
- **$ECA0**: .BYT   $FF,$10,$0C,$FF,$FF,$1B,$00,$FF
- **$ECA8**: .BYT   $1C,$FF,$1D,$FF,$FF,$1F,$1E,$FF
- **$ECB0**: .BYT   $90,$06,$FF,$05,$FF,$FF,$11,$FF
- **$ECB8**: .BYT   $FF             ;END OF TABLE NULL TVIC .BYT   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ;SPRITES (0-16) .BYT   $1B,0,0,0,0,$08,0,$14,0,0,0,0,0,0,0 ;DATA (17-31)
- **$ECB9**: .BYT   14,6,1,2,3,4,0,1,2,3,4,5,6,7 ;32-46 ;
- **$ECE7**: RUNTB  .BYT 'LOAD',$D,'RUN',$D ; LINZ0  = VICSCN LINZ1  = LINZ0+LLEN LINZ2  = LINZ1+LLEN LINZ3  = LINZ2+LLEN LINZ4  = LINZ3+LLEN LINZ5  = LINZ4+LLEN LINZ6  = LINZ5+LLEN LINZ7  = LINZ6+LLEN LINZ8  = LINZ7+LLEN LINZ9  = LINZ8+LLEN LINZ10 = LINZ9+LLEN LINZ11 = LINZ10+LLEN LINZ12 = LINZ11+LLEN LINZ13 = LINZ12+LLEN LINZ14 = LINZ13+LLEN LINZ15 = LINZ14+LLEN LINZ16 = LINZ15+LLEN LINZ17 = LINZ16+LLEN LINZ18 = LINZ17+LLEN LINZ19 = LINZ18+LLEN LINZ20 = LINZ19+LLEN LINZ21 = LINZ20+LLEN LINZ22 = LINZ21+LLEN LINZ23 = LINZ22+LLEN LINZ24 = LINZ23+LLEN

### Original Disassembly (—)
- **$EA87**: clear A
- **$EA89**: clear the keyboard shift/control/c= flag
- **$EA8C**: set no key
- **$EA8E**: save which key
- **$EA90**: clear VIA 1 DRA, keyboard column drive
- **$EA93**: read VIA 1 DRB, keyboard row port
- **$EA96**: compare with all bits set
- **$EA98**: if no key pressed clear current key and exit (does further BEQ to $EBBA)
- **$EA9A**: clear the key count
- **$EA9B**: get the decode table low byte
- **$EA9D**: save the keyboard pointer low byte
- **$EA9F**: get the decode table high byte
- **$EAA1**: save the keyboard pointer high byte
- **$EAA3**: set column 0 low
- **$EAA5**: save VIA 1 DRA, keyboard column drive
- **$EAA8**: set the row count
- **$EAAA**: save the column
- **$EAAB**: read VIA 1 DRB, keyboard row port
- **$EAAE**: compare it with itself
- **$EAB1**: loop if changing
- **$EAB3**: shift row to Cb
- **$EAB4**: if no key closed on this row go do next row
- **$EAB6**: save row
- **$EAB7**: get character from decode table
- **$EAB9**: compare with $05, there is no $05 key but the control keys are all less than $05
- **$EABB**: if not shift/control/c=/stop go save key count else was shift/control/c=/stop key
- **$EABD**: compare with $03, stop
- **$EABF**: if stop go save key count and continue character is $01 - shift, $02 - c= or $04 - control
- **$EAC1**: OR it with the keyboard shift/control/c= flag
- **$EAC4**: save the keyboard shift/control/c= flag
- **$EAC7**: skip save key, branch always
- **$EAC9**: save key count
- **$EACB**: restore row
- **$EACC**: increment key count
- **$EACD**: compare with max+1
- **$EACF**: exit loop if >= max+1 else still in matrix
- **$EAD1**: decrement row count
- **$EAD2**: loop if more rows to do
- **$EAD4**: set carry for keyboard column shift
- **$EAD5**: restore the column
- **$EAD6**: shift the keyboard column
- **$EAD7**: save VIA 1 DRA, keyboard column drive
- **$EADA**: loop for next column, branch always
- **$EADC**: dump the saved column
- **$EADD**: evaluate the SHIFT/CTRL/C= keys, $EBDC key decoding continues here after the SHIFT/CTRL/C= keys are evaluated
- **$EAE0**: get saved key count
- **$EAE2**: get character from decode table
- **$EAE4**: copy character to X
- **$EAE5**: compare key count with last key count
- **$EAE7**: if this key = current key, key held, go test repeat
- **$EAE9**: set the repeat delay count
- **$EAEB**: save the repeat delay count
- **$EAEE**: go save key to buffer and exit, branch always
- **$EAF0**: clear b7
- **$EAF2**: test key repeat
- **$EAF5**: if repeat all go ??
- **$EAF7**: if repeat none go ??
- **$EAF9**: compare with end marker
- **$EAFB**: if $00/end marker go save key to buffer and exit
- **$EAFD**: compare with [INSERT]/[DELETE]
- **$EAFF**: if [INSERT]/[DELETE] go test for repeat
- **$EB01**: compare with [SPACE]
- **$EB03**: if [SPACE] go test for repeat
- **$EB05**: compare with [CURSOR RIGHT]
- **$EB07**: if [CURSOR RIGHT] go test for repeat
- **$EB09**: compare with [CURSOR DOWN]
- **$EB0B**: if not [CURSOR DOWN] just exit was one of the cursor movement keys, insert/delete key or the space bar so always do repeat tests
- **$EB0D**: get the repeat delay counter
- **$EB10**: if delay expired go ??
- **$EB12**: else decrement repeat delay counter
- **$EB15**: if delay not expired go ?? repeat delay counter has expired
- **$EB17**: decrement the repeat speed counter
- **$EB1A**: branch if repeat speed count not expired
- **$EB1C**: set for 4/60ths of a second
- **$EB1E**: save the repeat speed counter
- **$EB21**: get the keyboard buffer index
- **$EB23**: decrement it
- **$EB24**: if the buffer isn't empty just exit else repeat the key immediately possibly save the key to the keyboard buffer. if there was no key pressed or the key was not found during the scan (possibly due to key bounce) then X will be $FF here
- **$EB26**: get the key count
- **$EB28**: save it as the current key count
- **$EB2A**: get the keyboard shift/control/c= flag
- **$EB2D**: save it as last keyboard shift pattern
- **$EB30**: compare the character with the table end marker or no key
- **$EB32**: if it was the table end marker or no key just exit
- **$EB34**: copy the character to A
- **$EB35**: get the keyboard buffer index
- **$EB37**: compare it with the keyboard buffer size
- **$EB3A**: if the buffer is full just exit
- **$EB3C**: save the character to the keyboard buffer
- **$EB3F**: increment the index
- **$EB40**: save the keyboard buffer index
- **$EB42**: enable column 7 for the stop key
- **$EB44**: save VIA 1 DRA, keyboard column drive

### Commodore-64-intern-Buch (Commodore)
- **$EA89**: Shift/CTRL Flag rücksetzen
- **$EA8C**: $40 = keine Taste gedrückt
- **$EA8E**: Kode für gedrückte Taste
- **$EA90**: alle Bits des Port A löschen
- **$EA93**: Port B laden
- **$EA96**: keine Taste gedrückt ?
- **$EA98**: dann beenden
- **$EA9A**: Y-Register löschen
- **$EA9D**: $F5/$F6 = Zeiger auf
- **$EA9F**: Tastaturtabelle setzen
- **$EAA3**: erstes Bit für erste Matrixzeile löschen
- **$EAA5**: und in Port A schreiben
- **$EAA8**: 8 Matrixzeilen
- **$EAAA**: Bitstellung für Matrix retten
- **$EAAB**: Port B laden und
- **$EAAE**: Tastatur entprellen
- **$EAB1**: noch nicht entprellt ?
- **$EAB3**: Bits nacheinander ins Carry schieben
- **$EAB4**: '1' gleich nicht gedrückt
- **$EAB6**: Bitstelung retten
- **$EAB7**: ASCII-Kode aus Tabelle holen
- **$EAB9**: größer als 4, dann keine Control-Taste
- **$EABB**: verzweige bei größer/gleich 5
- **$EABD**: Kode für STOP-Taste ?
- **$EABF**: falls ja, dann verzweige
- **$EAC1**: entsprechendes Flag für SHIFT
- **$EAC4**: COMMOD.-Taste oder CTRL setzen
- **$EAC7**: unbedingter Sprung
- **$EAC9**: Nummer der Taste merken
- **$EACB**: Akku holen
- **$EACC**: Zähler für Taste erhöhen
- **$EACD**: schon alle Tasten?
- **$EACF**: wenn ja, verzweige
- **$EAD1**: nächste Matrix-Spalte
- **$EAD2**: unbedingter Sprung
- **$EAD4**: Carry setzen
- **$EAD5**: gespeicherte Bitfolge holen
- **$EAD6**: verschieben und
- **$EAD7**: in Port A schreiben
- **$EADA**: unbedingter Sprung
- **$EADC**: Stapel normalisieren
- **$EADD**: JMP $EB48 setzt Zeiger auf Tabelle
- **$EAE0**: Nummer der Taste
- **$EAE2**: ASCII-Wert aus Tabelle holen
- **$EAE4**: Tastenwert retten
- **$EAE5**: mit letzter Taste vergleichen
- **$EAE7**: verzweige wenn gleiche Taste
- **$EAE9**: Wert für Repeatverzögerung
- **$EAEB**: in Repeat-Verzögerungszähler
- **$EAEE**: unbedingter Sprung
- **$EAF0**: Bit 7 löschen
- **$EAF2**: Repeat-Funktion für alle Tasten ?
- **$EAF5**: Bit 7 gesetzt, dann alle Tasten wiederholen
- **$EAF7**: Bit 6 gesetzt, dann keine Wiederholung
- **$EAF9**: keine Taste?
- **$EAFB**: ja, dann verzweige
- **$EAFD**: 'DEL', 'INST' Kode
- **$EAFF**: wenn ja, verzweige
- **$EB01**: Leerzeichen
- **$EB03**: wenn ja, verzweige
- **$EB05**: Cursor right, left
- **$EB07**: wenn ja, verzweige
- **$EB09**: Cursor down, up
- **$EB0B**: verzweige wenn keine Taste zu wiederholen ist
- **$EB0D**: Repeatverzögerungszähler
- **$EB10**: wenn abgelaufen, so verzweige
- **$EB12**: herunterzählen
- **$EB15**: 0? nein dann verzweige
- **$EB17**: Repeatgeschwindigkeitszähler
- **$EB1A**: 0? nein dann verzweige
- **$EB1C**: Repeatgeschwindigkeits-
- **$EB1E**: zähler neu setzen
- **$EB21**: Anzahl der Zeichen im Tastaturpuffer
- **$EB23**: herunterzählen
- **$EB24**: mehr als ein Zeichen im Puffer, dann ignorieren
- **$EB26**: Tastennummermatrixcode
- **$EB28**: umspeichern
- **$EB2A**: sowie die Flags für SHIFT
- **$EB2D**: COMMOD.-Taste und CTRL
- **$EB30**: Tastatur-Kode ungültig ?
- **$EB32**: ja, dann ignorieren
- **$EB34**: gerettete Taste wieder holen
- **$EB35**: Anzahl der Zeichen im Tastaturpuffer
- **$EB37**: mit Haximalzahl vergleichen
- **$EB3A**: Puffer voll, dann Zeichen ignorieren
- **$EB3C**: Zeichen in Tastaturpuffer schreiben
- **$EB3F**: Zeichenanzahl erhöhen und
- **$EB40**: abspeichern
- **$EB42**: Tastatur-Matrix Abfrage
- **$EB44**: auf Normalwert
- **$EB47**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$EAFD**: delete
- **$EB01**: space
- **$EB05**: csr right/left
- **$EB09**: csr up/down

### Magnus Nyman (Magnus Nyman)
- **$EA89**: clear SHFLAG
- **$EA90**: store in keyboard write register
- **$EA93**: keyboard read register
- **$EA96**: no key pressed
- **$EA98**: skip
- **$EA9B**: point KEYTAB vector to $eb81
- **$EAA3**: bit0 = 0
- **$EAA5**: will test first row in matrix
- **$EAA8**: scan 8 rows in matrix
- **$EAAA**: temp store
- **$EAAB**: read
- **$EAAE**: wait for value to settle (key bouncing)
- **$EAB3**: test bit0
- **$EAB4**: no key pressed
- **$EAB7**: get key from KEYTAB
- **$EAB9**: value less than 5
- **$EABB**: nope
- **$EABD**: value = 3
- **$EABF**: nope
- **$EAC4**: store in SHFLAG
- **$EAC9**: store keynumber we pressed in SFDX
- **$EACC**: key counter
- **$EACD**: all 64 keys (8*8)
- **$EACF**: jump if ready
- **$EAD1**: next key in row
- **$EAD2**: row ready
- **$EAD4**: prepare for rol
- **$EAD6**: next row
- **$EAD7**: store bit
- **$EADA**: always jump
- **$EADC**: clean up

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*