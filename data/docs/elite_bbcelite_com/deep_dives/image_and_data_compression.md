---
title: Image and data compression
source_url: https://elite.bbcelite.com/deep_dives/image_and_data_compression.html
category: source-code
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CPU
- CIA
- BASIC ROM
related:
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- cia-registers
scraped_at: '2026-07-20'
---

# Image and data compression

## How images and data are compressed in NES Elite

One of the advantages of running Elite on the NES is the vastly increased amount of program space compared to earlier versions. The NES Elite ROM cartridge contains 128K of ROM, and that's just for the program code; in comparison the original BBC Micro version used pretty much every spare byte and had to squeeze the game binary into a relatively tiny 21K (see the [BBC Micro cassette Elite memory map](https://elite.bbcelite.com/the_elite_memory_map.html) for details). To authors who were so used to chasing down every single free byte, that 128K of NES ROM must have felt endless.

But as we all know, storage space has a habit of filling itself up, and if you take all the [extra languages](https://elite.bbcelite.com/multi-language_support_in_nes_elite.html) and [sophisticated graphics routines](https://elite.bbcelite.com/drawing_vector_graphics_using_nes_tiles.html) and [multi-layer images](https://elite.bbcelite.com/displaying_two-layer_images.html) and try to squeeze them into 128K, they just don't fit, and by quite a long way too. It turns out that 128K isn't as large as it first seems, especially when you're playing with fancy graphics like the Elite logo on the Start screen:

![The Start screen in NES Elite](https://elite.bbcelite.com/images/nes/general/start.png) 

						As a result, Elite on the NES contains routines to unpack compressed blocks of data, which take up less space than they otherwise would. The [tokenised text system](https://elite.bbcelite.com/printing_text_tokens.html) that the authors developed for the original BBC Micro version is still present and correct, but these new routines decompress images and other binary data, unpacking the results into RAM or directly into the PPU.

We'll take a look at the algorithm in a moment, but first let's see how well it works on the data in Elite. Meanwhile, if you want to see what the unpacked images look like, check out the images folder in the [accompanying repository](https://github.com/markmoxon/elite-source-code-nes/tree/main/1-source-files/images), where you can also find Python scripts that implement the [unpacking process](https://github.com/markmoxon/elite-source-code-nes/blob/main/2-build-files/unpack-data.py) and [combine the results](https://github.com/markmoxon/elite-source-code-nes/blob/main/2-build-files/combine-images.py) into image files.

## Compression statistics

													 ----------------------

						The unpacking routines are at [UnpackToRAM](https://elite.bbcelite.com/nes/bank_7/subroutine/unpacktoram.html) and [UnpackToPPU](https://elite.bbcelite.com/nes/bank_7/subroutine/unpacktoppu.html), but before we pull them apart, let's take a look at how much memory they actually save.

The biggest single-use chunk of memory in NES Elite is taken up by the 15 system images in [ROM bank 5](https://elite.bbcelite.com/nes/all/bank_5.html), which gobble up 16,043 bytes between them (leaving precious little space out of the ROM bank's total size of 16,384 bytes). These 16,043 bytes contains the packed images, so let's see how the packed and unpacked versions compare.

Each system image unpacks to take up 1792 bytes (that's 896 bytes for each of the two layers in each image - see the deep dive on [displaying two-layer images](https://elite.bbcelite.com/displaying_two-layer_images.html) for details of how these images work). This is how the packed and unpacked file sizes compare:

| Image | Packed size | Unpacked size | Reduced to (%) | 
|---|---|---|---|
| [systemImage0](https://elite.bbcelite.com/nes/bank_5/variable/systemimage0.html) | 1080 | 1792 | 60.3% | 
| [systemImage1](https://elite.bbcelite.com/nes/bank_5/variable/systemimage1.html) | 1007 | 1792 | 56.2% | 
| [systemImage2](https://elite.bbcelite.com/nes/bank_5/variable/systemimage2.html) | 1473 | 1792 | 82.2% | 
| [systemImage3](https://elite.bbcelite.com/nes/bank_5/variable/systemimage3.html) | 1240 | 1792 | 69.2% | 
| [systemImage4](https://elite.bbcelite.com/nes/bank_5/variable/systemimage4.html) | 908 | 1792 | 50.7% | 
| [systemImage5](https://elite.bbcelite.com/nes/bank_5/variable/systemimage5.html) | 1060 | 1792 | 59.2% | 
| [systemImage6](https://elite.bbcelite.com/nes/bank_5/variable/systemimage6.html) | 1024 | 1792 | 57.1% | 
| [systemImage7](https://elite.bbcelite.com/nes/bank_5/variable/systemimage7.html) | 1112 | 1792 | 62.1% | 
| [systemImage8](https://elite.bbcelite.com/nes/bank_5/variable/systemimage8.html) | 809 | 1792 | 45.1% | 
| [systemImage9](https://elite.bbcelite.com/nes/bank_5/variable/systemimage9.html) | 967 | 1792 | 54.0% | 
| [systemImage10](https://elite.bbcelite.com/nes/bank_5/variable/systemimage10.html) | 1096 | 1792 | 61.2% | 
| [systemImage11](https://elite.bbcelite.com/nes/bank_5/variable/systemimage11.html) | 1042 | 1792 | 58.1% | 
| [systemImage12](https://elite.bbcelite.com/nes/bank_5/variable/systemimage12.html) | 1171 | 1792 | 65.3% | 
| [systemImage13](https://elite.bbcelite.com/nes/bank_5/variable/systemimage13.html) | 1090 | 1792 | 60.8% | 
| [systemImage14](https://elite.bbcelite.com/nes/bank_5/variable/systemimage14.html) | 964 | 1792 | 53.8% | 
| Totals | 16,043 | 26,880 | 59.7% | 

So on average, the images are being reduced to around 60% of their original size, bringing the total unpacked size of 26,880 bytes down to a more manageable 16,043 bytes. That's not too shabby.

The unpacking routine can be applied to any data. Some data is very suitable for packing and other data is less so, and a good example of this is in the view attribute variables. These 24 variables each contain 64 bytes for the view attributes, but their packing ratios vary wildly.

For example, [viewAttributes19](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes19.html) packs those 64 bytes down to 13, which is just 20.3% of the original size, but [viewAttributes18](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes18.html) only manages to pack them down to 50 bytes, which is 78.1% of the original. Looking at the unpacked data gives us a clue as to why. Here's the attribute data that packs down a lot:

AF 5F 5F 5F 5F 5F 5F 5F FB FA F5 F5 F5 F5 F5 F5 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 0F 0F 0F 0F 0F 0F 0F 0F

And here's the data that doesn't pack as well:

FF FF FF FF FF FF FF FF 73 50 50 A0 A0 60 50 50 77 00 99 AA AA 66 55 55 73 50 50 AA AA 66 55 55 77 55 99 AA AA 66 55 55 37 05 09 8A AA A6 A5 A5 F3 F0 F0 F8 FA FA FA FF FF FF FF FF FF FF FF FF

The first set of attributes contains lots of similar values, while the second contains far fewer repeats, and that gives us a big clue as to how the packing algorithm works.

It isn't all good news, though. The large logo on the Start screen, as shown above, turns out to be a terrible candidate for packing. The unpacked binary is 1664 bytes, but when it's packed and put into the game at [bigLogoImage](https://elite.bbcelite.com/nes/bank_4/variable/biglogoimage.html), it actually *increases* by 64%, with a packed size of 2736 bytes. I wonder why it wasn't simply included in its unpacked state? It's all a bit of a mystery...

## The unpacking algorithm

													 -----------------------

						The unpacking routines at [UnpackToRAM](https://elite.bbcelite.com/nes/bank_7/subroutine/unpacktoram.html) and [UnpackToPPU](https://elite.bbcelite.com/nes/bank_7/subroutine/unpacktoppu.html) both use the exact same algorithm to unpack data on the fly, with one unpacking to RAM and the other to the PPU's VRAM (via the PPU registers).

UnpackToRAM reads packed data from V(1 0) and writes unpacked data to SC(1 0) by fetching bytes one at a time from V(1 0), incrementing V(1 0) after each fetch, and unpacking and writing the data to SC(1 0) as it goes. The data is typically nametable or single-bitplane pattern data that is unpacked into the nametable or pattern buffers.

UnpackToPPU does the same thing, except it sends it straight to the PPU. The data is typically nametable or four-colour pattern data that is unpacked into the PPU's nametable or pattern tables.

The idea behind the unpacking algorithm is to work our way through the packed data one byte at a time, interpreting each byte according to the following rules:

$00 = unchanged $0x = output 0 for $0x bytes $10 = unchanged $1x = output $FF for $0x bytes $20 = unchanged $2x = output the next byte for $0x bytes $30 = unchanged $3x = output the next $0x bytes unchanged $40 and above = unchanged

So bytes like $63, $10 and $43 pass through the unpacker unchanged, but as soon as we bump into value with a special meaning, we apply the relevant rule. Here are some examples:

- If we come across $04 then we output $00 $00 $00 $00
- If we come across $13 then we output $FF $FF $FF
- If we come across $25 $1F then we output $1F $1F $1F $1F $1F
- If we come across $34 $01 $12 $23 $34 then we output $01 $12 $23 $34

You can see that the algorithm is designed to efficiently pack data with lots of repeated values, especially $00 and $FF, but if the data doesn't contain many repeats but does contain quite a few values under $40, the packed version will actually get longer. Images with large areas of the same colour are therefore excellent candidates for packing, but if we look at the big logo image, which contains its data as PPU-ready patterns, we can see why it doesn't pack well at all, as it's all over the place:

![The big logo image in NES Elite](https://elite.bbcelite.com/images/nes/unpacking/bigLogoImage_ppu.png) 

						Here's the unpacking algorithm itself, as implemented in the [UnpackToRAM](https://elite.bbcelite.com/nes/bank_7/subroutine/unpacktoram.html) routine. If we fetch byte $xx from V(1 0), then we unpack it as follows:

- If $xx >= $40, output byte $xx as it is and move on to the next byte.
- If $xx = $x0, output byte $x0 as it is and move on to the next byte.
- If $xx = $3F, stop and return from the subroutine, as we have finished.
- If $xx >= $20, jump to upac6 to do the following:
								- If $xx >= $30, jump to upac7 to output the next $0x bytes from V(1 0) as they are, incrementing V(1 0) as we go.
- If $xx >= $20, fetch the next byte from V(1 0), increment V(1 0), and output the fetched byte for $0x bytes.
 
- If $xx >= $10, jump to upac5 to output $FF for $0x bytes.
- If $xx < $10, output $00 for $0x bytes.

Let's finish off with a list of all the packed data in NES Elite.

## List of packed data

													 -------------------

						The following images and binaries are unpacked from the game binary using the above algorithm:

- [bigLogoImage](https://elite.bbcelite.com/nes/bank_4/variable/biglogoimage.html)- the big Elite logo shown on the Start screen
- [cobraImage](https://elite.bbcelite.com/nes/bank_3/variable/cobraimage.html)- the Cobra Mk III shown on the Equip Ship screen, and associated equipment images
- [dashImage](https://elite.bbcelite.com/nes/bank_3/variable/dashimage.html)- the dashboard and other pattern table 0 patterns
- [faceImage0](https://elite.bbcelite.com/nes/bank_4/variable/faceimage0.html)to- [faceImage13](https://elite.bbcelite.com/nes/bank_4/variable/faceimage13.html)- commander face images
- [glassesImage](https://elite.bbcelite.com/nes/bank_4/variable/glassesimage.html)- the glasses, earrings and medallion that the commander can wear
- [headImage0](https://elite.bbcelite.com/nes/bank_4/variable/headimage0.html)to- [headImage13](https://elite.bbcelite.com/nes/bank_4/variable/headimage13.html)- commander headshot images
- [logoBallImage](https://elite.bbcelite.com/nes/bank_3/variable/logoballimage.html)- the ball at the bottom of the big Elite logo shown on the Start screen
- [smallLogoImage](https://elite.bbcelite.com/nes/bank_3/variable/smalllogoimage.html)- the small Elite logo shown on the Save and Load screen
- [systemImage0](https://elite.bbcelite.com/nes/bank_5/variable/systemimage0.html)to- [systemImage14](https://elite.bbcelite.com/nes/bank_5/variable/systemimage14.html)- the system images
- [viewAttributes0](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes0.html)to- [viewAttributes23](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes23.html)- attribute data for the various views

All other images and data blocks (such as the icon bar images) are included in the source code without being packed.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
AF 5F 5F 5F 5F 5F 5F 5F
  FB FA F5 F5 F5 F5 F5 F5
  FF FF FF FF FF FF FF FF
  FF FF FF FF FF FF FF FF
  FF FF FF FF FF FF FF FF
  FF FF FF FF FF FF FF FF
  FF FF FF FF FF FF FF FF
  0F 0F 0F 0F 0F 0F 0F 0F
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
FF FF FF FF FF FF FF FF
  73 50 50 A0 A0 60 50 50
  77 00 99 AA AA 66 55 55
  73 50 50 AA AA 66 55 55
  77 55 99 AA AA 66 55 55
  37 05 09 8A AA A6 A5 A5
  F3 F0 F0 F8 FA FA FA FF
  FF FF FF FF FF FF FF FF
```

### Snippet Codice (BASIC)

```basic
$00 = unchanged
  $0x = output 0 for $0x bytes
  $10 = unchanged
  $1x = output $FF for $0x bytes
  $20 = unchanged
  $2x = output the next byte for $0x bytes
  $30 = unchanged
  $3x = output the next $0x bytes unchanged
  $40 and above = unchanged
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/image_and_data_compression.html](https://elite.bbcelite.com/deep_dives/image_and_data_compression.html)*
