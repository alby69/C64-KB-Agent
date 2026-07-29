---
title: continuation of garbage clean up
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $B606
  address_end: $B63A
  symbol: continuation-of-garbage-clean-up
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B606**: String zwischen Tabellenende'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B606 — continuation of garbage clean up

## Disassemblatura
```assembly
.B606  A5 4F    LDA $4F
.B608  05 4E    ORA $4E
.B60A  F0 F5    BEQ $B601
.B60C  A5 55    LDA $55
.B60E  29 04    AND #$04
.B610  4A       LSR
.B611  A8       TAY
.B612  85 55    STA $55
.B614  B1 4E    LDA ($4E),Y
.B616  65 5F    ADC $5F
.B618  85 5A    STA $5A
.B61A  A5 60    LDA $60
.B61C  69 00    ADC #$00
.B61E  85 5B    STA $5B
.B620  A5 33    LDA $33
.B622  A6 34    LDX $34
.B624  85 58    STA $58
.B626  86 59    STX $59
.B628  20 BF A3 JSR $A3BF
.B62B  A4 55    LDY $55
.B62D  C8       INY
.B62E  A5 58    LDA $58
.B630  91 4E    STA ($4E),Y
.B632  AA       TAX
.B633  E6 59    INC $59
.B635  A5 59    LDA $59
.B637  C8       INY
.B638  91 4E    STA ($4E),Y
.B63A  4C 2A B5 JMP $B52A
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B606**: String zwischen Tabellenende
- **$B608**: und dem oberen RAM-Bereich
- **$B60A**: gefunden ? nein, dann RTS
- **$B60C**: Arraysuchlauf, dann $55=03
- **$B60E**: ansonsten $55=07
- **$B610**: wenn Einzelvariable, dann
- **$B611**: Y-Reg =2 und 0 bei Array
- **$B612**: Wert sichern
- **$B614**: Stringlänge holen
- **$B616**: zum LOW-Byte der Stringanfangs-
- **$B618**: adresse Add., =Endadresse +1
- **$B61A**: auf gleiche
- **$B61C**: Weise das
- **$B61E**: HIGH-Byte berechnen
- **$B620**: Zielbereich
- **$B622**: für den
- **$B624**: Transfer
- **$B626**: holen
- **$B628**: Strings verschieben
- **$B62B**: LOW-Byte
- **$B62D**: der
- **$B62E**: Anfangsadresse in
- **$B630**: Descriptor speichern
- **$B632**: HIGH-Byte
- **$B633**: der Anfangsadresse
- **$B635**: in
- **$B637**: Descriptor
- **$B638**: bringen
- **$B63A**: nicht alles ?, dann weiter Stringverknüpfung '+'
- **$B63D**: HIGH-Byte des Descriptors vom
- **$B63F**: ersten String auf Stack
- **$B640**: LOW-Byte
- **$B642**: in Stack
- **$B643**: zweiten String holen
- **$B646**: prüft auf Stringvariable
- **$B649**: Descriptorzeiger des ersten
- **$B64A**: Strings wiederholen
- **$B64C**: und
- **$B64D**: speichern
- **$B64F**: Zähler auf Null
- **$B651**: Länge des ersten Strings
- **$B653**: plus Länge
- **$B654**: des zweiten Strings
- **$B656**: kleiner als 256
- **$B658**: Nummer für 'STRING TOO LONG'
- **$B65A**: Fehlermeldung ausgeben
- **$B65D**: Platz für verknüpften String
- **$B660**: ersten String übertragen
- **$B663**: Zeiger auf
- **$B665**: zweiten Stringdescriptor
- **$B667**: FRESTR
- **$B66A**: 2. String an 1. anhängen
- **$B66D**: Descriptorzeiger des
- **$B66F**: zweiten Strings
- **$B671**: FRESTR
- **$B674**: Descriptor in Stringstack
- **$B677**: zurück zur Formelauswertung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*