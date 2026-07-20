---
title: Commodore 64 BASIC data conversion functions
source_url: https://sta.c64.org/cbm64basconv.html
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- kernal-routines
- memory-map
scraped_at: '2026-07-20'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 BASIC data conversion functions

| Address | Function | 
|---|---|
| $A96B | Fetch line number from BASIC program and put result to memory addresses $0014-$0015; if first character not a digit then the result is 0; if result is 64000 or above then display "SYNTAX ERROR". (Must call $0073, CHRGET beforehands.) | 
| $A9C4 | Assign value to integer variable; convert FAC to integer and write into variable pointed by memory addresses $0049-$004A. | 
| $A9DA | Assign value to string variable, including TI$. (Also see $AA2C.) | 
| $A9E0 | Assign value to TI$, set Time of Day; read value from string pointed by memory addresses $0064-$0065. | 
| $AA2C | Assign value to string variable, excluding TI$; read value from string pointed by memory addresses $0064-$0065; write value into string variable pointed by memory addresses $0049-$004A. | 
| $AD8A | Fetch value of numerical expression from BASIC program into FAC. | 
| $AD8D | Check whether expression is numerical; if not, display "TYPE MISMATCH". | 
| $AD8F | Check whether expression is string; if not, display "TYPE MISMATCH". | 
| $AD9E | Fetch value of expression from BASIC program; for numerical expressions, value is written into FAC; for string expressions, length of value is written to memory address $0061, address of value to memory addresses $0062-$0063. | 
| $AEF1 | Fetch value of expression, enclosed into parentheses, from BASIC program. (Also see $AD9E). | 
| $AF28 | Fetch name of variable from BASIC program and load its value; address of variable is written into memory addresses $0064-$0065; for numerical variables, the value is written into FAC, in floating-point format; for ST, TI and TI$, get variable value from system area; for variables that do not exist, return empty value (0 for numerical or empty string for string variables). | 
| $AF48 | Compute value of TI$. | 
| $AF61 | Load value of integer variable pointed by memory addresses $0064-$0065 into FAC, in floating-point format. | 
| $AF6E | Load value of floating-point variable, including ST and TI, into FAC. (Also see $AFA0.) | 
| $AF7B | Compute value of TI into FAC. | 
| $AF9A | Compute value of ST into FAC. | 
| $AFA0 | Load value of floating-point variable, excluding ST and TI, pointed by memory addresses $0064-$0065 into FAC. | 
| $B08B | Fetch name of variable from BASIC program and find it; if found, address of variable is written into memory addresses $005F-$0060, address of value into memory addressesd $0047-$0048; if not found and the caller was $AF28, return empty value (0 for numerical or empty string for string variables), otherwise create new variable with empty value. | 
| $B128 | Create new variable with empty value (0 for numerical or empty string for string variables); name of variable is in memory addresses $0045-$0046. | 
| $B1B2 | Fetch integer value from BASIC program into memory addresses $0064-$0065; if value is not withing [-32768, 32767] range, display "ILLEGAL QUANTITY". | 
| $B391 | Write integer in A/Y into FAC, in floating-point format. | 
| $B3A2 | Write integer in Y into FAC, in floating-point format. | 
| $B794 | Write integer in A into FAC, in floating-point format. | 
| $B79B | Fetch byte value from BASIC program into X; if value is not withing [0, 255] range, display "ILLEGAL QUANTITY". | 
| $B7EB | Fetch word and byte, separated by a comma, from BASIC program into memory addresses $0014-$0015 and X. | 
| $B7F7 | Convert FAC into unsigned integer value at memory addresses $0014-$0015; if value is not withing [0, 65535] range, display "ILLEGAL QUANTITY". | 
| $B849 | FAC := FAC + 0.5. | 
| $B850 | FAC := (floating-point value pointed by A/Y) – FAC. | 
| $B853 | FAC := ARG – FAC. | 
| $B867 | FAC := (floating-point value pointed by A/Y) + FAC. | 
| $B86A | FAC := ARG + FAC. (Must do "LDA $61" beforehands.) | 
| $B947 | FAC := Two_Complement(FAC); invert FAC mantissa. | 
| $BA28 | FAC := (floating-point value pointed by A/Y) * FAC. | 
| $BA2B | FAC := ARG * FAC. (Must do "LDA $61" beforehands.) | 
| $BA8C | ARG := (floating-point value pointed by A/Y). | 
| $BAE2 | FAC := FAC * 10. | 
| $BAFE | FAC := FAC / 10. | 
| $BB0F | FAC := (floating-point value pointed by A/Y) / FAC. | 
| $BB12 | FAC := ARG / FAC; if FAC = 0, display "DIVISION BY ZERO". (Must do "LDA $61" beforehands.) | 
| $BBA2 | FAC := (floating-point value pointed by A/Y). | 
| $BBC7 | Arithmetic register #4 := FAC. | 
| $BBCA | Arithmetic register #4 := FAC. | 
| $BBD0 | Write FAC into floating-point variable pointed by memory addresses $0049-$004A. | 
| $BBD4 | Write FAC into floating-point variable pointed by X/Y. | 
| $BBFC | FAC := ARG. | 
| $BC0C | ARG := Integer(FAC). | 
| $BC0F | ARG := FAC. | 
| $BC1B | FAC := Integer(FAC). | 
| $BC2B | Fetch sign of FAC into A: 1 = Positive, 0 = Zero, 255 = Negative. | 
| $BC5B | Compare floating-point value pointed by A/Y with FAC, put result into A: 1 = FAC less, 0 = Equal, 255 = FAC greater. | 
| $BC9B | Convert FAC into integer value at memory addresses $0064-$0065. | 
| $BCF3 | Fetch floating-point value from BASIC program into FAC. | 
| $BDCD | Write integer value in A/X onto screen, in floating-point format. | 
| $BDDD | Convert FAC to zero-terminated string representation at memory addresses $0100-$010A. | 
| $BF71 | FAC := Square_Root(FAC). | 
| $BF78 | FAC := ARG ^ (floating-point value pointed by A/Y). | 
| $BF7B | FAC := ARG ^ FAC. | 
| $BFB4 | FAC := –FAC. |

---
*Fonte originale: [https://sta.c64.org/cbm64basconv.html](https://sta.c64.org/cbm64basconv.html)*
