---
title: garbage collection routine
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b526-garbage-collection
- b5bd-prft-beseitigungsmglichkeit
- b5c7-check-string-area
- b606-strings-zusammenfgen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B526
  address_end: $B63A
  symbol: garbage-collection-routine
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B526**: get end of memory low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B526**: LOW-Byte Basic-RAM-Zeiger'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B53C**: low  0019'
---

# $B526 — garbage collection routine

## Disassemblatura
```assembly
.B526  A6 37    LDX $37   ; get end of memory low byte
.B528  A5 38    LDA $38   ; get end of memory high byte re-run routine from last ending
.B52A  86 33    STX $33   ; set bottom of string space low byte
.B52C  85 34    STA $34   ; set bottom of string space high byte
.B52E  A0 00    LDY #$00   ; clear index
.B530  84 4F    STY $4F   ; clear working pointer high byte
.B532  84 4E    STY $4E   ; clear working pointer low byte
.B534  A5 31    LDA $31   ; get end of arrays low byte
.B536  A6 32    LDX $32   ; get end of arrays high byte
.B538  85 5F    STA $5F   ; save as highest uncollected string pointer low byte
.B53A  86 60    STX $60   ; save as highest uncollected string pointer high byte
.B53C  A9 19    LDA #$19   ; set descriptor stack pointer
.B53E  A2 00    LDX #$00   ; clear X
.B540  85 22    STA $22   ; save descriptor stack pointer low byte
.B542  86 23    STX $23   ; save descriptor stack pointer high byte ($00)
.B544  C5 16    CMP $16   ; compare with descriptor stack pointer
.B546  F0 05    BEQ $B54D   ; branch if =
.B548  20 C7 B5 JSR $B5C7   ; check string salvageability
.B54B  F0 F7    BEQ $B544   ; loop always done stacked strings, now do string variables
.B54D  A9 07    LDA #$07   ; set step size = $07, collecting variables
.B54F  85 53    STA $53   ; save garbage collection step size
.B551  A5 2D    LDA $2D   ; get start of variables low byte
.B553  A6 2E    LDX $2E   ; get start of variables high byte
.B555  85 22    STA $22   ; save as pointer low byte
.B557  86 23    STX $23   ; save as pointer high byte
.B559  E4 30    CPX $30   ; compare end of variables high byte, start of arrays high byte
.B55B  D0 04    BNE $B561   ; branch if no high byte match
.B55D  C5 2F    CMP $2F   ; else compare end of variables low byte, start of arrays low byte
.B55F  F0 05    BEQ $B566   ; branch if = variable memory end
.B561  20 BD B5 JSR $B5BD   ; check variable salvageability
.B564  F0 F3    BEQ $B559   ; loop always done string variables, now do string arrays
.B566  85 58    STA $58   ; save start of arrays low byte as working pointer
.B568  86 59    STX $59   ; save start of arrays high byte as working pointer
.B56A  A9 03    LDA #$03   ; set step size, collecting descriptors
.B56C  85 53    STA $53   ; save step size
.B56E  A5 58    LDA $58   ; get pointer low byte
.B570  A6 59    LDX $59   ; get pointer high byte
.B572  E4 32    CPX $32   ; compare with end of arrays high byte
.B574  D0 07    BNE $B57D   ; branch if not at end
.B576  C5 31    CMP $31   ; else compare with end of arrays low byte
.B578  D0 03    BNE $B57D   ; branch if not at end
.B57A  4C 06 B6 JMP $B606   ; collect string, tidy up and exit if at end ??
.B57D  85 22    STA $22   ; save pointer low byte
.B57F  86 23    STX $23   ; save pointer high byte
.B581  A0 00    LDY #$00   ; set index
.B583  B1 22    LDA ($22),Y   ; get array name first byte
.B585  AA       TAX   ; copy it
.B586  C8       INY   ; increment index
.B587  B1 22    LDA ($22),Y   ; get array name second byte
.B589  08       PHP   ; push the flags
.B58A  C8       INY   ; increment index
.B58B  B1 22    LDA ($22),Y   ; get array size low byte
.B58D  65 58    ADC $58   ; add start of this array low byte
.B58F  85 58    STA $58   ; save start of next array low byte
.B591  C8       INY   ; increment index
.B592  B1 22    LDA ($22),Y   ; get array size high byte
.B594  65 59    ADC $59   ; add start of this array high byte
.B596  85 59    STA $59   ; save start of next array high byte
.B598  28       PLP   ; restore the flags
.B599  10 D3    BPL $B56E   ; skip if not string array was possibly string array so ...
.B59B  8A       TXA   ; get name first byte back
.B59C  30 D0    BMI $B56E   ; skip if not string array
.B59E  C8       INY   ; increment index
.B59F  B1 22    LDA ($22),Y   ; get # of dimensions
.B5A1  A0 00    LDY #$00   ; clear index
.B5A3  0A       ASL   ; *2
.B5A4  69 05    ADC #$05   ; +5 (array header size)
.B5A6  65 22    ADC $22   ; add pointer low byte
.B5A8  85 22    STA $22   ; save pointer low byte
.B5AA  90 02    BCC $B5AE   ; branch if no rollover
.B5AC  E6 23    INC $23   ; else increment pointer high byte
.B5AE  A6 23    LDX $23   ; get pointer high byte
.B5B0  E4 59    CPX $59   ; compare pointer high byte with end of this array high byte
.B5B2  D0 04    BNE $B5B8   ; branch if not there yet
.B5B4  C5 58    CMP $58   ; compare pointer low byte with end of this array low byte
.B5B6  F0 BA    BEQ $B572   ; if at end of this array go check next array
.B5B8  20 C7 B5 JSR $B5C7   ; check string salvageability
.B5BB  F0 F3    BEQ $B5B0   ; loop check variable salvageability
.B5BD  B1 22    LDA ($22),Y   ; get variable name first byte
.B5BF  30 35    BMI $B5F6   ; add step and exit if not string
.B5C1  C8       INY   ; increment index
.B5C2  B1 22    LDA ($22),Y   ; get variable name second byte
.B5C4  10 30    BPL $B5F6   ; add step and exit if not string
.B5C6  C8       INY   ; increment index check string salvageability
.B5C7  B1 22    LDA ($22),Y   ; get string length
.B5C9  F0 2B    BEQ $B5F6   ; add step and exit if null string
.B5CB  C8       INY   ; increment index
.B5CC  B1 22    LDA ($22),Y   ; get string pointer low byte
.B5CE  AA       TAX   ; copy to X
.B5CF  C8       INY   ; increment index
.B5D0  B1 22    LDA ($22),Y   ; get string pointer high byte
.B5D2  C5 34    CMP $34   ; compare string pointer high byte with bottom of string space high byte
.B5D4  90 06    BCC $B5DC   ; if bottom of string space greater go test against highest uncollected string
.B5D6  D0 1E    BNE $B5F6   ; if bottom of string space less string has been collected so go update pointers, step to next and return high bytes were equal so test low bytes
.B5D8  E4 33    CPX $33   ; compare string pointer low byte with bottom of string space low byte
.B5DA  B0 1A    BCS $B5F6   ; if bottom of string space less string has been collected so go update pointers, step to next and return else test string against highest uncollected string so far
.B5DC  C5 60    CMP $60   ; compare string pointer high byte with highest uncollected string high byte
.B5DE  90 16    BCC $B5F6   ; if highest uncollected string is greater then go update pointers, step to next and return
.B5E0  D0 04    BNE $B5E6   ; if highest uncollected string is less then go set this string as highest uncollected so far high bytes were equal so test low bytes
.B5E2  E4 5F    CPX $5F   ; compare string pointer low byte with highest uncollected string low byte
.B5E4  90 10    BCC $B5F6   ; if highest uncollected string is greater then go update pointers, step to next and return else set current string as highest uncollected string
.B5E6  86 5F    STX $5F   ; save string pointer low byte as highest uncollected string low byte
.B5E8  85 60    STA $60   ; save string pointer high byte as highest uncollected string high byte
.B5EA  A5 22    LDA $22   ; get descriptor pointer low byte
.B5EC  A6 23    LDX $23   ; get descriptor pointer high byte
.B5EE  85 4E    STA $4E   ; save working pointer high byte
.B5F0  86 4F    STX $4F   ; save working pointer low byte
.B5F2  A5 53    LDA $53   ; get step size
.B5F4  85 55    STA $55   ; copy step size
.B5F6  A5 53    LDA $53   ; get step size
.B5F8  18       CLC   ; clear carry for add
.B5F9  65 22    ADC $22   ; add pointer low byte
.B5FB  85 22    STA $22   ; save pointer low byte
.B5FD  90 02    BCC $B601   ; branch if no rollover
.B5FF  E6 23    INC $23   ; else increment pointer high byte
.B601  A6 23    LDX $23   ; get pointer high byte
.B603  A0 00    LDY #$00   ; flag not moved
.B605  60       RTS   ; collect string
.B606  A5 4F    LDA $4F   ; get working pointer low byte
.B608  05 4E    ORA $4E   ; OR working pointer high byte
.B60A  F0 F5    BEQ $B601   ; exit if nothing to collect
.B60C  A5 55    LDA $55   ; get copied step size
.B60E  29 04    AND #$04   ; mask step size, $04 for variables, $00 for array or stack
.B610  4A       LSR   ; >> 1
.B611  A8       TAY   ; copy to index
.B612  85 55    STA $55   ; save offset to descriptor start
.B614  B1 4E    LDA ($4E),Y   ; get string length low byte
.B616  65 5F    ADC $5F   ; add string start low byte
.B618  85 5A    STA $5A   ; set block end low byte
.B61A  A5 60    LDA $60   ; get string start high byte
.B61C  69 00    ADC #$00   ; add carry
.B61E  85 5B    STA $5B   ; set block end high byte
.B620  A5 33    LDA $33   ; get bottom of string space low byte
.B622  A6 34    LDX $34   ; get bottom of string space high byte
.B624  85 58    STA $58   ; save destination end low byte
.B626  86 59    STX $59   ; save destination end high byte
.B628  20 BF A3 JSR $A3BF   ; open up space in memory, don't set array end. this copies the string from where it is to the end of the uncollected string memory
.B62B  A4 55    LDY $55   ; restore offset to descriptor start
.B62D  C8       INY   ; increment index to string pointer low byte
.B62E  A5 58    LDA $58   ; get new string pointer low byte
.B630  91 4E    STA ($4E),Y   ; save new string pointer low byte
.B632  AA       TAX   ; copy string pointer low byte
.B633  E6 59    INC $59   ; increment new string pointer high byte
.B635  A5 59    LDA $59   ; get new string pointer high byte
.B637  C8       INY   ; increment index to string pointer high byte
.B638  91 4E    STA ($4E),Y   ; save new string pointer high byte
.B63A  4C 2A B5 JMP $B52A   ; re-run routine from last ending, XA holds new bottom of string memory pointer
```


## Commenti

### Original Disassembly (—)
- **$B526**: get end of memory low byte
- **$B528**: get end of memory high byte re-run routine from last ending
- **$B52A**: set bottom of string space low byte
- **$B52C**: set bottom of string space high byte
- **$B52E**: clear index
- **$B530**: clear working pointer high byte
- **$B532**: clear working pointer low byte
- **$B534**: get end of arrays low byte
- **$B536**: get end of arrays high byte
- **$B538**: save as highest uncollected string pointer low byte
- **$B53A**: save as highest uncollected string pointer high byte
- **$B53C**: set descriptor stack pointer
- **$B53E**: clear X
- **$B540**: save descriptor stack pointer low byte
- **$B542**: save descriptor stack pointer high byte ($00)
- **$B544**: compare with descriptor stack pointer
- **$B546**: branch if =
- **$B548**: check string salvageability
- **$B54B**: loop always done stacked strings, now do string variables
- **$B54D**: set step size = $07, collecting variables
- **$B54F**: save garbage collection step size
- **$B551**: get start of variables low byte
- **$B553**: get start of variables high byte
- **$B555**: save as pointer low byte
- **$B557**: save as pointer high byte
- **$B559**: compare end of variables high byte, start of arrays high byte
- **$B55B**: branch if no high byte match
- **$B55D**: else compare end of variables low byte, start of arrays low byte
- **$B55F**: branch if = variable memory end
- **$B561**: check variable salvageability
- **$B564**: loop always done string variables, now do string arrays
- **$B566**: save start of arrays low byte as working pointer
- **$B568**: save start of arrays high byte as working pointer
- **$B56A**: set step size, collecting descriptors
- **$B56C**: save step size
- **$B56E**: get pointer low byte
- **$B570**: get pointer high byte
- **$B572**: compare with end of arrays high byte
- **$B574**: branch if not at end
- **$B576**: else compare with end of arrays low byte
- **$B578**: branch if not at end
- **$B57A**: collect string, tidy up and exit if at end ??
- **$B57D**: save pointer low byte
- **$B57F**: save pointer high byte
- **$B581**: set index
- **$B583**: get array name first byte
- **$B585**: copy it
- **$B586**: increment index
- **$B587**: get array name second byte
- **$B589**: push the flags
- **$B58A**: increment index
- **$B58B**: get array size low byte
- **$B58D**: add start of this array low byte
- **$B58F**: save start of next array low byte
- **$B591**: increment index
- **$B592**: get array size high byte
- **$B594**: add start of this array high byte
- **$B596**: save start of next array high byte
- **$B598**: restore the flags
- **$B599**: skip if not string array was possibly string array so ...
- **$B59B**: get name first byte back
- **$B59C**: skip if not string array
- **$B59E**: increment index
- **$B59F**: get # of dimensions
- **$B5A1**: clear index
- **$B5A3**: *2
- **$B5A4**: +5 (array header size)
- **$B5A6**: add pointer low byte
- **$B5A8**: save pointer low byte
- **$B5AA**: branch if no rollover
- **$B5AC**: else increment pointer high byte
- **$B5AE**: get pointer high byte
- **$B5B0**: compare pointer high byte with end of this array high byte
- **$B5B2**: branch if not there yet
- **$B5B4**: compare pointer low byte with end of this array low byte
- **$B5B6**: if at end of this array go check next array
- **$B5B8**: check string salvageability
- **$B5BB**: loop check variable salvageability
- **$B5BD**: get variable name first byte
- **$B5BF**: add step and exit if not string
- **$B5C1**: increment index
- **$B5C2**: get variable name second byte
- **$B5C4**: add step and exit if not string
- **$B5C6**: increment index check string salvageability
- **$B5C7**: get string length
- **$B5C9**: add step and exit if null string
- **$B5CB**: increment index
- **$B5CC**: get string pointer low byte
- **$B5CE**: copy to X
- **$B5CF**: increment index
- **$B5D0**: get string pointer high byte
- **$B5D2**: compare string pointer high byte with bottom of string space high byte
- **$B5D4**: if bottom of string space greater go test against highest uncollected string
- **$B5D6**: if bottom of string space less string has been collected so go update pointers, step to next and return high bytes were equal so test low bytes
- **$B5D8**: compare string pointer low byte with bottom of string space low byte
- **$B5DA**: if bottom of string space less string has been collected so go update pointers, step to next and return else test string against highest uncollected string so far
- **$B5DC**: compare string pointer high byte with highest uncollected string high byte
- **$B5DE**: if highest uncollected string is greater then go update pointers, step to next and return
- **$B5E0**: if highest uncollected string is less then go set this string as highest uncollected so far high bytes were equal so test low bytes
- **$B5E2**: compare string pointer low byte with highest uncollected string low byte
- **$B5E4**: if highest uncollected string is greater then go update pointers, step to next and return else set current string as highest uncollected string
- **$B5E6**: save string pointer low byte as highest uncollected string low byte
- **$B5E8**: save string pointer high byte as highest uncollected string high byte
- **$B5EA**: get descriptor pointer low byte
- **$B5EC**: get descriptor pointer high byte
- **$B5EE**: save working pointer high byte
- **$B5F0**: save working pointer low byte
- **$B5F2**: get step size
- **$B5F4**: copy step size
- **$B5F6**: get step size
- **$B5F8**: clear carry for add
- **$B5F9**: add pointer low byte
- **$B5FB**: save pointer low byte
- **$B5FD**: branch if no rollover
- **$B5FF**: else increment pointer high byte
- **$B601**: get pointer high byte
- **$B603**: flag not moved
- **$B605**: collect string
- **$B606**: get working pointer low byte
- **$B608**: OR working pointer high byte
- **$B60A**: exit if nothing to collect
- **$B60C**: get copied step size
- **$B60E**: mask step size, $04 for variables, $00 for array or stack
- **$B610**: >> 1
- **$B611**: copy to index
- **$B612**: save offset to descriptor start
- **$B614**: get string length low byte
- **$B616**: add string start low byte
- **$B618**: set block end low byte
- **$B61A**: get string start high byte
- **$B61C**: add carry
- **$B61E**: set block end high byte
- **$B620**: get bottom of string space low byte
- **$B622**: get bottom of string space high byte
- **$B624**: save destination end low byte
- **$B626**: save destination end high byte
- **$B628**: open up space in memory, don't set array end. this copies the string from where it is to the end of the uncollected string memory
- **$B62B**: restore offset to descriptor start
- **$B62D**: increment index to string pointer low byte
- **$B62E**: get new string pointer low byte
- **$B630**: save new string pointer low byte
- **$B632**: copy string pointer low byte
- **$B633**: increment new string pointer high byte
- **$B635**: get new string pointer high byte
- **$B637**: increment index to string pointer high byte
- **$B638**: save new string pointer high byte
- **$B63A**: re-run routine from last ending, XA holds new bottom of string memory pointer

### Commodore-64-intern-Buch (Commodore)
- **$B526**: LOW-Byte Basic-RAM-Zeiger
- **$B528**: HIGH-Byte Basic-RAM-Zeiger
- **$B52A**: in Stringzeiger
- **$B52C**: speichern
- **$B52E**: LOW- und HIGH-Byte
- **$B530**: der FN Zeiger
- **$B532**: auf Null setzen
- **$B534**: LOW- und HIGH-Byte der
- **$B536**: Array-Zeiger laden
- **$B538**: und in die Arithmetikregister
- **$B53A**: speichern
- **$B53C**: Startadresse
- **$B53E**: der Descriptorentabelle
- **$B540**: als Suchzeiger nach
- **$B542**: $22 und $23 bringen
- **$B544**: identisch mit String-Zeiger?
- **$B546**: wenn ja, dann weiter
- **$B548**: Stringposition feststellen
- **$B54B**: unbedingter Sprung
- **$B54D**: Schrittweite für die Suche
- **$B54F**: in Variablentabelle
- **$B551**: Tabellenzeiger
- **$B553**: laden
- **$B555**: und als Suchzeiger nach
- **$B557**: $22 und $23 bringen
- **$B559**: Am Ende der Tabelle angelangt
- **$B55B**: wenn nicht, dann zu $B561
- **$B55D**: ansonsten Sprung zur
- **$B55F**: Array-Behandlung
- **$B561**: Stringposition feststellen
- **$B564**: unbedingter Sprung
- **$B566**: Zeiger in die
- **$B568**: Array-Tabelle speichern
- **$B56A**: Schrittweite für Suche
- **$B56C**: innerhalb des Arrays festlegen
- **$B56E**: Am Ende
- **$B570**: der
- **$B572**: Arraytabelle angelangt, dann
- **$B574**: Sprung zu $B57D
- **$B576**: Vergleich mit HIGH-Byte
- **$B578**: Sprung zu $B57D
- **$B57A**: ansonsten Transfer
- **$B57D**: Zeiger auf Array-Header
- **$B57F**: stellen
- **$B581**: Zähler auf Null setzen
- **$B583**: Variablenname erstes Zeichen
- **$B585**: ins X-Reg übertragen
- **$B586**: Zähler erhöhen
- **$B587**: Variablenname zweites Zeichen
- **$B589**: Statusregister retten
- **$B58A**: Zähler erhöhen
- **$B58B**: Die Länge
- **$B58D**: des Arrays
- **$B58F**: zu
- **$B591**: Zeiger
- **$B592**: auf
- **$B594**: Arraytabelle
- **$B596**: addieren
- **$B598**: Statusregister wiederholen
- **$B599**: keine Stringvariable ?
- **$B59B**: dann weitersuchen
- **$B59C**: Stringvariable, nein, weiter
- **$B59E**: Zähler erhöhen
- **$B59F**: Dimensionenanzahl holen
- **$B5A1**: Zähler wieder Null
- **$B5A3**: mal 2
- **$B5A4**: plus 5
- **$B5A6**: zum Zeiger addieren
- **$B5A8**: und speichern
- **$B5AA**: wenn ungleich, dann zu $B5AE
- **$B5AC**: Zeiger erhöhen
- **$B5AE**: und in Array schieben
- **$B5B0**: auf nächstes Feld vergleichen
- **$B5B2**: wenn ungleich, dann zu $B5B8
- **$B5B4**: wenn gleich, dann
- **$B5B6**: zu $B572
- **$B5B8**: Stringposition feststellen
- **$B5BB**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
- **$B53C**: low  0019
- **$B53E**: high 0019

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*