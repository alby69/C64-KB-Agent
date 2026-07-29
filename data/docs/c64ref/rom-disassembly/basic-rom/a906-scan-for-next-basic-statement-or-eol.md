---
title: scan for next BASIC statement ([:] or [EOL])
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a906-trennzeichens-finden
- bit
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A906
  address_end: $A908
  symbol: scan-for-next-basic-statement-or-eol
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A906**: set look for character = ":"'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A906**: '':'' Doppelpunkt'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A906**: colon'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A906**: GET OFFSET IN Y TO EOL OR ":"'
---

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