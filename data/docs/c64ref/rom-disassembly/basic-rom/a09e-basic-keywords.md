---
title: BASIC keywords
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a09e-basic-befehlsworte
- a198-other-commands
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A09E
  address_end: $A19D
  symbol: basic-keywords
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A09E**: end'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A09E**: end'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A09E**: end'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A09E**: end'
---

# $A09E — BASIC keywords

## Disassemblatura
```assembly
.A09E  45 4E   ; end
.A0A0  C4 46 4F D2 4E 45 58 D4   ; for next
.A0A8  44 41 54 C1 49 4E 50 55   ; data input#
.A0B0  54 A3 49 4E 50 55 D4 44   ; input dim
.A0B8  49 CD 52 45 41 C4 4C 45   ; read let
.A0C0  D4 47 4F 54 CF 52 55 CE   ; goto run
.A0C8  49 C6 52 45 53 54 4F 52   ; if restore
.A0D0  C5 47 4F 53 55 C2 52 45   ; gosub return
.A0D8  54 55 52 CE 52 45 CD 53   ; rem stop
.A0E0  54 4F D0 4F CE 57 41 49   ; on wait
.A0E8  D4 4C 4F 41 C4 53 41 56   ; load save
.A0F0  C5 56 45 52 49 46 D9 44   ; verify def
.A0F8  45 C6 50 4F 4B C5 50 52   ; poke print#
.A100  49 4E 54 A3 50 52 49 4E   ; print
.A108  D4 43 4F 4E D4 4C 49 53   ; cont list
.A110  D4 43 4C D2 43 4D C4 53   ; clr cmd sys
.A118  59 D3 4F 50 45 CE 43 4C   ; open close
.A120  4F 53 C5 47 45 D4 4E 45   ; get new next are the secondary command keywords, these can not start a statement
.A128  D7 54 41 42 A8 54 CF 46   ; tab( to
.A130  CE 53 50 43 A8 54 48 45   ; spc( then
.A138  CE 4E 4F D4 53 54 45 D0   ; not step next are the operators
.A140  AB AD AA AF DE 41 4E C4   ; + - * / ' and
.A148  4F D2 BE BD BC   ; or <=>
.A14D  53 47 CE   ; sgn and finally the functions
.A150  49 4E D4 41 42 D3 55 53   ; int abs usr
.A158  D2 46 52 C5 50 4F D3 53   ; fre pos sqr
.A160  51 D2 52 4E C4 4C 4F C7   ; rnd log
.A168  45 58 D0 43 4F D3 53 49   ; exp cos sin
.A170  CE 54 41 CE 41 54 CE 50   ; tan atn peek
.A178  45 45 CB 4C 45 CE 53 54   ; len str$
.A180  52 A4 56 41 CC 41 53 C3   ; val asc
.A188  43 48 52 A4 4C 45 46 54   ; chr$ left$
.A190  A4 52 49 47 48 54 A4 4D   ; right$ mid$ lastly is GO, this is an add on so that GO TO, as well as GOTO, will work
.A198  49 44 A4 47 CF   ; go
.A19D  00   ; end marker
```


## Commenti

### Original Disassembly (—)
- **$A09E**: end
- **$A0A0**: for next
- **$A0A8**: data input#
- **$A0B0**: input dim
- **$A0B8**: read let
- **$A0C0**: goto run
- **$A0C8**: if restore
- **$A0D0**: gosub return
- **$A0D8**: rem stop
- **$A0E0**: on wait
- **$A0E8**: load save
- **$A0F0**: verify def
- **$A0F8**: poke print#
- **$A100**: print
- **$A108**: cont list
- **$A110**: clr cmd sys
- **$A118**: open close
- **$A120**: get new next are the secondary command keywords, these can not start a statement
- **$A128**: tab( to
- **$A130**: spc( then
- **$A138**: not step next are the operators
- **$A140**: + - * / ' and
- **$A148**: or <=>
- **$A14D**: sgn and finally the functions
- **$A150**: int abs usr
- **$A158**: fre pos sqr
- **$A160**: rnd log
- **$A168**: exp cos sin
- **$A170**: tan atn peek
- **$A178**: len str$
- **$A180**: val asc
- **$A188**: chr$ left$
- **$A190**: right$ mid$ lastly is GO, this is an add on so that GO TO, as well as GOTO, will work
- **$A198**: go
- **$A19D**: end marker

### Commodore-64-intern-Buch (Commodore)
- **$A09E**: end
- **$A0A0**: for next
- **$A0A8**: data input#
- **$A0B0**: input dim
- **$A0B8**: read let
- **$A0C0**: goto run
- **$A0C8**: if restore
- **$A0D0**: gosub return
- **$A0D8**: rem stop
- **$A0E0**: on wait
- **$A0E8**: load save
- **$A0F0**: verify def
- **$A0F8**: poke print#
- **$A100**: print
- **$A108**: cont list
- **$A110**: clr cmd sys
- **$A118**: open close
- **$A120**: get new
- **$A128**: tab( to
- **$A130**: spc( then
- **$A138**: not step
- **$A140**: + - * / ' and
- **$A148**: or <=> sgn
- **$A150**: int abs usr
- **$A158**: fre pos sqr
- **$A160**: rnd log
- **$A168**: exp cos sin
- **$A170**: tan atn peek
- **$A178**: len str$
- **$A180**: val asc
- **$A188**: chr$ left$
- **$A190**: right$ mid$
- **$A198**: go

### Marko Mäkelä (Marko Mäkelä)
- **$A09E**: end
- **$A0A1**: for
- **$A0A4**: next
- **$A0A8**: data
- **$A0AC**: input#
- **$A0B2**: input
- **$A0B7**: dim
- **$A0BA**: read
- **$A0BE**: let
- **$A0C1**: goto
- **$A0C5**: run
- **$A0C8**: if
- **$A0CA**: restore
- **$A0D1**: gosub
- **$A0D6**: return
- **$A0DC**: rem
- **$A0DF**: stop
- **$A0E3**: on
- **$A0E5**: wait
- **$A0E9**: load
- **$A0ED**: save
- **$A0F1**: verify
- **$A0F7**: def
- **$A0FA**: poke
- **$A0FE**: print#
- **$A104**: print
- **$A109**: cont
- **$A10D**: list
- **$A111**: clr
- **$A114**: cmd
- **$A117**: sys
- **$A11A**: open
- **$A11E**: close
- **$A123**: get
- **$A126**: new

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A09E**: end
- **$A0A0**: for next
- **$A0A8**: data input#
- **$A0B0**: input dim
- **$A0B8**: read let
- **$A0C0**: goto run
- **$A0C8**: if restore
- **$A0D0**: gosub return
- **$A0D8**: rem stop
- **$A0E0**: on wait
- **$A0E8**: load save
- **$A0F0**: verify def
- **$A0F8**: poke print#
- **$A100**: print
- **$A108**: cont list
- **$A110**: clr cmd sys
- **$A118**: open close
- **$A120**: get new
- **$A128**: tab( to
- **$A130**: spc( then
- **$A138**: not step
- **$A140**: + - * / ' and
- **$A148**: or <=>
- **$A14D**: sgn
- **$A150**: int abs usr
- **$A158**: fre pos sqr
- **$A160**: rnd log
- **$A168**: exp cos sin
- **$A170**: tan atn peek
- **$A178**: len str$
- **$A180**: val asc
- **$A188**: chr$ left$
- **$A190**: right$ mid$
- **$A198**: go
- **$A19D**: END OF TOKEN NAME TABLE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*