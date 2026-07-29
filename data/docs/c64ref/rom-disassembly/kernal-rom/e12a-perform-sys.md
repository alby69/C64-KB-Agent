---
title: perform SYS
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
- e12a-sys-befehl
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E12A
  address_end: $E155
  symbol: perform-sys
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E12A**: evaluate expression and check is numeric, else do type
      mismatch'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E12A**: FRMNUM, numerischen Ausdruck holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E130**: low  E146'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E12A**: evaluate text & confirm numeric'
---

# $E12A — perform SYS

## Disassemblatura
```assembly
.E12A  20 8A AD JSR $AD8A   ; evaluate expression and check is numeric, else do type mismatch
.E12D  20 F7 B7 JSR $B7F7   ; convert FAC_1 to integer in temporary integer
.E130  A9 E1    LDA #$E1   ; get return address high byte
.E132  48       PHA   ; push as return address
.E133  A9 46    LDA #$46   ; get return address low byte
.E135  48       PHA   ; push as return address
.E136  AD 0F 03 LDA $030F   ; get saved status register
.E139  48       PHA   ; put on stack
.E13A  AD 0C 03 LDA $030C   ; get saved A
.E13D  AE 0D 03 LDX $030D   ; get saved X
.E140  AC 0E 03 LDY $030E   ; get saved Y
.E143  28       PLP   ; pull processor status
.E144  6C 14 00 JMP ($0014)   ; call SYS address tail end of SYS code
.E147  08       PHP   ; save status
.E148  8D 0C 03 STA $030C   ; save returned A
.E14B  8E 0D 03 STX $030D   ; save returned X
.E14E  8C 0E 03 STY $030E   ; save returned Y
.E151  68       PLA   ; restore saved status
.E152  8D 0F 03 STA $030F   ; save status
.E155  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E12A**: evaluate expression and check is numeric, else do type mismatch
- **$E12D**: convert FAC_1 to integer in temporary integer
- **$E130**: get return address high byte
- **$E132**: push as return address
- **$E133**: get return address low byte
- **$E135**: push as return address
- **$E136**: get saved status register
- **$E139**: put on stack
- **$E13A**: get saved A
- **$E13D**: get saved X
- **$E140**: get saved Y
- **$E143**: pull processor status
- **$E144**: call SYS address tail end of SYS code
- **$E147**: save status
- **$E148**: save returned A
- **$E14B**: save returned X
- **$E14E**: save returned Y
- **$E151**: restore saved status
- **$E152**: save status

### Commodore-64-intern-Buch (Commodore)
- **$E12A**: FRMNUM, numerischen Ausdruck holen
- **$E12D**: in Adressformat wandeln, nach $14/$15
- **$E130**: Rück-
- **$E132**: sprungadresse
- **$E133**: auf
- **$E135**: Stack
- **$E136**: Status,
- **$E139**: in Stack
- **$E13A**: Akku,
- **$E13D**: X-Register und
- **$E140**: Y-Register übergeben
- **$E143**: Status setzen
- **$E144**: Routine aufrufen
- **$E147**: Status speichern
- **$E148**: Akku,
- **$E14B**: X-Register,
- **$E14E**: Y-Register und
- **$E151**: Status
- **$E152**: wieder speichern
- **$E155**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E130**: low  E146
- **$E133**: high E146

### Magnus Nyman (Magnus Nyman)
- **$E12A**: evaluate text & confirm numeric
- **$E12D**: convert fac#1 to integer in LINNUM
- **$E130**: set return address on stack to $ea46
- **$E136**: SPREG, user flag register
- **$E13A**: SAREG, user (A) register
- **$E13D**: SXREG, user (X) register
- **$E140**: SYREG, user (Y) register
- **$E144**: execute user routine, exit with rts
- **$E148**: store in SAREG, user (A) register
- **$E14B**: store in SXREG, user (X) register
- **$E14E**: store in SYREG, user (Y) register
- **$E152**: store in SPREG, user flag register
- **$E155**: back

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*