---
title: The Encyclopedia Galactica
source_url: https://elite.bbcelite.com/deep_dives/elite-a_the_encyclopedia_galactica.html
category: manual
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
- BASIC ROM
related:
- sid-registers
- sound-programming
- memory-map
- kernal-routines
- music-player
scraped_at: '2026-07-20'
---

# The Encyclopedia Galactica

## Inside the encyclopedia, Elite-A's most recognisable modification

Most of the screenshots you see of Elite-A show the Encyclopedia Galactica in action. They typically show one of the ship entries, with a 3D wireframe rotating in the midst of a bewildering crowd of information. I suspect this is because it's the most photogenic of Elite-A's unique feature, and there is no doubt that it's a clear enhancement over the original Elite. It certainly looks good to this commander, anyway:

![The Elite-A Encyclopedia Galactica entry for the Iguana](https://elite.bbcelite.com/images/elite-a/encyclopedia_iguana.png) 

						After all, the original Acornsoft Elite is famous for being bundled with an astonishing amount of documentation, all of it densely packed with galactic information and lore. The 64-page Space Trader's Flight Training Manual is a work of art that really builds the excitement of starting a career as a space commander, fresh out of pilot school and about to take charge of your very own Cobra Mk III. As if this wasn't enough, the accompanying novel by Robert Holdstock, The Dark Wheel, fleshes out the game universe's atmosphere in a way that blew people's minds back in the day. It is still an excellent read.

Perhaps not surprisingly, given the constraints of the BBC Micro, the amount of blurb in the game itself is comparatively limited, though the procedural generation of [system names](https://elite.bbcelite.com/generating_system_names.html) and [system data](https://elite.bbcelite.com/generating_system_data.html) certainly helps to bring the galaxy to life, along with the [extended system descriptions](https://elite.bbcelite.com/extended_system_descriptions.html) and mission briefings of the enhanced versions.

## The Elite-A Encyclopedia

													 ------------------------

						In Elite-A, Angus Duggan tackled this imbalance head-on with the Encyclopedia Galactica, which you can bring up by pressing CTRL-f6 when docked. This loads a brand new game code file that's broadly based on the docked code, but with all the non-encyclopedia code stripped out and replaced by the new data and menu systems used by the encyclopedia.

The encyclopedia itself is a menu-based tome that contains information on almost all of the ships in the game, along with details of controls and equipment. The latter screens are fairly text-heavy and do the job in a fairly perfunctory way, but the ship entries are things of beauty. Each ship is shown on an information card, with the main statistics arranged around the edge of the card, while the 3D wireframe of the ship in question zooms in from the centre of the card and rotates away until you dismiss the screen. For those of us who only ever got glimpses of the rarer ships when playing the game, the encyclopedia is a real thrill.

That said, the encyclopedia doesn't contain all of the different ships in Elite-A. The following don't have entries: Constrictor, Dragon, Rattler and Shuttle Mk II. There are also no entries for the non-ship objects: missile, asteroid, boulder, splinter, cargo canister and alloy plate. The game has to keep some of its secrets, after all.

Let's take a closer look at how Angus built the encyclopedia's menus and ship card system, starting with some details of the text token system.

## Text tokens in the encyclopedia

													 -------------------------------

						The extra text for the menus and ship cards are stored in a new table, [msg_3](https://elite.bbcelite.com/elite-a/encyclopedia/variable/msg_3.html), whose tokens can be printed using the [write_msg3](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/write_msg3.html) routine. This is a standard extension of the original version's [extended text token system](https://elite.bbcelite.com/extended_text_tokens.html), in exactly the same way that [RUTOK](https://elite.bbcelite.com/elite-a/docked/variable/rutok.html) and [DETOK3](https://elite.bbcelite.com/elite-a/docked/subroutine/detok3.html) extend [TKN1](https://elite.bbcelite.com/elite-a/docked/variable/tkn1.html) and [DETOK](https://elite.bbcelite.com/elite-a/docked/subroutine/detok.html) in the original version.

It's worth noting that although the encyclopedia's text token system is pretty much the same as in the rest of the game, some of the jump tokens are different. You can see the differences by looking at the modifications made to the [encyclopedia's JMTB table](https://elite.bbcelite.com/elite-a/encyclopedia/variable/jmtb.html), where (for example) token 22 is now a tab to column 16, rather than the pause token from the docked version.

## The menu system

													 ---------------

						We can show a top-level menu by calling the [menu](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/menu.html) routine with a menu number as its argument. There are five top-level menus, each with a unique number, as follows:

- Encyclopedia Galactica (the main menu)
- Ships A-G
- Ships I-W
- Controls
- Equipment

The routine returns the number of the choice that's made. The details for each of these menus are stored in five tables:

- The [menu_entry](https://elite.bbcelite.com/elite-a/encyclopedia/variable/menu_entry.html)table contains the menu's size (i.e. the number of entries)
- The [menu_offset](https://elite.bbcelite.com/elite-a/encyclopedia/variable/menu_offset.html)table contains the token number of the menu's first item
- The [menu_query](https://elite.bbcelite.com/elite-a/encyclopedia/variable/menu_query.html)table contains the menu's query token, which is the token for the query prompt at the bottom of the menu
- The [menu_title](https://elite.bbcelite.com/elite-a/encyclopedia/variable/menu_title.html)table contains the menu's title token number
- The [menu_titlex](https://elite.bbcelite.com/elite-a/encyclopedia/variable/menu_titlex.html)table contains the menu's title x-coordinate

Given the above, the following routines display and process the various menus:

- The top-level Encyclopedia Galactica menu is displayed and processed by the [info_menu](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/info_menu.html)routine
- The Ships A-G and Ships I-W menus are displayed and processed by the [ships_ag](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/ships_ag.html)routine
- The Controls menu is displayed and processed by the [controls](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/controls.html)routine
- The Equipment menu is displayed and processed by the [equip_data](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/equip_data.html)routine

The Controls and Equipment pages are stored as text tokens in [msg_3](https://elite.bbcelite.com/elite-a/encyclopedia/variable/msg_3.html), with each page of text stored in one token, so those routines are fairly straightforward and just print the corresponding token for the chosen entry.

The [ships_ag](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/ships_ag.html) routine, meanwhile, is responsible for displaying ship cards, which are a lot more complicated, so let's take a look at that next.

## The ship cards

													 --------------

						When a ship is chosen from the Ships A-G or Ships I-W menu, [ships_ag](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/ships_ag.html) processes the response. The first task is to load the relevant ship blueprints file for the chosen ship, so we can display the 3D wireframe in the middle of the ship card - though note that the contents of the blueprint file has no effect on the ship statistics shown on the card, which are hard-coded as text tokens in the encyclopedia code rather than being extracted from the blueprint itself. If the correct file is already loaded then we are done, otherwise the name of the relevant ship blueprints file is fetched from the [ship_file](https://elite.bbcelite.com/elite-a/encyclopedia/variable/ship_file.html) table, and the file is loaded from disc.

Once the correct blueprints are loaded, we print the ship's name as the card's title, using the [ship_centre](https://elite.bbcelite.com/elite-a/encyclopedia/variable/ship_centre.html) table to make sure the title is nicely centred. The ship names themselves come from tokens 7 to 34 in the [msg_3](https://elite.bbcelite.com/elite-a/encyclopedia/variable/msg_3.html) table.

Next, we print the ship's statistics around the edges of the card by calling the [write_card](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/write_card.html) routine. This uses a pretty sophisticated pattern system to display all the statistics in the correct places. Each card uses the same layout, which is defined in the [card_pattern](https://elite.bbcelite.com/elite-a/encyclopedia/variable/card_pattern.html) table, but none of the cards show every piece of information - that's determined by the data for the individual ship type (see the next section for more on this).

Each ship card in the encyclopedia consists of multiple sections, each of which consists of one or more text labels, plus the corresponding ship data. The card pattern table defines these sections and how they are laid out on screen - in other words, this table contains a set of patterns, one for each section, that define how to lay out that section on-screen.

Each line in the [card_pattern](https://elite.bbcelite.com/elite-a/encyclopedia/variable/card_pattern.html) table defines a screen position and something to print there. The first two numbers are the text column and row, and the third number specifies a text token from the msg_3 table (when non-zero) or the actual data (when zero).
						

So, for example, the "cargo space" section looks like this:

EQUB 1, 12, 61 EQUB 1, 13, 45 EQUB 1, 14, 0

which defines the following layout pattern:

- Token 61 ("CARGO") at column 1, row 12
- Token 45 ("SPACE:") at column 1, row 13
- The relevant ship data (the ship's cargo capacity) at column 1, row 14

The data itself comes from the card data for the specific ship. Each section in the card_data table corresponds to a numbered section in the card data, so the cargo space section is number 7, for example (see the next section for a list of section numbers and more on the ship data).

Once the ship card has been displayed by the write_card routine, we return to the ships_ag routine to display the 3D wireframe of the ship in the middle of the card. More specifically, we display the wireframe whose 3D data is in the blueprint position given in the [ship_posn](https://elite.bbcelite.com/elite-a/encyclopedia/variable/ship_posn.html) table, starting the ship at a fair distance and zooming it in until it reaches the distance given in the [ship_dist](https://elite.bbcelite.com/elite-a/encyclopedia/variable/ship_dist.html) table.

At this point the ship card is fully displayed, and we wait for a key press before returning to the menu.

## The card data

													 -------------

						For the statistics shown on each ship card, there's a lookup table at [card_addr](https://elite.bbcelite.com/elite-a/encyclopedia/variable/card_addr.html) that links to the relevant ship card data. There are cards for 28 different ship designs, from [adder](https://elite.bbcelite.com/elite-a/encyclopedia/variable/adder.html) all the way through to [worm](https://elite.bbcelite.com/elite-a/encyclopedia/variable/worm.html).

Each ship has its own hand-crafted set of data, which contains all the relevant statistics for that ship. Each statistic is encoded with the type of data as the first byte, as follows:

- Inservice date
- Combat factor
- Dimensions
- Speed
- Crew
- Range
- Cargo space
- Armaments
- Hull
- Drive motors
- Space

This is then followed by the statistic to show after the relevant label on the ship card (the label itself is defined in the card pattern, as described above). The ship card data is encoded using the normal recursive text system, but with a couple of differences. First, the text is not obfuscated in any way (so text can be entered in the table using the standard EQUS operative), and second, the range of token values is subtly different to those in the normal [extended token tables](https://elite.bbcelite.com/extended_text_tokens.html), as follows:

| Character | Macro | Process | 
|---|---|---|
| 1-31 | [EJMP](https://elite.bbcelite.com/elite-a/encyclopedia/macro/ejmp.html) | Call the corresponding [JMTB](https://elite.bbcelite.com/elite-a/encyclopedia/variable/jmtb.html)routine | 
| 32-127 | EQUS | Print numbers and punctuation with [TT27](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/tt27.html) | 
| 128-214 | [CTOK](https://elite.bbcelite.com/elite-a/encyclopedia/macro/ctok.html) | Print an extended recursive token with [write_msg3](https://elite.bbcelite.com/elite-a/encyclopedia/subroutine/write_msg3.html)(subtract 128 to get 0-86) | 
| 215-255 | [ETWO](https://elite.bbcelite.com/elite-a/encyclopedia/macro/etwo.html) | Print an extended two-letter token from table [TKN2](https://elite.bbcelite.com/elite-a/encyclopedia/variable/tkn2.html)/[QQ16](https://elite.bbcelite.com/elite-a/encyclopedia/variable/qq16.html)(subtract 215 to get 0-40) | 

The [CTOK](https://elite.bbcelite.com/elite-a/encyclopedia/macro/ctok.html) macro is unique to the ship card data encoding, and as mentioned above, the [encyclopedia's JMTB table](https://elite.bbcelite.com/elite-a/encyclopedia/variable/jmtb.html) is subtly different to the [version in the docked code](https://elite.bbcelite.com/elite-a/docked/variable/jmtb.html), but at least the ETWO macro is the same as always.

And that's how the Encyclopedia Galactica works.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
EQUB  1, 12, 61
   EQUB  1, 13, 45
   EQUB  1, 14,  0
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/elite-a_the_encyclopedia_galactica.html](https://elite.bbcelite.com/deep_dives/elite-a_the_encyclopedia_galactica.html)*
