---
id: f2f2-close-file-index-x
type: entity
title: close file index X
aliases:
- close file index X
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f2f2-close-file-index-x.md
  sha256: d8290fd4e21f6ac9138bae82dcdf4d7a58b7bb6e2603cfb08315ca26d532f268
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f2f2-close-file-index-x
---

# close file index X



# $F2F2 — close file index X

## Disassemblatura
```assembly
.F2F2  AA       TAX   ; copy index to file to close
.F2F3  C6 98    DEC $98   ; decrement the open file count
.F2F5  E4 98    CPX $98   ; compare the index with the open file count
.F2F7  F0 14    BEQ $F30D   ; exit if equal, last entry was closing file else entry was not last in list so copy last table entry file details over the details of the closing one
.F2F9  A4 98    LDY $98   ; get the open file count as index
.F2FB  B9 59 02 LDA $0259,Y   ; get last+1 logical file number from logical file table
.F2FE  9D 59 02 STA $0259,X   ; save logical file number over closed file
.F301  B9 63 02 LDA $0263,Y   ; get last+1 device number from device number table
.F304  9D 63 02 STA $0263,X   ; save device number over closed file
.F307  B9 6D 02 LDA $026D,Y   ; get last+1 secondary address from secondary address table
.F30A  9D 6D 02 STA $026D,X   ; save secondary address over closed file
.F30D  18       CLC   ; flag ok
.F30E  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F2F2**: copy index to file to close
- **$F2F3**: decrement the open file count
- **$F2F5**: compare the index with the open file count
- **$F2F7**: exit if equal, last entry was closing file else entry was not last in list so copy last table entry file details over the details of the closing one
- **$F2F9**: get the open file count as index
- **$F2FB**: get last+1 logical file number from logical file table
- **$F2FE**: save logical file number over closed file
- **$F301**: get last+1 device number from device number table
- **$F304**: save device number over closed file
- **$F307**: get last+1 secondary address from secondary address table
- **$F30A**: save secondary address over closed file
- **$F30D**: flag ok

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f2f2-close-file-index-x]]
