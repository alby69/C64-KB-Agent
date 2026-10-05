---
id: f014-send-byte-to-the-rs232-buffer
type: entity
title: send byte to the RS232 buffer
aliases:
- send byte to the RS232 buffer
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f014-send-byte-to-the-rs232-buffer.md
  sha256: 33415c36bf11e8bb9af77b5f39c682641830a7d1b7292812644ede22507209db
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f014-send-byte-to-the-rs232-buffer
---

# send byte to the RS232 buffer



# $F014 — send byte to the RS232 buffer

## Disassemblatura
```assembly
.F014  20 28 F0 JSR $F028   ; setup for RS232 transmit send byte to the RS232 buffer, no setup
.F017  AC 9E 02 LDY $029E   ; get index to Tx buffer end
.F01A  C8       INY   ; + 1
.F01B  CC 9D 02 CPY $029D   ; compare with index to Tx buffer start
.F01E  F0 F4    BEQ $F014   ; loop while buffer full
.F020  8C 9E 02 STY $029E   ; set index to Tx buffer end
.F023  88       DEY   ; index to available buffer byte
.F024  A5 9E    LDA $9E   ; read the RS232 character buffer
.F026  91 F9    STA ($F9),Y   ; save the byte to the buffer
```


## Commenti

### Original Disassembly (—)
- **$F014**: setup for RS232 transmit send byte to the RS232 buffer, no setup
- **$F017**: get index to Tx buffer end
- **$F01A**: + 1
- **$F01B**: compare with index to Tx buffer start
- **$F01E**: loop while buffer full
- **$F020**: set index to Tx buffer end
- **$F023**: index to available buffer byte
- **$F024**: read the RS232 character buffer
- **$F026**: save the byte to the buffer

### Commodore-64-intern-Buch (Commodore)
- **$F014**: falls erforderlich Übertragung starten
- **$F017**: Zeiger auf Ausgabepuffer laden
- **$F01A**: und erhöhen
- **$F01B**: und mit Lesezeiger vergleichen
- **$F01E**: Puffer voll, dann warten
- **$F020**: neuen Wert für Schreibzeiger merken
- **$F023**: und wieder normalisieren
- **$F024**: auszugebendes Byte holen und
- **$F026**: in Puffer schreiben
- **$F028**: RS 232 NMI Status laden
- **$F02B**: Bit 0 testen (läuft Sendebetrieb)
- **$F02C**: verzweige wenn ja
- **$F02E**: Bitwert für Timer starten
- **$F030**: Timer A starten
- **$F033**: Timer für
- **$F036**: Sende-Baud-Rate
- **$F039**: neu
- **$F03C**: setzen
- **$F03F**: Code für Timer-Unterlauf NMI Timer A
- **$F041**: in IC-Register schreiben
- **$F044**: CTS und DSR prüfen und Übertragung freigeben
- **$F047**: Bitwert Timer A starten
- **$F049**: Timer A starten
- **$F04C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f014-send-byte-to-the-rs232-buffer]]
