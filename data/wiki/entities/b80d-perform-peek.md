---
id: b80d-perform-peek
type: entity
title: perform PEEK()
aliases:
- perform PEEK()
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b80d-perform-peek.md
  sha256: 0874aa8abfd113a37461de6ba12011031a3abcc8967782109362a796d427ebe4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b80d-perform-peek
---

# perform PEEK()



# $B80D — perform PEEK()

## Disassemblatura
```assembly
.B80D  A5 15    LDA $15   ; get line number high byte
.B80F  48       PHA   ; save line number high byte
.B810  A5 14    LDA $14   ; get line number low byte
.B812  48       PHA   ; save line number low byte
.B813  20 F7 B7 JSR $B7F7   ; convert FAC_1 to integer in temporary integer
.B816  A0 00    LDY #$00   ; clear index
.B818  B1 14    LDA ($14),Y   ; read byte
.B81A  A8       TAY   ; copy byte to A
.B81B  68       PLA   ; pull byte
.B81C  85 14    STA $14   ; restore line number low byte
.B81E  68       PLA   ; pull byte
.B81F  85 15    STA $15   ; restore line number high byte
.B821  4C A2 B3 JMP $B3A2   ; convert Y to byte in FAC_1 and return
```


## Commenti

### Original Disassembly (—)
- **$B80D**: get line number high byte
- **$B80F**: save line number high byte
- **$B810**: get line number low byte
- **$B812**: save line number low byte
- **$B813**: convert FAC_1 to integer in temporary integer
- **$B816**: clear index
- **$B818**: read byte
- **$B81A**: copy byte to A
- **$B81B**: pull byte
- **$B81C**: restore line number low byte
- **$B81E**: pull byte
- **$B81F**: restore line number high byte
- **$B821**: convert Y to byte in FAC_1 and return

### Commodore-64-intern-Buch (Commodore)
- **$B80D**: $14 und $15
- **$B80F**: in
- **$B810**: Stack
- **$B812**: sichern
- **$B813**: FAC nach Adressformat wandeln
- **$B816**: Zähler auf Null
- **$B818**: Peek-Wert holen
- **$B81A**: nach Y-Reg
- **$B81B**: $14 und $15
- **$B81C**: wieder
- **$B81E**: vom Stack
- **$B81F**: zurückholen
- **$B821**: Y nach Fließkommaformat

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B80D**: SAVE (LINNUM) ON STACK DURING PEEK
- **$B813**: GET ADDRESS PEEKING AT
- **$B818**: TAKE A QUICK LOOK
- **$B81A**: VALUE IN Y-REG
- **$B81B**: RESTORE LINNUM FROM STACK
- **$B821**: FLOAT Y-REG INTO FAC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b80d-perform-peek]]
