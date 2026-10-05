---
id: aa68-move-descriptor-into-variable
type: entity
title: move descriptor into variable
aliases:
- move descriptor into variable
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aa68-move-descriptor-into-variable.md
  sha256: df37543d3ec43932e8784e8f53aee827d67325e11d842b594dc6ca69bc78a615
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-aa68-move-descriptor-into-variable
---

# move descriptor into variable



# $AA68 — move descriptor into variable

## Disassemblatura
```assembly
.AA68  85 50    STA $50
.AA6A  84 51    STY $51
.AA6C  20 DB B6 JSR $B6DB
.AA6F  A0 00    LDY #$00
.AA71  B1 50    LDA ($50),Y
.AA73  91 49    STA ($49),Y
.AA75  C8       INY
.AA76  B1 50    LDA ($50),Y
.AA78  91 49    STA ($49),Y
.AA7A  C8       INY
.AA7B  B1 50    LDA ($50),Y
.AA7D  91 49    STA ($49),Y
.AA7F  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-aa68-move-descriptor-into-variable]]
