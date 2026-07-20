---
title: Reading the error channel of a disk drive
source_url: https://codebase.c64.org/doku.php?id=base%3Areading_the_error_channel_of_a_disk_drive
category: tool
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---


# Reading the error channel of a disk drive

# Reading the error channel of a disk drive

A simple example on how to read the error channel of a disk drive and print the error string to screen.

The error string has a very simple format: error number, error string, track, sector

A small warning: Both the BASIC and the Assembler versions will deadlock if the device is not present.

Examples:

00, OK,00,00 (no error)

21, READ ERROR,18,00 (read error on track 18, sector 0)

BASIC code like you should do it in BASIC:

10 OPEN 15,8,15 20 INPUT#15,F,E$,T,S 30 PRINT F;E$;T;S 40 CLOSE 15

BASIC code similar to the assembler code:

10 OPEN 15,8,15 20 IF ST<>0 THEN GOTO 40 30 GET#15,A$:PRINT A$;:GOTO 20 40 CLOSE 15

Assembler:

```
        LDA #$00      ; no filename
        LDX #$00
        LDY #$00
        JSR $FFBD     ; call SETNAM
        LDA #$0F      ; file number 15
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$0F      ; secondary address 15 (error channel)
        JSR $FFBA     ; call SETLFS
        JSR $FFC0     ; call OPEN
        BCS .error    ; if carry set, the file could not be opened
        LDX #$0F      ; filenumber 15
        JSR $FFC6     ; call CHKIN (file 15 now used as input)
.loop   JSR $FFB7     ; call READST (read status byte)
        BNE .eof      ; either EOF or read error
        JSR $FFCF     ; call CHRIN (get a byte from file)
        JSR $FFD2     ; call CHROUT (print byte to screen)
        JMP .loop     ; next byte
.eof
.close
        LDA #$0F      ; filenumber 15
        JSR $FFC3     ; call CLOSE
        JSR $FFCC     ; call CLRCHN
        RTS
.error
        ; Akkumulator contains BASIC error code
        ; most likely error:
        ; A = $05 (DEVICE NOT PRESENT)
        ... error handling for open errors ...
        JMP .close    ; even if OPEN failed, the file has to be closed
```
There is an easier method to read the error channel of a drive by avoiding the Kernal file API. This will limit you to IEC-bus devices but allows you to avoid the deadlock if a device is not present. In this version the status-byte is accessed directly which reduces the portability of the code. The LISTEN/SECLSN/UNLSN sequence is needed to detect the drive without deadlock:

```
        LDA #$00
        STA $90       ; clear STATUS flags
        LDA $BA       ; device number
        JSR $FFB1     ; call LISTEN
        LDA #$6F      ; secondary address 15 (command channel)
        JSR $FF93     ; call SECLSN (SECOND)
        JSR $FFAE     ; call UNLSN
        LDA $90       ; get STATUS flags
        BNE .devnp    ; device not present
        LDA $BA       ; device number
        JSR $FFB4     ; call TALK
        LDA #$6F      ; secondary address 15 (error channel)
        JSR $FF96     ; call SECTLK (TKSA)
.loop   LDA $90       ; get STATUS flags
        BNE .eof      ; either EOF or error
        JSR $FFA5     ; call IECIN (get byte from IEC bus)
        JSR $FFD2     ; call CHROUT (print byte to screen)
        JMP .loop     ; next byte
.eof
        JSR $FFAB     ; call UNTLK
        RTS
.devnp
        ... device not present handling ...
        RTS
```

## Codice Estratto

### Snippet Codice (BASIC)

```basic
10 OPEN 15,8,15
20 INPUT#15,F,E$,T,S
30 PRINT F;E$;T;S
40 CLOSE 15
```

### Snippet Codice (BASIC)

```basic
10 OPEN 15,8,15
20 IF ST<>0 THEN GOTO 40
30 GET#15,A$:PRINT A$;:GOTO 20
40 CLOSE 15
```

### Snippet Codice (BASIC)

```basic
LDA #$00      ; no filename
        LDX #$00
        LDY #$00
        JSR $FFBD     ; call SETNAM

        LDA #$0F      ; file number 15
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$0F      ; secondary address 15 (error channel)
        JSR $FFBA     ; call SETLFS

        JSR $FFC0     ; call OPEN
        BCS .error    ; if carry set, the file could not be opened

        LDX #$0F      ; filenumber 15
        JSR $FFC6     ; call CHKIN (file 15 now used as input)

.loop   JSR $FFB7     ; call READST (read status byte)
        BNE .eof      ; either EOF or read error
        JSR $FFCF     ; call CHRIN (get a byte from file)
        JSR $FFD2     ; call CHROUT (print byte to screen)
        JMP .loop     ; next byte

.eof
.close
        LDA #$0F      ; filenumber 15
        JSR $FFC3     ; call CLOSE

        JSR $FFCC     ; call CLRCHN
        RTS
.error
        ; Akkumulator contains BASIC error code

        ; most likely error:
        ; A = $05 (DEVICE NOT PRESENT)

        ... error handling for open errors ...
        JMP .close    ; even if OPEN failed, the file has to be closed
```

### Snippet Codice (BASIC)

```basic
LDA #$00
        STA $90       ; clear STATUS flags

        LDA $BA       ; device number
        JSR $FFB1     ; call LISTEN
        LDA #$6F      ; secondary address 15 (command channel)
        JSR $FF93     ; call SECLSN (SECOND)
        JSR $FFAE     ; call UNLSN
        LDA $90       ; get STATUS flags
        BNE .devnp    ; device not present

        LDA $BA       ; device number
        JSR $FFB4     ; call TALK
        LDA #$6F      ; secondary address 15 (error channel)
        JSR $FF96     ; call SECTLK (TKSA)

.loop   LDA $90       ; get STATUS flags
        BNE .eof      ; either EOF or error
        JSR $FFA5     ; call IECIN (get byte from IEC bus)
        JSR $FFD2     ; call CHROUT (print byte to screen)
        JMP .loop     ; next byte
.eof
        JSR $FFAB     ; call UNTLK
        RTS
.devnp
        ... device not present handling ...
        RTS
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Areading_the_error_channel_of_a_disk_drive](https://codebase.c64.org/doku.php?id=base%3Areading_the_error_channel_of_a_disk_drive)*


### Collegamenti e Riferimenti Hardware
- **$FFD2 (CHROUT (Output Character))**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#ffd2).
