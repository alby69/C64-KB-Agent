---
title: Quick start guide
source_url: https://elite.bbcelite.com/about_site/quick_start_guide.html
category: source-code
topics:
- basic
- assembly
difficulty: beginner
language: assembly
hardware:
- CPU
- BASIC ROM
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# Quick start guide

Welcome to the fully documented source code for the classic space game Elite on the BBC Micro, Acorn Electron, Commodore 64, Apple II and NES. Here's a quick summary of what you'll find on this site, whether you're looking to read about Elite and how it works, or you're just keen to get stuck into the code.

If you want to play the game and its various hacks, see [playing 8-bit Elite in the 21st century](https://elite.bbcelite.com/playing_elite/). If you want to explore the source code and find out how this amzing game works, read on.

## Finding out how Elite works

						                             ---------------------------

						- Read the [about this project](https://elite.bbcelite.com/about_this_project.html)page for an introduction to this site.
- Read some of the deep dive articles to discover how Elite works under the hood. The following selection is a good place to start:
- Check out the [index of all deep dive articles](https://elite.bbcelite.com/deep_dives/)to continue exploring.

## Exploring the Elite source code

						                             -------------------------------

						- See the [map of the source code](https://elite.bbcelite.com/cassette/articles/map_of_the_source_code.html)for an overview of the program structure for the BBC Micro cassette version. You can dive straight into the source code from here - just click on the routine names and away you go.
- Read the [notes on terminology used in this commentary](https://elite.bbcelite.com/terminology_used_in_this_commentary.html), as without this it might be a bit tricky to follow the comments (in particular, you should understand the terminology I use for multi-byte numbers).
- You can explore the source code in two different ways. The easiest way is with each routine shown individually, which is what you'll see if you click the links from the map of the source code. These pages are small and easy to navigate in a browser. For example, the main game code starts at routine [TT170](https://elite.bbcelite.com/cassette/main/subroutine/tt170.html), while the 3D scanner code is in[SCAN](https://elite.bbcelite.com/cassette/main/subroutine/scan.html).
- The other way is to explore the original source code file structure, as shown in the [map of the source code](https://elite.bbcelite.com/cassette/articles/map_of_the_source_code.html). The original source files are pretty big and can be a bit unwieldy, but they do show the routines in their original context. For example, the source code for the BBC Micro cassette version splits into the following files:- The [Loader](https://elite.bbcelite.com/cassette/all/loader.html), which displays the loading screen, implements the copy protection and sets things up for the main game
- The main game source, which consists of [Workspaces](https://elite.bbcelite.com/cassette/all/workspaces.html),[Text tokens](https://elite.bbcelite.com/cassette/all/text_tokens.html),[Elite A](https://elite.bbcelite.com/cassette/all/elite_a.html),[Elite B](https://elite.bbcelite.com/cassette/all/elite_b.html),[Elite C](https://elite.bbcelite.com/cassette/all/elite_c.html),[Elite D](https://elite.bbcelite.com/cassette/all/elite_d.html),[Elite E](https://elite.bbcelite.com/cassette/all/elite_e.html),[Elite F](https://elite.bbcelite.com/cassette/all/elite_f.html),[Elite G](https://elite.bbcelite.com/cassette/all/elite_g.html)and[Ship blueprints](https://elite.bbcelite.com/cassette/all/elite_ships.html)
- The [Big Code File](https://elite.bbcelite.com/cassette/all/bcfs.html), which concatenates the files produced by the above and adds a bit more copy protection
 [BBC Micro disc](https://elite.bbcelite.com/disc/articles/map_of_the_source_code.html),[6502 Second Processor](https://elite.bbcelite.com/6502sp/articles/map_of_the_source_code.html),[Commodore 64](https://elite.bbcelite.com/c64/articles/map_of_the_source_code.html),[Apple II](https://elite.bbcelite.com/apple/articles/map_of_the_source_code.html),[BBC Master](https://elite.bbcelite.com/master/articles/map_of_the_source_code.html),[NES](https://elite.bbcelite.com/nes/articles/map_of_the_source_code.html)and[Elite-A](https://elite.bbcelite.com/elite-a/articles/map_of_the_source_code.html)versions have even more source files than the BBC Micro cassette version, while the[Electron](https://elite.bbcelite.com/electron/articles/map_of_the_source_code.html)version has the same number. See the page on[building Elite from the source](https://elite.bbcelite.com/building_elite.html)for more about the original source file structure.
- The 
- You can see more information on a routine by using the "Show more" link. Amongst other things, this is where you can switch between the two ways of looking at the code. For example, here is [TT170 shown on its own page](https://elite.bbcelite.com/cassette/main/subroutine/tt170.html), and here's[the same routine in context](https://elite.bbcelite.com/cassette/all/elite_f.html#header-tt170)as part of the Elite F source file.
- When viewing the source code, you can click on variable and routine names to see more information in a popup. The source code also has syntax highlighting.
- If you're interested in comparing the code for the different versions of Elite, you can find out how to do this in the section on [how to compare the Acornsoft versions of Elite](https://elite.bbcelite.com/compare/how_to_compare.html).
- Important routines are flagged with a "*" in the site menu.
- The entry point for the main game code is routine [TT170](https://elite.bbcelite.com/cassette/main/subroutine/tt170.html). If you want to follow the program flow all the way from the title screen around the main game loop, then there's a deep dive on[program flow of the main game loop](https://elite.bbcelite.com/deep_dives/program_flow_of_the_main_game_loop.html)that has you covered.

## Finding your way around

						                             -----------------------

						- There is a whole section of the site dedicated to indexes and analyses, to help you find what you are looking for. Look in the site menu for the "Indexes to the source code" section for details.
- There are loads of subroutines in Elite - literally hundreds. You can find them all listed and linked in the indexes for each individual version; for example, the BBC Micro cassette version has indexes of [subroutines](https://elite.bbcelite.com/cassette/indexes/subroutines.html),[variables](https://elite.bbcelite.com/cassette/indexes/variables.html),[workspaces](https://elite.bbcelite.com/cassette/indexes/workspaces.html)and[macros](https://elite.bbcelite.com/cassette/indexes/macros.html).
- Each version also has an [A-Z index of the whole source](https://elite.bbcelite.com/cassette/indexes/a-z.html), which lists every single label across all the source files, as well as[source code statistics](https://elite.bbcelite.com/cassette/articles/source_code_statistics.html), and an index of[cross-references](https://elite.bbcelite.com/cassette/articles/source_code_cross-references.html)to help you find what you're looking for.
- The above links are for the BBC Micro cassette version, which is probably the best place to start. For the more adventurous, the site menu contains indexes to the more complex [BBC Micro disc](https://elite.bbcelite.com/disc/indexes/a-z.html),[6502 Second Processor](https://elite.bbcelite.com/6502sp/indexes/a-z.html),[Commodore 64](https://elite.bbcelite.com/c64/indexes/a-z.html),[Apple II](https://elite.bbcelite.com/apple/indexes/a-z.html),[BBC Master](https://elite.bbcelite.com/master/indexes/a-z.html),[NES](https://elite.bbcelite.com/nes/indexes/a-z.html)and[Elite-A](https://elite.bbcelite.com/elite-a/indexes/a-z.html)versions, as well as the simpler[Electron](https://elite.bbcelite.com/electron/indexes/a-z.html)version.
- There is also a complete index of the entire codebase, showing which parts of the code are used in which versions. This comes in three parts: [shared code with variations](https://elite.bbcelite.com/compare/indexes/shared_code_with_variations.html),[shared code without variations](https://elite.bbcelite.com/compare/indexes/shared_code_no_variations.html)and[version-specific code](https://elite.bbcelite.com/compare/indexes/version_specific_code.html).
- The index section also contains statistics for each of the versions. For example, here are the [statistics for the BBC Micro cassette version](https://elite.bbcelite.com/cassette/articles/source_code_statistics.html). Statistics for the other versions can be found in the same section.

## Other helpful hints

						                             -------------------

						- If you want to build the source on a modern computer, then check out the page on [building Elite from the source](https://elite.bbcelite.com/building_elite.html).
- The source code is designed to be read at an 80-column width and with a monospaced font, just like in the good old days. If you're viewing this on a phone, you may find it easier to view the source code pages in landscape.
- You can change the site's colour scheme by clicking the theme icons in the top-right corner. The dark themes are inspired by the colour schemes used in the [BBC Micro Model B and 6502 Second Processor versions](https://elite.bbcelite.com/compare/versions_of_elite.html)of the game, but with a modern, IDE-like twist.

I hope you enjoy exploring the inner workings of Elite as much as I have.

---
*Fonte originale: [https://elite.bbcelite.com/about_site/quick_start_guide.html](https://elite.bbcelite.com/about_site/quick_start_guide.html)*
