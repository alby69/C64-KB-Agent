---
title: PROCESS KEY IMAGE
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/magnus_nyman.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 00c5-lstx
- 00c6-ndx
- 00cb-sfdx
- 00f5-keytab
- 0289-xmax
- 028a-rptflg
- 028b-kount
- 028c-delay
- 028d-shflag
- 028e-lstshf
- 028f-keylog
- 0291-mode
- eadd-process-key-image
- eb48-commodore
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  address: $EADD
  address_end: $EB76
  symbol: process-key-image
  sources:
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EADD**: jump through KEYLOG vector, points to $eae0'
---

# $EADD — PROCESS KEY IMAGE

## Disassemblatura
```assembly
.EADD  6C 8F 02 JMP ($028F)   ; jump through KEYLOG vector, points to $eae0
.EAE0  A4 CB    LDY $CB   ; SFDX, number of the key we pressed
.EAE2  B1 F5    LDA ($F5),Y   ; get ASCII value from decode table
.EAE4  AA       TAX   ; temp store
.EAE5  C4 C5    CPY $C5   ; same key as former interrupt
.EAE7  F0 07    BEQ $EAF0   ; yepp
.EAE9  A0 10    LDY #$10   ; restore the repeat delay counter
.EAEB  8C 8C 02 STY $028C   ; DELAY
.EAEE  D0 36    BNE $EB26   ; always jump
.EAF0  29 7F    AND #$7F
.EAF2  2C 8A 02 BIT $028A   ; RPTFLG, test repeat mode
.EAF5  30 16    BMI $EB0D   ; repeat all keys
.EAF7  70 49    BVS $EB42   ; repeat none - exit routine
.EAF9  C9 7F    CMP #$7F
.EAFB  F0 29    BEQ $EB26
.EAFD  C9 14    CMP #$14   ; <DEL> key pressed
.EAFF  F0 0C    BEQ $EB0D   ; yepp...
.EB01  C9 20    CMP #$20   ; <space> key pressed
.EB03  F0 08    BEQ $EB0D   ; yepp...
.EB05  C9 1D    CMP #$1D   ; <CRSR LEFT/RIGHT>
.EB07  F0 04    BEQ $EB0D   ; yepp..
.EB09  C9 11    CMP #$11   ; <CRSRS DOWN/UP>
.EB0B  D0 35    BNE $EB42   ; yepp..
.EB0D  AC 8C 02 LDY $028C   ; DELAY
.EB10  F0 05    BEQ $EB17   ; skip
.EB12  CE 8C 02 DEC $028C   ; decrement DELAY
.EB15  D0 2B    BNE $EB42   ; end
.EB17  CE 8B 02 DEC $028B   ; decrement KOUNT, repeat speed counter
.EB1A  D0 26    BNE $EB42   ; end
.EB1C  A0 04    LDY #$04
.EB1E  8C 8B 02 STY $028B   ; init KOUNT
.EB21  A4 C6    LDY $C6   ; read NDX, number of keys in keyboard queue
.EB23  88       DEY
.EB24  10 1C    BPL $EB42   ; end
.EB26  A4 CB    LDY $CB   ; read SFDX
.EB28  84 C5    STY $C5   ; store in LSTX
.EB2A  AC 8D 02 LDY $028D   ; read SHFLAG
.EB2D  8C 8E 02 STY $028E   ; store in LSTSHF, last keyboard shift pattern
.EB30  E0 FF    CPX #$FF   ; no valid key pressed
.EB32  F0 0E    BEQ $EB42   ; end
.EB34  8A       TXA
.EB35  A6 C6    LDX $C6   ; NDX, number of keys in buffer
.EB37  EC 89 02 CPX $0289   ; compare to XMAX, max numbers oc characters in buffer
.EB3A  B0 06    BCS $EB42   ; buffer is full, end
.EB3C  9D 77 02 STA $0277,X   ; store new character in keyboard buffer
.EB3F  E8       INX   ; increment counter
.EB40  86 C6    STX $C6   ; and store in NDX
.EB42  A9 7F    LDA #$7F
.EB44  8D 00 DC STA $DC00   ; keyboard write register
.EB47  60       RTS   ; exit
.EB48  AD 8D 02 LDA $028D   ; SHFLAG
.EB4B  C9 03    CMP #$03   ; <SHIFT> and <CBM> at the same time
.EB4D  D0 15    BNE $EB64   ; nope
.EB4F  CD 8E 02 CMP $028E   ; same as LSTSHF
.EB52  F0 EE    BEQ $EB42   ; if so, end
.EB54  AD 91 02 LDA $0291   ; read MODE, shift key enable flag
.EB57  30 1D    BMI $EB76   ; end
.EB59  AD 18 D0 LDA $D018   ; VIC memory control register
.EB5C  49 02    EOR #$02   ; toggle character set, upper/lower case
.EB5E  8D 18 D0 STA $D018   ; and store
.EB61  4C 76 EB JMP $EB76   ; process key image
.EB64  0A       ASL
.EB65  C9 08    CMP #$08   ; test <CTRL>
.EB67  90 02    BCC $EB6B   ; nope
.EB69  A9 06    LDA #$06   ; set offset for ctrl
.EB6B  AA       TAX   ; to (X)
.EB6C  BD 79 EB LDA $EB79,X   ; read keyboard select vectors, low byte
.EB6F  85 F5    STA $F5   ; store in KEYTAB, decode table vector
.EB71  BD 7A EB LDA $EB7A,X   ; read keyboard select vectors, high byte
.EB74  85 F6    STA $F6   ; KEYTAB+1
.EB76  4C E0 EA JMP $EAE0   ; process key image
```


## Commenti

### Magnus Nyman (Magnus Nyman)
- **$EADD**: jump through KEYLOG vector, points to $eae0
- **$EAE0**: SFDX, number of the key we pressed
- **$EAE2**: get ASCII value from decode table
- **$EAE4**: temp store
- **$EAE5**: same key as former interrupt
- **$EAE7**: yepp
- **$EAE9**: restore the repeat delay counter
- **$EAEB**: DELAY
- **$EAEE**: always jump
- **$EAF2**: RPTFLG, test repeat mode
- **$EAF5**: repeat all keys
- **$EAF7**: repeat none - exit routine
- **$EAFD**: <DEL> key pressed
- **$EAFF**: yepp...
- **$EB01**: <space> key pressed
- **$EB03**: yepp...
- **$EB05**: <CRSR LEFT/RIGHT>
- **$EB07**: yepp..
- **$EB09**: <CRSRS DOWN/UP>
- **$EB0B**: yepp..
- **$EB0D**: DELAY
- **$EB10**: skip
- **$EB12**: decrement DELAY
- **$EB15**: end
- **$EB17**: decrement KOUNT, repeat speed counter
- **$EB1A**: end
- **$EB1E**: init KOUNT
- **$EB21**: read NDX, number of keys in keyboard queue
- **$EB24**: end
- **$EB26**: read SFDX
- **$EB28**: store in LSTX
- **$EB2A**: read SHFLAG
- **$EB2D**: store in LSTSHF, last keyboard shift pattern
- **$EB30**: no valid key pressed
- **$EB32**: end
- **$EB35**: NDX, number of keys in buffer
- **$EB37**: compare to XMAX, max numbers oc characters in buffer
- **$EB3A**: buffer is full, end
- **$EB3C**: store new character in keyboard buffer
- **$EB3F**: increment counter
- **$EB40**: and store in NDX
- **$EB44**: keyboard write register
- **$EB47**: exit
- **$EB48**: SHFLAG
- **$EB4B**: <SHIFT> and <CBM> at the same time
- **$EB4D**: nope
- **$EB4F**: same as LSTSHF
- **$EB52**: if so, end
- **$EB54**: read MODE, shift key enable flag
- **$EB57**: end
- **$EB59**: VIC memory control register
- **$EB5C**: toggle character set, upper/lower case
- **$EB5E**: and store
- **$EB61**: process key image
- **$EB65**: test <CTRL>
- **$EB67**: nope
- **$EB69**: set offset for ctrl
- **$EB6B**: to (X)
- **$EB6C**: read keyboard select vectors, low byte
- **$EB6F**: store in KEYTAB, decode table vector
- **$EB71**: read keyboard select vectors, high byte
- **$EB74**: KEYTAB+1
- **$EB76**: process key image

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*