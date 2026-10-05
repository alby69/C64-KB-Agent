---
id: e8cb-set-the-colour-code-enter-with-the-colour-character-in-a-if-a-does-not-contain-a
type: entity
title: set the colour code. enter with the colour character in A. if A does not contain
  a
aliases:
- set the colour code. enter with the colour character in A. if A does not contain
  a
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e8cb-set-the-colour-code-enter-with-the-colour-character-in-a-if-a-does-not-contain-a.md
  sha256: 74e6178b9b86cb941e249cf0aee9006ff870652b2df2b52bd00a92ad8afb508d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e8cb-set-the-colour-code-enter-with-the-colour-character-in-a-if-a-does-not-contain-a
---

# set the colour code. enter with the colour character in A. if A does not contain a



# $E8CB — set the colour code. enter with the colour character in A. if A does not contain a

## Disassemblatura
```assembly
.E8CB  A2 0F    LDX #$0F   ; set the colour code count
.E8CD  DD DA E8 CMP $E8DA,X   ; compare the character with a table code
.E8D0  F0 04    BEQ $E8D6   ; if a match go save the colour and exit
.E8D2  CA       DEX   ; else decrement the index
.E8D3  10 F8    BPL $E8CD   ; loop if more to do
.E8D5  60       RTS
.E8D6  8E 86 02 STX $0286   ; save the current colour code
.E8D9  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E8CB**: set the colour code count
- **$E8CD**: compare the character with a table code
- **$E8D0**: if a match go save the colour and exit
- **$E8D2**: else decrement the index
- **$E8D3**: loop if more to do
- **$E8D6**: save the current colour code

### Commodore-64-intern-Buch (Commodore)
- **$E8CB**: Anzahl der Kodes
- **$E8CD**: mit Farbcodetabelle vergleichen
- **$E8D0**: wenn gefunden, dann farbe setzen
- **$E8D2**: nächster Farbcode
- **$E8D3**: schon alle ?
- **$E8D5**: Rücksprung
- **$E8D6**: Farbcode setzen
- **$E8D9**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E8CB**: 16 values to be tested
- **$E8CD**: compare with colour code table
- **$E8D0**: found, jump
- **$E8D2**: next colour in table
- **$E8D3**: till all 16 are tested
- **$E8D5**: if not found, return
- **$E8D6**: if found, store code in COLOR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e8cb-set-the-colour-code-enter-with-the-colour-character-in-a-if-a-does-not-contain-a]]
