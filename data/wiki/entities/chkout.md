---
id: chkout
type: entity
title: Execution F250/F309-F278/F331
aliases:
- Execution F250/F309-F278/F331
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/chkout.md
  sha256: 3873b18f72284a33b0a4a7d697d6c452cec16c6bf91805045132281f526f799e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-chkout
---

# Execution F250/F309-F278/F331



# CHKOUT — Execution F250/F309-F278/F331 ($F250)

## Panoramica
La routine KERNAL `CHKOUT` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F250`
- **Chiamata**: `JSR CHKOUT` o `SYS 62032`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (0320) from Kernal CHKOUT vector at
FFC9.

 logical file number passed in the accumulator at en-
 not in the logical file table, display the FILE NOT OPEN
message.

 logical file is in the file number table, obtain the
t device number and secondary address for this logical
file.

 device is the keyboard, display the NOT OUTPUT
rror message.

 device is the screen, store the device number in the
 device number, 9A, and exit.

 device is a serial device, branch to Open Serial Out-
annel.

 device number is 2 (RS-232), jump to Open RS-232
 Channel.

 device is tape, the secondary address must not be
cause this indicates read from tape. If $60 is found, dis-
he NOT OUTPUT FILE error message. If the secondary
s is legal, set the output device number, 9A, to the
1.

ation**:

 F30F/F3CF to see if the logical file number passed in
 X register is in the logical file number table. If not, JMP
1/F784 to display the FILE NOT OPEN error message
 return with 3 in accumulator and carry set, then exit.
 F31F/F3DF to obtain the current device number and
 current secondary address from their respective tables.
the current device is the keyboard, JMP F70D/F790 to
play the NOT OUTPUT FILE error message, set accu-
ator to 7, set carry, and exit.
the current device is the screen, store the device number
9A, the output device number, then CLC, and exit.
the current device is a serial device, branch to F279/F332
Open Serial Output Channel.
the current device is an RS-232 device, JMP EFE1/F0BC
Open RS-232 Output Channel.
the current device is tape, the secondary address must not
$60 (read tape). If the secondary address is $60, JMP to
 OUTPUT FILE error, set accumulator to 7, set carry,
 exit. If the secondary address is legal, set the output de-
e number, 9A, to 1 (tape).
 and RTS.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-chkout]]
