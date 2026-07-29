---
title: make space in string memory for string A long
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b4f4-lnge-in-a
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B4F4
  address_end: $B524
  symbol: make-space-in-string-memory-for-string-a-long
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B4F4**: clear garbage collected flag (b7) make space for string
      A long'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B4F4**: Flag für Garbage Collection zurücksetzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B4F4 — make space in string memory for string A long

## Disassemblatura
```assembly
.B4F4  46 0F    LSR $0F   ; clear garbage collected flag (b7) make space for string A long
.B4F6  48       PHA   ; save string length
.B4F7  49 FF    EOR #$FF   ; complement it
.B4F9  38       SEC   ; set carry for subtract, two's complement add
.B4FA  65 33    ADC $33   ; add bottom of string space low byte, subtract length
.B4FC  A4 34    LDY $34   ; get bottom of string space high byte
.B4FE  B0 01    BCS $B501   ; skip decrement if no underflow
.B500  88       DEY   ; decrement bottom of string space high byte
.B501  C4 32    CPY $32   ; compare with end of arrays high byte
.B503  90 11    BCC $B516   ; do out of memory error if less
.B505  D0 04    BNE $B50B   ; if not = skip next test
.B507  C5 31    CMP $31   ; compare with end of arrays low byte
.B509  90 0B    BCC $B516   ; do out of memory error if less
.B50B  85 33    STA $33   ; save bottom of string space low byte
.B50D  84 34    STY $34   ; save bottom of string space high byte
.B50F  85 35    STA $35   ; save string utility ptr low byte
.B511  84 36    STY $36   ; save string utility ptr high byte
.B513  AA       TAX   ; copy low byte to X
.B514  68       PLA   ; get string length back
.B515  60       RTS
.B516  A2 10    LDX #$10   ; error code $10, out of memory error
.B518  A5 0F    LDA $0F   ; get garbage collected flag
.B51A  30 B6    BMI $B4D2   ; if set then do error code X
.B51C  20 26 B5 JSR $B526   ; else go do garbage collection
.B51F  A9 80    LDA #$80   ; flag for garbage collected
.B521  85 0F    STA $0F   ; set garbage collected flag
.B523  68       PLA   ; pull length
.B524  D0 D0    BNE $B4F6   ; go try again (loop always, length should never be = $00)
```


## Commenti

### Original Disassembly (—)
- **$B4F4**: clear garbage collected flag (b7) make space for string A long
- **$B4F6**: save string length
- **$B4F7**: complement it
- **$B4F9**: set carry for subtract, two's complement add
- **$B4FA**: add bottom of string space low byte, subtract length
- **$B4FC**: get bottom of string space high byte
- **$B4FE**: skip decrement if no underflow
- **$B500**: decrement bottom of string space high byte
- **$B501**: compare with end of arrays high byte
- **$B503**: do out of memory error if less
- **$B505**: if not = skip next test
- **$B507**: compare with end of arrays low byte
- **$B509**: do out of memory error if less
- **$B50B**: save bottom of string space low byte
- **$B50D**: save bottom of string space high byte
- **$B50F**: save string utility ptr low byte
- **$B511**: save string utility ptr high byte
- **$B513**: copy low byte to X
- **$B514**: get string length back
- **$B516**: error code $10, out of memory error
- **$B518**: get garbage collected flag
- **$B51A**: if set then do error code X
- **$B51C**: else go do garbage collection
- **$B51F**: flag for garbage collected
- **$B521**: set garbage collected flag
- **$B523**: pull length
- **$B524**: go try again (loop always, length should never be = $00)

### Commodore-64-intern-Buch (Commodore)
- **$B4F4**: Flag für Garbage Collection zurücksetzen
- **$B4F6**: Stringlänge
- **$B4F7**: Alle Bits umdrehen
- **$B4F9**: mit HIGH-Byte des
- **$B4FA**: Stringanfangs-Zeigers addieren
- **$B4FC**: LOW-Byte ins Y-Reg.
- **$B4FE**: Carry gesetzt ? dann weiter
- **$B500**: ansonsten LOW-Byte erniedrigen
- **$B501**: Zu wenig Platz, dann
- **$B503**: Garbage Collection durchführen
- **$B505**: alles ok ?
- **$B507**: Ende der Arrays, dann
- **$B509**: Garbage Collect durchführen
- **$B50B**: ansonsten
- **$B50D**: alle
- **$B50F**: Zeiger
- **$B511**: neu
- **$B513**: setzen
- **$B514**: Stringlänge zurückholen
- **$B515**: Rücksprung
- **$B516**: Nummer für 'OUT OF MEMORY'
- **$B518**: Flag für Garbage Collection
- **$B51A**: durchgeführt? 'OUT OF MEMORY'
- **$B51C**: Garbage Collection
- **$B51F**: Flag setzen
- **$B521**: und speichern
- **$B523**: Stringlänge
- **$B524**: String nochmals einbauen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*