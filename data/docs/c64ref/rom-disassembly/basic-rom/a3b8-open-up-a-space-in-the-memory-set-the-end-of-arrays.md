---
title: open up a space in the memory, set the end of arrays
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
- a3b8-block-verschiebe-routine
- a3bf-move-bytes-routine
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A3B8
  address_end: $A3FA
  symbol: open-up-a-space-in-the-memory-set-the-end-of-arrays
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A3B8**: check available memory, do out of memory error if no
      room'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A3B8**: prüft auf Platz im Speicher'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A3B8**: BE SURE (Y,A) < FRETOP'
---

# $A3B8 — open up a space in the memory, set the end of arrays

## Disassemblatura
```assembly
.A3B8  20 08 A4 JSR $A408   ; check available memory, do out of memory error if no room
.A3BB  85 31    STA $31   ; set end of arrays low byte
.A3BD  84 32    STY $32   ; set end of arrays high byte open up a space in the memory, don't set the array end
.A3BF  38       SEC   ; set carry for subtract
.A3C0  A5 5A    LDA $5A   ; get block end low byte
.A3C2  E5 5F    SBC $5F   ; subtract block start low byte
.A3C4  85 22    STA $22   ; save MOD(block length/$100) byte
.A3C6  A8       TAY   ; copy MOD(block length/$100) byte to Y
.A3C7  A5 5B    LDA $5B   ; get block end high byte
.A3C9  E5 60    SBC $60   ; subtract block start high byte
.A3CB  AA       TAX   ; copy block length high byte to X
.A3CC  E8       INX   ; +1 to allow for count=0 exit
.A3CD  98       TYA   ; copy block length low byte to A
.A3CE  F0 23    BEQ $A3F3   ; branch if length low byte=0 block is (X-1)*256+Y bytes, do the Y bytes first
.A3D0  A5 5A    LDA $5A   ; get block end low byte
.A3D2  38       SEC   ; set carry for subtract
.A3D3  E5 22    SBC $22   ; subtract MOD(block length/$100) byte
.A3D5  85 5A    STA $5A   ; save corrected old block end low byte
.A3D7  B0 03    BCS $A3DC   ; branch if no underflow
.A3D9  C6 5B    DEC $5B   ; else decrement block end high byte
.A3DB  38       SEC   ; set carry for subtract
.A3DC  A5 58    LDA $58   ; get destination end low byte
.A3DE  E5 22    SBC $22   ; subtract MOD(block length/$100) byte
.A3E0  85 58    STA $58   ; save modified new block end low byte
.A3E2  B0 08    BCS $A3EC   ; branch if no underflow
.A3E4  C6 59    DEC $59   ; else decrement block end high byte
.A3E6  90 04    BCC $A3EC   ; branch always
.A3E8  B1 5A    LDA ($5A),Y   ; get byte from source
.A3EA  91 58    STA ($58),Y   ; copy byte to destination
.A3EC  88       DEY   ; decrement index
.A3ED  D0 F9    BNE $A3E8   ; loop until Y=0 now do Y=0 indexed byte
.A3EF  B1 5A    LDA ($5A),Y   ; get byte from source
.A3F1  91 58    STA ($58),Y   ; save byte to destination
.A3F3  C6 5B    DEC $5B   ; decrement source pointer high byte
.A3F5  C6 59    DEC $59   ; decrement destination pointer high byte
.A3F7  CA       DEX   ; decrement block count
.A3F8  D0 F2    BNE $A3EC   ; loop until count = $0
.A3FA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A3B8**: check available memory, do out of memory error if no room
- **$A3BB**: set end of arrays low byte
- **$A3BD**: set end of arrays high byte open up a space in the memory, don't set the array end
- **$A3BF**: set carry for subtract
- **$A3C0**: get block end low byte
- **$A3C2**: subtract block start low byte
- **$A3C4**: save MOD(block length/$100) byte
- **$A3C6**: copy MOD(block length/$100) byte to Y
- **$A3C7**: get block end high byte
- **$A3C9**: subtract block start high byte
- **$A3CB**: copy block length high byte to X
- **$A3CC**: +1 to allow for count=0 exit
- **$A3CD**: copy block length low byte to A
- **$A3CE**: branch if length low byte=0 block is (X-1)*256+Y bytes, do the Y bytes first
- **$A3D0**: get block end low byte
- **$A3D2**: set carry for subtract
- **$A3D3**: subtract MOD(block length/$100) byte
- **$A3D5**: save corrected old block end low byte
- **$A3D7**: branch if no underflow
- **$A3D9**: else decrement block end high byte
- **$A3DB**: set carry for subtract
- **$A3DC**: get destination end low byte
- **$A3DE**: subtract MOD(block length/$100) byte
- **$A3E0**: save modified new block end low byte
- **$A3E2**: branch if no underflow
- **$A3E4**: else decrement block end high byte
- **$A3E6**: branch always
- **$A3E8**: get byte from source
- **$A3EA**: copy byte to destination
- **$A3EC**: decrement index
- **$A3ED**: loop until Y=0 now do Y=0 indexed byte
- **$A3EF**: get byte from source
- **$A3F1**: save byte to destination
- **$A3F3**: decrement source pointer high byte
- **$A3F5**: decrement destination pointer high byte
- **$A3F7**: decrement block count
- **$A3F8**: loop until count = $0

### Commodore-64-intern-Buch (Commodore)
- **$A3B8**: prüft auf Platz im Speicher
- **$A3BB**: Ende des Arraybereichs
- **$A3BD**: als Beginn für freien Platz
- **$A3BF**: Carry setzen (Subtraktion)
- **$A3C0**: Startadresse von Endad. des
- **$A3C2**: Bereichs abziehen (LOW)
- **$A3C4**: Ergebnis (=Länge) speichern
- **$A3C6**: Gleiches System für HIGH:
- **$A3C7**: Altes Blockende (HIGH) und
- **$A3C9**: davon alter Blockanfang sub
- **$A3CB**: Länge nach X bringen
- **$A3CC**: Ist ein Rest ( Länge nicht
- **$A3CD**: 256 Bytes)?
- **$A3CE**: Nein: dann nur ganze Blöcke
- **$A3D0**: Alte Endadresse (LOW) und
- **$A3D2**: davon Länge des Restab-
- **$A3D3**: schnitts subtrahieren ergibt Adresse des
- **$A3D5**: Restabschnitts
- **$A3D7**: Berechnung für HIGH umgehen
- **$A3D9**: Dasselbe System für HIGH
- **$A3DB**: Carry setzen (Subtraktion)
- **$A3DC**: Alte Endadresse (HIGH) und
- **$A3DE**: davon Länge des Rests sub-
- **$A3E0**: trahieren ergibt neue Adresse
- **$A3E2**: Unbedingter Sprung zur
- **$A3E4**: Kopierroutine für ganze
- **$A3E6**: Blöcke
- **$A3E8**: Kopierroutine für Rest-
- **$A3EA**: abschnitt
- **$A3EC**: Zähler vermindern
- **$A3ED**: Alles? wenn nicht: weiter
- **$A3EF**: Kopierroutine für ganze
- **$A3F1**: Blöcke
- **$A3F3**: Adresszähler vermindern
- **$A3F5**: Adresszähler vermindern
- **$A3F7**: Zähler vermindern
- **$A3F8**: Alles? Wenn nicht: weiter
- **$A3FA**: sonst Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A3B8**: BE SURE (Y,A) < FRETOP
- **$A3BB**: NEW TOP OF ARRAY STORAGE
- **$A3C0**: COMPUTE # OF BYTES TO BE MOVED
- **$A3C2**: (FROM LOWTR THRU HIGHTR-1)
- **$A3C4**: PARTIAL PAGE AMOUNT
- **$A3CB**: # OF WHOLE PAGES IN X-REG
- **$A3CD**: # BYTES IN PARTIAL PAGE
- **$A3CE**: NO PARTIAL PAGE
- **$A3D0**: BACK UP HIGHTR # BYTES IN PARTIAL PAGE
- **$A3DC**: BACK UP HIGHDS # BYTES IN PARTIAL PAGE
- **$A3E6**: ...ALWAYS
- **$A3E8**: MOVE THE BYTES
- **$A3ED**: LOOP TO END OF THIS 256 BYTES
- **$A3EF**: MOVE ONE MORE BYTE
- **$A3F3**: DOWN TO NEXT BLOCK OF 256
- **$A3F7**: ANOTHER BLOCK OF 256 TO MOVE?
- **$A3F8**: YES
- **$A3FA**: NO, FINISHED

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*