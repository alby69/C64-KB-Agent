---
title: Sending a command to a disk drive, the easy way
source_url: https://codebase.c64.org/doku.php?id=base%3Asending_a_command_to_a_disk_drive
category: tool
topics:
- basic
- assembly
difficulty: beginner
language: assembly
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---


# Sending a command to a disk drive, the easy way

base:sending_a_command_to_a_disk_drive

                ### Table of Contents

# Sending a command to a disk drive, the easy way

The easiest way of sending a command to the disk drive is by simply using the command string as filename when calling OPEN.

BASIC code:

OPEN 15,8,15,"I":CLOSE 15

Assembler code:

```
        LDA #cmd_end-cmd
        LDX #<cmd
        LDY #>cmd
        JSR $FFBD     ; call SETNAM
        LDA #$0F      ; file number 15
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$0F      ; secondary address 15
        JSR $FFBA     ; call SETLFS
        JSR $FFC0     ; call OPEN
        BCS .error    ; if carry set, the file could not be opened
.close
        LDA #$0F      ; filenumber 15
        JSR $FFC3     ; call CLOSE
        JSR $FFCC     ; call CLRCHN
        RTS
.error
        ; Akkumulator contains BASIC error code
        ; most likely errors:
        ; A = $05 (DEVICE NOT PRESENT)
        ... error handling for open errors ...
        JMP .close    ; even if OPEN failed, the file has to be closed
cmd:    .TEXT "I"     ; command string
cmd_end:
```
# Sending a command to a disk drive, the flexible way

Another way of sending a command to the disk drive is by leaving the filename string empty and send the command string afterwards. The advantage of this is that you can send several commands but only open the command channel one time.

BASIC code:

OPEN 15,8,15:PRINT#15,"I":CLOSE 15

Assembler code:

```
        LDA #$00
        LDX #$00
        LDY #$00
        JSR $FFBD     ; call SETNAM (no filename)
        LDA #$0F      ; file number 15
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$0F      ; secondary address 15
        JSR $FFBA     ; call SETLFS
        JSR $FFC0     ; call OPEN
        BCS .error    ; if carry set, the file could not be opened
        LDX #$0F      ; filenumber 15
        JSR $FFC9     ; call CHKOUT (file 15 now used as output)
        LDY #$00
.loop   LDA cmd,y     ; get byte from command string
        JSR $FFD2     ; call CHROUT (send byte through command channel)
        INY
        CPY #cmd_end-cmd
        BNE .loop
.close
        LDA #$0F      ; filenumber 15
        JSR $FFC3     ; call CLOSE
        JSR $FFCC     ; call CLRCHN
        RTS
.error
        ; Akkumulator contains BASIC error code
        ; most likely errors:
        ; A = $05 (DEVICE NOT PRESENT)
        ... error handling for open errors ...
        JMP .close    ; even if OPEN failed, the file has to be closed
cmd:    .TEXT "I"     ; command string
        .BYTE $0D     ; carriage return, needed if more than one command is sent
cmd_end:
```
base/sending_a_command_to_a_disk_drive.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
OPEN 15,8,15,"I":CLOSE 15
```

### Snippet Codice (BASIC)

```basic
LDA #cmd_end-cmd
        LDX #<cmd
        LDY #>cmd
        JSR $FFBD     ; call SETNAM

        LDA #$0F      ; file number 15
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$0F      ; secondary address 15
        JSR $FFBA     ; call SETLFS

        JSR $FFC0     ; call OPEN
        BCS .error    ; if carry set, the file could not be opened
.close
        LDA #$0F      ; filenumber 15
        JSR $FFC3     ; call CLOSE

        JSR $FFCC     ; call CLRCHN
        RTS
.error
        ; Akkumulator contains BASIC error code

        ; most likely errors:
        ; A = $05 (DEVICE NOT PRESENT)

        ... error handling for open errors ...
        JMP .close    ; even if OPEN failed, the file has to be closed

cmd:    .TEXT "I"     ; command string
cmd_end:
```

### Snippet Codice (BASIC)

```basic
OPEN 15,8,15:PRINT#15,"I":CLOSE 15
```

### Snippet Codice (BASIC)

```basic
LDA #$00
        LDX #$00
        LDY #$00
        JSR $FFBD     ; call SETNAM (no filename)

        LDA #$0F      ; file number 15
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$0F      ; secondary address 15
        JSR $FFBA     ; call SETLFS

        JSR $FFC0     ; call OPEN
        BCS .error    ; if carry set, the file could not be opened

        LDX #$0F      ; filenumber 15
        JSR $FFC9     ; call CHKOUT (file 15 now used as output)

        LDY #$00
.loop   LDA cmd,y     ; get byte from command string
        JSR $FFD2     ; call CHROUT (send byte through command channel)
        INY
        CPY #cmd_end-cmd
        BNE .loop
.close
        LDA #$0F      ; filenumber 15
        JSR $FFC3     ; call CLOSE

        JSR $FFCC     ; call CLRCHN
        RTS
.error
        ; Akkumulator contains BASIC error code

        ; most likely errors:
        ; A = $05 (DEVICE NOT PRESENT)

        ... error handling for open errors ...
        JMP .close    ; even if OPEN failed, the file has to be closed

cmd:    .TEXT "I"     ; command string
        .BYTE $0D     ; carriage return, needed if more than one command is sent
cmd_end:
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asending_a_command_to_a_disk_drive](https://codebase.c64.org/doku.php?id=base%3Asending_a_command_to_a_disk_drive)*


### Collegamenti e Riferimenti Hardware
- **$FFD2 (CHROUT (Output Character))**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#ffd2).
