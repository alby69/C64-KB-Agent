---
title: compare FAC1 with (AY)
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bc5b-fac
- bc5d-special-entry-from-next-processor
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BC5B
  address_end: $BC98
  symbol: compare-fac1-with-ay
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC5B**: save pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BC5B**: Zeiger auf'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC5B**: USE DEST FOR PNTR'
---

# $BC5B — compare FAC1 with (AY)

## Disassemblatura
```assembly
.BC5B  85 24    STA $24   ; save pointer low byte
.BC5D  84 25    STY $25   ; save pointer high byte
.BC5F  A0 00    LDY #$00   ; clear index
.BC61  B1 24    LDA ($24),Y   ; get exponent
.BC63  C8       INY   ; increment index
.BC64  AA       TAX   ; copy (AY) exponent to X
.BC65  F0 C4    BEQ $BC2B   ; branch if (AY) exponent=0 and get FAC1 sign A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve
.BC67  B1 24    LDA ($24),Y   ; get (AY) mantissa 1, with sign
.BC69  45 66    EOR $66   ; EOR FAC1 sign (b7)
.BC6B  30 C2    BMI $BC2F   ; if signs <> do return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve and return
.BC6D  E4 61    CPX $61   ; compare (AY) exponent with FAC1 exponent
.BC6F  D0 21    BNE $BC92   ; branch if different
.BC71  B1 24    LDA ($24),Y   ; get (AY) mantissa 1, with sign
.BC73  09 80    ORA #$80   ; normalise top bit
.BC75  C5 62    CMP $62   ; compare with FAC1 mantissa 1
.BC77  D0 19    BNE $BC92   ; branch if different
.BC79  C8       INY   ; increment index
.BC7A  B1 24    LDA ($24),Y   ; get mantissa 2
.BC7C  C5 63    CMP $63   ; compare with FAC1 mantissa 2
.BC7E  D0 12    BNE $BC92   ; branch if different
.BC80  C8       INY   ; increment index
.BC81  B1 24    LDA ($24),Y   ; get mantissa 3
.BC83  C5 64    CMP $64   ; compare with FAC1 mantissa 3
.BC85  D0 0B    BNE $BC92   ; branch if different
.BC87  C8       INY   ; increment index
.BC88  A9 7F    LDA #$7F   ; set for 1/2 value rounding byte
.BC8A  C5 70    CMP $70   ; compare with FAC1 rounding byte (set carry)
.BC8C  B1 24    LDA ($24),Y   ; get mantissa 4
.BC8E  E5 65    SBC $65   ; subtract FAC1 mantissa 4
.BC90  F0 28    BEQ $BCBA   ; exit if mantissa 4 equal gets here if number <> FAC1
.BC92  A5 66    LDA $66   ; get FAC1 sign (b7)
.BC94  90 02    BCC $BC98   ; branch if FAC1 > (AY)
.BC96  49 FF    EOR #$FF   ; else toggle FAC1 sign
.BC98  4C 31 BC JMP $BC31   ; return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve
```


## Commenti

### Original Disassembly (—)
- **$BC5B**: save pointer low byte
- **$BC5D**: save pointer high byte
- **$BC5F**: clear index
- **$BC61**: get exponent
- **$BC63**: increment index
- **$BC64**: copy (AY) exponent to X
- **$BC65**: branch if (AY) exponent=0 and get FAC1 sign A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve
- **$BC67**: get (AY) mantissa 1, with sign
- **$BC69**: EOR FAC1 sign (b7)
- **$BC6B**: if signs <> do return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve and return
- **$BC6D**: compare (AY) exponent with FAC1 exponent
- **$BC6F**: branch if different
- **$BC71**: get (AY) mantissa 1, with sign
- **$BC73**: normalise top bit
- **$BC75**: compare with FAC1 mantissa 1
- **$BC77**: branch if different
- **$BC79**: increment index
- **$BC7A**: get mantissa 2
- **$BC7C**: compare with FAC1 mantissa 2
- **$BC7E**: branch if different
- **$BC80**: increment index
- **$BC81**: get mantissa 3
- **$BC83**: compare with FAC1 mantissa 3
- **$BC85**: branch if different
- **$BC87**: increment index
- **$BC88**: set for 1/2 value rounding byte
- **$BC8A**: compare with FAC1 rounding byte (set carry)
- **$BC8C**: get mantissa 4
- **$BC8E**: subtract FAC1 mantissa 4
- **$BC90**: exit if mantissa 4 equal gets here if number <> FAC1
- **$BC92**: get FAC1 sign (b7)
- **$BC94**: branch if FAC1 > (AY)
- **$BC96**: else toggle FAC1 sign
- **$BC98**: return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve

### Commodore-64-intern-Buch (Commodore)
- **$BC5B**: Zeiger auf
- **$BC5D**: Konstante
- **$BC5F**: Zähler setzen
- **$BC61**: Exponent
- **$BC63**: Zähler erhöhen
- **$BC64**: ins X-Reg
- **$BC65**: null?, dann Vorzeichen von FAC holen
- **$BC67**: Konstante
- **$BC69**: FAC-Vorzeichen
- **$BC6B**: verschiedene Vorzeichen?, dann zu $BC2F
- **$BC6D**: Exponenten vergleichen
- **$BC6F**: falls verschieden, dann zu $BC92
- **$BC71**: das
- **$BC73**: erste
- **$BC75**: Byte
- **$BC77**: vergleichen
- **$BC79**: Zähler erhöhen
- **$BC7A**: das zweite
- **$BC7C**: Byte
- **$BC7E**: vergleichen
- **$BC80**: Zähler erhöhen
- **$BC81**: das dritte
- **$BC83**: Byte
- **$BC85**: vergleichen
- **$BC87**: Zähler erhöhen
- **$BC88**: FAC-Rundungsstelle mit
- **$BC8A**: $7F vergleichen
- **$BC8C**: letzte Stellen, gemäß Ver-
- **$BC8E**: gleich der Rundungsstelle, subtrahieren
- **$BC90**: wenn alle Stellen gleich sind, dann RTS
- **$BC92**: FAC-Vorzeichen
- **$BC94**: ist die Konstante kleiner FAC, dann zu $BC98
- **$BC96**: Ergebnis kleiner, dann invertieren
- **$BC98**: Flag für Ergebnis setzen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC5B**: USE DEST FOR PNTR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*