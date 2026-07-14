---
title: Commodore 64 machine instructions (sorted by instruction)
source_url: https://sta.c64.org/cbm64mcinst2.html
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
last_modified: Fri, 02 Sep 2022 22:00:00 GMT
---

# Commodore 64 machine instructions (sorted by instruction)

## Commodore 64 machine instructions (sorted by instruction)

| Instruction | - | # | ZP | ZP,X | ZP,Y | (ZP,X) | (ZP),Y | ABS | ABS,X | ABS,Y | (ABS) | REL | A | 
|---|
| ADC |  | $69 | $65 | $75 |  | $61 | $71 | $6D | $7D | $79 |  |  |  | 
| AND |  | $29 | $25 | $35 |  | $21 | $31 | $2D | $3D | $29 |  |  |  | 
| ASL |  |  | $06 | $16 |  |  |  | $0E | $1E |  |  |  | $0A | 
| BCC |  |  |  |  |  |  |  |  |  |  |  | $90 |  | 
| BCS |  |  |  |  |  |  |  |  |  |  |  | $B0 |  | 
| BEQ |  |  |  |  |  |  |  |  |  |  |  | $F0 |  | 
| BIT |  |  | $24 |  |  |  |  | $2C |  |  |  |  |  | 
| BMI |  |  |  |  |  |  |  |  |  |  |  | $30 |  | 
| BNE |  |  |  |  |  |  |  |  |  |  |  | $D0 |  | 
| BPL |  |  |  |  |  |  |  |  |  |  |  | $10 |  | 
| BRK | $00 |  |  |  |  |  |  |  |  |  |  |  |  | 
| BVC |  |  |  |  |  |  |  |  |  |  |  | $50 |  | 
| BVS |  |  |  |  |  |  |  |  |  |  |  | $70 |  | 
| CLC | $18 |  |  |  |  |  |  |  |  |  |  |  |  | 
| CLD | $D8 |  |  |  |  |  |  |  |  |  |  |  |  | 
| CLI | $58 |  |  |  |  |  |  |  |  |  |  |  |  | 
| CLV | $B8 |  |  |  |  |  |  |  |  |  |  |  |  | 
| CMP |  | $C9 | $C5 | $D5 |  | $C1 | $D1 | $CD | $DD | $D9 |  |  |  | 
| CPX |  | $E0 | $E4 |  |  |  |  | $EC |  |  |  |  |  | 
| CPY |  | $C0 | $C4 |  |  |  |  | $CC |  |  |  |  |  | 
| DEC |  |  | $C6 | $D6 |  |  |  | $CE | $DE |  |  |  |  | 
| DEX | $CA |  |  |  |  |  |  |  |  |  |  |  |  | 
| DEY | $88 |  |  |  |  |  |  |  |  |  |  |  |  | 
| EOR |  | $49 | $45 | $55 |  | $41 | $51 | $4D | $5D | $59 |  |  |  | 
| INC |  |  | $E6 | $F6 |  |  |  | $EE | $FE |  |  |  |  | 
| INX | $E8 |  |  |  |  |  |  |  |  |  |  |  |  | 
| INY | $C8 |  |  |  |  |  |  |  |  |  |  |  |  | 
| JMP |  |  |  |  |  |  |  | $4C |  |  | $6C |  |  | 
| JSR |  |  |  |  |  |  |  | $20 |  |  |  |  |  | 
| LDA |  | $A9 | $A5 | $B5 |  | $A1 | $B1 | $AD | $BD | $B9 |  |  |  | 
| LDX |  | $A2 | $A6 |  | $B6 |  |  | $AE |  | $BE |  |  |  | 
| LDY |  | $A0 | $A4 | $B4 |  |  |  | $AC | $BC |  |  |  |  | 
| LSR |  |  | $46 | $56 |  |  |  | $4E | $5E |  |  |  | $4A | 
| NOP | $EA |  |  |  |  |  |  |  |  |  |  |  |  | 
| ORA |  | $09 | $05 | $15 |  | $01 | $11 | $0D | $1D | $19 |  |  |  | 
| PHA | $48 |  |  |  |  |  |  |  |  |  |  |  |  | 
| PHP | $08 |  |  |  |  |  |  |  |  |  |  |  |  | 
| PLA | $68 |  |  |  |  |  |  |  |  |  |  |  |  | 
| PLP | $28 |  |  |  |  |  |  |  |  |  |  |  |  | 
| ROL |  |  | $26 | $36 |  |  |  | $2E | $3E |  |  |  | $2A | 
| ROR |  |  | $66 | $76 |  |  |  | $6E | $7E |  |  |  | $6A | 
| RTI | $40 |  |  |  |  |  |  |  |  |  |  |  |  | 
| RTS | $60 |  |  |  |  |  |  |  |  |  |  |  |  | 
| SBC |  | $E9 | $E5 | $F5 |  | $E1 | $F1 | $ED | $FD | $E9 |  |  |  | 
| SEC | $38 |  |  |  |  |  |  |  |  |  |  |  |  | 
| SED | $F8 |  |  |  |  |  |  |  |  |  |  |  |  | 
| SEI | $78 |  |  |  |  |  |  |  |  |  |  |  |  | 
| STA |  |  | $85 | $95 |  | $81 | $91 | $8D | $9D | $99 |  |  |  | 
| STX |  |  | $86 |  | $96 |  |  | $8E |  |  |  |  |  | 
| STY |  |  | $84 | $94 |  |  |  | $8C |  |  |  |  |  | 
| TAX | $AA |  |  |  |  |  |  |  |  |  |  |  |  | 
| TAY | $A8 |  |  |  |  |  |  |  |  |  |  |  |  | 
| TSX | $BA |  |  |  |  |  |  |  |  |  |  |  |  | 
| TXA | $8A |  |  |  |  |  |  |  |  |  |  |  |  | 
| TXS | $9A |  |  |  |  |  |  |  |  |  |  |  |  | 
| TYA | $98 |  |  |  |  |  |  |  |  |  |  |  |  |

---
*Fonte originale: [https://sta.c64.org/cbm64mcinst2.html](https://sta.c64.org/cbm64mcinst2.html)*
