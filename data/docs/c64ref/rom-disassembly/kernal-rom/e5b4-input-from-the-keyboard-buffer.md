---
title: input from the keyboard buffer
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
- e5b4-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E5B4
  address_end: $E5C9
  symbol: input-from-the-keyboard-buffer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E5B4**: get the current character from the buffer'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E5B4**: erstes Zeichen holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E5B4**: read KEYD, first character in keyboard buffer queue'
---

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