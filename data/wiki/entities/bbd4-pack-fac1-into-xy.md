---
id: bbd4-pack-fac1-into-xy
type: entity
title: pack FAC1 into (XY)
aliases:
- pack FAC1 into (XY)
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bbd4-pack-fac1-into-xy.md
  sha256: 9e8a6769252aa5a5b139934276b229da6980b69d4ea8d0583cafea91ec15320c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bbd4-pack-fac1-into-xy
---

# pack FAC1 into (XY)



# $BBD4 — pack FAC1 into (XY)

## Disassemblatura
```assembly
.BBD4  20 1B BC JSR $BC1B   ; round FAC1
.BBD7  86 22    STX $22   ; save pointer low byte
.BBD9  84 23    STY $23   ; save pointer high byte
.BBDB  A0 04    LDY #$04   ; set index
.BBDD  A5 65    LDA $65   ; get FAC1 mantissa 4
.BBDF  91 22    STA ($22),Y   ; store in destination
.BBE1  88       DEY   ; decrement index
.BBE2  A5 64    LDA $64   ; get FAC1 mantissa 3
.BBE4  91 22    STA ($22),Y   ; store in destination
.BBE6  88       DEY   ; decrement index
.BBE7  A5 63    LDA $63   ; get FAC1 mantissa 2
.BBE9  91 22    STA ($22),Y   ; store in destination
.BBEB  88       DEY   ; decrement index
.BBEC  A5 66    LDA $66   ; get FAC1 sign (b7)
.BBEE  09 7F    ORA #$7F   ; set bits x111 1111
.BBF0  25 62    AND $62   ; AND in FAC1 mantissa 1
.BBF2  91 22    STA ($22),Y   ; store in destination
.BBF4  88       DEY   ; decrement index
.BBF5  A5 61    LDA $61   ; get FAC1 exponent
.BBF7  91 22    STA ($22),Y   ; store in destination
.BBF9  84 70    STY $70   ; clear FAC1 rounding byte
.BBFB  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BBD4**: round FAC1
- **$BBD7**: save pointer low byte
- **$BBD9**: save pointer high byte
- **$BBDB**: set index
- **$BBDD**: get FAC1 mantissa 4
- **$BBDF**: store in destination
- **$BBE1**: decrement index
- **$BBE2**: get FAC1 mantissa 3
- **$BBE4**: store in destination
- **$BBE6**: decrement index
- **$BBE7**: get FAC1 mantissa 2
- **$BBE9**: store in destination
- **$BBEB**: decrement index
- **$BBEC**: get FAC1 sign (b7)
- **$BBEE**: set bits x111 1111
- **$BBF0**: AND in FAC1 mantissa 1
- **$BBF2**: store in destination
- **$BBF4**: decrement index
- **$BBF5**: get FAC1 exponent
- **$BBF7**: store in destination
- **$BBF9**: clear FAC1 rounding byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BBD4**: ROUND VALUE IN FAC USING EXTENSION
- **$BBD7**: USE INDEX FOR PNTR
- **$BBDB**: STORING 5 PACKED BYTES
- **$BBEC**: PACK SIGN IN TOP BIT OF MANTISSA
- **$BBF5**: EXPONENT
- **$BBF9**: ZERO THE EXTENSION

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bbd4-pack-fac1-into-xy]]
