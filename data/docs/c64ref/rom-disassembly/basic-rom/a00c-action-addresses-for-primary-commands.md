---
title: action addresses for primary commands
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
- 00d7-data
- a00c-interpreterkode-adresse-befehl
- ab45-print
- close
- ece7-load
- ecec-run
- f34a-open
- f5ed-save
- input
- return
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A00C
  address_end: $A050
  symbol: action-addresses-for-primary-commands
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A00C**: perform END     $80'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A00C**: $80 $A831 END'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A00C**: end'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A00C**: $80 $A831 END'
---

# $A00C — action addresses for primary commands

## Disassemblatura
```assembly
.A00C  30 A8   ; perform END     $80
.A00E  41 A7   ; perform FOR     $81
.A010  1D AD   ; perform NEXT    $82
.A012  F7 A8   ; perform DATA    $83
.A014  A4 AB   ; perform INPUT#  $84
.A016  BE AB   ; perform INPUT   $85
.A018  80 B0   ; perform DIM     $86
.A01A  05 AC   ; perform READ    $87
.A01C  A4 A9   ; perform LET     $88
.A01E  9F A8   ; perform GOTO    $89
.A020  70 A8   ; perform RUN     $8A
.A022  27 A9   ; perform IF      $8B
.A024  1C A8   ; perform RESTORE $8C
.A026  82 A8   ; perform GOSUB   $8D
.A028  D1 A8   ; perform RETURN  $8E
.A02A  3A A9   ; perform REM     $8F
.A02C  2E A8   ; perform STOP    $90
.A02E  4A A9   ; perform ON      $91
.A030  2C B8   ; perform WAIT    $92
.A032  67 E1   ; perform LOAD    $93
.A034  55 E1   ; perform SAVE    $94
.A036  64 E1   ; perform VERIFY  $95
.A038  B2 B3   ; perform DEF     $96
.A03A  23 B8   ; perform POKE    $97
.A03C  7F AA   ; perform PRINT#  $98
.A03E  9F AA   ; perform PRINT   $99
.A040  56 A8   ; perform CONT    $9A
.A042  9B A6   ; perform LIST    $9B
.A044  5D A6   ; perform CLR     $9C
.A046  85 AA   ; perform CMD     $9D
.A048  29 E1   ; perform SYS     $9E
.A04A  BD E1   ; perform OPEN    $9F
.A04C  C6 E1   ; perform CLOSE   $A0
.A04E  7A AB   ; perform GET     $A1
.A050  41 A6   ; perform NEW     $A2
```


## Commenti

### Original Disassembly (—)
- **$A00C**: perform END     $80
- **$A00E**: perform FOR     $81
- **$A010**: perform NEXT    $82
- **$A012**: perform DATA    $83
- **$A014**: perform INPUT#  $84
- **$A016**: perform INPUT   $85
- **$A018**: perform DIM     $86
- **$A01A**: perform READ    $87
- **$A01C**: perform LET     $88
- **$A01E**: perform GOTO    $89
- **$A020**: perform RUN     $8A
- **$A022**: perform IF      $8B
- **$A024**: perform RESTORE $8C
- **$A026**: perform GOSUB   $8D
- **$A028**: perform RETURN  $8E
- **$A02A**: perform REM     $8F
- **$A02C**: perform STOP    $90
- **$A02E**: perform ON      $91
- **$A030**: perform WAIT    $92
- **$A032**: perform LOAD    $93
- **$A034**: perform SAVE    $94
- **$A036**: perform VERIFY  $95
- **$A038**: perform DEF     $96
- **$A03A**: perform POKE    $97
- **$A03C**: perform PRINT#  $98
- **$A03E**: perform PRINT   $99
- **$A040**: perform CONT    $9A
- **$A042**: perform LIST    $9B
- **$A044**: perform CLR     $9C
- **$A046**: perform CMD     $9D
- **$A048**: perform SYS     $9E
- **$A04A**: perform OPEN    $9F
- **$A04C**: perform CLOSE   $A0
- **$A04E**: perform GET     $A1
- **$A050**: perform NEW     $A2

### Commodore-64-intern-Buch (Commodore)
- **$A00C**: $80 $A831 END
- **$A00E**: $81 $A742 FOR
- **$A010**: $82 $AD1E NEXT
- **$A012**: $83 $A8F8 DATA
- **$A014**: $84 $ABA5 INPUT#
- **$A016**: $85 $ABBF INPUT
- **$A018**: $86 $B081 DIM
- **$A01A**: $87 $AC06 READ
- **$A01C**: $88 $A9A5 LET
- **$A01E**: $89 $A8A0 GOTO
- **$A020**: $8A $A871 RUN
- **$A022**: $8B $A928 IF
- **$A024**: $8C $A81D RESTORE
- **$A026**: $8D $A883 GOSUB
- **$A028**: $8E $A8D2 RETURN
- **$A02A**: $8F $A93B REM
- **$A02C**: $90 $A82F STOP
- **$A02E**: $91 $A94B ON
- **$A030**: $92 $B82D WAIT
- **$A032**: $93 $E168 LOAD
- **$A034**: $94 $E156 SAVE
- **$A036**: $95 $E165 VERIFY
- **$A038**: $96 $B3B3 DEF
- **$A03A**: $97 $B824 POKE
- **$A03C**: $98 $AA80 PRINT#
- **$A03E**: $99 $AAA0 PRINT
- **$A040**: $9A $A857 CONT
- **$A042**: $9B $A69C LIST
- **$A044**: $9C $A65E CLR
- **$A046**: $9D $AA86 CMD
- **$A048**: $9E $E12A SYS
- **$A04A**: $9F $E1BE OPEN
- **$A04C**: $A0 $E1C7 CLOSE
- **$A04E**: $A1 $AB7B GET
- **$A050**: $A2 $A642 NEW

### Marko Mäkelä (Marko Mäkelä)
- **$A00C**: end
- **$A00E**: for
- **$A010**: next
- **$A012**: data
- **$A014**: input#
- **$A016**: input
- **$A018**: dim
- **$A01A**: read
- **$A01C**: let
- **$A01E**: goto
- **$A020**: run
- **$A022**: if
- **$A024**: restore
- **$A026**: gosub
- **$A028**: return
- **$A02A**: rem
- **$A02C**: stop
- **$A02E**: on
- **$A030**: wait
- **$A032**: load
- **$A034**: save
- **$A036**: verify
- **$A038**: def
- **$A03A**: poke
- **$A03C**: print#
- **$A03E**: print
- **$A040**: cont
- **$A042**: list
- **$A044**: clr
- **$A046**: cmd
- **$A048**: sys
- **$A04A**: open
- **$A04C**: close
- **$A04E**: get
- **$A050**: new

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A00C**: $80 $A831 END
- **$A00E**: $81 $A742 FOR
- **$A010**: $82 $AD1E NEXT
- **$A012**: $83 $A8F8 DATA
- **$A014**: $84 $ABA5 INPUT#
- **$A016**: $85 $ABBF INPUT
- **$A018**: $86 $B081 DIM
- **$A01A**: $87 $AC06 READ
- **$A01C**: $88 $A9A5 LET
- **$A01E**: $89 $A8A0 GOTO
- **$A020**: $8A $A871 RUN
- **$A022**: $8B $A928 IF
- **$A024**: $8C $A81D RESTORE
- **$A026**: $8D $A883 GOSUB
- **$A028**: $8E $A8D2 RETURN
- **$A02A**: $8F $A93B REM
- **$A02C**: $90 $A82F STOP
- **$A02E**: $91 $A94B ON
- **$A030**: $92 $B82D WAIT
- **$A032**: $93 $E168 LOAD
- **$A034**: $94 $E156 SAVE
- **$A036**: $95 $E165 VERIFY
- **$A038**: $96 $B3B3 DEF
- **$A03A**: $97 $B824 POKE
- **$A03C**: $98 $AA80 PRINT#
- **$A03E**: $99 $AAA0 PRINT
- **$A040**: $9A $A857 CONT
- **$A042**: $9B $A69C LIST
- **$A044**: $9C $A65E CLR
- **$A046**: $9D $AA86 CMD
- **$A048**: $9E $E12A SYS
- **$A04A**: $9F $E1BE OPEN
- **$A04C**: $A0 $E1C7 CLOSE
- **$A04E**: $A1 $AB7B GET
- **$A050**: $A2 $A642 NEW
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

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*