---
id: b82d-perform-wait
type: entity
title: perform WAIT
aliases:
- perform WAIT
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b82d-perform-wait.md
  sha256: 9a310ac28e6734b8766705712c515664504642f2febff27c8fdd7c28150b072b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b82d-perform-wait
---

# perform WAIT



# $B82D — perform WAIT

## Disassemblatura
```assembly
.B82D  20 EB B7 JSR $B7EB   ; get parameters for POKE/WAIT
.B830  86 49    STX $49   ; save byte
.B832  A2 00    LDX #$00   ; clear mask
.B834  20 79 00 JSR $0079   ; scan memory
.B837  F0 03    BEQ $B83C   ; skip if no third argument
.B839  20 F1 B7 JSR $B7F1   ; scan for "," and get byte, else syntax error then warm start
.B83C  86 4A    STX $4A   ; save EOR argument
.B83E  A0 00    LDY #$00   ; clear index
.B840  B1 14    LDA ($14),Y   ; get byte via temporary integer (address)
.B842  45 4A    EOR $4A   ; EOR with second argument       (mask)
.B844  25 49    AND $49   ; AND with first argument        (byte)
.B846  F0 F8    BEQ $B840   ; loop if result is zero
.B848  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B82D**: get parameters for POKE/WAIT
- **$B830**: save byte
- **$B832**: clear mask
- **$B834**: scan memory
- **$B837**: skip if no third argument
- **$B839**: scan for "," and get byte, else syntax error then warm start
- **$B83C**: save EOR argument
- **$B83E**: clear index
- **$B840**: get byte via temporary integer (address)
- **$B842**: EOR with second argument       (mask)
- **$B844**: AND with first argument        (byte)
- **$B846**: loop if result is zero

### Commodore-64-intern-Buch (Commodore)
- **$B82D**: Adresse und Wert holen
- **$B830**: zweiter Parameter nach $49
- **$B832**: Default für dritten Parameter
- **$B834**: CHRGOT letztes Zeichen
- **$B837**: kein dritter Parameter ?
- **$B839**: prüft auf Komma und holt Parameter
- **$B83C**: dritter Parameter nach $4A
- **$B83E**: Zähler auf Null
- **$B840**: Wait-Adresse
- **$B842**: logisch
- **$B844**: verknüpfen
- **$B846**: weiter warten
- **$B848**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B82D**: GET ADDRESS IN LINNUM, MASK IN X
- **$B830**: SAVE MASK
- **$B834**: ANOTHER PARAMETER?
- **$B837**: NO, USE $00 FOR EXCLUSIVE-OR
- **$B839**: GET XOR-MASK
- **$B83C**: SAVE XOR-MASK HERE
- **$B840**: GET BYTE AT ADDRESS
- **$B842**: INVERT SPECIFIED BITS
- **$B844**: SELECT SPECIFIED BITS
- **$B846**: LOOP TILL NOT 0

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b82d-perform-wait]]
