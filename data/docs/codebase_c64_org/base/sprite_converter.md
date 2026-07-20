---
title: Bitmap to sprite converter written in Python
source_url: https://codebase.c64.org/doku.php?id=base%3Asprite_converter
category: reference
topics:
- graphics
- assembly
- sprite programming
- basic
difficulty: beginner
language: mixed
hardware:
- KERNAL
- VIC-II
related:
- memory-map
- sprite-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Bitmap to sprite converter written in Python

base:sprite_converter

                # Bitmap to sprite converter written in Python

This is a simple Python hack that converts monochrome images with a multiple of 24x21px to an array of sprites. It can save the sprites with or without load address. Public Domain.

```
#!/usr/bin/env python
# .spr converter for arbitrary sized images (multiple of 24x21)
# 1st argument: file to convert
# 2nd argument: target file
# 3rd argument: load address in hex (optional)
# no error checking at all, I'm lazy :)
import sys, struct
from PIL import Image
img = Image.open(sys.argv[1]).convert("1")
if (img.size[0] % 24) != 0 or (img.size[1] % 21) != 0:
    print "image size of %s isn't a multiple of 24x21!" % (str(img.size))
    print "exiting!"
    sys.exit(1)
xoff = 0
yoff = 0
if len(sys.argv) > 3:
    print "adding loader address"
    sprbuf = struct.pack("<H", int(sys.argv[3], 16))
else:
    sprbuf = str()
while yoff < img.size[1]:
    while xoff < img.size[0]:
        crop = (xoff, yoff, xoff+24, yoff+21)
        print crop
        cut = img.crop(crop)
        cut_str = cut.tostring()
        sprbuf = sprbuf + cut_str + struct.pack("x")
        xoff = xoff + 24
    yoff = yoff + 21
    xoff = 0
open(sys.argv[2], "w").write(sprbuf)
```
base/sprite_converter.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
#!/usr/bin/env python
# .spr converter for arbitrary sized images (multiple of 24x21)
# 1st argument: file to convert
# 2nd argument: target file
# 3rd argument: load address in hex (optional)
# no error checking at all, I'm lazy :)

import sys, struct
from PIL import Image

img = Image.open(sys.argv[1]).convert("1")

if (img.size[0] % 24) != 0 or (img.size[1] % 21) != 0:
    print "image size of %s isn't a multiple of 24x21!" % (str(img.size))
    print "exiting!"
    sys.exit(1)

xoff = 0
yoff = 0

if len(sys.argv) > 3:
    print "adding loader address"
    sprbuf = struct.pack("<H", int(sys.argv[3], 16))
else:
    sprbuf = str()

while yoff < img.size[1]:
    while xoff < img.size[0]:
        crop = (xoff, yoff, xoff+24, yoff+21)
        print crop
        cut = img.crop(crop)
        cut_str = cut.tostring()
        sprbuf = sprbuf + cut_str + struct.pack("x")
        xoff = xoff + 24
    yoff = yoff + 21
    xoff = 0

open(sys.argv[2], "w").write(sprbuf)
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asprite_converter](https://codebase.c64.org/doku.php?id=base%3Asprite_converter)*
