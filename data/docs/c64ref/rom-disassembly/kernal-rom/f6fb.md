---
title: ;
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
- 0001-r6510
- 0068-bits
- 0090-status
- 0091-stkey
- 0092-svxt
- 0093-verck
- 0096-syno
- 009b-prty
- 009c-dpsw
- 009d-msgflg
- 009e-ptr1
- 009f-ptr2
- 00a0-time
- 00a3-pcntr
- 00a4-firt
- 00a5-count
- 00a6-bufpt
- 00a7-shcnl
- 00a8-rer
- 00a9-rez
- 00aa-rdflg
- 00ab-shcnh
- 00ac-sal
- 00ae-eal
- 00af-eah
- 00b0-cmp0
- 00b1-temp
- 00b2-tape1
- 00b4-snsw1
- 00b5-diff
- 00b6-prp
- 00b7-fnlen
- 00bb-fnadr
- 00bd-ochar
- 00be-fsblk
- 00bf-mych
- 00c0-cas1
- 00c1-stal
- 00c2-stah
- 00d7-data
- 0100-bad
- 0200-buf
- 028c-delay
- 0291-mode
- 029f-irqtmp
- 02a2-caston
- 02a3-kika26
- 02a4-stupid
- 0314-cinv
- ab45-print
- adc
- asl
- bcc
- bcs
- beq
- bit
- bmi
- bne
- bpl
- bsout
- bvc
- check
- clc
- clear
- cli
- close
- clrch
- cmp
- cpx
- cpy
- dec
- dex
- dey
- ece7-load
- enable
- eor
- f34a-open
- f5ed-save
- f6fb-systems-ausgeben
- f72c-lesen
- f76a-band-schreiben
- f7d0-und-prfen-ob-gltig
- f7d7-ferstartadresse-c0-192
- f7ea-bandheader-nach-namen-suchen
- f80d-bandpufferzeiger-erhhen
- f817-wartet-auf-bandtaste
- f82e-gedrckt
- f838-schreiben
- f841-block-vom-band-lesen
- f84a-programm-vom-band-laden
- f864-bandpuffer-auf-band-schreiben
- f86b-schreiben
- f875-common-code-for-cassette-read-and-write
- f8be-io-abschlu-abwarten
- f8d0-testet-auf-stop-taste
- f8dc-clear-saved-irq-address
- f8e2-band-fr-lesen-vorbereiten
- f92c-lesen
- fa60-receive-next-byte-from-cassette
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
- output
- pha
- pla
- reads
- return
- rol
- ror
- rti
- rts
- sbc
- screen
- sec
- second
- sei
- sta
- stop
- store
- stx
- sty
- tax
- tay
- txa
- tya
- vector
- write
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F6FB
  address_end: $FA6E
  sources:
  - name: Original Disassembly
    author: Commodore
    description: '- **$F6FB**: ERROR1 LDA #1          ;TOO MANY FILES'
  - name: Original Disassembly
    author: —
    description: '- **$F6FB**: ''too many files'' error'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F6FB**: ''TOO MANY FILES'''
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$F6FB**: too many files'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F6FB**: error #1, too many files'
---

# $F6FB — ;

## Disassemblatura
```assembly
.F6FB  A9 01    LDA #$01   ; ERROR1 LDA #1          ;TOO MANY FILES
.F6FD  2C       .BYTE $2C   ; .BYT   $2C
.F6FE  A9 02    LDA #$02   ; ERROR2 LDA #2          ;FILE OPEN
.F700  2C       .BYTE $2C   ; .BYT   $2C
.F701  A9 03    LDA #$03   ; ERROR3 LDA #3          ;FILE NOT OPEN
.F703  2C       .BYTE $2C   ; .BYT   $2C
.F704  A9 04    LDA #$04   ; ERROR4 LDA #4          ;FILE NOT FOUND
.F706  2C       .BYTE $2C   ; .BYT   $2C
.F707  A9 05    LDA #$05   ; ERROR5 LDA #5          ;DEVICE NOT PRESENT
.F709  2C       .BYTE $2C   ; .BYT   $2C
.F70A  A9 06    LDA #$06   ; ERROR6 LDA #6          ;NOT INPUT FILE
.F70C  2C       .BYTE $2C   ; .BYT   $2C
.F70D  A9 07    LDA #$07   ; ERROR7 LDA #7          ;NOT OUTPUT FILE
.F70F  2C       .BYTE $2C   ; .BYT   $2C
.F710  A9 08    LDA #$08   ; ERROR8 LDA #8          ;MISSING FILE NAME
.F712  2C       .BYTE $2C   ; .BYT   $2C
.F713  A9 09    LDA #$09   ; ERROR9 LDA #9          ;BAD DEVICE # ;
.F715  48       PHA   ; PHA                    ;ERROR NUMBER ON STACK
.F716  20 CC FF JSR $FFCC   ; JSR    CLRCH           ;RESTORE I/O CHANNELS ;
.F719  A0 00    LDY #$00   ; LDY    #MS1-MS1
.F71B  24 9D    BIT $9D   ; BIT    MSGFLG          ;ARE WE PRINTING ERROR?
.F71D  50 0A    BVC $F729   ; BVC    EREXIT          ;NO... ;
.F71F  20 2F F1 JSR $F12F   ; JSR    MSG             ;PRINT "CBM I/O ERROR #"
.F722  68       PLA   ; PLA
.F723  48       PHA   ; PHA
.F724  09 30    ORA #$30   ; ORA    #$30            ;MAKE ERROR # ASCII
.F726  20 D2 FF JSR $FFD2   ; JSR    BSOUT           ;PRINT IT ;
.F729  68       PLA   ; EREXIT PLA
.F72A  38       SEC   ; SEC
.F72B  60       RTS   ; RTS .END .LIB   TAPEFILE ;FAH -- FIND ANY HEADER ; ;READS TAPE DEVICE UNTIL ONE OF FOLLOWING ;BLOCK TYPES FOUND: BDFH--BASIC DATA ;FILE HEADER, BLF--BASIC LOAD FILE ;FOR SUCCESS CARRY IS CLEAR ON RETURN. ;FOR FAILURE CARRY IS SET ON RETURN. ;IN ADDITION ACCUMULATOR IS 0 IF STOP ;KEY WAS PRESSED. ;
.F72C  A5 93    LDA $93   ; FAH    LDA VERCK       ;SAVE OLD VERIFY
.F72E  48       PHA   ; PHA
.F72F  20 41 F8 JSR $F841   ; JSR    RBLK            ;READ TAPE BLOCK
.F732  68       PLA   ; PLA
.F733  85 93    STA $93   ; STA    VERCK           ;RESTORE VERIFY FLAG
.F735  B0 32    BCS $F769   ; BCS    FAH40           ;READ TERMINATED ;
.F737  A0 00    LDY #$00   ; LDY    #0
.F739  B1 B2    LDA ($B2),Y   ; LDA    (TAPE1)Y        ;GET HEADER TYPE ;
.F73B  C9 05    CMP #$05   ; CMP    #EOT            ;CHECK END OF TAPE?
.F73D  F0 2A    BEQ $F769   ; BEQ    FAH40           ;YES...FAILURE ;
.F73F  C9 01    CMP #$01   ; CMP    #BLF            ;BASIC LOAD FILE?
.F741  F0 08    BEQ $F74B   ; BEQ    FAH50           ;YES...SUCCESS ;
.F743  C9 03    CMP #$03   ; CMP    #PLF            ;FIXED LOAD FILE?
.F745  F0 04    BEQ $F74B   ; BEQ    FAH50           ;YES...SUCCESS ;
.F747  C9 04    CMP #$04   ; CMP    #BDFH           ;BASIC DATA FILE?
.F749  D0 E1    BNE $F72C   ; BNE    FAH             ;NO...KEEP TRYING ;
.F74B  AA       TAX   ; FAH50  TAX             ;RETURN FILE TYPE IN .X
.F74C  24 9D    BIT $9D   ; BIT    MSGFLG          ;PRINTING MESSAGES?
.F74E  10 17    BPL $F767   ; BPL    FAH45           ;NO... ;
.F750  A0 63    LDY #$63   ; LDY    #MS17-MS1       ;PRINT "FOUND"
.F752  20 2F F1 JSR $F12F   ; JSR    MSG ; ;OUTPUT COMPLETE FILE NAME ;
.F755  A0 05    LDY #$05   ; LDY    #5
.F757  B1 B2    LDA ($B2),Y   ; FAH55  LDA (TAPE1)Y
.F759  20 D2 FF JSR $FFD2   ; JSR    BSOUT
.F75C  C8       INY   ; INY
.F75D  C0 15    CPY #$15   ; CPY    #21
.F75F  D0 F6    BNE $F757   ; BNE    FAH55 ;
.F761  A5 A1    LDA $A1   ; FAH56  LDA STKEY       ;KEY  DOWN ON LAST ROW...
.F763  20 E0 E4 JSR $E4E0   ; JSR FPATCH      ;GOTO PATCH...
.F766  EA       NOP   ; NOP ;
.F767  18       CLC   ; FAH45  CLC             ;SUCCESS FLAG
.F768  88       DEY   ; DEY                    ;MAKE NONZERO FOR OKAY RETURN ;
.F769  60       RTS   ; FAH40  RTS ;TAPEH--WRITE TAPE HEADER ;ERROR IF TAPE BUFFER DE-ALLOCATED ;CARRY CLEAR IF O.K. ;
.F76A  85 9E    STA $9E   ; TAPEH  STA T1 ; ;DETERMINE ADDRESS OF BUFFER ;
.F76C  20 D0 F7 JSR $F7D0   ; JSR    ZZZ
.F76F  90 5E    BCC $F7CF   ; BCC    TH40            ;BUFFER WAS DE-ALLOCATED ; ;PRESERVE START AND END ADDRESSES ;FOR CASE OF HEADER FOR LOAD FILE ;
.F771  A5 C2    LDA $C2   ; LDA    STAH
.F773  48       PHA   ; PHA
.F774  A5 C1    LDA $C1   ; LDA    STAL
.F776  48       PHA   ; PHA
.F777  A5 AF    LDA $AF   ; LDA    EAH
.F779  48       PHA   ; PHA
.F77A  A5 AE    LDA $AE   ; LDA    EAL
.F77C  48       PHA   ; PHA ; ;PUT BLANKS IN TAPE BUFFER ;
.F77D  A0 BF    LDY #$BF   ; LDY    #BUFSZ-1
.F77F  A9 20    LDA #$20   ; LDA    #'
.F781  91 B2    STA ($B2),Y   ; BLNK2  STA (TAPE1)Y
.F783  88       DEY   ; DEY
.F784  D0 FB    BNE $F781   ; BNE    BLNK2 ; ;PUT BLOCK TYPE IN HEADER ;
.F786  A5 9E    LDA $9E   ; LDA    T1
.F788  91 B2    STA ($B2),Y   ; STA    (TAPE1)Y ; ;PUT START LOAD ADDRESS IN HEADER ;
.F78A  C8       INY   ; INY
.F78B  A5 C1    LDA $C1   ; LDA    STAL
.F78D  91 B2    STA ($B2),Y   ; STA    (TAPE1)Y
.F78F  C8       INY   ; INY
.F790  A5 C2    LDA $C2   ; LDA    STAH
.F792  91 B2    STA ($B2),Y   ; STA    (TAPE1)Y ; ;PUT END LOAD ADDRESS IN HEADER ;
.F794  C8       INY   ; INY
.F795  A5 AE    LDA $AE   ; LDA    EAL
.F797  91 B2    STA ($B2),Y   ; STA    (TAPE1)Y
.F799  C8       INY   ; INY
.F79A  A5 AF    LDA $AF   ; LDA    EAH
.F79C  91 B2    STA ($B2),Y   ; STA    (TAPE1)Y ; ;PUT FILE NAME IN HEADER ;
.F79E  C8       INY   ; INY
.F79F  84 9F    STY $9F   ; STY    T2
.F7A1  A0 00    LDY #$00   ; LDY    #0
.F7A3  84 9E    STY $9E   ; STY    T1
.F7A5  A4 9E    LDY $9E   ; TH20   LDY T1
.F7A7  C4 B7    CPY $B7   ; CPY    FNLEN
.F7A9  F0 0C    BEQ $F7B7   ; BEQ    TH30
.F7AB  B1 BB    LDA ($BB),Y   ; LDA    (FNADR)Y
.F7AD  A4 9F    LDY $9F   ; LDY    T2
.F7AF  91 B2    STA ($B2),Y   ; STA    (TAPE1)Y
.F7B1  E6 9E    INC $9E   ; INC    T1
.F7B3  E6 9F    INC $9F   ; INC    T2
.F7B5  D0 EE    BNE $F7A5   ; BNE    TH20 ; ;SET UP START AND END ADDRESS OF HEADER ;
.F7B7  20 D7 F7 JSR $F7D7   ; TH30   JSR LDAD1 ; ;SET UP TIME FOR LEADER ;
.F7BA  A9 69    LDA #$69   ; LDA    #$69
.F7BC  85 AB    STA $AB   ; STA    SHCNH ;
.F7BE  20 6B F8 JSR $F86B   ; JSR    TWRT2           ;WRITE HEADER ON TAPE ; ;RESTORE START AND END ADDRESS OF ;LOAD FILE. ;
.F7C1  A8       TAY   ; TAY                    ;SAVE ERROR CODE IN .Y
.F7C2  68       PLA   ; PLA
.F7C3  85 AE    STA $AE   ; STA    EAL
.F7C5  68       PLA   ; PLA
.F7C6  85 AF    STA $AF   ; STA    EAH
.F7C8  68       PLA   ; PLA
.F7C9  85 C1    STA $C1   ; STA    STAL
.F7CB  68       PLA   ; PLA
.F7CC  85 C2    STA $C2   ; STA    STAH
.F7CE  98       TYA   ; TYA                    ;RESTORE ERROR CODE FOR RETURN ;
.F7CF  60       RTS   ; TH40   RTS ;FUNCTION TO RETURN TAPE BUFFER ;ADDRESS IN TAPE1 ;
.F7D0  A6 B2    LDX $B2   ; ZZZ    LDX TAPE1       ;ASSUME TAPE1
.F7D2  A4 B3    LDY $B3   ; LDY    TAPE1+1
.F7D4  C0 02    CPY #$02   ; CPY    #>BUF           ;CHECK FOR ALLOCATION... ;...[TAPE1+1]=0 OR 1 MEANS DEALLOCATED ;...C CLR => DEALLOCATED
.F7D6  60       RTS   ; RTS
.F7D7  20 D0 F7 JSR $F7D0   ; LDAD1  JSR ZZZ         ;GET PTR TO CASSETTE
.F7DA  8A       TXA   ; TXA
.F7DB  85 C1    STA $C1   ; STA    STAL            ;SAVE START LOW
.F7DD  18       CLC   ; CLC
.F7DE  69 C0    ADC #$C0   ; ADC    #BUFSZ          ;COMPUTE POINTER TO END
.F7E0  85 AE    STA $AE   ; STA    EAL             ;SAVE END LOW
.F7E2  98       TYA   ; TYA
.F7E3  85 C2    STA $C2   ; STA    STAH            ;SAVE START HIGH
.F7E5  69 00    ADC #$00   ; ADC    #0              ;COMPUTE POINTER TO END
.F7E7  85 AF    STA $AF   ; STA    EAH             ;SAVE END HIGH
.F7E9  60       RTS   ; RTS
.F7EA  20 2C F7 JSR $F72C   ; FAF    JSR FAH         ;FIND ANY HEADER
.F7ED  B0 1D    BCS $F80C   ; BCS    FAF40           ;FAILED ; ;SUCCESS...SEE IF RIGHT NAME ;
.F7EF  A0 05    LDY #$05   ; LDY    #5              ;OFFSET INTO TAPE HEADER
.F7F1  84 9F    STY $9F   ; STY    T2
.F7F3  A0 00    LDY #$00   ; LDY    #0              ;OFFSET INTO FILE NAME
.F7F5  84 9E    STY $9E   ; STY    T1
.F7F7  C4 B7    CPY $B7   ; FAF20  CPY FNLEN       ;COMPARE THIS MANY
.F7F9  F0 10    BEQ $F80B   ; BEQ    FAF30           ;DONE ;
.F7FB  B1 BB    LDA ($BB),Y   ; LDA    (FNADR)Y
.F7FD  A4 9F    LDY $9F   ; LDY    T2
.F7FF  D1 B2    CMP ($B2),Y   ; CMP    (TAPE1)Y
.F801  D0 E7    BNE $F7EA   ; BNE    FAF             ;MISMATCH--TRY NEXT HEADER
.F803  E6 9E    INC $9E   ; INC    T1
.F805  E6 9F    INC $9F   ; INC    T2
.F807  A4 9E    LDY $9E   ; LDY    T1
.F809  D0 EC    BNE $F7F7   ; BNE    FAF20           ;BRANCH ALWAYS ;
.F80B  18       CLC   ; FAF30  CLC             ;SUCCESS FLAG
.F80C  60       RTS   ; FAF40  RTS .END .LIB   TAPECONTROL
.F80D  20 D0 F7 JSR $F7D0   ; JTP20  JSR ZZZ
.F810  E6 A6    INC $A6   ; INC    BUFPT
.F812  A4 A6    LDY $A6   ; LDY    BUFPT
.F814  C0 C0    CPY #$C0   ; CPY    #BUFSZ
.F816  60       RTS   ; RTS ;STAYS IN ROUTINE D2T1LL PLAY SWITCH ;
.F817  20 2E F8 JSR $F82E   ; CSTE1  JSR CS10
.F81A  F0 1A    BEQ $F836   ; BEQ    CS25
.F81C  A0 1B    LDY #$1B   ; LDY    #MS7-MS1        ;"PRESS PLAY..."
.F81E  20 2F F1 JSR $F12F   ; CS30   JSR MSG
.F821  20 D0 F8 JSR $F8D0   ; CS40   JSR TSTOP       ;WATCH FOR STOP KEY
.F824  20 2E F8 JSR $F82E   ; JSR    CS10            ;WATCH CASSETTE SWITCHES
.F827  D0 F8    BNE $F821   ; BNE    CS40
.F829  A0 6A    LDY #$6A   ; LDY    #MS18-MS1       ;"OK"
.F82B  4C 2F F1 JMP $F12F   ; JMP    MSG ;SUBR RETURNS <> FOR CASSETTE SWITCH ;
.F82E  A9 10    LDA #$10   ; CS10   LDA #$10        ;CHECK PORT
.F830  24 01    BIT $01   ; BIT    R6510           ;CLOSED?...
.F832  D0 02    BNE $F836   ; BNE    CS25            ;NO. . .
.F834  24 01    BIT $01   ; BIT    R6510           ;CHECK AGAIN TO DEBOUNCE
.F836  18       CLC   ; CS25   CLC             ;GOOD RETURN
.F837  60       RTS   ; RTS ;CHECKS FOR PLAY & RECORD ;
.F838  20 2E F8 JSR $F82E   ; CSTE2  JSR CS10
.F83B  F0 F9    BEQ $F836   ; BEQ    CS25
.F83D  A0 2E    LDY #$2E   ; LDY    #MS8-MS1        ;"RECORD"
.F83F  D0 DD    BNE $F81E   ; BNE    CS30 ;READ HEADER BLOCK ENTRY ;
.F841  A9 00    LDA #$00   ; RBLK   LDA #0
.F843  85 90    STA $90   ; STA    STATUS
.F845  85 93    STA $93   ; STA    VERCK
.F847  20 D7 F7 JSR $F7D7   ; JSR    LDAD1 ;READ LOAD BLOCK ENTRY ;
.F84A  20 17 F8 JSR $F817   ; TRD    JSR CSTE1       ;SAY 'PRESS PLAY'
.F84D  B0 1F    BCS $F86E   ; BCS    TWRT3           ;STOP KEY PRESSED
.F84F  78       SEI   ; SEI
.F850  A9 00    LDA #$00   ; LDA    #0              ;CLEAR FLAGS...
.F852  85 AA    STA $AA   ; STA    RDFLG
.F854  85 B4    STA $B4   ; STA    SNSW1
.F856  85 B0    STA $B0   ; STA    CMP0
.F858  85 9E    STA $9E   ; STA    PTR1
.F85A  85 9F    STA $9F   ; STA    PTR2
.F85C  85 9C    STA $9C   ; STA    DPSW
.F85E  A9 90    LDA #$90   ; LDA    #$90            ;ENABLE FOR CA1 IRQ...READ LINE
.F860  A2 0E    LDX #$0E   ; LDX    #14             ;POINT IRQ VECTOR TO READ
.F862  D0 11    BNE $F875   ; BNE    TAPE            ;JMP ;WRITE HEADER BLOCK ENTRY ;
.F864  20 D7 F7 JSR $F7D7   ; WBLK   JSR LDAD1 ; ;WRITE LOAD BLOCK ENTRY ;
.F867  A9 14    LDA #$14   ; TWRT   LDA #20         ;BETWEEN BLOCK SHORTS
.F869  85 AB    STA $AB   ; STA    SHCNH
.F86B  20 38 F8 JSR $F838   ; TWRT2  JSR CSTE2       ;SAY 'PRESS PLAY & RECORD'
.F86E  B0 6C    BCS $F8DC   ; TWRT3  BCS STOP3       ;STOP KEY PRESSED
.F870  78       SEI   ; SEI
.F871  A9 82    LDA #$82   ; LDA    #$82            ;ENABLE T2 IRQS...WRITE TIME
.F873  A2 08    LDX #$08   ; LDX    #8              ;VECTOR IRQ TO WRTZ ;START TAPE OPERATION ENTRY POINT ;
.F875  A0 7F    LDY #$7F   ; TAPE   LDY #$7F        ;KILL UNWANTED IRQ'S
.F877  8C 0D DC STY $DC0D   ; STY D1ICR
.F87A  8D 0D DC STA $DC0D   ; STA D1ICR       ;TURN ON WANTED
.F87D  AD 0E DC LDA $DC0E   ; LDA D1CRA       ;CALC TIMER ENABLES
.F880  09 19    ORA #$19   ; ORA #$19
.F882  8D 0F DC STA $DC0F   ; STA D1CRB       ;TURN ON T2 IRQ'S FOR CASS WRITE(ONE SHOT)
.F885  29 91    AND #$91   ; AND #$91        ;SAVE TOD 50/60 INDICATION
.F887  8D A2 02 STA $02A2   ; STA CASTON      ;PLACE IN AUTO MODE FOR T1 ; WAIT FOR RS-232 TO FINISH
.F88A  20 A4 F0 JSR $F0A4   ; JSR RSP232 ; DISABLE SCREEN DISPLAY
.F88D  AD 11 D0 LDA $D011   ; LDA VICREG+17
.F890  29 EF    AND #$EF   ; AND #$FF-$10    ;DISABLE SCREEN
.F892  8D 11 D0 STA $D011   ; STA VICREG+17 ; MOVE IRQ TO IRQTEMP FOR CASS OPS
.F895  AD 14 03 LDA $0314   ; LDA    CINV
.F898  8D 9F 02 STA $029F   ; STA    IRQTMP
.F89B  AD 15 03 LDA $0315   ; LDA    CINV+1
.F89E  8D A0 02 STA $02A0   ; STA    IRQTMP+1
.F8A1  20 BD FC JSR $FCBD   ; JSR    BSIV            ;GO CHANGE IRQ VECTOR
.F8A4  A9 02    LDA #$02   ; LDA    #2              ;FSBLK STARTS AT 2
.F8A6  85 BE    STA $BE   ; STA    FSBLK
.F8A8  20 97 FB JSR $FB97   ; JSR    NEWCH           ;PREP LOCAL COUNTERS AND FLAGS
.F8AB  A5 01    LDA $01   ; LDA    R6510           ;TURN MOTOR ON
.F8AD  29 1F    AND #$1F   ; AND    #%011111        ;LOW TURNS ON
.F8AF  85 01    STA $01   ; STA    R6510
.F8B1  85 C0    STA $C0   ; STA    CAS1            ;FLAG INTERNAL CONTROL OF CASS MOTOR
.F8B3  A2 FF    LDX #$FF   ; LDX    #$FF            ;DELAY BETWEEN BLOCKS
.F8B5  A0 FF    LDY #$FF   ; TP32   LDY #$FF
.F8B7  88       DEY   ; TP35   DEY
.F8B8  D0 FD    BNE $F8B7   ; BNE    TP35
.F8BA  CA       DEX   ; DEX
.F8BB  D0 F8    BNE $F8B5   ; BNE    TP32
.F8BD  58       CLI   ; CLI
.F8BE  AD A0 02 LDA $02A0   ; TP40   LDA IRQTMP+1    ;CHECK FOR INTERRUPT VECTOR...
.F8C1  CD 15 03 CMP $0315   ; CMP    CINV+1          ;...POINTING AT KEY ROUTINE
.F8C4  18       CLC   ; CLC
.F8C5  F0 15    BEQ $F8DC   ; BEQ    STOP3           ;...YES RETURN
.F8C7  20 D0 F8 JSR $F8D0   ; JSR    TSTOP           ;...NO CHECK FOR STOP KEY ; ; 60 HZ KEYSCAN IGNORED ;
.F8CA  20 BC F6 JSR $F6BC   ; JSR    UD60            ; STOP KEY CHECK
.F8CD  4C BE F8 JMP $F8BE   ; JMP    TP40            ;STAY IN LOOP UNTILL TAPES ARE DONE
.F8D0  20 E1 FF JSR $FFE1   ; TSTOP  JSR STOP        ;STOP KEY DOWN?
.F8D3  18       CLC   ; CLC                    ;ASSUME NO STOP
.F8D4  D0 0B    BNE $F8E1   ; BNE    STOP4           ;WE WERE RIGHT ; ;STOP KEY DOWN... ;
.F8D6  20 93 FC JSR $FC93   ; JSR    TNIF            ;TURN OFF CASSETTES
.F8D9  38       SEC   ; SEC                    ;FAILURE FLAG
.F8DA  68       PLA   ; PLA                    ;BACK ONE SQUARE...
.F8DB  68       PLA   ; PLA ; ; LDA #0 ;STOP KEY FLAG ;
.F8DC  A9 00    LDA #$00   ; STOP3  LDA #0          ;DEALLOCATE IRQTMP
.F8DE  8D A0 02 STA $02A0   ; STA    IRQTMP+1        ;IF C-SET THEN STOP KEY
.F8E1  60       RTS   ; STOP4  RTS ; ; STT1 - SET UP TIMEOUT WATCH FOR NEXT DIPOLE ;
.F8E2  86 B1    STX $B1   ; STT1   STX TEMP        ;.X HAS CONSTANT FOR TIMEOUT
.F8E4  A5 B0    LDA $B0   ; LDA    CMP0            ;CMP0*5
.F8E6  0A       ASL   ; ASL    A
.F8E7  0A       ASL   ; ASL    A
.F8E8  18       CLC   ; CLC
.F8E9  65 B0    ADC $B0   ; ADC    CMP0
.F8EB  18       CLC   ; CLC
.F8EC  65 B1    ADC $B1   ; ADC    TEMP            ;ADJUST LONG BYTE COUNT
.F8EE  85 B1    STA $B1   ; STA    TEMP
.F8F0  A9 00    LDA #$00   ; LDA    #0
.F8F2  24 B0    BIT $B0   ; BIT    CMP0            ;CHECK CMP0 ...
.F8F4  30 01    BMI $F8F7   ; BMI    STT2            ;...MINUS, NO ADJUST
.F8F6  2A       ROL   ; ROL    A               ;...PLUS SO ADJUST POS
.F8F7  06 B1    ASL $B1   ; STT2   ASL TEMP        ;MULTIPLY CORRECTED VALUE BY 4
.F8F9  2A       ROL   ; ROL    A
.F8FA  06 B1    ASL $B1   ; ASL    TEMP
.F8FC  2A       ROL   ; ROL    A
.F8FD  AA       TAX   ; TAX
.F8FE  AD 06 DC LDA $DC06   ; STT3   LDA D1T2L       ;WATCH OUT FOR D1T2H ROLLOVER...
.F901  C9 16    CMP #$16   ; CMP    #22             ;...TIME FOR ROUTINE...!!!...
.F903  90 F9    BCC $F8FE   ; BCC    STT3            ;...TOO CLOSE SO WAIT UNTILL PAST
.F905  65 B1    ADC $B1   ; ADC    TEMP            ;CALCULATE AND...
.F907  8D 04 DC STA $DC04   ; STA    D1T1L           ;...STORE ADUSTED TIME COUNT
.F90A  8A       TXA   ; TXA
.F90B  6D 07 DC ADC $DC07   ; ADC    D1T2H           ;ADJUST FOR HIGH TIME COUNT
.F90E  8D 05 DC STA $DC05   ; STA    D1T1H
.F911  AD A2 02 LDA $02A2   ; LDA    CASTON          ;ENABLE TIMERS
.F914  8D 0E DC STA $DC0E   ; STA    D1CRA
.F917  8D A4 02 STA $02A4   ; STA    STUPID          ;NON-ZERO MEANS AN T1 IRQ HAS NOT OCCURED YET
.F91A  AD 0D DC LDA $DC0D   ; LDA    D1ICR           ;CLEAR OLD T1 INTERRUPT
.F91D  29 10    AND #$10   ; AND    #$10            ;CHECK FOR OLD-FLAG IRQ
.F91F  F0 09    BEQ $F92A   ; BEQ    STT4            ;NO...NORMAL EXIT
.F921  A9 F9    LDA #$F9   ; LDA    #>STT4          ;PUSH SIMULATED RETURN ADDRESS ON STACK
.F923  48       PHA   ; PHA
.F924  A9 2A    LDA #$2A   ; LDA    #<STT4
.F926  48       PHA   ; PHA
.F927  4C 43 FF JMP $FF43   ; JMP    SIMIRQ
.F92A  58       CLI   ; STT4   CLI             ;ALLOW FOR RE-ENTRY CODE
.F92B  60       RTS   ; RTS .END .LIB   READ ; VARIABLES USED IN CASSETTE READ ROUTINES ; ;  REZ - COUNTS ZEROS (IF Z THEN CORRECT # OF DIPOLES) ;  RER - FLAGS ERRORS (IF Z THEN NO ERROR) ;  DIFF - USED TO PRESERVE SYNO (OUTSIDE OF BIT ROUTINES) ;  SYNO - FLAGS IF WE HAVE BLOCK SYNC (16 ZERO DIPOLES) ;  SNSW1 - FLAGS IF WE HAVE BYTE SYNC (A LONGLONG) ;  DATA - HOLDS MOST RECENT DIPOLE BIT VALUE ;  MYCH - HOLDS INPUT BYTE BEING BUILT ;  FIRT - USED TO INDICATE WHICH HALF OF DIPOLE WE'RE IN ;  SVXT - TEMP USED TO ADJUST SOFTWARE SERVO ;  TEMP - USED TO HOLD DIPOLE TIME DURING TYPE CALCULATIONS ;  PRTY - HOLDS CURRENT CALCULATED PARITY BIT ;  PRP - HAS COMBINED ERROR VALUES FROM BIT ROUTINES ;  FSBLK - INDICATE WHICH BLOCK WE'RE LOOKING AT (0 TO EXIT) ;  SHCNL - HOLDS FSBLK, USED TO DIRECT ROUTINES, BECAUSE OF EXIT CASE ;  RDFLG - HOLDS FUNCTION MODE ;     MI - WAITING FOR BLOCK SYNC ;     VS - IN DATA BLOCK READING DATA ;     NE - WAITING FOR BYTE SYNC ;  SAL - INDIRECT TO DATA STORAGE AREA ;  SHCNH - LEFT OVER FROM DEBUGGING ;  BAD - STORAGE SPACE FOR BAD READ LOCATIONS (BOTTOM OF STACK) ;  PTR1 - COUNT OF READ LOCATIONS IN ERROR (POINTER INTO BAD, MAX 61) ;  PTR2 - COUNT OF RE-READ LOCATIONS (POINTER INTO BAD, DURING RE-READ) ;  VERCHK - VERIFY OR LOAD FLAG (Z - LOADING) ;  CMP0 - SOFTWARE SERVO (+/- ADJUST TO TIME CALCS) ;  DPSW - IF NZ THEN EXPECTING LL/L COMBINATION THAT ENDS A BYTE ;  PCNTR - COUNTS DOWN FROM 8-0 FOR DATA THEN TO FF FOR PARITY ;  STUPID - HOLD INDICATOR (NZ - NO T1IRQ YET) FOR T1IRQ ;  KIKA26 - HOLDS OLD D1ICR AFTER CLEAR ON READ ;
.F92C  AE 07 DC LDX $DC07   ; READ   LDX D1T2H       ;GET TIME SINCE LAST INTERRUPT
.F92F  A0 FF    LDY #$FF   ; LDY    #$FF            ;COMPUTE COUNTER DIFFERENCE
.F931  98       TYA   ; TYA
.F932  ED 06 DC SBC $DC06   ; SBC    D1T2L
.F935  EC 07 DC CPX $DC07   ; CPX    D1T2H           ;CHECK FOR TIMER HIGH ROLLOVER...
.F938  D0 F2    BNE $F92C   ; BNE    READ            ;...YES THEN RECOMPUTE
.F93A  86 B1    STX $B1   ; STX    TEMP
.F93C  AA       TAX   ; TAX
.F93D  8C 06 DC STY $DC06   ; STY    D1T2L           ;RELOAD TIMER2 (COUNT DOWN FROM $FFFF)
.F940  8C 07 DC STY $DC07   ; STY    D1T2H
.F943  A9 19    LDA #$19   ; LDA    #$19            ;ENABLE TIMER
.F945  8D 0F DC STA $DC0F   ; STA    D1CRB
.F948  AD 0D DC LDA $DC0D   ; LDA    D1ICR           ;CLEAR READ INTERRUPT
.F94B  8D A3 02 STA $02A3   ; STA    KIKA26          ;SAVE FOR LATTER
.F94E  98       TYA   ; TYA
.F94F  E5 B1    SBC $B1   ; SBC    TEMP            ;CALCULATE HIGH
.F951  86 B1    STX $B1   ; STX    TEMP
.F953  4A       LSR   ; LSR    A               ;MOVE TWO BITS FROM HIGH TO TEMP
.F954  66 B1    ROR $B1   ; ROR    TEMP
.F956  4A       LSR   ; LSR    A
.F957  66 B1    ROR $B1   ; ROR    TEMP
.F959  A5 B0    LDA $B0   ; LDA    CMP0            ;CALC MIN PULSE VALUE
.F95B  18       CLC   ; CLC
.F95C  69 3C    ADC #$3C   ; ADC    #60
.F95E  C5 B1    CMP $B1   ; CMP    TEMP            ;IF PULSE LESS THAN MIN...
.F960  B0 4A    BCS $F9AC   ; BCS    RDBK            ;...THEN IGNORE AS NOISE
.F962  A6 9C    LDX $9C   ; LDX    DPSW            ;CHECK IF LAST BIT...
.F964  F0 03    BEQ $F969   ; BEQ    RJDJ            ;...NO THEN CONTINUE
.F966  4C 60 FA JMP $FA60   ; JMP    RADJ            ;...YES THEN GO FINISH BYTE
.F969  A6 A3    LDX $A3   ; RJDJ   LDX PCNTR       ;IF 9 BITS READ...
.F96B  30 1B    BMI $F988   ; BMI    JRAD2           ;... THEN GOTO ENDING
.F96D  A2 00    LDX #$00   ; LDX    #0              ;SET BIT VALUE TO ZERO
.F96F  69 30    ADC #$30   ; ADC    #48             ;ADD UP TO HALF WAY BETWEEN...
.F971  65 B0    ADC $B0   ; ADC    CMP0            ;...SHORT PULSE AND SYNC PULSE
.F973  C5 B1    CMP $B1   ; CMP    TEMP            ;CHECK FOR SHORT...
.F975  B0 1C    BCS $F993   ; BCS    RADX2           ;...YES IT'S A SHORT
.F977  E8       INX   ; INX                    ;SET BIT VALUE TO ONE
.F978  69 26    ADC #$26   ; ADC    #38             ;MOVE TO MIDDLE OF HIGH
.F97A  65 B0    ADC $B0   ; ADC    CMP0
.F97C  C5 B1    CMP $B1   ; CMP    TEMP            ;CHECK FOR ONE...
.F97E  B0 17    BCS $F997   ; BCS    RADL            ;...YES IT'S A ONE
.F980  69 2C    ADC #$2C   ; ADC    #44             ;MOVE TO LONGLONG
.F982  65 B0    ADC $B0   ; ADC    CMP0
.F984  C5 B1    CMP $B1   ; CMP    TEMP            ;CHECK FOR LONGLONG...
.F986  90 03    BCC $F98B   ; BCC    SRER            ;...GREATER THAN IS ERROR
.F988  4C 10 FA JMP $FA10   ; JRAD2  JMP RAD2        ;...IT'S A LONGLONG
.F98B  A5 B4    LDA $B4   ; SRER   LDA SNSW1       ;IF NOT SYNCRONIZED...
.F98D  F0 1D    BEQ $F9AC   ; BEQ    RDBK            ;...THEN NO ERROR
.F98F  85 A8    STA $A8   ; STA    RER             ;...ELSE FLAG RER
.F991  D0 19    BNE $F9AC   ; BNE    RDBK            ;JMP
.F993  E6 A9    INC $A9   ; RADX2  INC REZ         ;COUNT REZ UP ON ZEROS
.F995  B0 02    BCS $F999   ; BCS    RAD5            ;JMP
.F997  C6 A9    DEC $A9   ; RADL   DEC REZ         ;COUNT REZ DOWN ON ONES
.F999  38       SEC   ; RAD5   SEC             ;CALC ACTUAL VALUE FOR COMPARE STORE
.F99A  E9 13    SBC #$13   ; SBC    #19
.F99C  E5 B1    SBC $B1   ; SBC    TEMP            ;SUBTRACT INPUT VALUE FROM CONSTANT...
.F99E  65 92    ADC $92   ; ADC    SVXT            ;...ADD DIFFERENCE TO TEMP STORAGE...
.F9A0  85 92    STA $92   ; STA    SVXT            ;...USED LATER TO ADJUST SOFT SERVO
.F9A2  A5 A4    LDA $A4   ; LDA    FIRT            ;FLIP DIPOLE FLAG
.F9A4  49 01    EOR #$01   ; EOR    #1
.F9A6  85 A4    STA $A4   ; STA    FIRT
.F9A8  F0 2B    BEQ $F9D5   ; BEQ    RAD3            ;SECOND HALF OF DIPOLE
.F9AA  86 D7    STX $D7   ; STX    DATA            ;FIRST HALF SO STORE ITS VALUE
.F9AC  A5 B4    LDA $B4   ; RDBK   LDA SNSW1       ;IF NO BYTE START...
.F9AE  F0 22    BEQ $F9D2   ; BEQ    RADBK           ;...THEN RETURN
.F9B0  AD A3 02 LDA $02A3   ; LDA    KIKA26          ;CHECK TO SEE IF TIMER1 IRQD US...
.F9B3  29 01    AND #$01   ; AND    #$01
.F9B5  D0 05    BNE $F9BC   ; BNE    RADKX           ;...YES
.F9B7  AD A4 02 LDA $02A4   ; LDA    STUPID          ;CHECK FOR OLD T1IRQ
.F9BA  D0 16    BNE $F9D2   ; BNE    RADBK           ;NO...SO EXIT ;
.F9BC  A9 00    LDA #$00   ; RADKX  LDA #0          ;...YES, SET DIPOLE FLAG FOR FIRST HALF
.F9BE  85 A4    STA $A4   ; STA    FIRT
.F9C0  8D A4 02 STA $02A4   ; STA    STUPID          ;SET T1IRQ FLAG
.F9C3  A5 A3    LDA $A3   ; LDA    PCNTR           ;CHECK WHERE WE ARE IN BYTE...
.F9C5  10 30    BPL $F9F7   ; BPL    RAD4            ;...DOING DATA
.F9C7  30 BF    BMI $F988   ; BMI    JRAD2           ;...PROCESS PARITY
.F9C9  A2 A6    LDX #$A6   ; RADP   LDX #166        ;SET UP FOR LONGLONG TIMEOUT
.F9CB  20 E2 F8 JSR $F8E2   ; JSR    STT1
.F9CE  A5 9B    LDA $9B   ; LDA    PRTY            ;IF PARITY NOT EVEN...
.F9D0  D0 B9    BNE $F98B   ; BNE    SRER            ;...THEN GO SET ERROR
.F9D2  4C BC FE JMP $FEBC   ; RADBK  JMP PREND       ;GO RESTORE REGS AND RTI
.F9D5  A5 92    LDA $92   ; RAD3   LDA SVXT        ;ADJUST THE SOFTWARE SERVO (CMP0)
.F9D7  F0 07    BEQ $F9E0   ; BEQ    ROUT1           ;NO ADJUST
.F9D9  30 03    BMI $F9DE   ; BMI    ROUT2           ;ADJUST FOR MORE BASE TIME
.F9DB  C6 B0    DEC $B0   ; DEC    CMP0            ;ADJUST FOR LESS BASE TIME
.F9DD  2C       .BYTE $2C   ; .BYT   $2C             ;SKIP TWO BYTES
.F9DE  E6 B0    INC $B0   ; ROUT2  INC CMP0
.F9E0  A9 00    LDA #$00   ; ROUT1  LDA #0          ;CLEAR DIFFERENCE VALUE
.F9E2  85 92    STA $92   ; STA    SVXT ;CHECK FOR CONSECUTIVE LIKE VALUES IN DIPOLE...
.F9E4  E4 D7    CPX $D7   ; CPX    DATA
.F9E6  D0 0F    BNE $F9F7   ; BNE    RAD4            ;...NO, GO PROCESS INFO
.F9E8  8A       TXA   ; TXA                    ;...YES SO CHECK THE VALUES...
.F9E9  D0 A0    BNE $F98B   ; BNE    SRER            ;IF THEY WERE ONES THEN  ERROR ; CONSECUTIVE ZEROS
.F9EB  A5 A9    LDA $A9   ; LDA    REZ             ;...CHECK HOW MANY ZEROS HAVE HAPPENED
.F9ED  30 BD    BMI $F9AC   ; BMI    RDBK            ;...IF MANY DON'T CHECK
.F9EF  C9 10    CMP #$10   ; CMP    #16             ;... DO WE HAVE 16 YET?...
.F9F1  90 B9    BCC $F9AC   ; BCC    RDBK            ;....NO SO CONTINUE
.F9F3  85 96    STA $96   ; STA    SYNO            ;....YES SO FLAG SYNO (BETWEEN BLOCKS)
.F9F5  B0 B5    BCS $F9AC   ; BCS    RDBK            ;JMP
.F9F7  8A       TXA   ; RAD4   TXA             ;MOVE READ DATA TO .A
.F9F8  45 9B    EOR $9B   ; EOR    PRTY            ;CALCULATE PARITY
.F9FA  85 9B    STA $9B   ; STA    PRTY
.F9FC  A5 B4    LDA $B4   ; LDA    SNSW1           ;REAL DATA?...
.F9FE  F0 D2    BEQ $F9D2   ; BEQ    RADBK           ;...NO SO FORGET BY EXITING
.FA00  C6 A3    DEC $A3   ; DEC    PCNTR           ;DEC BIT COUNT
.FA02  30 C5    BMI $F9C9   ; BMI    RADP            ;IF MINUS THEN  TIME FOR PARITY
.FA04  46 D7    LSR $D7   ; LSR    DATA            ;SHIFT BIT FROM DATA...
.FA06  66 BF    ROR $BF   ; ROR    MYCH            ;...INTO BYTE STORAGE (MYCH) BUFFER
.FA08  A2 DA    LDX #$DA   ; LDX    #218            ;SET UP FOR NEXT DIPOLE
.FA0A  20 E2 F8 JSR $F8E2   ; JSR    STT1
.FA0D  4C BC FE JMP $FEBC   ; JMP    PREND           ;RESTORE REGS AND RTI ; RAD2 - LONGLONG HANDLER (COULD BE A LONG ONE)
.FA10  A5 96    LDA $96   ; RAD2   LDA SYNO        ;HAVE WE GOTTEN BLOCK SYNC...
.FA12  F0 04    BEQ $FA18   ; BEQ    RAD2Y           ;...NO
.FA14  A5 B4    LDA $B4   ; LDA    SNSW1           ;CHECK IF WE'VE HAD A REAL BYTE START...
.FA16  F0 07    BEQ $FA1F   ; BEQ    RAD2X           ;...NO
.FA18  A5 A3    LDA $A3   ; RAD2Y  LDA PCNTR       ;ARE WE AT END OF BYTE...
.FA1A  30 03    BMI $FA1F   ; BMI    RAD2X           ;YES...GO ADJUST FOR LONGLONG
.FA1C  4C 97 F9 JMP $F997   ; JMP    RADL            ;...NO SO TREAT IT AS A LONG ONE READ
.FA1F  46 B1    LSR $B1   ; RAD2X  LSR TEMP        ;ADJUST TIMEOUT FOR...
.FA21  A9 93    LDA #$93   ; LDA    #147            ;...LONGLONG PULSE VALUE
.FA23  38       SEC   ; SEC
.FA24  E5 B1    SBC $B1   ; SBC    TEMP
.FA26  65 B0    ADC $B0   ; ADC    CMP0
.FA28  0A       ASL   ; ASL    A
.FA29  AA       TAX   ; TAX                    ;AND SET TIMEOUT FOR LAST BIT
.FA2A  20 E2 F8 JSR $F8E2   ; JSR    STT1
.FA2D  E6 9C    INC $9C   ; INC    DPSW            ;SET BIT THROW AWAY FLAG
.FA2F  A5 B4    LDA $B4   ; LDA    SNSW1           ;IF BYTE SYNCRONIZED....
.FA31  D0 11    BNE $FA44   ; BNE    RADQ2           ;...THEN SKIP TO PASS CHAR
.FA33  A5 96    LDA $96   ; LDA    SYNO            ;THROWS OUT DATA UNTILL BLOCK SYNC...
.FA35  F0 26    BEQ $FA5D   ; BEQ    RDBK2           ;...NO BLOCK SYNC
.FA37  85 A8    STA $A8   ; STA    RER             ;FLAG DATA AS ERROR
.FA39  A9 00    LDA #$00   ; LDA    #0              ;KILL 16 SYNC FLAG
.FA3B  85 96    STA $96   ; STA    SYNO
.FA3D  A9 81    LDA #$81   ; LDA    #$81            ;SET UP FOR TIMER1 INTERRUPTS
.FA3F  8D 0D DC STA $DC0D   ; STA    D1ICR
.FA42  85 B4    STA $B4   ; STA    SNSW1           ;FLAG THAT WE HAVE BYTE SYNCRONIZED ;
.FA44  A5 96    LDA $96   ; RADQ2  LDA SYNO        ;SAVE SYNO STATUS
.FA46  85 B5    STA $B5   ; STA    DIFF
.FA48  F0 09    BEQ $FA53   ; BEQ    RADK            ;NO BLOCK SYNC, NO BYTE LOOKING
.FA4A  A9 00    LDA #$00   ; LDA    #0              ;TURN OFF BYTE SYNC SWITCH
.FA4C  85 B4    STA $B4   ; STA    SNSW1
.FA4E  A9 01    LDA #$01   ; LDA    #$01            ;DISABLE TIMER1 INTERRUPTS
.FA50  8D 0D DC STA $DC0D   ; STA    D1ICR
.FA53  A5 BF    LDA $BF   ; RADK   LDA MYCH        ;PASS CHARACTER TO BYTE ROUTINE
.FA55  85 BD    STA $BD   ; STA    OCHAR
.FA57  A5 A8    LDA $A8   ; LDA    RER             ;COMBINE ERROR VALUES WITH ZERO COUNT...
.FA59  05 A9    ORA $A9   ; ORA    REZ
.FA5B  85 B6    STA $B6   ; STA    PRP             ;...AND SAVE IN PRP
.FA5D  4C BC FE JMP $FEBC   ; RDBK2  JMP PREND       ;GO BACK AND GET LAST BYTE
.FA60  20 97 FB JSR $FB97   ; RADJ   JSR NEWCH       ;FINISH BYTE, CLR FLAGS
.FA63  85 9C    STA $9C   ; STA    DPSW            ;CLEAR BIT THROW AWAY FLAG
.FA65  A2 DA    LDX #$DA   ; LDX    #218            ;INITILIZE FOR NEXT DIPOLE
.FA67  20 E2 F8 JSR $F8E2   ; JSR    STT1
.FA6A  A5 BE    LDA $BE   ; LDA    FSBLK           ;CHECK FOR LAST VALUE
.FA6C  F0 02    BEQ $FA70   ; BEQ    RD15
.FA6E  85 A7    STA $A7   ; STA    SHCNL
```


## Commenti

### Original Disassembly (Commodore)
- **$F6FB**: ERROR1 LDA #1          ;TOO MANY FILES
- **$F6FD**: .BYT   $2C
- **$F6FE**: ERROR2 LDA #2          ;FILE OPEN
- **$F700**: .BYT   $2C
- **$F701**: ERROR3 LDA #3          ;FILE NOT OPEN
- **$F703**: .BYT   $2C
- **$F704**: ERROR4 LDA #4          ;FILE NOT FOUND
- **$F706**: .BYT   $2C
- **$F707**: ERROR5 LDA #5          ;DEVICE NOT PRESENT
- **$F709**: .BYT   $2C
- **$F70A**: ERROR6 LDA #6          ;NOT INPUT FILE
- **$F70C**: .BYT   $2C
- **$F70D**: ERROR7 LDA #7          ;NOT OUTPUT FILE
- **$F70F**: .BYT   $2C
- **$F710**: ERROR8 LDA #8          ;MISSING FILE NAME
- **$F712**: .BYT   $2C
- **$F713**: ERROR9 LDA #9          ;BAD DEVICE # ;
- **$F715**: PHA                    ;ERROR NUMBER ON STACK
- **$F716**: JSR    CLRCH           ;RESTORE I/O CHANNELS ;
- **$F719**: LDY    #MS1-MS1
- **$F71B**: BIT    MSGFLG          ;ARE WE PRINTING ERROR?
- **$F71D**: BVC    EREXIT          ;NO... ;
- **$F71F**: JSR    MSG             ;PRINT "CBM I/O ERROR #"
- **$F722**: PLA
- **$F723**: PHA
- **$F724**: ORA    #$30            ;MAKE ERROR # ASCII
- **$F726**: JSR    BSOUT           ;PRINT IT ;
- **$F729**: EREXIT PLA
- **$F72A**: SEC
- **$F72B**: RTS .END .LIB   TAPEFILE ;FAH -- FIND ANY HEADER ; ;READS TAPE DEVICE UNTIL ONE OF FOLLOWING ;BLOCK TYPES FOUND: BDFH--BASIC DATA ;FILE HEADER, BLF--BASIC LOAD FILE ;FOR SUCCESS CARRY IS CLEAR ON RETURN. ;FOR FAILURE CARRY IS SET ON RETURN. ;IN ADDITION ACCUMULATOR IS 0 IF STOP ;KEY WAS PRESSED. ;
- **$F72C**: FAH    LDA VERCK       ;SAVE OLD VERIFY
- **$F72E**: PHA
- **$F72F**: JSR    RBLK            ;READ TAPE BLOCK
- **$F732**: PLA
- **$F733**: STA    VERCK           ;RESTORE VERIFY FLAG
- **$F735**: BCS    FAH40           ;READ TERMINATED ;
- **$F737**: LDY    #0
- **$F739**: LDA    (TAPE1)Y        ;GET HEADER TYPE ;
- **$F73B**: CMP    #EOT            ;CHECK END OF TAPE?
- **$F73D**: BEQ    FAH40           ;YES...FAILURE ;
- **$F73F**: CMP    #BLF            ;BASIC LOAD FILE?
- **$F741**: BEQ    FAH50           ;YES...SUCCESS ;
- **$F743**: CMP    #PLF            ;FIXED LOAD FILE?
- **$F745**: BEQ    FAH50           ;YES...SUCCESS ;
- **$F747**: CMP    #BDFH           ;BASIC DATA FILE?
- **$F749**: BNE    FAH             ;NO...KEEP TRYING ;
- **$F74B**: FAH50  TAX             ;RETURN FILE TYPE IN .X
- **$F74C**: BIT    MSGFLG          ;PRINTING MESSAGES?
- **$F74E**: BPL    FAH45           ;NO... ;
- **$F750**: LDY    #MS17-MS1       ;PRINT "FOUND"
- **$F752**: JSR    MSG ; ;OUTPUT COMPLETE FILE NAME ;
- **$F755**: LDY    #5
- **$F757**: FAH55  LDA (TAPE1)Y
- **$F759**: JSR    BSOUT
- **$F75C**: INY
- **$F75D**: CPY    #21
- **$F75F**: BNE    FAH55 ;
- **$F761**: FAH56  LDA STKEY       ;KEY  DOWN ON LAST ROW...
- **$F763**: JSR FPATCH      ;GOTO PATCH...
- **$F766**: NOP ;
- **$F767**: FAH45  CLC             ;SUCCESS FLAG
- **$F768**: DEY                    ;MAKE NONZERO FOR OKAY RETURN ;
- **$F769**: FAH40  RTS ;TAPEH--WRITE TAPE HEADER ;ERROR IF TAPE BUFFER DE-ALLOCATED ;CARRY CLEAR IF O.K. ;
- **$F76A**: TAPEH  STA T1 ; ;DETERMINE ADDRESS OF BUFFER ;
- **$F76C**: JSR    ZZZ
- **$F76F**: BCC    TH40            ;BUFFER WAS DE-ALLOCATED ; ;PRESERVE START AND END ADDRESSES ;FOR CASE OF HEADER FOR LOAD FILE ;
- **$F771**: LDA    STAH
- **$F773**: PHA
- **$F774**: LDA    STAL
- **$F776**: PHA
- **$F777**: LDA    EAH
- **$F779**: PHA
- **$F77A**: LDA    EAL
- **$F77C**: PHA ; ;PUT BLANKS IN TAPE BUFFER ;
- **$F77D**: LDY    #BUFSZ-1
- **$F77F**: LDA    #'
- **$F781**: BLNK2  STA (TAPE1)Y
- **$F783**: DEY
- **$F784**: BNE    BLNK2 ; ;PUT BLOCK TYPE IN HEADER ;
- **$F786**: LDA    T1
- **$F788**: STA    (TAPE1)Y ; ;PUT START LOAD ADDRESS IN HEADER ;
- **$F78A**: INY
- **$F78B**: LDA    STAL
- **$F78D**: STA    (TAPE1)Y
- **$F78F**: INY
- **$F790**: LDA    STAH
- **$F792**: STA    (TAPE1)Y ; ;PUT END LOAD ADDRESS IN HEADER ;
- **$F794**: INY
- **$F795**: LDA    EAL
- **$F797**: STA    (TAPE1)Y
- **$F799**: INY
- **$F79A**: LDA    EAH
- **$F79C**: STA    (TAPE1)Y ; ;PUT FILE NAME IN HEADER ;
- **$F79E**: INY
- **$F79F**: STY    T2
- **$F7A1**: LDY    #0
- **$F7A3**: STY    T1
- **$F7A5**: TH20   LDY T1
- **$F7A7**: CPY    FNLEN
- **$F7A9**: BEQ    TH30
- **$F7AB**: LDA    (FNADR)Y
- **$F7AD**: LDY    T2
- **$F7AF**: STA    (TAPE1)Y
- **$F7B1**: INC    T1
- **$F7B3**: INC    T2
- **$F7B5**: BNE    TH20 ; ;SET UP START AND END ADDRESS OF HEADER ;
- **$F7B7**: TH30   JSR LDAD1 ; ;SET UP TIME FOR LEADER ;
- **$F7BA**: LDA    #$69
- **$F7BC**: STA    SHCNH ;
- **$F7BE**: JSR    TWRT2           ;WRITE HEADER ON TAPE ; ;RESTORE START AND END ADDRESS OF ;LOAD FILE. ;
- **$F7C1**: TAY                    ;SAVE ERROR CODE IN .Y
- **$F7C2**: PLA
- **$F7C3**: STA    EAL
- **$F7C5**: PLA
- **$F7C6**: STA    EAH
- **$F7C8**: PLA
- **$F7C9**: STA    STAL
- **$F7CB**: PLA
- **$F7CC**: STA    STAH
- **$F7CE**: TYA                    ;RESTORE ERROR CODE FOR RETURN ;
- **$F7CF**: TH40   RTS ;FUNCTION TO RETURN TAPE BUFFER ;ADDRESS IN TAPE1 ;
- **$F7D0**: ZZZ    LDX TAPE1       ;ASSUME TAPE1
- **$F7D2**: LDY    TAPE1+1
- **$F7D4**: CPY    #>BUF           ;CHECK FOR ALLOCATION... ;...[TAPE1+1]=0 OR 1 MEANS DEALLOCATED ;...C CLR => DEALLOCATED
- **$F7D6**: RTS
- **$F7D7**: LDAD1  JSR ZZZ         ;GET PTR TO CASSETTE
- **$F7DA**: TXA
- **$F7DB**: STA    STAL            ;SAVE START LOW
- **$F7DD**: CLC
- **$F7DE**: ADC    #BUFSZ          ;COMPUTE POINTER TO END
- **$F7E0**: STA    EAL             ;SAVE END LOW
- **$F7E2**: TYA
- **$F7E3**: STA    STAH            ;SAVE START HIGH
- **$F7E5**: ADC    #0              ;COMPUTE POINTER TO END
- **$F7E7**: STA    EAH             ;SAVE END HIGH
- **$F7E9**: RTS
- **$F7EA**: FAF    JSR FAH         ;FIND ANY HEADER
- **$F7ED**: BCS    FAF40           ;FAILED ; ;SUCCESS...SEE IF RIGHT NAME ;
- **$F7EF**: LDY    #5              ;OFFSET INTO TAPE HEADER
- **$F7F1**: STY    T2
- **$F7F3**: LDY    #0              ;OFFSET INTO FILE NAME
- **$F7F5**: STY    T1
- **$F7F7**: FAF20  CPY FNLEN       ;COMPARE THIS MANY
- **$F7F9**: BEQ    FAF30           ;DONE ;
- **$F7FB**: LDA    (FNADR)Y
- **$F7FD**: LDY    T2
- **$F7FF**: CMP    (TAPE1)Y
- **$F801**: BNE    FAF             ;MISMATCH--TRY NEXT HEADER
- **$F803**: INC    T1
- **$F805**: INC    T2
- **$F807**: LDY    T1
- **$F809**: BNE    FAF20           ;BRANCH ALWAYS ;
- **$F80B**: FAF30  CLC             ;SUCCESS FLAG
- **$F80C**: FAF40  RTS .END .LIB   TAPECONTROL
- **$F80D**: JTP20  JSR ZZZ
- **$F810**: INC    BUFPT
- **$F812**: LDY    BUFPT
- **$F814**: CPY    #BUFSZ
- **$F816**: RTS ;STAYS IN ROUTINE D2T1LL PLAY SWITCH ;
- **$F817**: CSTE1  JSR CS10
- **$F81A**: BEQ    CS25
- **$F81C**: LDY    #MS7-MS1        ;"PRESS PLAY..."
- **$F81E**: CS30   JSR MSG
- **$F821**: CS40   JSR TSTOP       ;WATCH FOR STOP KEY
- **$F824**: JSR    CS10            ;WATCH CASSETTE SWITCHES
- **$F827**: BNE    CS40
- **$F829**: LDY    #MS18-MS1       ;"OK"
- **$F82B**: JMP    MSG ;SUBR RETURNS <> FOR CASSETTE SWITCH ;
- **$F82E**: CS10   LDA #$10        ;CHECK PORT
- **$F830**: BIT    R6510           ;CLOSED?...
- **$F832**: BNE    CS25            ;NO. . .
- **$F834**: BIT    R6510           ;CHECK AGAIN TO DEBOUNCE
- **$F836**: CS25   CLC             ;GOOD RETURN
- **$F837**: RTS ;CHECKS FOR PLAY & RECORD ;
- **$F838**: CSTE2  JSR CS10
- **$F83B**: BEQ    CS25
- **$F83D**: LDY    #MS8-MS1        ;"RECORD"
- **$F83F**: BNE    CS30 ;READ HEADER BLOCK ENTRY ;
- **$F841**: RBLK   LDA #0
- **$F843**: STA    STATUS
- **$F845**: STA    VERCK
- **$F847**: JSR    LDAD1 ;READ LOAD BLOCK ENTRY ;
- **$F84A**: TRD    JSR CSTE1       ;SAY 'PRESS PLAY'
- **$F84D**: BCS    TWRT3           ;STOP KEY PRESSED
- **$F84F**: SEI
- **$F850**: LDA    #0              ;CLEAR FLAGS...
- **$F852**: STA    RDFLG
- **$F854**: STA    SNSW1
- **$F856**: STA    CMP0
- **$F858**: STA    PTR1
- **$F85A**: STA    PTR2
- **$F85C**: STA    DPSW
- **$F85E**: LDA    #$90            ;ENABLE FOR CA1 IRQ...READ LINE
- **$F860**: LDX    #14             ;POINT IRQ VECTOR TO READ
- **$F862**: BNE    TAPE            ;JMP ;WRITE HEADER BLOCK ENTRY ;
- **$F864**: WBLK   JSR LDAD1 ; ;WRITE LOAD BLOCK ENTRY ;
- **$F867**: TWRT   LDA #20         ;BETWEEN BLOCK SHORTS
- **$F869**: STA    SHCNH
- **$F86B**: TWRT2  JSR CSTE2       ;SAY 'PRESS PLAY & RECORD'
- **$F86E**: TWRT3  BCS STOP3       ;STOP KEY PRESSED
- **$F870**: SEI
- **$F871**: LDA    #$82            ;ENABLE T2 IRQS...WRITE TIME
- **$F873**: LDX    #8              ;VECTOR IRQ TO WRTZ ;START TAPE OPERATION ENTRY POINT ;
- **$F875**: TAPE   LDY #$7F        ;KILL UNWANTED IRQ'S
- **$F877**: STY D1ICR
- **$F87A**: STA D1ICR       ;TURN ON WANTED
- **$F87D**: LDA D1CRA       ;CALC TIMER ENABLES
- **$F880**: ORA #$19
- **$F882**: STA D1CRB       ;TURN ON T2 IRQ'S FOR CASS WRITE(ONE SHOT)
- **$F885**: AND #$91        ;SAVE TOD 50/60 INDICATION
- **$F887**: STA CASTON      ;PLACE IN AUTO MODE FOR T1 ; WAIT FOR RS-232 TO FINISH
- **$F88A**: JSR RSP232 ; DISABLE SCREEN DISPLAY
- **$F88D**: LDA VICREG+17
- **$F890**: AND #$FF-$10    ;DISABLE SCREEN
- **$F892**: STA VICREG+17 ; MOVE IRQ TO IRQTEMP FOR CASS OPS
- **$F895**: LDA    CINV
- **$F898**: STA    IRQTMP
- **$F89B**: LDA    CINV+1
- **$F89E**: STA    IRQTMP+1
- **$F8A1**: JSR    BSIV            ;GO CHANGE IRQ VECTOR
- **$F8A4**: LDA    #2              ;FSBLK STARTS AT 2
- **$F8A6**: STA    FSBLK
- **$F8A8**: JSR    NEWCH           ;PREP LOCAL COUNTERS AND FLAGS
- **$F8AB**: LDA    R6510           ;TURN MOTOR ON
- **$F8AD**: AND    #%011111        ;LOW TURNS ON
- **$F8AF**: STA    R6510
- **$F8B1**: STA    CAS1            ;FLAG INTERNAL CONTROL OF CASS MOTOR
- **$F8B3**: LDX    #$FF            ;DELAY BETWEEN BLOCKS
- **$F8B5**: TP32   LDY #$FF
- **$F8B7**: TP35   DEY
- **$F8B8**: BNE    TP35
- **$F8BA**: DEX
- **$F8BB**: BNE    TP32
- **$F8BD**: CLI
- **$F8BE**: TP40   LDA IRQTMP+1    ;CHECK FOR INTERRUPT VECTOR...
- **$F8C1**: CMP    CINV+1          ;...POINTING AT KEY ROUTINE
- **$F8C4**: CLC
- **$F8C5**: BEQ    STOP3           ;...YES RETURN
- **$F8C7**: JSR    TSTOP           ;...NO CHECK FOR STOP KEY ; ; 60 HZ KEYSCAN IGNORED ;
- **$F8CA**: JSR    UD60            ; STOP KEY CHECK
- **$F8CD**: JMP    TP40            ;STAY IN LOOP UNTILL TAPES ARE DONE
- **$F8D0**: TSTOP  JSR STOP        ;STOP KEY DOWN?
- **$F8D3**: CLC                    ;ASSUME NO STOP
- **$F8D4**: BNE    STOP4           ;WE WERE RIGHT ; ;STOP KEY DOWN... ;
- **$F8D6**: JSR    TNIF            ;TURN OFF CASSETTES
- **$F8D9**: SEC                    ;FAILURE FLAG
- **$F8DA**: PLA                    ;BACK ONE SQUARE...
- **$F8DB**: PLA ; ; LDA #0 ;STOP KEY FLAG ;
- **$F8DC**: STOP3  LDA #0          ;DEALLOCATE IRQTMP
- **$F8DE**: STA    IRQTMP+1        ;IF C-SET THEN STOP KEY
- **$F8E1**: STOP4  RTS ; ; STT1 - SET UP TIMEOUT WATCH FOR NEXT DIPOLE ;
- **$F8E2**: STT1   STX TEMP        ;.X HAS CONSTANT FOR TIMEOUT
- **$F8E4**: LDA    CMP0            ;CMP0*5
- **$F8E6**: ASL    A
- **$F8E7**: ASL    A
- **$F8E8**: CLC
- **$F8E9**: ADC    CMP0
- **$F8EB**: CLC
- **$F8EC**: ADC    TEMP            ;ADJUST LONG BYTE COUNT
- **$F8EE**: STA    TEMP
- **$F8F0**: LDA    #0
- **$F8F2**: BIT    CMP0            ;CHECK CMP0 ...
- **$F8F4**: BMI    STT2            ;...MINUS, NO ADJUST
- **$F8F6**: ROL    A               ;...PLUS SO ADJUST POS
- **$F8F7**: STT2   ASL TEMP        ;MULTIPLY CORRECTED VALUE BY 4
- **$F8F9**: ROL    A
- **$F8FA**: ASL    TEMP
- **$F8FC**: ROL    A
- **$F8FD**: TAX
- **$F8FE**: STT3   LDA D1T2L       ;WATCH OUT FOR D1T2H ROLLOVER...
- **$F901**: CMP    #22             ;...TIME FOR ROUTINE...!!!...
- **$F903**: BCC    STT3            ;...TOO CLOSE SO WAIT UNTILL PAST
- **$F905**: ADC    TEMP            ;CALCULATE AND...
- **$F907**: STA    D1T1L           ;...STORE ADUSTED TIME COUNT
- **$F90A**: TXA
- **$F90B**: ADC    D1T2H           ;ADJUST FOR HIGH TIME COUNT
- **$F90E**: STA    D1T1H
- **$F911**: LDA    CASTON          ;ENABLE TIMERS
- **$F914**: STA    D1CRA
- **$F917**: STA    STUPID          ;NON-ZERO MEANS AN T1 IRQ HAS NOT OCCURED YET
- **$F91A**: LDA    D1ICR           ;CLEAR OLD T1 INTERRUPT
- **$F91D**: AND    #$10            ;CHECK FOR OLD-FLAG IRQ
- **$F91F**: BEQ    STT4            ;NO...NORMAL EXIT
- **$F921**: LDA    #>STT4          ;PUSH SIMULATED RETURN ADDRESS ON STACK
- **$F923**: PHA
- **$F924**: LDA    #<STT4
- **$F926**: PHA
- **$F927**: JMP    SIMIRQ
- **$F92A**: STT4   CLI             ;ALLOW FOR RE-ENTRY CODE
- **$F92B**: RTS .END .LIB   READ ; VARIABLES USED IN CASSETTE READ ROUTINES ; ;  REZ - COUNTS ZEROS (IF Z THEN CORRECT # OF DIPOLES) ;  RER - FLAGS ERRORS (IF Z THEN NO ERROR) ;  DIFF - USED TO PRESERVE SYNO (OUTSIDE OF BIT ROUTINES) ;  SYNO - FLAGS IF WE HAVE BLOCK SYNC (16 ZERO DIPOLES) ;  SNSW1 - FLAGS IF WE HAVE BYTE SYNC (A LONGLONG) ;  DATA - HOLDS MOST RECENT DIPOLE BIT VALUE ;  MYCH - HOLDS INPUT BYTE BEING BUILT ;  FIRT - USED TO INDICATE WHICH HALF OF DIPOLE WE'RE IN ;  SVXT - TEMP USED TO ADJUST SOFTWARE SERVO ;  TEMP - USED TO HOLD DIPOLE TIME DURING TYPE CALCULATIONS ;  PRTY - HOLDS CURRENT CALCULATED PARITY BIT ;  PRP - HAS COMBINED ERROR VALUES FROM BIT ROUTINES ;  FSBLK - INDICATE WHICH BLOCK WE'RE LOOKING AT (0 TO EXIT) ;  SHCNL - HOLDS FSBLK, USED TO DIRECT ROUTINES, BECAUSE OF EXIT CASE ;  RDFLG - HOLDS FUNCTION MODE ;     MI - WAITING FOR BLOCK SYNC ;     VS - IN DATA BLOCK READING DATA ;     NE - WAITING FOR BYTE SYNC ;  SAL - INDIRECT TO DATA STORAGE AREA ;  SHCNH - LEFT OVER FROM DEBUGGING ;  BAD - STORAGE SPACE FOR BAD READ LOCATIONS (BOTTOM OF STACK) ;  PTR1 - COUNT OF READ LOCATIONS IN ERROR (POINTER INTO BAD, MAX 61) ;  PTR2 - COUNT OF RE-READ LOCATIONS (POINTER INTO BAD, DURING RE-READ) ;  VERCHK - VERIFY OR LOAD FLAG (Z - LOADING) ;  CMP0 - SOFTWARE SERVO (+/- ADJUST TO TIME CALCS) ;  DPSW - IF NZ THEN EXPECTING LL/L COMBINATION THAT ENDS A BYTE ;  PCNTR - COUNTS DOWN FROM 8-0 FOR DATA THEN TO FF FOR PARITY ;  STUPID - HOLD INDICATOR (NZ - NO T1IRQ YET) FOR T1IRQ ;  KIKA26 - HOLDS OLD D1ICR AFTER CLEAR ON READ ;
- **$F92C**: READ   LDX D1T2H       ;GET TIME SINCE LAST INTERRUPT
- **$F92F**: LDY    #$FF            ;COMPUTE COUNTER DIFFERENCE
- **$F931**: TYA
- **$F932**: SBC    D1T2L
- **$F935**: CPX    D1T2H           ;CHECK FOR TIMER HIGH ROLLOVER...
- **$F938**: BNE    READ            ;...YES THEN RECOMPUTE
- **$F93A**: STX    TEMP
- **$F93C**: TAX
- **$F93D**: STY    D1T2L           ;RELOAD TIMER2 (COUNT DOWN FROM $FFFF)
- **$F940**: STY    D1T2H
- **$F943**: LDA    #$19            ;ENABLE TIMER
- **$F945**: STA    D1CRB
- **$F948**: LDA    D1ICR           ;CLEAR READ INTERRUPT
- **$F94B**: STA    KIKA26          ;SAVE FOR LATTER
- **$F94E**: TYA
- **$F94F**: SBC    TEMP            ;CALCULATE HIGH
- **$F951**: STX    TEMP
- **$F953**: LSR    A               ;MOVE TWO BITS FROM HIGH TO TEMP
- **$F954**: ROR    TEMP
- **$F956**: LSR    A
- **$F957**: ROR    TEMP
- **$F959**: LDA    CMP0            ;CALC MIN PULSE VALUE
- **$F95B**: CLC
- **$F95C**: ADC    #60
- **$F95E**: CMP    TEMP            ;IF PULSE LESS THAN MIN...
- **$F960**: BCS    RDBK            ;...THEN IGNORE AS NOISE
- **$F962**: LDX    DPSW            ;CHECK IF LAST BIT...
- **$F964**: BEQ    RJDJ            ;...NO THEN CONTINUE
- **$F966**: JMP    RADJ            ;...YES THEN GO FINISH BYTE
- **$F969**: RJDJ   LDX PCNTR       ;IF 9 BITS READ...
- **$F96B**: BMI    JRAD2           ;... THEN GOTO ENDING
- **$F96D**: LDX    #0              ;SET BIT VALUE TO ZERO
- **$F96F**: ADC    #48             ;ADD UP TO HALF WAY BETWEEN...
- **$F971**: ADC    CMP0            ;...SHORT PULSE AND SYNC PULSE
- **$F973**: CMP    TEMP            ;CHECK FOR SHORT...
- **$F975**: BCS    RADX2           ;...YES IT'S A SHORT
- **$F977**: INX                    ;SET BIT VALUE TO ONE
- **$F978**: ADC    #38             ;MOVE TO MIDDLE OF HIGH
- **$F97A**: ADC    CMP0
- **$F97C**: CMP    TEMP            ;CHECK FOR ONE...
- **$F97E**: BCS    RADL            ;...YES IT'S A ONE
- **$F980**: ADC    #44             ;MOVE TO LONGLONG
- **$F982**: ADC    CMP0
- **$F984**: CMP    TEMP            ;CHECK FOR LONGLONG...
- **$F986**: BCC    SRER            ;...GREATER THAN IS ERROR
- **$F988**: JRAD2  JMP RAD2        ;...IT'S A LONGLONG
- **$F98B**: SRER   LDA SNSW1       ;IF NOT SYNCRONIZED...
- **$F98D**: BEQ    RDBK            ;...THEN NO ERROR
- **$F98F**: STA    RER             ;...ELSE FLAG RER
- **$F991**: BNE    RDBK            ;JMP
- **$F993**: RADX2  INC REZ         ;COUNT REZ UP ON ZEROS
- **$F995**: BCS    RAD5            ;JMP
- **$F997**: RADL   DEC REZ         ;COUNT REZ DOWN ON ONES
- **$F999**: RAD5   SEC             ;CALC ACTUAL VALUE FOR COMPARE STORE
- **$F99A**: SBC    #19
- **$F99C**: SBC    TEMP            ;SUBTRACT INPUT VALUE FROM CONSTANT...
- **$F99E**: ADC    SVXT            ;...ADD DIFFERENCE TO TEMP STORAGE...
- **$F9A0**: STA    SVXT            ;...USED LATER TO ADJUST SOFT SERVO
- **$F9A2**: LDA    FIRT            ;FLIP DIPOLE FLAG
- **$F9A4**: EOR    #1
- **$F9A6**: STA    FIRT
- **$F9A8**: BEQ    RAD3            ;SECOND HALF OF DIPOLE
- **$F9AA**: STX    DATA            ;FIRST HALF SO STORE ITS VALUE
- **$F9AC**: RDBK   LDA SNSW1       ;IF NO BYTE START...
- **$F9AE**: BEQ    RADBK           ;...THEN RETURN
- **$F9B0**: LDA    KIKA26          ;CHECK TO SEE IF TIMER1 IRQD US...
- **$F9B3**: AND    #$01
- **$F9B5**: BNE    RADKX           ;...YES
- **$F9B7**: LDA    STUPID          ;CHECK FOR OLD T1IRQ
- **$F9BA**: BNE    RADBK           ;NO...SO EXIT ;
- **$F9BC**: RADKX  LDA #0          ;...YES, SET DIPOLE FLAG FOR FIRST HALF
- **$F9BE**: STA    FIRT
- **$F9C0**: STA    STUPID          ;SET T1IRQ FLAG
- **$F9C3**: LDA    PCNTR           ;CHECK WHERE WE ARE IN BYTE...
- **$F9C5**: BPL    RAD4            ;...DOING DATA
- **$F9C7**: BMI    JRAD2           ;...PROCESS PARITY
- **$F9C9**: RADP   LDX #166        ;SET UP FOR LONGLONG TIMEOUT
- **$F9CB**: JSR    STT1
- **$F9CE**: LDA    PRTY            ;IF PARITY NOT EVEN...
- **$F9D0**: BNE    SRER            ;...THEN GO SET ERROR
- **$F9D2**: RADBK  JMP PREND       ;GO RESTORE REGS AND RTI
- **$F9D5**: RAD3   LDA SVXT        ;ADJUST THE SOFTWARE SERVO (CMP0)
- **$F9D7**: BEQ    ROUT1           ;NO ADJUST
- **$F9D9**: BMI    ROUT2           ;ADJUST FOR MORE BASE TIME
- **$F9DB**: DEC    CMP0            ;ADJUST FOR LESS BASE TIME
- **$F9DD**: .BYT   $2C             ;SKIP TWO BYTES
- **$F9DE**: ROUT2  INC CMP0
- **$F9E0**: ROUT1  LDA #0          ;CLEAR DIFFERENCE VALUE
- **$F9E2**: STA    SVXT ;CHECK FOR CONSECUTIVE LIKE VALUES IN DIPOLE...
- **$F9E4**: CPX    DATA
- **$F9E6**: BNE    RAD4            ;...NO, GO PROCESS INFO
- **$F9E8**: TXA                    ;...YES SO CHECK THE VALUES...
- **$F9E9**: BNE    SRER            ;IF THEY WERE ONES THEN  ERROR ; CONSECUTIVE ZEROS
- **$F9EB**: LDA    REZ             ;...CHECK HOW MANY ZEROS HAVE HAPPENED
- **$F9ED**: BMI    RDBK            ;...IF MANY DON'T CHECK
- **$F9EF**: CMP    #16             ;... DO WE HAVE 16 YET?...
- **$F9F1**: BCC    RDBK            ;....NO SO CONTINUE
- **$F9F3**: STA    SYNO            ;....YES SO FLAG SYNO (BETWEEN BLOCKS)
- **$F9F5**: BCS    RDBK            ;JMP
- **$F9F7**: RAD4   TXA             ;MOVE READ DATA TO .A
- **$F9F8**: EOR    PRTY            ;CALCULATE PARITY
- **$F9FA**: STA    PRTY
- **$F9FC**: LDA    SNSW1           ;REAL DATA?...
- **$F9FE**: BEQ    RADBK           ;...NO SO FORGET BY EXITING
- **$FA00**: DEC    PCNTR           ;DEC BIT COUNT
- **$FA02**: BMI    RADP            ;IF MINUS THEN  TIME FOR PARITY
- **$FA04**: LSR    DATA            ;SHIFT BIT FROM DATA...
- **$FA06**: ROR    MYCH            ;...INTO BYTE STORAGE (MYCH) BUFFER
- **$FA08**: LDX    #218            ;SET UP FOR NEXT DIPOLE
- **$FA0A**: JSR    STT1
- **$FA0D**: JMP    PREND           ;RESTORE REGS AND RTI ; RAD2 - LONGLONG HANDLER (COULD BE A LONG ONE)
- **$FA10**: RAD2   LDA SYNO        ;HAVE WE GOTTEN BLOCK SYNC...
- **$FA12**: BEQ    RAD2Y           ;...NO
- **$FA14**: LDA    SNSW1           ;CHECK IF WE'VE HAD A REAL BYTE START...
- **$FA16**: BEQ    RAD2X           ;...NO
- **$FA18**: RAD2Y  LDA PCNTR       ;ARE WE AT END OF BYTE...
- **$FA1A**: BMI    RAD2X           ;YES...GO ADJUST FOR LONGLONG
- **$FA1C**: JMP    RADL            ;...NO SO TREAT IT AS A LONG ONE READ
- **$FA1F**: RAD2X  LSR TEMP        ;ADJUST TIMEOUT FOR...
- **$FA21**: LDA    #147            ;...LONGLONG PULSE VALUE
- **$FA23**: SEC
- **$FA24**: SBC    TEMP
- **$FA26**: ADC    CMP0
- **$FA28**: ASL    A
- **$FA29**: TAX                    ;AND SET TIMEOUT FOR LAST BIT
- **$FA2A**: JSR    STT1
- **$FA2D**: INC    DPSW            ;SET BIT THROW AWAY FLAG
- **$FA2F**: LDA    SNSW1           ;IF BYTE SYNCRONIZED....
- **$FA31**: BNE    RADQ2           ;...THEN SKIP TO PASS CHAR
- **$FA33**: LDA    SYNO            ;THROWS OUT DATA UNTILL BLOCK SYNC...
- **$FA35**: BEQ    RDBK2           ;...NO BLOCK SYNC
- **$FA37**: STA    RER             ;FLAG DATA AS ERROR
- **$FA39**: LDA    #0              ;KILL 16 SYNC FLAG
- **$FA3B**: STA    SYNO
- **$FA3D**: LDA    #$81            ;SET UP FOR TIMER1 INTERRUPTS
- **$FA3F**: STA    D1ICR
- **$FA42**: STA    SNSW1           ;FLAG THAT WE HAVE BYTE SYNCRONIZED ;
- **$FA44**: RADQ2  LDA SYNO        ;SAVE SYNO STATUS
- **$FA46**: STA    DIFF
- **$FA48**: BEQ    RADK            ;NO BLOCK SYNC, NO BYTE LOOKING
- **$FA4A**: LDA    #0              ;TURN OFF BYTE SYNC SWITCH
- **$FA4C**: STA    SNSW1
- **$FA4E**: LDA    #$01            ;DISABLE TIMER1 INTERRUPTS
- **$FA50**: STA    D1ICR
- **$FA53**: RADK   LDA MYCH        ;PASS CHARACTER TO BYTE ROUTINE
- **$FA55**: STA    OCHAR
- **$FA57**: LDA    RER             ;COMBINE ERROR VALUES WITH ZERO COUNT...
- **$FA59**: ORA    REZ
- **$FA5B**: STA    PRP             ;...AND SAVE IN PRP
- **$FA5D**: RDBK2  JMP PREND       ;GO BACK AND GET LAST BYTE
- **$FA60**: RADJ   JSR NEWCH       ;FINISH BYTE, CLR FLAGS
- **$FA63**: STA    DPSW            ;CLEAR BIT THROW AWAY FLAG
- **$FA65**: LDX    #218            ;INITILIZE FOR NEXT DIPOLE
- **$FA67**: JSR    STT1
- **$FA6A**: LDA    FSBLK           ;CHECK FOR LAST VALUE
- **$FA6C**: BEQ    RD15
- **$FA6E**: STA    SHCNL

### Original Disassembly (—)
- **$F6FB**: 'too many files' error
- **$F6FD**: makes next line BIT $02A9
- **$F6FE**: 'file already open' error
- **$F700**: makes next line BIT $03A9
- **$F701**: 'file not open' error
- **$F703**: makes next line BIT $04A9
- **$F704**: 'file not found' error
- **$F706**: makes next line BIT $05A9
- **$F707**: 'device not present' error
- **$F709**: makes next line BIT $06A9
- **$F70A**: 'not input file' error
- **$F70C**: makes next line BIT $07A9
- **$F70D**: 'not output file' error
- **$F70F**: makes next line BIT $08A9
- **$F710**: 'missing file name' error
- **$F712**: makes next line BIT $09A9
- **$F713**: do 'illegal device number'
- **$F715**: save the error #
- **$F716**: close input and output channels
- **$F719**: index to "I/O ERROR #"
- **$F71B**: test message mode flag
- **$F71D**: exit if kernal messages off
- **$F71F**: display kernel I/O message
- **$F722**: restore error #
- **$F723**: copy error #
- **$F724**: convert to ASCII
- **$F726**: output character to channel
- **$F729**: pull error number
- **$F72A**: flag error

### Commodore-64-intern-Buch (Commodore)
- **$F6FB**: 'TOO MANY FILES'
- **$F6FD**: Skip zu $F700
- **$F6FE**: 'FILE OPEN'
- **$F700**: Skip zu $F703
- **$F701**: 'FILE NOT OPEN'
- **$F703**: Skip zu $F706
- **$F704**: 'FILE NOT FOUND'
- **$F706**: Skip zu $F709
- **$F707**: 'DIVICE NOT PRESENT'
- **$F709**: Skip zu $F70C
- **$F70A**: 'NOT INPUT FILE'
- **$F70C**: Skip zu $F70F
- **$F70D**: 'NOT OUTPUT FILE'
- **$F70F**: Skip zu $F712
- **$F710**: 'MISSING FILENAME'
- **$F712**: Skip zu $F715
- **$F713**: 'ILLEGAL DEVICE NUMBER'
- **$F715**: Fehlernummer merken
- **$F716**: Ein-Ausgabe zurücksetzen CLRCH
- **$F71B**: Flag auf Direkt-Mode testen
- **$F71D**: nicht gesetzt, dann übergehen
- **$F71F**: 'I/O ERROR #' ausgeben
- **$F722**: Fehlernummer holen
- **$F723**: und wieder merken
- **$F724**: nach ASCII wandeln
- **$F726**: und ausgeben
- **$F729**: Fehlernummer holen
- **$F72A**: Carry =1 (Fehlerkennzeichen)
- **$F72B**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$F6FB**: too many files
- **$F6FE**: file open
- **$F701**: file not open
- **$F704**: file not found
- **$F707**: device not present
- **$F70A**: not input file
- **$F70D**: not output file
- **$F710**: file name missing
- **$F713**: illegal device no.

### Magnus Nyman (Magnus Nyman)
- **$F6FB**: error #1, too many files
- **$F6FE**: error #2, file open
- **$F701**: error #3, file not open
- **$F704**: error #4, file not found
- **$F707**: error #5, device not found
- **$F70A**: error #6, not input file
- **$F70D**: error #7, not output file
- **$F710**: error #8, missing filename
- **$F713**: error #9, illegal device number
- **$F716**: CLRCHN, close all I/O channels
- **$F71B**: test MSGFLAG, KERNAL messages enabled
- **$F71D**: no
- **$F71F**: print "I/O ERROR #"
- **$F724**: convert (A) to ASCII number
- **$F726**: use CHROUT to print number in (A)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*