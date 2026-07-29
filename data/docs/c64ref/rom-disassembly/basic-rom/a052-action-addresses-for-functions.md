---
title: action addresses for functions
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a052-adressen-der-basic-funktionen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A052
  address_end: $A07E
  symbol: action-addresses-for-functions
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A052**: perform SGN     $B4'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A052**: $B4 $BC39 SGN'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A052**: sgn'
---

# $A052 — action addresses for functions

## Disassemblatura
```assembly
.A052  39 BC   ; perform SGN     $B4
.A054  CC BC   ; perform INT     $B5
.A056  58 BC   ; perform ABS     $B6
.A058  10 03   ; perform USR     $B7
.A05A  7D B3   ; perform FRE     $B8
.A05C  9E B3   ; perform POS     $B9
.A05E  71 BF   ; perform SQR     $BA
.A060  97 E0   ; perform RND     $BB
.A062  EA B9   ; perform LOG     $BC
.A064  ED BF   ; perform EXP     $BD
.A066  64 E2   ; perform COS     $BE
.A068  6B E2   ; perform SIN     $BF
.A06A  B4 E2   ; perform TAN     $C0
.A06C  0E E3   ; perform ATN     $C1
.A06E  0D B8   ; perform PEEK    $C2
.A070  7C B7   ; perform LEN     $C3
.A072  65 B4   ; perform STR$    $C4
.A074  AD B7   ; perform VAL     $C5
.A076  8B B7   ; perform ASC     $C6
.A078  EC B6   ; perform CHR$    $C7
.A07A  00 B7   ; perform LEFT$   $C8
.A07C  2C B7   ; perform RIGHT$  $C9
.A07E  37 B7   ; perform MID$    $CA
```


## Commenti

### Original Disassembly (—)
- **$A052**: perform SGN     $B4
- **$A054**: perform INT     $B5
- **$A056**: perform ABS     $B6
- **$A058**: perform USR     $B7
- **$A05A**: perform FRE     $B8
- **$A05C**: perform POS     $B9
- **$A05E**: perform SQR     $BA
- **$A060**: perform RND     $BB
- **$A062**: perform LOG     $BC
- **$A064**: perform EXP     $BD
- **$A066**: perform COS     $BE
- **$A068**: perform SIN     $BF
- **$A06A**: perform TAN     $C0
- **$A06C**: perform ATN     $C1
- **$A06E**: perform PEEK    $C2
- **$A070**: perform LEN     $C3
- **$A072**: perform STR$    $C4
- **$A074**: perform VAL     $C5
- **$A076**: perform ASC     $C6
- **$A078**: perform CHR$    $C7
- **$A07A**: perform LEFT$   $C8
- **$A07C**: perform RIGHT$  $C9
- **$A07E**: perform MID$    $CA

### Commodore-64-intern-Buch (Commodore)
- **$A052**: $B4 $BC39 SGN
- **$A054**: $B5 $BCCC INT
- **$A056**: $B6 $BC58 ABS
- **$A058**: $B7 $0310 USR
- **$A05A**: $B8 $B37D FRE
- **$A05C**: $B9 $B39E POS
- **$A05E**: $BA $BF71 SQR
- **$A060**: $BB $E097 RND
- **$A062**: $BC $B9EA LOG
- **$A064**: $BD $BFED EXP
- **$A066**: $BE $E264 COS
- **$A068**: $BF $E26B SIN
- **$A06A**: $C0 $E2B4 TAN
- **$A06C**: $C1 $E30E ATN
- **$A06E**: $C2 $B80D PEEK
- **$A070**: $C3 $B77C LEN
- **$A072**: $C4 $B465 STR$
- **$A074**: $C5 $B7AD VAL
- **$A076**: $C6 $B78B ASC
- **$A078**: $C7 $B6EC CHR$
- **$A07A**: $C8 $B700 LEFT$
- **$A07C**: $C9 $B72C RIGHT$
- **$A07E**: $CA $B737 MID$

### Marko Mäkelä (Marko Mäkelä)
- **$A052**: sgn
- **$A054**: int
- **$A056**: abs
- **$A058**: usr
- **$A05A**: fre
- **$A05C**: pos
- **$A05E**: sqr
- **$A060**: rnd
- **$A062**: log
- **$A064**: exp
- **$A066**: cos
- **$A068**: sin
- **$A06A**: tan
- **$A06C**: atn
- **$A06E**: peek
- **$A070**: len
- **$A072**: str$
- **$A074**: val
- **$A076**: asc
- **$A078**: chr$
- **$A07A**: left$
- **$A07C**: right$
- **$A07E**: mid$

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*