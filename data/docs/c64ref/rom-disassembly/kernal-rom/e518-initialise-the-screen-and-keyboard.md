---
title: initialise the screen and keyboard
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
- e518-bildschirm-reset
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E518
  address_end: $E542
  symbol: initialise-the-screen-and-keyboard
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E518**: initialise the vic chip'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E518**: Videocontroller initialisieren'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E522**: low  EB48'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E518**: set I/O defaults'
---

# $E518 — initialise the screen and keyboard

## Disassemblatura
```assembly
.E518  20 A0 E5 JSR $E5A0   ; initialise the vic chip
.E51B  A9 00    LDA #$00   ; clear A
.E51D  8D 91 02 STA $0291   ; clear the shift mode switch
.E520  85 CF    STA $CF   ; clear the cursor blink phase
.E522  A9 48    LDA #$48   ; get the keyboard decode logic pointer low byte
.E524  8D 8F 02 STA $028F   ; save the keyboard decode logic pointer low byte
.E527  A9 EB    LDA #$EB   ; get the keyboard decode logic pointer high byte
.E529  8D 90 02 STA $0290   ; save the keyboard decode logic pointer high byte
.E52C  A9 0A    LDA #$0A   ; set the maximum size of the keyboard buffer
.E52E  8D 89 02 STA $0289   ; save the maximum size of the keyboard buffer
.E531  8D 8C 02 STA $028C   ; save the repeat delay counter
.E534  A9 0E    LDA #$0E   ; set light blue
.E536  8D 86 02 STA $0286   ; save the current colour code
.E539  A9 04    LDA #$04   ; speed 4
.E53B  8D 8B 02 STA $028B   ; save the repeat speed counter
.E53E  A9 0C    LDA #$0C   ; set the cursor flash timing
.E540  85 CD    STA $CD   ; save the cursor timing countdown
.E542  85 CC    STA $CC   ; save the cursor enable, $00 = flash cursor
```


## Commenti

### Original Disassembly (—)
- **$E518**: initialise the vic chip
- **$E51B**: clear A
- **$E51D**: clear the shift mode switch
- **$E520**: clear the cursor blink phase
- **$E522**: get the keyboard decode logic pointer low byte
- **$E524**: save the keyboard decode logic pointer low byte
- **$E527**: get the keyboard decode logic pointer high byte
- **$E529**: save the keyboard decode logic pointer high byte
- **$E52C**: set the maximum size of the keyboard buffer
- **$E52E**: save the maximum size of the keyboard buffer
- **$E531**: save the repeat delay counter
- **$E534**: set light blue
- **$E536**: save the current colour code
- **$E539**: speed 4
- **$E53B**: save the repeat speed counter
- **$E53E**: set the cursor flash timing
- **$E540**: save the cursor timing countdown
- **$E542**: save the cursor enable, $00 = flash cursor

### Commodore-64-intern-Buch (Commodore)
- **$E518**: Videocontroller initialisieren
- **$E51B**: Shift-
- **$E51D**: Commodore ermöglichen
- **$E520**: Cursor nicht in Blinkphase
- **$E522**: Adresse
- **$E524**: ($028F) = $EB48
- **$E527**: setzen
- **$E529**: = Zeiger auf Adressen für Tastaturdekodierung
- **$E52C**: 10
- **$E52E**: max. Länge des Tastaturpuffers
- **$E531**: Zähler für Repeat-Geschwindigkeit
- **$E534**: hellblau
- **$E536**: Augenblickliche Farbe
- **$E539**: Repeat-
- **$E53B**: Geschwindigkeit
- **$E53E**: Cursor
- **$E540**: Blinkzeit
- **$E542**: Cursor Blinkflag

### Marko Mäkelä (Marko Mäkelä)
- **$E522**: low  EB48
- **$E527**: high EB48

### Magnus Nyman (Magnus Nyman)
- **$E518**: set I/O defaults
- **$E51D**: disable <SHIFT + CBM> by writing zero into MODE
- **$E520**: the cursor blink flag, set BLNON on
- **$E527**: set the KEYLOG vector to point at $eb48
- **$E52C**: set max number of character is keyboard buffer to 10
- **$E52E**: XMAX
- **$E531**: How many 1/60 of a second to wait before key is repeated. Used together with $028b
- **$E534**: set character colour to light blue
- **$E536**: COLOR
- **$E539**: How many $028c before a new entry is
- **$E53B**: put in the keyboard buffer, KOUNT
- **$E540**: store in BLCNT, cursor toggle timer
- **$E542**: store in BLNSW, cursor enable

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*