---
id: a906-scan-for-next-basic-statement-or-eol
type: entity
title: scan for next BASIC statement ([:] or [EOL])
aliases:
- scan for next BASIC statement ([:] or [EOL])
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a906-scan-for-next-basic-statement-or-eol.md
  sha256: d17f58f488e7219a125f4161822bf8e15504059e820a47676d3ff51347be5ce5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a906-scan-for-next-basic-statement-or-eol
---

# scan for next BASIC statement ([:] or [EOL])



# $A906 — scan for next BASIC statement ([:] or [EOL])

## Disassemblatura
```assembly
.A906  A2 3A    LDX #$3A   ; set look for character = ":"
.A908  2C       .BYTE $2C   ; makes next line BIT $00A2
```


## Commenti

### Original Disassembly (—)
- **$A906**: set look for character = ":"
- **$A908**: makes next line BIT $00A2

### Commodore-64-intern-Buch (Commodore)
- **$A906**: ':' Doppelpunkt
- **$A909**: $0 Zeilenende
- **$A90B**: als Suchzeichen
- **$A90D**: Zähler
- **$A90F**: initialisieren
- **$A911**: Speicherzelle $7
- **$A913**: gesuchtes Zeichen
- **$A915**: mit $8
- **$A917**: vertauschen
- **$A919**: Zeichen holen
- **$A91B**: Zeilenende, dann fertig
- **$A91D**: = Suchzeichen?
- **$A91F**: ja: $A905
- **$A921**: Zeiger erhöhen
- **$A922**: "" Hochkomma?
- **$A924**: nein: $A919
- **$A926**: sonst $7 und $8 vertauschen

### Marko Mäkelä (Marko Mäkelä)
- **$A906**: colon

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A906**: GET OFFSET IN Y TO EOL OR ":"
- **$A908**: FAKE
- **$A909**: TO EOL ONLY
- **$A911**: TRICK TO COUNT QUOTE PARITY
- **$A91B**: END OF LINE
- **$A91F**: COLON IF LOOKING FOR COLONS
- **$A926**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a906-scan-for-next-basic-statement-or-eol]]
