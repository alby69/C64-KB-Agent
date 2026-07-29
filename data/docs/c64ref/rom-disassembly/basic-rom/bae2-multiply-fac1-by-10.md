---
title: multiply FAC1 by 10
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
- bae2-fac-fac-10
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BAE2
  address_end: $BAF8
  symbol: multiply-fac1-by-10
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BAE2**: round and copy FAC1 to FAC2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BAE2**: FAC runden und nach ARG'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BAE5**: TEXT FAC EXPONENT'
---

# $BAE2 — multiply FAC1 by 10

## Disassemblatura
```assembly
.BAE2  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.BAE5  AA       TAX   ; copy exponent (set the flags)
.BAE6  F0 10    BEQ $BAF8   ; exit if zero
.BAE8  18       CLC   ; clear carry for add
.BAE9  69 02    ADC #$02   ; add two to exponent (*4)
.BAEB  B0 F2    BCS $BADF   ; do overflow error if > $FF FAC1 = (FAC1 + FAC2) * 2
.BAED  A2 00    LDX #$00   ; clear byte
.BAEF  86 6F    STX $6F   ; clear sign compare (FAC1 EOR FAC2)
.BAF1  20 77 B8 JSR $B877   ; add FAC2 to FAC1 (*5)
.BAF4  E6 61    INC $61   ; increment FAC1 exponent (*10)
.BAF6  F0 E7    BEQ $BADF   ; if exponent now zero go do overflow error
.BAF8  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BAE2**: round and copy FAC1 to FAC2
- **$BAE5**: copy exponent (set the flags)
- **$BAE6**: exit if zero
- **$BAE8**: clear carry for add
- **$BAE9**: add two to exponent (*4)
- **$BAEB**: do overflow error if > $FF FAC1 = (FAC1 + FAC2) * 2
- **$BAED**: clear byte
- **$BAEF**: clear sign compare (FAC1 EOR FAC2)
- **$BAF1**: add FAC2 to FAC1 (*5)
- **$BAF4**: increment FAC1 exponent (*10)
- **$BAF6**: if exponent now zero go do overflow error

### Commodore-64-intern-Buch (Commodore)
- **$BAE2**: FAC runden und nach ARG
- **$BAE5**: FAC-Exponent
- **$BAE6**: FAC gleich null, dann fertig
- **$BAE8**: Exponent + 2
- **$BAE9**: entspricht mal 4
- **$BAEB**: Übertrag ?
- **$BAED**: Vergleichsbyte
- **$BAEF**: löschen
- **$BAF1**: FAC = FAC + ARG entspricht mal 5
- **$BAF4**: Exponent erhöhen entspricht mal 2
- **$BAF6**: Übertrag, dann 'OVERFLOW'
- **$BAF8**: Rücksprung
- **$BAF9**: Fließkommakonstante 10

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BAE5**: TEXT FAC EXPONENT
- **$BAE6**: FINISHED IF FAC=0
- **$BAE9**: ADD 2 TO EXPONENT GIVES (FAC)*4
- **$BAEB**: OVERFLOW
- **$BAF1**: MAKES (FAC)*5
- **$BAF4**: *2, MAKES (FAC)*10
- **$BAF6**: OVERFLOW
- **$BAF9**: 10

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*