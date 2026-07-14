---
title: Commodore 64 PETSCII codes
source_url: https://sta.c64.org/cbm64pet.html
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware:
- CIA
- BASIC ROM
- KERNAL
related:
- joystick-reading
- keyboard-handling
- memory-map
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
last_modified: Sat, 13 Mar 2021 23:00:00 GMT
---

# Commodore 64 PETSCII codes

This page uses inline images for faster display. See the
  [original](https://sta.c64.org/cbm64pet_orig.html) with linked images.

| PETSCII code (dec, hex) | Character (up/gfx, lo/up) | PETSCII code (dec, hex) | Character (up/gfx, lo/up) | PETSCII code (dec, hex) | Character (up/gfx, lo/up) | PETSCII code (dec, hex) | Character (up/gfx, lo/up) | ||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | $00 | 64 | $40 | 128 | $80 | 192 | $C0 | ||||||||
| 1 | $01 | 65 | $41 | 129 | $81 | orange | 193 | $C1 | |||||||
| 2 | $02 | 66 | $42 | 130 | $82 | 194 | $C2 | ||||||||
| 3 | $03 | Stop | 67 | $43 | 131 | $83 | Run | 195 | $C3 | ||||||
| 4 | $04 | 68 | $44 | 132 | $84 | 196 | $C4 | ||||||||
| 5 | $05 | white | 69 | $45 | 133 | $85 | F1 | 197 | $C5 | ||||||
| 6 | $06 | 70 | $46 | 134 | $86 | F3 | 198 | $C6 | |||||||
| 7 | $07 | 71 | $47 | 135 | $87 | F5 | 199 | $C7 | |||||||
| 8 | $08 | disable C=-Shift | 72 | $48 | 136 | $88 | F7 | 200 | $C8 | ||||||
| 9 | $09 | enable C=-Shift | 73 | $49 | 137 | $89 | F2 | 201 | $C9 | ||||||
| 10 | $0A | 74 | $4A | 138 | $8A | F4 | 202 | $CA | |||||||
| 11 | $0B | 75 | $4B | 139 | $8B | F6 | 203 | $CB | |||||||
| 12 | $0C | 76 | $4C | 140 | $8C | F8 | 204 | $CC | |||||||
| 13 | $0D | Return | 77 | $4D | 141 | $8D | Shift-Return | 205 | $CD | ||||||
| 14 | $0E | lo/up charset | 78 | $4E | 142 | $8E | up/gfx charset | 206 | $CE | ||||||
| 15 | $0F | 79 | $4F | 143 | $8F | 207 | $CF | ||||||||
| 16 | $10 | 80 | $50 | 144 | $90 | black | 208 | $D0 | |||||||
| 17 | $11 | cursor down | 81 | $51 | 145 | $91 | cursor up | 209 | $D1 | ||||||
| 18 | $12 | reverse on | 82 | $52 | 146 | $92 | reverse off | 210 | $D2 | ||||||
| 19 | $13 | Home | 83 | $53 | 147 | $93 | Clear | 211 | $D3 | ||||||
| 20 | $14 | Delete | 84 | $54 | 148 | $94 | Insert | 212 | $D4 | ||||||
| 21 | $15 | 85 | $55 | 149 | $95 | brown | 213 | $D5 | |||||||
| 22 | $16 | 86 | $56 | 150 | $96 | pink | 214 | $D6 | |||||||
| 23 | $17 | 87 | $57 | 151 | $97 | dark grey | 215 | $D7 | |||||||
| 24 | $18 | 88 | $58 | 152 | $98 | grey | 216 | $D8 | |||||||
| 25 | $19 | 89 | $59 | 153 | $99 | light green | 217 | $D9 | |||||||
| 26 | $1A | 90 | $5A | 154 | $9A | light blue | 218 | $DA | |||||||
| 27 | $1B | 91 | $5B | 155 | $9B | light grey | 219 | $DB | |||||||
| 28 | $1C | red | 92 | $5C | 156 | $9C | purple | 220 | $DC | ||||||
| 29 | $1D | cursor right | 93 | $5D | 157 | $9D | cursor left | 221 | $DD | ||||||
| 30 | $1E | green | 94 | $5E | 158 | $9E | yellow | 222 | $DE | ||||||
| 31 | $1F | blue | 95 | $5F | 159 | $9F | cyan | 223 | $DF | ||||||
| 32 | $20 | 96 | $60 | 160 | $A0 | 224 | $E0 | ||||||||
| 33 | $21 | 97 | $61 | 161 | $A1 | 225 | $E1 | ||||||||
| 34 | $22 | 98 | $62 | 162 | $A2 | 226 | $E2 | ||||||||
| 35 | $23 | 99 | $63 | 163 | $A3 | 227 | $E3 | ||||||||
| 36 | $24 | 100 | $64 | 164 | $A4 | 228 | $E4 | ||||||||
| 37 | $25 | 101 | $65 | 165 | $A5 | 229 | $E5 | ||||||||
| 38 | $26 | 102 | $66 | 166 | $A6 | 230 | $E6 | ||||||||
| 39 | $27 | 103 | $67 | 167 | $A7 | 231 | $E7 | ||||||||
| 40 | $28 | 104 | $68 | 168 | $A8 | 232 | $E8 | ||||||||
| 41 | $29 | 105 | $69 | 169 | $A9 | 233 | $E9 | ||||||||
| 42 | $2A | 106 | $6A | 170 | $AA | 234 | $EA | ||||||||
| 43 | $2B | 107 | $6B | 171 | $AB | 235 | $EB | ||||||||
| 44 | $2C | 108 | $6C | 172 | $AC | 236 | $EC | ||||||||
| 45 | $2D | 109 | $6D | 173 | $AD | 237 | $ED | ||||||||
| 46 | $2E | 110 | $6E | 174 | $AE | 238 | $EE | ||||||||
| 47 | $2F | 111 | $6F | 175 | $AF | 239 | $EF | ||||||||
| 48 | $30 | 112 | $70 | 176 | $B0 | 240 | $F0 | ||||||||
| 49 | $31 | 113 | $71 | 177 | $B1 | 241 | $F1 | ||||||||
| 50 | $32 | 114 | $72 | 178 | $B2 | 242 | $F2 | ||||||||
| 51 | $33 | 115 | $73 | 179 | $B3 | 243 | $F3 | ||||||||
| 52 | $34 | 116 | $74 | 180 | $B4 | 244 | $F4 | ||||||||
| 53 | $35 | 117 | $75 | 181 | $B5 | 245 | $F5 | ||||||||
| 54 | $36 | 118 | $76 | 182 | $B6 | 246 | $F6 | ||||||||
| 55 | $37 | 119 | $77 | 183 | $B7 | 247 | $F7 | ||||||||
| 56 | $38 | 120 | $78 | 184 | $B8 | 248 | $F8 | ||||||||
| 57 | $39 | 121 | $79 | 185 | $B9 | 249 | $F9 | ||||||||
| 58 | $3A | 122 | $7A | 186 | $BA | 250 | $FA | ||||||||
| 59 | $3B | 123 | $7B | 187 | $BB | 251 | $FB | ||||||||
| 60 | $3C | 124 | $7C | 188 | $BC | 252 | $FC | ||||||||
| 61 | $3D | 125 | $7D | 189 | $BD | 253 | $FD | ||||||||
| 62 | $3E | 126 | $7E | 190 | $BE | 254 | $FE | ||||||||
| 63 | $3F | 127 | $7F | 191 | $BF | 255 | $FF | ||||||||

Notes:

- Codes $00-$1F and $80-$9F are control codes. Printing them will cause a change in screen layout or behavior, not an actual character displayed. 
- Codes $60-$7F and $E0-$FE are not used. Although you can print them, these are, actually, copies of codes $C0-$DF and $A0-$BE. 
- Code $FF is the BASIC token of the π (pi) symbol. It is converted internally to code $DE when printed and, vice versa, code $DE is converted to $FF when fetched from the screen. However, when reading the keyboard buffer, you will find code $DE for Shift-↑ (up arrow) as no conversion takes place there yet.

---
*Fonte originale: [https://sta.c64.org/cbm64pet.html](https://sta.c64.org/cbm64pet.html)*
