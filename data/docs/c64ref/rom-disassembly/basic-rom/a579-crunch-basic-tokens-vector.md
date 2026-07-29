---
title: crunch BASIC tokens vector
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a579-interpreter-code
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A579
  address_end: $A579
  symbol: crunch-basic-tokens-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A579**: do crunch BASIC tokens'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A579**: JMP $A57C'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A579**: normally A57C'
---

# $A579 — crunch BASIC tokens vector

## Disassemblatura
```assembly
.A579  6C 04 03 JMP ($0304)   ; do crunch BASIC tokens
```


## Commenti

### Original Disassembly (—)
- **$A579**: do crunch BASIC tokens

### Commodore-64-intern-Buch (Commodore)
- **$A579**: JMP $A57C
- **$A57C**: Zeiger setzen, erstes Zeichen
- **$A57E**: Wert für codierte Zeile
- **$A580**: Flag für Hochkomma
- **$A582**: Zeichen aus Puffer holen
- **$A585**: kein BASIC-Code ? kleiner 128
- **$A587**: Code für Pi ?
- **$A589**: Ja: dann speichern
- **$A58B**: Zeiger erhöhen
- **$A58C**: nächstes Zeichen überprüfen
- **$A58E**: ' ' Leerzeichen?
- **$A590**: Ja: dann speichern
- **$A592**: in Hochkomma-Flag speichern
- **$A594**: "'" Hochkomma?
- **$A596**: Ja: dann speichern
- **$A598**: Überprüft auf Bit 6
- **$A59A**: gesetzt: ASCII speichern
- **$A59C**: '?' Fragezeichen?
- **$A59E**: Nein: dann weiter prüfen
- **$A5A0**: PRINT-Code für ? laden
- **$A5A2**: und abspeichern
- **$A5A4**: Kleiner $30 ? (Code für 0)
- **$A5A6**: Ja: dann $A5AC
- **$A5A8**: Mit $3C vergleichen
- **$A5AA**: wenn größer, dann $A5C9
- **$A5AC**: Zeiger Zwischenspeichern
- **$A5AE**: Zähler für Tokentabelle
- **$A5B0**: initialisieren
- **$A5B3**: Zeiger auf Eingabepuffer
- **$A5B5**: zwischenspeichern
- **$A5B6**: X- und Y-Register
- **$A5B7**: um 1 erhöhen
- **$A5B8**: Zeichen aus Puffer laden
- **$A5BB**: Carry für Subtr. löschen
- **$A5BC**: Zeichen mit Befehlswort vergleichen
- **$A5BF**: Gefunden? Ja: nächstes Zeich.
- **$A5C1**: mit $80 (128) vergleichen
- **$A5C3**: Befehl nicht gefunden: $A5F5
- **$A5C5**: BASIC-Code gleich Zähler +$80
- **$A5C7**: Zeiger auf cod. Zeile holen
- **$A5CA**: Zeiger erhöhen
- **$A5CB**: BASIC-Code speichern
- **$A5CE**: und Statusregister setzen
- **$A5D1**: =0 (Ende): dann fertig
- **$A5D3**: Carry setzen (Subtraktion)
- **$A5D4**: ':' Trennzeichen?
- **$A5D6**: Ja: dann $A5DC
- **$A5D8**: DATA-Code ?
- **$A5DA**: Nein: Speichern überspringen
- **$A5DC**: nach Hochkomma-Flag speichern
- **$A5DE**: Carry setzen
- **$A5DF**: REM-Code ?
- **$A5E1**: Nein: zum Schleifenanfang
- **$A5E3**: 0 in Hochkomma-Flag
- **$A5E5**: nächstes Zeichen holen
- **$A5E8**: =0 (Ende)? Ja: dann $A5C9
- **$A5EA**: Als ASCII speichern?
- **$A5EC**: Nein: dann $A5C9
- **$A5EE**: Zeiger erhöhen
- **$A5EF**: Code abspeichern
- **$A5F2**: Zeiger erhöhen
- **$A5F3**: Zum Schleifenanfang
- **$A5F5**: Zeiger wieder auf Eingabep.
- **$A5F7**: Suchzähler erhöhen
- **$A5F9**: Zähler erhöhen
- **$A5FA**: nächsten Befehl suchen
- **$A5FD**: Gefunden? Nein: weitersuchen
- **$A5FF**: Ende der Tabelle?
- **$A602**: Nein: dann weiter
- **$A604**: nächstes Zeichen holen
- **$A607**: kleiner $80? Ja: $A5C7
- **$A609**: im Eingabepuffer speichern
- **$A60C**: CHRGET-Zeiger zurücksetzen
- **$A60E**: Zeiger auf Eingabepuffer -1
- **$A610**: setzen (LOW)
- **$A612**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$A579**: normally A57C

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*