---
id: f5af-print-searching
type: entity
title: print "Searching..."
aliases:
- print "Searching..."
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5af-print-searching.md
  sha256: 346bc5682394ffba1b22be0775471b5606c5458fbc0db122401df1bec0033c90
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f5af-print-searching
---

# print "Searching..."



# $F5AF — print "Searching..."

## Disassemblatura
```assembly
.F5AF  A5 9D    LDA $9D   ; get message mode flag
.F5B1  10 1E    BPL $F5D1   ; exit if control messages off
.F5B3  A0 0C    LDY #$0C   ; index to "SEARCHING "
.F5B5  20 2F F1 JSR $F12F   ; display kernel I/O message
.F5B8  A5 B7    LDA $B7   ; get file name length
.F5BA  F0 15    BEQ $F5D1   ; exit if null name
.F5BC  A0 17    LDY #$17   ; else index to "FOR "
.F5BE  20 2F F1 JSR $F12F   ; display kernel I/O message
```


## Commenti

### Original Disassembly (—)
- **$F5AF**: get message mode flag
- **$F5B1**: exit if control messages off
- **$F5B3**: index to "SEARCHING "
- **$F5B5**: display kernel I/O message
- **$F5B8**: get file name length
- **$F5BA**: exit if null name
- **$F5BC**: else index to "FOR "
- **$F5BE**: display kernel I/O message

### Commodore-64-intern-Buch (Commodore)
- **$F5AF**: Direkt-Modus-Flag laden
- **$F5B1**: verzweige wenn Bit 7 =0 (Programm-Mode)
- **$F5B3**: Offset für 'SEARCHING'
- **$F5B5**: Meldung ausgeben
- **$F5B8**: Länge des Filenamens
- **$F5BA**: gleich Null, dann fertig
- **$F5BC**: Offset für 'FOR'
- **$F5BE**: Meldung ausgeben
- **$F5C1**: Länge des Filenamens
- **$F5C3**: gleich Null, dann fertig
- **$F5C5**: Zähler setzen
- **$F5C7**: Filenamen holen
- **$F5C9**: und ausgeben
- **$F5CC**: Zähler erhöhen
- **$F5CD**: mit Länge des Filenamens ver- gleichen
- **$F5CF**: verzweige wenn noch nicht alle Buchstaben
- **$F5D1**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F5AF**: MSGFLG, direct or program mode?
- **$F5B1**: program mode, don´t print, exit
- **$F5B5**: print "SEARCHING"
- **$F5B8**: FNLEN, length of current filename
- **$F5BA**: no name, exit
- **$F5BE**: print "FOR"

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f5af-print-searching]]
