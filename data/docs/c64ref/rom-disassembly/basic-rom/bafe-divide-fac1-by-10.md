---
title: divide FAC1 by 10
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
- bafe-fac-fac-10
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BAFE
  address_end: $BB05
  symbol: divide-fac1-by-10
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BAFE**: round and copy FAC1 to FAC2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BAFE**: FAC runden und nach ARG'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BB01**: low  BAF9'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BB01**: SET UP TO PUT'
---

# $BAFE — divide FAC1 by 10

## Disassemblatura
```assembly
.BAFE  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.BB01  A9 F9    LDA #$F9   ; set 10 pointer low byte
.BB03  A0 BA    LDY #$BA   ; set 10 pointer high byte
.BB05  A2 00    LDX #$00   ; clear sign
```


## Commenti

### Original Disassembly (—)
- **$BAFE**: round and copy FAC1 to FAC2
- **$BB01**: set 10 pointer low byte
- **$BB03**: set 10 pointer high byte
- **$BB05**: clear sign

### Commodore-64-intern-Buch (Commodore)
- **$BAFE**: FAC runden und nach ARG
- **$BB01**: Zeiger
- **$BB03**: auf
- **$BB05**: Konstante 10
- **$BB07**: Vergleichsbyte löschen
- **$BB09**: Konstante 10 nach FAC
- **$BB0C**: FAC = ARG / FAC

### Marko Mäkelä (Marko Mäkelä)
- **$BB01**: low  BAF9
- **$BB03**: high BAF9

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BB01**: SET UP TO PUT
- **$BB03**: 10 IN FAC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*