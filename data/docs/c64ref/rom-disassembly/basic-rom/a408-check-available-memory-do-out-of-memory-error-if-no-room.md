---
title: check available memory, do out of memory error if no room
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
- a408-schafft-platz-im-speicher
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A408
  address_end: $A434
  symbol: check-available-memory-do-out-of-memory-error-if-no-room
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A408**: compare with bottom of string space high byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A408**: für Zeileneinfügung'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A408**: HIGH BYTE'
---

# $A408 — check available memory, do out of memory error if no room

## Disassemblatura
```assembly
.A408  C4 34    CPY $34   ; compare with bottom of string space high byte
.A40A  90 28    BCC $A434   ; if less then exit (is ok)
.A40C  D0 04    BNE $A412   ; skip next test if greater (tested <) high byte was =, now do low byte
.A40E  C5 33    CMP $33   ; compare with bottom of string space low byte
.A410  90 22    BCC $A434   ; if less then exit (is ok) address is > string storage ptr (oops!)
.A412  48       PHA   ; push address low byte
.A413  A2 09    LDX #$09   ; set index to save $57 to $60 inclusive
.A415  98       TYA   ; copy address high byte (to push on stack) save misc numeric work area
.A416  48       PHA   ; push byte
.A417  B5 57    LDA $57,X   ; get byte from $57 to $60
.A419  CA       DEX   ; decrement index
.A41A  10 FA    BPL $A416   ; loop until all done
.A41C  20 26 B5 JSR $B526   ; do garbage collection routine restore misc numeric work area
.A41F  A2 F7    LDX #$F7   ; set index to restore bytes
.A421  68       PLA   ; pop byte
.A422  95 61    STA $61,X   ; save byte to $57 to $60
.A424  E8       INX   ; increment index
.A425  30 FA    BMI $A421   ; loop while -ve
.A427  68       PLA   ; pop address high byte
.A428  A8       TAY   ; copy back to Y
.A429  68       PLA   ; pop address low byte
.A42A  C4 34    CPY $34   ; compare with bottom of string space high byte
.A42C  90 06    BCC $A434   ; if less then exit (is ok)
.A42E  D0 05    BNE $A435   ; if greater do out of memory error then warm start high byte was =, now do low byte
.A430  C5 33    CMP $33   ; compare with bottom of string space low byte
.A432  B0 01    BCS $A435   ; if >= do out of memory error then warm start ok exit, carry clear
.A434  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A408**: compare with bottom of string space high byte
- **$A40A**: if less then exit (is ok)
- **$A40C**: skip next test if greater (tested <) high byte was =, now do low byte
- **$A40E**: compare with bottom of string space low byte
- **$A410**: if less then exit (is ok) address is > string storage ptr (oops!)
- **$A412**: push address low byte
- **$A413**: set index to save $57 to $60 inclusive
- **$A415**: copy address high byte (to push on stack) save misc numeric work area
- **$A416**: push byte
- **$A417**: get byte from $57 to $60
- **$A419**: decrement index
- **$A41A**: loop until all done
- **$A41C**: do garbage collection routine restore misc numeric work area
- **$A41F**: set index to restore bytes
- **$A421**: pop byte
- **$A422**: save byte to $57 to $60
- **$A424**: increment index
- **$A425**: loop while -ve
- **$A427**: pop address high byte
- **$A428**: copy back to Y
- **$A429**: pop address low byte
- **$A42A**: compare with bottom of string space high byte
- **$A42C**: if less then exit (is ok)
- **$A42E**: if greater do out of memory error then warm start high byte was =, now do low byte
- **$A430**: compare with bottom of string space low byte
- **$A432**: if >= do out of memory error then warm start ok exit, carry clear

### Commodore-64-intern-Buch (Commodore)
- **$A408**: für Zeileneinfügung
- **$A40A**: und Variablen
- **$A40C**: A/Y = Adresse, bis zu der
- **$A40E**: Platz benötigt wird.
- **$A410**: Kleiner als Stringzeiger
- **$A412**: Akku Zwischenspeichern
- **$A413**: Zähler setzen
- **$A415**: Y-Register auf
- **$A416**: Stapel retten
- **$A417**: Ab $57 Zwischenspeichern
- **$A419**: Zähler vermindern
- **$A41A**: Alle? sonst weiter
- **$A41C**: Garbage Collection
- **$A41F**: Zähler setzen, um
- **$A421**: Akku, Y-Register und andere
- **$A422**: Register zurückholen
- **$A424**: Zähler vermindern
- **$A425**: Fertig? Nein, dann weiter
- **$A427**: Y-Register von Stapel
- **$A428**: zurückholen
- **$A429**: Akku holen
- **$A42A**: Ist jetzt genügend Platz?
- **$A42C**: Ja, dann Rücksprung
- **$A42E**: kein Platz, dann Fehler-
- **$A430**: meldung 1 out of memory 1
- **$A432**: ausgeben
- **$A434**: Rücksprung
- **$A435**: Fehlernummer 'out of memory'

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A408**: HIGH BYTE
- **$A40A**: PLENTY OF ROOM
- **$A40C**: NOT ENOUGH, TRY GARBAGE COLLECTION
- **$A40E**: LOW BYTE
- **$A410**: ENOUGH ROOM
- **$A412**: SAVE (Y,A), TEMP1, AND TEMP2
- **$A41C**: MAKE AS MUCH ROOM AS POSSIBLE
- **$A41F**: RESTORE TEMP1 AND TEMP2
- **$A421**: AND (Y,A)
- **$A429**: DID WE FIND ENOUGH ROOM?
- **$A42A**: HIGH BYTE
- **$A42C**: YES, AT LEAST A PAGE
- **$A42E**: NO, MEM FULL ERR
- **$A430**: LOW BYTE
- **$A432**: NO, MEM FULL ERR
- **$A434**: YES, RETURN

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*