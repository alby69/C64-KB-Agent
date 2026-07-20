---
title: Commodore 1541 drive memory map
source_url: https://sta.c64.org/cbm1541mem.html
category: reference
topics:
- memory management
- basic
- sprite programming
- assembly
difficulty: advanced
language: mixed
hardware:
- KERNAL
- VIC-II
- CIA
- CPU
- SID
related:
- sid-registers
- sound-programming
- vic-ii-registers
- cia-registers
- joystick-reading
- memory-map
- raster-interrupts
- keyboard-handling
- music-player
- sprite-programming
- kernal-routines
scraped_at: '2026-07-20'
last_modified: Mon, 15 May 2023 22:00:00 GMT
---

# Commodore 1541 drive memory map

| **Address** | Description  | 
|---|
| **$0000-$00FF**Zero page
 | 
| $0000 | Buffer #0 command
  and status registers. Bits: Bits #0-#6: Status or command code.Bit #7: 0 = Job finished, register contains status
    code; 1 = Job to be executed, register contains command code. Values: $00: "24,READ ERROR" (only during disk format).$01: "00,OK" (no error).$02: "20,READ ERROR".$03: "21,READ ERROR".$04: "22,READ ERROR".$05: "23,READ ERROR".$06: "24,READ ERROR" (may not occur).$07: "25,WRITE ERROR".$08: "26,WRITE PROTECT ON".$09: "27,READ ERROR".$0A: "28,READ ERROR" (may not occur).$0B: "29,DISK ID MISMATCH".$0F: "74,DRIVE NOT READY". $80: Read sector.
  $90: Write sector.$A0: Verify sector.$B0: Read in sector header and fetch header ID.$C0: Bump head.$D0: Execute code in buffer.$E0: Read in sector header and then execute code in
    buffer.$F0: Read in sector header. | 
| $0001 | Buffer #1 command and status register. | 
| $0002 | Buffer #2 command and status register. | 
| $0003 | Buffer #3 command and status register. | 
| $0004 | Buffer #4 command and status register. | 
| $0005 | Unused. (Command and status register of
  not existing buffer #5.) | 
| $0006-$0007 | Buffer #0 track and sector
  register. | 
| $0008-$0009 | Buffer #1 track and sector
  register. | 
| $000A-$000B | Buffer #2 track and sector
  register. | 
| $000C-$000D | Buffer #3 track and sector
  register. | 
| $000E-$000F | Buffer #4 track and sector
  register. | 
| $0010-$0011 | Unused. (Track and sector register
  of not existing buffer #5.) | 
| $0012-$0013 | Unit #0 expected sector header
  ID. | 
| $0014-$0015 | Unused. (Expected sector header ID
  of not existing unit #1.) | 
| $0016-$0017 | Header ID from header of sector last
  read from disk. | 
| $0018-$0019 | Track and sector number from header
  of sector last read from disk. | 
| $001A | Header checksum from header of sector last
  read from disk. | 
| $001B | Unused. | 
| $001C | Unit #0 disk change indicator. Bits: | 
| $001D | Unused. (Disk change indicator of not
  existing unit #1.) | 
| $001E | Previous status of unit #0 write protect
  photocell (in bit #4). | 
| $001F | Unused. (Previous status of write protect
  photocell of not existing unit #1.) | 
| $0020 | Unit #0 disk controller internal command
  register. Bits: Bit #4: 1 = Switch motor off.Bit #5: 1 = Idle.Bit #6: 1 = Seeking in progress.Bit #7: 1 = Waiting for motor to spin up. | 
| $0021 | Unused. (Disk controller internal command
  register of not existing unit #1.) | 
| $0022 | Unit #0 current track number. | 
| $0023 | Serial bus communication speed switch.
  Values: $00: C64, lower speed, extra waits are needed.
    (Compensation for the delays caused by sprite DMA in the host.)$01-$FF: VIC20, higher speed. | 
| $0024-$002B | Header of sector last read from or
  next to be written onto disk, in GCR-encoded form. | 
| $002C-$002D | Unused. | 
| $002E-$002F | Pointer to current byte in buffer
  during GCR-encoding/decoding. | 
| $0030-$0031 | Pointer to beginning of current
  buffer. | 
| $0032-$0033 | Pointer to track and sector
  registers of current  buffer. | 
| $0034 | GCR-byte counter during
  GCR-encoding/decoding. | 
| $0035 | Unused. | 
| $0036 | Byte counter during
  GCR-encoding/decoding. | 
| $0037 | Unused. | 
| $0038 | Data block signature byte of sector last
  read from disk. | 
| $0039 | Expected value of sector header signature
  byte.Default: $08.
 | 
| $003A | Computed checksum of data in buffer. | 
| $003B-$003C | Unused. | 
| $003D | Disk controller current unit number.
  Values: Default: $00, 0. | 
| $003E | Disk controller previous unit number.
  Values: $00: Unit #0.$01: Unit #1. (Makes no sense, will not work.)$FF: Motor is off, must spin it up before
    seeking. Default: $00, 0. | 
| $003F | Disk controller current buffer number. | 
| $0040 | Current track number. | 
| $0041 | Buffer number that needs seeking. | 
| $0042 | Number of tracks to move during
  seeking. | 
| $0043 | Number of sectors on current track. | 
| $0044 | Data density (in bits #5-#6).Temporary register for buffer command.
 | 
| $0045 | Disk controller buffer command
  register. | 
| $0046 | Unused. | 
| $0047 | Expected value of data block header
  signature byte.Default: $07.
 | 
| $0048 | Motor spin up/down delay counter. | 
| $0049 | Original value of stack pointer before
  execution of disk controller interrupt. | 
| $004A | Number of halftracks to move during
  seeking. | 
| $004B | Retry counter for reading sector
  header.Temporary area during seeking.
 | 
| $004C | On current track, the distance of the
  sector, that matches the sector of a buffer and is nearest to the one last
  read from disk. (The execution of the command whose sector is optimal in
  time?) | 
| $004D | On current track, the sector that is two
  sectors away from the one last read from disk. (Apparently, the optimization
  takes about two sectors worth of time.) | 
| $004E-$004F | Pointer to beginning of auxiliary
  buffer during GCR-encoding (byte swapped). | 
| $0050 | Indicator of buffer data currently being
  in GCR-encoded form. Values: $00: Data in normal form.$01-$FF: Data in GCR-encoded form. Upon exiting the
    disk controller interrupt, data must be decoded. | 
| $0051 | Current track number during formatting.
  Bits: | 
| $0052-$0055 | Temporary area for data bytes during
  GCR-encoding/decoding. | 
| $0056-$005D | Temporary area for data nybbles and
  GCR bytes during GCR-encoding/decoding. | 
| $005E | Number of halftracks to
  accelerate/decelerate through during accelerated seeking.(Twice this value must be less than value of address $0064.)
 | 
| $005F | Acceleration/deceleration factor during
  accelerated seeking.(Value of address $1C07 plus/minus value of address $005E times this value
  must not be too low – below about 12-20, depends on drive mechanics
  – or too high – above 255.)
 | 
| $0060 | Delay counter after seeking. (So that head
  stops vibrating.)Halftrack counter for acceleration/deceleration during accelerated
  seeking.
 | 
| $0061 | Halftrack counter for full speed during
  accelerated seeking. | 
| $0062-$0063 | Pointer to routine next to be
  executed during seeking. | 
| $0064 | Lower distance limit of accelerated
  seeking, in halftracks.(When moving to a track further than this many halftracks, seeking will be
  accelerated.)
 Default: $C8, 200.
 | 
| $0065-$0066 | Pointer to warm reset ("UI" command)
  routine.Default: $EB22.
 | 
| $0067 | Unknown. | 
| $0068 | Automatic disk initialization switch.
  Values: $00: When initializing units upon processing
    commands, the BAM must be loaded.$01-$FF: Unit initialization does not include loading
    the BAM. Default: $00. | 
| $0069 | Soft interleave. (Distance, in sectors,
  for allocating the next sector for files.)Default: $0A, 10.
 | 
| $006A | Number of retries on disk commands.
  Bits: Bits #0-#5: Number of retries.Bit #6: 1 = Do not retry on adjacent halftracks.Bit #7: 1 = Do not bump head. Default: $05, 5. | 
| $006B-$006C | Pointer to "Ux" user command pointer
  table.Default: $FFEA.
 | 
| $006D-$006E | Temporary pointer for BAM
  operations. | 
| $006F-$0070 | Temporary pointer for various
  operations. | 
| $0071-$0074 | Unknown. | 
| $0075-$0076 | Pointer to current byte during
  memory test upon startup.Execution address of current "Ux" user command.
 | 
| $0077 | Serial bus LISTEN command to accept.
  (Device number OR $20.) | 
| $0078 | Serial bus TALK command to accept. (Device
  number OR $40.) | 
| $0079 | Serial bus LISTEN command indicator.
  Values: | 
| $007A | Serial bus TALK command indicator.
  Values: | 
| $007B | Unknown. | 
| $007C | Serial bus ATN arrival indicator.
  Values: | 
| $007D | End of command indicator. Values: | 
| $007E | Track number of previously opened file.
  (Used when opening "*".) Values: | 
| $007F | Current unit. Values: Default: $00, 0. | 
| $0080-$0081 | Track and sector number for various
  operations. | 
| $0082 | Current channel number. Values: | 
| $0083 | Current secondary address (only bits
  #0-#3). | 
| $0084 | Current secondary address. | 
| $0085 | Data byte read from serial bus.Data byte read from buffer or to be written into buffer.
 | 
| $0086-$0087 | Pointer to current byte in directory
  buffer when writing entries into directory.Pointer to current byte of error message.
 $0086: Counter of files deleted during "SCRATCH" command.
 Start switch during "&" command ($01-$FF: Execute code.)
 Temporary unit number during job processing.
 $0087: Computed block checksum during "&" command.
 | 
| $0088-$0089 | Pointer to current byte during "&"
  command.Execution address of user code during "&" command.
 | 
| $008A | Unknown. | 
| $008B-$008D | Temporary area for integer division.
  (Used to compute the side sector of relative files.) | 
| $008E-$0093 | Unknown. | 
| $0094-$0095 | Pointer to current directory
  entry. | 
| $0096-$0097 | Unused. | 
| $0098 | Bit counter during serial bus
  input/output. | 
| $0099-$009A | Pointer to buffer #0.Default: $0300.
 | 
| $009B-$009C | Pointer to buffer #1.Default: $0400.
 | 
| $009D-$009E | Pointer to buffer #2.Default: $0500.
 | 
| $009F-$00A0 | Pointer to buffer #3.Default: $0600.
 | 
| $00A1-$00A2 | Pointer to buffer #4.Default: $0700.
 | 
| $00A3-$00A4 | Pointer to input buffer.Default: $0200.
 | 
| $00A5-$00A6 | Pointer to error message buffer.Default: $02D5.
 | 
| $00A7-$00AD | Primary buffer number assigned to
  channels. Bits: | 
| $00AE-$00B4 | Secondary buffer number assigned to
  channels. Bits: | 
| $00B5-$00BA | Length of file assigned to channels,
  low byte. For relative files, number of records, low byte. | 
| $00BB-$00C0 | Length of file assigned to channels,
  high byte. For relative files, number of records, high byte. | 
| $00C1-$00C6 | Offset of current byte in buffer
  assigned to channels. | 
| $00C7-$00CC | Record length of relative file
  assigned to channels. | 
| $00CD-$00D2 | Buffer number holding side sector of
  relative file assigned to channels. Values: | 
| $00D3 | Comma counter during fetching unit numbers
  from command. | 
| $00D4 | Offset of current byte in relative file
  record. | 
| $00D5 | Side sector number belonging to current
  relative file record. | 
| $00D6 | Offset of track and sector number of
  current relative file record in side sector. | 
| $00D7 | Offset of record in relative file data
  sector. | 
| $00D8-$00DC | Sector number of directory entry of
  files. | 
| $00DD-$00E1 | Offset of directory entry of
  files. | 
| $00E2-$00E6 | Unit number of files. Bits: | 
| $00E7-$00EB | File type and flags of files.
  Bits: Bits #0-#2: File type; 0 = DEL; 1 = SEQ; 2 = PRG; 3 =
    USR; 4 = REL.Bit #5: 0 = File has been closed.Bit #6: 1 = File is write protected.Bit #7: 1 = Wildcards are present in the file
    name. | 
| $00EC-$00F1 | Unit number, file type and flags of
  files assigned to channels. Bits: Bit #0: Unit number.Bits #1-#3: File type; 0-4: Usual file types; 7 =
    "#", direct disk access.Bit #5: 1 = End of record.Bit #6: 1 = End of file.Bit #7: 1 = Directory entry of file must be
    updated. | 
| $00F2-$00F7 | Input/output flags of channels.
  Bits: | 
| $00F8 | End of file indicator of current channel.
  Values: | 
| $00F9 | Current buffer number. | 
| $00FA-$00FE | Unknown. | 
| $00FF | Unit #0 BAM input/output error indicator.
  Values:  | 
| **$0100-$01FF**Processor stack
 | 
| $0100 | Reserved, do not use. (BAM input/output
  error indicator of not existing unit #1.) | 
| $0101 | Unit #0 BAM version code. (Byte at offset
  #$02 in sector 18;00.)Expected: $41, "A".
 | 
| $0102 | Reserved, do not use. (BAM version code of
  not existing unit #1.) | 
| $0103-$0145 | Actual processor stack. | 
| $0146-$01B9 | Unused. | 
| $01BA-$01FF | Auxiliary buffer for
  GCR-encoding/decoding.  | 
| **$0200-$02FF** | 
| $0200-$0229 | Input buffer (42 bytes). (Used for
  accepting commands from host.) | 
| $022A | DOS command number. Values: $00: OPEN.$01-$0B: DOS commands.$0C: OPEN "$".$80-$FE: "B-x" commands.$FF: Command too long. | 
| $022B-$023D | Channel number assigned to secondary
  addresses. Values: | 
| $023E-$0242 | Temporary area of next data byte to
  be written from buffers #0-#4 to serial bus. | 
| $0243 | Temporary area of next data byte to be
  written from error message buffer to serial bus. | 
| $0244-$0248 | Offset of last data byte in buffers
  #0-#4. | 
| $0249 | Offset of last data byte in error message
  buffer. | 
| $024A | File type of current file. | 
| $024B | Length of name of current file. | 
| $024C | Temporary area for secondary address. | 
| $024D | Temporary area for disk controller
  command. | 
| $024E | Number of sectors on current track. | 
| $024F-$0250 | Buffer allocation register.
  Bits: Default: $FFE0, all existing buffers are free. | 
| $0251 | Unit #0 BAM change indicator. Values: | 
| $0252 | Reserved, do not use. (BAM change
  indicator of not existing unit #1.) | 
| $0253 | File found indicator during searching for
  a file name in directory. Bits: | 
| $0254 | LOAD channel directory indicator.
  Values: | 
| $0255 | End of command indicator. Values: | 
| $0256 | Channel allocation register. Bits: | 
| $0257 | Temporary area for channel number.
  Values: | 
| $0258 | Record length of current relative
  file. | 
| $0259-$025A | Track and sector number of first
  side sector of current relative file. | 
| $025B-$025F | Original disk controller commands of
  buffers #0-#4. | 
| $0260-$0265 | Sector number of directory entry of
  files specified in command. | 
| $0266-$026B | Offset of directory entry of files
  specified in command. | 
| $026C | Switch for displaying warning messages of
  relative files. Values: Delay counter for LED blinking that indicates hardware
  problem upon startup. | 
| $026D | Unit #0 LED bit. Values: | 
| $026E | Unit number of previously opened file.
  (Used when opening "*".) | 
| $026F | Sector number of previously opened file.
  (Used when opening "*".) | 
| $0270 | Temporary area for channel number. | 
| $0271 | Unused. | 
| $0272-$0273 | BASIC line number for entries sent
  to host during LOAD'ing "$". (For header, unit number; for files, length of
  file, in blocks; for footer, number of free blocks.) | 
| $0274 | Length of command. | 
| $0275 | First character of command.Character to search for in input buffer.
 | 
| $0276 | Offset of first character after file name
  in command. | 
| $0277 | Temporary area for number of commas in
  command. | 
| $0278 | Number of commas or unit numbers in
  command. | 
| $0279 | Number of commas before equation mark in
  command.Number of current file in command during searching for files specified in
  command.
 | 
| $027A | Offset of character before colon in
  command. (Probably, the character resembles a unit number.) | 
| $027B-$027F | Offset of file names in command.
  (Last offset specifies end of command.) | 
| $0280-$0284 | Track number of files specified in
  command. Values: For "B-x" commands, upper byte of parameters. | 
| $0285-$0289 | Sector number of files specified in
  command. For "B-x" commands, lower byte of parameters. | 
| $028A | Number of wildcards found in current file
  name. | 
| $028B | Command syntax flags. Bits: Bit #0: 0 = Equation marks are present in the
    command.Bit #1: 1 = Equation marks are present in the
    command.Bit #2: 1 = Commas after equation marks are present
    in the command.Bit #3: 1 = Wildcards after equation marks are
    present in the command.Bit #6: 1 = Commas before equation marks are present
    in the command.Bit #7: 1 = Wildcards before equation marks are
    present in the command. | 
| $028C | Number of units to process during reading
  the directory. Values: $00: Only one unit.$01: Both units. | 
| $028D | Current unit number during reading the
  directory. Values: | 
| $028E | Previous unit number during reading the
  directory. | 
| $028F | Indicator to keep searching in the
  directory. Values: $00: More files are to be searched for.$01-$FF: All files have been found, no need to
    continue search. | 
| $0290 | Current directory sector number. | 
| $0291 | Directory sector number to read.
  Values: | 
| $0292 | Offset of current directory entry in
  directory sector. | 
| $0293 | End of directory indicator. Values: | 
| $0294 | Offset of current directory entry in
  directory sector. | 
| $0295 | Number of remaining directory entries in
  directory sector minus 1. Values: | 
| $0296 | File type of file being searched in
  directory. Values: | 
| $0297 | File open mode. Values: | 
| $0298 | Message display switch for disk errors.
  Bits: Bit #7: 0 = Silently ignore "26,WRITE PROTECT ON",
    "29,DISK ID MISMATCH" and "74,DRIVE NOT READY" errors when executing disk
    commands; 1 = Display error message. | 
| $0299 | Offset of current byte in halftrack seek
  table during retrying disk operations on adjacent halftracks. | 
| $029A | Direction of seeking back to original
  halftrack during retrying disk operations on adjacent halftracks. | 
| $029B | Unit #0 track number of current BAM
  entry. | 
| $029C | Reserved, do not use. (Track number of
  current BAM entry of not existing unit #1.) | 
| $029D-$029E | Unit #0 track numbers of two cached
  BAM entries. | 
| $029F-$02A0 | Reserved, do not use. (Track numbers
  of two cached BAM entries of not existing unit #1). | 
| $02A1-$02A8 | Unit #0 two cached BAM entries. | 
| $02A9-$02B0 | Reserved, do not use. (Two cached
  BAM entries of not existing unit #1.) | 
| $02B1-$02CB | Buffer for constructing current
  entry (BASIC line) while LOAD'ing "$". | 
| $02CC-$02D4 | Unused. | 
| $02D5-$02F8 | Error message buffer. | 
| $02F9 | Disk update upon BAM change switch.
  Different BAM-related operations expect different values here. | 
| $02FA | Unit #0 number of free blocks, low
  byte. | 
| $02FB | Reserved, do not use. (Number of free
  blocks, low byte, of not existing unit #1.) | 
| $02FC | Unit #0 number of free blocks, high
  byte. | 
| $02FD | Reserved, do not use. (Number of free
  blocks, high byte, of not existing unit #1.) | 
| $02FE | Unit #0 direction of seeking of adjacent
  halftrack. Values: $00: No seeking.$01: Seek a halftrack upwards.$02: Halftrack seeking complete.$FF: Seek a halftrack downwards. | 
| $02FF | Reserved, do not use. (Direction of
  seeking of adjacent halftrack of not existing unit #1.)  | 
| **$0300-$07FF**Data buffers
 | 
| $0300-$03FF | Buffer #0. | 
| $0400-$04FF | Buffer #1. | 
| $0500-$05FF | Buffer #2. | 
| $0600-$06FF | Buffer #3. | 
| $0700-$07FF | Buffer #4.  | 
| **$1800-$180F**VIA #1; serial bus
  access
 | 
| $1800 | Port B, serial bus. Bits: Bit #0: DATA IN; 0 = Low; 1 = High.Bit #1: DATA OUT; 0 = Low; 1 = High.Bit #2: CLOCK IN; 0 = Low; 1 = High.Bit #3: CLOCK OUT; 0 = Low; 1 = High.Bit #4: ATNA OUT; 1 = Enable device presence
    detection by automatically acknowledging ATN IN signals on DATA OUT.Bits #5-#6: Device number, set with jumper, minus 8;
    %00 = 8; %01 = 9; %10 = 10; %11 = 11. Default: %00, 8.Bit #7: ATN IN; 0 = Low; 1 = High. | 
| $1801 | Port A. Read to acknowledge interrupt
  generated by ATN IN going high. | 
| $1802 | Port B data direction register. Bits: Default: $1A, %00011010. | 
| $1803 | Port A data direction register.Default: $FF, %11111111.
 | 
| $1804-$1805 | Timer. Read low byte or write high
  byte to start timer or restart timer upon underflow. | 
| $1806-$1807 | Timer latch. Read/write starting
  value of timer from/to here. | 
| $1808-$180A | Unused. | 
| $180B | Timer control register. Bits: | 
| $180C | Unused. | 
| $180D | Interrupt status register. Bits: | 
| $180E | Interrupt control register. Read bits: Write bits: Bit #1: 1 = Enable interrupts generated by ATN IN
   going high.Bit #7: Fill bit; bits #0-#6, that are set to 1, get
    their values from this bit; bits #0-#6, that are set to 0, are left
    unchanged. | 
| $180F | Unused.  | 
| **$1C00-$1C0F**VIA #2; drive control
 | 
| $1C00 | Port B. Bits: Bits #0-#1: Head step direction. Decrease value
    (%00-%11-%10-%01-%00...) to move head downwards; increase value
    (%00-%01-%10-%11-%00...) to move head upwards.Bit #2: Motor control; 0 = Off; 1 = On.Bit #3: LED control; 0 = Off; 1 = On.Bit #4: Write protect photocell status; 0 = Write
    protect tab covered, disk protected; 1 = Tab uncovered, disk not
    protected.Bits #5-#6: Data density; %00 = Lowest; %11 =
    Highest.Bit #7: 0 = SYNC marks are being currently read from
    disk; 1 = Data bytes are being read. | 
| $1C01 | Port A. Data byte last read from or to be
  next written onto disk. | 
| $1C02 | Port B data direction register. Bits: Default: $6F, %01101111. | 
| $1C03 | Port A data direction register. Bits: Values: $00: Read from disk.$FF: Write onto disk. | 
| $1C04-$1C05 | Timer. Read low byte or write high
  byte to start timer or restart timer upon underflow. | 
| $1C06-$1C07 | Timer latch. Read/write starting
  value of timer from/to here. | 
| $1C08-$1C0A | Unused. | 
| $1C0B | Timer control register. Bits: | 
| $1C0C | Auxiliary control register. Bits: Bits #1-#3: %111 = Attach Byte Ready line to oVerflow
    processor flag. (Whenever a data byte has been successfully read from or
    written to disk, V flag is set to 1.)Bits #5-#7: Head control; %111 = Read; %110 = Write. | 
| $1C0D | Interrupt status register. Bits: | 
| $1C0E | Interrupt control register. Read bits: Write bits: Bit #6: 1 = Enable interrupts generated by timer
    underflow.Bit #7: Fill bit; bits #0-#6, that are set to 1, get
    their values from this bit; bits #0-#6, that are set to 0, are left
    unchanged. | 
| $1C0F | Unused. |

---
*Fonte originale: [https://sta.c64.org/cbm1541mem.html](https://sta.c64.org/cbm1541mem.html)*
