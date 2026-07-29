---
title: '# store character'
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
- fa60-receive-next-byte-from-cassette
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $FA60
  address_end: $FB8B
  symbol: store-character
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FA60**: new tape byte setup'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FA60 — # store character

## Disassemblatura
```assembly
.FA60  20 97 FB JSR $FB97   ; new tape byte setup
.FA63  85 9C    STA $9C   ; clear byte received flag
.FA65  A2 DA    LDX #$DA   ; set timing max byte
.FA67  20 E2 F8 JSR $F8E2   ; set timing
.FA6A  A5 BE    LDA $BE   ; get copies count
.FA6C  F0 02    BEQ $FA70
.FA6E  85 A7    STA $A7   ; save receiver input bit temporary storage
.FA70  A9 0F    LDA #$0F
.FA72  24 AA    BIT $AA
.FA74  10 17    BPL $FA8D
.FA76  A5 B5    LDA $B5
.FA78  D0 0C    BNE $FA86
.FA7A  A6 BE    LDX $BE   ; get copies count
.FA7C  CA       DEX
.FA7D  D0 0B    BNE $FA8A   ; if ?? restore registers and exit interrupt
.FA7F  A9 08    LDA #$08   ; set short block
.FA81  20 1C FE JSR $FE1C   ; OR into serial status byte
.FA84  D0 04    BNE $FA8A   ; restore registers and exit interrupt, branch always
.FA86  A9 00    LDA #$00
.FA88  85 AA    STA $AA
.FA8A  4C BC FE JMP $FEBC   ; restore registers and exit interrupt
.FA8D  70 31    BVS $FAC0
.FA8F  D0 18    BNE $FAA9
.FA91  A5 B5    LDA $B5
.FA93  D0 F5    BNE $FA8A
.FA95  A5 B6    LDA $B6
.FA97  D0 F1    BNE $FA8A
.FA99  A5 A7    LDA $A7   ; get receiver input bit temporary storage
.FA9B  4A       LSR
.FA9C  A5 BD    LDA $BD   ; get RS232 parity byte
.FA9E  30 03    BMI $FAA3
.FAA0  90 18    BCC $FABA
.FAA2  18       CLC
.FAA3  B0 15    BCS $FABA
.FAA5  29 0F    AND #$0F
.FAA7  85 AA    STA $AA
.FAA9  C6 AA    DEC $AA
.FAAB  D0 DD    BNE $FA8A
.FAAD  A9 40    LDA #$40
.FAAF  85 AA    STA $AA
.FAB1  20 8E FB JSR $FB8E   ; copy I/O start address to buffer address
.FAB4  A9 00    LDA #$00
.FAB6  85 AB    STA $AB
.FAB8  F0 D0    BEQ $FA8A
.FABA  A9 80    LDA #$80
.FABC  85 AA    STA $AA
.FABE  D0 CA    BNE $FA8A   ; restore registers and exit interrupt, branch always
.FAC0  A5 B5    LDA $B5
.FAC2  F0 0A    BEQ $FACE
.FAC4  A9 04    LDA #$04
.FAC6  20 1C FE JSR $FE1C   ; OR into serial status byte
.FAC9  A9 00    LDA #$00
.FACB  4C 4A FB JMP $FB4A
.FACE  20 D1 FC JSR $FCD1   ; check read/write pointer, return Cb = 1 if pointer >= end
.FAD1  90 03    BCC $FAD6
.FAD3  4C 48 FB JMP $FB48
.FAD6  A6 A7    LDX $A7   ; get receiver input bit temporary storage
.FAD8  CA       DEX
.FAD9  F0 2D    BEQ $FB08
.FADB  A5 93    LDA $93   ; get load/verify flag
.FADD  F0 0C    BEQ $FAEB   ; if load go ??
.FADF  A0 00    LDY #$00   ; clear index
.FAE1  A5 BD    LDA $BD   ; get RS232 parity byte
.FAE3  D1 AC    CMP ($AC),Y
.FAE5  F0 04    BEQ $FAEB
.FAE7  A9 01    LDA #$01
.FAE9  85 B6    STA $B6
.FAEB  A5 B6    LDA $B6
.FAED  F0 4B    BEQ $FB3A
.FAEF  A2 3D    LDX #$3D
.FAF1  E4 9E    CPX $9E
.FAF3  90 3E    BCC $FB33
.FAF5  A6 9E    LDX $9E
.FAF7  A5 AD    LDA $AD
.FAF9  9D 01 01 STA $0101,X
.FAFC  A5 AC    LDA $AC
.FAFE  9D 00 01 STA $0100,X
.FB01  E8       INX
.FB02  E8       INX
.FB03  86 9E    STX $9E
.FB05  4C 3A FB JMP $FB3A
.FB08  A6 9F    LDX $9F
.FB0A  E4 9E    CPX $9E
.FB0C  F0 35    BEQ $FB43
.FB0E  A5 AC    LDA $AC
.FB10  DD 00 01 CMP $0100,X
.FB13  D0 2E    BNE $FB43
.FB15  A5 AD    LDA $AD
.FB17  DD 01 01 CMP $0101,X
.FB1A  D0 27    BNE $FB43
.FB1C  E6 9F    INC $9F
.FB1E  E6 9F    INC $9F
.FB20  A5 93    LDA $93   ; get load/verify flag
.FB22  F0 0B    BEQ $FB2F   ; if load ??
.FB24  A5 BD    LDA $BD   ; get RS232 parity byte
.FB26  A0 00    LDY #$00
.FB28  D1 AC    CMP ($AC),Y
.FB2A  F0 17    BEQ $FB43
.FB2C  C8       INY
.FB2D  84 B6    STY $B6
.FB2F  A5 B6    LDA $B6
.FB31  F0 07    BEQ $FB3A
.FB33  A9 10    LDA #$10
.FB35  20 1C FE JSR $FE1C   ; OR into serial status byte
.FB38  D0 09    BNE $FB43
.FB3A  A5 93    LDA $93   ; get load/verify flag
.FB3C  D0 05    BNE $FB43   ; if verify go ??
.FB3E  A8       TAY
.FB3F  A5 BD    LDA $BD   ; get RS232 parity byte
.FB41  91 AC    STA ($AC),Y
.FB43  20 DB FC JSR $FCDB   ; increment read/write pointer
.FB46  D0 43    BNE $FB8B   ; restore registers and exit interrupt, branch always
.FB48  A9 80    LDA #$80
.FB4A  85 AA    STA $AA
.FB4C  78       SEI
.FB4D  A2 01    LDX #$01   ; disable timer A interrupt
.FB4F  8E 0D DC STX $DC0D   ; save VIA 1 ICR
.FB52  AE 0D DC LDX $DC0D   ; read VIA 1 ICR
.FB55  A6 BE    LDX $BE   ; get copies count
.FB57  CA       DEX
.FB58  30 02    BMI $FB5C
.FB5A  86 BE    STX $BE   ; save copies count
.FB5C  C6 A7    DEC $A7   ; decrement receiver input bit temporary storage
.FB5E  F0 08    BEQ $FB68
.FB60  A5 9E    LDA $9E
.FB62  D0 27    BNE $FB8B   ; if ?? restore registers and exit interrupt
.FB64  85 BE    STA $BE   ; save copies count
.FB66  F0 23    BEQ $FB8B   ; restore registers and exit interrupt, branch always
.FB68  20 93 FC JSR $FC93   ; restore everything for STOP
.FB6B  20 8E FB JSR $FB8E   ; copy I/O start address to buffer address
.FB6E  A0 00    LDY #$00   ; clear index
.FB70  84 AB    STY $AB   ; clear checksum
.FB72  B1 AC    LDA ($AC),Y   ; get byte from buffer
.FB74  45 AB    EOR $AB   ; XOR with checksum
.FB76  85 AB    STA $AB   ; save new checksum
.FB78  20 DB FC JSR $FCDB   ; increment read/write pointer
.FB7B  20 D1 FC JSR $FCD1   ; check read/write pointer, return Cb = 1 if pointer >= end
.FB7E  90 F2    BCC $FB72   ; loop if not at end
.FB80  A5 AB    LDA $AB   ; get computed checksum
.FB82  45 BD    EOR $BD   ; compare with stored checksum ??
.FB84  F0 05    BEQ $FB8B   ; if checksum ok restore registers and exit interrupt
.FB86  A9 20    LDA #$20   ; else set checksum error
.FB88  20 1C FE JSR $FE1C   ; OR into the serial status byte
.FB8B  4C BC FE JMP $FEBC   ; restore registers and exit interrupt
```


## Commenti

### Original Disassembly (—)
- **$FA60**: new tape byte setup
- **$FA63**: clear byte received flag
- **$FA65**: set timing max byte
- **$FA67**: set timing
- **$FA6A**: get copies count
- **$FA6E**: save receiver input bit temporary storage
- **$FA7A**: get copies count
- **$FA7D**: if ?? restore registers and exit interrupt
- **$FA7F**: set short block
- **$FA81**: OR into serial status byte
- **$FA84**: restore registers and exit interrupt, branch always
- **$FA8A**: restore registers and exit interrupt
- **$FA99**: get receiver input bit temporary storage
- **$FA9C**: get RS232 parity byte
- **$FAB1**: copy I/O start address to buffer address
- **$FABE**: restore registers and exit interrupt, branch always
- **$FAC6**: OR into serial status byte
- **$FACE**: check read/write pointer, return Cb = 1 if pointer >= end
- **$FAD6**: get receiver input bit temporary storage
- **$FADB**: get load/verify flag
- **$FADD**: if load go ??
- **$FADF**: clear index
- **$FAE1**: get RS232 parity byte
- **$FB20**: get load/verify flag
- **$FB22**: if load ??
- **$FB24**: get RS232 parity byte
- **$FB35**: OR into serial status byte
- **$FB3A**: get load/verify flag
- **$FB3C**: if verify go ??
- **$FB3F**: get RS232 parity byte
- **$FB43**: increment read/write pointer
- **$FB46**: restore registers and exit interrupt, branch always
- **$FB4D**: disable timer A interrupt
- **$FB4F**: save VIA 1 ICR
- **$FB52**: read VIA 1 ICR
- **$FB55**: get copies count
- **$FB5A**: save copies count
- **$FB5C**: decrement receiver input bit temporary storage
- **$FB62**: if ?? restore registers and exit interrupt
- **$FB64**: save copies count
- **$FB66**: restore registers and exit interrupt, branch always
- **$FB68**: restore everything for STOP
- **$FB6B**: copy I/O start address to buffer address
- **$FB6E**: clear index
- **$FB70**: clear checksum
- **$FB72**: get byte from buffer
- **$FB74**: XOR with checksum
- **$FB76**: save new checksum
- **$FB78**: increment read/write pointer
- **$FB7B**: check read/write pointer, return Cb = 1 if pointer >= end
- **$FB7E**: loop if not at end
- **$FB80**: get computed checksum
- **$FB82**: compare with stored checksum ??
- **$FB84**: if checksum ok restore registers and exit interrupt
- **$FB86**: else set checksum error
- **$FB88**: OR into the serial status byte
- **$FB8B**: restore registers and exit interrupt

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*