---
title: Saving a memory range to a file
source_url: https://codebase.c64.org/doku.php?id=base%3Asaving_a_file
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---

# Saving a memory range to a file

base:saving_a_file

                # Saving a memory range to a file

```
file_start = $2000    ; example addresses
file_end   = $4000
        LDA #fname_end-fname
        LDX #<fname
        LDY #>fname
        JSR $FFBD     ; call SETNAM
        LDA #$00
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$00
        JSR $FFBA     ; call SETLFS
        LDA #<file_start
        STA $C1
        LDA #>file_start
        STA $C2
        LDX #<file_end
        LDY #>file_end
        LDA #$C1      ; start address located in $C1/$C2
        JSR $FFD8     ; call SAVE
        BCS .error    ; if carry set, a load error has happened
        RTS
.error
        ; Akkumulator contains BASIC error code
        ... error handling ...
        RTS
fname:  .TEXT "JUST A FILENAME"
fname_end:
```
base/saving_a_file.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
file_start = $2000    ; example addresses
file_end   = $4000

        LDA #fname_end-fname
        LDX #<fname
        LDY #>fname
        JSR $FFBD     ; call SETNAM
        LDA #$00
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$00
        JSR $FFBA     ; call SETLFS

        LDA #<file_start
        STA $C1
        LDA #>file_start
        STA $C2

        LDX #<file_end
        LDY #>file_end
        LDA #$C1      ; start address located in $C1/$C2
        JSR $FFD8     ; call SAVE
        BCS .error    ; if carry set, a load error has happened
        RTS
.error
        ; Akkumulator contains BASIC error code

        ... error handling ...
        RTS

fname:  .TEXT "JUST A FILENAME"
fname_end:
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asaving_a_file](https://codebase.c64.org/doku.php?id=base%3Asaving_a_file)*
