---
title: Commodore 64 machine instruction flag usage
source_url: https://sta.c64.org/cbm64mcflag.html
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 machine instruction flag usage

| Instruction | N | V | B | D | I | Z | C | 
|---|---|---|---|---|---|---|---|
| ADC | X | X | X | X | |||
| AND | X | X | |||||
| ASL | X | X | X | ||||
| BCC | |||||||
| BCS | |||||||
| BEQ | |||||||
| BIT | B7 | B6 | X | ||||
| BMI | |||||||
| BNE | |||||||
| BPL | |||||||
| BRK | 1 | ||||||
| BVC | |||||||
| BVS | |||||||
| CLC | 0 | ||||||
| CLD | 0 | ||||||
| CLI | 0 | ||||||
| CLV | 0 | ||||||
| CMP | X | X | X | ||||
| CPX | X | X | X | ||||
| CPY | X | X | X | ||||
| DEC | X | X | |||||
| DEX | X | X | |||||
| DEY | X | X | |||||
| EOR | X | X | |||||
| INC | X | X | |||||
| INX | X | X | |||||
| INY | X | X | |||||
| JMP | |||||||
| JSR | |||||||
| LDA | X | X | |||||
| LDX | X | X | |||||
| LDY | X | X | |||||
| LSR | 0 | X | X | ||||
| NOP | |||||||
| ORA | X | X | |||||
| PHA | |||||||
| PHP | |||||||
| PLA | X | X | |||||
| PLP | X | X | X | X | X | X | X | 
| ROL | X | X | X | ||||
| ROR | X | X | X | ||||
| RTI | X | X | X | X | X | X | X | 
| RTS | |||||||
| SBC | X | X | X | X | |||
| SEC | 1 | ||||||
| SED | 1 | ||||||
| SEI | 1 | ||||||
| STA | |||||||
| STX | |||||||
| STY | |||||||
| TAX | X | X | |||||
| TAY | X | X | |||||
| TSX | X | X | |||||
| TXA | X | X | |||||
| TXS | |||||||
| TYA | X | X | 

Notes:

- The BIT instruction fetches bits #6-#7 of the operand into the N and V flags.

---
*Fonte originale: [https://sta.c64.org/cbm64mcflag.html](https://sta.c64.org/cbm64mcflag.html)*
