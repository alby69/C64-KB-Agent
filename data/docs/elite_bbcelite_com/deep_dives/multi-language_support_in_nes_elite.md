---
title: Multi-language support in NES Elite
source_url: https://elite.bbcelite.com/deep_dives/multi-language_support_in_nes_elite.html
category: manual
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- BASIC ROM
- CIA
- SID
- CPU
- KERNAL
related:
- keyboard-handling
- music-player
- sound-programming
- joystick-reading
- memory-map
- kernal-routines
- sid-registers
- cia-registers
scraped_at: '2026-07-14'
---

# Multi-language support in NES Elite

## How the NES version supports English, German and French text

NES Elite was only released in one format - a PAL cartridge for the European market - and one of its most Europe-friendly features is multi-language support. The original English text is all present and correct, but you can also choose to play Elite in German or French, right from the Start screen:

![The Start screen in NES Elite](https://elite.bbcelite.com/images/nes/general/start.png) 

						This changes all the text in the game. For example, here's the Market Prices screen in English:

						![The Lave market prices screen in NES Elite](https://elite.bbcelite.com/images/nes/general/market_lave.png) 

						

And here it is in German:

![The Lave market prices screen in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/market_lave_german.png) 

						And here it is in French:

						![The Lave market prices screen in French in NES Elite](https://elite.bbcelite.com/images/nes/languages/market_lave_french.png) 

						

Interestingly, the codebase supports four languages but only three are enabled (there isn't enough room for another set of text, so presumably that's why). However, there is one place where the fourth language is populated. It's in the [cheatCmdrName](https://elite.bbcelite.com/nes/bank_6/variable/cheatcmdrname.html) variable, which contains the secret commander name that triggers cheat mode. In English, this is "CHEATER", in German it's "BETRUG", in French it's "TRICHER"... and in Italian it's "INGANNO". Alas, this is the only trace of Italian in the whole game binary, but at least we know what language four would have been had there been more free space.

(Incidentally, NES Elite was released with the manual translated into Italian, as can be seen on the excellent [Frontier Astro](https://www.frontierastro.co.uk/Elite/nes.html) site, but I haven't managed to find an actual game with Italian text in it. If anyone knows of such a thing, I would love to hear from you...)

## Text tables in multiple languages

													 ---------------------------------

						The text for all three languages is stored using the exact same tokenisation system as in the other 6502 versions of Elite. The only difference is in the obfuscation value that's used to hide the standard text tokens from prying eyes: the NES version EOR's its text tokens with a value of $3E, while the other versions use $23.

The text-tokenisation system is described in detail in the deep dives on [printing text tokens](https://elite.bbcelite.com/printing_text_tokens.html), [extended text tokens](https://elite.bbcelite.com/extended_text_tokens.html) and [extended system descriptions](https://elite.bbcelite.com/extended_system_descriptions.html). As explained in these articles, the game text is all stored in the following text-related tables:

- [QQ16](https://elite.bbcelite.com/nes/bank_2/variable/qq16.html)contains the set of two-letter tokens
- [TKN2](https://elite.bbcelite.com/nes/bank_2/variable/tkn2.html)contains the extended set of two-letter tokens
- [QQ18](https://elite.bbcelite.com/nes/bank_2/variable/qq18.html)contains the standard set of text tokens
- [TKN1](https://elite.bbcelite.com/nes/bank_2/variable/tkn1.html)contains the extended set of text tokens
- [RUTOK](https://elite.bbcelite.com/nes/bank_2/variable/rutok.html)contains the second extended set of text tokens
- [RUGAL](https://elite.bbcelite.com/nes/bank_2/variable/rugal.html)contains the criteria for extended description overrides
- [RUPLA](https://elite.bbcelite.com/nes/bank_2/variable/rupla.html)contains system numbers that have extended description overrides

These same tables are present in NES Elite, and they contain the English text as expected, but to support two extra languages, the token tables have their own separate versions for each language. The two-letter tokens are the same in all languages, but the non-English text can be found in the following tables for German:

- [QQ18_DE](https://elite.bbcelite.com/nes/bank_2/variable/qq18_de.html)contains the standard set of text tokens in
- [TKN1_DE](https://elite.bbcelite.com/nes/bank_2/variable/tkn1_de.html)contains the extended set of text tokens
- [RUTOK_DE](https://elite.bbcelite.com/nes/bank_2/variable/rutok_de.html)contains the second extended set of text tokens
- [RUGAL_DE](https://elite.bbcelite.com/nes/bank_2/variable/rugal_de.html)contains the criteria for extended description overrides
- [RUPLA_DE](https://elite.bbcelite.com/nes/bank_2/variable/rupla_de.html)contains system numbers that have extended description overrides

And the following tables for French:

- [QQ18_FR](https://elite.bbcelite.com/nes/bank_2/variable/qq18_fr.html)contains the standard set of text tokens in
- [TKN1_FR](https://elite.bbcelite.com/nes/bank_2/variable/tkn1_fr.html)contains the extended set of text tokens
- [RUTOK_FR](https://elite.bbcelite.com/nes/bank_2/variable/rutok_fr.html)contains the second extended set of text tokens
- [RUGAL_FR](https://elite.bbcelite.com/nes/bank_2/variable/rugal_fr.html)contains the criteria for extended description overrides
- [RUPLA_FR](https://elite.bbcelite.com/nes/bank_2/variable/rupla_fr.html)contains system numbers that have extended description overrides

A good comparison of the different text styles can be found in the mission briefings. Consider the first mission, where we are sent to find the stolen Constrictor (see the deep dive on [the Constrictor mission](https://elite.bbcelite.com/the_constrictor_mission.html) for details). The English and French briefings nicely fit onto two screens, like this for the English version:

						![The first briefing screen for mission 1 in NES Elite](https://elite.bbcelite.com/images/nes/missions/mission_1a.png) 

						![The second briefing screen for mission 1 in NES Elite](https://elite.bbcelite.com/images/nes/missions/mission_1b.png) 

						

And like this for French:

						![The first briefing screen for mission 1 in French in NES Elite](https://elite.bbcelite.com/images/nes/languages/mission_1a_french.png) 

						![The second briefing screen for mission 1 in French in NES Elite](https://elite.bbcelite.com/images/nes/languages/mission_1b_french.png) 

						

But the German version needs a whole extra screen, like this:

![The first briefing screen for mission 1 in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/mission_1a_german.png) 

						![The second briefing screen for mission 1 in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/mission_1b_german.png) 

						![The third briefing screen for mission 1 in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/mission_1c_german.png) 

						The [ChooseLanguage](https://elite.bbcelite.com/nes/bank_6/subroutine/chooselanguage.html) routine manages the language choice on the Start screen, and stores the number of the chosen language in [languageIndex](https://elite.bbcelite.com/nes/common/workspace/wp.html#languageindex) (which gets set to 0 for English, 1 for German and 2 for French) and [languageNumber](https://elite.bbcelite.com/nes/common/workspace/wp.html#languagenumber) (which has bit 0 set for English, bit 1 set for German and bit 2 set for French). These two variables are used throughout the codebase to fetch the correct settings needed for the chosen language.

For example, languageIndex is used as an index into the following tables, which contain the addresses of the five main text tables:

- ([tokensHi](https://elite.bbcelite.com/nes/bank_6/variable/tokenshi.html)[tokensLo](https://elite.bbcelite.com/nes/bank_6/variable/tokenslo.html)) contains the address of each language's QQ18 table
- ([extendedTokensHi](https://elite.bbcelite.com/nes/bank_6/variable/extendedtokenshi.html)[extendedTokensLo](https://elite.bbcelite.com/nes/bank_6/variable/extendedtokenslo.html)) contains the address of each language's TKN1 table
- ([rutokHi](https://elite.bbcelite.com/nes/bank_2/variable/rutokhi.html)[rutokLo](https://elite.bbcelite.com/nes/bank_2/variable/rutoklo.html)) contains the address of each language's RUTOK table
- ([rugalHi](https://elite.bbcelite.com/nes/bank_2/variable/rugalhi.html)[rugalLo](https://elite.bbcelite.com/nes/bank_2/variable/rugallo.html)) contains the address of each language's RUPLA table
- ([ruplaHi](https://elite.bbcelite.com/nes/bank_2/variable/ruplahi.html)[ruplaLo](https://elite.bbcelite.com/nes/bank_2/variable/ruplalo.html)) contains the address of each language's RUPLA table

And here's a small selection of other language-specific lookup tables that enable us to support all sorts of tweaks, depending on the chosen language:

- ([autoplayKeys1Hi](https://elite.bbcelite.com/nes/bank_5/variable/autoplaykeys1hi.html)[autoplayKeys1Lo](https://elite.bbcelite.com/nes/bank_5/variable/autoplaykeys1lo.html)) contains the address of each language's autoplayKeys table, so the combat demo's auto-play feature behaves differently depending on the chosen language
- [decimalPointLang](https://elite.bbcelite.com/nes/bank_6/variable/decimalpointlang.html)lets us set a different decimal point character for each language
- [popupWidth](https://elite.bbcelite.com/nes/bank_0/variable/popupwidth.html)controls the width of the laser view popup for each language
- ([scrollText1Hi](https://elite.bbcelite.com/nes/bank_6/variable/scrolltext1hi.html)[scrollText1Lo](https://elite.bbcelite.com/nes/bank_6/variable/scrolltext1lo.html)) contains the address of the combat demo's scroll text in each different language
- ([viewAttributesHi](https://elite.bbcelite.com/nes/bank_3/variable/viewattributeshi.html)[viewAttributesLo](https://elite.bbcelite.com/nes/bank_3/variable/viewattributeslo.html)) contains the address of each language's view attributes table, so views can have different attribute layouts (i.e. different colour layouts) in different languages
- [xStatusMode](https://elite.bbcelite.com/nes/bank_0/variable/xstatusmode.html)defines the text column for the list of equipment on the Status Mode screen for each language
- [yHeadshot](https://elite.bbcelite.com/nes/bank_0/variable/yheadshot.html)defines the text row to use for the commander image on the Status Mode screen for each language

On top of the lookup tables, the code contains a lot of bitwise checks on the bits in the languageNumber variable. Not only is the text different in each language, but the layouts need to be different too, and logic is scattered throughout the game to cater for the quirks of each language. For example, the list of equipment on the Equip Ship screen is printed in a different column in German compared to French and English, as the word length is different (it's longer in German). Here's the English layout:

![The Equip Ship screen in NES Elite](https://elite.bbcelite.com/images/nes/general/equipment.png) 

						And here it is in French:

![The Equip Ship screen in French in NES Elite](https://elite.bbcelite.com/images/nes/languages/equipment_french.png) 

						And here it is in German, where you can see each equipment name starts one column to the left, so the list can cope with longer equipment names:

![The Equip Ship screen in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/equipment_german.png) 

						This particular spacing is controlled in the [PrintEquipment](https://elite.bbcelite.com/nes/bank_0/subroutine/printequipment.html) routine, which prints extra spaces (or otherwise) depending on the chosen language. Here are some other examples:

- The [TT66](https://elite.bbcelite.com/nes/bank_0/subroutine/tt66.html#scrn10)routine checks to see if the chosen language is German by checking bit 1 of languageNumber, and if it is set, then it displays the space view name ("Front View" in English) with the words the other way around, i.e. with the view name after the view noun, so we get "Ansicht Vorn" and "Ansicht Hinten" instead of "Front View" and "Rear View". (The French equivalents are simply "Avant" and "Arrière", so no extra logic needs to be applied here.)
- The [fwl](https://elite.bbcelite.com/nes/bank_0/subroutine/fwl.html)routine checks the chosen language to decide how to display the fuel levels, as it appears in a different row and column in the French Status Mode screen when compared to the others.

Unfortunately, one of the features that had to be dropped for German and French players is the "goat soup" extended system description system, as that would need to be completely recoded to cater for the different grammatical rules of each language (see the deep dive on [extended system descriptions](https://elite.bbcelite.com/extended_system_descriptions.html) for details). As a result, instead of getting long descriptions like this in the Data on System screen:

![The Data on System view in NES Elite](https://elite.bbcelite.com/images/nes/general/data_on_diso.png) 

						We get this in German:

![The Data on System view in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/data_on_diso_german.png) 

						And this in French:

![The Data on System view in French in NES Elite](https://elite.bbcelite.com/images/nes/languages/data_on_diso_french.png) 

						This means there are no edible poets in German or French Elite. Never mind.

## Accented characters in text tokens

													 ----------------------------------

						As the BBC Micro's character set is based on ASCII, it doesn't support accented characters. As a result, accented characters in NES Elite's text tokens are implemented by mapping unused punctuation characters instead. As all the text is drawn using a custom font, this just means the font needs to contain the correct accented character at the mapped character number.

The font system is described in detail in the deep dive on [fonts in NES Elite](https://elite.bbcelite.com/fonts_in_nes_elite.html), but here's a quick summary of how to include accented characters in the text token tables. The following table shows which ASCII characters are mapped to accented characters in the font:

| ASCII code | CHAR/ECHR macro | Accented character | Font character | 
|---|---|---|---|
| 34 | CHAR '"' | À | A | 
| 35 | CHAR '#' | Ô | O | 
| 36 | CHAR '$' | à | à | 
| 37 | CHAR '%' | é | é | 
| 42 | CHAR '*' | è | è | 
| 43 | CHAR '+' | ê | ê | 
| 47 | CHAR '/' | ô | ô | 
| 59 | CHAR ';' | ß | ß | 
| 60 | CHAR '<' | É | E | 
| 61 | CHAR '=' | È | E | 
| 64 | CHAR '@' | Ç | Ç | 
| 91 | CHAR '[' | Ä | Ä | 
| 92 | CHAR '\' | Ö | Ö | 
| 93 | CHAR ']' | Ü | Ü | 
| 94 | CHAR '^' | ẞ | ẞ | 
| 95 | CHAR '_' | Ê | E | 
| 96 | CHAR '`' | ç | ç | 
| 123 | CHAR '{' | ä | ä | 
| 124 | CHAR '|' | ö | ö | 
| 125 | CHAR '}' | ü | ü | 

So, for example, to include é in a text token, we can use CHAR '%' (in standard tokens) or ECHR '%' (in extended tokens), and this will display correctly on-screen.

That said, the custom font doesn't display all the accents on capital letters. Here's the font, as loaded from the [fontImage](https://elite.bbcelite.com/nes/bank_7/variable/fontimage.html) table:

![The custom font in NES Elite](https://elite.bbcelite.com/images/nes/languages/fontImage_ram.png) 

						Taking the third and fourth characters as an example, these appear as "A" and "O" in the font, but they actually represent "À" and "Ô". The accents would be a bit of a squeeze into the 8x8-pixel character grid, so perhaps this is why they were left out, even though the game text does include the correct codes (using CHAR '"' and CHAR '#' for "À" and "Ô" respectively).

## Different screen layouts

													 ------------------------

						One of the language-dependent variables mentioned above is ([viewAttributesHi](https://elite.bbcelite.com/nes/bank_3/variable/viewattributeshi.html) [viewAttributesLo](https://elite.bbcelite.com/nes/bank_3/variable/viewattributeslo.html)), which contains the address of each language's view attributes table. Each view has an associated set of attributes that defines the colours used for each 2x2-tile block on the screen, taken from one of 24 view attribute tables (see the deep dive on [views and view types in NES Elite](https://elite.bbcelite.com/views_and_view_types_in_nes_elite.html) for more on this).

Each language has its own viewAttributes table, which maps view types to view attributes. The three tables are at [viewAttributes_EN](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes_en.html), [viewAttributes_DE](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes_de.html) and [viewAttributes_FR](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes_fr.html), and each table has a slightly different mapping.

For example, the Status Mode screen uses [viewAttributes13](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes13.html) in English, [viewAttributes14](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes14.html) in German and [viewAttributes15](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes15.html) in French. These look similar, but they differ in the colours allocated to the text - in the following images, try running your eye down the split between the red/green palette in the top-left and the white/green palette in the top-right, and you should see what I mean.

Here's the English layout, which has a very jagged boundary between the left and right palettes:

![The attributes for the Status Mode view in English in NES Elite](https://elite.bbcelite.com/images/nes/languages/status_attr_english.png) 

						Here's the German layout, which generally slopes down from left to right:

![The attributes for the Status Mode view in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/status_attr_german.png) 

						And here's the French layout, which generally slopes up from left to right, as well as dropping the greyscale box on the right down a row (this box contains the commander headshot image):

![The attributes for the Status Mode view in French in NES Elite](https://elite.bbcelite.com/images/nes/languages/status_attr_french.png) 

						These different palette layouts cater for the different text layouts in the Status Mode screen. Because the text length is so different in each language, the order in which it appears has to be changed to fit it onto the screen. To see this in action, consider the maxed-out commander, which fills the screen to capacity.

Here he is in English, with its jagged green text:

						![The maximum commander in NES Elite](https://elite.bbcelite.com/images/nes/commander/max_commander.png) 

						

Here he is in German, with the green text sloping down from left to right:

						![The maximum commander in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/max_commander_german.png) 

						

And here he is in French, with the green text sloping up from to right, and with the lower-down commander image:

![The maximum commander in French in NES Elite](https://elite.bbcelite.com/images/nes/languages/max_commander_french.png) 

						You can see in these screenshots how the layout of the screen changes depending on the language, to fit the different amounts of text. Unfortunately, in the maxed-out commander, this also breaks some of the styling, which you can see towards the left end of the cash levels in the German and French screens, where the cash encroaches into the area of green text. As there's only one attribute for each 2x2-character block, things can go wrong unless you specifically cater for all the possible layouts.

Part of the solution to this issue is the [PrintTokenAndColon](https://elite.bbcelite.com/nes/bank_0/subroutine/printtokenandcolon.html) routine. This prints a text token followed by a colon, but it prints it in colour 3, which is green in the white/green palette in the top-right attribute block on the Status Mode screen. This is used to "extend" any green-labelled text on the left into territory that has the white/green palette, while retaining the correct colour.

Unfortunately the bug with the green cash in the maxed-out commander is the other way around, so the fix would be a bit more involved (and it's made more complicated by the fact that the cash and its label are printed using control code 5, which doesn't support colour changes). Anyway, it's a minor wrinkle in a game that is impressively bug-free, and it does at least let us examine the effect of the language-dependent view attributes.

For completeness, there is also a control code that is language-dependent (see the deep dive on [printing text tokens](https://elite.bbcelite.com/printing_text_tokens.html) for more on control codes). In the BBC Micro version of Elite, CONT 9 tabs the text cursor to column 21 before printing a colon. In NES Elite the colon is printed before the tab, and the tab size depends on the language: in English and French, it tabs to column 22, and in German it tabs to column 23. This control code is used in the Status Mode screen, and you can see the impact above: the two system names and condition in the top-right corner are one column to the right in the German version compared to the English and French versions, as that's the language-specific CONT 9 in action. The relevant code is in the [PrintCtrlCode](https://elite.bbcelite.com/nes/bank_0/subroutine/printctrlcode.html#ptok3) routine, which checks the value of languageNumber and tabs accordingly.

It's just one of the many tweaks in NES Elite that enable multi-language support.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/multi-language_support_in_nes_elite.html](https://elite.bbcelite.com/deep_dives/multi-language_support_in_nes_elite.html)*
