---
id: a909-scan-for-next-basic-line
type: entity
title: scan for next BASIC line
aliases:
- scan for next BASIC line
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a909-scan-for-next-basic-line.md
  sha256: d87a2fa6c0824db75aa27ce22b6f6f9e52935c0a85c3bb3a2cc8323749f9ad63
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a909-scan-for-next-basic-line
---

# scan for next BASIC line



# $A909 — scan for next BASIC line

## Disassemblatura
```assembly
.A909  A2 00    LDX #$00   ; set alternate search character = [EOL]
.A90B  86 07    STX $07   ; store alternate search character
.A90D  A0 00    LDY #$00   ; set search character = [EOL]
.A90F  84 08    STY $08   ; save the search character
.A911  A5 08    LDA $08   ; get search character
.A913  A6 07    LDX $07   ; get alternate search character
.A915  85 07    STA $07   ; make search character = alternate search character
.A917  86 08    STX $08   ; make alternate search character = search character
.A919  B1 7A    LDA ($7A),Y   ; get BASIC byte
.A91B  F0 E8    BEQ $A905   ; exit if null [EOL]
.A91D  C5 08    CMP $08   ; compare with search character
.A91F  F0 E4    BEQ $A905   ; exit if found
.A921  C8       INY   ; else increment index
.A922  C9 22    CMP #$22   ; compare current character with open quote
.A924  D0 F3    BNE $A919   ; if found go swap search character for alternate search character
.A926  F0 E9    BEQ $A911   ; loop for next character, branch always
```


## Commenti

### Original Disassembly (—)
- **$A909**: set alternate search character = [EOL]
- **$A90B**: store alternate search character
- **$A90D**: set search character = [EOL]
- **$A90F**: save the search character
- **$A911**: get search character
- **$A913**: get alternate search character
- **$A915**: make search character = alternate search character
- **$A917**: make alternate search character = search character
- **$A919**: get BASIC byte
- **$A91B**: exit if null [EOL]
- **$A91D**: compare with search character
- **$A91F**: exit if found
- **$A921**: else increment index
- **$A922**: compare current character with open quote
- **$A924**: if found go swap search character for alternate search character
- **$A926**: loop for next character, branch always

### Marko Mäkelä (Marko Mäkelä)
- **$A922**: quote mark

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a909-scan-for-next-basic-line]]
