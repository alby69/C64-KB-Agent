---
title: eyboard
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
related: []
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
  address: $FF9F
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: None'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine will scan the keyboard and check for pressed keys. It is the
      same
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: eyboard
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: None.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: '- - -  - - -  A X Y'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : None.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: die Tastatur ab
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: ubroutine is called by the IRQ interrupt handler above to read
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine scans the keyboard matrix to determine which
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: Routine ist elementar zur Tastatur-
---

# $FF9F — eyboard ($FF9F)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF9F`
- **Chiamata**: `JSR None` o `SYS 65439`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: IOINIT
r returns: None
k requirements: 5
sters affected: A, X, Y

scription**: This routine scans the Commodore 64 keyboard and checks
essed keys. It is the same routine called by the interrupt handler.
ey is down, its ASCII value is placed in the keyboard queue. This
e is called only if the normal IRQ interrupt is bypassed.

 to Use:

l this routine.

MPLE:

T  JSR SCNKEY      ;SCAN KEYBOARD
   JSR GETIN       ;GET CHARACTER
   CMP #0          ;IS IT NULL?
   BEQ GET         ;YES... SCAN AGAIN
   JSR CHROUT      ;PRINT IT

### Standard KERNAL Functions (Joe Forster / STA)
–
: –
egisters: A, X, Y.
ddress: $EA87.

### Commented ROM Disassembly (Lee Davison)
outine will scan the keyboard and check for pressed keys. It is the same
e called by the interrupt handler. If a key is down, its ASCII value is
 in the keyboard queue.

### Cracking The Kernal (Peter Marcotty)
eyboard

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: None.

87/EB1E to the Keyboard Scan routine (see chap-
 to check for a keypress. If a valid key is found down and
yboard buffer is not full, the ASCII code value for the
 placed in the buffer.

 is useful if you have written a machine language
m that runs with IRQ interrupts disabled, but you still
o scan the keyboard.

### C64 KERNAL jump table (Frank Kontros)
- - -  - - -  A X Y

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : None.
emory Changed: Relevant System Keyboard Values

### Das neue Commodore-64-intern-Buch (Baloui et al.)
die Tastatur ab

### Mapping the Commodore 64 (Sheldon Leemon)
ubroutine is called by the IRQ interrupt handler above to read
yboard device which is connected to CIA #1 (see entry for 56320
) for details on how to read the keyboard).

outine returns the keycode of the key
tly being pressed in 203 ($CB), sets the shift/control flag if
riate, and jumps through the vector at 655 ($28F) to the routine
ets up the proper table to translate the keycode to PETASCII.
cludes with the next routine, which places the PETASCII value of
aracter in the keyboard buffer.

### Machine Language Routines (Todd D Heimarck)
outine scans the keyboard matrix to determine which
if any, are currently pressed. The standard KQ service
e calls SCNKEY, so it's not usually necessary to call it
itly to read the keyboard. The character code for the key
tly pressed is loaded into the keyboard buffer, from
it can be retrieved using the Kernal GETIN routine. The
 code of the keypress read during this routine can also
d in location $CB (64) or $D4 (128), and the status of
ift keys can be read in location $028D (64) or $D3 (128).

### Commodore 128 intern (Jörg Schieb et al.)
Routine ist elementar zur Tastatur-
erung. Die Tastatur wird auf eine gedrückte Taste anhand
staturdekodiertabellen überprüft. Wird eine gedrückte
ermittelt, so wird der ASCII-Wert errechnet und dieser
staturbuffer (ab $034A) hinzugefügt.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*