---
title: character get subroutine for zero page
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0079-chrgot
- e3a2-kopie-der-chrget-routine
- sbc
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  - marko_mäkelä.txt
  - bob_sander-cederlof.txt
  - magnus_nyman.txt
  address: $E3A2
  address_end: $E3B9
  symbol: character-get-subroutine-for-zero-page
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E3A2**: increment BASIC execute pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E3A2**: LOW-Byte Zeiger erhöhen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E3AB**: colon'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E3A8**: <<< ACTUAL ADDRESS FILLED IN LATER >>>'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E3A2**: increment <TXTPTR'
---

# $E3A2 — character get subroutine for zero page

## Disassemblatura
```assembly
.E3A2  E6 7A    INC $7A   ; increment BASIC execute pointer low byte
.E3A4  D0 02    BNE $E3A8   ; branch if no carry else
.E3A6  E6 7B    INC $7B   ; increment BASIC execute pointer high byte page 0 initialisation table from $0079 scan memory
.E3A8  AD 60 EA LDA $EA60   ; get byte to scan, address set by call routine
.E3AB  C9 3A    CMP #$3A   ; compare with ":"
.E3AD  B0 0A    BCS $E3B9   ; exit if>= page 0 initialisation table from $0080 clear Cb if numeric
.E3AF  C9 20    CMP #$20   ; compare with " "
.E3B1  F0 EF    BEQ $E3A2   ; if " " go do next
.E3B3  38       SEC   ; set carry for SBC
.E3B4  E9 30    SBC #$30   ; subtract "0"
.E3B6  38       SEC   ; set carry for SBC
.E3B7  E9 D0    SBC #$D0   ; subtract -"0" clear carry if byte = "0"-"9"
.E3B9  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E3A2**: increment BASIC execute pointer low byte
- **$E3A4**: branch if no carry else
- **$E3A6**: increment BASIC execute pointer high byte page 0 initialisation table from $0079 scan memory
- **$E3A8**: get byte to scan, address set by call routine
- **$E3AB**: compare with ":"
- **$E3AD**: exit if>= page 0 initialisation table from $0080 clear Cb if numeric
- **$E3AF**: compare with " "
- **$E3B1**: if " " go do next
- **$E3B3**: set carry for SBC
- **$E3B4**: subtract "0"
- **$E3B6**: set carry for SBC
- **$E3B7**: subtract -"0" clear carry if byte = "0"-"9"

### Commodore-64-intern-Buch (Commodore)
- **$E3A2**: LOW-Byte Zeiger erhöhen
- **$E3A4**: Zeiger in BASIC-Text erhöhen
- **$E3A6**: HIGH-Byte Zeiger erhöhen
- **$E3A8**: BASIC-Adresse laden
- **$E3AB**: keine Zahl,
- **$E3AD**: dann fertig
- **$E3AF**: ' ' Leerzeichen überlesen
- **$E3B1**: ja, nächstes Zeichen
- **$E3B3**: Test auf
- **$E3B4**: Ziffer,
- **$E3B6**: dann
- **$E3B7**: C=1
- **$E3B9**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E3AB**: colon
- **$E3AF**: space
- **$E3B4**: 0

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E3A8**: <<< ACTUAL ADDRESS FILLED IN LATER >>>
- **$E3AB**: EOS, ALSO TOP OF NUMERIC RANGE
- **$E3AD**: NOT NUMBER, MIGHT BE EOS
- **$E3AF**: IGNORE BLANKS
- **$E3B3**: TEST FOR NUMERIC RANGE IN WAY THAT
- **$E3B4**: CLEARS CARRY IF CHAR IS DIGIT
- **$E3B6**: AND LEAVES CHAR IN A-REG

### Magnus Nyman (Magnus Nyman)
- **$E3A2**: increment <TXTPTR
- **$E3A4**: skip high byte
- **$E3A6**: increment >TXTPTR
- **$E3A8**: CHRGOT entry, read TXTPTR
- **$E3AB**: colon (terminator), sets (Z)
- **$E3AF**: space, get next character
- **$E3B4**: zero

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*