---
title: print "..." string to string utility area
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
- aebd-string-constant-element
- aed4-basic-befehl-not
- aee3-comparison-for-equality-operator
- aef1-holt-term-in-klammern
- aef7-prft-auf-zeichen-im-b-text
- aeff-unless-char-at-txtptr-a-syntax-error
- af0d-recursive-get-value
- bit
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $AEBD
  address_end: $AF11
  symbol: print-string-to-string-utility-area
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AEBD**: get BASIC execute pointer low byte'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AEBD**: ADD (CARRY) TO GET ADDRESS OF 1ST CHAR'
---

# $AEBD — print "..." string to string utility area

## Disassemblatura
```assembly
.AEBD  A5 7A    LDA $7A   ; get BASIC execute pointer low byte
.AEBF  A4 7B    LDY $7B   ; get BASIC execute pointer high byte
.AEC1  69 00    ADC #$00   ; add carry to low byte
.AEC3  90 01    BCC $AEC6   ; branch if no overflow
.AEC5  C8       INY   ; increment high byte
.AEC6  20 87 B4 JSR $B487   ; print " terminated string to utility pointer
.AEC9  4C E2 B7 JMP $B7E2   ; restore BASIC execute pointer from temp and return get value from line .. continued wasn't a string so ...
.AECC  C9 A8    CMP #$A8   ; compare with token for NOT
.AECE  D0 13    BNE $AEE3   ; branch if not token for NOT was NOT token
.AED0  A0 18    LDY #$18   ; offset to NOT function
.AED2  D0 3B    BNE $AF0F   ; do set-up for function then execute, branch always do = compare
.AED4  20 BF B1 JSR $B1BF   ; evaluate integer expression, no sign check
.AED7  A5 65    LDA $65   ; get FAC1 mantissa 4
.AED9  49 FF    EOR #$FF   ; invert it
.AEDB  A8       TAY   ; copy it
.AEDC  A5 64    LDA $64   ; get FAC1 mantissa 3
.AEDE  49 FF    EOR #$FF   ; invert it
.AEE0  4C 91 B3 JMP $B391   ; convert fixed integer AY to float FAC1 and return get value from line .. continued wasn't a string or NOT so ...
.AEE3  C9 A5    CMP #$A5   ; compare with token for FN
.AEE5  D0 03    BNE $AEEA   ; branch if not token for FN
.AEE7  4C F4 B3 JMP $B3F4   ; else go evaluate FNx get value from line .. continued wasn't a string, NOT or FN so ...
.AEEA  C9 B4    CMP #$B4   ; compare with token for SGN
.AEEC  90 03    BCC $AEF1   ; if less than SGN token evaluate expression in parentheses else was a function token
.AEEE  4C A7 AF JMP $AFA7   ; go set up function references, branch always get value from line .. continued if here it can only be something in brackets so .... evaluate expression within parentheses
.AEF1  20 FA AE JSR $AEFA   ; scan for "(", else do syntax error then warm start
.AEF4  20 9E AD JSR $AD9E   ; evaluate expression all the 'scan for' routines return the character after the sought character scan for ")", else do syntax error then warm start
.AEF7  A9 29    LDA #$29   ; load A with ")"
.AEF9  2C       .BYTE $2C   ; makes next line BIT $28A9 scan for "(", else do syntax error then warm start
.AEFA  A9 28    LDA #$28   ; load A with "("
.AEFC  2C       .BYTE $2C   ; makes next line BIT $2CA9 scan for ",", else do syntax error then warm start
.AEFD  A9 2C    LDA #$2C   ; load A with "," scan for CHR$(A), else do syntax error then warm start
.AEFF  A0 00    LDY #$00   ; clear index
.AF01  D1 7A    CMP ($7A),Y   ; compare with BASIC byte
.AF03  D0 03    BNE $AF08   ; if not expected byte do syntax error then warm start
.AF05  4C 73 00 JMP $0073   ; else increment and scan memory and return syntax error then warm start
.AF08  A2 0B    LDX #$0B   ; error code $0B, syntax error
.AF0A  4C 37 A4 JMP $A437   ; do error #X then warm start
.AF0D  A0 15    LDY #$15   ; set offset from base to > operator
.AF0F  68       PLA   ; dump return address low byte
.AF10  68       PLA   ; dump return address high byte
.AF11  4C FA AD JMP $ADFA   ; execute function then continue evaluation
```


## Commenti

### Original Disassembly (—)
- **$AEBD**: get BASIC execute pointer low byte
- **$AEBF**: get BASIC execute pointer high byte
- **$AEC1**: add carry to low byte
- **$AEC3**: branch if no overflow
- **$AEC5**: increment high byte
- **$AEC6**: print " terminated string to utility pointer
- **$AEC9**: restore BASIC execute pointer from temp and return get value from line .. continued wasn't a string so ...
- **$AECC**: compare with token for NOT
- **$AECE**: branch if not token for NOT was NOT token
- **$AED0**: offset to NOT function
- **$AED2**: do set-up for function then execute, branch always do = compare
- **$AED4**: evaluate integer expression, no sign check
- **$AED7**: get FAC1 mantissa 4
- **$AED9**: invert it
- **$AEDB**: copy it
- **$AEDC**: get FAC1 mantissa 3
- **$AEDE**: invert it
- **$AEE0**: convert fixed integer AY to float FAC1 and return get value from line .. continued wasn't a string or NOT so ...
- **$AEE3**: compare with token for FN
- **$AEE5**: branch if not token for FN
- **$AEE7**: else go evaluate FNx get value from line .. continued wasn't a string, NOT or FN so ...
- **$AEEA**: compare with token for SGN
- **$AEEC**: if less than SGN token evaluate expression in parentheses else was a function token
- **$AEEE**: go set up function references, branch always get value from line .. continued if here it can only be something in brackets so .... evaluate expression within parentheses
- **$AEF1**: scan for "(", else do syntax error then warm start
- **$AEF4**: evaluate expression all the 'scan for' routines return the character after the sought character scan for ")", else do syntax error then warm start
- **$AEF7**: load A with ")"
- **$AEF9**: makes next line BIT $28A9 scan for "(", else do syntax error then warm start
- **$AEFA**: load A with "("
- **$AEFC**: makes next line BIT $2CA9 scan for ",", else do syntax error then warm start
- **$AEFD**: load A with "," scan for CHR$(A), else do syntax error then warm start
- **$AEFF**: clear index
- **$AF01**: compare with BASIC byte
- **$AF03**: if not expected byte do syntax error then warm start
- **$AF05**: else increment and scan memory and return syntax error then warm start
- **$AF08**: error code $0B, syntax error
- **$AF0A**: do error #X then warm start
- **$AF0D**: set offset from base to > operator
- **$AF0F**: dump return address low byte
- **$AF10**: dump return address high byte
- **$AF11**: execute function then continue evaluation

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AEBD**: ADD (CARRY) TO GET ADDRESS OF 1ST CHAR
- **$AEBF**: OF STRING IN Y,A
- **$AEC6**: BUILD DESCRIPTOR TO STRING GET ADDRESS OF DESCRIPTOR IN FAC
- **$AEC9**: POINT TXTPTR AFTER TRAILING QUOTE
- **$AECE**: NOT "NOT", TRY "FN"
- **$AED0**: POINT AT = COMPARISON
- **$AED2**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*