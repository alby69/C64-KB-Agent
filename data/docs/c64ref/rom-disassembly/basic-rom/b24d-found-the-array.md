---
title: found the array
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
- b24d-found-the-array
- b261-arrayvariable-anlegen
- b2e9-arrayelement-suchen
- b2ea-find-specified-array-element
- b30e-eines-arrayelements
- b34c-arrayberechnung
- b37d-basic-funktion-fre
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $B24D
  address_end: $B38F
  symbol: found-the-array
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B24D**: set error $13, double dimension error'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B24D**: SET UP FOR REDIM''D ARRAY ERROR'
---

# $B24D — found the array

## Disassemblatura
```assembly
.B24D  A2 13    LDX #$13   ; set error $13, double dimension error
.B24F  A5 0C    LDA $0C   ; get DIM flag
.B251  D0 F7    BNE $B24A   ; if we are trying to dimension it do error #X then warm start found the array and we're not dimensioning it so we must find an element in it
.B253  20 94 B1 JSR $B194   ; set-up array pointer to first element in array
.B256  A5 0B    LDA $0B   ; get dimensions count
.B258  A0 04    LDY #$04   ; set index to array's # of dimensions
.B25A  D1 5F    CMP ($5F),Y   ; compare with no of dimensions
.B25C  D0 E7    BNE $B245   ; if wrong do bad subscript error
.B25E  4C EA B2 JMP $B2EA   ; found array so go get element array not found, so build it
.B261  20 94 B1 JSR $B194   ; set-up array pointer to first element in array
.B264  20 08 A4 JSR $A408   ; check available memory, do out of memory error if no room
.B267  A0 00    LDY #$00   ; clear Y
.B269  84 72    STY $72   ; clear array data size high byte
.B26B  A2 05    LDX #$05   ; set default element size
.B26D  A5 45    LDA $45   ; get variable name 1st byte
.B26F  91 5F    STA ($5F),Y   ; save array name 1st byte
.B271  10 01    BPL $B274   ; branch if not string or floating point array
.B273  CA       DEX   ; decrement element size, $04
.B274  C8       INY   ; increment index
.B275  A5 46    LDA $46   ; get variable name 2nd byte
.B277  91 5F    STA ($5F),Y   ; save array name 2nd byte
.B279  10 02    BPL $B27D   ; branch if not integer or string
.B27B  CA       DEX   ; decrement element size, $03
.B27C  CA       DEX   ; decrement element size, $02
.B27D  86 71    STX $71   ; save element size
.B27F  A5 0B    LDA $0B   ; get dimensions count
.B281  C8       INY   ; increment index ..
.B282  C8       INY   ; .. to array  ..
.B283  C8       INY   ; .. dimension count
.B284  91 5F    STA ($5F),Y   ; save array dimension count
.B286  A2 0B    LDX #$0B   ; set default dimension size low byte
.B288  A9 00    LDA #$00   ; set default dimension size high byte
.B28A  24 0C    BIT $0C   ; test DIM flag
.B28C  50 08    BVC $B296   ; branch if default to be used
.B28E  68       PLA   ; pull dimension size low byte
.B28F  18       CLC   ; clear carry for add
.B290  69 01    ADC #$01   ; add 1, allow for zeroeth element
.B292  AA       TAX   ; copy low byte to X
.B293  68       PLA   ; pull dimension size high byte
.B294  69 00    ADC #$00   ; add carry to high byte
.B296  C8       INY   ; increment index to dimension size high byte
.B297  91 5F    STA ($5F),Y   ; save dimension size high byte
.B299  C8       INY   ; increment index to dimension size low byte
.B29A  8A       TXA   ; copy dimension size low byte
.B29B  91 5F    STA ($5F),Y   ; save dimension size low byte
.B29D  20 4C B3 JSR $B34C   ; compute array size
.B2A0  86 71    STX $71   ; save result low byte
.B2A2  85 72    STA $72   ; save result high byte
.B2A4  A4 22    LDY $22   ; restore index
.B2A6  C6 0B    DEC $0B   ; decrement dimensions count
.B2A8  D0 DC    BNE $B286   ; loop if not all done
.B2AA  65 59    ADC $59   ; add array data pointer high byte
.B2AC  B0 5D    BCS $B30B   ; if overflow do out of memory error then warm start
.B2AE  85 59    STA $59   ; save array data pointer high byte
.B2B0  A8       TAY   ; copy array data pointer high byte
.B2B1  8A       TXA   ; copy array size low byte
.B2B2  65 58    ADC $58   ; add array data pointer low byte
.B2B4  90 03    BCC $B2B9   ; branch if no rollover
.B2B6  C8       INY   ; else increment next array pointer high byte
.B2B7  F0 52    BEQ $B30B   ; if rolled over do out of memory error then warm start
.B2B9  20 08 A4 JSR $A408   ; check available memory, do out of memory error if no room
.B2BC  85 31    STA $31   ; set end of arrays low byte
.B2BE  84 32    STY $32   ; set end of arrays high byte now the array is created we need to zero all the elements in it
.B2C0  A9 00    LDA #$00   ; clear A for array clear
.B2C2  E6 72    INC $72   ; increment array size high byte, now block count
.B2C4  A4 71    LDY $71   ; get array size low byte, now index to block
.B2C6  F0 05    BEQ $B2CD   ; branch if $00
.B2C8  88       DEY   ; decrement index, do 0 to n-1
.B2C9  91 58    STA ($58),Y   ; clear array element byte
.B2CB  D0 FB    BNE $B2C8   ; loop until this block done
.B2CD  C6 59    DEC $59   ; decrement array pointer high byte
.B2CF  C6 72    DEC $72   ; decrement block count high byte
.B2D1  D0 F5    BNE $B2C8   ; loop until all blocks done
.B2D3  E6 59    INC $59   ; correct for last loop
.B2D5  38       SEC   ; set carry for subtract
.B2D6  A5 31    LDA $31   ; get end of arrays low byte
.B2D8  E5 5F    SBC $5F   ; subtract array start low byte
.B2DA  A0 02    LDY #$02   ; index to array size low byte
.B2DC  91 5F    STA ($5F),Y   ; save array size low byte
.B2DE  A5 32    LDA $32   ; get end of arrays high byte
.B2E0  C8       INY   ; index to array size high byte
.B2E1  E5 60    SBC $60   ; subtract array start high byte
.B2E3  91 5F    STA ($5F),Y   ; save array size high byte
.B2E5  A5 0C    LDA $0C   ; get default DIM flag
.B2E7  D0 62    BNE $B34B   ; exit if this was a DIM command else, find element
.B2E9  C8       INY   ; set index to # of dimensions, the dimension indexes are on the stack and will be removed as the position of the array element is calculated
.B2EA  B1 5F    LDA ($5F),Y   ; get array's dimension count
.B2EC  85 0B    STA $0B   ; save it
.B2EE  A9 00    LDA #$00   ; clear byte
.B2F0  85 71    STA $71   ; clear array data pointer low byte
.B2F2  85 72    STA $72   ; save array data pointer high byte
.B2F4  C8       INY   ; increment index, point to array bound high byte
.B2F5  68       PLA   ; pull array index low byte
.B2F6  AA       TAX   ; copy to X
.B2F7  85 64    STA $64   ; save index low byte to FAC1 mantissa 3
.B2F9  68       PLA   ; pull array index high byte
.B2FA  85 65    STA $65   ; save index high byte to FAC1 mantissa 4
.B2FC  D1 5F    CMP ($5F),Y   ; compare with array bound high byte
.B2FE  90 0E    BCC $B30E   ; branch if within bounds
.B300  D0 06    BNE $B308   ; if outside bounds do bad subscript error else high byte was = so test low bytes
.B302  C8       INY   ; index to array bound low byte
.B303  8A       TXA   ; get array index low byte
.B304  D1 5F    CMP ($5F),Y   ; compare with array bound low byte
.B306  90 07    BCC $B30F   ; branch if within bounds
.B308  4C 45 B2 JMP $B245   ; do bad subscript error
.B30B  4C 35 A4 JMP $A435   ; do out of memory error then warm start
.B30E  C8       INY   ; index to array bound low byte
.B30F  A5 72    LDA $72   ; get array data pointer high byte
.B311  05 71    ORA $71   ; OR with array data pointer low byte
.B313  18       CLC   ; clear carry for either add, carry always clear here ??
.B314  F0 0A    BEQ $B320   ; branch if array data pointer = null, skip multiply
.B316  20 4C B3 JSR $B34C   ; compute array size
.B319  8A       TXA   ; get result low byte
.B31A  65 64    ADC $64   ; add index low byte from FAC1 mantissa 3
.B31C  AA       TAX   ; save result low byte
.B31D  98       TYA   ; get result high byte
.B31E  A4 22    LDY $22   ; restore index
.B320  65 65    ADC $65   ; add index high byte from FAC1 mantissa 4
.B322  86 71    STX $71   ; save array data pointer low byte
.B324  C6 0B    DEC $0B   ; decrement dimensions count
.B326  D0 CA    BNE $B2F2   ; loop if dimensions still to do
.B328  85 72    STA $72   ; save array data pointer high byte
.B32A  A2 05    LDX #$05   ; set default element size
.B32C  A5 45    LDA $45   ; get variable name 1st byte
.B32E  10 01    BPL $B331   ; branch if not string or floating point array
.B330  CA       DEX   ; decrement element size, $04
.B331  A5 46    LDA $46   ; get variable name 2nd byte
.B333  10 02    BPL $B337   ; branch if not integer or string
.B335  CA       DEX   ; decrement element size, $03
.B336  CA       DEX   ; decrement element size, $02
.B337  86 28    STX $28   ; save dimension size low byte
.B339  A9 00    LDA #$00   ; clear dimension size high byte
.B33B  20 55 B3 JSR $B355   ; compute array size
.B33E  8A       TXA   ; copy array size low byte
.B33F  65 58    ADC $58   ; add array data start pointer low byte
.B341  85 47    STA $47   ; save as current variable pointer low byte
.B343  98       TYA   ; copy array size high byte
.B344  65 59    ADC $59   ; add array data start pointer high byte
.B346  85 48    STA $48   ; save as current variable pointer high byte
.B348  A8       TAY   ; copy high byte to Y
.B349  A5 47    LDA $47   ; get current variable pointer low byte pointer to element is now in AY
.B34B  60       RTS   ; compute array size, result in XY
.B34C  84 22    STY $22   ; save index
.B34E  B1 5F    LDA ($5F),Y   ; get dimension size low byte
.B350  85 28    STA $28   ; save dimension size low byte
.B352  88       DEY   ; decrement index
.B353  B1 5F    LDA ($5F),Y   ; get dimension size high byte
.B355  85 29    STA $29   ; save dimension size high byte
.B357  A9 10    LDA #$10   ; count = $10 (16 bit multiply)
.B359  85 5D    STA $5D   ; save bit count
.B35B  A2 00    LDX #$00   ; clear result low byte
.B35D  A0 00    LDY #$00   ; clear result high byte
.B35F  8A       TXA   ; get result low byte
.B360  0A       ASL   ; *2
.B361  AA       TAX   ; save result low byte
.B362  98       TYA   ; get result high byte
.B363  2A       ROL   ; *2
.B364  A8       TAY   ; save result high byte
.B365  B0 A4    BCS $B30B   ; if overflow go do "Out of memory" error
.B367  06 71    ASL $71   ; shift element size low byte
.B369  26 72    ROL $72   ; shift element size high byte
.B36B  90 0B    BCC $B378   ; skip add if no carry
.B36D  18       CLC   ; else clear carry for add
.B36E  8A       TXA   ; get result low byte
.B36F  65 28    ADC $28   ; add dimension size low byte
.B371  AA       TAX   ; save result low byte
.B372  98       TYA   ; get result high byte
.B373  65 29    ADC $29   ; add dimension size high byte
.B375  A8       TAY   ; save result high byte
.B376  B0 93    BCS $B30B   ; if overflow go do "Out of memory" error
.B378  C6 5D    DEC $5D   ; decrement bit count
.B37A  D0 E3    BNE $B35F   ; loop until all done
.B37C  60       RTS   ; perform FRE()
.B37D  A5 0D    LDA $0D   ; get data type flag, $FF = string, $00 = numeric
.B37F  F0 03    BEQ $B384   ; branch if numeric
.B381  20 A6 B6 JSR $B6A6   ; pop string off descriptor stack, or from top of string space returns with A = length, X=$71=pointer low byte, Y=$72=pointer high byte FRE(n) was numeric so do this
.B384  20 26 B5 JSR $B526   ; go do garbage collection
.B387  38       SEC   ; set carry for subtract
.B388  A5 33    LDA $33   ; get bottom of string space low byte
.B38A  E5 31    SBC $31   ; subtract end of arrays low byte
.B38C  A8       TAY   ; copy result to Y
.B38D  A5 34    LDA $34   ; get bottom of string space high byte
.B38F  E5 32    SBC $32   ; subtract end of arrays high byte
```


## Commenti

### Original Disassembly (—)
- **$B24D**: set error $13, double dimension error
- **$B24F**: get DIM flag
- **$B251**: if we are trying to dimension it do error #X then warm start found the array and we're not dimensioning it so we must find an element in it
- **$B253**: set-up array pointer to first element in array
- **$B256**: get dimensions count
- **$B258**: set index to array's # of dimensions
- **$B25A**: compare with no of dimensions
- **$B25C**: if wrong do bad subscript error
- **$B25E**: found array so go get element array not found, so build it
- **$B261**: set-up array pointer to first element in array
- **$B264**: check available memory, do out of memory error if no room
- **$B267**: clear Y
- **$B269**: clear array data size high byte
- **$B26B**: set default element size
- **$B26D**: get variable name 1st byte
- **$B26F**: save array name 1st byte
- **$B271**: branch if not string or floating point array
- **$B273**: decrement element size, $04
- **$B274**: increment index
- **$B275**: get variable name 2nd byte
- **$B277**: save array name 2nd byte
- **$B279**: branch if not integer or string
- **$B27B**: decrement element size, $03
- **$B27C**: decrement element size, $02
- **$B27D**: save element size
- **$B27F**: get dimensions count
- **$B281**: increment index ..
- **$B282**: .. to array  ..
- **$B283**: .. dimension count
- **$B284**: save array dimension count
- **$B286**: set default dimension size low byte
- **$B288**: set default dimension size high byte
- **$B28A**: test DIM flag
- **$B28C**: branch if default to be used
- **$B28E**: pull dimension size low byte
- **$B28F**: clear carry for add
- **$B290**: add 1, allow for zeroeth element
- **$B292**: copy low byte to X
- **$B293**: pull dimension size high byte
- **$B294**: add carry to high byte
- **$B296**: increment index to dimension size high byte
- **$B297**: save dimension size high byte
- **$B299**: increment index to dimension size low byte
- **$B29A**: copy dimension size low byte
- **$B29B**: save dimension size low byte
- **$B29D**: compute array size
- **$B2A0**: save result low byte
- **$B2A2**: save result high byte
- **$B2A4**: restore index
- **$B2A6**: decrement dimensions count
- **$B2A8**: loop if not all done
- **$B2AA**: add array data pointer high byte
- **$B2AC**: if overflow do out of memory error then warm start
- **$B2AE**: save array data pointer high byte
- **$B2B0**: copy array data pointer high byte
- **$B2B1**: copy array size low byte
- **$B2B2**: add array data pointer low byte
- **$B2B4**: branch if no rollover
- **$B2B6**: else increment next array pointer high byte
- **$B2B7**: if rolled over do out of memory error then warm start
- **$B2B9**: check available memory, do out of memory error if no room
- **$B2BC**: set end of arrays low byte
- **$B2BE**: set end of arrays high byte now the array is created we need to zero all the elements in it
- **$B2C0**: clear A for array clear
- **$B2C2**: increment array size high byte, now block count
- **$B2C4**: get array size low byte, now index to block
- **$B2C6**: branch if $00
- **$B2C8**: decrement index, do 0 to n-1
- **$B2C9**: clear array element byte
- **$B2CB**: loop until this block done
- **$B2CD**: decrement array pointer high byte
- **$B2CF**: decrement block count high byte
- **$B2D1**: loop until all blocks done
- **$B2D3**: correct for last loop
- **$B2D5**: set carry for subtract
- **$B2D6**: get end of arrays low byte
- **$B2D8**: subtract array start low byte
- **$B2DA**: index to array size low byte
- **$B2DC**: save array size low byte
- **$B2DE**: get end of arrays high byte
- **$B2E0**: index to array size high byte
- **$B2E1**: subtract array start high byte
- **$B2E3**: save array size high byte
- **$B2E5**: get default DIM flag
- **$B2E7**: exit if this was a DIM command else, find element
- **$B2E9**: set index to # of dimensions, the dimension indexes are on the stack and will be removed as the position of the array element is calculated
- **$B2EA**: get array's dimension count
- **$B2EC**: save it
- **$B2EE**: clear byte
- **$B2F0**: clear array data pointer low byte
- **$B2F2**: save array data pointer high byte
- **$B2F4**: increment index, point to array bound high byte
- **$B2F5**: pull array index low byte
- **$B2F6**: copy to X
- **$B2F7**: save index low byte to FAC1 mantissa 3
- **$B2F9**: pull array index high byte
- **$B2FA**: save index high byte to FAC1 mantissa 4
- **$B2FC**: compare with array bound high byte
- **$B2FE**: branch if within bounds
- **$B300**: if outside bounds do bad subscript error else high byte was = so test low bytes
- **$B302**: index to array bound low byte
- **$B303**: get array index low byte
- **$B304**: compare with array bound low byte
- **$B306**: branch if within bounds
- **$B308**: do bad subscript error
- **$B30B**: do out of memory error then warm start
- **$B30E**: index to array bound low byte
- **$B30F**: get array data pointer high byte
- **$B311**: OR with array data pointer low byte
- **$B313**: clear carry for either add, carry always clear here ??
- **$B314**: branch if array data pointer = null, skip multiply
- **$B316**: compute array size
- **$B319**: get result low byte
- **$B31A**: add index low byte from FAC1 mantissa 3
- **$B31C**: save result low byte
- **$B31D**: get result high byte
- **$B31E**: restore index
- **$B320**: add index high byte from FAC1 mantissa 4
- **$B322**: save array data pointer low byte
- **$B324**: decrement dimensions count
- **$B326**: loop if dimensions still to do
- **$B328**: save array data pointer high byte
- **$B32A**: set default element size
- **$B32C**: get variable name 1st byte
- **$B32E**: branch if not string or floating point array
- **$B330**: decrement element size, $04
- **$B331**: get variable name 2nd byte
- **$B333**: branch if not integer or string
- **$B335**: decrement element size, $03
- **$B336**: decrement element size, $02
- **$B337**: save dimension size low byte
- **$B339**: clear dimension size high byte
- **$B33B**: compute array size
- **$B33E**: copy array size low byte
- **$B33F**: add array data start pointer low byte
- **$B341**: save as current variable pointer low byte
- **$B343**: copy array size high byte
- **$B344**: add array data start pointer high byte
- **$B346**: save as current variable pointer high byte
- **$B348**: copy high byte to Y
- **$B349**: get current variable pointer low byte pointer to element is now in AY
- **$B34B**: compute array size, result in XY
- **$B34C**: save index
- **$B34E**: get dimension size low byte
- **$B350**: save dimension size low byte
- **$B352**: decrement index
- **$B353**: get dimension size high byte
- **$B355**: save dimension size high byte
- **$B357**: count = $10 (16 bit multiply)
- **$B359**: save bit count
- **$B35B**: clear result low byte
- **$B35D**: clear result high byte
- **$B35F**: get result low byte
- **$B360**: *2
- **$B361**: save result low byte
- **$B362**: get result high byte
- **$B363**: *2
- **$B364**: save result high byte
- **$B365**: if overflow go do "Out of memory" error
- **$B367**: shift element size low byte
- **$B369**: shift element size high byte
- **$B36B**: skip add if no carry
- **$B36D**: else clear carry for add
- **$B36E**: get result low byte
- **$B36F**: add dimension size low byte
- **$B371**: save result low byte
- **$B372**: get result high byte
- **$B373**: add dimension size high byte
- **$B375**: save result high byte
- **$B376**: if overflow go do "Out of memory" error
- **$B378**: decrement bit count
- **$B37A**: loop until all done
- **$B37C**: perform FRE()
- **$B37D**: get data type flag, $FF = string, $00 = numeric
- **$B37F**: branch if numeric
- **$B381**: pop string off descriptor stack, or from top of string space returns with A = length, X=$71=pointer low byte, Y=$72=pointer high byte FRE(n) was numeric so do this
- **$B384**: go do garbage collection
- **$B387**: set carry for subtract
- **$B388**: get bottom of string space low byte
- **$B38A**: subtract end of arrays low byte
- **$B38C**: copy result to Y
- **$B38D**: get bottom of string space high byte
- **$B38F**: subtract end of arrays high byte

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B24D**: SET UP FOR REDIM'D ARRAY ERROR
- **$B24F**: CALLED FROM "DIM" STATEMENT?
- **$B251**: YES, ERROR
- **$B253**: SET (ARYPNT) = ADDR OF FIRST ELEMENT
- **$B256**: COMPARE NUMBER OF DIMENSIONS
- **$B25C**: NOT SAME, SUBSCRIPT ERROR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*