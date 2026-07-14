---
title: Commodore 64 machine instruction execution times
source_url: https://sta.c64.org/cbm64mctime.html
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
last_modified: Mon, 27 Nov 2023 23:00:00 GMT
---

# Commodore 64 machine instruction execution times

| Instruction | - | # | ZP | ZP,X | ZP,Y | (ZP,X) | (ZP),Y | ABS | ABS,X | ABS,Y | (ABS) | REL | A | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADC | 2 | 3 | 4 | 6 | 5+ | 4 | 4+ | 4+ | |||||
| AND | 2 | 3 | 4 | 6 | 5+ | 4 | 4+ | 4+ | |||||
| ASL | 5 | 6 | 6 | 7 | 2 | ||||||||
| BCC | 2+* | ||||||||||||
| BCS | 2+* | ||||||||||||
| BEQ | 2+* | ||||||||||||
| BIT | 3 | 4 | |||||||||||
| BMI | 2+* | ||||||||||||
| BNE | 2+* | ||||||||||||
| BPL | 2+* | ||||||||||||
| BRK | 7 | ||||||||||||
| BVC | 2+* | ||||||||||||
| BVS | 2+* | ||||||||||||
| CLC | 2 | ||||||||||||
| CLD | 2 | ||||||||||||
| CLI | 2 | ||||||||||||
| CLV | 2 | ||||||||||||
| CMP | 2 | 3 | 4 | 6 | 5+ | 4 | 4+ | 4+ | |||||
| CPX | 2 | 3 | 4 | ||||||||||
| CPY | 2 | 3 | 4 | ||||||||||
| DEC | 5 | 6 | 6 | 7 | |||||||||
| DEX | 2 | ||||||||||||
| DEY | 2 | ||||||||||||
| EOR | 2 | 3 | 4 | 6 | 5+ | 4 | 4+ | 4+ | |||||
| INC | 5 | 6 | 6 | 7 | |||||||||
| INX | 2 | ||||||||||||
| INY | 2 | ||||||||||||
| JMP | 3 | 5 | |||||||||||
| JSR | 6 | ||||||||||||
| LDA | 2 | 3 | 4 | 6 | 5+ | 4 | 4+ | 4+ | |||||
| LDX | 2 | 3 | 4 | 4 | 4+ | ||||||||
| LDY | 2 | 3 | 4 | 4 | 4+ | ||||||||
| LSR | 5 | 6 | 6 | 7 | 2 | ||||||||
| NOP | 2 | ||||||||||||
| ORA | 2 | 3 | 4 | 6 | 5+ | 4 | 4+ | 4+ | |||||
| PHA | 3 | ||||||||||||
| PHP | 3 | ||||||||||||
| PLA | 4 | ||||||||||||
| PLP | 4 | ||||||||||||
| ROL | 5 | 6 | 6 | 7 | 2 | ||||||||
| ROR | 5 | 6 | 6 | 7 | 2 | ||||||||
| RTI | 6 | ||||||||||||
| RTS | 6 | ||||||||||||
| SBC | 2 | 3 | 4 | 6 | 5+ | 4 | 4+ | 4+ | |||||
| SEC | 2 | ||||||||||||
| SED | 2 | ||||||||||||
| SEI | 2 | ||||||||||||
| STA | 3 | 4 | 6 | 6 | 4 | 5 | 5 | ||||||
| STX | 3 | 4 | 4 | ||||||||||
| STY | 3 | 4 | 4 | ||||||||||
| TAX | 2 | ||||||||||||
| TAY | 2 | ||||||||||||
| TSX | 2 | ||||||||||||
| TXA | 2 | ||||||||||||
| TXS | 2 | ||||||||||||
| TYA | 2 | 

Notes:

- The "+" mark means an additional cycle upon crossing a page boundary. 
- The "*" mark means an additional cycle if the branch is actually taken.

---
*Fonte originale: [https://sta.c64.org/cbm64mctime.html](https://sta.c64.org/cbm64mctime.html)*
