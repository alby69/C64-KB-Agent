---
title: Commodore 64 PETSCII codes (with key combinations)
source_url: https://sta.c64.org/cbm64petkey_orig.html
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
| 32 | $20 | ![Space](https://sta.c64.org/cbmpet20.png) | Space | 160 | $A0 | ![Shift-Space](https://sta.c64.org/cbmpeta0.png) | Shift-Space | ||
| 33 | $21 | ![!](https://sta.c64.org/cbmpet21.png) | Shift-1 | 161 | $A1 | ![$A1](https://sta.c64.org/cbmpeta1.png) | C=-K | ||
| 34 | $22 | !["](https://sta.c64.org/cbmpet22.png) | Shift-2 | 162 | $A2 | ![$A2](https://sta.c64.org/cbmpeta2.png) | C=-I | ||
| 35 | $23 | ![#](https://sta.c64.org/cbmpet23.png) | Shift-3 | 163 | $A3 | ![$A3](https://sta.c64.org/cbmpeta3.png) | C=-T | ||
| 36 | $24 | ![$](https://sta.c64.org/cbmpet24.png) | Shift-4 | 164 | $A4 | ![$A4](https://sta.c64.org/cbmpeta4.png) | C=-@ (at) | ||
| 37 | $25 | ![%](https://sta.c64.org/cbmpet25.png) | Shift-5 | 165 | $A5 | ![$A5](https://sta.c64.org/cbmpeta5.png) | C=-G | ||
| 38 | $26 | ![&](https://sta.c64.org/cbmpet26.png) | Shift-6 | 166 | $A6 | ![$A6](https://sta.c64.org/cbmpeta6.png) | C=-+ (plus) | ||
| 39 | $27 | !['](https://sta.c64.org/cbmpet27.png) | Shift-7 | 167 | $A7 | ![$A7](https://sta.c64.org/cbmpeta7.png) | C=-M | ||
| 40 | $28 | ![(](https://sta.c64.org/cbmpet28.png) | Shift-8 | 168 | $A8 | ![$A8](https://sta.c64.org/cbmpeta8.png) | C=-£ (pound) | ||
| 41 | $29 | ![)](https://sta.c64.org/cbmpet29.png) | Shift-9 | 169 | $A9 | ![$A9](https://sta.c64.org/cbmpeta9u.png) | ![$A9](https://sta.c64.org/cbmpeta9l.png) | Shift-£ (pound) | |
| 42 | $2A | ![*](https://sta.c64.org/cbmpet2a.png) | * (asterisk) | 170 | $AA | ![$AA](https://sta.c64.org/cbmpetaa.png) | C=-N | ||
| 43 | $2B | ![+](https://sta.c64.org/cbmpet2b.png) | + (plus) | 171 | $AB | ![$AB](https://sta.c64.org/cbmpetab.png) | C=-Q | ||
| 44 | $2C | ![,](https://sta.c64.org/cbmpet2c.png) | , (comma) | 172 | $AC | ![$AC](https://sta.c64.org/cbmpetac.png) | C=-D | ||
| 45 | $2D | ![-](https://sta.c64.org/cbmpet2d.png) | – (minus) | 173 | $AD | ![$AD](https://sta.c64.org/cbmpetad.png) | C=-Z | ||
| 46 | $2E | ![.](https://sta.c64.org/cbmpet2e.png) | . (period) | 174 | $AE | ![$AE](https://sta.c64.org/cbmpetae.png) | C=-S | ||
| 47 | $2F | ![/](https://sta.c64.org/cbmpet2f.png) | / (slash) | 175 | $AF | ![$AF](https://sta.c64.org/cbmpetaf.png) | C=-P | ||
| 48 | $30 | ![0](https://sta.c64.org/cbmpet30.png) | 0 | 176 | $B0 | ![$B0](https://sta.c64.org/cbmpetb0.png) | C=-A | ||
| 49 | $31 | ![1](https://sta.c64.org/cbmpet31.png) | 1 | 177 | $B1 | ![$B1](https://sta.c64.org/cbmpetb1.png) | C=-E | ||
| 50 | $32 | ![2](https://sta.c64.org/cbmpet32.png) | 2 | 178 | $B2 | ![$B2](https://sta.c64.org/cbmpetb2.png) | C=-R | ||
| 51 | $33 | ![3](https://sta.c64.org/cbmpet33.png) | 3 | 179 | $B3 | ![$B3](https://sta.c64.org/cbmpetb3.png) | C=-W | ||
| 52 | $34 | ![4](https://sta.c64.org/cbmpet34.png) | 4 | 180 | $B4 | ![$B4](https://sta.c64.org/cbmpetb4.png) | C=-H | ||
| 53 | $35 | ![5](https://sta.c64.org/cbmpet35.png) | 5 | 181 | $B5 | ![$B5](https://sta.c64.org/cbmpetb5.png) | C=-J | ||
| 54 | $36 | ![6](https://sta.c64.org/cbmpet36.png) | 6 | 182 | $B6 | ![$B6](https://sta.c64.org/cbmpetb6.png) | C=-L | ||
| 55 | $37 | ![7](https://sta.c64.org/cbmpet37.png) | 7 | 183 | $B7 | ![$B7](https://sta.c64.org/cbmpetb7.png) | C=-Y | ||
| 56 | $38 | ![8](https://sta.c64.org/cbmpet38.png) | 8 | 184 | $B8 | ![$B8](https://sta.c64.org/cbmpetb8.png) | C=-U | ||
| 57 | $39 | ![9](https://sta.c64.org/cbmpet39.png) | 9 | 185 | $B9 | ![$B9](https://sta.c64.org/cbmpetb9.png) | C=-O | ||
| 58 | $3A | ![:](https://sta.c64.org/cbmpet3a.png) | : (colon) | 186 | $BA | ![$BA](https://sta.c64.org/cbmpetbau.png) | ![$BA](https://sta.c64.org/cbmpetbal.png) | Shift-@ (at) | |
| 59 | $3B | ![;](https://sta.c64.org/cbmpet3b.png) | ; (semicolon) | 187 | $BB | ![$BB](https://sta.c64.org/cbmpetbb.png) | C=-F | ||
| 60 | $3C | ![<](https://sta.c64.org/cbmpet3c.png) | Shift-, (comma) | 188 | $BC | ![$BC](https://sta.c64.org/cbmpetbc.png) | C=-C | ||
| 61 | $3D | ![=](https://sta.c64.org/cbmpet3d.png) | = (equal) | 189 | $BD | ![$BD](https://sta.c64.org/cbmpetbd.png) | C=-X | ||
| 62 | $3E | ![>](https://sta.c64.org/cbmpet3e.png) | Shift-. (period) | 190 | $BE | ![$BE](https://sta.c64.org/cbmpetbe.png) | C=-V | ||
| 63 | $3F | ![?](https://sta.c64.org/cbmpet3f.png) | Shift-/ (slash) | 191 | $BF | ![$BF](https://sta.c64.org/cbmpetbf.png) | C=-B | ||
| 64 | $40 | ![@](https://sta.c64.org/cbmpet40.png) | @ (at) | 192 | $C0 | ![$C0](https://sta.c64.org/cbmpetc0.png) | Shift-* (asterisk) | ||
| 65 | $41 | ![A](https://sta.c64.org/cbmpet41u.png) | ![a](https://sta.c64.org/cbmpet41l.png) | A | 193 | $C1 | ![$C1](https://sta.c64.org/cbmpetc1.png) | ![A](https://sta.c64.org/cbmpet41u.png) | Shift-A | 
| 66 | $42 | ![B](https://sta.c64.org/cbmpet42u.png) | ![b](https://sta.c64.org/cbmpet42l.png) | B | 194 | $C2 | ![$C2](https://sta.c64.org/cbmpetc2.png) | ![B](https://sta.c64.org/cbmpet42u.png) | Shift-B | 
| 67 | $43 | ![C](https://sta.c64.org/cbmpet43u.png) | ![c](https://sta.c64.org/cbmpet43l.png) | C | 195 | $C3 | ![$C3](https://sta.c64.org/cbmpetc3.png) | ![C](https://sta.c64.org/cbmpet43u.png) | Shift-C | 
| 68 | $44 | ![D](https://sta.c64.org/cbmpet44u.png) | ![d](https://sta.c64.org/cbmpet44l.png) | D | 196 | $C4 | ![$C4](https://sta.c64.org/cbmpetc4.png) | ![D](https://sta.c64.org/cbmpet44u.png) | Shift-D | 
| 69 | $45 | ![E](https://sta.c64.org/cbmpet45u.png) | ![e](https://sta.c64.org/cbmpet45l.png) | E | 197 | $C5 | ![$C5](https://sta.c64.org/cbmpetc5.png) | ![E](https://sta.c64.org/cbmpet45u.png) | Shift-E | 
| 70 | $46 | ![F](https://sta.c64.org/cbmpet46u.png) | ![f](https://sta.c64.org/cbmpet46l.png) | F | 198 | $C6 | ![$C6](https://sta.c64.org/cbmpetc6.png) | ![F](https://sta.c64.org/cbmpet46u.png) | Shift-F | 
| 71 | $47 | ![G](https://sta.c64.org/cbmpet47u.png) | ![g](https://sta.c64.org/cbmpet47l.png) | G | 199 | $C7 | ![$C7](https://sta.c64.org/cbmpetc7.png) | ![G](https://sta.c64.org/cbmpet47u.png) | Shift-G | 
| 72 | $48 | ![H](https://sta.c64.org/cbmpet48u.png) | ![h](https://sta.c64.org/cbmpet48l.png) | H | 200 | $C8 | ![$C8](https://sta.c64.org/cbmpetc8.png) | ![H](https://sta.c64.org/cbmpet48u.png) | Shift-H | 
| 73 | $49 | ![I](https://sta.c64.org/cbmpet49u.png) | ![i](https://sta.c64.org/cbmpet49l.png) | I | 201 | $C9 | ![$C9](https://sta.c64.org/cbmpetc9.png) | ![I](https://sta.c64.org/cbmpet49u.png) | Shift-I | 
| 74 | $4A | ![J](https://sta.c64.org/cbmpet4au.png) | ![j](https://sta.c64.org/cbmpet4al.png) | J | 202 | $CA | ![$CA](https://sta.c64.org/cbmpetca.png) | ![J](https://sta.c64.org/cbmpet4au.png) | Shift-J | 
| 75 | $4B | ![K](https://sta.c64.org/cbmpet4bu.png) | ![k](https://sta.c64.org/cbmpet4bl.png) | K | 203 | $CB | ![$CB](https://sta.c64.org/cbmpetcb.png) | ![K](https://sta.c64.org/cbmpet4bu.png) | Shift-K | 
| 76 | $4C | ![L](https://sta.c64.org/cbmpet4cu.png) | ![l](https://sta.c64.org/cbmpet4cl.png) | L | 204 | $CC | ![$CC](https://sta.c64.org/cbmpetcc.png) | ![L](https://sta.c64.org/cbmpet4cu.png) | Shift-L | 
| 77 | $4D | ![M](https://sta.c64.org/cbmpet4du.png) | ![m](https://sta.c64.org/cbmpet4dl.png) | M | 205 | $CD | ![$CD](https://sta.c64.org/cbmpetcd.png) | ![M](https://sta.c64.org/cbmpet4du.png) | Shift-M | 
| 78 | $4E | ![N](https://sta.c64.org/cbmpet4eu.png) | ![n](https://sta.c64.org/cbmpet4el.png) | N | 206 | $CE | ![$CE](https://sta.c64.org/cbmpetce.png) | ![N](https://sta.c64.org/cbmpet4eu.png) | Shift-N | 
| 79 | $4F | ![O](https://sta.c64.org/cbmpet4fu.png) | ![o](https://sta.c64.org/cbmpet4fl.png) | O | 207 | $CF | ![$CF](https://sta.c64.org/cbmpetcf.png) | ![O](https://sta.c64.org/cbmpet4fu.png) | Shift-O | 
| 80 | $50 | ![P](https://sta.c64.org/cbmpet50u.png) | ![p](https://sta.c64.org/cbmpet50l.png) | P | 208 | $D0 | ![$D0](https://sta.c64.org/cbmpetd0.png) | ![P](https://sta.c64.org/cbmpet50u.png) | Shift-P | 
| 81 | $51 | ![Q](https://sta.c64.org/cbmpet51u.png) | ![q](https://sta.c64.org/cbmpet51l.png) | Q | 209 | $D1 | ![$D1](https://sta.c64.org/cbmpetd1.png) | ![Q](https://sta.c64.org/cbmpet51u.png) | Shift-Q | 
| 82 | $52 | ![R](https://sta.c64.org/cbmpet52u.png) | ![r](https://sta.c64.org/cbmpet52l.png) | R | 210 | $D2 | ![$D2](https://sta.c64.org/cbmpetd2.png) | ![R](https://sta.c64.org/cbmpet52u.png) | Shift-R | 
| 83 | $53 | ![S](https://sta.c64.org/cbmpet53u.png) | ![s](https://sta.c64.org/cbmpet53l.png) | S | 211 | $D3 | ![$D3](https://sta.c64.org/cbmpetd3.png) | ![S](https://sta.c64.org/cbmpet53u.png) | Shift-S | 
| 84 | $54 | ![T](https://sta.c64.org/cbmpet54u.png) | ![t](https://sta.c64.org/cbmpet54l.png) | T | 212 | $D4 | ![$D4](https://sta.c64.org/cbmpetd4.png) | ![T](https://sta.c64.org/cbmpet54u.png) | Shift-T | 
| 85 | $55 | ![U](https://sta.c64.org/cbmpet55u.png) | ![u](https://sta.c64.org/cbmpet55l.png) | U | 213 | $D5 | ![$D5](https://sta.c64.org/cbmpetd5.png) | ![U](https://sta.c64.org/cbmpet55u.png) | Shift-U | 
| 86 | $56 | ![V](https://sta.c64.org/cbmpet56u.png) | ![v](https://sta.c64.org/cbmpet56l.png) | V | 214 | $D6 | ![$D6](https://sta.c64.org/cbmpetd6.png) | ![V](https://sta.c64.org/cbmpet56u.png) | Shift-V | 
| 87 | $57 | ![W](https://sta.c64.org/cbmpet57u.png) | ![w](https://sta.c64.org/cbmpet57l.png) | W | 215 | $D7 | ![$D7](https://sta.c64.org/cbmpetd7.png) | ![W](https://sta.c64.org/cbmpet57u.png) | Shift-W | 
| 88 | $58 | ![X](https://sta.c64.org/cbmpet58u.png) | ![x](https://sta.c64.org/cbmpet58l.png) | X | 216 | $D8 | ![$D8](https://sta.c64.org/cbmpetd8.png) | ![X](https://sta.c64.org/cbmpet58u.png) | Shift-X | 
| 89 | $59 | ![Y](https://sta.c64.org/cbmpet59u.png) | ![y](https://sta.c64.org/cbmpet59l.png) | Y | 217 | $D9 | ![$D9](https://sta.c64.org/cbmpetd9.png) | ![Y](https://sta.c64.org/cbmpet59u.png) | Shift-Y | 
| 90 | $5A | ![Z](https://sta.c64.org/cbmpet5au.png) | ![z](https://sta.c64.org/cbmpet5al.png) | Z | 218 | $DA | ![$DA](https://sta.c64.org/cbmpetda.png) | ![Z](https://sta.c64.org/cbmpet5au.png) | Shift-Z | 
| 91 | $5B | ![[](https://sta.c64.org/cbmpet5b.png) | Shift-: (colon) | 219 | $DB | ![$DB](https://sta.c64.org/cbmpetdb.png) | Shift-+ (plus) | ||
| 92 | $5C | ![pound](https://sta.c64.org/cbmpet5c.png) | £ (pound) | 220 | $DC | ![$DC](https://sta.c64.org/cbmpetdc.png) | C=-– (minus) | ||
| 93 | $5D | ![]](https://sta.c64.org/cbmpet5d.png) | Shift-; (semicolon) | 221 | $DD | ![$DD](https://sta.c64.org/cbmpetdd.png) | Shift-– (minus) | ||
| 94 | $5E | ![up arrow](https://sta.c64.org/cbmpet5e.png) | ↑ (up arrow) | 222 | $DE | ![$DE](https://sta.c64.org/cbmpetdeu.png) | ![$DE](https://sta.c64.org/cbmpetdel.png) | Shift-↑ (up arrow) | |
| 95 | $5F | ![left arrow](https://sta.c64.org/cbmpet5f.png) | ← (left arrow) | 223 | $DF | ![$DF](https://sta.c64.org/cbmpetdfu.png) | ![$DF](https://sta.c64.org/cbmpetdfl.png) | C=-* (asterisk) | |
| 96 | $60 | ![$C0](https://sta.c64.org/cbmpetc0.png) | 224 | $E0 | ![$A0](https://sta.c64.org/cbmpeta0.png) | ||||
| 97 | $61 | ![$C1](https://sta.c64.org/cbmpetc1.png) | ![$41](https://sta.c64.org/cbmpet41u.png) | 225 | $E1 | ![$A1](https://sta.c64.org/cbmpeta1.png) | |||
| 98 | $62 | ![$C2](https://sta.c64.org/cbmpetc2.png) | ![$42](https://sta.c64.org/cbmpet42u.png) | 226 | $E2 | ![$A2](https://sta.c64.org/cbmpeta2.png) | |||
| 99 | $63 | ![$C3](https://sta.c64.org/cbmpetc3.png) | ![$43](https://sta.c64.org/cbmpet43u.png) | 227 | $E3 | ![$A3](https://sta.c64.org/cbmpeta3.png) | |||
| 100 | $64 | ![$C4](https://sta.c64.org/cbmpetc4.png) | ![$44](https://sta.c64.org/cbmpet44u.png) | 228 | $E4 | ![$A4](https://sta.c64.org/cbmpeta4.png) | |||
| 101 | $65 | ![$C5](https://sta.c64.org/cbmpetc5.png) | ![$45](https://sta.c64.org/cbmpet45u.png) | 229 | $E5 | ![$A5](https://sta.c64.org/cbmpeta5.png) | |||
| 102 | $66 | ![$C6](https://sta.c64.org/cbmpetc6.png) | ![$46](https://sta.c64.org/cbmpet46u.png) | 230 | $E6 | ![$A6](https://sta.c64.org/cbmpeta6.png) | |||
| 103 | $67 | ![$C7](https://sta.c64.org/cbmpetc7.png) | ![$47](https://sta.c64.org/cbmpet47u.png) | 231 | $E7 | ![$A7](https://sta.c64.org/cbmpeta7.png) | |||
| 104 | $68 | ![$C8](https://sta.c64.org/cbmpetc8.png) | ![$48](https://sta.c64.org/cbmpet48u.png) | 232 | $E8 | ![$A8](https://sta.c64.org/cbmpeta8.png) | |||
| 105 | $69 | ![$C9](https://sta.c64.org/cbmpetc9.png) | ![$49](https://sta.c64.org/cbmpet49u.png) | 233 | $E9 | ![$A9](https://sta.c64.org/cbmpeta9u.png) | ![$A9](https://sta.c64.org/cbmpeta9l.png) | ||
| 106 | $6A | ![$CA](https://sta.c64.org/cbmpetca.png) | ![$4A](https://sta.c64.org/cbmpet4au.png) | 234 | $EA | ![$AA](https://sta.c64.org/cbmpetaa.png) | |||
| 107 | $6B | ![$CB](https://sta.c64.org/cbmpetcb.png) | ![$4B](https://sta.c64.org/cbmpet4bu.png) | 235 | $EB | ![$AB](https://sta.c64.org/cbmpetab.png) | |||
| 108 | $6C | ![$CC](https://sta.c64.org/cbmpetcc.png) | ![$4C](https://sta.c64.org/cbmpet4cu.png) | 236 | $EC | ![$AC](https://sta.c64.org/cbmpetac.png) | |||
| 109 | $6D | ![$CD](https://sta.c64.org/cbmpetcd.png) | ![$4D](https://sta.c64.org/cbmpet4du.png) | 237 | $ED | ![$AD](https://sta.c64.org/cbmpetad.png) | |||
| 110 | $6E | ![$CE](https://sta.c64.org/cbmpetce.png) | ![$4E](https://sta.c64.org/cbmpet4eu.png) | 238 | $EE | ![$AE](https://sta.c64.org/cbmpetae.png) | |||
| 111 | $6F | ![$CF](https://sta.c64.org/cbmpetcf.png) | ![$4F](https://sta.c64.org/cbmpet4fu.png) | 239 | $EF | ![$AF](https://sta.c64.org/cbmpetaf.png) | |||
| 112 | $70 | ![$D0](https://sta.c64.org/cbmpetd0.png) | ![$50](https://sta.c64.org/cbmpet50u.png) | 240 | $F0 | ![$B0](https://sta.c64.org/cbmpetb0.png) | |||
| 113 | $71 | ![$D1](https://sta.c64.org/cbmpetd1.png) | ![$51](https://sta.c64.org/cbmpet51u.png) | 241 | $F1 | ![$B1](https://sta.c64.org/cbmpetb1.png) | |||
| 114 | $72 | ![$D2](https://sta.c64.org/cbmpetd2.png) | ![$52](https://sta.c64.org/cbmpet52u.png) | 242 | $F2 | ![$B2](https://sta.c64.org/cbmpetb2.png) | |||
| 115 | $73 | ![$D3](https://sta.c64.org/cbmpetd3.png) | ![$53](https://sta.c64.org/cbmpet53u.png) | 243 | $F3 | ![$B3](https://sta.c64.org/cbmpetb3.png) | |||
| 116 | $74 | ![$D4](https://sta.c64.org/cbmpetd4.png) | ![$54](https://sta.c64.org/cbmpet54u.png) | 244 | $F4 | ![$B4](https://sta.c64.org/cbmpetb4.png) | |||
| 117 | $75 | ![$D5](https://sta.c64.org/cbmpetd5.png) | ![$55](https://sta.c64.org/cbmpet55u.png) | 245 | $F5 | ![$B5](https://sta.c64.org/cbmpetb5.png) | |||
| 118 | $76 | ![$D6](https://sta.c64.org/cbmpetd6.png) | ![$56](https://sta.c64.org/cbmpet56u.png) | 246 | $F6 | ![$B6](https://sta.c64.org/cbmpetb6.png) | |||
| 119 | $77 | ![$D7](https://sta.c64.org/cbmpetd7.png) | ![$57](https://sta.c64.org/cbmpet57u.png) | 247 | $F7 | ![$B7](https://sta.c64.org/cbmpetb7.png) | |||
| 120 | $78 | ![$D8](https://sta.c64.org/cbmpetd8.png) | ![$58](https://sta.c64.org/cbmpet58u.png) | 248 | $F8 | ![$B8](https://sta.c64.org/cbmpetb8.png) | |||
| 121 | $79 | ![$D9](https://sta.c64.org/cbmpetd9.png) | ![$59](https://sta.c64.org/cbmpet59u.png) | 249 | $F9 | ![$B9](https://sta.c64.org/cbmpetb9.png) | |||
| 122 | $7A | ![$DA](https://sta.c64.org/cbmpetda.png) | ![$5A](https://sta.c64.org/cbmpet5au.png) | 250 | $FA | ![$BA](https://sta.c64.org/cbmpetbau.png) | ![$BA](https://sta.c64.org/cbmpetbal.png) | ||
| 123 | $7B | ![$DB](https://sta.c64.org/cbmpetdb.png) | 251 | $FB | ![$BB](https://sta.c64.org/cbmpetbb.png) | ||||
| 124 | $7C | ![$DC](https://sta.c64.org/cbmpetdc.png) | 252 | $FC | ![$BC](https://sta.c64.org/cbmpetbc.png) | ||||
| 125 | $7D | ![$DD](https://sta.c64.org/cbmpetdd.png) | 253 | $FD | ![$BD](https://sta.c64.org/cbmpetbd.png) | ||||
| 126 | $7E | ![$DE](https://sta.c64.org/cbmpetdeu.png) | ![$DE](https://sta.c64.org/cbmpetdel.png) | 254 | $FE | ![$BE](https://sta.c64.org/cbmpetbe.png) | |||
| 127 | $7F | ![$DF](https://sta.c64.org/cbmpetdfu.png) | ![$DF](https://sta.c64.org/cbmpetdfl.png) | 255 | $FF | ![$DE](https://sta.c64.org/cbmpetdeu.png) | ![$DE](https://sta.c64.org/cbmpetdel.png) | ||

Notes:

- Codes $00-$1F and $80-$9F are control codes. Printing them will cause a change in screen layout or behavior, not an actual character displayed. 
- Codes $60-$7F and $E0-$FE are not used. Although you can print them, these are, actually, copies of codes $C0-$DF and $A0-$BE. 
- Code $FF is the BASIC token of the π (pi) symbol. It is converted internally to code $DE when printed and, vice versa, code $DE is converted to $FF when fetched from the screen. However, when reading the keyboard buffer, you will find code $DE for Shift-↑ (up arrow) as no conversion takes place there yet.

---
*Fonte originale: [https://sta.c64.org/cbm64petkey_orig.html](https://sta.c64.org/cbm64petkey_orig.html)*
