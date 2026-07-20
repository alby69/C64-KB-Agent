---
title: Commodore 64 BASIC instructions (sorted by instruction)
source_url: https://sta.c64.org/cbm64basins1.html
category: reference
topics:
- basic
difficulty: intermediate
language: basic
hardware:
- BASIC ROM
- CIA
related:
- cia-registers
- keyboard-handling
- joystick-reading
scraped_at: '2026-07-20'
last_modified: Mon, 03 Mar 2025 00:00:00 GMT
---

# Commodore 64 BASIC instructions (sorted by instruction)

| Instruction | Token (hex, dec) | Exec address | Type | ||
|---|---|---|---|---|---|
| ABS | abs | $B6 | 182 | $BC58 | Function, numerical | 
| AND | aN | $AF | 175 | $AFE9 | Operator, logical | 
| ASC | aS | $C6 | 198 | $B78B | Function, numerical | 
| ATN | aT | $C1 | 193 | $E30E | Function, numerical | 
| CHR$ | cH | $C7 | 199 | $B6EC | Function, string | 
| CLOSE | clO | $A0 | 160 | $E1C7 | Instruction/command | 
| CLR | cL | $9C | 156 | $A65E | Instruction/command | 
| CMD | cM | $9D | 157 | $AA86 | Instruction/command | 
| CONT | cO | $9A | 154 | $A857 | Command | 
| COS | cos | $BE | 190 | $E264 | Function, numerical | 
| DATA | dA | $83 | 131 | $A8F8 | Instruction/command | 
| DEF | dE | $96 | 150 | $B3F3 | Instruction | 
| DIM | dI | $86 | 134 | $B081 | Instruction/command | 
| END | eN | $80 | 128 | $A831 | Instruction/command | 
| EXP | eX | $BD | 189 | $BFED | Function, numerical | 
| FN | fn | $A5 | 165 | $B3F4 | Function, numerical, special | 
| FOR | fO | $81 | 129 | $A742 | Instruction/command | 
| FRE | fR | $B8 | 184 | $B37D | Function, numerical, special | 
| GET | gE | $A1 | 161 | $AB7B | Instruction | 
| GO | go | $CB | 203 | $A812 | Instruction/command, special | 
| GOSUB | goS | $8D | 141 | $A883 | Instruction/command | 
| GOTO | gO | $89 | 137 | $A8A0 | Instruction/command | 
| IF | if | $8B | 139 | $A928 | Instruction/command | 
| INPUT | input | $85 | 133 | $ABBF | Instruction | 
| INPUT# | iN | $84 | 132 | $ABA5 | Instruction | 
| INT | int | $B5 | 181 | $BCCC | Function, numerical | 
| LEFT$ | leF | $C8 | 200 | $B700 | Function, string | 
| LEN | len | $C3 | 195 | $B77C | Function, numerical | 
| LET | lE | $88 | 136 | $A9A5 | Instruction/command | 
| LIST | lI | $9B | 155 | $A69C | Instruction/command | 
| LOAD | lO | $93 | 147 | $E168 | Instruction/command | 
| LOG | log | $BC | 188 | $B9EA | Function, numerical | 
| MID$ | mI | $CA | 202 | $B737 | Function, string | 
| NEW | new | $A2 | 162 | $A642 | Instruction/command | 
| NEXT | nE | $82 | 130 | $AD1E | Instruction/command | 
| NOT | nO | $A8 | 168 | $AED4 | Operator, logical | 
| ON | on | $91 | 145 | $A94B | Instruction/command | 
| OPEN | oP | $9F | 159 | $E1BE | Instruction/command | 
| OR | or | $B0 | 176 | $AFE6 | Operator, logical | 
| PEEK | pE | $C2 | 194 | $B80E | Function, numerical | 
| POKE | pO | $97 | 151 | $B824 | Instruction/command | 
| POS | pos | $B9 | 185 | $B39E | Function, numerical, special | 
| ? | $99 | 153 | $AAA0 | Instruction/command | |
| PRINT# | pR | $98 | 152 | $AA80 | Instruction/command | 
| READ | rE | $87 | 135 | $AC06 | Instruction | 
| REM | rem | $8F | 143 | $A93B | Instruction/command | 
| RESTORE | reS | $8C | 140 | $A81d | Instruction/command | 
| RETURN | reT | $8E | 142 | $A8D2 | Instruction/command | 
| RIGHT$ | rI | $C9 | 201 | $B72C | Function, string | 
| RND | rN | $BB | 187 | $E097 | Function, numerical | 
| RUN | rU | $8A | 138 | $A871 | Instruction/command | 
| SAVE | sA | $94 | 148 | $E156 | Instruction/command | 
| SGN | sG | $B4 | 180 | $BC39 | Function, numerical | 
| SIN | sI | $BF | 191 | $E26B | Function, numerical | 
| SPC( | sP | $A6 | 166 | $AAF8 | Function, PRINT (Carry = 0!) | 
| SQR | sQ | $BA | 186 | $BF71 | Function, numerical | 
| STEP | stE | $A9 | 169 | $A799 | Instruction/command, special | 
| STOP | sT | $90 | 144 | $A82F | Instruction/command | 
| STR$ | stR | $C4 | 196 | $B465 | Function, string | 
| SYS | sY | $9E | 158 | $E12A | Instruction/command | 
| TAB( | tA | $A3 | 163 | $AAF8 | Function, PRINT (Carry = 1!) | 
| TAN | tan | $C0 | 192 | $E2B4 | Function, numerical | 
| THEN | tH | $A7 | 167 | $A932 | Instruction/command, special | 
| TO | to | $A4 | 164 | $A76D | Instruction/command, special | 
| USR | uS | $B7 | 183 | $0310 | Function, numerical/string | 
| VAL | vA | $C5 | 197 | $B7AD | Function, numerical | 
| VERIFY | vE | $95 | 149 | $E165 | Instruction/command | 
| WAIT | wA | $92 | 146 | $B82D | Instruction/command | 
| + | + | $AA | 170 | $B86A | Operator, numerical/string | 
| - | - | $AB | 171 | $B853 | Operator, numerical | 
| * | * | $AC | 172 | $BA2B | Operator, numerical | 
| / | / | $AD | 173 | $BB12 | Operator, numerical | 
| ^ | ^ | $AE | 174 | $BF7B | Operator, numerical | 
| > | > | $B1 | 177 | $B016 | Operator, logical | 
| = | = | $B2 | 178 | $B016 | Operator, logical | 
| < | < | $B3 | 179 | $B016 | Operator, logical | 
| π (pi) | π (pi) | $FF | 255 | $AE9E | Function, numerical, special |

---
*Fonte originale: [https://sta.c64.org/cbm64basins1.html](https://sta.c64.org/cbm64basins1.html)*
