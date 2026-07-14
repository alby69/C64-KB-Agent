---
title: Commodore 64 PETSCII codes
source_url: https://sta.c64.org/cbm64pet_orig.html
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

| PETSCII code (dec, hex) | Character (up/gfx, lo/up) | PETSCII code (dec, hex) | Character (up/gfx, lo/up) | PETSCII code (dec, hex) | Character (up/gfx, lo/up) | PETSCII code (dec, hex) | Character (up/gfx, lo/up) | ||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | $00 | 64 | $40 | ![@](https://sta.c64.org/cbmpet40.png) | 128 | $80 | 192 | $C0 | ![$C0](https://sta.c64.org/cbmpetc0.png) | ||||||
| 1 | $01 | 65 | $41 | ![A](https://sta.c64.org/cbmpet41u.png) | ![a](https://sta.c64.org/cbmpet41l.png) | 129 | $81 | orange | 193 | $C1 | ![$C1](https://sta.c64.org/cbmpetc1.png) | ![A](https://sta.c64.org/cbmpet41u.png) | |||
| 2 | $02 | 66 | $42 | ![B](https://sta.c64.org/cbmpet42u.png) | ![b](https://sta.c64.org/cbmpet42l.png) | 130 | $82 | 194 | $C2 | ![$C2](https://sta.c64.org/cbmpetc2.png) | ![B](https://sta.c64.org/cbmpet42u.png) | ||||
| 3 | $03 | Stop | 67 | $43 | ![C](https://sta.c64.org/cbmpet43u.png) | ![c](https://sta.c64.org/cbmpet43l.png) | 131 | $83 | Run | 195 | $C3 | ![$C3](https://sta.c64.org/cbmpetc3.png) | ![C](https://sta.c64.org/cbmpet43u.png) | ||
| 4 | $04 | 68 | $44 | ![D](https://sta.c64.org/cbmpet44u.png) | ![d](https://sta.c64.org/cbmpet44l.png) | 132 | $84 | 196 | $C4 | ![$C4](https://sta.c64.org/cbmpetc4.png) | ![D](https://sta.c64.org/cbmpet44u.png) | ||||
| 5 | $05 | white | 69 | $45 | ![E](https://sta.c64.org/cbmpet45u.png) | ![e](https://sta.c64.org/cbmpet45l.png) | 133 | $85 | F1 | 197 | $C5 | ![$C5](https://sta.c64.org/cbmpetc5.png) | ![E](https://sta.c64.org/cbmpet45u.png) | ||
| 6 | $06 | 70 | $46 | ![F](https://sta.c64.org/cbmpet46u.png) | ![f](https://sta.c64.org/cbmpet46l.png) | 134 | $86 | F3 | 198 | $C6 | ![$C6](https://sta.c64.org/cbmpetc6.png) | ![F](https://sta.c64.org/cbmpet46u.png) | |||
| 7 | $07 | 71 | $47 | ![G](https://sta.c64.org/cbmpet47u.png) | ![g](https://sta.c64.org/cbmpet47l.png) | 135 | $87 | F5 | 199 | $C7 | ![$C7](https://sta.c64.org/cbmpetc7.png) | ![G](https://sta.c64.org/cbmpet47u.png) | |||
| 8 | $08 | disable C=-Shift | 72 | $48 | ![H](https://sta.c64.org/cbmpet48u.png) | ![h](https://sta.c64.org/cbmpet48l.png) | 136 | $88 | F7 | 200 | $C8 | ![$C8](https://sta.c64.org/cbmpetc8.png) | ![H](https://sta.c64.org/cbmpet48u.png) | ||
| 9 | $09 | enable C=-Shift | 73 | $49 | ![I](https://sta.c64.org/cbmpet49u.png) | ![i](https://sta.c64.org/cbmpet49l.png) | 137 | $89 | F2 | 201 | $C9 | ![$C9](https://sta.c64.org/cbmpetc9.png) | ![I](https://sta.c64.org/cbmpet49u.png) | ||
| 10 | $0A | 74 | $4A | ![J](https://sta.c64.org/cbmpet4au.png) | ![j](https://sta.c64.org/cbmpet4al.png) | 138 | $8A | F4 | 202 | $CA | ![$CA](https://sta.c64.org/cbmpetca.png) | ![J](https://sta.c64.org/cbmpet4au.png) | |||
| 11 | $0B | 75 | $4B | ![K](https://sta.c64.org/cbmpet4bu.png) | ![k](https://sta.c64.org/cbmpet4bl.png) | 139 | $8B | F6 | 203 | $CB | ![$CB](https://sta.c64.org/cbmpetcb.png) | ![K](https://sta.c64.org/cbmpet4bu.png) | |||
| 12 | $0C | 76 | $4C | ![L](https://sta.c64.org/cbmpet4cu.png) | ![l](https://sta.c64.org/cbmpet4cl.png) | 140 | $8C | F8 | 204 | $CC | ![$CC](https://sta.c64.org/cbmpetcc.png) | ![L](https://sta.c64.org/cbmpet4cu.png) | |||
| 13 | $0D | Return | 77 | $4D | ![M](https://sta.c64.org/cbmpet4du.png) | ![m](https://sta.c64.org/cbmpet4dl.png) | 141 | $8D | Shift-Return | 205 | $CD | ![$CD](https://sta.c64.org/cbmpetcd.png) | ![M](https://sta.c64.org/cbmpet4du.png) | ||
| 14 | $0E | lo/up charset | 78 | $4E | ![N](https://sta.c64.org/cbmpet4eu.png) | ![n](https://sta.c64.org/cbmpet4el.png) | 142 | $8E | up/gfx charset | 206 | $CE | ![$CE](https://sta.c64.org/cbmpetce.png) | ![N](https://sta.c64.org/cbmpet4eu.png) | ||
| 15 | $0F | 79 | $4F | ![O](https://sta.c64.org/cbmpet4fu.png) | ![o](https://sta.c64.org/cbmpet4fl.png) | 143 | $8F | 207 | $CF | ![$CF](https://sta.c64.org/cbmpetcf.png) | ![O](https://sta.c64.org/cbmpet4fu.png) | ||||
| 16 | $10 | 80 | $50 | ![P](https://sta.c64.org/cbmpet50u.png) | ![p](https://sta.c64.org/cbmpet50l.png) | 144 | $90 | black | 208 | $D0 | ![$D0](https://sta.c64.org/cbmpetd0.png) | ![P](https://sta.c64.org/cbmpet50u.png) | |||
| 17 | $11 | cursor down | 81 | $51 | ![Q](https://sta.c64.org/cbmpet51u.png) | ![q](https://sta.c64.org/cbmpet51l.png) | 145 | $91 | cursor up | 209 | $D1 | ![$D1](https://sta.c64.org/cbmpetd1.png) | ![Q](https://sta.c64.org/cbmpet51u.png) | ||
| 18 | $12 | reverse on | 82 | $52 | ![R](https://sta.c64.org/cbmpet52u.png) | ![r](https://sta.c64.org/cbmpet52l.png) | 146 | $92 | reverse off | 210 | $D2 | ![$D2](https://sta.c64.org/cbmpetd2.png) | ![R](https://sta.c64.org/cbmpet52u.png) | ||
| 19 | $13 | Home | 83 | $53 | ![S](https://sta.c64.org/cbmpet53u.png) | ![s](https://sta.c64.org/cbmpet53l.png) | 147 | $93 | Clear | 211 | $D3 | ![$D3](https://sta.c64.org/cbmpetd3.png) | ![S](https://sta.c64.org/cbmpet53u.png) | ||
| 20 | $14 | Delete | 84 | $54 | ![T](https://sta.c64.org/cbmpet54u.png) | ![t](https://sta.c64.org/cbmpet54l.png) | 148 | $94 | Insert | 212 | $D4 | ![$D4](https://sta.c64.org/cbmpetd4.png) | ![T](https://sta.c64.org/cbmpet54u.png) | ||
| 21 | $15 | 85 | $55 | ![U](https://sta.c64.org/cbmpet55u.png) | ![u](https://sta.c64.org/cbmpet55l.png) | 149 | $95 | brown | 213 | $D5 | ![$D5](https://sta.c64.org/cbmpetd5.png) | ![U](https://sta.c64.org/cbmpet55u.png) | |||
| 22 | $16 | 86 | $56 | ![V](https://sta.c64.org/cbmpet56u.png) | ![v](https://sta.c64.org/cbmpet56l.png) | 150 | $96 | pink | 214 | $D6 | ![$D6](https://sta.c64.org/cbmpetd6.png) | ![V](https://sta.c64.org/cbmpet56u.png) | |||
| 23 | $17 | 87 | $57 | ![W](https://sta.c64.org/cbmpet57u.png) | ![w](https://sta.c64.org/cbmpet57l.png) | 151 | $97 | dark grey | 215 | $D7 | ![$D7](https://sta.c64.org/cbmpetd7.png) | ![W](https://sta.c64.org/cbmpet57u.png) | |||
| 24 | $18 | 88 | $58 | ![X](https://sta.c64.org/cbmpet58u.png) | ![x](https://sta.c64.org/cbmpet58l.png) | 152 | $98 | grey | 216 | $D8 | ![$D8](https://sta.c64.org/cbmpetd8.png) | ![X](https://sta.c64.org/cbmpet58u.png) | |||
| 25 | $19 | 89 | $59 | ![Y](https://sta.c64.org/cbmpet59u.png) | ![y](https://sta.c64.org/cbmpet59l.png) | 153 | $99 | light green | 217 | $D9 | ![$D9](https://sta.c64.org/cbmpetd9.png) | ![Y](https://sta.c64.org/cbmpet59u.png) | |||
| 26 | $1A | 90 | $5A | ![Z](https://sta.c64.org/cbmpet5au.png) | ![z](https://sta.c64.org/cbmpet5al.png) | 154 | $9A | light blue | 218 | $DA | ![$DA](https://sta.c64.org/cbmpetda.png) | ![Z](https://sta.c64.org/cbmpet5au.png) | |||
| 27 | $1B | 91 | $5B | ![[](https://sta.c64.org/cbmpet5b.png) | 155 | $9B | light grey | 219 | $DB | ![$DB](https://sta.c64.org/cbmpetdb.png) | |||||
| 28 | $1C | red | 92 | $5C | ![pound](https://sta.c64.org/cbmpet5c.png) | 156 | $9C | purple | 220 | $DC | ![$DC](https://sta.c64.org/cbmpetdc.png) | ||||
| 29 | $1D | cursor right | 93 | $5D | ![]](https://sta.c64.org/cbmpet5d.png) | 157 | $9D | cursor left | 221 | $DD | ![$DD](https://sta.c64.org/cbmpetdd.png) | ||||
| 30 | $1E | green | 94 | $5E | ![up arrow](https://sta.c64.org/cbmpet5e.png) | 158 | $9E | yellow | 222 | $DE | ![$DE](https://sta.c64.org/cbmpetdeu.png) | ![$DE](https://sta.c64.org/cbmpetdel.png) | |||
| 31 | $1F | blue | 95 | $5F | ![left arrow](https://sta.c64.org/cbmpet5f.png) | 159 | $9F | cyan | 223 | $DF | ![$DF](https://sta.c64.org/cbmpetdfu.png) | ![$DF](https://sta.c64.org/cbmpetdfl.png) | |||
| 32 | $20 | ![Space](https://sta.c64.org/cbmpet20.png) | 96 | $60 | ![$C0](https://sta.c64.org/cbmpetc0.png) | 160 | $A0 | ![Shift-Space](https://sta.c64.org/cbmpeta0.png) | 224 | $E0 | ![$A0](https://sta.c64.org/cbmpeta0.png) | ||||
| 33 | $21 | ![!](https://sta.c64.org/cbmpet21.png) | 97 | $61 | ![$C1](https://sta.c64.org/cbmpetc1.png) | ![$41](https://sta.c64.org/cbmpet41u.png) | 161 | $A1 | ![$A1](https://sta.c64.org/cbmpeta1.png) | 225 | $E1 | ![$A1](https://sta.c64.org/cbmpeta1.png) | |||
| 34 | $22 | !["](https://sta.c64.org/cbmpet22.png) | 98 | $62 | ![$C2](https://sta.c64.org/cbmpetc2.png) | ![$42](https://sta.c64.org/cbmpet42u.png) | 162 | $A2 | ![$A2](https://sta.c64.org/cbmpeta2.png) | 226 | $E2 | ![$A2](https://sta.c64.org/cbmpeta2.png) | |||
| 35 | $23 | ![#](https://sta.c64.org/cbmpet23.png) | 99 | $63 | ![$C3](https://sta.c64.org/cbmpetc3.png) | ![$43](https://sta.c64.org/cbmpet43u.png) | 163 | $A3 | ![$A3](https://sta.c64.org/cbmpeta3.png) | 227 | $E3 | ![$A3](https://sta.c64.org/cbmpeta3.png) | |||
| 36 | $24 | ![$](https://sta.c64.org/cbmpet24.png) | 100 | $64 | ![$C4](https://sta.c64.org/cbmpetc4.png) | ![$44](https://sta.c64.org/cbmpet44u.png) | 164 | $A4 | ![$A4](https://sta.c64.org/cbmpeta4.png) | 228 | $E4 | ![$A4](https://sta.c64.org/cbmpeta4.png) | |||
| 37 | $25 | ![%](https://sta.c64.org/cbmpet25.png) | 101 | $65 | ![$C5](https://sta.c64.org/cbmpetc5.png) | ![$45](https://sta.c64.org/cbmpet45u.png) | 165 | $A5 | ![$A5](https://sta.c64.org/cbmpeta5.png) | 229 | $E5 | ![$A5](https://sta.c64.org/cbmpeta5.png) | |||
| 38 | $26 | ![&](https://sta.c64.org/cbmpet26.png) | 102 | $66 | ![$C6](https://sta.c64.org/cbmpetc6.png) | ![$46](https://sta.c64.org/cbmpet46u.png) | 166 | $A6 | ![$A6](https://sta.c64.org/cbmpeta6.png) | 230 | $E6 | ![$A6](https://sta.c64.org/cbmpeta6.png) | |||
| 39 | $27 | !['](https://sta.c64.org/cbmpet27.png) | 103 | $67 | ![$C7](https://sta.c64.org/cbmpetc7.png) | ![$47](https://sta.c64.org/cbmpet47u.png) | 167 | $A7 | ![$A7](https://sta.c64.org/cbmpeta7.png) | 231 | $E7 | ![$A7](https://sta.c64.org/cbmpeta7.png) | |||
| 40 | $28 | ![(](https://sta.c64.org/cbmpet28.png) | 104 | $68 | ![$C8](https://sta.c64.org/cbmpetc8.png) | ![$48](https://sta.c64.org/cbmpet48u.png) | 168 | $A8 | ![$A8](https://sta.c64.org/cbmpeta8.png) | 232 | $E8 | ![$A8](https://sta.c64.org/cbmpeta8.png) | |||
| 41 | $29 | ![)](https://sta.c64.org/cbmpet29.png) | 105 | $69 | ![$C9](https://sta.c64.org/cbmpetc9.png) | ![$49](https://sta.c64.org/cbmpet49u.png) | 169 | $A9 | ![$A9](https://sta.c64.org/cbmpeta9u.png) | ![$A9](https://sta.c64.org/cbmpeta9l.png) | 233 | $E9 | ![$A9](https://sta.c64.org/cbmpeta9u.png) | ![$A9](https://sta.c64.org/cbmpeta9l.png) | |
| 42 | $2A | ![*](https://sta.c64.org/cbmpet2a.png) | 106 | $6A | ![$CA](https://sta.c64.org/cbmpetca.png) | ![$4A](https://sta.c64.org/cbmpet4au.png) | 170 | $AA | ![$AA](https://sta.c64.org/cbmpetaa.png) | 234 | $EA | ![$AA](https://sta.c64.org/cbmpetaa.png) | |||
| 43 | $2B | ![+](https://sta.c64.org/cbmpet2b.png) | 107 | $6B | ![$CB](https://sta.c64.org/cbmpetcb.png) | ![$4B](https://sta.c64.org/cbmpet4bu.png) | 171 | $AB | ![$AB](https://sta.c64.org/cbmpetab.png) | 235 | $EB | ![$AB](https://sta.c64.org/cbmpetab.png) | |||
| 44 | $2C | ![,](https://sta.c64.org/cbmpet2c.png) | 108 | $6C | ![$CC](https://sta.c64.org/cbmpetcc.png) | ![$4C](https://sta.c64.org/cbmpet4cu.png) | 172 | $AC | ![$AC](https://sta.c64.org/cbmpetac.png) | 236 | $EC | ![$AC](https://sta.c64.org/cbmpetac.png) | |||
| 45 | $2D | ![-](https://sta.c64.org/cbmpet2d.png) | 109 | $6D | ![$CD](https://sta.c64.org/cbmpetcd.png) | ![$4D](https://sta.c64.org/cbmpet4du.png) | 173 | $AD | ![$AD](https://sta.c64.org/cbmpetad.png) | 237 | $ED | ![$AD](https://sta.c64.org/cbmpetad.png) | |||
| 46 | $2E | ![.](https://sta.c64.org/cbmpet2e.png) | 110 | $6E | ![$CE](https://sta.c64.org/cbmpetce.png) | ![$4E](https://sta.c64.org/cbmpet4eu.png) | 174 | $AE | ![$AE](https://sta.c64.org/cbmpetae.png) | 238 | $EE | ![$AE](https://sta.c64.org/cbmpetae.png) | |||
| 47 | $2F | ![/](https://sta.c64.org/cbmpet2f.png) | 111 | $6F | ![$CF](https://sta.c64.org/cbmpetcf.png) | ![$4F](https://sta.c64.org/cbmpet4fu.png) | 175 | $AF | ![$AF](https://sta.c64.org/cbmpetaf.png) | 239 | $EF | ![$AF](https://sta.c64.org/cbmpetaf.png) | |||
| 48 | $30 | ![0](https://sta.c64.org/cbmpet30.png) | 112 | $70 | ![$D0](https://sta.c64.org/cbmpetd0.png) | ![$50](https://sta.c64.org/cbmpet50u.png) | 176 | $B0 | ![$B0](https://sta.c64.org/cbmpetb0.png) | 240 | $F0 | ![$B0](https://sta.c64.org/cbmpetb0.png) | |||
| 49 | $31 | ![1](https://sta.c64.org/cbmpet31.png) | 113 | $71 | ![$D1](https://sta.c64.org/cbmpetd1.png) | ![$51](https://sta.c64.org/cbmpet51u.png) | 177 | $B1 | ![$B1](https://sta.c64.org/cbmpetb1.png) | 241 | $F1 | ![$B1](https://sta.c64.org/cbmpetb1.png) | |||
| 50 | $32 | ![2](https://sta.c64.org/cbmpet32.png) | 114 | $72 | ![$D2](https://sta.c64.org/cbmpetd2.png) | ![$52](https://sta.c64.org/cbmpet52u.png) | 178 | $B2 | ![$B2](https://sta.c64.org/cbmpetb2.png) | 242 | $F2 | ![$B2](https://sta.c64.org/cbmpetb2.png) | |||
| 51 | $33 | ![3](https://sta.c64.org/cbmpet33.png) | 115 | $73 | ![$D3](https://sta.c64.org/cbmpetd3.png) | ![$53](https://sta.c64.org/cbmpet53u.png) | 179 | $B3 | ![$B3](https://sta.c64.org/cbmpetb3.png) | 243 | $F3 | ![$B3](https://sta.c64.org/cbmpetb3.png) | |||
| 52 | $34 | ![4](https://sta.c64.org/cbmpet34.png) | 116 | $74 | ![$D4](https://sta.c64.org/cbmpetd4.png) | ![$54](https://sta.c64.org/cbmpet54u.png) | 180 | $B4 | ![$B4](https://sta.c64.org/cbmpetb4.png) | 244 | $F4 | ![$B4](https://sta.c64.org/cbmpetb4.png) | |||
| 53 | $35 | ![5](https://sta.c64.org/cbmpet35.png) | 117 | $75 | ![$D5](https://sta.c64.org/cbmpetd5.png) | ![$55](https://sta.c64.org/cbmpet55u.png) | 181 | $B5 | ![$B5](https://sta.c64.org/cbmpetb5.png) | 245 | $F5 | ![$B5](https://sta.c64.org/cbmpetb5.png) | |||
| 54 | $36 | ![6](https://sta.c64.org/cbmpet36.png) | 118 | $76 | ![$D6](https://sta.c64.org/cbmpetd6.png) | ![$56](https://sta.c64.org/cbmpet56u.png) | 182 | $B6 | ![$B6](https://sta.c64.org/cbmpetb6.png) | 246 | $F6 | ![$B6](https://sta.c64.org/cbmpetb6.png) | |||
| 55 | $37 | ![7](https://sta.c64.org/cbmpet37.png) | 119 | $77 | ![$D7](https://sta.c64.org/cbmpetd7.png) | ![$57](https://sta.c64.org/cbmpet57u.png) | 183 | $B7 | ![$B7](https://sta.c64.org/cbmpetb7.png) | 247 | $F7 | ![$B7](https://sta.c64.org/cbmpetb7.png) | |||
| 56 | $38 | ![8](https://sta.c64.org/cbmpet38.png) | 120 | $78 | ![$D8](https://sta.c64.org/cbmpetd8.png) | ![$58](https://sta.c64.org/cbmpet58u.png) | 184 | $B8 | ![$B8](https://sta.c64.org/cbmpetb8.png) | 248 | $F8 | ![$B8](https://sta.c64.org/cbmpetb8.png) | |||
| 57 | $39 | ![9](https://sta.c64.org/cbmpet39.png) | 121 | $79 | ![$D9](https://sta.c64.org/cbmpetd9.png) | ![$59](https://sta.c64.org/cbmpet59u.png) | 185 | $B9 | ![$B9](https://sta.c64.org/cbmpetb9.png) | 249 | $F9 | ![$B9](https://sta.c64.org/cbmpetb9.png) | |||
| 58 | $3A | ![:](https://sta.c64.org/cbmpet3a.png) | 122 | $7A | ![$DA](https://sta.c64.org/cbmpetda.png) | ![$5A](https://sta.c64.org/cbmpet5au.png) | 186 | $BA | ![$BA](https://sta.c64.org/cbmpetbau.png) | ![$BA](https://sta.c64.org/cbmpetbal.png) | 250 | $FA | ![$BA](https://sta.c64.org/cbmpetbau.png) | ![$BA](https://sta.c64.org/cbmpetbal.png) | |
| 59 | $3B | ![;](https://sta.c64.org/cbmpet3b.png) | 123 | $7B | ![$DB](https://sta.c64.org/cbmpetdb.png) | 187 | $BB | ![$BB](https://sta.c64.org/cbmpetbb.png) | 251 | $FB | ![$BB](https://sta.c64.org/cbmpetbb.png) | ||||
| 60 | $3C | ![<](https://sta.c64.org/cbmpet3c.png) | 124 | $7C | ![$DC](https://sta.c64.org/cbmpetdc.png) | 188 | $BC | ![$BC](https://sta.c64.org/cbmpetbc.png) | 252 | $FC | ![$BC](https://sta.c64.org/cbmpetbc.png) | ||||
| 61 | $3D | ![=](https://sta.c64.org/cbmpet3d.png) | 125 | $7D | ![$DD](https://sta.c64.org/cbmpetdd.png) | 189 | $BD | ![$BD](https://sta.c64.org/cbmpetbd.png) | 253 | $FD | ![$BD](https://sta.c64.org/cbmpetbd.png) | ||||
| 62 | $3E | ![>](https://sta.c64.org/cbmpet3e.png) | 126 | $7E | ![$DE](https://sta.c64.org/cbmpetdeu.png) | ![$DE](https://sta.c64.org/cbmpetdel.png) | 190 | $BE | ![$BE](https://sta.c64.org/cbmpetbe.png) | 254 | $FE | ![$BE](https://sta.c64.org/cbmpetbe.png) | |||
| 63 | $3F | ![?](https://sta.c64.org/cbmpet3f.png) | 127 | $7F | ![$DF](https://sta.c64.org/cbmpetdfu.png) | ![$DF](https://sta.c64.org/cbmpetdfl.png) | 191 | $BF | ![$BF](https://sta.c64.org/cbmpetbf.png) | 255 | $FF | ![$DE](https://sta.c64.org/cbmpetdeu.png) | ![$DE](https://sta.c64.org/cbmpetdel.png) | ||

Notes:

- Codes $00-$1F and $80-$9F are control codes. Printing them will cause a change in screen layout or behavior, not an actual character displayed. 
- Codes $60-$7F and $E0-$FE are not used. Although you can print them, these are, actually, copies of codes $C0-$DF and $A0-$BE. 
- Code $FF is the BASIC token of the π (pi) symbol. It is converted internally to code $DE when printed and, vice versa, code $DE is converted to $FF when fetched from the screen. However, when reading the keyboard buffer, you will find code $DE for Shift-↑ (up arrow) as no conversion takes place there yet.

---
*Fonte originale: [https://sta.c64.org/cbm64pet_orig.html](https://sta.c64.org/cbm64pet_orig.html)*
