---
title: perform STR$()
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
- b465-basic-funktion-str
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B465
  address_end: $B473
  symbol: perform-str
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B465**: check if source is numeric, else do type mismatch'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B465**: prüft auf numerisch'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B465**: EXPRESSION MUST BE NUMERIC'
---

# $B465 — perform STR$()

## Disassemblatura
```assembly
.B465  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.B468  A0 00    LDY #$00   ; set string index
.B46A  20 DF BD JSR $BDDF   ; convert FAC1 to string
.B46D  68       PLA   ; dump return address (skip type check)
.B46E  68       PLA   ; dump return address (skip type check)
.B46F  A9 FF    LDA #$FF   ; set result string low pointer
.B471  A0 00    LDY #$00   ; set result string high pointer
.B473  F0 12    BEQ $B487   ; print null terminated string to utility pointer
```


## Commenti

### Original Disassembly (—)
- **$B465**: check if source is numeric, else do type mismatch
- **$B468**: set string index
- **$B46A**: convert FAC1 to string
- **$B46D**: dump return address (skip type check)
- **$B46E**: dump return address (skip type check)
- **$B46F**: set result string low pointer
- **$B471**: set result string high pointer
- **$B473**: print null terminated string to utility pointer

### Commodore-64-intern-Buch (Commodore)
- **$B465**: prüft auf numerisch
- **$B468**: Wert laden und
- **$B46A**: FAC nach ASCII umwandeln
- **$B46D**: Rücksprungadresse vom
- **$B46E**: Stapel entfernen
- **$B46F**: LOW-Byte
- **$B471**: Startadresse des Strings=$FF

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B465**: EXPRESSION MUST BE NUMERIC
- **$B468**: START STRING AT STACK-1 ($00FF) SO STRLIT CAN DIFFRENTIATE STR$ CALLS
- **$B46A**: CONVERT FAC TO STRING
- **$B46D**: POP RETURN OFF STACK
- **$B46F**: POINT TO STACK-1
- **$B471**: (WHICH=0)
- **$B473**: ...ALWAYS, CREATE DESC &amp; MOVE STRING GET SPACE AND MAKE DESCRIPTOR FOR STRING WHOSE ADDRESS IS IN FAC+3,4 AND WHOSE LENGTH IS IN A-REG
- **$B475**: Y,X = STRING ADDRESS
- **$B47B**: GET SPACE AND MAKE DESCRIPTOR FOR STRING WHOSE ADDRESS IS IN Y,X AND WHOSE LENGTH IS IN A-REG
- **$B47D**: A HOLDS LENGTH
- **$B480**: SAVE DESCRIPTOR IN FAC
- **$B482**: ---FAC--- --FAC+1-- --FAC+2--
- **$B484**: <LENGTH>  <ADDR-LO> <ADDR-HI>
- **$B486**: BUILD A DESCRIPTOR FOR STRING STARTING AT Y,A AND TERMINATED BY $00 OR QUOTATION MARK RETURN WITH DESCRIPTOR IN A TEMPORARY AND ADDRESS OF DESCRIPTOR IN FAC+3,4
- **$B487**: SET UP LITERAL SCAN TO STOP ON
- **$B489**: QUOTATION MARK OR $00
- **$B48B**: BUILD A DESCRIPTOR FOR STRING STARTING AT Y,A AND TERMINATED BY $00, (CHARAC), OR (ENDCHR) RETURN WITH DESCRIPTOR IN A TEMPORARY AND ADDRESS OF DESCRIPTOR IN FAC+3,4
- **$B48D**: SAVE ADDRESS OF STRING
- **$B491**: ...AGAIN
- **$B497**: FIND END OF STRING
- **$B498**: NEXT STRING CHAR
- **$B49A**: END OF STRING
- **$B49C**: ALTERNATE TERMINATOR # 1?
- **$B49E**: YES
- **$B4A0**: ALTERNATE TERMINATOR # 2?
- **$B4A2**: NO, KEEP SCANNING
- **$B4A4**: IS STRING ENDED WITH QUOTE MARK?
- **$B4A6**: YES, C=1 TO INCLUDE " IN STRING
- **$B4A9**: SAVE LENGTH
- **$B4AC**: COMPUTE ADDRESS OF END OF STRING
- **$B4AE**: (OF 00 BYTE, OR JUST AFTER ")
- **$B4B7**: WHERE DOES THE STRING START?
- **$B4B9**: PAGE 0, MUST BE FROM STR$ FUNCTION
- **$B4BB**: PAGE 2?
- **$B4BD**: NO, NOT PAGE 0 OR 2
- **$B4BF**: LENGTH OF STRING
- **$B4C0**: MAKE SPACE FOR STRING
- **$B4C7**: MOVE IT IN STORE DESCRIPTOR IN TEMPORARY DESCRIPTOR STACK THE DESCRIPTOR IS NOW IN FAC, FAC+1, FAC+2 PUT ADDRESS OF TEMP DESCRIPTOR IN FAC+3,4
- **$B4CA**: POINTER TO NEXT TEMP STRING SLOT
- **$B4CC**: MAX OF 3 TEMP STRINGS
- **$B4CE**: ROOM FOR ANOTHER ONE
- **$B4D0**: TOO MANY, FORMULA TOO COMPLEX
- **$B4D5**: COPY TEMP DESCRIPTOR INTO TEMP STACK
- **$B4E3**: ADDRESS OF TEMP DESCRIPTOR
- **$B4E5**: IN Y,X AND FAC+3,4
- **$B4E9**: Y=$FF
- **$B4EA**: FLAG (FAC ) AS STRING
- **$B4EC**: INDEX OF LAST POINTER
- **$B4EE**: UPDATE FOR NEXT TEMP ENTRY
- **$B4F3**: MAKE SPACE FOR STRING AT BOTTOM OF STRING SPACE (A)=# BYTES SPACE TO MAKE RETURN WITH (A) SAME, AND Y,X = ADDRESS OF SPACE ALLOCATED
- **$B4F4**: CLEAR SIGNBIT OF FLAG
- **$B4F6**: A HOLDS LENGTH
- **$B4F7**: GET -LENGTH
- **$B4FA**: COMPUTE STARTING ADDRESS OF SPACE
- **$B4FC**: FOR THE STRING
- **$B501**: SEE IF FITS IN REMAINING MEMORY
- **$B503**: NO, TRY GARBAGE
- **$B505**: YES, IT FITS
- **$B507**: HAVE TO CHECK LOWER BYTES
- **$B509**: NOT ENUF ROOM YET
- **$B50B**: THERE IS ROOM SO SAVE NEW FRETOP
- **$B513**: ADDR IN Y,X
- **$B514**: LENGTH IN A
- **$B518**: GARBAGE DONE YET?
- **$B51A**: YES, MEMORY IS REALLY FULL
- **$B51C**: NO, TRY COLLECTING NOW
- **$B51F**: FLAG THAT COLLECTED GARBAGE ALREADY
- **$B523**: GET STRING LENGTH AGAIN
- **$B524**: ...ALWAYS SHOVE ALL REFERENCED STRINGS AS HIGH AS POSSIBLE IN MEMORY (AGAINST HIMEM) FREEING UP SPACE BELOW STRING AREA DOWN TO STREND.
- **$B526**: COLLECT FROM TOP DOWN
- **$B52A**: ONE PASS THROUGH ALL VARS
- **$B52C**: FOR EACH ACTIVE STRING!
- **$B530**: FLAG IN CASE NO STRINGS TO COLLECT
- **$B53A**: START BY COLLECTING TEMPORARIES
- **$B544**: FINISHED WITH TEMPS YET?
- **$B546**: YES, NOW DO SIMPLE VARIABLES
- **$B548**: DO A TEMP
- **$B54B**: ...ALWAYS NOW COLLECT SIMPLE VARIABLES
- **$B54D**: LENGTH OF EACH VARIABLE IS 7 BYTES
- **$B551**: START AT BEGINNING OF VARTAB
- **$B559**: FINISHED WITH SIMPLE VARIABLES?
- **$B55B**: NO
- **$B55D**: MAYBE, CHECK LO-BYTE
- **$B55F**: YES, NOW DO ARRAYS
- **$B564**: ...ALWAYS NOW COLLECT ARRAY VARIABLES
- **$B56A**: DESCRIPTORS IN ARRAYS ARE 3-BYTES EACH
- **$B56E**: COMPARE TO END OF ARRAYS
- **$B572**: FINISHED WITH ARRAYS YET?
- **$B574**: NOT YET
- **$B576**: MAYBE, CHECK LO-BYTE
- **$B578**: NOT FINISHED YET
- **$B57A**: FINISHED
- **$B57D**: SET UP PNTR TO START OF ARRAY
- **$B581**: POINT AT NAME OF ARRAY
- **$B585**: 1ST LETTER OF NAME IN X-REG
- **$B589**: STATUS FROM SECOND LETTER OF NAME
- **$B58B**: OFFSET TO NEXT ARRAY
- **$B58D**: (CARRY ALWAYS CLEAR)
- **$B58F**: CALCULATE START OF NEXT ARRAY
- **$B592**: HI-BYTE OF OFFSET
- **$B598**: GET STATUS FROM 2ND CHAR OF NAME
- **$B599**: NOT A STRING ARRAY
- **$B59B**: SET STATUS WITH 1ST CHAR OF NAME
- **$B59C**: NOT A STRING ARRAY
- **$B59F**: # OF DIMENSIONS FOR THIS ARRAY
- **$B5A3**: PREAMBLE SIZE = 2*#DIMS + 5
- **$B5A6**: MAKE INDEX POINT AT FIRST ELEMENT
- **$B5A8**: IN THE ARRAY
- **$B5AE**: STEP THRU EACH STRING IN THIS ARRAY
- **$B5B0**: ARRAY DONE?
- **$B5B2**: NO, PROCESS NEXT ELEMENT
- **$B5B4**: MAYBE, CHECK LO-BYTE
- **$B5B6**: YES, MOVE TO NEXT ARRAY
- **$B5B8**: PROCESS THE ARRAY
- **$B5BB**: ...ALWAYS PROCESS A SIMPLE VARIABLE
- **$B5BD**: LOOK AT 1ST CHAR OF NAME
- **$B5BF**: NOT A STRING VARIABLE
- **$B5C2**: LOOK AT 2ND CHAR OF NAME
- **$B5C4**: NOT A STRING VARIABLE
- **$B5C6**: IF STRING IS NOT EMPTY, CHECK IF IT IS HIGHEST
- **$B5C7**: GET LENGTH OF STRING
- **$B5C9**: IGNORE STRING IF LENGTH IS ZERO
- **$B5CC**: GET ADDRESS OF STRING
- **$B5D2**: CHECK IF ALREADY COLLECTED
- **$B5D4**: NO, BELOW FRETOP
- **$B5D6**: YES, ABOVE FRETOP
- **$B5D8**: MAYBE, CHECK LO-BYTE
- **$B5DA**: YES, ABOVE FRETOP
- **$B5DC**: ABOVE HIGHEST STRING FOUND?
- **$B5DE**: NO, IGNORE FOR NOW
- **$B5E0**: YES, THIS IS THE NEW HIGHEST
- **$B5E2**: MAYBE, TRY LO-BYTE
- **$B5E4**: NO, IGNORE FOR NOW
- **$B5E6**: MAKE THIS THE HIGHEST STRING
- **$B5EA**: SAVE ADDRESS OF DESCRIPTOR TOO
- **$B5F4**: ADD (DSCLEN) TO PNTR IN INDEX RETURN WITH Y=0, PNTR ALSO IN X,A
- **$B5F6**: BUMP TO NEXT VARIABLE
- **$B605**: FOUND HIGHEST NON-EMPTY STRING, SO MOVE IT TO TOP AND GO BACK FOR ANOTHER

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*