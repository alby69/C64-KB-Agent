---
title: perform RND()
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e097-basic-funktion-rnd
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $E097
  address_end: $E0F4
  symbol: perform-rnd
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E097**: get FAC1 sign return A = $FF -ve, A = $01 +ve'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E097**: Vorzeichen holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E097**: REDUCE ARGUMENT TO -1, 0, OR +1'
---

# $E097 — perform RND()

## Disassemblatura
```assembly
.E097  20 2B BC JSR $BC2B   ; get FAC1 sign return A = $FF -ve, A = $01 +ve
.E09A  30 37    BMI $E0D3   ; if n<0 copy byte swapped FAC1 into RND() seed
.E09C  D0 20    BNE $E0BE   ; if n>0 get next number in RND() sequence else n=0 so get the RND() number from VIA 1 timers
.E09E  20 F3 FF JSR $FFF3   ; return base address of I/O devices
.E0A1  86 22    STX $22   ; save pointer low byte
.E0A3  84 23    STY $23   ; save pointer high byte
.E0A5  A0 04    LDY #$04   ; set index to T1 low byte
.E0A7  B1 22    LDA ($22),Y   ; get T1 low byte
.E0A9  85 62    STA $62   ; save FAC1 mantissa 1
.E0AB  C8       INY   ; increment index
.E0AC  B1 22    LDA ($22),Y   ; get T1 high byte
.E0AE  85 64    STA $64   ; save FAC1 mantissa 3
.E0B0  A0 08    LDY #$08   ; set index to T2 low byte
.E0B2  B1 22    LDA ($22),Y   ; get T2 low byte
.E0B4  85 63    STA $63   ; save FAC1 mantissa 2
.E0B6  C8       INY   ; increment index
.E0B7  B1 22    LDA ($22),Y   ; get T2 high byte
.E0B9  85 65    STA $65   ; save FAC1 mantissa 4
.E0BB  4C E3 E0 JMP $E0E3   ; set exponent and exit
.E0BE  A9 8B    LDA #$8B   ; set seed pointer low address
.E0C0  A0 00    LDY #$00   ; set seed pointer high address
.E0C2  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
.E0C5  A9 8D    LDA #$8D   ; set 11879546 pointer low byte
.E0C7  A0 E0    LDY #$E0   ; set 11879546 pointer high byte
.E0C9  20 28 BA JSR $BA28   ; do convert AY, FCA1*(AY)
.E0CC  A9 92    LDA #$92   ; set 3.927677739E-8 pointer low byte
.E0CE  A0 E0    LDY #$E0   ; set 3.927677739E-8 pointer high byte
.E0D0  20 67 B8 JSR $B867   ; add (AY) to FAC1
.E0D3  A6 65    LDX $65   ; get FAC1 mantissa 4
.E0D5  A5 62    LDA $62   ; get FAC1 mantissa 1
.E0D7  85 65    STA $65   ; save FAC1 mantissa 4
.E0D9  86 62    STX $62   ; save FAC1 mantissa 1
.E0DB  A6 63    LDX $63   ; get FAC1 mantissa 2
.E0DD  A5 64    LDA $64   ; get FAC1 mantissa 3
.E0DF  85 63    STA $63   ; save FAC1 mantissa 2
.E0E1  86 64    STX $64   ; save FAC1 mantissa 3
.E0E3  A9 00    LDA #$00   ; clear byte
.E0E5  85 66    STA $66   ; clear FAC1 sign (always +ve)
.E0E7  A5 61    LDA $61   ; get FAC1 exponent
.E0E9  85 70    STA $70   ; save FAC1 rounding byte
.E0EB  A9 80    LDA #$80   ; set exponent = $80
.E0ED  85 61    STA $61   ; save FAC1 exponent
.E0EF  20 D7 B8 JSR $B8D7   ; normalise FAC1
.E0F2  A2 8B    LDX #$8B   ; set seed pointer low address
.E0F4  A0 00    LDY #$00   ; set seed pointer high address
```


## Commenti

### Original Disassembly (—)
- **$E097**: get FAC1 sign return A = $FF -ve, A = $01 +ve
- **$E09A**: if n<0 copy byte swapped FAC1 into RND() seed
- **$E09C**: if n>0 get next number in RND() sequence else n=0 so get the RND() number from VIA 1 timers
- **$E09E**: return base address of I/O devices
- **$E0A1**: save pointer low byte
- **$E0A3**: save pointer high byte
- **$E0A5**: set index to T1 low byte
- **$E0A7**: get T1 low byte
- **$E0A9**: save FAC1 mantissa 1
- **$E0AB**: increment index
- **$E0AC**: get T1 high byte
- **$E0AE**: save FAC1 mantissa 3
- **$E0B0**: set index to T2 low byte
- **$E0B2**: get T2 low byte
- **$E0B4**: save FAC1 mantissa 2
- **$E0B6**: increment index
- **$E0B7**: get T2 high byte
- **$E0B9**: save FAC1 mantissa 4
- **$E0BB**: set exponent and exit
- **$E0BE**: set seed pointer low address
- **$E0C0**: set seed pointer high address
- **$E0C2**: unpack memory (AY) into FAC1
- **$E0C5**: set 11879546 pointer low byte
- **$E0C7**: set 11879546 pointer high byte
- **$E0C9**: do convert AY, FCA1*(AY)
- **$E0CC**: set 3.927677739E-8 pointer low byte
- **$E0CE**: set 3.927677739E-8 pointer high byte
- **$E0D0**: add (AY) to FAC1
- **$E0D3**: get FAC1 mantissa 4
- **$E0D5**: get FAC1 mantissa 1
- **$E0D7**: save FAC1 mantissa 4
- **$E0D9**: save FAC1 mantissa 1
- **$E0DB**: get FAC1 mantissa 2
- **$E0DD**: get FAC1 mantissa 3
- **$E0DF**: save FAC1 mantissa 2
- **$E0E1**: save FAC1 mantissa 3
- **$E0E3**: clear byte
- **$E0E5**: clear FAC1 sign (always +ve)
- **$E0E7**: get FAC1 exponent
- **$E0E9**: save FAC1 rounding byte
- **$E0EB**: set exponent = $80
- **$E0ED**: save FAC1 exponent
- **$E0EF**: normalise FAC1
- **$E0F2**: set seed pointer low address
- **$E0F4**: set seed pointer high address

### Commodore-64-intern-Buch (Commodore)
- **$E097**: Vorzeichen holen
- **$E09A**: negativ ?, dann zu $E0D3
- **$E09C**: nicht Null?, dann zu $E0BE
- **$E09E**: Basis-Adresse CIA holen
- **$E0A1**: als Zeiger
- **$E0A3**: speichern
- **$E0A5**: Zähler setzen
- **$E0A7**: LOW-Byte Timer A laden
- **$E0A9**: und speichern
- **$E0AB**: Zähler erhöhen
- **$E0AC**: HIGH-Byte Timer A laden
- **$E0AE**: und speichern
- **$E0B0**: Zähler neu setzen
- **$E0B2**: TOD 1/10 sec laden
- **$E0B4**: und speichern
- **$E0B6**: Zähler erhöhen
- **$E0B7**: TOD sec laden
- **$E0B9**: und speichern
- **$E0BB**: weiter bei $E0E3
- **$E0BE**: Zeiger auf
- **$E0C0**: letzten RND-Wert
- **$E0C2**: nach FAC holen
- **$E0C5**: Zeiger auf
- **$E0C7**: Konstante
- **$E0C9**: FAC = FAC * Konstante
- **$E0CC**: Zeiger auf
- **$E0CE**: Konstante
- **$E0D0**: FAC = FAC + Konstante
- **$E0D3**: alle
- **$E0D5**: Stel-
- **$E0D7**: len
- **$E0D9**: im
- **$E0DB**: FAC
- **$E0DD**: ver-
- **$E0DF**: tau-
- **$E0E1**: schen
- **$E0E3**: Vorzeichen
- **$E0E5**: positiv
- **$E0E7**: Exponent in
- **$E0E9**: Rundungsstelle
- **$E0EB**: Zufallszahl
- **$E0ED**: speichern
- **$E0EF**: FAC linksbündig machen
- **$E0F2**: Zeiger auf
- **$E0F4**: letzten RND-Wert
- **$E0F6**: FAC runden und speichern

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E097**: REDUCE ARGUMENT TO -1, 0, OR +1
- **$E09A**: = -1, USE CURRENT ARGUMENT FOR SEED
- **$E0BE**: USE CURRENT SEED
- **$E0C5**: VERY POOR RND ALGORITHM
- **$E0CC**: ALSO, CONSTANTS ARE TRUNCATED
- **$E0CE**: <<<THIS DOES NOTHING, DUE TO >>> <<<SMALL EXPONENT            >>>
- **$E0D3**: SHUFFLE HI AND LO BYTES
- **$E0D5**: TO SUPPOSEDLY MAKE IT MORE RANDOM
- **$E0DD**: MAKE IT POSITIVE
- **$E0E3**: A SOMEWHAT RANDOM EXTENSION
- **$E0E7**: EXPONENT TO MAKE VALUE < 1.0
- **$E0F2**: MOVE FAC TO RND SEED

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*