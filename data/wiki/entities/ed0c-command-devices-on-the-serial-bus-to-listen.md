---
id: ed0c-command-devices-on-the-serial-bus-to-listen
type: entity
title: command devices on the serial bus to LISTEN
aliases:
- command devices on the serial bus to LISTEN
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ed0c-command-devices-on-the-serial-bus-to-listen.md
  sha256: 503193cfa87b97e6cf4b26f747344812810723022d1f95df92e1637e22bea89a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ed0c-command-devices-on-the-serial-bus-to-listen
---

# command devices on the serial bus to LISTEN



# $ED0C — command devices on the serial bus to LISTEN

## Disassemblatura
```assembly
.ED0C  09 20    ORA #$20   ; OR with the LISTEN command
.ED0E  20 A4 F0 JSR $F0A4   ; check RS232 bus idle
```


## Commenti

### Original Disassembly (—)
- **$ED0C**: OR with the LISTEN command
- **$ED0E**: check RS232 bus idle

### Commodore-64-intern-Buch (Commodore)
- **$ED0C**: Bit für Listen setzen
- **$ED0E**: Ende der RS 232 Übertragung abwarten
- **$ED11**: Akku merken
- **$ED12**: Noch Zeichen im Puffer ?
- **$ED14**: verzweige wenn nein
- **$ED16**: Carry setzen
- **$ED17**: Bit für EOI setzen
- **$ED19**: Byte auf IEC-Bus ausgeben
- **$ED1C**: Flag für Zeichen im Puffer löschen
- **$ED1E**: Flag für EOI löschen
- **$ED20**: Akku wiederholen und
- **$ED21**: im Puffer speichern
- **$ED23**: Interruptflag setzen
- **$ED24**: DATA auf LOW setzen
- **$ED27**: Akku kann nicht $3F sein
- **$ED29**: unbedingter Sprung
- **$ED2B**: CLOCK auf LOW setzen
- **$ED2E**: Port A laden
- **$ED31**: ATN HIGH setzen und
- **$ED33**: ausgeben
- **$ED36**: InterruptfLag setzen
- **$ED37**: CLOCK auf HIGH setzen
- **$ED3A**: DATA auf LOW setzen
- **$ED3D**: eine Millisekunde warten

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ed0c-command-devices-on-the-serial-bus-to-listen]]
