---
title: wait for a key from the keyboard
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
- e5cd-wait-for-a-key-from-the-keyboard
- ece7-load
- ecec-run
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $E5CD
  address_end: $E630
  symbol: wait-for-a-key-from-the-keyboard
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E5CD**: get the keyboard buffer index'
---

# $E5CD — wait for a key from the keyboard

## Disassemblatura
```assembly
.E5CD  A5 C6    LDA $C6   ; get the keyboard buffer index
.E5CF  85 CC    STA $CC   ; cursor enable, $00 = flash cursor, $xx = no flash
.E5D1  8D 92 02 STA $0292   ; screen scrolling flag, $00 = scroll, $xx = no scroll this disables both the cursor flash and the screen scroll while there are characters in the keyboard buffer
.E5D4  F0 F7    BEQ $E5CD   ; loop if the buffer is empty
.E5D6  78       SEI   ; disable the interrupts
.E5D7  A5 CF    LDA $CF   ; get the cursor blink phase
.E5D9  F0 0C    BEQ $E5E7   ; if cursor phase skip the overwrite else it is the character phase
.E5DB  A5 CE    LDA $CE   ; get the character under the cursor
.E5DD  AE 87 02 LDX $0287   ; get the colour under the cursor
.E5E0  A0 00    LDY #$00   ; clear Y
.E5E2  84 CF    STY $CF   ; clear the cursor blink phase
.E5E4  20 13 EA JSR $EA13   ; print character A and colour X
.E5E7  20 B4 E5 JSR $E5B4   ; input from the keyboard buffer
.E5EA  C9 83    CMP #$83   ; compare with [SHIFT][RUN]
.E5EC  D0 10    BNE $E5FE   ; if not [SHIFT][RUN] skip the buffer fill keys are [SHIFT][RUN] so put "LOAD",$0D,"RUN",$0D into the buffer
.E5EE  A2 09    LDX #$09   ; set the byte count
.E5F0  78       SEI   ; disable the interrupts
.E5F1  86 C6    STX $C6   ; set the keyboard buffer index
.E5F3  BD E6 EC LDA $ECE6,X   ; get byte from the auto load/run table
.E5F6  9D 76 02 STA $0276,X   ; save it to the keyboard buffer
.E5F9  CA       DEX   ; decrement the count/index
.E5FA  D0 F7    BNE $E5F3   ; loop while more to do
.E5FC  F0 CF    BEQ $E5CD   ; loop for the next key, branch always was not [SHIFT][RUN]
.E5FE  C9 0D    CMP #$0D   ; compare the key with [CR]
.E600  D0 C8    BNE $E5CA   ; if not [CR] print the character and get the next key else it was [CR]
.E602  A4 D5    LDY $D5   ; get the current screen line length
.E604  84 D0    STY $D0   ; input from keyboard or screen, $xx = screen, $00 = keyboard
.E606  B1 D1    LDA ($D1),Y   ; get the character from the current screen line
.E608  C9 20    CMP #$20   ; compare it with [SPACE]
.E60A  D0 03    BNE $E60F   ; if not [SPACE] continue
.E60C  88       DEY   ; else eliminate the space, decrement end of input line
.E60D  D0 F7    BNE $E606   ; loop, branch always
.E60F  C8       INY   ; increment past the last non space character on line
.E610  84 C8    STY $C8   ; save the input [EOL] pointer
.E612  A0 00    LDY #$00   ; clear A
.E614  8C 92 02 STY $0292   ; clear the screen scrolling flag, $00 = scroll
.E617  84 D3    STY $D3   ; clear the cursor column
.E619  84 D4    STY $D4   ; clear the cursor quote flag, $xx = quote, $00 = no quote
.E61B  A5 C9    LDA $C9   ; get the input cursor row
.E61D  30 1B    BMI $E63A
.E61F  A6 D6    LDX $D6   ; get the cursor row
.E621  20 ED E6 JSR $E6ED   ; find and set the pointers for the start of logical line
.E624  E4 C9    CPX $C9   ; compare with input cursor row
.E626  D0 12    BNE $E63A
.E628  A5 CA    LDA $CA   ; get the input cursor column
.E62A  85 D3    STA $D3   ; save the cursor column
.E62C  C5 C8    CMP $C8   ; compare the cursor column with input [EOL] pointer
.E62E  90 0A    BCC $E63A   ; if less, cursor is in line, go ??
.E630  B0 2B    BCS $E65D   ; else the cursor is beyond the line end, branch always
```


## Commenti

### Original Disassembly (—)
- **$E5CD**: get the keyboard buffer index
- **$E5CF**: cursor enable, $00 = flash cursor, $xx = no flash
- **$E5D1**: screen scrolling flag, $00 = scroll, $xx = no scroll this disables both the cursor flash and the screen scroll while there are characters in the keyboard buffer
- **$E5D4**: loop if the buffer is empty
- **$E5D6**: disable the interrupts
- **$E5D7**: get the cursor blink phase
- **$E5D9**: if cursor phase skip the overwrite else it is the character phase
- **$E5DB**: get the character under the cursor
- **$E5DD**: get the colour under the cursor
- **$E5E0**: clear Y
- **$E5E2**: clear the cursor blink phase
- **$E5E4**: print character A and colour X
- **$E5E7**: input from the keyboard buffer
- **$E5EA**: compare with [SHIFT][RUN]
- **$E5EC**: if not [SHIFT][RUN] skip the buffer fill keys are [SHIFT][RUN] so put "LOAD",$0D,"RUN",$0D into the buffer
- **$E5EE**: set the byte count
- **$E5F0**: disable the interrupts
- **$E5F1**: set the keyboard buffer index
- **$E5F3**: get byte from the auto load/run table
- **$E5F6**: save it to the keyboard buffer
- **$E5F9**: decrement the count/index
- **$E5FA**: loop while more to do
- **$E5FC**: loop for the next key, branch always was not [SHIFT][RUN]
- **$E5FE**: compare the key with [CR]
- **$E600**: if not [CR] print the character and get the next key else it was [CR]
- **$E602**: get the current screen line length
- **$E604**: input from keyboard or screen, $xx = screen, $00 = keyboard
- **$E606**: get the character from the current screen line
- **$E608**: compare it with [SPACE]
- **$E60A**: if not [SPACE] continue
- **$E60C**: else eliminate the space, decrement end of input line
- **$E60D**: loop, branch always
- **$E60F**: increment past the last non space character on line
- **$E610**: save the input [EOL] pointer
- **$E612**: clear A
- **$E614**: clear the screen scrolling flag, $00 = scroll
- **$E617**: clear the cursor column
- **$E619**: clear the cursor quote flag, $xx = quote, $00 = no quote
- **$E61B**: get the input cursor row
- **$E61F**: get the cursor row
- **$E621**: find and set the pointers for the start of logical line
- **$E624**: compare with input cursor row
- **$E628**: get the input cursor column
- **$E62A**: save the cursor column
- **$E62C**: compare the cursor column with input [EOL] pointer
- **$E62E**: if less, cursor is in line, go ??
- **$E630**: else the cursor is beyond the line end, branch always

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*