---
title: perform LEFT$()
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
- b700-basic-funktion-left
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B700
  address_end: $B729
  symbol: perform-left
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B700**: pull string data and byte parameter from stack return
      pointer in...'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B700**: Stringadresse & Länge aus Stack holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B703**: COMPARE 1ST PARAMETER TO LENGTH'
---

# $B700 — perform LEFT$()

## Disassemblatura
```assembly
.B700  20 61 B7 JSR $B761   ; pull string data and byte parameter from stack return pointer in descriptor, byte in A (and X), Y=0
.B703  D1 50    CMP ($50),Y   ; compare byte parameter with string length
.B705  98       TYA   ; clear A
.B706  90 04    BCC $B70C   ; branch if string length > byte parameter
.B708  B1 50    LDA ($50),Y   ; else make parameter = length
.B70A  AA       TAX   ; copy to byte parameter copy
.B70B  98       TYA   ; clear string start offset
.B70C  48       PHA   ; save string start offset
.B70D  8A       TXA   ; copy byte parameter (or string length if <)
.B70E  48       PHA   ; save string length
.B70F  20 7D B4 JSR $B47D   ; make string space A bytes long
.B712  A5 50    LDA $50   ; get descriptor pointer low byte
.B714  A4 51    LDY $51   ; get descriptor pointer high byte
.B716  20 AA B6 JSR $B6AA   ; pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.B719  68       PLA   ; get string length back
.B71A  A8       TAY   ; copy length to Y
.B71B  68       PLA   ; get string start offset back
.B71C  18       CLC   ; clear carry for add
.B71D  65 22    ADC $22   ; add start offset to string start pointer low byte
.B71F  85 22    STA $22   ; save string start pointer low byte
.B721  90 02    BCC $B725   ; branch if no overflow
.B723  E6 23    INC $23   ; else increment string start pointer high byte
.B725  98       TYA   ; copy length to A
.B726  20 8C B6 JSR $B68C   ; store string from pointer to utility pointer
.B729  4C CA B4 JMP $B4CA   ; check space on descriptor stack then put string address and length on descriptor stack and update stack pointers
```


## Commenti

### Original Disassembly (—)
- **$B700**: pull string data and byte parameter from stack return pointer in descriptor, byte in A (and X), Y=0
- **$B703**: compare byte parameter with string length
- **$B705**: clear A
- **$B706**: branch if string length > byte parameter
- **$B708**: else make parameter = length
- **$B70A**: copy to byte parameter copy
- **$B70B**: clear string start offset
- **$B70C**: save string start offset
- **$B70D**: copy byte parameter (or string length if <)
- **$B70E**: save string length
- **$B70F**: make string space A bytes long
- **$B712**: get descriptor pointer low byte
- **$B714**: get descriptor pointer high byte
- **$B716**: pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$B719**: get string length back
- **$B71A**: copy length to Y
- **$B71B**: get string start offset back
- **$B71C**: clear carry for add
- **$B71D**: add start offset to string start pointer low byte
- **$B71F**: save string start pointer low byte
- **$B721**: branch if no overflow
- **$B723**: else increment string start pointer high byte
- **$B725**: copy length to A
- **$B726**: store string from pointer to utility pointer
- **$B729**: check space on descriptor stack then put string address and length on descriptor stack and update stack pointers

### Commodore-64-intern-Buch (Commodore)
- **$B700**: Stringadresse & Länge aus Stack holen
- **$B703**: Länge mit LEFT$-Parameter vergleichen
- **$B705**: LEFT$-Parameter
- **$B706**: kleiner als Stringlänge ?
- **$B708**: Stringlänge holen
- **$B70A**: und ins X-Reg schieben
- **$B70B**: Stringlänge und
- **$B70C**: Parameter für LEFT$
- **$B70D**: in Stack
- **$B70E**: schieben
- **$B70F**: Platz für neuen String reservieren
- **$B712**: Zeiger auf Stringdescriptor
- **$B714**: laden
- **$B716**: FRESTR
- **$B719**: Länge des neuen Strings aus
- **$B71A**: Stack holen und ins X-Reg
- **$B71B**: alte
- **$B71C**: Stringadresse
- **$B71D**: entsprechend
- **$B71F**: erhöhen
- **$B721**: und speichern
- **$B723**: HIGH-Byte erhöhen
- **$B725**: neue Stringlänge holen
- **$B726**: neuen String in Stringbereich übertragen
- **$B729**: Descriptor in Stringstack bringen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B703**: COMPARE 1ST PARAMETER TO LENGTH
- **$B705**: Y=A=0
- **$B706**: 1ST PARAMETER SMALLER, USE IT
- **$B708**: 1ST IS LONGER, USE STRING LENGTH
- **$B70A**: IN X-REG
- **$B70B**: Y=A=0 AGAIN
- **$B70C**: PUSH LEFT END OF SUBSTRING
- **$B70E**: PUSH LENGTH OF SUBSTRING
- **$B70F**: MAKE ROOM FOR STRING OF (A) BYTES
- **$B712**: RELEASE PARAMETER STRING IF TEMP
- **$B719**: GET LENGTH OF SUBSTRING
- **$B71A**: IN Y-REG
- **$B71B**: GET LEFT END OF SUBSTRING
- **$B71C**: ADD TO POINTER TO STRING
- **$B725**: LENGTH
- **$B726**: COPY STRING INTO SPACE
- **$B729**: ADD TO TEMPS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*