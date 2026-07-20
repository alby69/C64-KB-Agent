---
title: base:makefile_to_use_with_ca65_vice [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Amakefile_to_use_with_ca65_vice
category: reference
topics:
- raster interrupts
difficulty: beginner
language: none
hardware:
- CPU
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---

# base:makefile_to_use_with_ca65_vice [Codebase64 wiki]

base:makefile_to_use_with_ca65_vice

                Simple Makefile for ca65 projects, that puts compiled binary to .d64 files, and also shows the directory. Variation of this is used in practically all of my modern C64 projects.

“make run” also passes labels to VICE monitor for easier debugging.

Tested on Ubuntu & MorphOS.

CPU = 6502 C1541 = c1541 # Also pass symbols to VICE monitor X64 = x64 -moncommands symbols OUTPUT = "diskcontents/myprg.prg" DISKFILENAME = my.d64 DISKNAME = myprg ID = 17 AS = ca65 # Add defines, if needed (-DWHATEVER) ASFLAGS = -g --cpu $(CPU) --include-dir src/ LD = ld65 #Define segments & files in config.cfg LDFLAGS = -m labels.txt -Ln symbols -o $(OUTPUT) -C config.cfg OBJS = \ src/main.o \ src/irq.o all: d64 myprg: $(OBJS) $(LD) $(LDFLAGS) $(OBJS) d64: myprg $(C1541) -format $(DISKNAME),$(ID) d64 $(DISKFILENAME) $(C1541) -attach $(DISKFILENAME) -write $(OUTPUT) $(C1541) -attach $(DISKFILENAME) -list run: d64 $(X64) $(DISKFILENAME) clean: rm -f src/*.o diskcontents/* labels.txt symbols $(DISKFILENAME)

base/makefile_to_use_with_ca65_vice.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
CPU = 6502
C1541 = c1541
# Also pass symbols to VICE monitor
X64 = x64 -moncommands symbols
OUTPUT = "diskcontents/myprg.prg"

DISKFILENAME = my.d64
DISKNAME = myprg
ID = 17

AS = ca65
# Add defines, if needed (-DWHATEVER)
ASFLAGS = -g --cpu $(CPU) --include-dir src/

LD = ld65
#Define segments & files in config.cfg
LDFLAGS = -m labels.txt -Ln symbols -o $(OUTPUT) -C config.cfg

OBJS = \
	src/main.o \
	src/irq.o

all: d64

myprg: $(OBJS)
	$(LD) $(LDFLAGS) $(OBJS)

d64: myprg
	$(C1541) -format $(DISKNAME),$(ID) d64 $(DISKFILENAME)
	$(C1541) -attach $(DISKFILENAME) -write $(OUTPUT)
	$(C1541) -attach $(DISKFILENAME) -list

run: d64
	$(X64) $(DISKFILENAME)

clean:
	rm -f src/*.o diskcontents/* labels.txt symbols $(DISKFILENAME)
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Amakefile_to_use_with_ca65_vice](https://codebase.c64.org/doku.php?id=base%3Amakefile_to_use_with_ca65_vice)*
