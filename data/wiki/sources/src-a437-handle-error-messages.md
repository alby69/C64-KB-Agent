---
id: src-a437-handle-error-messages
type: source
title: 'Source Summary: handle error messages'
aliases:
- handle error messages
- a437-handle-error-messages.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a437-handle-error-messages.md
  sha256: bbfbb6b3ef86aacfa2533865745e18b4a2002aff61e4aea9dca320d11c2aa55e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: handle error messages

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a437-handle-error-messages.md`
**SHA256**: `bbfbb6b3ef86aacfa2533865745e18b4a2002aff61e4aea9dca320d11c2aa55e`

## Summary



# $A437 — handle error messages

## Disassemblatura
```assembly
.A437  6C 00 03 JMP ($0300)   ; normally A43A
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A437**: Zum BASIC-Warmstart ($E38B)

### Marko Mäkelä (Marko Mäkelä)
- **$A437**: normally A43A

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A483**: READ A LINE
- **$A486**: SET UP CHRGET TO SCAN THE LINE
- **$A48E**: EMPTY LINE
- **$A490**: $FF IN HI-BYTE OF CURLIN MEANS
- **$A492**: WE ARE IN DIRECT MODE
- **$A49...
