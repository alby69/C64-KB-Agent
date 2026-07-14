---
title: Turbo Assembler 5.2 reference
source_url: https://codebase.c64.org/doku.php?id=base%3Aturboassembler_5.2_bacchus_version
category: manual
topics:
- raster interrupts
- memory management
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- VIC-II
- CIA
- CPU
- KERNAL
related:
- sprite-programming
- keyboard-handling
- cia-registers
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
- joystick-reading
scraped_at: '2026-07-14'
---


# Turbo Assembler 5.2 reference

### Table of Contents

# Turbo Assembler 5.2 reference

This document was written by Bacchus/Fairlight quite some time ago. Frantic took it from the [Fairlight homepage](http://www.fairlight.to/docs/text/xass33.html) and put it up here at the Codebase64 wiki, with permission from Bacchus. It documents [Bacchus' own version](https://codebase.c64.org/lib/exe/fetch.php?media=base:turboass_5.2_fix.zip) of Turbo Assembler, built on someone's hacked and featurepatched version. Most of these features work the same way in all common versions of Turbo Assembler, so you will probably find this document useful no matter what version of Turbo Assembler you use. Anyway… Here comes Bacchus' document!

## TurboAssembler 5.2

Version by Bacchus/FairLight

### Commands

Commands are invoked by pressing the following keys, preceded by the “left-arrow”-key. Note that some are meant to be capital letters, and should hence be entered Shift+letter

| Arrow up | Put row in the line buffer | 
| * | Directory | 
| + | Addition routine | 
| - | Subtraction routine | 
| : | List marks | 
| ; | Kill mark | 
| = | Join lines (Hard to explain! Try!) | 
| @ | Disk status | 
| 1 | Back to basic | 
| 2 | Insert separator line | 
| 3 | Assemble | 
| 4 | Print (? - print, name - to file, ' - To Screen) | 
| 5 | 
Produce object file (assemble to disk)  
*= $1000  
*=$2000  Assembled to disk you'll load six bytes; 
$1000 : LDA $1000  As you see, the assembly is right, but it landed in the wrong place! | 
| 6 | Input part of the memory as data - import binary data as .byte | 
| 7 | Set tab (Cursor pos after Return) | 
| 8 | Position of mnemonic column | 
| a | Enter control codes (Abort with ←) | 
| b | Block command (A block must be defined with the “m” command first). You can from here copy, write to disk, kill or save out the section previously defined | 
| c | Cold start (Like “NEW” in basic) | 
| d | control codes | 
| e | Enter a SEQ file (Load) | 
| F | Fill memory (specify range) | 
| f | Find: … (See “h”) | 
| g | c mark (See “m”) | 
| h | Hunt next (Define with “f”) | 
| i | Initialize memory (Zero fill unused) | 
| j | Hex dump specified memory area | 
| K | Key click on/off (yuack!) | 
| k | Redefine F3-F6 (followed by the key you wish to redefine) | 
| L | Load data at address (return at question loads at the files default address) | 
| l | Load file in PRG format | 
| m | Set marks (0-9 for bookmarks, S - Start of block, E - End of block) | 
| n | Go to specified line in the source | 
| o | Change colours | 
| p | Protect file (Enter an EOR for the file - Stupid!!! Some versions had $33 as default. Beware!!) | 
| q | Cursor to the left edge - especially good for F-key macros! | 
| r | Replace: … By: … Finds the first occurrence (See ”t” and ”y”) | 
| Return | Insert a line (undo “=”) | 
| S | Save data at address | 
| s | Save file in PRG format | 
| t | Executes first replace (See “r”) | 
| u | List labels (? - To Printer, Name to disk, ' to screen) | 
| v | Memory map (DON'T use with Action Replay as the LDA $DE00 hangs the computer!!!) | 
| w | Write as SEQ file (Save) | 
| y | Executes ALL replaces. (See “r”) | 
| ö/£ | Paste buffer (See “arrow up”) | 
| F1 | F-key reset (undo “”+“k” edits) | 
| DEL | Delete line | 
| / | Delete the data the rest of the line, after the cursorposition. (Very useful to delete crap from resource files!) | 
| INST | Line insert ON/OFF | 
| ← | To insert a “←” (left arrow), just doublepress the key! | 

### Keys without previous keypress

Note that the keys F1, F2, F7 and F8 are static, whereas F3-F6 are redefinable from within the program. If you find another “kewl version”, it's almost always only new F-key definitions they've added. Normally, i.e. they are something like:

| F1 | One screen up | 
| F2 | Go to top | 
| F7 | One screen down | 
| F8 | Go to bottom | 
| F3 | .WORD/.TEXT/DIR (Either of 'em) | 
| F4 | Assemble and start | 
| F5 | .BYTE | 
| F6 | Delete current row | 
| Inst | Insertmode ON/OFF (i.e. insert or overstrike) | 

### Pseudo Op-codes

| .BYTE | .BYTE “p”, $ab,%100011001,49,&19Enter data. Either within quotes (one character), as hex ($E0) binary (%10001110), decimal (45) or octal (&34). Separate numbers with commas. | 
| .WORD |  .WORD label, $1000, label+$f8/2, *-9 Enter 16 bit/2 byte address in the normal 6502/6510 way, i.e. lowbyte, highbyte. Any label and expression is valid! | 
| * |  * = $XXXX XXXX is here the start for your code. Can be used any number of time, but beware while assembling to disk (“”+“5”). | 
| .TEXT |  .TEXT “Some text” Enter some text in ASCII-format. Beware that there is no obvious way of entering pokecodes, but for this purpose I recommend my own method. Either AND #$3F or: Enter your monitor. Type the text to the screen and transfer it into a safe place in the memory. Enter TurboAss and insert the data with “”+“6” | 
| ; |  ; <Comment> A comment for information purposes. Enter any comment after the semicolon. Truly good for you when you want to understand the crappy, ununderstandable code you produced when you were lame (last week! label LDA #$00 ;Load accumulator with zero! | 
| .OFFS |  .OFFS XXXX This is a toughie, that relocates the code. The value after the offs is a value added to the *= value. F.ex. *=$1000 followed by .OFFS $0800 makes the code land on $1800 and .OFFS $F800 makes it land on $0800. Inserting things like drivecode, is a joy thanks to this feature, even if it could have been done a bit easier to understand. The trick to make it work is this piece of code, so this will also work *=$1000 label1 *=$0400 ;Start for f.ex. drive code .OFFS 0-(*-label1) label2 LDA label2 Labels will be initialized to the following: Label1 =$1000 Label2 =$0400 The code LDA $0400 will be placed at $1000 in memory. | 

### Working with labels

| label | = myarse | 
| borderco | = $d020 | 
| memptrlab | = *+3 ;Offset from prgcount | 
| andtest | = $213&127 ;Logical AND | 
| ortest | = %1000:$03 ;Logical OR | 
| lowtest | = <irqptr ;LowByte of sth | 
| hitest | = >irqptr ;Guess ? | 
| screencol | = bordercol + 1 ;Define label. | 

Calculations or absolute numbers work just as good.

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aturboassembler_5.2_bacchus_version](https://codebase.c64.org/doku.php?id=base%3Aturboassembler_5.2_bacchus_version)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).
