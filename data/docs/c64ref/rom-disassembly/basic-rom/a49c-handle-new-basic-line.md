---
title: handle new BASIC line
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
- a49c-programmzeilen
- a4a9-programmzeile-lschen
- a4ed-programmzeile-einfgen
- a52a-clear-all-variables
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A49C
  address_end: $A530
  symbol: handle-new-basic-line
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A49C**: get fixed-point number into temporary integer'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A49C**: Zeilenr. nach Adressformat'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A4A2**: SAVE INDEX TO INPUT BUFFER'
---

# $A49C — handle new BASIC line

## Disassemblatura
```assembly
.A49C  20 6B A9 JSR $A96B   ; get fixed-point number into temporary integer
.A49F  20 79 A5 JSR $A579   ; crunch keywords into BASIC tokens
.A4A2  84 0B    STY $0B   ; save index pointer to end of crunched line
.A4A4  20 13 A6 JSR $A613   ; search BASIC for temporary integer line number
.A4A7  90 44    BCC $A4ED   ; if not found skip the line delete line # already exists so delete it
.A4A9  A0 01    LDY #$01   ; set index to next line pointer high byte
.A4AB  B1 5F    LDA ($5F),Y   ; get next line pointer high byte
.A4AD  85 23    STA $23   ; save it
.A4AF  A5 2D    LDA $2D   ; get start of variables low byte
.A4B1  85 22    STA $22   ; save it
.A4B3  A5 60    LDA $60   ; get found line pointer high byte
.A4B5  85 25    STA $25   ; save it
.A4B7  A5 5F    LDA $5F   ; get found line pointer low byte
.A4B9  88       DEY   ; decrement index
.A4BA  F1 5F    SBC ($5F),Y   ; subtract next line pointer low byte
.A4BC  18       CLC   ; clear carry for add
.A4BD  65 2D    ADC $2D   ; add start of variables low byte
.A4BF  85 2D    STA $2D   ; set start of variables low byte
.A4C1  85 24    STA $24   ; save destination pointer low byte
.A4C3  A5 2E    LDA $2E   ; get start of variables high byte
.A4C5  69 FF    ADC #$FF   ; -1 + carry
.A4C7  85 2E    STA $2E   ; set start of variables high byte
.A4C9  E5 60    SBC $60   ; subtract found line pointer high byte
.A4CB  AA       TAX   ; copy to block count
.A4CC  38       SEC   ; set carry for subtract
.A4CD  A5 5F    LDA $5F   ; get found line pointer low byte
.A4CF  E5 2D    SBC $2D   ; subtract start of variables low byte
.A4D1  A8       TAY   ; copy to bytes in first block count
.A4D2  B0 03    BCS $A4D7   ; branch if no underflow
.A4D4  E8       INX   ; increment block count, correct for = 0 loop exit
.A4D5  C6 25    DEC $25   ; decrement destination high byte
.A4D7  18       CLC   ; clear carry for add
.A4D8  65 22    ADC $22   ; add source pointer low byte
.A4DA  90 03    BCC $A4DF   ; branch if no overflow
.A4DC  C6 23    DEC $23   ; else decrement source pointer high byte
.A4DE  18       CLC   ; clear carry close up memory to delete old line
.A4DF  B1 22    LDA ($22),Y   ; get byte from source
.A4E1  91 24    STA ($24),Y   ; copy to destination
.A4E3  C8       INY   ; increment index
.A4E4  D0 F9    BNE $A4DF   ; while <> 0 do this block
.A4E6  E6 23    INC $23   ; increment source pointer high byte
.A4E8  E6 25    INC $25   ; increment destination pointer high byte
.A4EA  CA       DEX   ; decrement block count
.A4EB  D0 F2    BNE $A4DF   ; loop until all done got new line in buffer and no existing same #
.A4ED  20 59 A6 JSR $A659   ; reset execution to start, clear variables, flush stack and return
.A4F0  20 33 A5 JSR $A533   ; rebuild BASIC line chaining
.A4F3  AD 00 02 LDA $0200   ; get first byte from buffer
.A4F6  F0 88    BEQ $A480   ; if no line go do BASIC warm start else insert line into memory
.A4F8  18       CLC   ; clear carry for add
.A4F9  A5 2D    LDA $2D   ; get start of variables low byte
.A4FB  85 5A    STA $5A   ; save as source end pointer low byte
.A4FD  65 0B    ADC $0B   ; add index pointer to end of crunched line
.A4FF  85 58    STA $58   ; save as destination end pointer low byte
.A501  A4 2E    LDY $2E   ; get start of variables high byte
.A503  84 5B    STY $5B   ; save as source end pointer high byte
.A505  90 01    BCC $A508   ; branch if no carry to high byte
.A507  C8       INY   ; else increment high byte
.A508  84 59    STY $59   ; save as destination end pointer high byte
.A50A  20 B8 A3 JSR $A3B8   ; open up space in memory most of what remains to do is copy the crunched line into the space opened up in memory, however, before the crunched line comes the next line pointer and the line number. the line number is retrieved from the temporary integer and stored in memory, this overwrites the bottom two bytes on the stack. next the line is copied and the next line pointer is filled with whatever was in two bytes above the line number in the stack. this is ok because the line pointer gets fixed in the line chain re-build.
.A50D  A5 14    LDA $14   ; get line number low byte
.A50F  A4 15    LDY $15   ; get line number high byte
.A511  8D FE 01 STA $01FE   ; save line number low byte before crunched line
.A514  8C FF 01 STY $01FF   ; save line number high byte before crunched line
.A517  A5 31    LDA $31   ; get end of arrays low byte
.A519  A4 32    LDY $32   ; get end of arrays high byte
.A51B  85 2D    STA $2D   ; set start of variables low byte
.A51D  84 2E    STY $2E   ; set start of variables high byte
.A51F  A4 0B    LDY $0B   ; get index to end of crunched line
.A521  88       DEY   ; -1
.A522  B9 FC 01 LDA $01FC,Y   ; get byte from crunched line
.A525  91 5F    STA ($5F),Y   ; save byte to memory
.A527  88       DEY   ; decrement index
.A528  10 F8    BPL $A522   ; loop while more to do reset execution, clear variables, flush stack, rebuild BASIC chain and do warm start
.A52A  20 59 A6 JSR $A659   ; reset execution to start, clear variables and flush stack
.A52D  20 33 A5 JSR $A533   ; rebuild BASIC line chaining
.A530  4C 80 A4 JMP $A480   ; go do BASIC warm start
```


## Commenti

### Original Disassembly (—)
- **$A49C**: get fixed-point number into temporary integer
- **$A49F**: crunch keywords into BASIC tokens
- **$A4A2**: save index pointer to end of crunched line
- **$A4A4**: search BASIC for temporary integer line number
- **$A4A7**: if not found skip the line delete line # already exists so delete it
- **$A4A9**: set index to next line pointer high byte
- **$A4AB**: get next line pointer high byte
- **$A4AD**: save it
- **$A4AF**: get start of variables low byte
- **$A4B1**: save it
- **$A4B3**: get found line pointer high byte
- **$A4B5**: save it
- **$A4B7**: get found line pointer low byte
- **$A4B9**: decrement index
- **$A4BA**: subtract next line pointer low byte
- **$A4BC**: clear carry for add
- **$A4BD**: add start of variables low byte
- **$A4BF**: set start of variables low byte
- **$A4C1**: save destination pointer low byte
- **$A4C3**: get start of variables high byte
- **$A4C5**: -1 + carry
- **$A4C7**: set start of variables high byte
- **$A4C9**: subtract found line pointer high byte
- **$A4CB**: copy to block count
- **$A4CC**: set carry for subtract
- **$A4CD**: get found line pointer low byte
- **$A4CF**: subtract start of variables low byte
- **$A4D1**: copy to bytes in first block count
- **$A4D2**: branch if no underflow
- **$A4D4**: increment block count, correct for = 0 loop exit
- **$A4D5**: decrement destination high byte
- **$A4D7**: clear carry for add
- **$A4D8**: add source pointer low byte
- **$A4DA**: branch if no overflow
- **$A4DC**: else decrement source pointer high byte
- **$A4DE**: clear carry close up memory to delete old line
- **$A4DF**: get byte from source
- **$A4E1**: copy to destination
- **$A4E3**: increment index
- **$A4E4**: while <> 0 do this block
- **$A4E6**: increment source pointer high byte
- **$A4E8**: increment destination pointer high byte
- **$A4EA**: decrement block count
- **$A4EB**: loop until all done got new line in buffer and no existing same #
- **$A4ED**: reset execution to start, clear variables, flush stack and return
- **$A4F0**: rebuild BASIC line chaining
- **$A4F3**: get first byte from buffer
- **$A4F6**: if no line go do BASIC warm start else insert line into memory
- **$A4F8**: clear carry for add
- **$A4F9**: get start of variables low byte
- **$A4FB**: save as source end pointer low byte
- **$A4FD**: add index pointer to end of crunched line
- **$A4FF**: save as destination end pointer low byte
- **$A501**: get start of variables high byte
- **$A503**: save as source end pointer high byte
- **$A505**: branch if no carry to high byte
- **$A507**: else increment high byte
- **$A508**: save as destination end pointer high byte
- **$A50A**: open up space in memory most of what remains to do is copy the crunched line into the space opened up in memory, however, before the crunched line comes the next line pointer and the line number. the line number is retrieved from the temporary integer and stored in memory, this overwrites the bottom two bytes on the stack. next the line is copied and the next line pointer is filled with whatever was in two bytes above the line number in the stack. this is ok because the line pointer gets fixed in the line chain re-build.
- **$A50D**: get line number low byte
- **$A50F**: get line number high byte
- **$A511**: save line number low byte before crunched line
- **$A514**: save line number high byte before crunched line
- **$A517**: get end of arrays low byte
- **$A519**: get end of arrays high byte
- **$A51B**: set start of variables low byte
- **$A51D**: set start of variables high byte
- **$A51F**: get index to end of crunched line
- **$A521**: -1
- **$A522**: get byte from crunched line
- **$A525**: save byte to memory
- **$A527**: decrement index
- **$A528**: loop while more to do reset execution, clear variables, flush stack, rebuild BASIC chain and do warm start
- **$A52A**: reset execution to start, clear variables and flush stack
- **$A52D**: rebuild BASIC line chaining
- **$A530**: go do BASIC warm start

### Commodore-64-intern-Buch (Commodore)
- **$A49C**: Zeilenr. nach Adressformat
- **$A49F**: BASIC-Zeile in Code wandeln
- **$A4A2**: Zeiger in Eingabepuffer
- **$A4A4**: Zeilenadresse berechnen
- **$A4A7**: Vorhanden? Ja: löschen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A4A2**: SAVE INDEX TO INPUT BUFFER
- **$A4A4**: IS THIS LINE # ALREADY IN PROGRAM?
- **$A4A7**: NO
- **$A4A9**: YES, SO DELETE IT
- **$A4AB**: LOWTR POINTS AT LINE
- **$A4AD**: GET HIGH BYTE OF FORWARD PNTR
- **$A4DF**: MOVE HIGHER LINES OF PROGRAM
- **$A4E1**: DOWN OVER THE DELETED LINE.
- **$A4F3**: ANY CHARACTERS AFTER LINE #?
- **$A4F6**: NO, SO NOTHING TO INSERT.
- **$A4F9**: SET UP BLTU SUBROUTINE
- **$A4FB**: INSERT NEW LINE.
- **$A50A**: MAKE ROOM FOR THE LINE
- **$A50D**: PUT LINE NUMBER IN LINE IMAGE
- **$A521**: COPY LINE INTO PROGRAM

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*