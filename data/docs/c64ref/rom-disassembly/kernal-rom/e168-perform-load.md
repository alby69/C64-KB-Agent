---
title: perform LOAD
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e168-load-befehl
- ece7-load
- f5ed-save
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $E168
  address_end: $E194
  symbol: perform-load
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E168**: flag load'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E168**: Load-Flag'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $E168 — perform LOAD

## Disassemblatura
```assembly
.E168  A9 00    LDA #$00   ; flag load
.E16A  85 0A    STA $0A   ; set load/verify flag
.E16C  20 D4 E1 JSR $E1D4   ; get parameters for LOAD/SAVE
.E16F  A5 0A    LDA $0A   ; get load/verify flag
.E171  A6 2B    LDX $2B   ; get start of memory low byte
.E173  A4 2C    LDY $2C   ; get start of memory high byte
.E175  20 D5 FF JSR $FFD5   ; load RAM from a device
.E178  B0 57    BCS $E1D1   ; if error go handle BASIC I/O error
.E17A  A5 0A    LDA $0A   ; get load/verify flag
.E17C  F0 17    BEQ $E195   ; branch if load
.E17E  A2 1C    LDX #$1C   ; error $1C, verify error
.E180  20 B7 FF JSR $FFB7   ; read I/O status word
.E183  29 10    AND #$10   ; mask for tape read error
.E185  D0 17    BNE $E19E   ; branch if no read error
.E187  A5 7A    LDA $7A   ; get the BASIC execute pointer low byte is this correct ?? won't this mean the "OK" prompt when doing a load from within a program ?
.E189  C9 02    CMP #$02
.E18B  F0 07    BEQ $E194   ; if ?? skip "OK" prompt
.E18D  A9 64    LDA #$64   ; set "OK" pointer low byte
.E18F  A0 A3    LDY #$A3   ; set "OK" pointer high byte
.E191  4C 1E AB JMP $AB1E   ; print null terminated string
.E194  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E168**: flag load
- **$E16A**: set load/verify flag
- **$E16C**: get parameters for LOAD/SAVE
- **$E16F**: get load/verify flag
- **$E171**: get start of memory low byte
- **$E173**: get start of memory high byte
- **$E175**: load RAM from a device
- **$E178**: if error go handle BASIC I/O error
- **$E17A**: get load/verify flag
- **$E17C**: branch if load
- **$E17E**: error $1C, verify error
- **$E180**: read I/O status word
- **$E183**: mask for tape read error
- **$E185**: branch if no read error
- **$E187**: get the BASIC execute pointer low byte is this correct ?? won't this mean the "OK" prompt when doing a load from within a program ?
- **$E18B**: if ?? skip "OK" prompt
- **$E18D**: set "OK" pointer low byte
- **$E18F**: set "OK" pointer high byte
- **$E191**: print null terminated string

### Commodore-64-intern-Buch (Commodore)
- **$E168**: Load-Flag
- **$E16A**: speichern
- **$E16C**: Parameter holen
- **$E16F**: Flag
- **$E171**: Startadresse gleich
- **$E173**: BASIC-Start
- **$E175**: Load-Routine
- **$E178**: Fehler ?
- **$E17A**: Load/Verify - Flag
- **$E17C**: Load ?
- **$E17E**: Offset für 'VERIFY ERROR'
- **$E180**: Status holen
- **$E183**: Fehler-Bit isolieren
- **$E185**: Statusbit gesetzt, dann Fehler
- **$E187**: muß HIGH-Byte $7B sein
- **$E189**: Test auf Direkt-Modus
- **$E18B**: ja, dann fertig
- **$E18D**: Zeiger auf
- **$E18F**: 'OK'
- **$E191**: ausgeben
- **$E194**: Rücksprung
- **$E195**: Status holen
- **$E198**: EOF-Bit löschen
- **$E19A**: kein Fehler
- **$E19C**: Offset für 'LOAD ERROR'
- **$E19E**: Fehlermeldung ausgeben
- **$E1A1**: Direkt-
- **$E1A3**: modus testen
- **$E1A5**: nein, dann weiter
- **$E1A7**: Endadresse gleich
- **$E1A9**: Rücksprung
- **$E1AB**: Zeiger auf
- **$E1AD**: 'READY'
- **$E1AF**: String ausgeben
- **$E1B2**: Programmzeilen neu binden, CLR
- **$E1B5**: CHRGET-Zeiger auf Programmstart
- **$E1B8**: Programmzeilen neu binden
- **$E1BB**: RESTORE, BASIC initialisieren

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*