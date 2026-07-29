---
title: altime clock
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/commodore_128_intern.txt
category: reference
topics:
- kernal-api
- system-routines
- jumps
difficulty: intermediate
language: assembly
hardware:
- C64
related:
- jsr
- lda
- ldx
- ldy
- rdtim
- settim
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - commodore_128_intern.txt
  - cracking_the_kernal.txt
  - mapping_the_commodore_64.txt
  - kernal_64_/_128.txt
  - machine_language_routines.txt
  - c64_kernal_jump_table.txt
  - c64_programmer's_reference_guide.txt
  - commented_rom_disassembly.txt
  - das_neue_commodore-64-intern-buch.txt
  - standard_kernal_functions.txt
  - compute!'s_tool_kit:_kernal.txt
  address: $FFDB
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A, X, Y'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: A/X/Y = New TOD value.
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: stem clock is maintained by an interrupt routine that updates the
      clock
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: 'is the opposite of RDTIM: it SETs the system clock instead of ReaDing
      it.'
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JMP at AA1A/CA1A in BASIC''s TI$.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': A=MSB, X=middle, Y=LSB             A X Y  - - -  - - -'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : .AXY - Clock value in jiffies (1/60 secs).'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: die laufende Zeit neu
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: outine performs the reverse operation from RDTIM, storing the value
      in the
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine sets the value in the software jiffy dock. The
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: utine setzt die Systemuhr TI, die ab
---

# $FFDB — altime clock ($FFDB)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFDB`
- **Chiamata**: `JSR None` o `SYS 65499`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: None

scription**: A system clock is maintained by an interrupt routine that
s the clock every 1/60th of a second (one "jiffy"). The clock is
bytes long, which gives it the capability to count up to 5,184,000
s (24 hours). At that point the clock resets to zero. Before
g this routine to set the clock, the accumulator must contain the
ignificant byte, the X index register the next most significant
and the Y index register the least significant byte of the initial
etting (in jiffies).

 to Use:
d the accumulator with the MSB of the 3-byte number to set the
ck.
d the X register with the next byte.
d the Y register with the LSB.
l this routine.

MPLE:
ET THE CLOCK TO 10 MINUTES = 3600 JIFFIES
   LDA #0               ;MOST SIGNIFICANT
   LDX #>3600
   LDY #<3600           ;LEAST SIGNIFICANT
   JSR SETTIM

### Standard KERNAL Functions (Joe Forster / STA)
A/X/Y = New TOD value.
: –
egisters: –
ddress: $F6E4.

### Commented ROM Disassembly (Lee Davison)
stem clock is maintained by an interrupt routine that updates the clock
1/60th of a second. The clock is three bytes long which gives the capability
nt from zero up to 5,184,000 jiffies - 24 hours plus one jiffy. At that point
ock resets to zero. Before calling this routine to set the clock the new time,
fies, should be in YXA, the accumulator containing the most significant byte.

### Cracking The Kernal (Peter Marcotty)
is the opposite of RDTIM: it SETs the system clock instead of ReaDing it.

et system clock to 10 minutes =3600 jiffies.
   LDA #0
   LDX #L,3600
   LDY #H,3600
   JSR SETTIM
his allows very accurate timing for many things.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP at AA1A/CA1A in BASIC's TI$.

y requirements**:
cumulator should hold the high byte to be stored in the
clock. The X register should hold the middle byte to be
 in the jiffy clock. The Y register should hold the low
o be stored in the jiffy clock.

E4/F767 to set the three-byte jiffy clock at A2-A0
he values in the accumulator, X register, and Y register.

### C64 KERNAL jump table (Frank Kontros)
: A=MSB, X=middle, Y=LSB             A X Y  - - -  - - -

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .AXY - Clock value in jiffies (1/60 secs).
egisters Out : None.
emory Changed: Relevant system time locations set.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
die laufende Zeit neu

### Mapping the Commodore 64 (Sheldon Leemon)
outine performs the reverse operation from RDTIM, storing the value in the
ister into location 160 ($A0), the .X register into 161 ($A1),
e Accumulator into 162 ($A2).  Interrupts are first disabled, to
ure that the clock will not be updated while being set.

### Machine Language Routines (Todd D Heimarck)
outine sets the value in the software jiffy dock. The
in the accumulator is transferred to the low byte (loca-
A2), the value in .X to the middle byte (location $A1),
e value in .Y to the high byte (location $A0). The speci-
alue should be less than $4F1A01, which corresponds to
00 hours.

### Commodore 128 intern (Jörg Schieb et al.)
utine setzt die Systemuhr TI, die ab
e $A0 definiert ist. Diese Uhr wird von der Kernal-IRQ-
e gesteuert und ist nicht sehr genau. Legen Sie auf eine
re Uhr Wert, so benutzen Sie die Timer in den beiden
(Siehe auch entsprechendes Kapitel) Das höchstwertige
er 24-Stunden-Uhr wird im Y-Register übergeben.

abeparameter**: .A, .X, .Y

piel**:

      ;Rücksetzen der Systemuhr
      LDA #$00  ;Rücksetzen bedeutet
      TAY       ;auf 0,0,0 setzen
      TAX       ;Alle drei Register auf null
      JSR $FFDB ;SETTIM

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*