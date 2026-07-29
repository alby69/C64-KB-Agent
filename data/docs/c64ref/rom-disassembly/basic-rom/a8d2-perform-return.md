---
title: perform RETURN
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
- a8d2-basic-befehl-return
- a8eb-remove-gosub-block-from-stack
- bit
- return
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A8D2
  address_end: $A8F6
  symbol: perform-return
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A8D2**: exit if following token to allow syntax error'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A8D2**: Kein Trennzeichen: SYNTAX ERR'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A8D8**: TO CANCEL FOR/NEXT IN SUB'
---

# $A8D2 — perform RETURN

## Disassemblatura
```assembly
.A8D2  D0 FD    BNE $A8D1   ; exit if following token to allow syntax error
.A8D4  A9 FF    LDA #$FF   ; set byte so no match possible
.A8D6  85 4A    STA $4A   ; save FOR/NEXT variable pointer high byte
.A8D8  20 8A A3 JSR $A38A   ; search the stack for FOR or GOSUB activity, get token off stack
.A8DB  9A       TXS   ; correct the stack
.A8DC  C9 8D    CMP #$8D   ; compare with GOSUB token
.A8DE  F0 0B    BEQ $A8EB   ; if matching GOSUB go continue RETURN
.A8E0  A2 0C    LDX #$0C   ; else error code $04, return without gosub error
.A8E2  2C       .BYTE $2C   ; makes next line BIT $11A2
.A8E3  A2 11    LDX #$02   ; error code $11, undefined statement error
.A8E5  4C 37 A4 JMP $A437   ; do error #X then warm start
.A8E8  4C 08 AF JMP $AF08   ; do syntax error then warm start was matching GOSUB token
.A8EB  68       PLA   ; dump token byte
.A8EC  68       PLA   ; pull return line low byte
.A8ED  85 39    STA $39   ; save current line number low byte
.A8EF  68       PLA   ; pull return line high byte
.A8F0  85 3A    STA $3A   ; save current line number high byte
.A8F2  68       PLA   ; pull return address low byte
.A8F3  85 7A    STA $7A   ; save BASIC execute pointer low byte
.A8F5  68       PLA   ; pull return address high byte
.A8F6  85 7B    STA $7B   ; save BASIC execute pointer high byte
```


## Commenti

### Original Disassembly (—)
- **$A8D2**: exit if following token to allow syntax error
- **$A8D4**: set byte so no match possible
- **$A8D6**: save FOR/NEXT variable pointer high byte
- **$A8D8**: search the stack for FOR or GOSUB activity, get token off stack
- **$A8DB**: correct the stack
- **$A8DC**: compare with GOSUB token
- **$A8DE**: if matching GOSUB go continue RETURN
- **$A8E0**: else error code $04, return without gosub error
- **$A8E2**: makes next line BIT $11A2
- **$A8E3**: error code $11, undefined statement error
- **$A8E5**: do error #X then warm start
- **$A8E8**: do syntax error then warm start was matching GOSUB token
- **$A8EB**: dump token byte
- **$A8EC**: pull return line low byte
- **$A8ED**: save current line number low byte
- **$A8EF**: pull return line high byte
- **$A8F0**: save current line number high byte
- **$A8F2**: pull return address low byte
- **$A8F3**: save BASIC execute pointer low byte
- **$A8F5**: pull return address high byte
- **$A8F6**: save BASIC execute pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$A8D2**: Kein Trennzeichen: SYNTAX ERR
- **$A8D4**: Wert laden und
- **$A8D6**: FOR-NEXT-ZEIGER neu setzen
- **$A8D8**: GOSUB-Datensatz suchen
- **$A8DC**: 'GOSUB'-Code?
- **$A8DE**: ja: $A8E8
- **$A8E0**: Nr für 'return without gosub’
- **$A8E2**: BIT-Befehl um folgenden Befehl auszulassen
- **$A8E3**: Nr für 'undef'd statement'
- **$A8E5**: Fehlermeldung ausgeben
- **$A8E8**: 'syntax error' ausgeben
- **$A8EB**: GOSUB-Code vom Stapel holen
- **$A8EC**: Zeilennummer (LOW) wieder-
- **$A8ED**: holen und abspeichern
- **$A8EF**: Zeilennummer (HIGH) holen
- **$A8F0**: und abspeichern
- **$A8F2**: Programmzeiger (LOW) wieder-
- **$A8F3**: holen und abspeichern
- **$A8F5**: Programmzeiger (HIGH) holen
- **$A8F6**: abspeichern

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A8D8**: TO CANCEL FOR/NEXT IN SUB
- **$A8DC**: LAST GOSUB FOUND?
- **$A8E2**: FAKE
- **$A8EB**: DISCARD GOSUB TOKEN
- **$A8ED**: PULL LINE #
- **$A8F3**: PULL TXTPTR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*