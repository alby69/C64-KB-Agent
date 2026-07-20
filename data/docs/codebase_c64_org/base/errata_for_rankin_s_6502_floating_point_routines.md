---
title: ERRATA FOR RANKIN'S 6502 FLOATING POINT ROUTINES
source_url: https://codebase.c64.org/doku.php?id=base%3Aerrata_for_rankin_s_6502_floating_point_routines
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# ERRATA FOR RANKIN'S 6502 FLOATING POINT ROUTINES

base:errata_for_rankin_s_6502_floating_point_routines

                # ERRATA FOR RANKIN'S 6502 FLOATING POINT ROUTINES

```
Dr. Dobb's Journal, November/December 1976, page 57.
Sept. 22, 1976
Dear Jim,
Subsequent to the publication of "Floating Point
Routines for the 6502" (Vol.1, No.7) an error which I made in
the LOG routine came to light which causes improper results
if the argument is less than 1.  The following changes will
correct the error.
1.  After:            CONT JSR SWAP (1D07)
    Add:    A2 00          LDX =0    LOAD X FOR HIGH BYTE OF EXPONENT
2.  After:                 STA M1+1 (1D12)
    Delete:                LDA =0
                           STA M1
    Add:    10 01          BPL *+3   IS EXPONENT NEGATIVE
            CA             DEX       YES, SET X TO $FF
            86 09          STX M1    SET UPPER BYTE OF EXPONENT
3.  Changes 1 and 2 shift the code by 3 bytes so add 3 to the
addresses of the constants LN10 through MHLF whenever
they are referenced.  For example the address of LN10 changes
from 1DCD to 1DD0.  Note also that the entry point for
LOG10 becomes 1DBF.  The routines stays within the page
and hence the following routines (EXP etc.) are not affected.
Yours truly,
Roy Rankin
Dep. of Mech. Eng.
Stanford University
```
base/errata_for_rankin_s_6502_floating_point_routines.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
Dr. Dobb's Journal, November/December 1976, page 57.

Sept. 22, 1976

Dear Jim,

Subsequent to the publication of "Floating Point
Routines for the 6502" (Vol.1, No.7) an error which I made in
the LOG routine came to light which causes improper results
if the argument is less than 1.  The following changes will
correct the error.

1.  After:            CONT JSR SWAP (1D07)
    Add:    A2 00          LDX =0    LOAD X FOR HIGH BYTE OF EXPONENT

2.  After:                 STA M1+1 (1D12)
    Delete:                LDA =0
                           STA M1
    Add:    10 01          BPL *+3   IS EXPONENT NEGATIVE
            CA             DEX       YES, SET X TO $FF
            86 09          STX M1    SET UPPER BYTE OF EXPONENT

3.  Changes 1 and 2 shift the code by 3 bytes so add 3 to the
addresses of the constants LN10 through MHLF whenever
they are referenced.  For example the address of LN10 changes
from 1DCD to 1DD0.  Note also that the entry point for
LOG10 becomes 1DBF.  The routines stays within the page
and hence the following routines (EXP etc.) are not affected.

Yours truly,

Roy Rankin
Dep. of Mech. Eng.
Stanford University
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aerrata_for_rankin_s_6502_floating_point_routines](https://codebase.c64.org/doku.php?id=base%3Aerrata_for_rankin_s_6502_floating_point_routines)*
