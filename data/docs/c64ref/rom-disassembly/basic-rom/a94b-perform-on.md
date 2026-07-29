---
title: perform ON
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a94b-basic-befehl-on
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A94B
  address_end: $A96A
  symbol: perform-on
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A94B**: get byte parameter'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A94B**: Byte-Wert (0 bis 255) holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A94F**: GOSUB code'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A94B**: EVALUATE <EXP>, AS BYTE IN FAC+4'
---

# $A94B — perform ON

## Disassemblatura
```assembly
.A94B  20 9E B7 JSR $B79E   ; get byte parameter
.A94E  48       PHA   ; push next character
.A94F  C9 8D    CMP #$8D   ; compare with GOSUB token
.A951  F0 04    BEQ $A957   ; if GOSUB go see if it should be executed
.A953  C9 89    CMP #$89   ; compare with GOTO token
.A955  D0 91    BNE $A8E8   ; if not GOTO do syntax error then warm start next character was GOTO or GOSUB, see if it should be executed
.A957  C6 65    DEC $65   ; decrement the byte value
.A959  D0 04    BNE $A95F   ; if not zero go see if another line number exists
.A95B  68       PLA   ; pull keyword token
.A95C  4C EF A7 JMP $A7EF   ; go execute it
.A95F  20 73 00 JSR $0073   ; increment and scan memory
.A962  20 6B A9 JSR $A96B   ; get fixed-point number into temporary integer skip this n
.A965  C9 2C    CMP #$2C   ; compare next character with ","
.A967  F0 EE    BEQ $A957   ; loop if ","
.A969  68       PLA   ; else pull keyword token, ran out of options
.A96A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A94B**: get byte parameter
- **$A94E**: push next character
- **$A94F**: compare with GOSUB token
- **$A951**: if GOSUB go see if it should be executed
- **$A953**: compare with GOTO token
- **$A955**: if not GOTO do syntax error then warm start next character was GOTO or GOSUB, see if it should be executed
- **$A957**: decrement the byte value
- **$A959**: if not zero go see if another line number exists
- **$A95B**: pull keyword token
- **$A95C**: go execute it
- **$A95F**: increment and scan memory
- **$A962**: get fixed-point number into temporary integer skip this n
- **$A965**: compare next character with ","
- **$A967**: loop if ","
- **$A969**: else pull keyword token, ran out of options

### Commodore-64-intern-Buch (Commodore)
- **$A94B**: Byte-Wert (0 bis 255) holen
- **$A94E**: Code merken
- **$A94F**: 'GOSUB'-Code?
- **$A951**: ja: $A957
- **$A953**: 'GOTO'-Code?
- **$A955**: nein: dann 'SYNTAX ERROR'
- **$A957**: Zähler vermindern
- **$A959**: noch nicht null?
- **$A95B**: ja: Code zurückholen
- **$A95C**: und Befehl ausführen
- **$A95F**: CHRGET nächstes Zeichen holen
- **$A962**: Zeilennummer holen
- **$A965**: ',' Komma?
- **$A967**: ja: dann weiter
- **$A969**: kein Sprung: Code zurückholen
- **$A96A**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$A94F**: GOSUB code
- **$A953**: GOTO code
- **$A965**: comma

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A94B**: EVALUATE <EXP>, AS BYTE IN FAC+4
- **$A94E**: SAVE NEXT CHAR ON STACK
- **$A957**: COUNTED TO RIGHT ONE YET?
- **$A959**: NO, KEEP LOOKING
- **$A95B**: YES, RETRIEVE CMD
- **$A95C**: AND GO.
- **$A95F**: PRIME CONVERT SUBROUTINE
- **$A962**: CONVERT LINE #
- **$A965**: TERMINATE WITH COMMA?
- **$A967**: YES
- **$A969**: NO, END OF LIST, SO IGNORE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*