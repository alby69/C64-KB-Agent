---
title: concatenate
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
- b63d-concatenate-two-strings
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $B63D
  address_end: $B677
  symbol: concatenate
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B63D**: get descriptor pointer high byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B63D**: SAVE ADDRESS OF FIRST DESCRIPTOR'
---

# $B63D — concatenate

## Disassemblatura
```assembly
.B63D  A5 65    LDA $65   ; get descriptor pointer high byte
.B63F  48       PHA   ; put on stack
.B640  A5 64    LDA $64   ; get descriptor pointer low byte
.B642  48       PHA   ; put on stack
.B643  20 83 AE JSR $AE83   ; get value from line
.B646  20 8F AD JSR $AD8F   ; check if source is string, else do type mismatch
.B649  68       PLA   ; get descriptor pointer low byte back
.B64A  85 6F    STA $6F   ; set pointer low byte
.B64C  68       PLA   ; get descriptor pointer high byte back
.B64D  85 70    STA $70   ; set pointer high byte
.B64F  A0 00    LDY #$00   ; clear index
.B651  B1 6F    LDA ($6F),Y   ; get length of first string from descriptor
.B653  18       CLC   ; clear carry for add
.B654  71 64    ADC ($64),Y   ; add length of second string
.B656  90 05    BCC $B65D   ; branch if no overflow
.B658  A2 17    LDX #$17   ; else error $17, string too long error
.B65A  4C 37 A4 JMP $A437   ; do error #X then warm start
.B65D  20 75 B4 JSR $B475   ; copy descriptor pointer and make string space A bytes long
.B660  20 7A B6 JSR $B67A   ; copy string from descriptor to utility pointer
.B663  A5 50    LDA $50   ; get descriptor pointer low byte
.B665  A4 51    LDY $51   ; get descriptor pointer high byte
.B667  20 AA B6 JSR $B6AA   ; pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.B66A  20 8C B6 JSR $B68C   ; store string from pointer to utility pointer
.B66D  A5 6F    LDA $6F   ; get descriptor pointer low byte
.B66F  A4 70    LDY $70   ; get descriptor pointer high byte
.B671  20 AA B6 JSR $B6AA   ; pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.B674  20 CA B4 JSR $B4CA   ; check space on descriptor stack then put string address and length on descriptor stack and update stack pointers
.B677  4C B8 AD JMP $ADB8   ; continue evaluation
```


## Commenti

### Original Disassembly (—)
- **$B63D**: get descriptor pointer high byte
- **$B63F**: put on stack
- **$B640**: get descriptor pointer low byte
- **$B642**: put on stack
- **$B643**: get value from line
- **$B646**: check if source is string, else do type mismatch
- **$B649**: get descriptor pointer low byte back
- **$B64A**: set pointer low byte
- **$B64C**: get descriptor pointer high byte back
- **$B64D**: set pointer high byte
- **$B64F**: clear index
- **$B651**: get length of first string from descriptor
- **$B653**: clear carry for add
- **$B654**: add length of second string
- **$B656**: branch if no overflow
- **$B658**: else error $17, string too long error
- **$B65A**: do error #X then warm start
- **$B65D**: copy descriptor pointer and make string space A bytes long
- **$B660**: copy string from descriptor to utility pointer
- **$B663**: get descriptor pointer low byte
- **$B665**: get descriptor pointer high byte
- **$B667**: pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$B66A**: store string from pointer to utility pointer
- **$B66D**: get descriptor pointer low byte
- **$B66F**: get descriptor pointer high byte
- **$B671**: pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$B674**: check space on descriptor stack then put string address and length on descriptor stack and update stack pointers
- **$B677**: continue evaluation

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B63D**: SAVE ADDRESS OF FIRST DESCRIPTOR
- **$B643**: GET SECOND STRING ELEMENT
- **$B646**: MUST BE A STRING
- **$B649**: RECOVER ADDRES OF 1ST DESCRIPTOR
- **$B651**: ADD LENGTHS, GET CONCATENATED SIZE
- **$B656**: OK IF < $100
- **$B65D**: GET SPACE FOR CONCATENATED STRINGS
- **$B660**: MOVE 1ST STRING
- **$B66A**: MOVE 2ND STRING
- **$B674**: SET UP DESCRIPTOR
- **$B677**: FINISH EXPRESSION GET STRING DESCRIPTOR POINTED AT BY (STRNG1) AND MOVE DESCRIBED STRING TO (FRESPC)
- **$B67E**: LENGTH
- **$B682**: PUT STRING POINTER IN X,Y
- **$B687**: RETRIEVE LENGTH MOVE STRING AT (Y,X) WITH LENGTH (A) TO DESTINATION WHOSE ADDRESS IS IN FRESPC,FRESPC+1
- **$B688**: PUT POINTER IN INDEX
- **$B68C**: LENGTH TO Y-REG
- **$B68D**: IF LENGTH IS ZERO, FINISHED
- **$B68F**: SAVE LENGTH ON STACK
- **$B690**: MOVE BYTES FROM (INDEX) TO (FRESPC)
- **$B695**: TEST IF ANY LEFT TO MOVE
- **$B696**: YES, KEEP MOVING
- **$B698**: NO, FINISHED.  GET LENGTH
- **$B699**: AND ADD TO FRESPC, SO
- **$B69A**: FRESPC POINTS TO NEXT HIGHER
- **$B69C**: BYTE.  (USED BY CONCATENATION)
- **$B6A2**: IF (FAC) IS A TEMPORARY STRING, RELEASE DESCRIPTOR
- **$B6A3**: LAST RESULT A STRING? IF STRING DESCRIPTOR POINTED TO BY FAC+3,4 IS A TEMPORARY STRING, RELEASE IT.
- **$B6A6**: GET DESCRIPTOR POINTER
- **$B6A8**: IF STRING DESCRIPTOR WHOSE ADDRESS IS IN Y,A IS A TEMPORARY STRING, RELEASE IT.
- **$B6AA**: SAVE THE ADDRESS OF THE DESCRIPTOR
- **$B6AE**: FREE DESCRIPTOR IF IT IS TEMPORARY
- **$B6B1**: REMEMBER IF TEMP
- **$B6B2**: POINT AT LENGTH OF STRING
- **$B6B6**: SAVE LENGTH ON STACK
- **$B6BA**: GET ADDRESS OF STRING IN Y,X
- **$B6BF**: LENGTH IN A
- **$B6C0**: RETRIEVE STATUS, Z=1 IF TEMP
- **$B6C1**: NOT A TEMPORARY STRING
- **$B6C3**: IS IT THE LOWEST STRING?
- **$B6C5**: NO
- **$B6C9**: NO
- **$B6CB**: YES, PUSH LENGTH AGAIN
- **$B6CC**: RECOVER THE SPACE USED BY
- **$B6CD**: THE STRING
- **$B6D5**: RETRIEVE LENGTH AGAIN
- **$B6D6**: ADDRESS OF STRING IN Y,X
- **$B6D8**: LENGTH OF STRING IN A-REG
- **$B6DA**: RELEASE TEMPORARY DESCRIPTOR IF Y,A = LASTPT
- **$B6DB**: COMPARE Y,A TO LATEST TEMP
- **$B6DD**: NOT SAME ONE, CANNOT RELEASE
- **$B6E1**: NOT SAME ONE, CANNOT RELEASE
- **$B6E3**: UPDATE TEMPT FOR NEXT TEMP
- **$B6E5**: BACK OFF LASTPT
- **$B6E9**: NOW Y,A POINTS TO TOP TEMP
- **$B6EB**: Z=0 IF NOT TEMP, Z=1 IF TEMP

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*