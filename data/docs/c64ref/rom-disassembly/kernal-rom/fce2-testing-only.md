---
title: ; TESTING ONLY
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
- 0000-d6510
- 0001-r6510
- '0002'
- 0022-index
- 0055-size
- 0068-bits
- 0090-status
- 009d-msgflg
- 00a0-time
- 00a5-count
- 00a7-inbit
- 00a8-bitci
- 00b2-tape1
- 00b5-nxtbit
- 00b7-fnlen
- 00bb-fnadr
- 00c1-tmp0
- 00c3-tmp2
- 00d7-data
- 00f3-user
- 0200-buf
- 0281-memstr
- 0283-memsiz
- 0285-timout
- 0288-hibase
- 0295-m51ajb
- 0297-rsstat
- 0298-bitnum
- 0299-baudof
- 02a1-enabl
- 02a6-palnts
- 0300-ierror
- 0314-cinv
- 0316-cbinv
- 0318-nminv
- 031a-iopen
- 031c-iclose
- 031e-ichkin
- 0320-ickout
- 0322-iclrch
- 0324-ibasin
- 0326-ibsout
- 0328-istop
- 032a-igetin
- 032c-iclall
- 032e-usrcmd
- 033c-tbuffr
- a000-start-of-the-rom
- acptr
- adc
- basin
- bcc
- bcs
- beq
- bit
- bmi
- bne
- bpl
- brk
- bsout
- check
- chkin
- cint
- ciout
- ckout
- clall
- clc
- cld
- clear
- cli
- close
- clrch
- cmp
- dex
- dey
- e447-vectors
- ece7-load
- enable
- eor
- f07d-handshake
- f13e-getin
- f34a-open
- f5ed-save
- fce2-reset
- fd02-prft-auf-rom-in-8000
- fd10-cbm80
- fd10-rom-modul-identifizierung
- fd15-setzenholen
- fd1a-vector-kernal-move
- fd30-und-io-vektoren
- fd50-arbeitsspei-initialisieren
- fd9b-irq-vektoren
- fda3-interrupt-initialisierung
- fddd-enable-timer
- fdf9-parameter-f-filenamen-setzen
- fe00-file-setzen
- fe07-status-holen
- fe18-meldungen-setzen
- fe1a-read-st
- fe1c-status-setzen
- fe21-timeout-flag-fr-iec-setzen
- fe25-basic-ram-holensetzen
- fe27-read-the-top-of-memory
- fe2d-set-the-top-of-memory
- fe34-basic-ram-holensetzen
- fe43-nmi-einsprung
- fe47-standard-nmi-routine
- fe66-warm-start-basic
- fe72-nmi-routine-fr-rs-232
- fec2-ntsc-version
- fed6-eingabe
- ff07-nmi-routine-rs-232-ausgabe
- ff2e-ermitteln
- ff41-unused-bytes
- ff43-einsprung-aus-bandroutine
- ff47
- ff48-irq-einsprung
- ff4a
- ff4d
- ff53
- ff5b-video-reset
- ff81-betriebssystem-routinen
- ff84-initialise-sid-cia-and-irq-unused
- ff87-ram-test-and-find-ram-end
- ff8a-restore-default-io-vectors
- ff8d-readset-vectored-io
- ff90-control-kernal-messages
- ff93-send-secondary-address-after-listen
- ff96-send-secondary-address-after-talk
- ff99-readset-the-top-of-memory
- ff9c-readset-the-bottom-of-memory
- ff9f-scan-the-keyboard
- ffa2-set-timeout-on-serial-bus
- ffa5-input-byte-from-serial-bus
- ffa8-output-a-byte-to-serial-bus
- ffab-command-serial-bus-to-untalk
- ffae-command-serial-bus-to-unlisten
- ffb1-command-devices-on-the-serial-bus-to-listen
- ffb4-command-serial-bus-device-to-talk
- ffb7-read-io-status-word
- ffba-set-logical-first-and-second-addresses
- ffbd-set-the-filename
- ffc0-open-a-logical-file
- ffc3-close-a-specified-logical-file
- ffc6-open-channel-for-input
- ffc9-open-channel-for-output
- ffcc-close-input-and-output-channels
- ffcf-input-character-from-channel
- ffd2-output-character-to-channel
- ffd5-load-ram-from-a-device
- ffd8-save-ram-to-a-device
- ffdb-set-the-real-time-clock
- ffde-read-the-real-time-clock
- ffe1-scan-the-stop-key
- ffe4-get-character-from-input-device
- ffe7-close-all-channels-and-files
- ffea-increment-real-time-clock
- ffed-return-xy-organization-of-screen
- fff0-readset-xy-cursor-position
- fff3-return-the-base-address-of-the-io-devices
- fff6-unused
- fffa-hardware-vektoren
- inc
- input
- iny
- iobase
- ioinit
- jmp
- jsr
- lda
- ldx
- ldy
- listen
- manage
- membot
- memory
- memtop
- nop
- ora
- output
- pha
- php
- pla
- plot
- ramtas
- rdtim
- readst
- restor
- return
- rol
- rti
- rts
- sbc
- scnkey
- screen
- sei
- setlfs
- setmsg
- setnam
- settim
- settmo
- sta
- stop
- stx
- sty
- system
- talk
- tax
- tay
- tksa
- tsx
- txa
- txs
- tya
- udtim
- unlsn
- untalk
- untlk
- update
- vector
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FCE2
  address_end: $FFFE
  symbol: testing-only
  sources:
  - name: Original Disassembly
    author: Commodore
    description: '- **$FCE2**: START  LDX #$FF'
  - name: Original Disassembly
    author: —
    description: '- **$FCE2**: set X for stack'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FCE2**: Wert für Stapelzeiger'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FCEC**: start cartridge'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FCE5**: Set stackpointer to #ff'
---

# $FCE2 — ; TESTING ONLY

## Disassemblatura
```assembly
.FCE2  A2 FF    LDX #$FF   ; START  LDX #$FF
.FCE4  78       SEI   ; SEI
.FCE5  9A       TXS   ; TXS
.FCE6  D8       CLD   ; CLD
.FCE7  20 02 FD JSR $FD02   ; JSR A0INT       ;TEST FOR $A0 ROM IN
.FCEA  D0 03    BNE $FCEF   ; BNE START1
.FCEC  6C 00 80 JMP ($8000)   ; JMP ($8000)     ; GO INIT AS $A000 ROM WANTS
.FCEF  8E 16 D0 STX $D016   ; START1 STX VICREG+22   ;SET UP REFRESH (.X=<5)
.FCF2  20 A3 FD JSR $FDA3   ; JSR IOINIT      ;GO INITILIZE I/O DEVICES
.FCF5  20 50 FD JSR $FD50   ; JSR RAMTAS      ;GO RAM TEST AND SET
.FCF8  20 15 FD JSR $FD15   ; JSR RESTOR      ;GO SET UP OS VECTORS ;
.FCFB  20 5B FF JSR $FF5B   ; JSR CINT        ;GO INITILIZE SCREEN
.FCFE  58       CLI   ; CLI             ;INTERRUPTS OKAY NOW
.FCFF  6C 00 A0 JMP ($A000)   ; JMP ($A000)     ;GO TO BASIC SYSTEM ; A0INT - TEST FOR AN $8000 ROM ;  RETURNS Z - $8000 IN ;
.FD02  A2 05    LDX #$05   ; A0INT  LDX #TBLA0E-TBLA0R ;CHECK FOR $8000
.FD04  BD 0F FD LDA $FD0F,X   ; A0IN1  LDA TBLA0R-1,X
.FD07  DD 03 80 CMP $8003,X   ; CMP $8004-1,X
.FD0A  D0 03    BNE $FD0F   ; BNE A0IN2
.FD0C  CA       DEX   ; DEX
.FD0D  D0 F5    BNE $FD04   ; BNE A0IN1
.FD0F  60       RTS   ; A0IN2  RTS ;
.FD10  C3 C2 CD 38 30   ; TBLA0R .BYT $C3,$C2,$CD,'80' ;..CBM80.. TBLA0E ; RESTOR - SET KERNAL INDIRECTS AND VECTORS (SYSTEM) ;
.FD15  A2 30    LDX #$30   ; RESTOR LDX #<VECTSS
.FD17  A0 FD    LDY #$FD   ; LDY #>VECTSS
.FD19  18       CLC   ; CLC ; ; VECTOR - SET KERNAL INDIRECT AND VECTORS (USER) ;
.FD1A  86 C3    STX $C3   ; VECTOR STX TMP2
.FD1C  84 C4    STY $C4   ; STY TMP2+1
.FD1E  A0 1F    LDY #$1F   ; LDY #VECTSE-VECTSS-1
.FD20  B9 14 03 LDA $0314,Y   ; MOVOS1 LDA CINV,Y      ;GET FROM STORAGE
.FD23  B0 02    BCS $FD27   ; BCS MOVOS2      ;C...WANT STORAGE TO USER
.FD25  B1 C3    LDA ($C3),Y   ; LDA (TMP2)Y     ;...WANT USER TO STORAGE
.FD27  91 C3    STA ($C3),Y   ; MOVOS2 STA (TMP2)Y     ;PUT IN USER
.FD29  99 14 03 STA $0314,Y   ; STA CINV,Y      ;PUT IN STORAGE
.FD2C  88       DEY   ; DEY
.FD2D  10 F1    BPL $FD20   ; BPL MOVOS1
.FD2F  60       RTS   ; RTS ; VECTSS .WOR KEY,TIMB,NNMI .WOR   NOPEN,NCLOSE,NCHKIN .WOR   NCKOUT,NCLRCH,NBASIN .WOR   NBSOUT,NSTOP,NGETIN .WOR   NCLALL,TIMB     ;GOTO BREAK ON A USRCMD JMP
.FD30  31 EA 66 FE 47 FE 4A F3   ; .WOR   NLOAD,NSAVE VECTSE ; RAMTAS - MEMORY SIZE CHECK AND SET ;
.FD50  A9 00    LDA #$00   ; RAMTAS LDA #0          ;ZERO LOW MEMORY
.FD52  A8       TAY   ; TAY             ;START AT 0002
.FD53  99 02 00 STA $0002,Y   ; RAMTZ0 STA $0002,Y     ;ZERO PAGE
.FD56  99 00 02 STA $0200,Y   ; STA $0200,Y     ;USER BUFFERS AND VARS
.FD59  99 00 03 STA $0300,Y   ; STA $0300,Y     ;SYSTEM SPACE AND USER SPACE
.FD5C  C8       INY   ; INY
.FD5D  D0 F4    BNE $FD53   ; BNE RAMTZ0 ; ;ALLOCATE TAPE BUFFERS ;
.FD5F  A2 3C    LDX #$3C   ; LDX #<TBUFFR
.FD61  A0 03    LDY #$03   ; LDY #>TBUFFR
.FD63  86 B2    STX $B2   ; STX TAPE1
.FD65  84 B3    STY $B3   ; STY TAPE1+1 ; ; SET TOP OF MEMORY ; RAMTBT
.FD67  A8       TAY   ; TAY             ;MOVE $00 TO .Y
.FD68  A9 03    LDA #$03   ; LDA #3          ;SET HIGH INITAL INDEX
.FD6A  85 C2    STA $C2   ; STA TMP0+1 ;
.FD6C  E6 C2    INC $C2   ; RAMTZ1 INC TMP0+1      ;MOVE INDEX THRU MEMORY
.FD6E  B1 C1    LDA ($C1),Y   ; RAMTZ2 LDA (TMP0)Y     ;GET PRESENT DATA
.FD70  AA       TAX   ; TAX             ;SAVE IN .X
.FD71  A9 55    LDA #$55   ; LDA #$55        ;DO A $55,$AA TEST
.FD73  91 C1    STA ($C1),Y   ; STA (TMP0)Y
.FD75  D1 C1    CMP ($C1),Y   ; CMP (TMP0)Y
.FD77  D0 0F    BNE $FD88   ; BNE SIZE
.FD79  2A       ROL   ; ROL A
.FD7A  91 C1    STA ($C1),Y   ; STA (TMP0)Y
.FD7C  D1 C1    CMP ($C1),Y   ; CMP (TMP0)Y
.FD7E  D0 08    BNE $FD88   ; BNE SIZE
.FD80  8A       TXA   ; TXA             ;RESTORE OLD DATA
.FD81  91 C1    STA ($C1),Y   ; STA (TMP0)Y
.FD83  C8       INY   ; INY
.FD84  D0 E8    BNE $FD6E   ; BNE RAMTZ2
.FD86  F0 E4    BEQ $FD6C   ; BEQ RAMTZ1 ;
.FD88  98       TYA   ; SIZE   TYA             ;SET TOP OF MEMORY
.FD89  AA       TAX   ; TAX
.FD8A  A4 C2    LDY $C2   ; LDY TMP0+1
.FD8C  18       CLC   ; CLC
.FD8D  20 2D FE JSR $FE2D   ; JSR SETTOP
.FD90  A9 08    LDA #$08   ; LDA #$08        ;SET BOTTOM OF MEMORY
.FD92  8D 82 02 STA $0282   ; STA MEMSTR+1    ;ALWAYS AT $0800
.FD95  A9 04    LDA #$04   ; LDA #$04        ;SCREEN ALWAYS AT $400
.FD97  8D 88 02 STA $0288   ; STA HIBASE      ;SET BASE OF SCREEN
.FD9A  60       RTS   ; RTS
.FD9B  6A FC CD FB 31 EA 2C F9   ; BSIT   .WOR WRTZ,WRTN,KEY,READ ;TABLE OF INDIRECTS FOR CASSETTE IRQ'S ; IOINIT - INITILIZE IO DEVICES ;
.FDA3  A9 7F    LDA #$7F   ; IOINIT LDA #$7F        ;KILL INTERRUPTS
.FDA5  8D 0D DC STA $DC0D   ; STA D1ICR
.FDA8  8D 0D DD STA $DD0D   ; STA D2ICR
.FDAB  8D 00 DC STA $DC00   ; STA D1PRA       ;TURN ON STOP KEY
.FDAE  A9 08    LDA #$08   ; LDA #%00001000  ;SHUT OFF TIMERS
.FDB0  8D 0E DC STA $DC0E   ; STA D1CRA
.FDB3  8D 0E DD STA $DD0E   ; STA D2CRA
.FDB6  8D 0F DC STA $DC0F   ; STA D1CRB
.FDB9  8D 0F DD STA $DD0F   ; STA D2CRB ; CONFIGURE PORTS
.FDBC  A2 00    LDX #$00   ; LDX #$00        ;SET UP KEYBOARD INPUTS
.FDBE  8E 03 DC STX $DC03   ; STX D1DDRB      ;KEYBOARD INPUTS
.FDC1  8E 03 DD STX $DD03   ; STX D2DDRB      ;USER PORT (NO RS-232)
.FDC4  8E 18 D4 STX $D418   ; STX SIDREG+24   ;TURN OFF SID
.FDC7  CA       DEX   ; DEX
.FDC8  8E 02 DC STX $DC02   ; STX D1DDRA      ;KEYBOARD OUTPUTS
.FDCB  A9 07    LDA #$07   ; LDA #%00000111  ;SET SERIAL/VA14/15 (CLKHI)
.FDCD  8D 00 DD STA $DD00   ; STA D2PRA
.FDD0  A9 3F    LDA #$3F   ; LDA #%00111111  ;SET SERIAL IN/OUT, VA14/15OUT
.FDD2  8D 02 DD STA $DD02   ; STA D2DDRA ; ; SET UP THE 6510 LINES ;
.FDD5  A9 E7    LDA #$E7   ; LDA #%11100111  ;MOTOR ON, HIRAM LOWRAM CHAREN HIGH
.FDD7  85 01    STA $01   ; STA R6510
.FDD9  A9 2F    LDA #$2F   ; LDA #%00101111  ;MTR OUT,SW IN,WR OUT,CONTROL OUT
.FDDB  85 00    STA $00   ; STA D6510
.FDDD  AD A6 02 LDA $02A6   ; IOKEYS LDA PALNTS      ;PAL OR NTSC
.FDE0  F0 0A    BEQ $FDEC   ; BEQ I0010       ;NTSC
.FDE2  A9 25    LDA #$25   ; LDA #<SIXTYP
.FDE4  8D 04 DC STA $DC04   ; STA D1T1L
.FDE7  A9 40    LDA #$40   ; LDA #>SIXTYP
.FDE9  4C F3 FD JMP $FDF3   ; JMP I0020
.FDEC  A9 95    LDA #$95   ; I0010  LDA #<SIXTY     ;KEYBOARD SCAN IRQ'S
.FDEE  8D 04 DC STA $DC04   ; STA D1T1L
.FDF1  A9 42    LDA #$42   ; LDA #>SIXTY
.FDF3  8D 05 DC STA $DC05   ; I0020  STA D1T1H
.FDF6  4C 6E FF JMP $FF6E   ; JMP PIOKEY ; LDA #$81 ;ENABLE T1 IRQ'S ; STA D1ICR ; LDA D1CRA ; AND #$80 ;SAVE ONLY TOD BIT ; ORA #%00010001 ;ENABLE TIMER1 ; STA D1CRA ; JMP CLKLO ;RELEASE THE CLOCK LINE ; ; SIXTY HERTZ VALUE ; SIXTY  = 16667
.FDF9  85 B7    STA $B7   ; SETNAM STA FNLEN
.FDFB  86 BB    STX $BB   ; STX    FNADR
.FDFD  84 BC    STY $BC   ; STY    FNADR+1
.FDFF  60       RTS   ; RTS
.FE00  85 B8    STA $B8   ; SETLFS STA LA
.FE02  86 BA    STX $BA   ; STX    FA
.FE04  84 B9    STY $B9   ; STY    SA
.FE06  60       RTS   ; RTS
.FE07  A5 BA    LDA $BA   ; READSS LDA FA          ;SEE WHICH DEVICES' TO READ
.FE09  C9 02    CMP #$02   ; CMP #2          ;IS IT RS-232?
.FE0B  D0 0D    BNE $FE1A   ; BNE READST      ;NO...READ SERIAL/CASS
.FE0D  AD 97 02 LDA $0297   ; LDA RSSTAT      ;YES...GET RS-232 UP
.FE10  48       PHA   ; PHA
.FE11  A9 00    LDA #$00   ; LDA #00         ;CLEAR RS232 STATUS WHEN READ
.FE13  8D 97 02 STA $0297   ; STA RSSTAT
.FE16  68       PLA   ; PLA
.FE17  60       RTS   ; RTS
.FE18  85 9D    STA $9D   ; SETMSG STA MSGFLG
.FE1A  A5 90    LDA $90   ; READST LDA STATUS
.FE1C  05 90    ORA $90   ; UDST   ORA STATUS
.FE1E  85 90    STA $90   ; STA    STATUS
.FE20  60       RTS   ; RTS
.FE21  8D 85 02 STA $0285   ; SETTMO STA TIMOUT
.FE24  60       RTS   ; RTS
.FE25  90 06    BCC $FE2D   ; MEMTOP BCC SETTOP ; ;CARRY SET--READ TOP OF MEMORY ;
.FE27  AE 83 02 LDX $0283   ; GETTOP LDX MEMSIZ
.FE2A  AC 84 02 LDY $0284   ; LDY    MEMSIZ+1 ; ;CARRY CLEAR--SET TOP OF MEMORY ;
.FE2D  8E 83 02 STX $0283   ; SETTOP STX MEMSIZ
.FE30  8C 84 02 STY $0284   ; STY    MEMSIZ+1
.FE33  60       RTS   ; RTS ;MANAGE BOTTOM OF MEMORY ;
.FE34  90 06    BCC $FE3C   ; MEMBOT BCC SETBOT ; ;CARRY SET--READ BOTTOM OF MEMORY ;
.FE36  AE 81 02 LDX $0281   ; LDX    MEMSTR
.FE39  AC 82 02 LDY $0282   ; LDY    MEMSTR+1 ; ;CARRY CLEAR--SET BOTTOM OF MEMORY ;
.FE3C  8E 81 02 STX $0281   ; SETBOT STX MEMSTR
.FE3F  8C 82 02 STY $0282   ; STY    MEMSTR+1
.FE42  60       RTS   ; RTS .END .LIB   RS232NMI
.FE43  78       SEI   ; NMI    SEI             ;NO IRQ'S ALLOWED...
.FE44  6C 18 03 JMP ($0318)   ; JMP (NMINV)     ;...COULD MESS UP CASSETTES
.FE47  48       PHA   ; NNMI   PHA
.FE48  8A       TXA   ; TXA
.FE49  48       PHA   ; PHA
.FE4A  98       TYA   ; TYA
.FE4B  48       PHA   ; PHA
.FE4C  A9 7F    LDA #$7F   ; NNMI10 LDA #$7F        ;DISABLE ALL NMI'S
.FE4E  8D 0D DD STA $DD0D   ; STA D2ICR
.FE51  AC 0D DD LDY $DD0D   ; LDY D2ICR       ;CHECK IF REAL NMI...
.FE54  30 1C    BMI $FE72   ; BMI NNMI20      ;NO...RS232/OTHER ;
.FE56  20 02 FD JSR $FD02   ; NNMI18 JSR A0INT       ;CHECK IF $A0 IN...NO .Y
.FE59  D0 03    BNE $FE5E   ; BNE NNMI19      ;...NO
.FE5B  6C 02 80 JMP ($8002)   ; JMP ($8002)     ;...YES ; ; CHECK FOR STOP KEY DOWN ; NNMI19
.FE5E  20 BC F6 JSR $F6BC   ; JSR UD60        ;NO .Y
.FE61  20 E1 FF JSR $FFE1   ; JSR STOP        ;NO .Y
.FE64  D0 0C    BNE $FE72   ; BNE NNMI20      ;NO STOP KEY...TEST FOR RS232 ; ; TIMB - WHERE SYSTEM GOES ON A BRK INSTRUCTION ;
.FE66  20 15 FD JSR $FD15   ; TIMB   JSR RESTOR      ;RESTORE SYSTEM INDIRECTS
.FE69  20 A3 FD JSR $FDA3   ; JSR IOINIT      ;RESTORE I/O FOR BASIC
.FE6C  20 18 E5 JSR $E518   ; JSR CINT        ;RESTORE SCREEN FOR BASIC
.FE6F  6C 02 A0 JMP ($A002)   ; JMP ($A002)     ;...NO, SO BASIC WARM START ; DISABLE NMI'S UNTILL READY ;  SAVE ON STACK ;
.FE72  98       TYA   ; NNMI20 TYA             ;.Y SAVED THROUGH RESTORE
.FE73  2D A1 02 AND $02A1   ; AND ENABL       ;SHOW ONLY ENABLES
.FE76  AA       TAX   ; TAX             ;SAVE IN .X FOR LATTER ; ; T1 NMI CHECK - TRANSMITT A BIT ;
.FE77  29 01    AND #$01   ; AND #$01        ;CHECK FOR T1
.FE79  F0 28    BEQ $FEA3   ; BEQ NNMI30      ;NO... ;
.FE7B  AD 00 DD LDA $DD00   ; LDA D2PRA
.FE7E  29 FB    AND #$FB   ; AND #$FF-$04    ;FIX FOR CURRENT I/O
.FE80  05 B5    ORA $B5   ; ORA NXTBIT      ;LOAD DATA AND...
.FE82  8D 00 DD STA $DD00   ; STA D2PRA       ;...SEND IT ;
.FE85  AD A1 02 LDA $02A1   ; LDA ENABL       ;RESTORE NMI'S
.FE88  8D 0D DD STA $DD0D   ; STA D2ICR       ;READY FOR NEXT... ; ; BECAUSE OF 6526 ICR STRUCTURE... ;  HANDLE ANOTHER NMI AS A SUBROUTINE ;
.FE8B  8A       TXA   ; TXA             ;TEST FOR ANOTHER NMI
.FE8C  29 12    AND #$12   ; AND #$12        ;TEST FOR T2 OR FLAG
.FE8E  F0 0D    BEQ $FE9D   ; BEQ NNMI25
.FE90  29 02    AND #$02   ; AND #$02        ;CHECK FOR T2
.FE92  F0 06    BEQ $FE9A   ; BEQ NNMI22      ;MUST BE A FLAG ;
.FE94  20 D6 FE JSR $FED6   ; JSR T2NMI       ;HANDLE A NORMAL BIT IN...
.FE97  4C 9D FE JMP $FE9D   ; JMP NNMI25      ;...THEN CONTINUE OUTPUT ;
.FE9A  20 07 FF JSR $FF07   ; NNMI22 JSR FLNMI       ;HANDLE A START BIT... ;
.FE9D  20 BB EE JSR $EEBB   ; NNMI25 JSR RSTRAB      ;GO CALC INFO (CODE COULD BE IN LINE)
.FEA0  4C B6 FE JMP $FEB6   ; JMP NMIRTI ; ; T2 NMI CHECK - RECIEVE A BIT ;
.FEA3  8A       TXA   ; NNMI30 TXA
.FEA4  29 02    AND #$02   ; AND #$02        ;MASK TO T2
.FEA6  F0 06    BEQ $FEAE   ; BEQ NNMI40      ;NO... ;
.FEA8  20 D6 FE JSR $FED6   ; JSR T2NMI       ;HANDLE INTERRUPT
.FEAB  4C B6 FE JMP $FEB6   ; JMP NMIRTI ; FLAG NMI HANDLER - RECIEVE A START BIT ;
.FEAE  8A       TXA   ; NNMI40 TXA             ;CHECK FOR EDGE
.FEAF  29 10    AND #$10   ; AND #$10        ;ON FLAG...
.FEB1  F0 03    BEQ $FEB6   ; BEQ NMIRTI      ;NO... ;
.FEB3  20 07 FF JSR $FF07   ; JSR FLNMI       ;START BIT ROUTINE
.FEB6  AD A1 02 LDA $02A1   ; NMIRTI LDA ENABL       ;RESTORE NMI'S
.FEB9  8D 0D DD STA $DD0D   ; STA D2ICR
.FEBC  68       PLA   ; PREND  PLA             ;BECAUSE OF MISSING SCREEN EDITOR
.FEBD  A8       TAY   ; TAY
.FEBE  68       PLA   ; PLA
.FEBF  AA       TAX   ; TAX
.FEC0  68       PLA   ; PLA
.FEC1  40       RTI   ; RTI ; BAUDO TABLE CONTAINS VALUES ;  FOR 1E6/BAUD RATE/2 ;
.FEC2  C1 27   ; BAUDO  .WOR 10000-CBIT ; 50 BAUD
.FEC4  3E 1A   ; .WOR 6667-CBIT  ;   75   BAUD
.FEC6  C5 11   ; .WOR 4545-CBIT  ;  110   BAUD
.FEC8  74 0E   ; .WOR 3715-CBIT  ;  134.6 BAUD
.FECA  ED 0C   ; .WOR 3333-CBIT  ;  150   BAUD
.FECC  45 06   ; .WOR 1667-CBIT  ;  300   BAUD
.FECE  F0 02   ; .WOR 833-CBIT   ;  600   BAUD
.FED0  46 01   ; .WOR 417-CBIT   ; 1200   BAUD
.FED2  B8 00   ; .WOR 278-CBIT   ; 1800   BAUD
.FED4  71 00   ; .WOR 208-CBIT   ; 2400   BAUD ; ; CBIT - AN ADJUSTMENT TO MAKE NEXT T2 HIT NEAR CENTER ;   OF THE NEXT BIT. ;   APROX THE TIME TO SERVICE A CB1 NMI CBIT   =100            ;CYCLES ; T2NMI - SUBROUTINE TO HANDLE AN RS232 ;  BIT INPUT. ;
.FED6  AD 01 DD LDA $DD01   ; T2NMI  LDA D2PRB       ;GET DATA IN
.FED9  29 01    AND #$01   ; AND #01         ;MASK OFF...
.FEDB  85 A7    STA $A7   ; STA INBIT       ;...SAVE FOR LATTER ; ; UPDATE T2 FOR MID BIT CHECK ;   (WORST CASE <213 CYCLES TO HERE) ;   (CALC 125 CYCLES+43-66 DEAD) ;
.FEDD  AD 06 DD LDA $DD06   ; LDA D2T2L       ;CALC NEW TIME & CLR NMI
.FEE0  E9 1C    SBC #$1C   ; SBC #22+6
.FEE2  6D 99 02 ADC $0299   ; ADC BAUDOF
.FEE5  8D 06 DD STA $DD06   ; STA D2T2L
.FEE8  AD 07 DD LDA $DD07   ; LDA D2T2H
.FEEB  6D 9A 02 ADC $029A   ; ADC BAUDOF+1
.FEEE  8D 07 DD STA $DD07   ; STA D2T2H ;
.FEF1  A9 11    LDA #$11   ; LDA #$11        ;ENABLE TIMER
.FEF3  8D 0F DD STA $DD0F   ; STA D2CRB ;
.FEF6  AD A1 02 LDA $02A1   ; LDA ENABL       ;RESTORE NMI'S EARLY...
.FEF9  8D 0D DD STA $DD0D   ; STA D2ICR ;
.FEFC  A9 FF    LDA #$FF   ; LDA #$FF        ;ENABLE COUNT FROM $FFFF
.FEFE  8D 06 DD STA $DD06   ; STA D2T2L
.FF01  8D 07 DD STA $DD07   ; STA D2T2H ;
.FF04  4C 59 EF JMP $EF59   ; JMP RSRCVR      ;GO SHIFT IN... FLNMI ; ; GET HALF BIT RATE VALUE ;
.FF07  AD 95 02 LDA $0295   ; LDA M51AJB
.FF0A  8D 06 DD STA $DD06   ; STA D2T2L
.FF0D  AD 96 02 LDA $0296   ; LDA M51AJB+1
.FF10  8D 07 DD STA $DD07   ; STA D2T2H ;
.FF13  A9 11    LDA #$11   ; LDA #$11        ;ENABLE TIMER
.FF15  8D 0F DD STA $DD0F   ; STA D2CRB ;
.FF18  A9 12    LDA #$12   ; LDA #$12        ;DISABLE FLAG, ENABLE T2
.FF1A  4D A1 02 EOR $02A1   ; EOR ENABL
.FF1D  8D A1 02 STA $02A1   ; STA ENABL ;ORA #$82 ;STA D2ICR ;
.FF20  A9 FF    LDA #$FF   ; LDA #$FF        ;PRESET FOR COUNT DOWN
.FF22  8D 06 DD STA $DD06   ; STA D2T2L
.FF25  8D 07 DD STA $DD07   ; STA D2T2H ;
.FF28  AE 98 02 LDX $0298   ; LDX BITNUM      ;GET #OF BITS IN
.FF2B  86 A8    STX $A8   ; STX BITCI       ;PUT IN RCVRCNT
.FF2D  60       RTS   ; RTS ; ; POPEN - PATCHES OPEN RS232 FOR UNIVERSAL KERNAL ;
.FF2E  AA       TAX   ; POPEN  TAX             ;WE'RE CALCULATING BAUD RATE
.FF2F  AD 96 02 LDA $0296   ; LDA M51AJB+1    ; M51AJB=FREQ/BAUD/2-100
.FF32  2A       ROL   ; ROL A
.FF33  A8       TAY   ; TAY
.FF34  8A       TXA   ; TXA
.FF35  69 C8    ADC #$C8   ; ADC #CBIT+CBIT
.FF37  8D 99 02 STA $0299   ; STA BAUDOF
.FF3A  98       TYA   ; TYA
.FF3B  69 00    ADC #$00   ; ADC #0
.FF3D  8D 9A 02 STA $029A   ; STA BAUDOF+1
.FF40  60       RTS   ; RTS
.FF41  EA       NOP   ; NOP
.FF42  EA       NOP   ; NOP .END .LIB   IRQFILE ; SIMIRQ - SIMULATE AN IRQ (FOR CASSETTE READ) ;  ENTER BY A JSR SIMIRQ ;
.FF43  08       PHP   ; SIMIRQ PHP
.FF44  68       PLA   ; PLA             ;FIX THE BREAK FLAG
.FF45  29 EF    AND #$EF   ; AND #$EF
.FF47  48       PHA   ; PHA ; PULS - CHECKS FOR REAL IRQ'S OR BREAKS ;
.FF48  48       PHA   ; PULS   PHA
.FF49  8A       TXA   ; TXA
.FF4A  48       PHA   ; PHA
.FF4B  98       TYA   ; TYA
.FF4C  48       PHA   ; PHA
.FF4D  BA       TSX   ; TSX
.FF4E  BD 04 01 LDA $0104,X   ; LDA $104,X      ;GET OLD P STATUS
.FF51  29 10    AND #$10   ; AND #$10        ;BREAK FLAG?
.FF53  F0 03    BEQ $FF58   ; BEQ PULS1       ;...NO
.FF55  6C 16 03 JMP ($0316)   ; JMP (CBINV)     ;...YES...BREAK INSTR
.FF58  6C 14 03 JMP ($0314)   ; PULS1  JMP (CINV)      ;...IRQ .END .LIB   VECTORS
.FF5B  20 18 E5 JSR $E518   ; *=$FF8A-9
.FF81  4C 5B FF JMP $FF5B   ; JMP    CINT
.FF84  4C A3 FD JMP $FDA3   ; JMP    IOINIT
.FF87  4C 50 FD JMP $FD50   ; JMP    RAMTAS *=$FF8A                ;NEW VECTORS FOR BASIC
.FF8A  4C 15 FD JMP $FD15   ; JMP    RESTOR          ;RESTORE VECTORS TO INITIAL SYSTEM
.FF8D  4C 1A FD JMP $FD1A   ; JMP    VECTOR          ;CHANGE VECTORS FOR USER *      =$FF90
.FF90  4C 18 FE JMP $FE18   ; JMP    SETMSG          ;CONTROL O.S. MESSAGES
.FF93  4C B9 ED JMP $EDB9   ; JMP    SECND           ;SEND SA AFTER LISTEN
.FF96  4C C7 ED JMP $EDC7   ; JMP    TKSA            ;SEND SA AFTER TALK
.FF99  4C 25 FE JMP $FE25   ; JMP    MEMTOP          ;SET/READ TOP OF MEMORY
.FF9C  4C 34 FE JMP $FE34   ; JMP    MEMBOT          ;SET/READ BOTTOM OF MEMORY
.FF9F  4C 87 EA JMP $EA87   ; JMP    SCNKEY          ;SCAN KEYBOARD
.FFA2  4C 21 FE JMP $FE21   ; JMP    SETTMO          ;SET TIMEOUT IN IEEE
.FFA5  4C 13 EE JMP $EE13   ; JMP    ACPTR           ;HANDSHAKE IEEE BYTE IN
.FFA8  4C DD ED JMP $EDDD   ; JMP    CIOUT           ;HANDSHAKE IEEE BYTE OUT
.FFAB  4C EF ED JMP $EDEF   ; JMP    UNTLK           ;SEND UNTALK OUT IEEE
.FFAE  4C FE ED JMP $EDFE   ; JMP    UNLSN           ;SEND UNLISTEN OUT IEEE
.FFB1  4C 0C ED JMP $ED0C   ; JMP    LISTN           ;SEND LISTEN OUT IEEE
.FFB4  4C 09 ED JMP $ED09   ; JMP    TALK            ;SEND TALK OUT IEEE
.FFB7  4C 07 FE JMP $FE07   ; JMP    READSS          ;RETURN I/O STATUS BYTE
.FFBA  4C 00 FE JMP $FE00   ; JMP    SETLFS          ;SET LA, FA, SA
.FFBD  4C F9 FD JMP $FDF9   ; JMP    SETNAM          ;SET LENGTH AND FN ADR
.FFC0  6C 1A 03 JMP ($031A)   ; OPEN   JMP (IOPEN)     ;OPEN LOGICAL FILE
.FFC3  6C 1C 03 JMP ($031C)   ; CLOSE  JMP (ICLOSE)    ;CLOSE LOGICAL FILE
.FFC6  6C 1E 03 JMP ($031E)   ; CHKIN  JMP (ICHKIN)    ;OPEN CHANNEL IN
.FFC9  6C 20 03 JMP ($0320)   ; CKOUT  JMP (ICKOUT)    ;OPEN CHANNEL OUT
.FFCC  6C 22 03 JMP ($0322)   ; CLRCH  JMP (ICLRCH)    ;CLOSE I/O CHANNEL
.FFCF  6C 24 03 JMP ($0324)   ; BASIN  JMP (IBASIN)    ;INPUT FROM CHANNEL
.FFD2  6C 26 03 JMP ($0326)   ; BSOUT  JMP (IBSOUT)    ;OUTPUT TO CHANNEL
.FFD5  4C 9E F4 JMP $F49E   ; JMP    LOADSP          ;LOAD FROM FILE
.FFD8  4C DD F5 JMP $F5DD   ; JMP    SAVESP          ;SAVE TO FILE
.FFDB  4C E4 F6 JMP $F6E4   ; JMP    SETTIM          ;SET INTERNAL CLOCK
.FFDE  4C DD F6 JMP $F6DD   ; JMP    RDTIM           ;READ INTERNAL CLOCK
.FFE1  6C 28 03 JMP ($0328)   ; STOP   JMP (ISTOP)     ;SCAN STOP KEY
.FFE4  6C 2A 03 JMP ($032A)   ; GETIN  JMP (IGETIN)    ;GET CHAR FROM Q
.FFE7  6C 2C 03 JMP ($032C)   ; CLALL  JMP (ICLALL)    ;CLOSE ALL FILES
.FFEA  4C 9B F6 JMP $F69B   ; JMP    UDTIM           ;INCREMENT CLOCK
.FFED  4C 05 E5 JMP $E505   ; JSCROG JMP SCRORG      ;SCREEN ORG
.FFF0  4C 0A E5 JMP $E50A   ; JPLOT  JMP PLOT        ;READ/SET X,Y COORD
.FFF3  4C 00 E5 JMP $E500   ; JIOBAS JMP IOBASE      ;RETURN I/O BASE
.FFF6  52 52 42 59   ; *=$FFFA
.FFFA  43 FE   ; .WOR   NMI             ;PROGRAM DEFINEABLE
.FFFC  E2 FC   ; .WOR   START           ;INITIALIZATION CODE
.FFFE  48 FF   ; .WOR   PULS            ;INTERRUPT HANDLER
```


## Commenti

### Original Disassembly (Commodore)
- **$FCE2**: START  LDX #$FF
- **$FCE4**: SEI
- **$FCE5**: TXS
- **$FCE6**: CLD
- **$FCE7**: JSR A0INT       ;TEST FOR $A0 ROM IN
- **$FCEA**: BNE START1
- **$FCEC**: JMP ($8000)     ; GO INIT AS $A000 ROM WANTS
- **$FCEF**: START1 STX VICREG+22   ;SET UP REFRESH (.X=<5)
- **$FCF2**: JSR IOINIT      ;GO INITILIZE I/O DEVICES
- **$FCF5**: JSR RAMTAS      ;GO RAM TEST AND SET
- **$FCF8**: JSR RESTOR      ;GO SET UP OS VECTORS ;
- **$FCFB**: JSR CINT        ;GO INITILIZE SCREEN
- **$FCFE**: CLI             ;INTERRUPTS OKAY NOW
- **$FCFF**: JMP ($A000)     ;GO TO BASIC SYSTEM ; A0INT - TEST FOR AN $8000 ROM ;  RETURNS Z - $8000 IN ;
- **$FD02**: A0INT  LDX #TBLA0E-TBLA0R ;CHECK FOR $8000
- **$FD04**: A0IN1  LDA TBLA0R-1,X
- **$FD07**: CMP $8004-1,X
- **$FD0A**: BNE A0IN2
- **$FD0C**: DEX
- **$FD0D**: BNE A0IN1
- **$FD0F**: A0IN2  RTS ;
- **$FD10**: TBLA0R .BYT $C3,$C2,$CD,'80' ;..CBM80.. TBLA0E ; RESTOR - SET KERNAL INDIRECTS AND VECTORS (SYSTEM) ;
- **$FD15**: RESTOR LDX #<VECTSS
- **$FD17**: LDY #>VECTSS
- **$FD19**: CLC ; ; VECTOR - SET KERNAL INDIRECT AND VECTORS (USER) ;
- **$FD1A**: VECTOR STX TMP2
- **$FD1C**: STY TMP2+1
- **$FD1E**: LDY #VECTSE-VECTSS-1
- **$FD20**: MOVOS1 LDA CINV,Y      ;GET FROM STORAGE
- **$FD23**: BCS MOVOS2      ;C...WANT STORAGE TO USER
- **$FD25**: LDA (TMP2)Y     ;...WANT USER TO STORAGE
- **$FD27**: MOVOS2 STA (TMP2)Y     ;PUT IN USER
- **$FD29**: STA CINV,Y      ;PUT IN STORAGE
- **$FD2C**: DEY
- **$FD2D**: BPL MOVOS1
- **$FD2F**: RTS ; VECTSS .WOR KEY,TIMB,NNMI .WOR   NOPEN,NCLOSE,NCHKIN .WOR   NCKOUT,NCLRCH,NBASIN .WOR   NBSOUT,NSTOP,NGETIN .WOR   NCLALL,TIMB     ;GOTO BREAK ON A USRCMD JMP
- **$FD30**: .WOR   NLOAD,NSAVE VECTSE ; RAMTAS - MEMORY SIZE CHECK AND SET ;
- **$FD50**: RAMTAS LDA #0          ;ZERO LOW MEMORY
- **$FD52**: TAY             ;START AT 0002
- **$FD53**: RAMTZ0 STA $0002,Y     ;ZERO PAGE
- **$FD56**: STA $0200,Y     ;USER BUFFERS AND VARS
- **$FD59**: STA $0300,Y     ;SYSTEM SPACE AND USER SPACE
- **$FD5C**: INY
- **$FD5D**: BNE RAMTZ0 ; ;ALLOCATE TAPE BUFFERS ;
- **$FD5F**: LDX #<TBUFFR
- **$FD61**: LDY #>TBUFFR
- **$FD63**: STX TAPE1
- **$FD65**: STY TAPE1+1 ; ; SET TOP OF MEMORY ; RAMTBT
- **$FD67**: TAY             ;MOVE $00 TO .Y
- **$FD68**: LDA #3          ;SET HIGH INITAL INDEX
- **$FD6A**: STA TMP0+1 ;
- **$FD6C**: RAMTZ1 INC TMP0+1      ;MOVE INDEX THRU MEMORY
- **$FD6E**: RAMTZ2 LDA (TMP0)Y     ;GET PRESENT DATA
- **$FD70**: TAX             ;SAVE IN .X
- **$FD71**: LDA #$55        ;DO A $55,$AA TEST
- **$FD73**: STA (TMP0)Y
- **$FD75**: CMP (TMP0)Y
- **$FD77**: BNE SIZE
- **$FD79**: ROL A
- **$FD7A**: STA (TMP0)Y
- **$FD7C**: CMP (TMP0)Y
- **$FD7E**: BNE SIZE
- **$FD80**: TXA             ;RESTORE OLD DATA
- **$FD81**: STA (TMP0)Y
- **$FD83**: INY
- **$FD84**: BNE RAMTZ2
- **$FD86**: BEQ RAMTZ1 ;
- **$FD88**: SIZE   TYA             ;SET TOP OF MEMORY
- **$FD89**: TAX
- **$FD8A**: LDY TMP0+1
- **$FD8C**: CLC
- **$FD8D**: JSR SETTOP
- **$FD90**: LDA #$08        ;SET BOTTOM OF MEMORY
- **$FD92**: STA MEMSTR+1    ;ALWAYS AT $0800
- **$FD95**: LDA #$04        ;SCREEN ALWAYS AT $400
- **$FD97**: STA HIBASE      ;SET BASE OF SCREEN
- **$FD9A**: RTS
- **$FD9B**: BSIT   .WOR WRTZ,WRTN,KEY,READ ;TABLE OF INDIRECTS FOR CASSETTE IRQ'S ; IOINIT - INITILIZE IO DEVICES ;
- **$FDA3**: IOINIT LDA #$7F        ;KILL INTERRUPTS
- **$FDA5**: STA D1ICR
- **$FDA8**: STA D2ICR
- **$FDAB**: STA D1PRA       ;TURN ON STOP KEY
- **$FDAE**: LDA #%00001000  ;SHUT OFF TIMERS
- **$FDB0**: STA D1CRA
- **$FDB3**: STA D2CRA
- **$FDB6**: STA D1CRB
- **$FDB9**: STA D2CRB ; CONFIGURE PORTS
- **$FDBC**: LDX #$00        ;SET UP KEYBOARD INPUTS
- **$FDBE**: STX D1DDRB      ;KEYBOARD INPUTS
- **$FDC1**: STX D2DDRB      ;USER PORT (NO RS-232)
- **$FDC4**: STX SIDREG+24   ;TURN OFF SID
- **$FDC7**: DEX
- **$FDC8**: STX D1DDRA      ;KEYBOARD OUTPUTS
- **$FDCB**: LDA #%00000111  ;SET SERIAL/VA14/15 (CLKHI)
- **$FDCD**: STA D2PRA
- **$FDD0**: LDA #%00111111  ;SET SERIAL IN/OUT, VA14/15OUT
- **$FDD2**: STA D2DDRA ; ; SET UP THE 6510 LINES ;
- **$FDD5**: LDA #%11100111  ;MOTOR ON, HIRAM LOWRAM CHAREN HIGH
- **$FDD7**: STA R6510
- **$FDD9**: LDA #%00101111  ;MTR OUT,SW IN,WR OUT,CONTROL OUT
- **$FDDB**: STA D6510
- **$FDDD**: IOKEYS LDA PALNTS      ;PAL OR NTSC
- **$FDE0**: BEQ I0010       ;NTSC
- **$FDE2**: LDA #<SIXTYP
- **$FDE4**: STA D1T1L
- **$FDE7**: LDA #>SIXTYP
- **$FDE9**: JMP I0020
- **$FDEC**: I0010  LDA #<SIXTY     ;KEYBOARD SCAN IRQ'S
- **$FDEE**: STA D1T1L
- **$FDF1**: LDA #>SIXTY
- **$FDF3**: I0020  STA D1T1H
- **$FDF6**: JMP PIOKEY ; LDA #$81 ;ENABLE T1 IRQ'S ; STA D1ICR ; LDA D1CRA ; AND #$80 ;SAVE ONLY TOD BIT ; ORA #%00010001 ;ENABLE TIMER1 ; STA D1CRA ; JMP CLKLO ;RELEASE THE CLOCK LINE ; ; SIXTY HERTZ VALUE ; SIXTY  = 16667
- **$FDF9**: SETNAM STA FNLEN
- **$FDFB**: STX    FNADR
- **$FDFD**: STY    FNADR+1
- **$FDFF**: RTS
- **$FE00**: SETLFS STA LA
- **$FE02**: STX    FA
- **$FE04**: STY    SA
- **$FE06**: RTS
- **$FE07**: READSS LDA FA          ;SEE WHICH DEVICES' TO READ
- **$FE09**: CMP #2          ;IS IT RS-232?
- **$FE0B**: BNE READST      ;NO...READ SERIAL/CASS
- **$FE0D**: LDA RSSTAT      ;YES...GET RS-232 UP
- **$FE10**: PHA
- **$FE11**: LDA #00         ;CLEAR RS232 STATUS WHEN READ
- **$FE13**: STA RSSTAT
- **$FE16**: PLA
- **$FE17**: RTS
- **$FE18**: SETMSG STA MSGFLG
- **$FE1A**: READST LDA STATUS
- **$FE1C**: UDST   ORA STATUS
- **$FE1E**: STA    STATUS
- **$FE20**: RTS
- **$FE21**: SETTMO STA TIMOUT
- **$FE24**: RTS
- **$FE25**: MEMTOP BCC SETTOP ; ;CARRY SET--READ TOP OF MEMORY ;
- **$FE27**: GETTOP LDX MEMSIZ
- **$FE2A**: LDY    MEMSIZ+1 ; ;CARRY CLEAR--SET TOP OF MEMORY ;
- **$FE2D**: SETTOP STX MEMSIZ
- **$FE30**: STY    MEMSIZ+1
- **$FE33**: RTS ;MANAGE BOTTOM OF MEMORY ;
- **$FE34**: MEMBOT BCC SETBOT ; ;CARRY SET--READ BOTTOM OF MEMORY ;
- **$FE36**: LDX    MEMSTR
- **$FE39**: LDY    MEMSTR+1 ; ;CARRY CLEAR--SET BOTTOM OF MEMORY ;
- **$FE3C**: SETBOT STX MEMSTR
- **$FE3F**: STY    MEMSTR+1
- **$FE42**: RTS .END .LIB   RS232NMI
- **$FE43**: NMI    SEI             ;NO IRQ'S ALLOWED...
- **$FE44**: JMP (NMINV)     ;...COULD MESS UP CASSETTES
- **$FE47**: NNMI   PHA
- **$FE48**: TXA
- **$FE49**: PHA
- **$FE4A**: TYA
- **$FE4B**: PHA
- **$FE4C**: NNMI10 LDA #$7F        ;DISABLE ALL NMI'S
- **$FE4E**: STA D2ICR
- **$FE51**: LDY D2ICR       ;CHECK IF REAL NMI...
- **$FE54**: BMI NNMI20      ;NO...RS232/OTHER ;
- **$FE56**: NNMI18 JSR A0INT       ;CHECK IF $A0 IN...NO .Y
- **$FE59**: BNE NNMI19      ;...NO
- **$FE5B**: JMP ($8002)     ;...YES ; ; CHECK FOR STOP KEY DOWN ; NNMI19
- **$FE5E**: JSR UD60        ;NO .Y
- **$FE61**: JSR STOP        ;NO .Y
- **$FE64**: BNE NNMI20      ;NO STOP KEY...TEST FOR RS232 ; ; TIMB - WHERE SYSTEM GOES ON A BRK INSTRUCTION ;
- **$FE66**: TIMB   JSR RESTOR      ;RESTORE SYSTEM INDIRECTS
- **$FE69**: JSR IOINIT      ;RESTORE I/O FOR BASIC
- **$FE6C**: JSR CINT        ;RESTORE SCREEN FOR BASIC
- **$FE6F**: JMP ($A002)     ;...NO, SO BASIC WARM START ; DISABLE NMI'S UNTILL READY ;  SAVE ON STACK ;
- **$FE72**: NNMI20 TYA             ;.Y SAVED THROUGH RESTORE
- **$FE73**: AND ENABL       ;SHOW ONLY ENABLES
- **$FE76**: TAX             ;SAVE IN .X FOR LATTER ; ; T1 NMI CHECK - TRANSMITT A BIT ;
- **$FE77**: AND #$01        ;CHECK FOR T1
- **$FE79**: BEQ NNMI30      ;NO... ;
- **$FE7B**: LDA D2PRA
- **$FE7E**: AND #$FF-$04    ;FIX FOR CURRENT I/O
- **$FE80**: ORA NXTBIT      ;LOAD DATA AND...
- **$FE82**: STA D2PRA       ;...SEND IT ;
- **$FE85**: LDA ENABL       ;RESTORE NMI'S
- **$FE88**: STA D2ICR       ;READY FOR NEXT... ; ; BECAUSE OF 6526 ICR STRUCTURE... ;  HANDLE ANOTHER NMI AS A SUBROUTINE ;
- **$FE8B**: TXA             ;TEST FOR ANOTHER NMI
- **$FE8C**: AND #$12        ;TEST FOR T2 OR FLAG
- **$FE8E**: BEQ NNMI25
- **$FE90**: AND #$02        ;CHECK FOR T2
- **$FE92**: BEQ NNMI22      ;MUST BE A FLAG ;
- **$FE94**: JSR T2NMI       ;HANDLE A NORMAL BIT IN...
- **$FE97**: JMP NNMI25      ;...THEN CONTINUE OUTPUT ;
- **$FE9A**: NNMI22 JSR FLNMI       ;HANDLE A START BIT... ;
- **$FE9D**: NNMI25 JSR RSTRAB      ;GO CALC INFO (CODE COULD BE IN LINE)
- **$FEA0**: JMP NMIRTI ; ; T2 NMI CHECK - RECIEVE A BIT ;
- **$FEA3**: NNMI30 TXA
- **$FEA4**: AND #$02        ;MASK TO T2
- **$FEA6**: BEQ NNMI40      ;NO... ;
- **$FEA8**: JSR T2NMI       ;HANDLE INTERRUPT
- **$FEAB**: JMP NMIRTI ; FLAG NMI HANDLER - RECIEVE A START BIT ;
- **$FEAE**: NNMI40 TXA             ;CHECK FOR EDGE
- **$FEAF**: AND #$10        ;ON FLAG...
- **$FEB1**: BEQ NMIRTI      ;NO... ;
- **$FEB3**: JSR FLNMI       ;START BIT ROUTINE
- **$FEB6**: NMIRTI LDA ENABL       ;RESTORE NMI'S
- **$FEB9**: STA D2ICR
- **$FEBC**: PREND  PLA             ;BECAUSE OF MISSING SCREEN EDITOR
- **$FEBD**: TAY
- **$FEBE**: PLA
- **$FEBF**: TAX
- **$FEC0**: PLA
- **$FEC1**: RTI ; BAUDO TABLE CONTAINS VALUES ;  FOR 1E6/BAUD RATE/2 ;
- **$FEC2**: BAUDO  .WOR 10000-CBIT ; 50 BAUD
- **$FEC4**: .WOR 6667-CBIT  ;   75   BAUD
- **$FEC6**: .WOR 4545-CBIT  ;  110   BAUD
- **$FEC8**: .WOR 3715-CBIT  ;  134.6 BAUD
- **$FECA**: .WOR 3333-CBIT  ;  150   BAUD
- **$FECC**: .WOR 1667-CBIT  ;  300   BAUD
- **$FECE**: .WOR 833-CBIT   ;  600   BAUD
- **$FED0**: .WOR 417-CBIT   ; 1200   BAUD
- **$FED2**: .WOR 278-CBIT   ; 1800   BAUD
- **$FED4**: .WOR 208-CBIT   ; 2400   BAUD ; ; CBIT - AN ADJUSTMENT TO MAKE NEXT T2 HIT NEAR CENTER ;   OF THE NEXT BIT. ;   APROX THE TIME TO SERVICE A CB1 NMI CBIT   =100            ;CYCLES ; T2NMI - SUBROUTINE TO HANDLE AN RS232 ;  BIT INPUT. ;
- **$FED6**: T2NMI  LDA D2PRB       ;GET DATA IN
- **$FED9**: AND #01         ;MASK OFF...
- **$FEDB**: STA INBIT       ;...SAVE FOR LATTER ; ; UPDATE T2 FOR MID BIT CHECK ;   (WORST CASE <213 CYCLES TO HERE) ;   (CALC 125 CYCLES+43-66 DEAD) ;
- **$FEDD**: LDA D2T2L       ;CALC NEW TIME & CLR NMI
- **$FEE0**: SBC #22+6
- **$FEE2**: ADC BAUDOF
- **$FEE5**: STA D2T2L
- **$FEE8**: LDA D2T2H
- **$FEEB**: ADC BAUDOF+1
- **$FEEE**: STA D2T2H ;
- **$FEF1**: LDA #$11        ;ENABLE TIMER
- **$FEF3**: STA D2CRB ;
- **$FEF6**: LDA ENABL       ;RESTORE NMI'S EARLY...
- **$FEF9**: STA D2ICR ;
- **$FEFC**: LDA #$FF        ;ENABLE COUNT FROM $FFFF
- **$FEFE**: STA D2T2L
- **$FF01**: STA D2T2H ;
- **$FF04**: JMP RSRCVR      ;GO SHIFT IN... FLNMI ; ; GET HALF BIT RATE VALUE ;
- **$FF07**: LDA M51AJB
- **$FF0A**: STA D2T2L
- **$FF0D**: LDA M51AJB+1
- **$FF10**: STA D2T2H ;
- **$FF13**: LDA #$11        ;ENABLE TIMER
- **$FF15**: STA D2CRB ;
- **$FF18**: LDA #$12        ;DISABLE FLAG, ENABLE T2
- **$FF1A**: EOR ENABL
- **$FF1D**: STA ENABL ;ORA #$82 ;STA D2ICR ;
- **$FF20**: LDA #$FF        ;PRESET FOR COUNT DOWN
- **$FF22**: STA D2T2L
- **$FF25**: STA D2T2H ;
- **$FF28**: LDX BITNUM      ;GET #OF BITS IN
- **$FF2B**: STX BITCI       ;PUT IN RCVRCNT
- **$FF2D**: RTS ; ; POPEN - PATCHES OPEN RS232 FOR UNIVERSAL KERNAL ;
- **$FF2E**: POPEN  TAX             ;WE'RE CALCULATING BAUD RATE
- **$FF2F**: LDA M51AJB+1    ; M51AJB=FREQ/BAUD/2-100
- **$FF32**: ROL A
- **$FF33**: TAY
- **$FF34**: TXA
- **$FF35**: ADC #CBIT+CBIT
- **$FF37**: STA BAUDOF
- **$FF3A**: TYA
- **$FF3B**: ADC #0
- **$FF3D**: STA BAUDOF+1
- **$FF40**: RTS
- **$FF41**: NOP
- **$FF42**: NOP .END .LIB   IRQFILE ; SIMIRQ - SIMULATE AN IRQ (FOR CASSETTE READ) ;  ENTER BY A JSR SIMIRQ ;
- **$FF43**: SIMIRQ PHP
- **$FF44**: PLA             ;FIX THE BREAK FLAG
- **$FF45**: AND #$EF
- **$FF47**: PHA ; PULS - CHECKS FOR REAL IRQ'S OR BREAKS ;
- **$FF48**: PULS   PHA
- **$FF49**: TXA
- **$FF4A**: PHA
- **$FF4B**: TYA
- **$FF4C**: PHA
- **$FF4D**: TSX
- **$FF4E**: LDA $104,X      ;GET OLD P STATUS
- **$FF51**: AND #$10        ;BREAK FLAG?
- **$FF53**: BEQ PULS1       ;...NO
- **$FF55**: JMP (CBINV)     ;...YES...BREAK INSTR
- **$FF58**: PULS1  JMP (CINV)      ;...IRQ .END .LIB   VECTORS
- **$FF5B**: *=$FF8A-9
- **$FF81**: JMP    CINT
- **$FF84**: JMP    IOINIT
- **$FF87**: JMP    RAMTAS *=$FF8A                ;NEW VECTORS FOR BASIC
- **$FF8A**: JMP    RESTOR          ;RESTORE VECTORS TO INITIAL SYSTEM
- **$FF8D**: JMP    VECTOR          ;CHANGE VECTORS FOR USER *      =$FF90
- **$FF90**: JMP    SETMSG          ;CONTROL O.S. MESSAGES
- **$FF93**: JMP    SECND           ;SEND SA AFTER LISTEN
- **$FF96**: JMP    TKSA            ;SEND SA AFTER TALK
- **$FF99**: JMP    MEMTOP          ;SET/READ TOP OF MEMORY
- **$FF9C**: JMP    MEMBOT          ;SET/READ BOTTOM OF MEMORY
- **$FF9F**: JMP    SCNKEY          ;SCAN KEYBOARD
- **$FFA2**: JMP    SETTMO          ;SET TIMEOUT IN IEEE
- **$FFA5**: JMP    ACPTR           ;HANDSHAKE IEEE BYTE IN
- **$FFA8**: JMP    CIOUT           ;HANDSHAKE IEEE BYTE OUT
- **$FFAB**: JMP    UNTLK           ;SEND UNTALK OUT IEEE
- **$FFAE**: JMP    UNLSN           ;SEND UNLISTEN OUT IEEE
- **$FFB1**: JMP    LISTN           ;SEND LISTEN OUT IEEE
- **$FFB4**: JMP    TALK            ;SEND TALK OUT IEEE
- **$FFB7**: JMP    READSS          ;RETURN I/O STATUS BYTE
- **$FFBA**: JMP    SETLFS          ;SET LA, FA, SA
- **$FFBD**: JMP    SETNAM          ;SET LENGTH AND FN ADR
- **$FFC0**: OPEN   JMP (IOPEN)     ;OPEN LOGICAL FILE
- **$FFC3**: CLOSE  JMP (ICLOSE)    ;CLOSE LOGICAL FILE
- **$FFC6**: CHKIN  JMP (ICHKIN)    ;OPEN CHANNEL IN
- **$FFC9**: CKOUT  JMP (ICKOUT)    ;OPEN CHANNEL OUT
- **$FFCC**: CLRCH  JMP (ICLRCH)    ;CLOSE I/O CHANNEL
- **$FFCF**: BASIN  JMP (IBASIN)    ;INPUT FROM CHANNEL
- **$FFD2**: BSOUT  JMP (IBSOUT)    ;OUTPUT TO CHANNEL
- **$FFD5**: JMP    LOADSP          ;LOAD FROM FILE
- **$FFD8**: JMP    SAVESP          ;SAVE TO FILE
- **$FFDB**: JMP    SETTIM          ;SET INTERNAL CLOCK
- **$FFDE**: JMP    RDTIM           ;READ INTERNAL CLOCK
- **$FFE1**: STOP   JMP (ISTOP)     ;SCAN STOP KEY
- **$FFE4**: GETIN  JMP (IGETIN)    ;GET CHAR FROM Q
- **$FFE7**: CLALL  JMP (ICLALL)    ;CLOSE ALL FILES
- **$FFEA**: JMP    UDTIM           ;INCREMENT CLOCK
- **$FFED**: JSCROG JMP SCRORG      ;SCREEN ORG
- **$FFF0**: JPLOT  JMP PLOT        ;READ/SET X,Y COORD
- **$FFF3**: JIOBAS JMP IOBASE      ;RETURN I/O BASE
- **$FFF6**: *=$FFFA
- **$FFFA**: .WOR   NMI             ;PROGRAM DEFINEABLE
- **$FFFC**: .WOR   START           ;INITIALIZATION CODE
- **$FFFE**: .WOR   PULS            ;INTERRUPT HANDLER

### Original Disassembly (—)
- **$FCE2**: set X for stack
- **$FCE4**: disable the interrupts
- **$FCE5**: clear stack
- **$FCE6**: clear decimal mode
- **$FCE7**: scan for autostart ROM at $8000
- **$FCEA**: if not there continue startup
- **$FCEC**: else call ROM start code
- **$FCEF**: read the horizontal fine scroll and control register
- **$FCF2**: initialise SID, CIA and IRQ
- **$FCF5**: RAM test and find RAM end
- **$FCF8**: restore default I/O vectors
- **$FCFB**: initialise VIC and screen editor
- **$FCFE**: enable the interrupts
- **$FCFF**: execute BASIC

### Commodore-64-intern-Buch (Commodore)
- **$FCE2**: Wert für Stapelzeiger
- **$FCE4**: Interrupt setzen
- **$FCE5**: Stapelzeiger initialisieren
- **$FCE6**: Dezimalflag zurücksetzen
- **$FCE7**: prüft auf ROM in $8000
- **$FCEA**: kein Autostart-Modul ?
- **$FCEC**: Sprung auf Modul-Start
- **$FCEF**: Videocontroller Steuerreg. 2
- **$FCF2**: Interrupt vorbereiten
- **$FCF5**: Arbeitsspeicher initialisieren
- **$FCF8**: Hardware und I/O Vekt. setzen
- **$FCFB**: Video-Reset
- **$FCFF**: zum BASIC Kaltstart

### Marko Mäkelä (Marko Mäkelä)
- **$FCEC**: start cartridge
- **$FCFF**: start basic

### Magnus Nyman (Magnus Nyman)
- **$FCE5**: Set stackpointer to #ff
- **$FCE7**: Check ROM at $8000
- **$FCEC**: Jump to autostart vector
- **$FCF2**: Init I/O
- **$FCF5**: Init system constants
- **$FCF8**: KERNAL reset
- **$FCFB**: Setup PAL/NTSC
- **$FCFF**: Basic coldstart

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*