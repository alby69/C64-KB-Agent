---
title: tape write IRQ routine
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 00b0-cmp0
- 00c0-cas1
- eor
- fbcd-schreiben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FBCD
  address_end: $FC68
  symbol: tape-write-irq-routine
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FBCD**: get start bit first cycle done flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FBCD**: falls ''Byte''-Impuls ge-'
---

# $FBCD — tape write IRQ routine

## Disassemblatura
```assembly
.FBCD  A5 A8    LDA $A8   ; get start bit first cycle done flag
.FBCF  D0 12    BNE $FBE3   ; if first cycle done go do rest of byte each byte sent starts with two half cycles of $0110 system clocks and the whole block ends with two more such half cycles
.FBD1  A9 10    LDA #$10   ; set first start cycle time constant low byte
.FBD3  A2 01    LDX #$01   ; set first start cycle time constant high byte
.FBD5  20 B1 FB JSR $FBB1   ; write time constant and toggle tape
.FBD8  D0 2F    BNE $FC09   ; if first half cycle go restore registers and exit interrupt
.FBDA  E6 A8    INC $A8   ; set start bit first start cycle done flag
.FBDC  A5 B6    LDA $B6   ; get buffer address high byte
.FBDE  10 29    BPL $FC09   ; if block not complete go restore registers and exit interrupt. the end of a block is indicated by the tape buffer high byte b7 being set to 1
.FBE0  4C 57 FC JMP $FC57   ; else do tape routine, block complete exit continue tape byte write. the first start cycle, both half cycles of it, is complete so the routine drops straight through to here
.FBE3  A5 A9    LDA $A9   ; get start bit check flag
.FBE5  D0 09    BNE $FBF0   ; if the start bit is complete go send the byte bits after the two half cycles of $0110 system clocks the start bit is completed with two half cycles of $00B0 system clocks. this is the same as the first part of a 1 bit
.FBE7  20 AD FB JSR $FBAD   ; set time constant for bit = 1 and toggle tape
.FBEA  D0 1D    BNE $FC09   ; if first half cycle go restore registers and exit interrupt
.FBEC  E6 A9    INC $A9   ; set start bit check flag
.FBEE  D0 19    BNE $FC09   ; restore registers and exit interrupt, branch always continue tape byte write. the start bit, both cycles of it, is complete so the routine drops straight through to here. now the cycle pairs for each bit, and the parity bit, are sent
.FBF0  20 A6 FB JSR $FBA6   ; send lsb from tape write byte to tape
.FBF3  D0 14    BNE $FC09   ; if first half cycle go restore registers and exit interrupt else two half cycles have been done
.FBF5  A5 A4    LDA $A4   ; get tape bit cycle phase
.FBF7  49 01    EOR #$01   ; toggle b0
.FBF9  85 A4    STA $A4   ; save tape bit cycle phase
.FBFB  F0 0F    BEQ $FC0C   ; if bit cycle phase complete go setup for next bit each bit is written as two full cycles. a 1 is sent as a full cycle of $0160 system clocks then a full cycle of $00C0 system clocks. a 0 is sent as a full cycle of $00C0 system clocks then a full cycle of $0160 system clocks. to do this each bit from the write byte is inverted during the second bit cycle phase. as the bit is inverted it is also added to the, one bit, parity count for this byte
.FBFD  A5 BD    LDA $BD   ; get tape write byte
.FBFF  49 01    EOR #$01   ; invert bit being sent
.FC01  85 BD    STA $BD   ; save tape write byte
.FC03  29 01    AND #$01   ; mask b0
.FC05  45 9B    EOR $9B   ; EOR with tape write byte parity bit
.FC07  85 9B    STA $9B   ; save tape write byte parity bit
.FC09  4C BC FE JMP $FEBC   ; restore registers and exit interrupt the bit cycle phase is complete so shift out the just written bit and test for byte end
.FC0C  46 BD    LSR $BD   ; shift bit out of tape write byte
.FC0E  C6 A3    DEC $A3   ; decrement tape write bit count
.FC10  A5 A3    LDA $A3   ; get tape write bit count
.FC12  F0 3A    BEQ $FC4E   ; if all the data bits have been written go setup for sending the parity bit next and exit the interrupt
.FC14  10 F3    BPL $FC09   ; if all the data bits are not yet sent just restore the registers and exit the interrupt do next tape byte the byte is complete. the start bit, data bits and parity bit have been written to the tape so setup for the next byte
.FC16  20 97 FB JSR $FB97   ; new tape byte setup
.FC19  58       CLI   ; enable the interrupts
.FC1A  A5 A5    LDA $A5   ; get cassette synchronization character count
.FC1C  F0 12    BEQ $FC30   ; if synchronisation characters done go do block data at the start of each block sent to tape there are a number of synchronisation bytes that count down to the actual data. the commodore tape system saves two copies of all the tape data, the first is loaded and is indicated by the synchronisation bytes having b7 set, and the second copy is indicated by the synchronisation bytes having b7 clear. the sequence goes $09, $08, ..... $02, $01, data bytes
.FC1E  A2 00    LDX #$00   ; clear X
.FC20  86 D7    STX $D7   ; clear checksum byte
.FC22  C6 A5    DEC $A5   ; decrement cassette synchronization byte count
.FC24  A6 BE    LDX $BE   ; get cassette copies count
.FC26  E0 02    CPX #$02   ; compare with load block indicator
.FC28  D0 02    BNE $FC2C   ; branch if not the load block
.FC2A  09 80    ORA #$80   ; this is the load block so make the synchronisation count go $89, $88, ..... $82, $81
.FC2C  85 BD    STA $BD   ; save the synchronisation byte as the tape write byte
.FC2E  D0 D9    BNE $FC09   ; restore registers and exit interrupt, branch always the synchronization bytes have been done so now check and do the actual block data
.FC30  20 D1 FC JSR $FCD1   ; check read/write pointer, return Cb = 1 if pointer >= end
.FC33  90 0A    BCC $FC3F   ; if not all done yet go get the byte to send
.FC35  D0 91    BNE $FBC8   ; if pointer > end go flag block done and exit interrupt else the block is complete, it only remains to write the checksum byte to the tape so setup for that
.FC37  E6 AD    INC $AD   ; increment buffer pointer high byte, this means the block done branch will always be taken next time without having to worry about the low byte wrapping to zero
.FC39  A5 D7    LDA $D7   ; get checksum byte
.FC3B  85 BD    STA $BD   ; save checksum as tape write byte
.FC3D  B0 CA    BCS $FC09   ; restore registers and exit interrupt, branch always the block isn't finished so get the next byte to write to tape
.FC3F  A0 00    LDY #$00   ; clear index
.FC41  B1 AC    LDA ($AC),Y   ; get byte from buffer
.FC43  85 BD    STA $BD   ; save as tape write byte
.FC45  45 D7    EOR $D7   ; XOR with checksum byte
.FC47  85 D7    STA $D7   ; save new checksum byte
.FC49  20 DB FC JSR $FCDB   ; increment read/write pointer
.FC4C  D0 BB    BNE $FC09   ; restore registers and exit interrupt, branch always set parity as next bit and exit interrupt
.FC4E  A5 9B    LDA $9B   ; get parity bit
.FC50  49 01    EOR #$01   ; toggle it
.FC52  85 BD    STA $BD   ; save as tape write byte
.FC54  4C BC FE JMP $FEBC   ; restore registers and exit interrupt tape routine, block complete exit
.FC57  C6 BE    DEC $BE   ; decrement copies remaining to read/write
.FC59  D0 03    BNE $FC5E   ; branch if more to do
.FC5B  20 CA FC JSR $FCCA   ; stop the cassette motor
.FC5E  A9 50    LDA #$50   ; set tape write leader count
.FC60  85 A7    STA $A7   ; save tape write leader count
.FC62  A2 08    LDX #$08   ; set index for write tape leader vector
.FC64  78       SEI   ; disable the interrupts
.FC65  20 BD FC JSR $FCBD   ; set the tape vector
.FC68  D0 EA    BNE $FC54   ; restore registers and exit interrupt, branch always
```


## Commenti

### Original Disassembly (—)
- **$FBCD**: get start bit first cycle done flag
- **$FBCF**: if first cycle done go do rest of byte each byte sent starts with two half cycles of $0110 system clocks and the whole block ends with two more such half cycles
- **$FBD1**: set first start cycle time constant low byte
- **$FBD3**: set first start cycle time constant high byte
- **$FBD5**: write time constant and toggle tape
- **$FBD8**: if first half cycle go restore registers and exit interrupt
- **$FBDA**: set start bit first start cycle done flag
- **$FBDC**: get buffer address high byte
- **$FBDE**: if block not complete go restore registers and exit interrupt. the end of a block is indicated by the tape buffer high byte b7 being set to 1
- **$FBE0**: else do tape routine, block complete exit continue tape byte write. the first start cycle, both half cycles of it, is complete so the routine drops straight through to here
- **$FBE3**: get start bit check flag
- **$FBE5**: if the start bit is complete go send the byte bits after the two half cycles of $0110 system clocks the start bit is completed with two half cycles of $00B0 system clocks. this is the same as the first part of a 1 bit
- **$FBE7**: set time constant for bit = 1 and toggle tape
- **$FBEA**: if first half cycle go restore registers and exit interrupt
- **$FBEC**: set start bit check flag
- **$FBEE**: restore registers and exit interrupt, branch always continue tape byte write. the start bit, both cycles of it, is complete so the routine drops straight through to here. now the cycle pairs for each bit, and the parity bit, are sent
- **$FBF0**: send lsb from tape write byte to tape
- **$FBF3**: if first half cycle go restore registers and exit interrupt else two half cycles have been done
- **$FBF5**: get tape bit cycle phase
- **$FBF7**: toggle b0
- **$FBF9**: save tape bit cycle phase
- **$FBFB**: if bit cycle phase complete go setup for next bit each bit is written as two full cycles. a 1 is sent as a full cycle of $0160 system clocks then a full cycle of $00C0 system clocks. a 0 is sent as a full cycle of $00C0 system clocks then a full cycle of $0160 system clocks. to do this each bit from the write byte is inverted during the second bit cycle phase. as the bit is inverted it is also added to the, one bit, parity count for this byte
- **$FBFD**: get tape write byte
- **$FBFF**: invert bit being sent
- **$FC01**: save tape write byte
- **$FC03**: mask b0
- **$FC05**: EOR with tape write byte parity bit
- **$FC07**: save tape write byte parity bit
- **$FC09**: restore registers and exit interrupt the bit cycle phase is complete so shift out the just written bit and test for byte end
- **$FC0C**: shift bit out of tape write byte
- **$FC0E**: decrement tape write bit count
- **$FC10**: get tape write bit count
- **$FC12**: if all the data bits have been written go setup for sending the parity bit next and exit the interrupt
- **$FC14**: if all the data bits are not yet sent just restore the registers and exit the interrupt do next tape byte the byte is complete. the start bit, data bits and parity bit have been written to the tape so setup for the next byte
- **$FC16**: new tape byte setup
- **$FC19**: enable the interrupts
- **$FC1A**: get cassette synchronization character count
- **$FC1C**: if synchronisation characters done go do block data at the start of each block sent to tape there are a number of synchronisation bytes that count down to the actual data. the commodore tape system saves two copies of all the tape data, the first is loaded and is indicated by the synchronisation bytes having b7 set, and the second copy is indicated by the synchronisation bytes having b7 clear. the sequence goes $09, $08, ..... $02, $01, data bytes
- **$FC1E**: clear X
- **$FC20**: clear checksum byte
- **$FC22**: decrement cassette synchronization byte count
- **$FC24**: get cassette copies count
- **$FC26**: compare with load block indicator
- **$FC28**: branch if not the load block
- **$FC2A**: this is the load block so make the synchronisation count go $89, $88, ..... $82, $81
- **$FC2C**: save the synchronisation byte as the tape write byte
- **$FC2E**: restore registers and exit interrupt, branch always the synchronization bytes have been done so now check and do the actual block data
- **$FC30**: check read/write pointer, return Cb = 1 if pointer >= end
- **$FC33**: if not all done yet go get the byte to send
- **$FC35**: if pointer > end go flag block done and exit interrupt else the block is complete, it only remains to write the checksum byte to the tape so setup for that
- **$FC37**: increment buffer pointer high byte, this means the block done branch will always be taken next time without having to worry about the low byte wrapping to zero
- **$FC39**: get checksum byte
- **$FC3B**: save checksum as tape write byte
- **$FC3D**: restore registers and exit interrupt, branch always the block isn't finished so get the next byte to write to tape
- **$FC3F**: clear index
- **$FC41**: get byte from buffer
- **$FC43**: save as tape write byte
- **$FC45**: XOR with checksum byte
- **$FC47**: save new checksum byte
- **$FC49**: increment read/write pointer
- **$FC4C**: restore registers and exit interrupt, branch always set parity as next bit and exit interrupt
- **$FC4E**: get parity bit
- **$FC50**: toggle it
- **$FC52**: save as tape write byte
- **$FC54**: restore registers and exit interrupt tape routine, block complete exit
- **$FC57**: decrement copies remaining to read/write
- **$FC59**: branch if more to do
- **$FC5B**: stop the cassette motor
- **$FC5E**: set tape write leader count
- **$FC60**: save tape write leader count
- **$FC62**: set index for write tape leader vector
- **$FC64**: disable the interrupts
- **$FC65**: set the tape vector
- **$FC68**: restore registers and exit interrupt, branch always

### Commodore-64-intern-Buch (Commodore)
- **$FBCD**: falls 'Byte'-Impuls ge-
- **$FBCF**: schrieben, dann verzweige
- **$FBD1**: Timer auf
- **$FBD3**: $110 (272)
- **$FBD5**: Takt auf Band schreiben
- **$FBD8**: Rückkehr vom Interrupt
- **$FBDA**: '1' Byte-Write-Flag setzen
- **$FBDC**: falls Block-Write-Flag positiv, dann
- **$FBDE**: Rückkehr vom Interrupt
- **$FBE0**: zweiten Block schreiben
- **$FBE3**: falls '1' Bit gesezt
- **$FBE5**: dann verzweige
- **$FBE7**: '1' Bit schreiben
- **$FBEA**: Rückkehr vom Interrupt
- **$FBEC**: '1' Bit-Flag setzen
- **$FBEE**: Rückkehr vom Interrupt
- **$FBF0**: Bit auf Band schreiben
- **$FBF3**: Rückkehr vom Interrupt
- **$FBF5**: Bit-Impulsflag laden
- **$FBF7**: Bit 0 invertieren
- **$FBF9**: und speichern
- **$FBFB**: falls null, dann verzweige
- **$FBFD**: Bit-SHIFT-Register laden
- **$FBFF**: Bit für Ausgabe invertieren
- **$FC01**: und speichern
- **$FC03**: Bit holen und mit
- **$FC05**: Parity-Bit verknüpfen
- **$FC07**: und speichern
- **$FC09**: Rückkehr vom Interrupt
- **$FC0C**: nächstes Bit in Position 0
- **$FC0E**: Bitzähler erniedrigen
- **$FC10**: und laden
- **$FC12**: nächstes Bit ausgeben
- **$FC14**: Rückkehr vom Interrupt
- **$FC16**: Bitzähler wieder auf 8 setzen
- **$FC19**: Interrupt freigeben
- **$FC1A**: Falls Synchronbytes geschrie- ben
- **$FC1C**: dann verzweige
- **$FC1E**: Prüfsumme
- **$FC20**: löschen
- **$FC22**: Zähler vermindern
- **$FC24**: noch zu schreibende Blockanzahl laden
- **$FC26**: falls erster Block nicht
- **$FC28**: geschrieben, dann verzweige
- **$FC2A**: Bit 7 setzen
- **$FC2C**: und speichern
- **$FC2E**: Rückkehr vom Interrupt
- **$FC30**: Endadresse schon erreicht ?
- **$FC33**: falls kleiner, dann weiterschreiben
- **$FC35**: falls ungleich, dann Block-Write-Flag setzen
- **$FC37**: HIGH-Byte ungleich machen
- **$FC39**: Prüfsumme laden
- **$FC3B**: und in SHIFT-Flag speichern
- **$FC3D**: Rückkehr vom Interrupt
- **$FC3F**: Zähler auf Null
- **$FC41**: zu schreibendes Byte laden
- **$FC43**: in SHIFT-Flag bringen
- **$FC45**: Prüfsumme
- **$FC47**: bilden
- **$FC49**: Adresszeiger erhöhen
- **$FC4C**: Rückkehr vom Interrupt
- **$FC4E**: Parity-Bit
- **$FC50**: invertieren
- **$FC52**: und ins SHIFT-Flag speichern
- **$FC54**: Rückkehr vom Interrupt
- **$FC57**: Zähler für Blocks erniedrigen
- **$FC59**: falls noch ein Block,
- **$FC5B**: dann Bandmotor aus
- **$FC5E**: 80
- **$FC60**: Zähler für Impulse
- **$FC62**: Offset für IRQ
- **$FC64**: Interrupt verhindern
- **$FC65**: IRQ auf $FC6A
- **$FC68**: Rückkehr vom Interrupt

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*