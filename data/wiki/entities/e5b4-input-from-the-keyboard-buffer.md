---
id: e5b4-input-from-the-keyboard-buffer
type: entity
title: input from the keyboard buffer
aliases:
- input from the keyboard buffer
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e5b4-input-from-the-keyboard-buffer.md
  sha256: 52a6420baae7d3f8b24943cd1f092609600672e246a59d193f000f41d27a1354
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e5b4-input-from-the-keyboard-buffer
---

# input from the keyboard buffer



# $E5B4 — input from the keyboard buffer

## Disassemblatura
```assembly
.E5B4  AC 77 02 LDY $0277   ; get the current character from the buffer
.E5B7  A2 00    LDX #$00   ; clear the index
.E5B9  BD 78 02 LDA $0278,X   ; get the next character,X from the buffer
.E5BC  9D 77 02 STA $0277,X   ; save it as the current character,X in the buffer
.E5BF  E8       INX   ; increment the index
.E5C0  E4 C6    CPX $C6   ; compare it with the keyboard buffer index
.E5C2  D0 F5    BNE $E5B9   ; loop if more to do
.E5C4  C6 C6    DEC $C6   ; decrement keyboard buffer index
.E5C6  98       TYA   ; copy the key to A
.E5C7  58       CLI   ; enable the interrupts
.E5C8  18       CLC   ; flag got byte
.E5C9  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E5B4**: get the current character from the buffer
- **$E5B7**: clear the index
- **$E5B9**: get the next character,X from the buffer
- **$E5BC**: save it as the current character,X in the buffer
- **$E5BF**: increment the index
- **$E5C0**: compare it with the keyboard buffer index
- **$E5C2**: loop if more to do
- **$E5C4**: decrement keyboard buffer index
- **$E5C6**: copy the key to A
- **$E5C7**: enable the interrupts
- **$E5C8**: flag got byte

### Commodore-64-intern-Buch (Commodore)
- **$E5B4**: erstes Zeichen holen
- **$E5B7**: Zähler auf Null
- **$E5B9**: Puffer nach
- **$E5BC**: vorne aufrücken
- **$E5BF**: Zähler erhöhen
- **$E5C0**: mit Anzahl der
- **$E5C2**: Zeichen vergleichen
- **$E5C4**: Zeichenzahl erniedrigen
- **$E5C6**: Zeichen in Akku holen
- **$E5C7**: Interrupt freigeben
- **$E5C8**: Carry löschen
- **$E5C9**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E5B4**: read KEYD, first character in keyboard buffer queue
- **$E5B9**: overwrite with next in queue
- **$E5C0**: compare with NDX, number of characters in queue
- **$E5C2**: till all characters are moved
- **$E5C4**: decrement NDX
- **$E5C6**: transfer read character to (A)
- **$E5C7**: enable interrupt

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e5b4-input-from-the-keyboard-buffer]]
