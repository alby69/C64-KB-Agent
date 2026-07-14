---
title: geoRAM Register Description
source_url: https://codebase.c64.org/doku.php?id=base%3Ageoram_registers
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# geoRAM Register Description

base:georam_registers

                # geoRAM Register Description

by White Flame

The geoRAM is a banked memory system. It uses the registers at $dffe and $dfff to determine what part of the geoRAM memory should be visible in the banked window at $de00-$deff.

$dfff - block selection, each block is 16KB $dffe - select a 256-byte page within the block (0-63)

Since there are only 64 256-byte pages that fit in 16k, the value in $dffe ranges from 0 to 63. The number of 16k blocks that is available depends on the size of the geoRAM:

512k = 0- 31, $00-$1f 1024k = 0- 63, $00-$3f 2048k = 0-127, $00-$7f

The two registers are write-only. Attempting to read them will only return bus noise. If you need to know the current values of the registers, you need to write a copy in normal RAM when you set them.

To convert a straight 24-bit offset into the geoRAM block/page format, you need to shift the two upper bits from the middle byte into the high byte:

.byte temp .byte addressLo, addressMd, addressHi lda addressMd sta temp and #%00111111 sta $dffe lda addressHi asl temp rol asl temp rol sta $dfff ldx addressLo lda $de00,x

base/georam_registers.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
$dfff - block selection, each block is 16KB
$dffe - select a 256-byte page within the block (0-63)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
512k = 0- 31, $00-$1f
 1024k = 0- 63, $00-$3f
 2048k = 0-127, $00-$7f
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.byte temp
.byte addressLo, addressMd, addressHi

lda addressMd
sta temp
and #%00111111
sta $dffe

lda addressHi
asl temp
rol
asl temp
rol
sta $dfff

ldx addressLo
lda $de00,x
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ageoram_registers](https://codebase.c64.org/doku.php?id=base%3Ageoram_registers)*
