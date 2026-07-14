---
title: Commodore 64 PETSCII codes (with key combinations)
source_url: https://sta.c64.org/cbm64petkey.html
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

# Commodore 64 PETSCII codes (with key combinations)

This page uses inline images for faster display. See the
  [original](https://sta.c64.org/cbm64petkey_orig.html) with linked images.

| PETSCII code (dec, hex) | Character (up/gfx, lo/up) | Key combination | PETSCII code (dec, hex) | Character (up/gfx, lo/up) | Key combination | ||||
|---|---|---|---|---|---|---|---|---|---|
| 0 | $00 | Ctrl-@ (at) | 128 | $80 | |||||
| 1 | $01 | Ctrl-A | 129 | $81 | orange | C=-1 | |||
| 2 | $02 | Ctrl-B | 130 | $82 | |||||
| 3 | $03 | Stop | Run/Stop, Ctrl-C | 131 | $83 | Run | Shift-Run/Stop | ||
| 4 | $04 | Ctrl-D | 132 | $84 | |||||
| 5 | $05 | white | Ctrl-2, Ctrl-E | 133 | $85 | F1 | F1/F2 | ||
| 6 | $06 | Ctrl-F | 134 | $86 | F3 | F3/F4 | |||
| 7 | $07 | Ctrl-G | 135 | $87 | F5 | F5/F6 | |||
| 8 | $08 | disable C=-Shift | Ctrl-H | 136 | $88 | F7 | F7/F8 | ||
| 9 | $09 | enable C=-Shift | Ctrl-I | 137 | $89 | F2 | Shift-F1/F2 | ||
| 10 | $0A | Ctrl-J | 138 | $8A | F4 | Shift-F3/F4 | |||
| 11 | $0B | Ctrl-K | 139 | $8B | F6 | Shift-F5/F6 | |||
| 12 | $0C | Ctrl-L | 140 | $8C | F8 | Shift-F7/F8 | |||
| 13 | $0D | Return | Return, Ctrl-M | 141 | $8D | Shift-Return | Shift-Return | ||
| 14 | $0E | lo/up charset | Ctrl-N | 142 | $8E | up/gfx charset | |||
| 15 | $0F | Ctrl-O | 143 | $8F | |||||
| 16 | $10 | Ctrl-P | 144 | $90 | black | Ctrl-1 | |||
| 17 | $11 | cursor down | cursor up/down, Ctrl-Q | 145 | $91 | cursor up | Shift-cursor up/down | ||
| 18 | $12 | reverse on | Ctrl-9, Ctrl-R | 146 | $92 | reverse off | Ctrl-0 | ||
| 19 | $13 | Home | Clear/Home, Ctrl-S | 147 | $93 | Clear | Shift-Clear/Home | ||
| 20 | $14 | Delete | Insert/Delete, Ctrl-T | 148 | $94 | Insert | Shift-Insert/Delete | ||
| 21 | $15 | Ctrl-U | 149 | $95 | brown | C=-2 | |||
| 22 | $16 | Ctrl-V | 150 | $96 | pink | C=-3 | |||
| 23 | $17 | Ctrl-W | 151 | $97 | dark grey | C=-4 | |||
| 24 | $18 | Ctrl-X | 152 | $98 | grey | C=-5 | |||
| 25 | $19 | Ctrl-Y | 153 | $99 | light green | C=-6 | |||
| 26 | $1A | Ctrl-Z | 154 | $9A | light blue | C=-7 | |||
| 27 | $1B | Ctrl-: (colon) | 155 | $9B | light grey | C=-8 | |||
| 28 | $1C | red | Ctrl-3, Ctrl-£ (pound) | 156 | $9C | purple | Ctrl-5 | ||
| 29 | $1D | cursor right | cursor left/right, Ctrl-; (semicolon) | 157 | $9D | cursor left | Shift-cursor left/right | ||
| 30 | $1E | green | Ctrl-6, Ctrl-↑ (up arrow) | 158 | $9E | yellow | Ctrl-8 | ||
| 31 | $1F | blue | Ctrl-7, Ctrl-= (equal) | 159 | $9F | cyan | Ctrl-4 | ||
| 32 | $20 | Space | 160 | $A0 | Shift-Space | ||||
| 33 | $21 | Shift-1 | 161 | $A1 | C=-K | ||||
| 34 | $22 | Shift-2 | 162 | $A2 | C=-I | ||||
| 35 | $23 | Shift-3 | 163 | $A3 | C=-T | ||||
| 36 | $24 | Shift-4 | 164 | $A4 | C=-@ (at) | ||||
| 37 | $25 | Shift-5 | 165 | $A5 | C=-G | ||||
| 38 | $26 | Shift-6 | 166 | $A6 | C=-+ (plus) | ||||
| 39 | $27 | Shift-7 | 167 | $A7 | C=-M | ||||
| 40 | $28 | Shift-8 | 168 | $A8 | C=-£ (pound) | ||||
| 41 | $29 | Shift-9 | 169 | $A9 | Shift-£ (pound) | ||||
| 42 | $2A | * (asterisk) | 170 | $AA | C=-N | ||||
| 43 | $2B | + (plus) | 171 | $AB | C=-Q | ||||
| 44 | $2C | , (comma) | 172 | $AC | C=-D | ||||
| 45 | $2D | – (minus) | 173 | $AD | C=-Z | ||||
| 46 | $2E | . (period) | 174 | $AE | C=-S | ||||
| 47 | $2F | / (slash) | 175 | $AF | C=-P | ||||
| 48 | $30 | 0 | 176 | $B0 | C=-A | ||||
| 49 | $31 | 1 | 177 | $B1 | C=-E | ||||
| 50 | $32 | 2 | 178 | $B2 | C=-R | ||||
| 51 | $33 | 3 | 179 | $B3 | C=-W | ||||
| 52 | $34 | 4 | 180 | $B4 | C=-H | ||||
| 53 | $35 | 5 | 181 | $B5 | C=-J | ||||
| 54 | $36 | 6 | 182 | $B6 | C=-L | ||||
| 55 | $37 | 7 | 183 | $B7 | C=-Y | ||||
| 56 | $38 | 8 | 184 | $B8 | C=-U | ||||
| 57 | $39 | 9 | 185 | $B9 | C=-O | ||||
| 58 | $3A | : (colon) | 186 | $BA | Shift-@ (at) | ||||
| 59 | $3B | ; (semicolon) | 187 | $BB | C=-F | ||||
| 60 | $3C | Shift-, (comma) | 188 | $BC | C=-C | ||||
| 61 | $3D | = (equal) | 189 | $BD | C=-X | ||||
| 62 | $3E | Shift-. (period) | 190 | $BE | C=-V | ||||
| 63 | $3F | Shift-/ (slash) | 191 | $BF | C=-B | ||||
| 64 | $40 | @ (at) | 192 | $C0 | Shift-* (asterisk) | ||||
| 65 | $41 | A | 193 | $C1 | Shift-A | ||||
| 66 | $42 | B | 194 | $C2 | Shift-B | ||||
| 67 | $43 | C | 195 | $C3 | Shift-C | ||||
| 68 | $44 | D | 196 | $C4 | Shift-D | ||||
| 69 | $45 | E | 197 | $C5 | Shift-E | ||||
| 70 | $46 | F | 198 | $C6 | Shift-F | ||||
| 71 | $47 | G | 199 | $C7 | Shift-G | ||||
| 72 | $48 | H | 200 | $C8 | Shift-H | ||||
| 73 | $49 | I | 201 | $C9 | Shift-I | ||||
| 74 | $4A | J | 202 | $CA | Shift-J | ||||
| 75 | $4B | K | 203 | $CB | Shift-K | ||||
| 76 | $4C | L | 204 | $CC | Shift-L | ||||
| 77 | $4D | M | 205 | $CD | Shift-M | ||||
| 78 | $4E | N | 206 | $CE | Shift-N | ||||
| 79 | $4F | O | 207 | $CF | Shift-O | ||||
| 80 | $50 | P | 208 | $D0 | Shift-P | ||||
| 81 | $51 | Q | 209 | $D1 | Shift-Q | ||||
| 82 | $52 | R | 210 | $D2 | Shift-R | ||||
| 83 | $53 | S | 211 | $D3 | Shift-S | ||||
| 84 | $54 | T | 212 | $D4 | Shift-T | ||||
| 85 | $55 | U | 213 | $D5 | Shift-U | ||||
| 86 | $56 | V | 214 | $D6 | Shift-V | ||||
| 87 | $57 | W | 215 | $D7 | Shift-W | ||||
| 88 | $58 | X | 216 | $D8 | Shift-X | ||||
| 89 | $59 | Y | 217 | $D9 | Shift-Y | ||||
| 90 | $5A | Z | 218 | $DA | Shift-Z | ||||
| 91 | $5B | Shift-: (colon) | 219 | $DB | Shift-+ (plus) | ||||
| 92 | $5C | £ (pound) | 220 | $DC | C=-– (minus) | ||||
| 93 | $5D | Shift-; (semicolon) | 221 | $DD | Shift-– (minus) | ||||
| 94 | $5E | ↑ (up arrow) | 222 | $DE | Shift-↑ (up arrow) | ||||
| 95 | $5F | ← (left arrow) | 223 | $DF | C=-* (asterisk) | ||||
| 96 | $60 | 224 | $E0 | ||||||
| 97 | $61 | 225 | $E1 | ||||||
| 98 | $62 | 226 | $E2 | ||||||
| 99 | $63 | 227 | $E3 | ||||||
| 100 | $64 | 228 | $E4 | ||||||
| 101 | $65 | 229 | $E5 | ||||||
| 102 | $66 | 230 | $E6 | ||||||
| 103 | $67 | 231 | $E7 | ||||||
| 104 | $68 | 232 | $E8 | ||||||
| 105 | $69 | 233 | $E9 | ||||||
| 106 | $6A | 234 | $EA | ||||||
| 107 | $6B | 235 | $EB | ||||||
| 108 | $6C | 236 | $EC | ||||||
| 109 | $6D | 237 | $ED | ||||||
| 110 | $6E | 238 | $EE | ||||||
| 111 | $6F | 239 | $EF | ||||||
| 112 | $70 | 240 | $F0 | ||||||
| 113 | $71 | 241 | $F1 | ||||||
| 114 | $72 | 242 | $F2 | ||||||
| 115 | $73 | 243 | $F3 | ||||||
| 116 | $74 | 244 | $F4 | ||||||
| 117 | $75 | 245 | $F5 | ||||||
| 118 | $76 | 246 | $F6 | ||||||
| 119 | $77 | 247 | $F7 | ||||||
| 120 | $78 | 248 | $F8 | ||||||
| 121 | $79 | 249 | $F9 | ||||||
| 122 | $7A | 250 | $FA | ||||||
| 123 | $7B | 251 | $FB | ||||||
| 124 | $7C | 252 | $FC | ||||||
| 125 | $7D | 253 | $FD | ||||||
| 126 | $7E | 254 | $FE | ||||||
| 127 | $7F | 255 | $FF | ||||||

Notes:

- Codes $00-$1F and $80-$9F are control codes. Printing them will cause a change in screen layout or behavior, not an actual character displayed. 
- Codes $60-$7F and $E0-$FE are not used. Although you can print them, these are, actually, copies of codes $C0-$DF and $A0-$BE. 
- Code $FF is the BASIC token of the π (pi) symbol. It is converted internally to code $DE when printed and, vice versa, code $DE is converted to $FF when fetched from the screen. However, when reading the keyboard buffer, you will find code $DE for Shift-↑ (up arrow) as no conversion takes place there yet.

---
*Fonte originale: [https://sta.c64.org/cbm64petkey.html](https://sta.c64.org/cbm64petkey.html)*
