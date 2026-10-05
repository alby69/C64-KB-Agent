---
id: a71a-uncrunch-basic-tokens-the-uncrunch-basic-tokens-vector-is-initialised-to-point-here
type: entity
title: uncrunch BASIC tokens, the uncrunch BASIC tokens vector is initialised to point
  here
aliases:
- uncrunch BASIC tokens, the uncrunch BASIC tokens vector is initialised to point
  here
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a71a-uncrunch-basic-tokens-the-uncrunch-basic-tokens-vector-is-initialised-to-point-here.md
  sha256: 6b3935a52742c44c2435aa4e4a3aee02e660f2300a48db100b20bcf2c97f909c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a71a-uncrunch-basic-tokens-the-uncrunch-basic-tokens-vector-is-initialised-to-point-here
---

# uncrunch BASIC tokens, the uncrunch BASIC tokens vector is initialised to point here



# $A71A — uncrunch BASIC tokens, the uncrunch BASIC tokens vector is initialised to point here

## Disassemblatura
```assembly
.A71A  10 D7    BPL $A6F3   ; just go print it if not token byte else was token byte so uncrunch it
.A71C  C9 FF    CMP #$FF   ; compare with the token for PI. in this case the token is the same as the PI character so it just needs printing
.A71E  F0 D3    BEQ $A6F3   ; just print it if so
.A720  24 0F    BIT $0F   ; test the open quote flag
.A722  30 CF    BMI $A6F3   ; just go print character if open quote set
.A724  38       SEC   ; else set carry for subtract
.A725  E9 7F    SBC #$7F   ; reduce token range to 1 to whatever
.A727  AA       TAX   ; copy token # to X
.A728  84 49    STY $49   ; save index for line
.A72A  A0 FF    LDY #$FF   ; start from -1, adjust for pre increment
.A72C  CA       DEX   ; decrement token #
.A72D  F0 08    BEQ $A737   ; if now found go do printing
.A72F  C8       INY   ; else increment index
.A730  B9 9E A0 LDA $A09E,Y   ; get byte from keyword table
.A733  10 FA    BPL $A72F   ; loop until keyword end marker
.A735  30 F5    BMI $A72C   ; go test if this is required keyword, branch always found keyword, it's the next one
.A737  C8       INY   ; increment keyword table index
.A738  B9 9E A0 LDA $A09E,Y   ; get byte from table
.A73B  30 B2    BMI $A6EF   ; go restore index, mask byte and print if byte was end marker
.A73D  20 47 AB JSR $AB47   ; else go print the character
.A740  D0 F5    BNE $A737   ; go get next character, branch always
```


## Commenti

### Original Disassembly (—)
- **$A71A**: just go print it if not token byte else was token byte so uncrunch it
- **$A71C**: compare with the token for PI. in this case the token is the same as the PI character so it just needs printing
- **$A71E**: just print it if so
- **$A720**: test the open quote flag
- **$A722**: just go print character if open quote set
- **$A724**: else set carry for subtract
- **$A725**: reduce token range to 1 to whatever
- **$A727**: copy token # to X
- **$A728**: save index for line
- **$A72A**: start from -1, adjust for pre increment
- **$A72C**: decrement token #
- **$A72D**: if now found go do printing
- **$A72F**: else increment index
- **$A730**: get byte from keyword table
- **$A733**: loop until keyword end marker
- **$A735**: go test if this is required keyword, branch always found keyword, it's the next one
- **$A737**: increment keyword table index
- **$A738**: get byte from table
- **$A73B**: go restore index, mask byte and print if byte was end marker
- **$A73D**: else go print the character
- **$A740**: go get next character, branch always

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a71a-uncrunch-basic-tokens-the-uncrunch-basic-tokens-vector-is-initialised-to-point-here]]
