---
title: set/read vectored I/O from (XY), Cb = 1 to read, Cb = 0 to set
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
- 0314-cinv
- bcc
- bpl
- dey
- fd1a-vector-kernal-move
- lda
- ldy
- rts
- sta
- stx
- sty
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $FD1A
  address_end: $FD2F
  symbol: setread-vectored-io-from-xy-cb-1-to-read-cb-0-to-set
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FD1A**: save pointer low byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FD1A**: MEMUSS - c3/c4 temporary used for address'
---

# $FD1A — set/read vectored I/O from (XY), Cb = 1 to read, Cb = 0 to set

## Disassemblatura
```assembly
.FD1A  86 C3    STX $C3   ; save pointer low byte
.FD1C  84 C4    STY $C4   ; save pointer high byte
.FD1E  A0 1F    LDY #$1F   ; set byte count
.FD20  B9 14 03 LDA $0314,Y   ; read vector byte from vectors
.FD23  B0 02    BCS $FD27   ; branch if read vectors
.FD25  B1 C3    LDA ($C3),Y   ; read vector byte from (XY)
.FD27  91 C3    STA ($C3),Y   ; save byte to (XY)
.FD29  99 14 03 STA $0314,Y   ; save byte to vector
.FD2C  88       DEY   ; decrement index
.FD2D  10 F1    BPL $FD20   ; loop if more to do
.FD2F  60       RTS   ; The above code works but it tries to write to the ROM. while this is usually harmless systems that use flash ROM may suffer. Here is a version that makes the extra write to RAM instead but is otherwise identical in function. ## set/read vectored I/O from (XY), Cb = 1 to read, Cb = 0 to set STX $C3         ; save pointer low byte STY $C4         ; save pointer high byte LDY #$1F        ; set byte count LDA ($C3),Y     ; read vector byte from (XY) BCC $FD29       ; branch if set vectors LDA $0314,Y     ; else read vector byte from vectors STA ($C3),Y     ; save byte to (XY) STA $0314,Y     ; save byte to vector DEY             ; decrement index BPL $FD20       ; loop if more to do RTS
```


## Commenti

### Original Disassembly (—)
- **$FD1A**: save pointer low byte
- **$FD1C**: save pointer high byte
- **$FD1E**: set byte count
- **$FD20**: read vector byte from vectors
- **$FD23**: branch if read vectors
- **$FD25**: read vector byte from (XY)
- **$FD27**: save byte to (XY)
- **$FD29**: save byte to vector
- **$FD2C**: decrement index
- **$FD2D**: loop if more to do
- **$FD2F**: The above code works but it tries to write to the ROM. while this is usually harmless systems that use flash ROM may suffer. Here is a version that makes the extra write to RAM instead but is otherwise identical in function. ## set/read vectored I/O from (XY), Cb = 1 to read, Cb = 0 to set STX $C3         ; save pointer low byte STY $C4         ; save pointer high byte LDY #$1F        ; set byte count LDA ($C3),Y     ; read vector byte from (XY) BCC $FD29       ; branch if set vectors LDA $0314,Y     ; else read vector byte from vectors STA ($C3),Y     ; save byte to (XY) STA $0314,Y     ; save byte to vector DEY             ; decrement index BPL $FD20       ; loop if more to do RTS

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FD1A**: MEMUSS - c3/c4 temporary used for address
- **$FD1E**: Number of bytes to transfer
- **$FD23**: Read or Write the vectors
- **$FD2D**: Again...

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*