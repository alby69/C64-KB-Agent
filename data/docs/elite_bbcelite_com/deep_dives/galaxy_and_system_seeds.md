---
title: Galaxy and system seeds
source_url: https://elite.bbcelite.com/deep_dives/galaxy_and_system_seeds.html
category: deep-dive
topics:
- memory management
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
- BASIC ROM
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# Galaxy and system seeds

## How system data is extracted from the galaxy and system seeds

Famously, Elite's galaxy and system data is generated procedurally, using a set of three 16-bit seed numbers and the Tribonnaci series to generate entire galaxies of systems like this:

![The Long-range Chart in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/long-range_chart.png) 

						Each of these systems has its own set of seeds, which can be calculated using a simple process called "twisting". For details of this process and how it can be used to generate 2048 different sets of seeds for the 256 systems in each of the game's eight galaxies, see the deep dive on [twisting the system seeds](https://elite.bbcelite.com/twisting_the_system_seeds.html).

Each set of seeds contains all the data for one specific system. In this article we'll take an overview of everything that's captured in the seeds, and for more detailed analysis you can read the deep dives on [generating system data](https://elite.bbcelite.com/generating_system_data.html), [generating system names](https://elite.bbcelite.com/generating_system_names.html) and [market item prices and availability](https://elite.bbcelite.com/market_item_prices_and_availability.html).

## Structure of the system seeds

													 -----------------------------

						The seeds are stored in two places: [QQ15](https://elite.bbcelite.com/cassette/main/workspace/zp.html#qq15) contains the seeds for the currently selected system in the system chart, and [QQ21](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq21) contains the seeds for system 0 in the current galaxy.

Seeds for each system in the galaxy can be generated from the seeds for system 0 in QQ21 by repeatedly twisting the seeds for system 0 - see the deep dive on [twisting the system seeds](https://elite.bbcelite.com/twisting_the_system_seeds.html) for details.

The seeds are stored as three little-endian 16-bit numbers, so the low (least significant) byte is first followed by the high (most significant) byte, in the same way that the 6502 stores 16-bit addresses. That means if the seeds are s0, s1 and s2, they are stored like this:

| Seed | Low byte | High byte | 
|---|---|---|
| s0 | QQ15 | QQ15+1 | 
| s1 | QQ15+2 | QQ15+3 | 
| s2 | QQ15+4 | QQ15+5 | 

Throughout this documentation, we denote the low byte of s0 as s0_lo and the high byte as s0_hi, and so on for s1_lo, s1_hi, s2_lo and s2_hi.

Given a set of seeds for a specific system, we can extract all the system data from those seeds. Here's a summary of which bits in which seeds are used to generate the various bits of data in the universe. The routine names where these data are generated are shown on the right.

```
   s0_hi    s0_lo    s1_hi    s1_lo    s2_hi    s2_lo
76543210 76543210 76543210 76543210 76543210 76543210
                                             ^------- Species is human    
```
[TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                                       ^^^----------- Species adjective 1 [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                                    ^^^-------------- Species adjective 2 [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
      ^^----------------^^--------------------------- Species adjective 3 [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                                          ^^--------- Species type        [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                  ^^^^^^^^--------------^^^^--------- Average radius      [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                             ^^^--------------------- Government type     [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
     ^^^--------------------------------------------- Prosperity level    [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
     ^----------------------------------------------- Economy type        [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
                        ^^--------------------------- Tech level          [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
                  ^^^^^^^^--------------------------- Galactic x-coord    [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
^^^^^^^^--------------------------------------------- Galactic y-coord    [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
                                               ^-^^^^ Long-range dot size [TT22](https://elite.bbcelite.com/cassette/main/subroutine/tt22.html)
                                                    ^ Short-range size    [TT23](https://elite.bbcelite.com/cassette/main/subroutine/tt23.html)
          ^------------------------------------------ Name length          [cpl](https://elite.bbcelite.com/cassette/main/subroutine/cpl.html)
                                       ^^^^^--------- Name token (x4)      [cpl](https://elite.bbcelite.com/cassette/main/subroutine/cpl.html)
     ^^^--------------------------------------------- Planet distance    [SOLAR](https://elite.bbcelite.com/cassette/main/subroutine/solar.html)
                       ^^^--------------------------- Sun distance       [SOLAR](https://elite.bbcelite.com/cassette/main/subroutine/solar.html)
                                          ^^--------- Sun x-y offset     [SOLAR](https://elite.bbcelite.com/cassette/main/subroutine/solar.html)
76543210 76543210 76543210 76543210 76543210 76543210
   s0_hi    s0_lo    s1_hi    s1_lo    s2_hi    s2_lo
						## An example

													 ----------

						Let's take a look at how this works with the starting system of Lave, which has a Data on System screen like this:

![The Data on System screen for Lave in the BBC Micro disc version of Elite](https://elite.bbcelite.com/images/disc/data_on_lave.png) 

						at this location on the Long-range Chart (where it's shown as a two-pixel dash):

![The Long-range Chart in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/long-range_chart.png) 

						and this appearance on the Short-range Chart (where it's shown as a medium star):

![The Short-range Chart in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/short-range_chart.png) 

						Lave's seeds are as follows:

```
   s0_hi    s0_lo    s1_hi    s1_lo    s2_hi    s2_lo
10101101 00111000 00010100 10011100 00010101 00011101
                                             ^------- Species is human    
```
[TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                                       ^^^----------- Species adjective 1 [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                                    ^^^-------------- Species adjective 2 [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
      ^^----------------^^--------------------------- Species adjective 3 [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                                          ^^--------- Species type        [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                  ^^^^^^^^--------------^^^^--------- Average radius      [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html)
                             ^^^--------------------- Government type     [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
     ^^^--------------------------------------------- Prosperity level    [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
     ^----------------------------------------------- Economy type        [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
                        ^^--------------------------- Tech level          [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
                  ^^^^^^^^--------------------------- Galactic x-coord    [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
^^^^^^^^--------------------------------------------- Galactic y-coord    [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html)
                                               ^-^^^^ Long-range dot size [TT22](https://elite.bbcelite.com/cassette/main/subroutine/tt22.html)
                                                    ^ Short-range size    [TT23](https://elite.bbcelite.com/cassette/main/subroutine/tt23.html)
          ^------------------------------------------ Name length          [cpl](https://elite.bbcelite.com/cassette/main/subroutine/cpl.html)
                                       ^^^^^--------- Name token (x4)      [cpl](https://elite.bbcelite.com/cassette/main/subroutine/cpl.html)
     ^^^--------------------------------------------- Planet distance    [SOLAR](https://elite.bbcelite.com/cassette/main/subroutine/solar.html)
                       ^^^--------------------------- Sun distance       [SOLAR](https://elite.bbcelite.com/cassette/main/subroutine/solar.html)
                                          ^^--------- Sun x-y offset     [SOLAR](https://elite.bbcelite.com/cassette/main/subroutine/solar.html)
10101101 00111000 00010100 10011100 00010101 00011101
   s0_hi    s0_lo    s1_hi    s1_lo    s2_hi    s2_lo
						We interpret these seeds as follows:

| Data | Seed bits | Result | 
|---|---|---|
| Species is human | %0 | Human Colonials | 
| Average radius | %00010100 %0101 | (%0101 + 11) * 256 + %00010100 = 4116 Shown as 4116 km | 
| Government type | %011 | Dictatorship | 
| Prosperity level | %101 | Rich | 
| Economy type | %1 | Agricultural | 
| Tech level | %00 | ~%101 + %00 + ceiling(%011 / 2) = 4 Shown as Tech level 5 | 
| Population | - | 4 * 4 + %101 + %011 + 1 = 25 Shown as 2.5 billion | 
| Productivity | - | (~%101 + 3) * (%011 + 4) * 25 * 8 = 7000 Shown as 7000 M CR | 
| Galactic x-coord | %00010100 | 20 | 
| Galactic y-coord | %10101101 | 173 >> 1 = 86 | 
| Long-range dot size | %x0x11101 | %x0x11101 OR %01010000 = %01011101 = 93 Shown as a single-height two-pixel dot | 
| Short-range size | %1 | %1 + 2 + no carry from cpl = 3 Shown as a medium-sized star | 
| Name length | %0 | Generate three pairs of letters for name | 
| Name token (x4) | %10101 %10110 %00000 %01100 | 128 + %10101 = 149 ("LA") 128 + %10110 = 150 ("VE") %00000 = 0 = skip Ignore fourth pair | 
| Planet distance | %101 | (%101 + 6 + bit 0 of FIST) >> 1 = %1011 >> 1 if bit 0 of FIST was 0 so planet spawns at: x = -(2 0 0) y = -(2 0 0) z = (5 0 0) = %1100 >> 1 if bit 0 of FIST was 1 so planet spawns at: x = (3 0 0) y = (3 0 0) z = (6 0 0) | 
| Sun distance | %100 | %101 OR %10000001 = %10000101 = -5 so sun spawns at: z = -(5 0 0) | 
| Sun x-y offset | %01 | So sun spawns at: x = (1 0 0) y = (1 0 0) |

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
s0_hi    s0_lo    s1_hi    s1_lo    s2_hi    s2_lo
76543210 76543210 76543210 76543210 76543210 76543210

                                             ^------- Species is human    TT25
                                       ^^^----------- Species adjective 1 TT25
                                    ^^^-------------- Species adjective 2 TT25
      ^^----------------^^--------------------------- Species adjective 3 TT25
                                          ^^--------- Species type        TT25
                  ^^^^^^^^--------------^^^^--------- Average radius      TT25
                             ^^^--------------------- Government type     TT24
     ^^^--------------------------------------------- Prosperity level    TT24
     ^----------------------------------------------- Economy type        TT24
                        ^^--------------------------- Tech level          TT24
                  ^^^^^^^^--------------------------- Galactic x-coord    TT24
^^^^^^^^--------------------------------------------- Galactic y-coord    TT24
                                               ^-^^^^ Long-range dot size TT22
                                                    ^ Short-range size    TT23
          ^------------------------------------------ Name length          cpl
                                       ^^^^^--------- Name token (x4)      cpl
     ^^^--------------------------------------------- Planet distance    SOLAR
                       ^^^--------------------------- Sun distance       SOLAR
                                          ^^--------- Sun x-y offset     SOLAR

76543210 76543210 76543210 76543210 76543210 76543210
   s0_hi    s0_lo    s1_hi    s1_lo    s2_hi    s2_lo
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
s0_hi    s0_lo    s1_hi    s1_lo    s2_hi    s2_lo
10101101 00111000 00010100 10011100 00010101 00011101

                                             ^------- Species is human    TT25
                                       ^^^----------- Species adjective 1 TT25
                                    ^^^-------------- Species adjective 2 TT25
      ^^----------------^^--------------------------- Species adjective 3 TT25
                                          ^^--------- Species type        TT25
                  ^^^^^^^^--------------^^^^--------- Average radius      TT25
                             ^^^--------------------- Government type     TT24
     ^^^--------------------------------------------- Prosperity level    TT24
     ^----------------------------------------------- Economy type        TT24
                        ^^--------------------------- Tech level          TT24
                  ^^^^^^^^--------------------------- Galactic x-coord    TT24
^^^^^^^^--------------------------------------------- Galactic y-coord    TT24
                                               ^-^^^^ Long-range dot size TT22
                                                    ^ Short-range size    TT23
          ^------------------------------------------ Name length          cpl
                                       ^^^^^--------- Name token (x4)      cpl
     ^^^--------------------------------------------- Planet distance    SOLAR
                       ^^^--------------------------- Sun distance       SOLAR
                                          ^^--------- Sun x-y offset     SOLAR

10101101 00111000 00010100 10011100 00010101 00011101
   s0_hi    s0_lo    s1_hi    s1_lo    s2_hi    s2_lo
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/galaxy_and_system_seeds.html](https://elite.bbcelite.com/deep_dives/galaxy_and_system_seeds.html)*
