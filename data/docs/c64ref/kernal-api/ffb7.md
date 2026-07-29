---
title: /O status word
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/commodore_128_intern.txt
category: reference
topics:
- kernal-api
- system-routines
- jumps
difficulty: intermediate
language: assembly
hardware:
- C64
related:
- beq
- cmp
- jsr
- readst
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - commodore_128_intern.txt
  - cracking_the_kernal.txt
  - mapping_the_commodore_64.txt
  - kernal_64_/_128.txt
  - machine_language_routines.txt
  - c64_kernal_jump_table.txt
  - c64_programmer's_reference_guide.txt
  - commented_rom_disassembly.txt
  - das_neue_commodore-64-intern-buch.txt
  - standard_kernal_functions.txt
  - compute!'s_tool_kit:_kernal.txt
  address: $FFB7
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine returns the current status of the I/O device in the accumulator.
      The
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: . When called, READST returns the status of the I/O devices. Any
      error code c...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at ABDD/CBDD in BASIC''s INPUT, JSR at AF9A/CF9A'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: t:A=status byte                      - - -  A - -  A - -
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : None.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: as Statuswort in den Akku
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: er an I/O error occurs, a bit of the Status Word is set to
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine (some Commodore references call it READSS) re-
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: d der aktuelle Systemstatus im <Akku>
---

# $FFB7 — /O status word ($FFB7)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFB7`
- **Chiamata**: `JSR None` o `SYS 65463`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: None
r returns: None
k requirements: 2
sters affected: A

scription**: This routine returns the current status of the I/O devices
 accumulator. The routine is usually called after new communication
I/O device. The routine gives you information about device status,
ors that have occurred during the I/O operation.

bits returned in the accumulator contain the following information:
able below)

it Position| ST Numeric Value | Cassette Read            | Serial Bus R/W     | Tape Verify + Load |
-----------|------------------|--------------------------|--------------------|--------------------|
           |      1           |                          |  time out write    |                    |
           |      2           |                          |  time out read     |                    |
           |      4           |  short block             |                    |    short block     |
           |      8           |   long block             |                    |    long block      |
           |     16           | unrecoverable read error |                    |   any mismatch     |
           |     32           |    checksum error        |                    |     checksum error |
           |     64           |  end of file             |  EOI line          |                    |
           |   -128           |  end of tape             | device not present |    end of tape     |

 to Use:

l this routine.
ode the information in the A register as it refers to your pro-
m.

MPLE:

HECK FOR END OF FILE DURING READ
   JSR READST
   AND #64                       ;CHECK EOF BIT (EOF=END OF FILE)
   BNE EOF                       ;BRANCH ON EOF

### Standard KERNAL Functions (Joe Forster / STA)
–
: A = Device status.
egisters: A.
ddress: $FE07.

### Commented ROM Disassembly (Lee Davison)
outine returns the current status of the I/O device in the accumulator. The
e is usually called after new communication to an I/O device. The routine
ive information about device status, or errors that have occurred during the
eration.

### Cracking The Kernal (Peter Marcotty)
. When called, READST returns the status of the I/O devices. Any error code can be translated as operator error.

heck for read error.
   JSR READST
   CMP #16
   BEQ ERROR
n this case, if the accumulator is 16, a read error occurred.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at ABDD/CBDD in BASIC's INPUT, JSR at AF9A/CF9A
IC's STATUS, JSR at E180/E17D E195 in BASIC's
ERIFY.

07/FE57 to read the I/O status word, 90, return-
e value in the accumulator. This value reflects certain
ions during serial or tape I/O.

/VIC Programmer's Reference Guides contain some
:

 when VERIFYing for a serial device, a VERIFY error
cur.

, for the VIC you cannot read the RS-232 status
er, 0297, by calling this routine. READST for RS-232 al-
eturns zero on the VIC. If you want to read the RS-232
 on the VIC, read 0297 directly; don't call this routine.
rror in READST is corrected in the 64.

 detecting an end-of-tape header allows BASIC to
y the DEVICE NOT PRESENT error message, but the
 routines for OPEN or LOAD/VERIFY do not set loca-
0. Thus, READST will not return the end-of-tape status
ion following OPEN or LOAD/VERIFY. You can check
-tape status upon return from OPEN or LOAD/VERIFY
cking for the carry bit set and the accumulator set to 5,
are the conditions that indicate end-of-tape.

ble below shows the possible values returned by
:

DST Values

Value | Bit | Serial I/O         | Tape Read/LOAD/VERIFY    | RS-232 (64 only)       |
------|-----|--------------------|--------------------------|------------------------|
      | 7   | Device not present |                          | Break detected         |
      | 6   | EOI status         | End of file              | DSR signal missing     |
      | 5   |                    | Checksum error           |                        |
      | 4   | VERIFY error       | Unrecoverable read error | CTS signal missing     |
      | 3   |                    | Long block               | Receive buffer empty   |
      | 2   |                    | Short block              | Receive buffer overrun |
      | 1   | Read timeout       |                          | Framing error          |
      | 0   | Write timeout      |                          | Parity error           |

tus Terms

 Block**: Tape read is trying to read data bytes after the
block has already completed.

t Block**: Tape read is reading leader bits between blocks
the byte action routine is still expecting to be reading
from the block.

coverable Read Error**: During tape read and
ERIFY, more than 31 errors were detected in block 1.
s also set if read or VERIFY errors for the same byte oc-
 in both blocks 1 and 2.

ksum Error**: Computed parity for the loaded area is not
me as the final byte of tape block 2 (the parity computed
 the SAVE of the second block).

of File**: This status is set when doing CHRIN from tape
sequential file and the read-ahead byte in the tape buffer

FY Error**: The byte retrieved from the serial device does
tch the byte in memory.

(End or Identify)**: This is set during the Receive Byte
erial Device routine when the EOI handshake is per-
. Set during serial read to indicate the last byte has
ent from the serial device. The unusual term EOI is a
er from the IEEE-488 bus definitions used on older
M computers; you may find it simpler just to remem-
is as End of File for disk.

ce Not Present**: Device does not respond with the proper
ake sequence during OPEN, LOAD, VERIFY, or SAVE
ions.

 Timeout, Write Timeout**: Read or write timeouts are set
he serial device doesn't handshake within the allocated
time.

k Detected**: This is set if the check for a stop bit finds a 0
 than a 1, and the data bits received so far are all 0's.

ing Error**: This is set if the check for a stop bit finds a 0
e data bits received so far included some bits set to 1.

Signal Missing**: The 64 can't detect the Data Set Ready
 from the RS-232 device during x-line handshaking.

Signal Missing**: The 64 can't detect the Clear To Send
 from the RS-232 device during x-line handshaking.

ty Error**: The parity bit indicates an error in transmission
s byte.

iver Buffer Empty**: Nothing is in the RS-232 input
. This allows routines to test the status so they don't
aiting for data.

iver Buffer Overrun**: The RS-232 input buffer is full and
r byte has been received.

### C64 KERNAL jump table (Frank Kontros)
t:A=status byte                      - - -  A - -  A - -

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .A = status byte. (see section on ERROR messages).
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
as Statuswort in den Akku

### Mapping the Commodore 64 (Sheldon Leemon)
er an I/O error occurs, a bit of the Status Word is set to
te what the problem was.  This routine allows you to read the
 word (it is returned in the Accumulator).  If the device was
-232, its status register is read and cleared to zero.  For the
gs of the various status codes, see the entry for location 144
or 663 ($297) for the RS-232 device.

### Machine Language Routines (Todd D Heimarck)
outine (some Commodore references call it READSS) re-
the status of the most recent I/O operation. The status
will be in the accumulator upon return; the contents of
 .Y are unaffected. If the current device number is 2 (in-
ng an RS-232 operation), the status value is retrieved
he RS-232 status flag (location $0297 for the 64 or
for the 128), and the flag is cleared. Otherwise, the sta-
lue is retrieved from the tape/serial status flag (location
That flag is not cleared after being read.

|  Value  | Meaning if set Serial | Meaning if set Tape                   | Meaning if set RS-232    |
|---------|-----------------------|---------------------------------------|--------------------------|
|   1/$01 | write timeout         |                                       | parity error             |
|   2/$02 | read timeout          |                                       | framing error            |
|   4/$04 |                       | short block                           | receiver buffer overflow |
|   8/$08 |                       | long block                            | receiver buffet empty    |
|  16/$10 | verify mismatch       | unrecoverable read or verify mismatch | CTS missing              |
|         |                       |                                       |                          |
|  32/$20 |                       | checksum mismatch                     |                          |
|  64/$40 | EOI (end of file)     | end of file                           | DSR missing              |
| 128/$80 | device not present    | end of tape                           | break                    |

### Commodore 128 intern (Jörg Schieb et al.)
d der aktuelle Systemstatus im <Akku>
gegeben. Ist die RS232 aktiv, so wird das Statusbyte
ben und direkt im Speicher gelöscht. Sollten Sie also das
byte öfters benötigen, so speichern Sie es zwischen. Ist ein
r als der RS232-Kanal geöffnet, so wird das Statusbyte
resse $90 übergeben.

abeparameter**: .A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*