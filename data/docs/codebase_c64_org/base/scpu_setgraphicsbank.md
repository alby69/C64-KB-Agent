---
title: SetGraphicsBank
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_setgraphicsbank
category: reference
topics:
- graphics
- assembly
- memory management
- basic
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-20'
---


# SetGraphicsBank

base:scpu_setgraphicsbank

                # SetGraphicsBank

Sets the VIC Grahoics Bank, The Screen Memory and the Bitmap Memory (both for Bitmap Graphics and Charset Graphics).

| SYNTAX: | SetGraphicsBank SCRMem : BMPMem | ||
| EXAMPLE: | SetGraphicsBank $0400 : $2000 | ||
| PARAMETERS: | Type | Minimum | Maximum | 
| SCRMem | U16 | $0000 | $ffff | 
| BMPMem | U16 | $0000 | $ffff | 

Imporvements: Don't like the write to $d019….

```
    .pseudocommand SetGraphicsBank SCRMem : BMPMem {
        // Graphics Bank Location ($dd00):
        //     $0000 - $3fff = XXXXXX11 (Default)
        //     $4000 - $7fff = XXXXXX10
        //     $8000 - $bfff = XXXXXX01
        //     $c000 - $ffff = XXXXXX00
        .if ([3 - [SCRMem.getValue() >> 14]]==0) {
            :lda #%0000000000000011
            :trb $dd00
        }
        .if ([3 - [SCRMem.getValue() >> 14]]==1) {
            :lda #%0000000000000001
            :tsb $dd00
            asl
            :trb $dd00
        }
        .if ([3 - [SCRMem.getValue() >> 14]]==2) {
            :lda #%0000000000000001
            :trb $dd00
            asl
            :tsb $dd00
        }
        .if ([3 - [SCRMem.getValue() >> 14]]==3) {
            :lda #%0000000000000011
            :tsb $dd00
        }
        // screen location ($d018):
        //     0000XXXX - Bank + $0000
        //     0001XXXX - Bank + $0400
        //     0010XXXX - Bank + $0800
        //     0011XXXX - Bank + $0c00
        //     0100XXXX - Bank + $1000
        //     0101XXXX - Bank + $1400
        //     0110XXXX - Bank + $1800
        //     0111XXXX - Bank + $1c00
        //     1000XXXX - Bank + $2000
        //     1001XXXX - Bank + $2400
        //     1010XXXX - Bank + $2800
        //     1011XXXX - Bank + $2c00
        //     1100XXXX - Bank + $3000
        //     1101XXXX - Bank + $3400
        //     1110XXXX - Bank + $3800
        //     1111XXXX - Bank + $3c00
        //
        // CharSet Location ($d018), LSB used for lower/Upper character set:
        //     XXXX000X - Bank + $0000
        //     XXXX001X - Bank + $0800
        //     XXXX010X - Bank + $1000
        //     XXXX011X - Bank + $1800
        //     XXXX100X - Bank + $2000
        //     XXXX101X - Bank + $2800
        //     XXXX110X - Bank + $3000
        //     XXXX111X - Bank + $3800
        //
        // Bitmap Location ($d018):
        //     XXXX0XXX - Bank + $0000
        //     XXXX1XXX - Bank + $2000
        :lda #[[[SCRMem.getValue() & %0011110000000000] >> 6] | [[BMPMem.getValue() & %0011110000000000]>> 10]]
        sta $d018
```
base/scpu_setgraphicsbank.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
.pseudocommand SetGraphicsBank SCRMem : BMPMem {

        // Graphics Bank Location ($dd00):
        //     $0000 - $3fff = XXXXXX11 (Default)
        //     $4000 - $7fff = XXXXXX10
        //     $8000 - $bfff = XXXXXX01
        //     $c000 - $ffff = XXXXXX00

        .if ([3 - [SCRMem.getValue() >> 14]]==0) {
            :lda #%0000000000000011
            :trb $dd00
        }
        .if ([3 - [SCRMem.getValue() >> 14]]==1) {
            :lda #%0000000000000001
            :tsb $dd00
            asl
            :trb $dd00
        }
        .if ([3 - [SCRMem.getValue() >> 14]]==2) {
            :lda #%0000000000000001
            :trb $dd00
            asl
            :tsb $dd00
        }
        .if ([3 - [SCRMem.getValue() >> 14]]==3) {
            :lda #%0000000000000011
            :tsb $dd00
        }

        // screen location ($d018):
        //     0000XXXX - Bank + $0000
        //     0001XXXX - Bank + $0400
        //     0010XXXX - Bank + $0800
        //     0011XXXX - Bank + $0c00
        //     0100XXXX - Bank + $1000
        //     0101XXXX - Bank + $1400
        //     0110XXXX - Bank + $1800
        //     0111XXXX - Bank + $1c00
        //     1000XXXX - Bank + $2000
        //     1001XXXX - Bank + $2400
        //     1010XXXX - Bank + $2800
        //     1011XXXX - Bank + $2c00
        //     1100XXXX - Bank + $3000
        //     1101XXXX - Bank + $3400
        //     1110XXXX - Bank + $3800
        //     1111XXXX - Bank + $3c00
        //
        // CharSet Location ($d018), LSB used for lower/Upper character set:
        //     XXXX000X - Bank + $0000
        //     XXXX001X - Bank + $0800
        //     XXXX010X - Bank + $1000
        //     XXXX011X - Bank + $1800
        //     XXXX100X - Bank + $2000
        //     XXXX101X - Bank + $2800
        //     XXXX110X - Bank + $3000
        //     XXXX111X - Bank + $3800
        //
        // Bitmap Location ($d018):
        //     XXXX0XXX - Bank + $0000
        //     XXXX1XXX - Bank + $2000

        :lda #[[[SCRMem.getValue() & %0011110000000000] >> 6] | [[BMPMem.getValue() & %0011110000000000]>> 10]]
        sta $d018
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_setgraphicsbank](https://codebase.c64.org/doku.php?id=base%3Ascpu_setgraphicsbank)*


### Collegamenti e Riferimenti Hardware
- **$D018 (Memory Setup Register)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d018).
