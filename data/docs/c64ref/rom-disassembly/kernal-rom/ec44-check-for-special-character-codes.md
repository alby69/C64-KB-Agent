---
title: check for special character codes
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
- ec44-prft-auf-steuerzeichen
- ec5e-shift-commodore-key-check
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EC44
  address_end: $EC75
  symbol: check-for-special-character-codes
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EC44**: compare with [SWITCH TO LOWER CASE]'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EC44**: chr$(14) Großschrift'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EC44**: <switch to lower case>'
---

# $EC44 — check for special character codes

## Disassemblatura
```assembly
.EC44  C9 0E    CMP #$0E   ; compare with [SWITCH TO LOWER CASE]
.EC46  D0 07    BNE $EC4F   ; if not [SWITCH TO LOWER CASE] skip the switch
.EC48  AD 18 D0 LDA $D018   ; get the start of character memory address
.EC4B  09 02    ORA #$02   ; mask xxxx xx1x, set lower case characters
.EC4D  D0 09    BNE $EC58   ; go save the new value, branch always check for special character codes except fro switch to lower case
.EC4F  C9 8E    CMP #$8E   ; compare with [SWITCH TO UPPER CASE]
.EC51  D0 0B    BNE $EC5E   ; if not [SWITCH TO UPPER CASE] go do the [SHIFT]+[C=] key check
.EC53  AD 18 D0 LDA $D018   ; get the start of character memory address
.EC56  29 FD    AND #$FD   ; mask xxxx xx0x, set upper case characters
.EC58  8D 18 D0 STA $D018   ; save the start of character memory address
.EC5B  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit do the [SHIFT]+[C=] key check
.EC5E  C9 08    CMP #$08   ; compare with disable [SHIFT][C=]
.EC60  D0 07    BNE $EC69   ; if not disable [SHIFT][C=] skip the set
.EC62  A9 80    LDA #$80   ; set to lock shift mode switch
.EC64  0D 91 02 ORA $0291   ; OR it with the shift mode switch
.EC67  30 09    BMI $EC72   ; go save the value, branch always
.EC69  C9 09    CMP #$09   ; compare with enable [SHIFT][C=]
.EC6B  D0 EE    BNE $EC5B   ; exit if not enable [SHIFT][C=]
.EC6D  A9 7F    LDA #$7F   ; set to unlock shift mode switch
.EC6F  2D 91 02 AND $0291   ; AND it with the shift mode switch
.EC72  8D 91 02 STA $0291   ; save the shift mode switch $00 = enabled, $80 = locked
.EC75  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
```


## Commenti

### Original Disassembly (—)
- **$EC44**: compare with [SWITCH TO LOWER CASE]
- **$EC46**: if not [SWITCH TO LOWER CASE] skip the switch
- **$EC48**: get the start of character memory address
- **$EC4B**: mask xxxx xx1x, set lower case characters
- **$EC4D**: go save the new value, branch always check for special character codes except fro switch to lower case
- **$EC4F**: compare with [SWITCH TO UPPER CASE]
- **$EC51**: if not [SWITCH TO UPPER CASE] go do the [SHIFT]+[C=] key check
- **$EC53**: get the start of character memory address
- **$EC56**: mask xxxx xx0x, set upper case characters
- **$EC58**: save the start of character memory address
- **$EC5B**: restore the registers, set the quote flag and exit do the [SHIFT]+[C=] key check
- **$EC5E**: compare with disable [SHIFT][C=]
- **$EC60**: if not disable [SHIFT][C=] skip the set
- **$EC62**: set to lock shift mode switch
- **$EC64**: OR it with the shift mode switch
- **$EC67**: go save the value, branch always
- **$EC69**: compare with enable [SHIFT][C=]
- **$EC6B**: exit if not enable [SHIFT][C=]
- **$EC6D**: set to unlock shift mode switch
- **$EC6F**: AND it with the shift mode switch
- **$EC72**: save the shift mode switch $00 = enabled, $80 = locked
- **$EC75**: restore the registers, set the quote flag and exit

### Commodore-64-intern-Buch (Commodore)
- **$EC44**: chr$(14) Großschrift
- **$EC46**: verzweige wenn nein
- **$EC48**: Character-Generator
- **$EC4B**: auf Großschrift-Modus
- **$EC4D**: unbedingter Sprung
- **$EC4F**: chr$(142) Kleinschrift
- **$EC51**: verzweige wenn nein
- **$EC53**: Character-Generator
- **$EC56**: Kleinschrift-Modus
- **$EC58**: setzen
- **$EC5B**: Ausgabe abschließen
- **$EC5E**: chr$(8) Code zur Blockierung SHIFT und COMMOD.-Taste
- **$EC60**: verzweige wenn nein
- **$EC62**: oberstes Bit des
- **$EC64**: Shift-Commodore Flags setzen
- **$EC67**: unbedingter Sprung
- **$EC69**: chr$(9) Code zur Freigabe von SHIFT und COMMOD.-Taste
- **$EC6B**: verzweige wenn nein
- **$EC6D**: oberstes Bit des
- **$EC6F**: Shift-Commodore Flags löschen
- **$EC72**: Wert speichern
- **$EC75**: Ausgabe abschließen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EC44**: <switch to lower case>
- **$EC46**: nope
- **$EC48**: VIC memory control register
- **$EC4B**: set bit1
- **$EC4D**: always branch
- **$EC4F**: <switch to upper case>
- **$EC51**: nope
- **$EC53**: VIC memory control register
- **$EC56**: clear bit1
- **$EC58**: and store
- **$EC5B**: finish screen print
- **$EC5E**: <disable <shift-CBM>>
- **$EC60**: nope
- **$EC64**: disable MODE
- **$EC67**: always jump
- **$EC69**: <enable <shift-CBM>>
- **$EC6B**: nope, exit
- **$EC6F**: enable MODE
- **$EC72**: store MODE, enable/disable shift keys
- **$EC75**: finish screen print

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*