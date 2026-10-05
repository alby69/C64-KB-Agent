---
id: e165-perform-verify
type: entity
title: perform VERIFY
aliases:
- perform VERIFY
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e165-perform-verify.md
  sha256: 2dd9d874487670198dc432ff84997978c97b21b3dbe84d73428500e47b0146a4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e165-perform-verify
---

# perform VERIFY



# $E165 — perform VERIFY

## Disassemblatura
```assembly
.E165  A9 01    LDA #$01   ; flag verify
.E167  2C       .BYTE $2C   ; makes next line BIT $00A9
```


## Commenti

### Original Disassembly (—)
- **$E165**: flag verify
- **$E167**: makes next line BIT $00A9

### Commodore-64-intern-Buch (Commodore)
- **$E165**: Verify-
- **$E167**: Flag

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E165**: flag verify
- **$E167**: mask
- **$E16A**: store in VRECK, LOAD/VERIFY flag
- **$E16C**: get LOAD/VERIFY parameters from text
- **$E16F**: get VRECK
- **$E171**: TXTTAB, start of BASIC
- **$E175**: execute LOAD, KERNAL routine
- **$E178**: if carry set, handle error
- **$E17A**: test VRECK for LOAD or VERIFY
- **$E17C**: do LOAD
- **$E17E**: set error $1c, VERIFY error
- **$E180**: do READST, get status I/O word
- **$E183**: %00010000, test for mismatch
- **$E185**: data mismatch, do error
- **$E187**: <TXTPTR
- **$E18D**: set address to text OK
- **$E18F**: at $a364
- **$E191**: output string in (A/Y)
- **$E195**: do READST, get status I/O for LOAD
- **$E198**: %10111111, test all but EOI
- **$E19A**: nope, no errors
- **$E19C**: set error $1d, LOAD error
- **$E19E**: do error
- **$E1A1**: >TXTPTR
- **$E1A7**: set VARTAB, start of variables
- **$E1AB**: set address to text READY
- **$E1AD**: at $a376
- **$E1AF**: output string in (A/Y)
- **$E1B2**: do CLR and restart BASIC
- **$E1B5**: reset TXTPTR
- **$E1B8**: rechain BASIC lines
- **$E1BB**: do RESTORE and reset OLDTXT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e165-perform-verify]]
