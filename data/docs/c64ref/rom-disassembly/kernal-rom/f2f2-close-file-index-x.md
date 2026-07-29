---
title: close file index X
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
- f2f2-reorganise-file-tables
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $F2F2
  address_end: $F30E
  symbol: close-file-index-x
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F2F2**: copy index to file to close'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

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