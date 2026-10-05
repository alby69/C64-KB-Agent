---
id: fe47-nmi-handler
type: entity
title: NMI handler
aliases:
- NMI handler
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe47-nmi-handler.md
  sha256: ea337855f03664a41374d207874615688f17f2fb1208264f750c335485b3c6ca
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe47-nmi-handler
---

# NMI handler



# $FE47 — NMI handler

## Disassemblatura
```assembly
.FE47  48       PHA   ; save A
.FE48  8A       TXA   ; copy X
.FE49  48       PHA   ; save X
.FE4A  98       TYA   ; copy Y
.FE4B  48       PHA   ; save Y
.FE4C  A9 7F    LDA #$7F   ; disable all interrupts
.FE4E  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.FE51  AC 0D DD LDY $DD0D   ; save VIA 2 ICR
.FE54  30 1C    BMI $FE72
.FE56  20 02 FD JSR $FD02   ; scan for autostart ROM at $8000
.FE59  D0 03    BNE $FE5E   ; branch if no autostart ROM
.FE5B  6C 02 80 JMP ($8002)   ; else do autostart ROM break entry
.FE5E  20 BC F6 JSR $F6BC   ; increment real time clock
.FE61  20 E1 FF JSR $FFE1   ; scan stop key
.FE64  D0 0C    BNE $FE72   ; if not [STOP] restore registers and exit interrupt
```


## Commenti

### Original Disassembly (—)
- **$FE47**: save A
- **$FE48**: copy X
- **$FE49**: save X
- **$FE4A**: copy Y
- **$FE4B**: save Y
- **$FE4C**: disable all interrupts
- **$FE4E**: save VIA 2 ICR
- **$FE51**: save VIA 2 ICR
- **$FE56**: scan for autostart ROM at $8000
- **$FE59**: branch if no autostart ROM
- **$FE5B**: else do autostart ROM break entry
- **$FE5E**: increment real time clock
- **$FE61**: scan stop key
- **$FE64**: if not [STOP] restore registers and exit interrupt

### Marko Mäkelä (Marko Mäkelä)
- **$FE5B**: cartridge warm start

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fe47-nmi-handler]]
