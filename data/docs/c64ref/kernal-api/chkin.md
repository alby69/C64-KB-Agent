---
title: Execution F20E/F2C7-F236/F2EF
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/compute!'s_tool_kit:_kernal.txt
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
- chkin
- clc
- f34a-open
- input
- jmp
- rts
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $F20E
  symbol: CHKIN
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**:'
---

# CHKIN — Execution F20E/F2C7-F236/F2EF ($F20E)

## Panoramica
La routine KERNAL `CHKIN` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F20E`
- **Chiamata**: `JSR CHKIN` o `SYS 61966`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**:
ct JMP through (031E) from Kernal CHKIN vector at FFC6.

 current logical file passed in the X register is in the
l file number table, obtain its corresponding device num-
d secondary address from the device number and
ary address tables. If it is not in the logical file number
 exit with FILE NOT OPEN error message.

 device is the screen or the keyboard, set location 99,
rrent input device number, from BA, the current device
, and exit.

 current device is an RS-232 device, JMP to the
S-232 Device routine.

 current device is a serial device, JMP to the Open
 Input Channel routine.

 current device is tape, see if the secondary address
tes reading from tape. If not, JMP to display the NOT
FILE message.

the current device number in the input device num-
9, CLC, and exit.

ation**:

 F30F/F3CF to see if the logical file number in the X
ister exists. If the logical file passed in the X register is
 in the logical file number table, JMP F701/F784 to FILE
 OPEN error message, set accumulator to 3, set the
ry, and exit.
 F31F/F3DF to set the current logical file number in B8,
 current device number in BA, and the current secondary
ress in B9 from the tables for the logical file, device
ber, and secondary address.
the current device, BA, is the keyboard (0), or the screen
, branch to step 8.
the current device number is > 3, the current device is a
ial device; branch to F237/F2F0 to open a logical file for
erial device.
the current device is an RS-232 device, JMP F04D/F116
open an RS-232 logical file as an input channel.
the current device is tape, see if the secondary address is
. If the secondary address is $60, branch to step 8. The
ondary address of $60 is set during the OPEN Execution
tine when the secondary address is ORed with $60.
the secondary address is not $60, JMP F70A/F78D to dis-
y the NOT INPUT FILE message and exit with the accu-
ator set to 6 and the carry set.
 (the current device number is in the accumulator) into
 the input device number.
 and RTS.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*