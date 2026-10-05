---
id: fec2-baud-rate-word-is-calculated-from
type: entity
title: baud rate word is calculated from ..
aliases:
- baud rate word is calculated from ..
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fec2-baud-rate-word-is-calculated-from.md
  sha256: 65a8d423e74f7c66fc6f5d2356b82715ba59f693a47a1247ae359ce0bd036138
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fec2-baud-rate-word-is-calculated-from
---

# baud rate word is calculated from ..



# $FEC2 — baud rate word is calculated from ..

## Disassemblatura
```assembly
.FEC2  C1 27   ; 50   baud   1027700
.FEC4  3E 1A   ; 75   baud   1022700
.FEC6  C5 11   ; 110   baud   1022780
.FEC8  74 0E   ; 134.5 baud   1022200
.FECA  ED 0C   ; 150   baud   1022700
.FECC  45 06   ; 300   baud   1023000
.FECE  F0 02   ; 600   baud   1022400
.FED0  46 01   ; 1200   baud   1022400
.FED2  B8 00   ; 1800   baud   1022400
.FED4  71 00   ; 2400   baud   1022400
```


## Commenti

### Original Disassembly (—)
- **$FEC2**: 50   baud   1027700
- **$FEC4**: 75   baud   1022700
- **$FEC6**: 110   baud   1022780
- **$FEC8**: 134.5 baud   1022200
- **$FECA**: 150   baud   1022700
- **$FECC**: 300   baud   1023000
- **$FECE**: 600   baud   1022400
- **$FED0**: 1200   baud   1022400
- **$FED2**: 1800   baud   1022400
- **$FED4**: 2400   baud   1022400

### Commodore-64-intern-Buch (Commodore)
- **$FEC2**: $27C1 = 10177       50 Baud
- **$FEC4**: $1A3E =  6718       75 Baud
- **$FEC6**: $11C5 =  4549      110 Baud
- **$FEC8**: $0E74 =  3700      134.5 Baud
- **$FECA**: $0CED =  3309      150 Baud
- **$FECC**: $0645 =  1605      300 Baud
- **$FECE**: $02F0 =   752      600 Baud
- **$FED0**: $0146 =   326     1200 Baud
- **$FED2**: $00B8 =   184     1800 Baud
- **$FED4**: $0071 =   113     2400 Baud

### Marko Mäkelä (Marko Mäkelä)
- **$FEC2**: 50
- **$FEC4**: 75
- **$FEC6**: 110
- **$FEC8**: 134.5
- **$FECA**: 150
- **$FECC**: 300
- **$FECE**: 600
- **$FED0**: 1200
- **$FED2**: 1800
- **$FED4**: 2400

### Magnus Nyman (Magnus Nyman)
- **$FEC2**: 50 baud
- **$FEC4**: 75 baud
- **$FEC6**: 110 baud
- **$FEC8**: 134.5 baud
- **$FECA**: 150 baud
- **$FECC**: 300 baud
- **$FECE**: 600 baud
- **$FED0**: 1200 baud
- **$FED2**: (1800) 2400 baud
- **$FED4**: 2400 baud

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fec2-baud-rate-word-is-calculated-from]]
