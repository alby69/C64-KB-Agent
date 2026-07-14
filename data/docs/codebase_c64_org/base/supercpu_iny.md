---
title: INY
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_iny
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware: []
related: []
scraped_at: '2026-07-14'
---

# INY

base:supercpu_iny

                # INY

Not neccessary, only for conveniance.

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: iny16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to increase Y with.
    //
    // SYNTAX:
    //   iny16 Value
    //
    // EXAMPLE:
    //   iny
    //   iny 8
    //
    // PARAMETERS:
    //                       Value     Min       Max
    //   Value                U16       0       65535
    //---------------------------------------------------------------------------------------------
    .pseudocommand iny16 val {
        .if (val.getType()==AT_NONE) {
            iny
        } else {
            .if (val.getValue()==1) {
                iny
            }
            .if (val.getValue()==2){
                iny
                iny
            }
            .if (val.getValue()==3){
                iny
                iny
                iny
            }
            .if (val.getValue()==4){
                iny
                iny
                iny
                iny
            }
            .if (val.getValue()>4){
                tya
                clc
                adc16 #val.getValue()
                tay
            }
        }
    }
```
base/supercpu_iny.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
//---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: iny16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to increase Y with.
    //
    // SYNTAX:
    //   iny16 Value
    //
    // EXAMPLE:
    //   iny
    //   iny 8
    //
    // PARAMETERS:
    //                       Value     Min       Max
    //   Value                U16       0       65535
    //---------------------------------------------------------------------------------------------

    .pseudocommand iny16 val {
        .if (val.getType()==AT_NONE) {
            iny
        } else {
            .if (val.getValue()==1) {
                iny
            }
            .if (val.getValue()==2){
                iny
                iny
            }
            .if (val.getValue()==3){
                iny
                iny
                iny
            }
            .if (val.getValue()==4){
                iny
                iny
                iny
                iny
            }
            .if (val.getValue()>4){
                tya
                clc
                adc16 #val.getValue()
                tay
            }
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_iny](https://codebase.c64.org/doku.php?id=base%3Asupercpu_iny)*
