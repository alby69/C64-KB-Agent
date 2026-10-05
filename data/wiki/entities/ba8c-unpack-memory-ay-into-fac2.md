---
id: ba8c-unpack-memory-ay-into-fac2
type: entity
title: unpack memory (AY) into FAC2
aliases:
- unpack memory (AY) into FAC2
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ba8c-unpack-memory-ay-into-fac2.md
  sha256: 59013883b2e128d5cf8d826a45c83ae6117760ed007f5c21e3456a518e4a8cc7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ba8c-unpack-memory-ay-into-fac2
---

# unpack memory (AY) into FAC2



# $BA8C — unpack memory (AY) into FAC2

## Disassemblatura
```assembly
.BA8C  85 22    STA $22   ; save pointer low byte
.BA8E  84 23    STY $23   ; save pointer high byte
.BA90  A0 04    LDY #$04   ; 5 bytes to get (0-4)
.BA92  B1 22    LDA ($22),Y   ; get mantissa 4
.BA94  85 6D    STA $6D   ; save FAC2 mantissa 4
.BA96  88       DEY   ; decrement index
.BA97  B1 22    LDA ($22),Y   ; get mantissa 3
.BA99  85 6C    STA $6C   ; save FAC2 mantissa 3
.BA9B  88       DEY   ; decrement index
.BA9C  B1 22    LDA ($22),Y   ; get mantissa 2
.BA9E  85 6B    STA $6B   ; save FAC2 mantissa 2
.BAA0  88       DEY   ; decrement index
.BAA1  B1 22    LDA ($22),Y   ; get mantissa 1 + sign
.BAA3  85 6E    STA $6E   ; save FAC2 sign (b7)
.BAA5  45 66    EOR $66   ; EOR with FAC1 sign (b7)
.BAA7  85 6F    STA $6F   ; save sign compare (FAC1 EOR FAC2)
.BAA9  A5 6E    LDA $6E   ; recover FAC2 sign (b7)
.BAAB  09 80    ORA #$80   ; set 1xxx xxx (set normal bit)
.BAAD  85 6A    STA $6A   ; save FAC2 mantissa 1
.BAAF  88       DEY   ; decrement index
.BAB0  B1 22    LDA ($22),Y   ; get exponent byte
.BAB2  85 69    STA $69   ; save FAC2 exponent
.BAB4  A5 61    LDA $61   ; get FAC1 exponent
.BAB6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BA8C**: save pointer low byte
- **$BA8E**: save pointer high byte
- **$BA90**: 5 bytes to get (0-4)
- **$BA92**: get mantissa 4
- **$BA94**: save FAC2 mantissa 4
- **$BA96**: decrement index
- **$BA97**: get mantissa 3
- **$BA99**: save FAC2 mantissa 3
- **$BA9B**: decrement index
- **$BA9C**: get mantissa 2
- **$BA9E**: save FAC2 mantissa 2
- **$BAA0**: decrement index
- **$BAA1**: get mantissa 1 + sign
- **$BAA3**: save FAC2 sign (b7)
- **$BAA5**: EOR with FAC1 sign (b7)
- **$BAA7**: save sign compare (FAC1 EOR FAC2)
- **$BAA9**: recover FAC2 sign (b7)
- **$BAAB**: set 1xxx xxx (set normal bit)
- **$BAAD**: save FAC2 mantissa 1
- **$BAAF**: decrement index
- **$BAB0**: get exponent byte
- **$BAB2**: save FAC2 exponent
- **$BAB4**: get FAC1 exponent

### Commodore-64-intern-Buch (Commodore)
- **$BA8C**: Die
- **$BA8E**: Konstante,
- **$BA90**: auf
- **$BA92**: die
- **$BA94**: das
- **$BA96**: Akku
- **$BA97**: und
- **$BA99**: das
- **$BA9B**: Y-Reg
- **$BA9C**: zeigt, nach ARG.
- **$BA9E**: Die
- **$BAA0**: gesamten
- **$BAA1**: Vor-
- **$BAA3**: zei -
- **$BAA5**: chen
- **$BAA7**: von
- **$BAA9**: FAC
- **$BAAB**: und
- **$BAAD**: ARG
- **$BAAF**: ver-
- **$BAB0**: knüp-
- **$BAB2**: fen
- **$BAB4**: FAC-Exponent
- **$BAB6**: Rücksprung
- **$BAB7**: wenn Exponent von ARG=0,
- **$BAB9**: dann zu $BADA
- **$BABB**: FAC- und ARG-
- **$BABC**: Exponent
- **$BABE**: addieren
- **$BAC0**: wenn Überlauf, dann 'OVERFLOW ERROR'
- **$BAC2**: Carry
- **$BAC3**: löschen
- **$BAC4**: Wenn Unterlauf, dann zu $BADA
- **$BAC6**: ergibt
- **$BAC8**: FAC-
- **$BACA**: Exponent
- **$BACC**: FAC = 0
- **$BACF**: FAC- und ARG-Vorzeichen verknüpfen
- **$BAD1**: und speichern
- **$BAD3**: Rücksprung
- **$BAD4**: wenn positives
- **$BAD6**: Vorzeichen, dann
- **$BAD8**: 'OVERFLOW ERROR'
- **$BADA**: Einsprungadresse
- **$BADB**: vom Stack holen
- **$BADC**: FAC = 0
- **$BADF**: 'OVERFLOW ERROR'

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BA8C**: USE INDEX FOR PNTR
- **$BA90**: FIVE BYTES TO MOVE
- **$BAA5**: SET COMBINED SIGN FOR MULT/DIV
- **$BAA9**: TURN ON NORMALIZED INVISIBLE BIT
- **$BAAB**: TO COMPLETE MANTISSA
- **$BAB2**: EXPONENT
- **$BAB4**: SET STATUS BITS ON FAC EXPONENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ba8c-unpack-memory-ay-into-fac2]]
