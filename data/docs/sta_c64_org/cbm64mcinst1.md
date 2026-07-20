---
title: Commodore 64 machine instructions (sorted by code)
source_url: https://sta.c64.org/cbm64mcinst1.html
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-20'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 machine instructions (sorted by code)

| Code (dec, hex) | Instruction | Code (dec, hex) | Instruction | Code (dec, hex) | Instruction | Code (dec, hex) | Instruction | ||||
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | $00 | BRK | 64 | $40 | RTI | 128 | $80 | 192 | $C0 | CPY # | |
| 1 | $01 | ORA (ZP,X) | 65 | $41 | EOR (ZP,X) | 129 | $81 | STA (ZP,X) | 193 | $C1 | CMP (ZP,X) | 
| 2 | $02 | 66 | $42 | 130 | $82 | 194 | $C2 | ||||
| 3 | $03 | 67 | $43 | 131 | $83 | 195 | $C3 | ||||
| 4 | $04 | 68 | $44 | 132 | $84 | STY ZP | 196 | $C4 | CPY ZP | ||
| 5 | $05 | ORA ZP | 69 | $45 | EOR ZP | 133 | $85 | STA ZP | 197 | $C5 | CMP ZP | 
| 6 | $06 | ASL ZP | 70 | $46 | LSR ZP | 134 | $86 | STX ZP | 198 | $C6 | DEC ZP | 
| 7 | $07 | 71 | $47 | 135 | $87 | 199 | $C7 | ||||
| 8 | $08 | PHP | 72 | $48 | PHA | 136 | $88 | DEY | 200 | $C8 | INY | 
| 9 | $09 | ORA # | 73 | $49 | EOR # | 137 | $89 | 201 | $C9 | CMP # | |
| 10 | $0A | ASL A | 74 | $4A | LSR A | 138 | $8A | TXA | 202 | $CA | DEX | 
| 11 | $0B | 75 | $4B | 139 | $8B | 203 | $CB | ||||
| 12 | $0C | 76 | $4C | JMP ABS | 140 | $8C | STY ABS | 204 | $CC | CPY ABS | |
| 13 | $0D | ORA ABS | 77 | $4D | EOR ABS | 141 | $8D | STA ABS | 205 | $CD | CMP ABS | 
| 14 | $0E | ASL ABS | 78 | $4E | LSR ABS | 142 | $8E | STX ABS | 206 | $CE | DEC ABS | 
| 15 | $0F | 79 | $4F | 143 | $8F | 207 | $CF | ||||
| 16 | $10 | BPL REL | 80 | $50 | BVC REL | 144 | $90 | BCC REL | 208 | $D0 | BNE REL | 
| 17 | $11 | ORA (ZP),Y | 81 | $51 | EOR (ZP),Y | 145 | $91 | STA (ZP),Y | 209 | $D1 | CMP (ZP),Y | 
| 18 | $12 | 82 | $52 | 146 | $92 | 210 | $D2 | ||||
| 19 | $13 | 83 | $53 | 147 | $93 | 211 | $D3 | ||||
| 20 | $14 | 84 | $54 | 148 | $94 | STY ZP,X | 212 | $D4 | |||
| 21 | $15 | ORA ZP,X | 85 | $55 | EOR ZP,X | 149 | $95 | STA ZP,X | 213 | $D5 | CMP ZP,X | 
| 22 | $16 | ASL ZP,X | 86 | $56 | LSR ZP,X | 150 | $96 | STX ZP,Y | 214 | $D6 | DEC ZP,X | 
| 23 | $17 | 87 | $57 | 151 | $97 | 215 | $D7 | ||||
| 24 | $18 | CLC | 88 | $58 | CLI | 152 | $98 | TYA | 216 | $D8 | CLD | 
| 25 | $19 | ORA ABS,Y | 89 | $59 | EOR ABS,Y | 153 | $99 | STA ABS,Y | 217 | $D9 | CMP ABS,Y | 
| 26 | $1A | 90 | $5A | 154 | $9A | TXS | 218 | $DA | |||
| 27 | $1B | 91 | $5B | 155 | $9B | 219 | $DB | ||||
| 28 | $1C | 92 | $5C | 156 | $9C | 220 | $DC | ||||
| 29 | $1D | ORA ABS,X | 93 | $5D | EOR ABS,X | 157 | $9D | STA ABS,X | 221 | $DD | CMP ABS,X | 
| 30 | $1E | ASL ABS,X | 94 | $5E | LSR ABS,X | 158 | $9E | 222 | $DE | DEC ABS,X | |
| 31 | $1F | 95 | $5F | 159 | $9F | 223 | $DF | ||||
| 32 | $20 | JSR ABS | 96 | $60 | RTS | 160 | $A0 | LDY # | 224 | $E0 | CPX # | 
| 33 | $21 | AND (ZP,X) | 97 | $61 | ADC (ZP,X) | 161 | $A1 | LDA (ZP,X) | 225 | $E1 | SBC (ZP,X) | 
| 34 | $22 | 98 | $62 | 162 | $A2 | LDX # | 226 | $E2 | |||
| 35 | $23 | 99 | $63 | 163 | $A3 | 227 | $E3 | ||||
| 36 | $24 | BIT ZP | 100 | $64 | 164 | $A4 | LDY ZP | 228 | $E4 | CPX ZP | |
| 37 | $25 | AND ZP | 101 | $65 | ADC ZP | 165 | $A5 | LDA ZP | 229 | $E5 | SBC ZP | 
| 38 | $26 | ROL ZP | 102 | $66 | ROR ZP | 166 | $A6 | LDX ZP | 230 | $E6 | INC ZP | 
| 39 | $27 | 103 | $67 | 167 | $A7 | 231 | $E7 | ||||
| 40 | $28 | PLP | 104 | $68 | PLA | 168 | $A8 | TAY | 232 | $E8 | INX | 
| 41 | $29 | AND # | 105 | $69 | ADC # | 169 | $A9 | LDA # | 233 | $E9 | SBC # | 
| 42 | $2A | ROL A | 106 | $6A | ROR A | 170 | $AA | TAX | 234 | $EA | NOP | 
| 43 | $2B | 107 | $6B | 171 | $AB | 235 | $EB | ||||
| 44 | $2C | BIT ABS | 108 | $6C | JMP (ABS) | 172 | $AC | LDY ABS | 236 | $EC | CPX ABS | 
| 45 | $2D | AND ABS | 109 | $6D | ADC ABS | 173 | $AD | LDA ABS | 237 | $ED | SBC ABS | 
| 46 | $2E | ROL ABS | 110 | $6E | ROR ABS | 174 | $AE | LDX ABS | 238 | $EE | INC ABS | 
| 47 | $2F | 111 | $6F | 175 | $AF | 239 | $EF | ||||
| 48 | $30 | BMI REL | 112 | $70 | BVS REL | 176 | $B0 | BCS REL | 240 | $F0 | BEQ REL | 
| 49 | $31 | AND (ZP),Y | 113 | $71 | ADC (ZP),Y | 177 | $B1 | LDA (ZP),Y | 241 | $F1 | SBC (ZP),Y | 
| 50 | $32 | 114 | $72 | 178 | $B2 | 242 | $F2 | ||||
| 51 | $33 | 115 | $73 | 179 | $B3 | 243 | $F3 | ||||
| 52 | $34 | 116 | $74 | 180 | $B4 | LDY ZP,X | 244 | $F4 | |||
| 53 | $35 | AND ZP,X | 117 | $75 | ADC ZP,X | 181 | $B5 | LDA ZP,X | 245 | $F5 | SBC ZP,X | 
| 54 | $36 | ROL ZP,X | 118 | $76 | ROR ZP,X | 182 | $B6 | LDX ZP,Y | 246 | $F6 | INC ZP,X | 
| 55 | $37 | 119 | $77 | 183 | $B7 | 247 | $F7 | ||||
| 56 | $38 | SEC | 120 | $78 | SEI | 184 | $B8 | CLV | 248 | $F8 | SED | 
| 57 | $39 | AND ABS,Y | 121 | $79 | ADC ABS,Y | 185 | $B9 | LDA ABS,Y | 249 | $F9 | SBC ABS,Y | 
| 58 | $3A | 122 | $7A | 186 | $BA | TSX | 250 | $FA | |||
| 59 | $3B | 123 | $7B | 187 | $BB | 251 | $FB | ||||
| 60 | $3C | 124 | $7C | 188 | $BC | LDY ABS,X | 252 | $FC | |||
| 61 | $3D | AND ABS,X | 125 | $7D | ADC ABS,X | 189 | $BD | LDA ABS,X | 253 | $FD | SBC ABS,X | 
| 62 | $3E | ROL ABS,X | 126 | $7E | ROR ABS,X | 190 | $BE | LDX ABS,Y | 254 | $FE | INC ABS,X | 
| 63 | $3F | 127 | $7F | 191 | $BF | 255 | $FF | ||||

---
*Fonte originale: [https://sta.c64.org/cbm64mcinst1.html](https://sta.c64.org/cbm64mcinst1.html)*
