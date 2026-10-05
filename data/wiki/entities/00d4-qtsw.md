---
id: 00d4-qtsw
type: entity
title: 0 = direct cursor, else programmed
aliases:
- 0 = direct cursor, else programmed
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00d4-qtsw.md
  sha256: e34d27f62c9110975a4fa82de9de50341647e6ca2c5fb5b5e97af7686ad70a76
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00d4-qtsw
---

# 0 = direct cursor, else programmed



# QTSW — 0 = direct cursor, else programmed ($00D4)

## Panoramica
Il registro o area di memoria QTSW è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D4` (`212` decimale)
- **Range**: `$00D4`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Quote switch

### Commodore-64-intern-Buch (Commodore)
Falls in dieser Speicherzelle eine
Null steht, dann befindet sich der
Computer im Normalmodus. Andere
Werte bewirken den Hochkommamodus.

### C64 Programmer's Reference Guide (Commodore)
Flag: Editor in Quote Mode, $00 = NO

### Memory Map (Jim Butterfield)
0 = direct cursor, else programmed

### Mapping the Commodore 64 (Sheldon Leemon)
A nonzero value in this location indicates that the editor is in quote
mode.  Quote mode is toggled every time that you type in a quotation
mark on a given line--the first quote mark turns it on, the second
turns it off, the third turns it back on, etc.

If the editor is in this mode when a cursor control character or other
nonprinting character is entered, a printed equivalent will appear on
the screen instead of the cursor movement or other control operation
taking place.  Instead, that action is deferred until the string is
sent to the string by a PRINT statement, at which time the cursor
movement or other control operation will take place.

The exception to this rule is the DELETE key, which will function
normally within quote mode.  The only way to print a character which
is equivalent to the DELETE key is by entering insert mode (see
location 216 ($00D8)).  Quote mode may be exited by printing a closing
quote, or by hitting the RETURN or SHIFT-RETURN keys.

Sometimes, it would be handy to be able to escape from quote mode or
insert mode without skipping to a new line.  The machine language
program below hooks into the keyscan interrupt routine, and allows you
to escape quote mode by changing this flag to 0 when you press the f1
key:

    10 FOR I=850 TO I+41:READ A:POKE I,A:NEXT
    20 PRINTCHR$(147)"PRESS F1 KEY TO ESCAPE QUOTE MODE"
    30 PRINT"TO RESTART AFTER RESTORE ONLY, SYS 850":SYS850:NEW
    40 DATA  173 , 143 , 2 , 141 , 46 , 3 , 173 , 144 , 2 , 141
    50 DATA 47 , 3 , 120 , 169 , 107 , 141 , 143 , 2 , 169 , 3
    60 DATA 141 , 144 , 2 , 88 , 96 , 165 , 203 , 201 , 4 , 208
    70 DATA 8 , 169 , 0 , 133 , 212 , 133 , 216 , 133 , 199 , 108 , 46 , 3

### Reference (Joe Forster / STA)
Values:

* $00: Normal mode.
* $01: Quotation mode.

### 64'er Magazin (64'er)
Steht in dieser Speicherzelle eine 0, dann befindet sich der Computer im
Gänsefuß-Modus, andere Zahlen bedeuten den Normal-Modus.

Selbst Anfängern ist der Gänsefuß-Modus sehr rasch geläufig, bietet er doch die
Möglichkeit, Zeichen mit der PRINT-Anweisung auszudrucken. Genauso bekannt sind
aber auch die Tücken der Gänsefüße. Die Cursor-Tasten reagieren nicht wie
gewohnt. Auch die Farbumschaltung und andere Steuertasten zeigen nicht die
übliche Wirkung, sondern drucken - allzu oft unerwartet - ein reverses Zeichen
auf den Bildschirm.

Eingeschaltet wird der Gänsefuß-Modus durch Drücken der geSHIFTeten 2-Taste
oder der geSHIFTeten INST/DEL-Taste. Abgeschaltet wird er nach jedem 2., 4.,
6., also nach jeder geradzahligen Wiederholung der Gänsefuß-Taste innerhalb
einer Zeile. Abgeschaltet wird er auch durch die RETURN-Taste. Das spezielle
Verhalten der Steuertasten zwischen Gänsefüßen läßt sich für faszinierende
Effekte ausnutzen.

Leider läßt sich der Inhalt der Speicherzelle 212 und damit der Status des
Gänsefuß-Modus von Basic aus nicht beeinflussen. Doch in Maschinensprache unter
Verwendung der Interrupt-Routine geht es, und einige Vorschläge zum Abschalten
des Gänsefuß-Modus per Tastendruck sind schon veröffentlicht worden.

### 64map (—)
Flag: Editor in Quote Mode; $00 = Not

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00d4-qtsw]]
