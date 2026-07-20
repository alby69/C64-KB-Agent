---
title: DEX
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_dex
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware:
- CIA
related:
- keyboard-handling
- cia-registers
- joystick-reading
scraped_at: '2026-07-20'
---

# DEX

base:supercpu_dex

                # DEX

Dex does not need a special pseudocommand, this is only for conveniance.

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: dex16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to Decrease X with.
    //
    // SYNTAX:
    //   dex16 Value
    //
    // EXAMPLE:
    //   dex16                                   // Decrease X with 1
    //   dex16 1                                 // Decrease X with 1
    //   dex16 2                                 // Decrease X with 2
    //   dex16 8                                 // Decrease X with 8
    //
    // PARAMETERS:
    //                       Value     Min       Max
    //   Value                U16       0       65535
    //---------------------------------------------------------------------------------------------
    .pseudocommand dex16 val {
        .if (val.getType()==AT_NONE) {
            dex
        } else {
            .if (val.getValue()==1) {
                dex
            }
            .if (val.getValue()==2){
                dex
                dex
            }
            .if (val.getValue()==3){
                dex
                dex
                dex
            }
            .if (val.getValue()==4){
                dex
                dex
                dex
                dex
            }
            .if (val.getValue()>4){
                txa
                sec
                sbc16 #val.getValue()
                tax
            }
        }
    }
```
base/supercpu_dex.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
//---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: dex16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to Decrease X with.
    //
    // SYNTAX:
    //   dex16 Value
    //
    // EXAMPLE:
    //   dex16                                   // Decrease X with 1
    //   dex16 1                                 // Decrease X with 1
    //   dex16 2                                 // Decrease X with 2
    //   dex16 8                                 // Decrease X with 8
    //
    // PARAMETERS:
    //                       Value     Min       Max
    //   Value                U16       0       65535
    //---------------------------------------------------------------------------------------------

    .pseudocommand dex16 val {
        .if (val.getType()==AT_NONE) {
            dex
        } else {
            .if (val.getValue()==1) {
                dex
            }
            .if (val.getValue()==2){
                dex
                dex
            }
            .if (val.getValue()==3){
                dex
                dex
                dex
            }
            .if (val.getValue()==4){
                dex
                dex
                dex
                dex
            }
            .if (val.getValue()>4){
                txa
                sec
                sbc16 #val.getValue()
                tax
            }
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_dex](https://codebase.c64.org/doku.php?id=base%3Asupercpu_dex)*
