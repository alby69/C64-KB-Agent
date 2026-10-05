---
id: e691-insert-uppercasegraphic-character
type: entity
title: insert uppercase/graphic character
aliases:
- insert uppercase/graphic character
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e691-insert-uppercasegraphic-character.md
  sha256: 31c2a9a7548d217752da4858211d22167bd6ef14df61d32f97e32f0eb89c6e0f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e691-insert-uppercasegraphic-character
---

# insert uppercase/graphic character



# $E691 — insert uppercase/graphic character

## Disassemblatura
```assembly
.E691  09 40    ORA #$40   ; change to uppercase/graphic
.E693  A6 C7    LDX $C7   ; get the reverse flag
.E695  F0 02    BEQ $E699   ; branch if not reverse else .. insert reversed character
.E697  09 80    ORA #$80   ; reverse character
.E699  A6 D8    LDX $D8   ; get the insert count
.E69B  F0 02    BEQ $E69F   ; branch if none
.E69D  C6 D8    DEC $D8   ; else decrement the insert count
.E69F  AE 86 02 LDX $0286   ; get the current colour code
.E6A2  20 13 EA JSR $EA13   ; print character A and colour X
.E6A5  20 B6 E6 JSR $E6B6   ; advance the cursor restore the registers, set the quote flag and exit
.E6A8  68       PLA   ; pull Y
.E6A9  A8       TAY   ; restore Y
.E6AA  A5 D8    LDA $D8   ; get the insert count
.E6AC  F0 02    BEQ $E6B0   ; skip quote flag clear if inserts to do
.E6AE  46 D4    LSR $D4   ; clear cursor quote flag, $xx = quote, $00 = no quote
.E6B0  68       PLA   ; pull X
.E6B1  AA       TAX   ; restore X
.E6B2  68       PLA   ; restore A
.E6B3  18       CLC
.E6B4  58       CLI   ; enable the interrupts
.E6B5  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E691**: change to uppercase/graphic
- **$E693**: get the reverse flag
- **$E695**: branch if not reverse else .. insert reversed character
- **$E697**: reverse character
- **$E699**: get the insert count
- **$E69B**: branch if none
- **$E69D**: else decrement the insert count
- **$E69F**: get the current colour code
- **$E6A2**: print character A and colour X
- **$E6A5**: advance the cursor restore the registers, set the quote flag and exit
- **$E6A8**: pull Y
- **$E6A9**: restore Y
- **$E6AA**: get the insert count
- **$E6AC**: skip quote flag clear if inserts to do
- **$E6AE**: clear cursor quote flag, $xx = quote, $00 = no quote
- **$E6B0**: pull X
- **$E6B1**: restore X
- **$E6B2**: restore A
- **$E6B4**: enable the interrupts

### Commodore-64-intern-Buch (Commodore)
- **$E691**: Bit 6 im Zeichen setzen
- **$E693**: RVS ?
- **$E695**: Umwandlung in Bildschirmcode
- **$E697**: ja, dann Bit 7 setzen
- **$E699**: wenn Einfügzähler Null,
- **$E69B**: dann zu $E69F
- **$E69D**: Zähler erniedrigen
- **$E69F**: Farbkode
- **$E6A2**: Zeichen in Bildschirm-RAM schreiben
- **$E6A5**: Tabelle der Zeilenanfänge aktualisieren
- **$E6A8**: Y-Reg
- **$E6A9**: aus Stack
- **$E6AA**: wenn Einfügzähler Null,
- **$E6AC**: dann zu $E6B0
- **$E6AE**: Hochkommamodus löschen
- **$E6B0**: X-Reg
- **$E6B1**: aus Stack
- **$E6B2**: Akku aus Stack
- **$E6B3**: Carry löschen
- **$E6B4**: Interrupt freigeben
- **$E6B5**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E693**: test RVS, flag for reversed characters
- **$E695**: nope
- **$E697**: set bit 7 to reverse character
- **$E699**: test INSRT, flag for insert mode
- **$E69B**: nope
- **$E69D**: decrement number of characters left to insert
- **$E69F**: get COLOR, current character colour code
- **$E6A2**: print to screen
- **$E6A5**: advance cursor
- **$E6AA**: INSRT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e691-insert-uppercasegraphic-character]]
