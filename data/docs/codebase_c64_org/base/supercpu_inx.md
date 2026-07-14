---
title: INX
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_inx
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware: []
related: []
scraped_at: '2026-07-14'
---

# INX

base:supercpu_inx

                # INX

Not neccessary, only for conveniance.

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: inx16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to increase X with.
    //
    // SYNTAX:
    //   inx16 Value
    //
    // EXAMPLE:
    //   inx
    //   inx 8
    //
    // PARAMETERS:
    //                       Value     Min       Max
    //   Value                U16       0       65535
    //---------------------------------------------------------------------------------------------
    .pseudocommand inx16 val {
        .if (val.getType()==AT_NONE) {
            inx
        } else {
            .if (val.getValue()==1) {
                inx
            }
            .if (val.getValue()==2){
                inx
                inx
            }
            .if (val.getValue()==3){
                inx
                inx
                inx
            }
            .if (val.getValue()==4){
                inx
                inx
                inx
                inx
            }
            .if (val.getValue()>4){
                txa
                clc
                adc16 #val.getValue()
                tax
            }
        }
    }
```
base/supercpu_inx.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
//---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: inx16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to increase X with.
    //
    // SYNTAX:
    //   inx16 Value
    //
    // EXAMPLE:
    //   inx
    //   inx 8
    //
    // PARAMETERS:
    //                       Value     Min       Max
    //   Value                U16       0       65535
    //---------------------------------------------------------------------------------------------

    .pseudocommand inx16 val {
        .if (val.getType()==AT_NONE) {
            inx
        } else {
            .if (val.getValue()==1) {
                inx
            }
            .if (val.getValue()==2){
                inx
                inx
            }
            .if (val.getValue()==3){
                inx
                inx
                inx
            }
            .if (val.getValue()==4){
                inx
                inx
                inx
                inx
            }
            .if (val.getValue()>4){
                txa
                clc
                adc16 #val.getValue()
                tax
            }
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_inx](https://codebase.c64.org/doku.php?id=base%3Asupercpu_inx)*
