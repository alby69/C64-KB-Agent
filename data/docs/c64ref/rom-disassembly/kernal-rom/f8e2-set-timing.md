---
title: '# set timing'
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
- f8e2-band-fr-lesen-vorbereiten
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F8E2
  address_end: $F92B
  symbol: set-timing
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F8E2**: save tape timing constant max byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F8E2**: X-Register speichern'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F8E2 — # set timing

## Disassemblatura
```assembly
.F8E2  86 B1    STX $B1   ; save tape timing constant max byte
.F8E4  A5 B0    LDA $B0   ; get tape timing constant min byte
.F8E6  0A       ASL   ; *2
.F8E7  0A       ASL   ; *4
.F8E8  18       CLC   ; clear carry for add
.F8E9  65 B0    ADC $B0   ; add tape timing constant min byte *5
.F8EB  18       CLC   ; clear carry for add
.F8EC  65 B1    ADC $B1   ; add tape timing constant max byte
.F8EE  85 B1    STA $B1   ; save tape timing constant max byte
.F8F0  A9 00    LDA #$00
.F8F2  24 B0    BIT $B0   ; test tape timing constant min byte
.F8F4  30 01    BMI $F8F7   ; branch if b7 set
.F8F6  2A       ROL   ; else shift carry into ??
.F8F7  06 B1    ASL $B1   ; shift tape timing constant max byte
.F8F9  2A       ROL
.F8FA  06 B1    ASL $B1   ; shift tape timing constant max byte
.F8FC  2A       ROL
.F8FD  AA       TAX
.F8FE  AD 06 DC LDA $DC06   ; get VIA 1 timer B low byte
.F901  C9 16    CMP #$16   ; compare with ??
.F903  90 F9    BCC $F8FE   ; loop if less
.F905  65 B1    ADC $B1   ; add tape timing constant max byte
.F907  8D 04 DC STA $DC04   ; save VIA 1 timer A low byte
.F90A  8A       TXA
.F90B  6D 07 DC ADC $DC07   ; add VIA 1 timer B high byte
.F90E  8D 05 DC STA $DC05   ; save VIA 1 timer A high byte
.F911  AD A2 02 LDA $02A2   ; read VIA 1 CRB shadow copy
.F914  8D 0E DC STA $DC0E   ; save VIA 1 CRA
.F917  8D A4 02 STA $02A4   ; save VIA 1 CRA shadow copy
.F91A  AD 0D DC LDA $DC0D   ; read VIA 1 ICR
.F91D  29 10    AND #$10   ; mask 000x 0000, FLAG interrupt
.F91F  F0 09    BEQ $F92A   ; if no FLAG interrupt just exit else first call the IRQ routine
.F921  A9 F9    LDA #$F9   ; set the return address high byte
.F923  48       PHA   ; push the return address high byte
.F924  A9 2A    LDA #$2A   ; set the return address low byte
.F926  48       PHA   ; push the return address low byte
.F927  4C 43 FF JMP $FF43   ; save the status and do the IRQ routine
.F92A  58       CLI   ; enable interrupts
.F92B  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F8E2**: save tape timing constant max byte
- **$F8E4**: get tape timing constant min byte
- **$F8E6**: *2
- **$F8E7**: *4
- **$F8E8**: clear carry for add
- **$F8E9**: add tape timing constant min byte *5
- **$F8EB**: clear carry for add
- **$F8EC**: add tape timing constant max byte
- **$F8EE**: save tape timing constant max byte
- **$F8F2**: test tape timing constant min byte
- **$F8F4**: branch if b7 set
- **$F8F6**: else shift carry into ??
- **$F8F7**: shift tape timing constant max byte
- **$F8FA**: shift tape timing constant max byte
- **$F8FE**: get VIA 1 timer B low byte
- **$F901**: compare with ??
- **$F903**: loop if less
- **$F905**: add tape timing constant max byte
- **$F907**: save VIA 1 timer A low byte
- **$F90B**: add VIA 1 timer B high byte
- **$F90E**: save VIA 1 timer A high byte
- **$F911**: read VIA 1 CRB shadow copy
- **$F914**: save VIA 1 CRA
- **$F917**: save VIA 1 CRA shadow copy
- **$F91A**: read VIA 1 ICR
- **$F91D**: mask 000x 0000, FLAG interrupt
- **$F91F**: if no FLAG interrupt just exit else first call the IRQ routine
- **$F921**: set the return address high byte
- **$F923**: push the return address high byte
- **$F924**: set the return address low byte
- **$F926**: push the return address low byte
- **$F927**: save the status and do the IRQ routine
- **$F92A**: enable interrupts

### Commodore-64-intern-Buch (Commodore)
- **$F8E2**: X-Register speichern
- **$F8E4**: Timing-Konstante laden
- **$F8E6**: mit vier
- **$F8E7**: multiplizieren
- **$F8E8**: zur Addition Carry löschen
- **$F8E9**: mit altem Wert addieren (*5)
- **$F8EB**: zur Addition Carry löschen
- **$F8EC**: alten X Wert dazuaddieren
- **$F8EE**: und im Hilfszeiger speichern
- **$F8F0**: Akku löschen
- **$F8F2**: prüfe Timing-Konstante
- **$F8F4**: verzweige, falls größer 128
- **$F8F6**: Carry in die unterste Position des Akkus schieben
- **$F8F7**: und Timer A
- **$F8F9**: Initialisierung
- **$F8FA**: mit vier
- **$F8FC**: multiplizieren
- **$F8FD**: Akku ins X-Register
- **$F8FE**: LOW-Byte Timer B laden
- **$F901**: mit $16 vergleichen
- **$F903**: verzweige, wenn kleiner
- **$F905**: LOW-Byte für Initialisierung addieren
- **$F907**: Timer A LOW speichern
- **$F90A**: HIGH-Byte für Initialisierung
- **$F90B**: zu Timer B HIGH addieren
- **$F90E**: und in Timer A HIGH schreiben
- **$F911**: Init. Wert für Band Zeitkon.
- **$F914**: zum Starten von Timer A
- **$F917**: Timer A Flag zurücksetzten
- **$F91A**: ICR laden
- **$F91D**: Bit isolieren
- **$F91F**: verzweige wenn IRQ nicht vom Pin Flag
- **$F921**: Rücksprungadresse
- **$F923**: auf
- **$F924**: Stack
- **$F926**: schieben
- **$F927**: zum Interrupt
- **$F92A**: alle Interrupts freigeben
- **$F92B**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*