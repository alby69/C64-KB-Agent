---
title: kernal vectors
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0314-cinv
- 0316-cbinv
- 0318-nminv
- 031a-iopen
- 031c-iclose
- 031e-ichkin
- 0320-ickout
- 0322-iclrch
- 0324-ibasin
- 0326-ibsout
- 0328-istop
- 032a-igetin
- 032c-iclall
- 032e-usrcmd
- 0330-iload
- 0332-isave
- brk
- fd30-und-io-vektoren
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FD30
  address_end: $FD4E
  symbol: kernal-vectors
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FD30**: $0314 IRQ vector'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Nessun commento disponibile.
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FD30**: IRQ'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FD30**: CINV VECTOR: hardware interrupt ($ea31)'
---

# $FD30 — kernal vectors

## Disassemblatura
```assembly
.FD30  31 EA   ; $0314 IRQ vector
.FD32  66 FE   ; $0316 BRK vector
.FD34  47 FE   ; $0318 NMI vector
.FD36  4A F3   ; $031A open a logical file
.FD38  91 F2   ; $031C close a specified logical file
.FD3A  0E F2   ; $031E open channel for input
.FD3C  50 F2   ; $0320 open channel for output
.FD3E  33 F3   ; $0322 close input and output channels
.FD40  57 F1   ; $0324 input character from channel
.FD42  CA F1   ; $0326 output character to channel
.FD44  ED F6   ; $0328 scan stop key
.FD46  3E F1   ; $032A get character from the input device
.FD48  2F F3   ; $032C close all channels and files
.FD4A  66 FE   ; $032E user function Vector to user defined command, currently points to BRK. This appears to be a holdover from PET days, when the built-in machine language monitor would jump through the $032E vector when it encountered a command that it did not understand, allowing the user to add new commands to the monitor. Although this vector is initialized to point to the routine called by STOP/RESTORE and the BRK interrupt, and is updated by the kernal vector routine at $FD57, it no longer has any function.
.FD4C  A5 F4   ; $0330 load
.FD4E  ED F5   ; $0332 save
```


## Commenti

### Original Disassembly (—)
- **$FD30**: $0314 IRQ vector
- **$FD32**: $0316 BRK vector
- **$FD34**: $0318 NMI vector
- **$FD36**: $031A open a logical file
- **$FD38**: $031C close a specified logical file
- **$FD3A**: $031E open channel for input
- **$FD3C**: $0320 open channel for output
- **$FD3E**: $0322 close input and output channels
- **$FD40**: $0324 input character from channel
- **$FD42**: $0326 output character to channel
- **$FD44**: $0328 scan stop key
- **$FD46**: $032A get character from the input device
- **$FD48**: $032C close all channels and files
- **$FD4A**: $032E user function Vector to user defined command, currently points to BRK. This appears to be a holdover from PET days, when the built-in machine language monitor would jump through the $032E vector when it encountered a command that it did not understand, allowing the user to add new commands to the monitor. Although this vector is initialized to point to the routine called by STOP/RESTORE and the BRK interrupt, and is updated by the kernal vector routine at $FD57, it no longer has any function.
- **$FD4C**: $0330 load
- **$FD4E**: $0332 save

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
- **$FD30**: IRQ
- **$FD32**: BRK
- **$FD34**: NMI
- **$FD36**: open
- **$FD38**: close
- **$FD3A**: set input dev
- **$FD3C**: set output dev
- **$FD3E**: restore I/O
- **$FD40**: input
- **$FD42**: output
- **$FD44**: test stop key
- **$FD46**: get
- **$FD48**: abort I/O
- **$FD4A**: unused (BRK)
- **$FD4C**: load ram
- **$FD4E**: save ram

### Magnus Nyman (Magnus Nyman)
- **$FD30**: CINV VECTOR: hardware interrupt ($ea31)
- **$FD32**: CBINV VECTOR: software interrupt ($fe66)
- **$FD34**: NMINV VECTOR: hardware nmi interrupt ($fe47)
- **$FD36**: IOPEN VECTOR: KERNAL open routine ($f34a)
- **$FD38**: ICLOSE VECTOR: KERNAL close routine ($f291)
- **$FD3A**: ICHKIN VECTOR: KERNAL chkin routine ($f20e)
- **$FD3C**: ICKOUT VECTOR: KERNAL chkout routine ($f250)
- **$FD3E**: ICLRCH VECTOR: KERNAL clrchn routine ($f333)
- **$FD40**: IBASIN VECTOR: KERNAL chrin routine ($f157)
- **$FD42**: IBSOUT VECTOR: KERNAL chrout routine ($f1ca)
- **$FD44**: ISTOP VECTOR: KERNAL stop routine ($f6ed)
- **$FD46**: IGETIN VECTOR: KERNAL getin routine ($f13e)
- **$FD48**: ICLALL VECTOR: KERNAL clall routine ($f32f)
- **$FD4A**: USRCMD VECTOR: user defined ($fe66)
- **$FD4C**: ILOAD VECTOR: KERNAL load routine ($f4a5)
- **$FD4E**: ISAVE VECTOR: KERNAL save routine ($f5ed)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*