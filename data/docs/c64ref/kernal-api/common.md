---
title: Exit for Close Logical File Routines F2F1/F3B1-F30E/F3CE
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
- beq
- bne
- clc
- f34a-open
- jsr
- rts
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $F2F1
  symbol: Common
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: Falls through after JSR to Close Logical File for Serial
      Device'
---

# Common — Exit for Close Logical File Routines F2F1/F3B1-F30E/F3CE ($F2F1)

## Panoramica
La routine KERNAL `Common` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F2F1`
- **Chiamata**: `JSR Common` o `SYS 62193`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Falls through after JSR to Close Logical File for Serial Device
E/FEAE, BEQ at F29F/F358 and F2A3/F35C in Deter-
evice to Close, BEQ at in F2CC/F391 Close Logical File
pe, BNE at F2E4/F34A in Close Logical File for Tape ,
 F2EB/F3AB in Close Logical File for Tape; alternate en-
 F2F2/F3B2 by JSR at F2AC/F365 in Close Logical File
-232 Device.

dex into the file tables for the current logical file is
ved from the stack (except for the alternate entry from
 which has already pulled it from the stack).

mber of open files, 98, is decremented and com-
to the index into the file tables. If equal, the current
l file is the last entry in the file table. In this case, there
need to delete the actual entries in the tables since the
r to the tables will now cause the next OPEN to over-
these entries.

 current logical file index is not equal to the number
n files (after the decrement), replace the current entries
 logical file number, device number, and secondary ad-
tables with the last entries in the table. As the order
 a particular table is unimportant, this rearrangement
ively deletes the current entries for the logical file, de-
and secondary address.
conditions:
into file tables for current logical file is pulled from the
at entry.

ation**:

l index into file tables for current logical file from stack.
nsfer the index into the tables to X register.
rement the number of open files (plus one), location 98.
X register equals the value in 98, the logical file being
sed is the last entry in the tables. Since 98 points to the
t available space in the tables, the next OPEN will over-
te the entries for this current logical file. Thus, just CLC
 RTS.
the number of open files (plus one) after decrement is not
al to the value in the X register, the current logical file
ng closed is not the last entry in the table. In this case,
e the last entries in the three tables (device number,
ondary address, logical file number) to the current logical
e entries. Before this move,the last entry is pointed to by
and the current entry by the X register.
 and RTS.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*