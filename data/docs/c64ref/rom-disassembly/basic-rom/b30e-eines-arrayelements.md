---
title: eines Arrayelements
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b30e-eines-arrayelements
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $B30E
  address_end: $B34B
  symbol: eines-arrayelements
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B30E**: Zeiger erhöhen'
---

# $B30E — eines Arrayelements

## Disassemblatura
```assembly
.B30E  C8       INY   ; Zeiger erhöhen
.B30F  A5 72    LDA $72   ; Zeiger auf Polynomausw.(HIGH)
.B311  05 71    ORA $71   ; Zeiger auf Polynomausw.(LOW)
.B313  18       CLC   ; Carry löschen
.B314  F0 0A    BEQ $B320   ; Multiplikation umgehen
.B316  20 4C B3 JSR $B34C   ; Multiplikation
.B319  8A       TXA   ; (X/Y)=($71/72)*(($5F/60),Y)
.B31A  65 64    ADC $64
.B31C  AA       TAX   ; Akku zurück ins X-Reg.
.B31D  98       TYA
.B31E  A4 22    LDY $22   ; Zeiger in Arrayheader
.B320  65 65    ADC $65
.B322  86 71    STX $71
.B324  C6 0B    DEC $0B   ; Anzahl der Dimensionen
.B326  D0 CA    BNE $B2F2   ; mit nächstem Index weiter
.B328  85 72    STA $72
.B32A  A2 05    LDX #$05   ; Variablenlänge (5, REAL)
.B32C  A5 45    LDA $45   ; erster Buchstabe des Namens
.B32E  10 01    BPL $B331   ; Integer? nein: $B331
.B330  CA       DEX   ; Länge vermindern
.B331  A5 46    LDA $46   ; zweiter Buchstabe des Namens
.B333  10 02    BPL $B337   ; FLP? ja: $B337
.B335  CA       DEX   ; Länge 2 mal
.B336  CA       DEX   ; vermindern
.B337  86 28    STX $28   ; Länge der Variablen 2,3 oder5
.B339  A9 00    LDA #$00   ; Wert laden und damit
.B33B  20 55 B3 JSR $B355   ; Offset im Array berechnen
.B33E  8A       TXA   ; zur Adresse des ersten
.B33F  65 58    ADC $58   ; Elements addieren
.B341  85 47    STA $47   ; ergibt Variablenadresse
.B343  98       TYA   ; 2.Byte in Akku holen
.B344  65 59    ADC $59   ; addieren, ergibt
.B346  85 48    STA $48   ; HIGH-Byte der Adresse
.B348  A8       TAY   ; ins Y-Reg. bringen und
.B349  A5 47    LDA $47   ; 1.Byte wieder in Akku holen
.B34B  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B30E**: Zeiger erhöhen
- **$B30F**: Zeiger auf Polynomausw.(HIGH)
- **$B311**: Zeiger auf Polynomausw.(LOW)
- **$B313**: Carry löschen
- **$B314**: Multiplikation umgehen
- **$B316**: Multiplikation
- **$B319**: (X/Y)=($71/72)*(($5F/60),Y)
- **$B31C**: Akku zurück ins X-Reg.
- **$B31E**: Zeiger in Arrayheader
- **$B324**: Anzahl der Dimensionen
- **$B326**: mit nächstem Index weiter
- **$B32A**: Variablenlänge (5, REAL)
- **$B32C**: erster Buchstabe des Namens
- **$B32E**: Integer? nein: $B331
- **$B330**: Länge vermindern
- **$B331**: zweiter Buchstabe des Namens
- **$B333**: FLP? ja: $B337
- **$B335**: Länge 2 mal
- **$B336**: vermindern
- **$B337**: Länge der Variablen 2,3 oder5
- **$B339**: Wert laden und damit
- **$B33B**: Offset im Array berechnen
- **$B33E**: zur Adresse des ersten
- **$B33F**: Elements addieren
- **$B341**: ergibt Variablenadresse
- **$B343**: 2.Byte in Akku holen
- **$B344**: addieren, ergibt
- **$B346**: HIGH-Byte der Adresse
- **$B348**: ins Y-Reg. bringen und
- **$B349**: 1.Byte wieder in Akku holen
- **$B34B**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*