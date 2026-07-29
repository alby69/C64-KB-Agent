---
title: IRQ vector
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
- ea31-interrupt-routine
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EA31
  address_end: $EA86
  symbol: irq-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EA31**: increment the real time clock'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EA31**: Stop-Taste, Zeit erhöhen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$EA31**: do clock'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EA31**: update realtime clock, routine UDTIM'
---

# $EA31 — IRQ vector

## Disassemblatura
```assembly
.EA31  20 EA FF JSR $FFEA   ; increment the real time clock
.EA34  A5 CC    LDA $CC   ; get the cursor enable, $00 = flash cursor
.EA36  D0 29    BNE $EA61   ; if flash not enabled skip the flash
.EA38  C6 CD    DEC $CD   ; decrement the cursor timing countdown
.EA3A  D0 25    BNE $EA61   ; if not counted out skip the flash
.EA3C  A9 14    LDA #$14   ; set the flash count
.EA3E  85 CD    STA $CD   ; save the cursor timing countdown
.EA40  A4 D3    LDY $D3   ; get the cursor column
.EA42  46 CF    LSR $CF   ; shift b0 cursor blink phase into carry
.EA44  AE 87 02 LDX $0287   ; get the colour under the cursor
.EA47  B1 D1    LDA ($D1),Y   ; get the character from current screen line
.EA49  B0 11    BCS $EA5C   ; branch if cursor phase b0 was 1
.EA4B  E6 CF    INC $CF   ; set the cursor blink phase to 1
.EA4D  85 CE    STA $CE   ; save the character under the cursor
.EA4F  20 24 EA JSR $EA24   ; calculate the pointer to colour RAM
.EA52  B1 F3    LDA ($F3),Y   ; get the colour RAM byte
.EA54  8D 87 02 STA $0287   ; save the colour under the cursor
.EA57  AE 86 02 LDX $0286   ; get the current colour code
.EA5A  A5 CE    LDA $CE   ; get the character under the cursor
.EA5C  49 80    EOR #$80   ; toggle b7 of character under cursor
.EA5E  20 1C EA JSR $EA1C   ; save the character and colour to the screen @ the cursor
.EA61  A5 01    LDA $01   ; read the 6510 I/O port
.EA63  29 10    AND #$10   ; mask 000x 0000, the cassette switch sense
.EA65  F0 0A    BEQ $EA71   ; if the cassette sense is low skip the motor stop the cassette sense was high, the switch was open, so turn off the motor and clear the interlock
.EA67  A0 00    LDY #$00   ; clear Y
.EA69  84 C0    STY $C0   ; clear the tape motor interlock
.EA6B  A5 01    LDA $01   ; read the 6510 I/O port
.EA6D  09 20    ORA #$20   ; mask xxxx xx1x, turn off the motor
.EA6F  D0 08    BNE $EA79   ; go save the port value, branch always the cassette sense was low so turn the motor on, perhaps
.EA71  A5 C0    LDA $C0   ; get the tape motor interlock
.EA73  D0 06    BNE $EA7B   ; if the cassette interlock <> 0 don't turn on motor
.EA75  A5 01    LDA $01   ; read the 6510 I/O port
.EA77  29 1F    AND #$1F   ; mask xxxx xx0x, turn on the motor
.EA79  85 01    STA $01   ; save the 6510 I/O port
.EA7B  20 87 EA JSR $EA87   ; scan the keyboard
.EA7E  AD 0D DC LDA $DC0D   ; read VIA 1 ICR, clear the timer interrupt flag
.EA81  68       PLA   ; pull Y
.EA82  A8       TAY   ; restore Y
.EA83  68       PLA   ; pull X
.EA84  AA       TAX   ; restore X
.EA85  68       PLA   ; restore A
.EA86  40       RTI
```


## Commenti

### Original Disassembly (—)
- **$EA31**: increment the real time clock
- **$EA34**: get the cursor enable, $00 = flash cursor
- **$EA36**: if flash not enabled skip the flash
- **$EA38**: decrement the cursor timing countdown
- **$EA3A**: if not counted out skip the flash
- **$EA3C**: set the flash count
- **$EA3E**: save the cursor timing countdown
- **$EA40**: get the cursor column
- **$EA42**: shift b0 cursor blink phase into carry
- **$EA44**: get the colour under the cursor
- **$EA47**: get the character from current screen line
- **$EA49**: branch if cursor phase b0 was 1
- **$EA4B**: set the cursor blink phase to 1
- **$EA4D**: save the character under the cursor
- **$EA4F**: calculate the pointer to colour RAM
- **$EA52**: get the colour RAM byte
- **$EA54**: save the colour under the cursor
- **$EA57**: get the current colour code
- **$EA5A**: get the character under the cursor
- **$EA5C**: toggle b7 of character under cursor
- **$EA5E**: save the character and colour to the screen @ the cursor
- **$EA61**: read the 6510 I/O port
- **$EA63**: mask 000x 0000, the cassette switch sense
- **$EA65**: if the cassette sense is low skip the motor stop the cassette sense was high, the switch was open, so turn off the motor and clear the interlock
- **$EA67**: clear Y
- **$EA69**: clear the tape motor interlock
- **$EA6B**: read the 6510 I/O port
- **$EA6D**: mask xxxx xx1x, turn off the motor
- **$EA6F**: go save the port value, branch always the cassette sense was low so turn the motor on, perhaps
- **$EA71**: get the tape motor interlock
- **$EA73**: if the cassette interlock <> 0 don't turn on motor
- **$EA75**: read the 6510 I/O port
- **$EA77**: mask xxxx xx0x, turn on the motor
- **$EA79**: save the 6510 I/O port
- **$EA7B**: scan the keyboard
- **$EA7E**: read VIA 1 ICR, clear the timer interrupt flag
- **$EA81**: pull Y
- **$EA82**: restore Y
- **$EA83**: pull X
- **$EA84**: restore X
- **$EA85**: restore A

### Commodore-64-intern-Buch (Commodore)
- **$EA31**: Stop-Taste, Zeit erhöhen
- **$EA34**: Blink-Flag für Cursor
- **$EA36**: nicht blinkend, dann weiter
- **$EA38**: Blinkzähler erniedrigen
- **$EA3A**: nicht Null, dann weiter
- **$EA3C**: Blinkzähler wieder auf 20 setzen
- **$EA3E**: und speichern
- **$EA40**: Cursorspalte
- **$EA42**: Blinkschalter eins dann C=1
- **$EA44**: Farbe unter Cursor
- **$EA47**: Zeichen-Kode holen
- **$EA49**: Blinkschalter war ein, dann weiter
- **$EA4B**: Blinkschalter ein
- **$EA4D**: Zeichen unter Cursor merken
- **$EA4F**: Zeiger in Farb-RAM berechnen
- **$EA52**: Farb-Code holen
- **$EA54**: und merken
- **$EA57**: Farb-Code unter Cursor
- **$EA5A**: Zeichen unter Cursor holen
- **$EA5C**: RVS-Bit umdrehen
- **$EA5E**: Zeichen und Farbe setzen
- **$EA61**: Prozessorport laden
- **$EA63**: prüft Rekorder-Taste
- **$EA65**: gedrückt, dann verzweige
- **$EA67**: Wert für keine Taste gedrückt
- **$EA69**: Rekorder-Flag setzen
- **$EA6B**: Prozessorport laden
- **$EA6D**: Rekoder-Motor ausschalten
- **$EA6F**: unbedingter Sprung
- **$EA71**: lade Rekorder-Flag
- **$EA73**: verzweige, wenn Motor läuft
- **$EA75**: Prozessorport laden
- **$EA77**: Rekorder-Motor einschalten
- **$EA79**: und wieder speichern
- **$EA7B**: Tastaturabfrage
- **$EA7E**: IRQ-Flag löschen
- **$EA81**: Accu aus dem Stapel holen
- **$EA82**: und in Y-Register schieben
- **$EA83**: Accu aus dem Stapel holen
- **$EA84**: und in X-Register schieben
- **$EA85**: und Rückkehr vom Interrupt

### Marko Mäkelä (Marko Mäkelä)
- **$EA31**: do clock
- **$EA34**: flash cursor
- **$EA5E**: display cursor
- **$EA61**: check cassette sense
- **$EA7B**: scan keyboard

### Magnus Nyman (Magnus Nyman)
- **$EA31**: update realtime clock, routine UDTIM
- **$EA34**: read BLNSW to see if cursor is enabled
- **$EA36**: nope
- **$EA38**: read BLNCT
- **$EA3A**: if zero, toggle cursor - else jump
- **$EA3C**: blink speed
- **$EA3E**: restore BLCNT
- **$EA40**: get PNTR, cursor column
- **$EA42**: BLNON, flag last cursor blink on/off
- **$EA44**: get background colour under cursor, GDCOL
- **$EA47**: get screen character
- **$EA49**: ?
- **$EA4B**: increment BLNON
- **$EA4D**: temporary store character under cursor
- **$EA4F**: synchronise colour pointer
- **$EA52**: get colour under character
- **$EA54**: store in GDCOL
- **$EA57**: get current COLOR
- **$EA5A**: retrieve character under cursor
- **$EA5C**: toggle cursor by inverting character
- **$EA5E**: print to screen by using part of 'print to screen'
- **$EA7B**: scan keyboard
- **$EA7E**: clear CIA#1 I.C.R to enable next IRQ
- **$EA81**: restore (Y), (X), (A)
- **$EA86**: back to normal

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*