---
title: perform AND
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- afe9-basic-befehl-and
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AFE9
  address_end: $B013
  symbol: perform-and
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AFE9**: clear Y for AND'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AFE9**: Flag fur AND'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $AFE9 — perform AND

## Disassemblatura
```assembly
.AFE9  A0 00    LDY #$00   ; clear Y for AND
.AFEB  84 0B    STY $0B   ; set AND/OR invert value
.AFED  20 BF B1 JSR $B1BF   ; evaluate integer expression, no sign check
.AFF0  A5 64    LDA $64   ; get FAC1 mantissa 3
.AFF2  45 0B    EOR $0B   ; EOR low byte
.AFF4  85 07    STA $07   ; save it
.AFF6  A5 65    LDA $65   ; get FAC1 mantissa 4
.AFF8  45 0B    EOR $0B   ; EOR high byte
.AFFA  85 08    STA $08   ; save it
.AFFC  20 FC BB JSR $BBFC   ; copy FAC2 to FAC1, get 2nd value in expression
.AFFF  20 BF B1 JSR $B1BF   ; evaluate integer expression, no sign check
.B002  A5 65    LDA $65   ; get FAC1 mantissa 4
.B004  45 0B    EOR $0B   ; EOR high byte
.B006  25 08    AND $08   ; AND with expression 1 high byte
.B008  45 0B    EOR $0B   ; EOR result high byte
.B00A  A8       TAY   ; save in Y
.B00B  A5 64    LDA $64   ; get FAC1 mantissa 3
.B00D  45 0B    EOR $0B   ; EOR low byte
.B00F  25 07    AND $07   ; AND with expression 1 low byte
.B011  45 0B    EOR $0B   ; EOR result low byte
.B013  4C 91 B3 JMP $B391   ; convert fixed integer AY to float FAC1 and return
```


## Commenti

### Original Disassembly (—)
- **$AFE9**: clear Y for AND
- **$AFEB**: set AND/OR invert value
- **$AFED**: evaluate integer expression, no sign check
- **$AFF0**: get FAC1 mantissa 3
- **$AFF2**: EOR low byte
- **$AFF4**: save it
- **$AFF6**: get FAC1 mantissa 4
- **$AFF8**: EOR high byte
- **$AFFA**: save it
- **$AFFC**: copy FAC2 to FAC1, get 2nd value in expression
- **$AFFF**: evaluate integer expression, no sign check
- **$B002**: get FAC1 mantissa 4
- **$B004**: EOR high byte
- **$B006**: AND with expression 1 high byte
- **$B008**: EOR result high byte
- **$B00A**: save in Y
- **$B00B**: get FAC1 mantissa 3
- **$B00D**: EOR low byte
- **$B00F**: AND with expression 1 low byte
- **$B011**: EOR result low byte
- **$B013**: convert fixed integer AY to float FAC1 and return

### Commodore-64-intern-Buch (Commodore)
- **$AFE9**: Flag fur AND
- **$AFEB**: Flag setzen
- **$AFED**: FAC nach INTEGER wandeln
- **$AFF0**: ersten Wert holen
- **$AFF2**: mit Flag verknüpfen
- **$AFF4**: und speichern
- **$AFF6**: zweiten Wert holen
- **$AFF8**: mit Flag verknüpfen
- **$AFFA**: und speichern
- **$AFFC**: ARG nach FAC
- **$AFFF**: FAC nach Integer
- **$B002**: zweites Byte holen
- **$B004**: mit Flag verknüpfen
- **$B006**: logische AND-Verknüpfung
- **$B008**: mit Flag verknüpfen
- **$B00A**: ins Y-Reg. retten
- **$B00B**: erstes Byte holen
- **$B00D**: mit Flag verknüpfen
- **$B00F**: logische AND-Verknüpfung
- **$B011**: mit Flag verknüpfen
- **$B013**: wieder in Fließkomma wandeln

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*