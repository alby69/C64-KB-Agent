---
title: get fixed-point number into temporary integer
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
- a96b-zeilennummer-nach-1415
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A96B
  address_end: $A9A2
  symbol: get-fixed-point-number-into-temporary-integer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A96B**: clear X'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A96B**: Wert Laden und'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A981**: times 2'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A96B**: ASC # TO HEX ADDRESS'
---

# $A96B — get fixed-point number into temporary integer

## Disassemblatura
```assembly
.A96B  A2 00    LDX #$00   ; clear X
.A96D  86 14    STX $14   ; clear temporary integer low byte
.A96F  86 15    STX $15   ; clear temporary integer high byte
.A971  B0 F7    BCS $A96A   ; return if carry set, end of scan, character was not 0-9
.A973  E9 2F    SBC #$2F   ; subtract $30, $2F+carry, from byte
.A975  85 07    STA $07   ; store #
.A977  A5 15    LDA $15   ; get temporary integer high byte
.A979  85 22    STA $22   ; save it for now
.A97B  C9 19    CMP #$19   ; compare with $19
.A97D  B0 D4    BCS $A953   ; branch if >= this makes the maximum line number 63999 because the next bit does $1900 * $0A = $FA00 = 64000 decimal. the branch target is really the SYNTAX error at $A8E8 but that is too far so an intermediate compare and branch to that location is used. the problem with this is that line number that gives a partial result from $8900 to $89FF, 35072x to 35327x, will pass the new target compare and will try to execute the remainder of the ON n GOTO/GOSUB. a solution to this is to copy the byte in A before the branch to X and then branch to $A955 skipping the second compare
.A97F  A5 14    LDA $14   ; get temporary integer low byte
.A981  0A       ASL   ; *2 low byte
.A982  26 22    ROL $22   ; *2 high byte
.A984  0A       ASL   ; *2 low byte
.A985  26 22    ROL $22   ; *2 high byte (*4)
.A987  65 14    ADC $14   ; + low byte (*5)
.A989  85 14    STA $14   ; save it
.A98B  A5 22    LDA $22   ; get high byte temp
.A98D  65 15    ADC $15   ; + high byte (*5)
.A98F  85 15    STA $15   ; save it
.A991  06 14    ASL $14   ; *2 low byte (*10d)
.A993  26 15    ROL $15   ; *2 high byte (*10d)
.A995  A5 14    LDA $14   ; get low byte
.A997  65 07    ADC $07   ; add #
.A999  85 14    STA $14   ; save low byte
.A99B  90 02    BCC $A99F   ; branch if no overflow to high byte
.A99D  E6 15    INC $15   ; else increment high byte
.A99F  20 73 00 JSR $0073   ; increment and scan memory
.A9A2  4C 71 A9 JMP $A971   ; loop for next character
```


## Commenti

### Original Disassembly (—)
- **$A96B**: clear X
- **$A96D**: clear temporary integer low byte
- **$A96F**: clear temporary integer high byte
- **$A971**: return if carry set, end of scan, character was not 0-9
- **$A973**: subtract $30, $2F+carry, from byte
- **$A975**: store #
- **$A977**: get temporary integer high byte
- **$A979**: save it for now
- **$A97B**: compare with $19
- **$A97D**: branch if >= this makes the maximum line number 63999 because the next bit does $1900 * $0A = $FA00 = 64000 decimal. the branch target is really the SYNTAX error at $A8E8 but that is too far so an intermediate compare and branch to that location is used. the problem with this is that line number that gives a partial result from $8900 to $89FF, 35072x to 35327x, will pass the new target compare and will try to execute the remainder of the ON n GOTO/GOSUB. a solution to this is to copy the byte in A before the branch to X and then branch to $A955 skipping the second compare
- **$A97F**: get temporary integer low byte
- **$A981**: *2 low byte
- **$A982**: *2 high byte
- **$A984**: *2 low byte
- **$A985**: *2 high byte (*4)
- **$A987**: + low byte (*5)
- **$A989**: save it
- **$A98B**: get high byte temp
- **$A98D**: + high byte (*5)
- **$A98F**: save it
- **$A991**: *2 low byte (*10d)
- **$A993**: *2 high byte (*10d)
- **$A995**: get low byte
- **$A997**: add #
- **$A999**: save low byte
- **$A99B**: branch if no overflow to high byte
- **$A99D**: else increment high byte
- **$A99F**: increment and scan memory
- **$A9A2**: loop for next character

### Commodore-64-intern-Buch (Commodore)
- **$A96B**: Wert Laden und
- **$A96D**: Vorsetzen
- **$A96F**: (für Zeilennummer gleich 0)
- **$A971**: keine Ziffer, dann fertig
- **$A973**: '0'-1 abziehen, gibt Hexwert
- **$A975**: merken
- **$A977**: HIGH-Byte holen
- **$A979**: Zwischenspeichern
- **$A97B**: Zahl bereits größer 6400?
- **$A97D**: dann 'SYNTAX ERROR'
- **$A97F**: Zahl * 10 (= *2*2+Zahl*2)
- **$A981**: Wert und Zwischenwert je
- **$A982**: 2 mal um 1 Bit nach
- **$A984**: links rollen
- **$A985**: (entspricht 2 * 2)
- **$A987**: plus ursprünglicher Wert
- **$A989**: und abspeichern
- **$A98B**: Zwischenwert zu
- **$A98D**: zweitem Wert addieren
- **$A98F**: und wieder abspeichern
- **$A991**: Speicherzelle $14 und
- **$A993**: $15 verdoppeln
- **$A995**: Wert wieder laden
- **$A997**: und Einerziffer addieren
- **$A999**: wieder speichern
- **$A99B**: Carry gesetzt? (Übertrag)
- **$A99D**: Übertrag addieren
- **$A99F**: CHRGET nächstes Zeichen holen
- **$A9A2**: und weiter machen

### Marko Mäkelä (Marko Mäkelä)
- **$A981**: times 2
- **$A984**: times 2
- **$A987**: add original
- **$A991**: times 2
- **$A993**: = times 10 overall

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A96B**: ASC # TO HEX ADDRESS
- **$A96D**: IN LINNUM.
- **$A971**: NOT A DIGIT
- **$A973**: CONVERT DIGIT TO BINARY
- **$A975**: SAVE THE DIGIT
- **$A977**: CHECK RANGE
- **$A97B**: LINE # TOO LARGE?
- **$A97D**: YES, > 63999, GO INDIRECTLY TO "SYNTAX ERROR". <<<<<DANGEROUS CODE>>>>> NOTE THAT IF (A) = $AB ON THE LINE ABOVE, ON.1 WILL COMPARE = AND CAUSE A CATASTROPHIC JUMP TO $22D9 (FOR GOTO), OR OTHER LOCATIONS FOR OTHER CALLS TO LINGET. YOU CAN SEE THIS IS YOU FIRST PUT "BRK" IN $22D9, THEN TYPE "GO TO 437761". ANY VALUE FROM 437760 THROUGH 440319 WILL CAUSE THE PROBLEM.  ($AB00 - $ABFF) <<<<<DANGEROUS CODE>>>>>
- **$A97F**: MULTIPLY BY TEN
- **$A997**: ADD DIGIT
- **$A99F**: GET NEXT CHAR
- **$A9A2**: MORE CONVERTING

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*