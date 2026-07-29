---
title: rebuild BASIC line chaining
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
- a533-basic-zeilen-neu-binden
- a560-eingabe-einer-zeile
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A533
  address_end: $A576
  symbol: rebuild-basic-line-chaining
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A533**: get start of memory low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A533**: Zeiger auf BASIC-Programm-'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $A533 — rebuild BASIC line chaining

## Disassemblatura
```assembly
.A533  A5 2B    LDA $2B   ; get start of memory low byte
.A535  A4 2C    LDY $2C   ; get start of memory high byte
.A537  85 22    STA $22   ; set line start pointer low byte
.A539  84 23    STY $23   ; set line start pointer high byte
.A53B  18       CLC   ; clear carry for add
.A53C  A0 01    LDY #$01   ; set index to pointer to next line high byte
.A53E  B1 22    LDA ($22),Y   ; get pointer to next line high byte
.A540  F0 1D    BEQ $A55F   ; exit if null, [EOT]
.A542  A0 04    LDY #$04   ; point to first code byte of line there is always 1 byte + [EOL] as null entries are deleted
.A544  C8       INY   ; next code byte
.A545  B1 22    LDA ($22),Y   ; get byte
.A547  D0 FB    BNE $A544   ; loop if not [EOL]
.A549  C8       INY   ; point to byte past [EOL], start of next line
.A54A  98       TYA   ; copy it
.A54B  65 22    ADC $22   ; add line start pointer low byte
.A54D  AA       TAX   ; copy to X
.A54E  A0 00    LDY #$00   ; clear index, point to this line's next line pointer
.A550  91 22    STA ($22),Y   ; set next line pointer low byte
.A552  A5 23    LDA $23   ; get line start pointer high byte
.A554  69 00    ADC #$00   ; add any overflow
.A556  C8       INY   ; increment index to high byte
.A557  91 22    STA ($22),Y   ; set next line pointer high byte
.A559  86 22    STX $22   ; set line start pointer low byte
.A55B  85 23    STA $23   ; set line start pointer high byte
.A55D  90 DD    BCC $A53C   ; go do next line, branch always
.A55F  60       RTS   ; call for BASIC input
.A560  A2 00    LDX #$00   ; set channel $00, keyboard
.A562  20 12 E1 JSR $E112   ; input character from channel with error check
.A565  C9 0D    CMP #$0D   ; compare with [CR]
.A567  F0 0D    BEQ $A576   ; if [CR] set XY to $200 - 1, print [CR] and exit character was not [CR]
.A569  9D 00 02 STA $0200,X   ; save character to buffer
.A56C  E8       INX   ; increment buffer index
.A56D  E0 59    CPX #$59   ; compare with max+1
.A56F  90 F1    BCC $A562   ; branch if < max+1
.A571  A2 17    LDX #$17   ; error $17, string too long error
.A573  4C 37 A4 JMP $A437   ; do error #X then warm start
.A576  4C CA AA JMP $AACA   ; set XY to $200 - 1 and print [CR]
```


## Commenti

### Original Disassembly (—)
- **$A533**: get start of memory low byte
- **$A535**: get start of memory high byte
- **$A537**: set line start pointer low byte
- **$A539**: set line start pointer high byte
- **$A53B**: clear carry for add
- **$A53C**: set index to pointer to next line high byte
- **$A53E**: get pointer to next line high byte
- **$A540**: exit if null, [EOT]
- **$A542**: point to first code byte of line there is always 1 byte + [EOL] as null entries are deleted
- **$A544**: next code byte
- **$A545**: get byte
- **$A547**: loop if not [EOL]
- **$A549**: point to byte past [EOL], start of next line
- **$A54A**: copy it
- **$A54B**: add line start pointer low byte
- **$A54D**: copy to X
- **$A54E**: clear index, point to this line's next line pointer
- **$A550**: set next line pointer low byte
- **$A552**: get line start pointer high byte
- **$A554**: add any overflow
- **$A556**: increment index to high byte
- **$A557**: set next line pointer high byte
- **$A559**: set line start pointer low byte
- **$A55B**: set line start pointer high byte
- **$A55D**: go do next line, branch always
- **$A55F**: call for BASIC input
- **$A560**: set channel $00, keyboard
- **$A562**: input character from channel with error check
- **$A565**: compare with [CR]
- **$A567**: if [CR] set XY to $200 - 1, print [CR] and exit character was not [CR]
- **$A569**: save character to buffer
- **$A56C**: increment buffer index
- **$A56D**: compare with max+1
- **$A56F**: branch if < max+1
- **$A571**: error $17, string too long error
- **$A573**: do error #X then warm start
- **$A576**: set XY to $200 - 1 and print [CR]

### Commodore-64-intern-Buch (Commodore)
- **$A533**: Zeiger auf BASIC-Programm-
- **$A535**: start holen und
- **$A537**: und als Suchzeiger nach
- **$A539**: $22/23 speichern
- **$A53B**: Carry löschen
- **$A53C**: Zeiger laden
- **$A53E**: Zeilenadresse holen
- **$A540**: =0? Ja: dann RTS
- **$A542**: Zeiger auf erstes BASIC-
- **$A544**: zeichen setzen
- **$A545**: Zeichen holen
- **$A547**: =0? (Zeilenende) nein: weiter
- **$A549**: Zeilenlänge nach
- **$A54A**: Akku schieben
- **$A54B**: + Zeiger auf aktuelle Zeile
- **$A54D**: (LOW) ins X-Register
- **$A54E**: Zeiger laden
- **$A550**: Akku als Adr.zeiger (LOW)
- **$A552**: Zeiger auf aktuelle Zeile (HIGH)
- **$A554**: Übertrag addieren
- **$A556**: Zähler um 1 erhöhen
- **$A557**: Adresszeiger (HIGH) speichern
- **$A559**: Startadresse der nächsten
- **$A55B**: Zeile abspeichern
- **$A55D**: Zum Zeilenanfang
- **$A55F**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*