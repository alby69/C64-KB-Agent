---
id: b9bc-constants-and-series-for-logn
type: entity
title: constants and series for LOG(n)
aliases:
- constants and series for LOG(n)
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b9bc-constants-and-series-for-logn.md
  sha256: ccc3a3a6318e9d58c0b4433057b0b3dd38dde631b02637e8ce8146fe51a79f49
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b9bc-constants-and-series-for-logn
---

# constants and series for LOG(n)



# $B9BC — constants and series for LOG(n)

## Disassemblatura
```assembly
.B9BC  81 00 00 00 00   ; 1
.B9C1  03   ; series counter
.B9C2  7F 5E 56 CB 79   ; .434255942
.B9C7  80 13 9B 0B 64   ; .576584541
.B9CC  80 76 38 93 16   ; .961800759
.B9D1  82 38 AA 3B 20   ; 2.88539007
.B9D6  80 35 04 F3 34   ; .707106781 = 1/SQR(2)
.B9DB  81 35 04 F3 34   ; 1.41421356 = SQR(2)
.B9E0  80 80 00 00 00   ; -.5
.B9E5  80 31 72 17 F8   ; .693147181  =  LOG(2)
```


## Commenti

### Original Disassembly (—)
- **$B9BC**: 1
- **$B9C1**: series counter
- **$B9C2**: .434255942
- **$B9C7**: .576584541
- **$B9CC**: .961800759
- **$B9D1**: 2.88539007
- **$B9D6**: .707106781 = 1/SQR(2)
- **$B9DB**: 1.41421356 = SQR(2)
- **$B9E0**: -.5
- **$B9E5**: .693147181  =  LOG(2)

### Commodore-64-intern-Buch (Commodore)
- **$B9BC**: 1
- **$B9C1**: 3 = Polynomgrad, dann 4 Koeffizienten
- **$B9C2**: .434255942
- **$B9C7**: .576584541
- **$B9CC**: .961800759
- **$B9D1**: 2.88539007
- **$B9D6**: .707106781 = 1/SQR(2)
- **$B9DB**: 1.41421356 = SQR(2)
- **$B9E0**: -.5
- **$B9E5**: .693147181  =  LOG(2)

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b9bc-constants-and-series-for-logn]]
