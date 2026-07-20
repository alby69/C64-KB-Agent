---
title: DEY
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_dey
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

# DEY

base:supercpu_dey

                # DEY

Dey does not need a special pseudocommand, this is only for conveniance.

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: dey16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to Decrease Y with.
    //
    // SYNTAX:
    //   dey16 Value
    //
    // EXAMPLE:
    //   dey16                                   // Decrease Y with 1
    //   dey16 1                                 // Decrease Y with 1
    //   dey16 2                                 // Decrease Y with 2
    //   dey16 8                                 // Decrease Y with 8
    //
    // PARAMETERS:
    //                       Value     Min       Max
    //   Value                U16       0       65535
    //---------------------------------------------------------------------------------------------
    .pseudocommand dey16 val {
        .if (val.getType()==AT_NONE) {
            dey
        } else {
            .if (val.getValue()==1) {
                dey
            }
            .if (val.getValue()==2){
                dey
                dey
            }
            .if (val.getValue()==3){
                dey
                dey
                dey
            }
            .if (val.getValue()==4){
                dey
                dey
                dey
                dey
            }
            .if (val.getValue()>4){
                tya
                sec
                sbc16 #val.getValue()
                tay
            }
        }
    }
```
base/supercpu_dey.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
//---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: dey16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to Decrease Y with.
    //
    // SYNTAX:
    //   dey16 Value
    //
    // EXAMPLE:
    //   dey16                                   // Decrease Y with 1
    //   dey16 1                                 // Decrease Y with 1
    //   dey16 2                                 // Decrease Y with 2
    //   dey16 8                                 // Decrease Y with 8
    //
    // PARAMETERS:
    //                       Value     Min       Max
    //   Value                U16       0       65535
    //---------------------------------------------------------------------------------------------

    .pseudocommand dey16 val {
        .if (val.getType()==AT_NONE) {
            dey
        } else {
            .if (val.getValue()==1) {
                dey
            }
            .if (val.getValue()==2){
                dey
                dey
            }
            .if (val.getValue()==3){
                dey
                dey
                dey
            }
            .if (val.getValue()==4){
                dey
                dey
                dey
                dey
            }
            .if (val.getValue()>4){
                tya
                sec
                sbc16 #val.getValue()
                tay
            }
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_dey](https://codebase.c64.org/doku.php?id=base%3Asupercpu_dey)*
