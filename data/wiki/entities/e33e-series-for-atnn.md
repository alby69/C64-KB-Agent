---
id: e33e-series-for-atnn
type: entity
title: series for ATN(n)
aliases:
- series for ATN(n)
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e33e-series-for-atnn.md
  sha256: 504a85d67ce0da9a531bd4830ef6b205e9b327fb1929b183a21e95349d81ea16
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e33e-series-for-atnn
---

# series for ATN(n)



# $E33E — series for ATN(n)

## Disassemblatura
```assembly
.E33E  0B   ; series counter
.E33F  76 B3 83 BD D3   ; -6.84793912E-04
.E344  79 1E F4 A6 F5   ; 4.85094216E-03
.E349  7B 83 FC B0 10   ; -.0161117015
.E34E  7C 0C 1F 67 CA   ; .034209638
.E353  7C DE 53 CB C1   ; -.054279133
.E358  7D 14 64 70 4C   ; .0724571965
.E35D  7D B7 EA 51 7A   ; -.0898019185
.E362  7D 63 30 88 7E   ; .110932413
.E367  7E 92 44 99 3A   ; -.142839808
.E36C  7E 4C CC 91 C7   ; .19999912
.E371  7F AA AA AA 13   ; -.333333316
.E376  81 00 00 00 00   ; 1
```


## Commenti

### Original Disassembly (—)
- **$E33E**: series counter
- **$E33F**: -6.84793912E-04
- **$E344**: 4.85094216E-03
- **$E349**: -.0161117015
- **$E34E**: .034209638
- **$E353**: -.054279133
- **$E358**: .0724571965
- **$E35D**: -.0898019185
- **$E362**: .110932413
- **$E367**: -.142839808
- **$E36C**: .19999912
- **$E371**: -.333333316
- **$E376**: 1

### Commodore-64-intern-Buch (Commodore)
- **$E33E**: 11 = Polynomgrad, dann 12 Koeffizienten
- **$E33F**: -6.84793912E-04
- **$E344**: 4.85094216E-03
- **$E349**: -.0161117015
- **$E34E**: .034209638
- **$E353**: -.054279133
- **$E358**: .0724571965
- **$E35D**: -.0898019185
- **$E362**: .110932413
- **$E367**: -.142839808
- **$E36C**: .19999912
- **$E371**: -.333333316
- **$E376**: 1

### Marko Mäkelä (Marko Mäkelä)
- **$E33E**: degree 12

### Magnus Nyman (Magnus Nyman)
- **$E33E**: ; 13 (one byte counter for ATN series)
- **$E33F**: ; -0.000684793912 (ATN constant 1)
- **$E344**: ; 0.00485094216   (ATN constant 2)
- **$E349**: ; -0.161117018    (ATN constant 3)
- **$E34E**: ; 0.034209638     (ATN constant 5)
- **$E353**: ; -0.0542791328   (ATN constant 6)
- **$E358**: ; 0.0724571965    (ATN constant 7)
- **$E35D**: ; -0.0898023954   (ATN constant 8)
- **$E362**: ; 0.110932413     (ATN constant 9)
- **$E367**: ; -0.14283908     (ATN constant 10)
- **$E36C**: ; 0.19999912      (ATN constant 11)
- **$E371**: ; -0.333333316    (ATN constant 12)
- **$E376**: ; 1               (ATN constant 13)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e33e-series-for-atnn]]
