---
title: initialise BASIC RAM locations
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
- e3a2-kopie-der-chrget-routine
- e3bf-ram-fr-basic-initialisieren
- e3e0-move-generic-chrget-and-random-seed-into-place
- jmp
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E3BF
  address_end: $E421
  symbol: initialise-basic-ram-locations
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E3BF**: opcode for JMP'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E3BF**: JMP'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E3C6**: low  B248'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E3BF**: ; opcode for JMP'
---

# $E3BF — initialise BASIC RAM locations

## Disassemblatura
```assembly
.E3BF  A9 4C    LDA #$4C   ; opcode for JMP
.E3C1  85 54    STA $54   ; save for functions vector jump
.E3C3  8D 10 03 STA $0310   ; save for USR() vector jump set USR() vector to illegal quantity error
.E3C6  A9 48    LDA #$48   ; set USR() vector low byte
.E3C8  A0 B2    LDY #$B2   ; set USR() vector high byte
.E3CA  8D 11 03 STA $0311   ; save USR() vector low byte
.E3CD  8C 12 03 STY $0312   ; save USR() vector high byte
.E3D0  A9 91    LDA #$91   ; set fixed to float vector low byte
.E3D2  A0 B3    LDY #$B3   ; set fixed to float vector high byte
.E3D4  85 05    STA $05   ; save fixed to float vector low byte
.E3D6  84 06    STY $06   ; save fixed to float vector high byte
.E3D8  A9 AA    LDA #$AA   ; set float to fixed vector low byte
.E3DA  A0 B1    LDY #$B1   ; set float to fixed vector high byte
.E3DC  85 03    STA $03   ; save float to fixed vector low byte
.E3DE  84 04    STY $04   ; save float to fixed vector high byte copy the character get subroutine from $E3A2 to $0074
.E3E0  A2 1C    LDX #$1C   ; set the byte count
.E3E2  BD A2 E3 LDA $E3A2,X   ; get a byte from the table
.E3E5  95 73    STA $73,X   ; save the byte in page zero
.E3E7  CA       DEX   ; decrement the count
.E3E8  10 F8    BPL $E3E2   ; loop if not all done clear descriptors, strings, program area and memory pointers
.E3EA  A9 03    LDA #$03   ; set the step size, collecting descriptors
.E3EC  85 53    STA $53   ; save the garbage collection step size
.E3EE  A9 00    LDA #$00   ; clear A
.E3F0  85 68    STA $68   ; clear FAC1 overflow byte
.E3F2  85 13    STA $13   ; clear the current I/O channel, flag default
.E3F4  85 18    STA $18   ; clear the current descriptor stack item pointer high byte
.E3F6  A2 01    LDX #$01   ; set X
.E3F8  8E FD 01 STX $01FD   ; set the chain link pointer low byte
.E3FB  8E FC 01 STX $01FC   ; set the chain link pointer high byte
.E3FE  A2 19    LDX #$19   ; initial the value for descriptor stack
.E400  86 16    STX $16   ; set descriptor stack pointer
.E402  38       SEC   ; set Cb = 1 to read the bottom of memory
.E403  20 9C FF JSR $FF9C   ; read/set the bottom of memory
.E406  86 2B    STX $2B   ; save the start of memory low byte
.E408  84 2C    STY $2C   ; save the start of memory high byte
.E40A  38       SEC   ; set Cb = 1 to read the top of memory
.E40B  20 99 FF JSR $FF99   ; read/set the top of memory
.E40E  86 37    STX $37   ; save the end of memory low byte
.E410  84 38    STY $38   ; save the end of memory high byte
.E412  86 33    STX $33   ; set the bottom of string space low byte
.E414  84 34    STY $34   ; set the bottom of string space high byte
.E416  A0 00    LDY #$00   ; clear the index
.E418  98       TYA   ; clear the A
.E419  91 2B    STA ($2B),Y   ; clear the the first byte of memory
.E41B  E6 2B    INC $2B   ; increment the start of memory low byte
.E41D  D0 02    BNE $E421   ; if no rollover skip the high byte increment
.E41F  E6 2C    INC $2C   ; increment start of memory high byte
.E421  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E3BF**: opcode for JMP
- **$E3C1**: save for functions vector jump
- **$E3C3**: save for USR() vector jump set USR() vector to illegal quantity error
- **$E3C6**: set USR() vector low byte
- **$E3C8**: set USR() vector high byte
- **$E3CA**: save USR() vector low byte
- **$E3CD**: save USR() vector high byte
- **$E3D0**: set fixed to float vector low byte
- **$E3D2**: set fixed to float vector high byte
- **$E3D4**: save fixed to float vector low byte
- **$E3D6**: save fixed to float vector high byte
- **$E3D8**: set float to fixed vector low byte
- **$E3DA**: set float to fixed vector high byte
- **$E3DC**: save float to fixed vector low byte
- **$E3DE**: save float to fixed vector high byte copy the character get subroutine from $E3A2 to $0074
- **$E3E0**: set the byte count
- **$E3E2**: get a byte from the table
- **$E3E5**: save the byte in page zero
- **$E3E7**: decrement the count
- **$E3E8**: loop if not all done clear descriptors, strings, program area and memory pointers
- **$E3EA**: set the step size, collecting descriptors
- **$E3EC**: save the garbage collection step size
- **$E3EE**: clear A
- **$E3F0**: clear FAC1 overflow byte
- **$E3F2**: clear the current I/O channel, flag default
- **$E3F4**: clear the current descriptor stack item pointer high byte
- **$E3F6**: set X
- **$E3F8**: set the chain link pointer low byte
- **$E3FB**: set the chain link pointer high byte
- **$E3FE**: initial the value for descriptor stack
- **$E400**: set descriptor stack pointer
- **$E402**: set Cb = 1 to read the bottom of memory
- **$E403**: read/set the bottom of memory
- **$E406**: save the start of memory low byte
- **$E408**: save the start of memory high byte
- **$E40A**: set Cb = 1 to read the top of memory
- **$E40B**: read/set the top of memory
- **$E40E**: save the end of memory low byte
- **$E410**: save the end of memory high byte
- **$E412**: set the bottom of string space low byte
- **$E414**: set the bottom of string space high byte
- **$E416**: clear the index
- **$E418**: clear the A
- **$E419**: clear the the first byte of memory
- **$E41B**: increment the start of memory low byte
- **$E41D**: if no rollover skip the high byte increment
- **$E41F**: increment start of memory high byte

### Commodore-64-intern-Buch (Commodore)
- **$E3BF**: JMP
- **$E3C1**: für Funktionen
- **$E3C3**: für USR-Funktion
- **$E3C6**: Zeiger auf
- **$E3C8**: 'ILLEGAL QUANTITY'
- **$E3CA**: als USR-Vektor
- **$E3CD**: speichern
- **$E3D0**: Adresse
- **$E3D2**: $B391
- **$E3D4**: als Vektor für
- **$E3D6**: Fest-/Fließkomma-Wandlung
- **$E3D8**: Adresse
- **$E3DA**: $B1AA
- **$E3DC**: als Vektor für
- **$E3DE**: Fließ-/Festkomma-Wandlung
- **$E3E0**: Zähler setzen
- **$E3E2**: CHRGET-Routine
- **$E3E5**: ins
- **$E3E7**: RAM kopieren
- **$E3E8**: schon alles?
- **$E3EA**: Schrittweise
- **$E3EC**: für Garbage Collection
- **$E3EE**: FAC-Rundungsbyte
- **$E3F0**: löschen
- **$E3F2**: Eingabegerät gleich
- **$E3F4**: Tastatur
- **$E3F6**: Dummys
- **$E3F8**: für Linkadresse beim
- **$E3FB**: Zeileneinbau
- **$E3FE**: Zeiger für
- **$E400**: Stringverwaltung
- **$E402**: RAM-
- **$E403**: Start holen
- **$E406**: als BASIC-Start
- **$E408**: speichern
- **$E40A**: RAM-
- **$E40B**: Ende holen
- **$E40E**: als
- **$E410**: BASIC-
- **$E412**: Ende
- **$E414**: speichern
- **$E416**: $00
- **$E418**: an
- **$E419**: BASIC-Start
- **$E41B**: den
- **$E41D**: BASIC-
- **$E41F**: Start + 1
- **$E421**: Programmnde
- **$E422**: Zeiger auf
- **$E424**: BASIC-RAM Start
- **$E426**: prüft auf Platz im Speicher
- **$E429**: Zeiger auf
- **$E42B**: Einschaltmeldung
- **$E42D**: String ausgeben
- **$E430**: BASIC-
- **$E432**: Ende
- **$E433**: minus
- **$E435**: BASIC-Start
- **$E436**: gleich
- **$E438**: Bytes free
- **$E43A**: Anzahl ausgeben
- **$E43D**: Zeiger auf
- **$E43F**: 'BASIC BYTES FREE'
- **$E441**: String ausgeben
- **$E444**: zum NEW-Befehl

### Marko Mäkelä (Marko Mäkelä)
- **$E3C6**: low  B248
- **$E3C8**: high B248
- **$E3D0**: low  B391
- **$E3D2**: high B391
- **$E3D8**: low  B1AA
- **$E3DA**: high B1AA

### Magnus Nyman (Magnus Nyman)
- **$E3BF**: ; opcode for JMP
- **$E3C1**: ; store in JMPER
- **$E3C3**: ; USRPOK, set USR JMP instruction
- **$E3C8**: ; vector to $b248, ?ILLEGAL QUANTITY
- **$E3CD**: ; store in USRADD
- **$E3D2**: ; vector to $b391
- **$E3D6**: ; store in ADRAY2
- **$E3DA**: ; vector to $b1aa
- **$E3DE**: ; store in ADRAY1
- **$E3E0**: ; copy the CHRGET routine and RNDSED to RAM
- **$E3E2**: ; source address
- **$E3E5**: ; destination address
- **$E3E7**: ; next byte
- **$E3E8**: ; till ready
- **$E3EC**: ; store #3 in FOUR6, garbage collection
- **$E3F0**: ; init BITS, fac#1 overflow
- **$E3F2**: ; init input prompt flag
- **$E3F4**: ; init LASTPT
- **$E400**: ; TEMPPT, pointer to descriptor stack
- **$E402**: ; set carry to indicate read mode
- **$E403**: ; read MEMBOT
- **$E406**: ; set TXTTAB, bottom of RAM
- **$E40A**: ; set carry to indicate read mode
- **$E40B**: ; read MEMTOP
- **$E40E**: ; set MEMSIZ, top of RAM
- **$E412**: ; set FRETOP = MEMTOP
- **$E419**: ; store zero at start of BASIC
- **$E41B**: ; increment TXTTAB to next memory position
- **$E41D**: ; skip msb
- **$E421**: ; return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*