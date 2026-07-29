---
title: schreiben
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 029f-irqtmp
- f86b-schreiben
- f875-common-code-for-cassette-read-and-write
- fc6a-schreiben
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F86B
  address_end: $F8BD
  symbol: schreiben
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F86B**: wartet auf Record & Play Taste'
---

# $F86B — schreiben

## Disassemblatura
```assembly
.F86B  20 38 F8 JSR $F838   ; wartet auf Record & Play Taste
.F86E  B0 6C    BCS $F8DC   ; verzweige falls STOP-Taste gedrückt
.F870  78       SEI   ; Interrupt verhindern
.F871  A9 82    LDA #$82   ; Bitwert für IRQ bei Unterlauf von Timer B
.F873  A2 08    LDX #$08   ; Nummer des IRQ-Vektors, $FC6A
.F875  A0 7F    LDY #$7F   ; Bitwert für alle IRQs sperren
.F877  8C 0D DC STY $DC0D   ; Wert schreiben
.F87A  8D 0D DC STA $DC0D   ; und neu setzen
.F87D  AD 0E DC LDA $DC0E   ; Control Register A laden
.F880  09 19    ORA #$19   ; Bitwert für one shot, starten
.F882  8D 0F DC STA $DC0F   ; und ins Steuerregister für Timer B
.F885  29 91    AND #$91   ; Vergleichszeiger für Bandope-
.F887  8D A2 02 STA $02A2   ; rationen entsprechend setzen
.F88A  20 A4 F0 JSR $F0A4   ; auf Ende RS-232 Übertragung warten
.F88D  AD 11 D0 LDA $D011   ; Bildschirm
.F890  29 EF    AND #$EF   ; dunkel
.F892  8D 11 D0 STA $D011   ; Tasten
.F895  AD 14 03 LDA $0314   ; IRQ-Vector
.F898  8D 9F 02 STA $029F   ; nach $029F
.F89B  AD 15 03 LDA $0315   ; und $02A0
.F89E  8D A0 02 STA $02A0   ; speichern
.F8A1  20 BD FC JSR $FCBD   ; IRQ-Vektor für Band I/O setzen (X-indiziert)
.F8A4  A9 02    LDA #$02   ; Anzahl der
.F8A6  85 BE    STA $BE   ; zu lesenden Blöcke
.F8A8  20 97 FB JSR $FB97   ; serielle Ausgabe vorbereiten Bit-Zähler setzen
.F8AB  A5 01    LDA $01   ; Prozessorport laden
.F8AD  29 1F    AND #$1F   ; Bandmotor einschalten
.F8AF  85 01    STA $01   ; und wieder speichern
.F8B1  85 C0    STA $C0   ; Flag für Bandmotor setzen
.F8B3  A2 FF    LDX #$FF   ; HIGH-Byte für Zähler
.F8B5  A0 FF    LDY #$FF   ; LOW-Byte für Zähler
.F8B7  88       DEY   ; Verzögerungsschleife
.F8B8  D0 FD    BNE $F8B7   ; für Bandhochlaufzeit
.F8BA  CA       DEX   ; HIGH-Byte veringern
.F8BB  D0 F8    BNE $F8B5   ; verzweige falls nicht Null
.F8BD  58       CLI   ; Interrupt für Band I/O freigeben
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F86B**: wartet auf Record & Play Taste
- **$F86E**: verzweige falls STOP-Taste gedrückt
- **$F870**: Interrupt verhindern
- **$F871**: Bitwert für IRQ bei Unterlauf von Timer B
- **$F873**: Nummer des IRQ-Vektors, $FC6A
- **$F875**: Bitwert für alle IRQs sperren
- **$F877**: Wert schreiben
- **$F87A**: und neu setzen
- **$F87D**: Control Register A laden
- **$F880**: Bitwert für one shot, starten
- **$F882**: und ins Steuerregister für Timer B
- **$F885**: Vergleichszeiger für Bandope-
- **$F887**: rationen entsprechend setzen
- **$F88A**: auf Ende RS-232 Übertragung warten
- **$F88D**: Bildschirm
- **$F890**: dunkel
- **$F892**: Tasten
- **$F895**: IRQ-Vector
- **$F898**: nach $029F
- **$F89B**: und $02A0
- **$F89E**: speichern
- **$F8A1**: IRQ-Vektor für Band I/O setzen (X-indiziert)
- **$F8A4**: Anzahl der
- **$F8A6**: zu lesenden Blöcke
- **$F8A8**: serielle Ausgabe vorbereiten Bit-Zähler setzen
- **$F8AB**: Prozessorport laden
- **$F8AD**: Bandmotor einschalten
- **$F8AF**: und wieder speichern
- **$F8B1**: Flag für Bandmotor setzen
- **$F8B3**: HIGH-Byte für Zähler
- **$F8B5**: LOW-Byte für Zähler
- **$F8B7**: Verzögerungsschleife
- **$F8B8**: für Bandhochlaufzeit
- **$F8BA**: HIGH-Byte veringern
- **$F8BB**: verzweige falls nicht Null
- **$F8BD**: Interrupt für Band I/O freigeben

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*