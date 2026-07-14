---
title: Extended text tokens
source_url: https://elite.bbcelite.com/deep_dives/extended_text_tokens.html
category: source-code
topics:
- basic
- assembly
difficulty: beginner
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

# Extended text tokens

## The extended text token system in the enhanced versions of Elite

All versions of Elite use a clever text tokenisation system to store the game's text in an efficient manner - you can read all about it in the deep dive on [printing text tokens](https://elite.bbcelite.com/printing_text_tokens.html). In addition to this system, the enhanced disc and 6502 Second Processor versions of Elite have two additional extended text token systems that provide a lot more text, supporting missions, disc access menus, extended system descriptions and more.

For example, here's the second briefing screen for [the Constrictor mission](https://elite.bbcelite.com/the_constrictor_mission.html), which uses token 10 from the extended token table at [TKN1](https://elite.bbcelite.com/6502sp/main/variable/tkn1.html):

![The second briefing screen for the Constrictor mission in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_1b.png) 

						The two extended text token systems are as follows:

- There are 256 recursive tokens in the [TKN1](https://elite.bbcelite.com/6502sp/main/variable/tkn1.html)table that can be printed with the[DETOK](https://elite.bbcelite.com/6502sp/main/subroutine/detok.html)routine. This is the bulk of the extended token system, and contains any game text that isn't already covered by the standard text tokens or the special extended descriptions in RUTOK.
- There are 27 special extended system descriptions in the [RUTOK](https://elite.bbcelite.com/6502sp/main/variable/rutok.html)table that can be printed with the[DETOK3](https://elite.bbcelite.com/6502sp/main/subroutine/detok3.html)routine. These override the procedurally generated descriptions for a small group of systems, typically during the two missions when they are used to guide the player towards their mission briefings and goals (though there are some non-mission descriptions in there that provide some interesting Easter eggs for the player to find).

To print an extended token, we simply put the token number into the accumulator and call either DETOK or DETOK3. It's a lot simpler than the encoding system we have to use with TT27 for the standard tokens, though under the hood, the extended token system is just as complicated...

## Types of extended token

													 -----------------------

						Just like the standard text tokens, the tokens in the TKN1 and RUTOK tables are themselves composed of different types of token, though this complexity is hidden inside the routine that does the actual printing. This routine is known by two names, which are aliases of each other: [TT26](https://elite.bbcelite.com/6502sp/main/subroutine/tt26.html), which shares its name with the character printing routine in the BBC Micro cassette version, and DASC, which points to exactly the same routine. We'll talk about DASC here, as it's a slightly friendlier name.

Like the standard token system, with its control codes, two-letter tokens and recursive tokens, there are quite a few different types of extended token that DASC prints. They are:

- Jump tokens: Instead of printing, these tokens call the corresponding routine from the jump table at [JMTB](https://elite.bbcelite.com/6502sp/main/variable/jmtb.html). These can do anything from setting the letter case to rotating ships on screen while waiting for key presses.
- Characters: These are standard ASCII characters, with the case determined by the extended token flags.
- Random tokens: These are used to display the procedurally generated extended system descriptions, which use the random number generator to generate random sequences of tokens. This randomness can be controlled by seeding the random number generator before printing, which is how we ensure each system always has the same description.
- Extended recursive tokens: These work in the same way as the recursive tokens from the standard text token system, allowing us to include tokens within tokens.
- Extended two-letter tokens: These work in the same way as the two-letter tokens in the standard text token system, but with a larger range of two-letter sequences that extends the standard set, at the expense of dropping four of the original tokens.

As with the standard token system, the type of token is determined by the character code that is stored in memory. So, in the same way that control codes in standard text tokens are in the range 0-13, jump tokens in the extended text tokens are in the range 1-31, and random tokens are in the range 91-128. Here's a breakdown of the code ranges:

| Character | Macro | Process | 
|---|---|---|
| 1-31 | EJMP | Call the corresponding JMTB routine | 
| 32-64 | ECHR | Print numbers and punctuation with TT27 | 
| 65-90 | ECHR | Print letters A-Z in the correct case with DASC | 
| 91-128 | ERND | Print an extended recursive token with DETOK, fetching the token number from the MTIN table (subtract 91 to get 0-37 then add random 0-4) | 
| 129-214 | ETOK | Print an extended recursive token with DETOK | 
| 215-255 | ETWO | Print an extended two-letter token from table TKN2 (subtract 215 to get 0-40) | 

As with the standard text tokens, let's make things easier to follow by referring to the four token types like this, where n is the character code:

| Syntax | Meaning | Range | 
|---|---|---|
| {n} | Jump token | n = 1 to 31 | 
| [n?] | Random token | n = 91 to 128 | 
| [n] | Recursive token | n = 129 to 215 | 
| <n> | Two-letter token | n = 215 to 255 | 

Also like the standard text tokens, the extended text tokens are stored in memory in an obfuscated manner, though this time they are EOR'd with the value of the VE configuration variable (&57) rather than the EOR 35 that is used to hide the standard tokens. To make the source code easier to read, we use various macros to assemble the tokens into memory while retaining some level of human readability of the source code. For extended tokens, the names all start with an "E", and they are:

| Macro | Action | Range | 
|---|---|---|
| [ECHR n](https://elite.bbcelite.com/disc/docked/macro/echr.html) | Insert ASCII character n | n = 32 to 99 | 
| [EJMP n](https://elite.bbcelite.com/disc/docked/macro/ejmp.html) | Insert jump token n | n = 1 to 31 | 
| [ERND n](https://elite.bbcelite.com/disc/docked/macro/ernd.html) | Insert random token n | n = 91 to 128 | 
| [ETOK n](https://elite.bbcelite.com/disc/docked/macro/etok.html) | Insert recursive token n | n = 129 to 215 | 
| [ETWO 'x', 'x'](https://elite.bbcelite.com/disc/docked/macro/etwo.html) | Insert two-letter token "xy" | "xy" is in the table below | 

Let's look at each of these types in turn, but before we do, it's worth noting that as part of the extended token system, it's possible to switch from extended tokens back to standard text tokens, and then back again, all within one extended token (we do this using jump tokens 5 and 6). When standard tokens are enabled, the DASC routing does the following instead:

| Character | Macro | Implementation | 
|---|---|---|
| 1-31 | EJMP | Call the corresponding JMTB routine | 
| 32-255 | RTOK | Print a standard text token with TT27 | 

This behaviour is controlled by bit 7 of the print flag in DTW3: if it is clear then extended tokens are enabled, and if it set then standard tokens are enabled.

Let's now take a look at the various types of token that make up the extended text token system.

## Extended recursive tokens: [n]

													 ------------------------------

						Extended recursive tokens work in the same way as standard recursive tokens, in that tokens can contain other tokens. However, the range of extended tokens that can be included in other tokens is a bit smaller than in the standard system, where you can include all but three tokens recursively. There are 256 extended tokens in the TKN1 table that the DETOK routine can print, but only tokens in the range 129 to 215 can be included in other tokens.

Apart from this, recursive tokens expand in the same way as in the standard system, and tokens can contain tokens that contain other tokens, recursing as deep as you like.

## Extended two-letter tokens: <n>

													 -------------------------------

						Also similar to the standard token system, the extended two-letter token system is based on the range of standard two-letter tokens from the table at [QQ16](https://elite.bbcelite.com/cassette/main/variable/qq16.html), but with an additional set of tokens, and four of the original tokens dropped. The full range of extended two-letter tokens is as follows:

| Token number | Two-letter token | 
|---|---|
| 215 | {crlf} | 
| 216 | AB | 
| 217 | OU | 
| 218 | SE | 
| 219 | IT | 
| 220 | IL | 
| 221 | ET | 
| 222 | ST | 
| 223 | ON | 
| 224 | LO | 
| 225 | NU | 
| 226 | TH | 
| 227 | NO | 
| 228 | AL | 
| 229 | LE | 
| 230 | XE | 
| 231 | GE | 
| 232 | ZA | 
| 233 | CE | 
| 234 | BI | 
| 235 | SO | 
| 236 | US | 
| 237 | ES | 
| 238 | AR | 
| 239 | MA | 
| 240 | IN | 
| 241 | DI | 
| 242 | RE | 
| 243 | A | 
| 244 | ER | 
| 245 | AT | 
| 246 | EN | 
| 247 | BE | 
| 248 | RA | 
| 249 | LA | 
| 250 | VE | 
| 251 | TI | 
| 252 | ED | 
| 253 | OR | 
| 254 | QU | 
| 255 | AN | 

Tokens 215 to 227 are exclusive to the extended token system, while the standard tokens start at 228. They have token numbers that are 100 higher than the same tokens in the standard system, which is why the last four standard tokens are not available in the extended list, as they would have to have token numbers higher than 255.

The new two-letter tokens can be found in the table at [TKN2](https://elite.bbcelite.com/6502sp/main/variable/tkn2.html), which appears directly before the standard two-letter token table at QQ16. This means we can subtract 215 from the token number to get a number in the range 0-40, which acts as an index into the TKN2/QQ16 table when doubled (as each entry takes up two bytes).

## Random tokens: [n?]

													 -------------------

						Random tokens are encoded with values in the range 91-128. When DASC is asked to print a random token in this range, it subtracts 91 from the token number to get a number in the range 0 to 37, and then it fetches the corresponding entry from the table at [MTIN](https://elite.bbcelite.com/6502sp/main/variable/mtin.html), adds a random number in the range 0-4 to this number, and calls DETOK to print that token.

The ERND macro, which we use to encode random tokens in the TKN1 and RUTOK tables, takes an argument between 0 and 37, which corresponds to the lookup value in MTIN.

Random tokens are used to generate the extended descriptions for each system. For example, the entry at position 13 in the MTIN table (counting from 0) is 66, so ERND 14 will expand into a random token in the range 66-70, i.e. one of "JUICE", "BRANDY", "WATER", "BREW" and "GARGLE BLASTERS".

## Jump tokens: {n}

													 ----------------

						Jump tokens do exactly that - they call subroutines instead of being printed. The jump token is a very powerful token type, and implements all sorts of functionality, from drawing boxes and setting letter case, to justifying text and fetching input from the keyboard.

Jump tokens are in the range 1 to 31, though some tokens don't do anything. The best way to work out what each token does is to visit the relevant routine in the source. Here is a list of jump tokens in the original BBC Micro disc version of Elite, along with the subroutines that they call (the MT routines are listed in more detail below):

| Jump token | Shorthand in documentation | Routine | 
|---|---|---|
| 1 | {all caps} | [MT1](https://elite.bbcelite.com/6502sp/main/subroutine/mt1.html) | 
| 2 | {sentence case} | [MT2](https://elite.bbcelite.com/6502sp/main/subroutine/mt2.html) | 
| 3 | {selected system name} | [TT27](https://elite.bbcelite.com/6502sp/main/subroutine/tt27.html) | 
| 4 | {commander name} | [TT27](https://elite.bbcelite.com/6502sp/main/subroutine/tt27.html) | 
| 5 | {extended tokens} | [MT5](https://elite.bbcelite.com/6502sp/main/subroutine/mt5.html) | 
| 6 | {standard tokens, sentence case} | [MT6](https://elite.bbcelite.com/6502sp/main/subroutine/mt6.html) | 
| 7 | {beep} | [DASC](https://elite.bbcelite.com/6502sp/main/subroutine/tt26.html) | 
| 8 | {tab 6} | [MT8](https://elite.bbcelite.com/6502sp/main/subroutine/mt8.html) | 
| 9 | {clear screen} | [MT9](https://elite.bbcelite.com/6502sp/main/subroutine/mt9.html) | 
| 10 | {lf} | [DASC](https://elite.bbcelite.com/6502sp/main/subroutine/tt26.html) | 
| 11 | {draw box around title} | [NLIN4](https://elite.bbcelite.com/6502sp/main/subroutine/nlin4.html) | 
| 12 | {cr} | [DASC](https://elite.bbcelite.com/6502sp/main/subroutine/tt26.html) | 
| 13 | {lower case} | [MT13](https://elite.bbcelite.com/6502sp/main/subroutine/mt13.html) | 
| 14 | {justify} | [MT14](https://elite.bbcelite.com/6502sp/main/subroutine/mt14.html) | 
| 15 | {left align} | [MT15](https://elite.bbcelite.com/6502sp/main/subroutine/mt15.html) | 
| 16 | {drive number} | [MT16](https://elite.bbcelite.com/6502sp/main/subroutine/mt16.html) | 
| 17 | {system name adjective} | [MT17](https://elite.bbcelite.com/6502sp/main/subroutine/mt17.html) | 
| 18 | {random 1-8 letter word} | [MT18](https://elite.bbcelite.com/6502sp/main/subroutine/mt18.html) | 
| 19 | {single cap} | [MT19](https://elite.bbcelite.com/6502sp/main/subroutine/mt19.html) | 
| 20 | Unused | [DASC](https://elite.bbcelite.com/6502sp/main/subroutine/tt26.html) | 
| 21 | {clear bottom of screen} | [CLYNS](https://elite.bbcelite.com/6502sp/main/subroutine/clyns.html) | 
| 22 | {display ship, wait for key press} | [PAUSE](https://elite.bbcelite.com/6502sp/main/subroutine/pause.html) | 
| 23 | {move to row 10, white, lower case} | [MT23](https://elite.bbcelite.com/6502sp/main/subroutine/mt23.html) | 
| 24 | {wait for key press} | [PAUSE2](https://elite.bbcelite.com/6502sp/main/subroutine/pause2.html) | 
| 25 | {incoming message screen, wait 2s} | [BRIS](https://elite.bbcelite.com/6502sp/main/subroutine/bris.html) | 
| 26 | {fetch line input from keyboard} | [MT26](https://elite.bbcelite.com/6502sp/main/subroutine/mt26.html) | 
| 27 | {mission captain's name} | [MT27](https://elite.bbcelite.com/6502sp/main/subroutine/mt27.html) | 
| 28 | {mission 1 location hint} | [MT28](https://elite.bbcelite.com/6502sp/main/subroutine/mt28.html) | 
| 29 | {move to row 6, white, lower case} | [MT29](https://elite.bbcelite.com/6502sp/main/subroutine/mt29.html) | 

There are some minor differences in later versions of Elite. The 6502 Second Processor version has an extra token 30 that switches to white text:

| Jump token | Shorthand in documentation | Routine | 
|---|---|---|
| 30 | {white} | [WHITETEXT](https://elite.bbcelite.com/6502sp/main/subroutine/whitetext.html) | 

The Commodore 64, Apple II, BBC Master and NES versions have extra tokens 30 and 31, which are used to display the different media (tape or disk), though these are only used in the Commodore 64 version:

| Jump token | Shorthand in documentation | Routine | 
|---|---|---|
| 30 | {currently selected media} | [FILEPR](https://elite.bbcelite.com/c64/main/subroutine/filepr.html) | 
| 31 | {other media} | [OTHERFILEPR](https://elite.bbcelite.com/c64/main/subroutine/otherfilepr.html) | 

The NES version has a few further differences, with tokens 9, 23 and 29 moving the text cursor to different positions, and token 26 no longer waits for keyboard input, but instead prints a space and then does a {single cap}:

| Jump token | Shorthand in documentation | Routine | 
|---|---|---|
| 9 | {clear screen} | [MT9](https://elite.bbcelite.com/nes/bank_2/subroutine/mt9.html) | 
| 23 | {move to row 9, lower case} | [MT23](https://elite.bbcelite.com/nes/bank_2/subroutine/mt23.html) | 
| 26 | " {single cap}" | [MT26](https://elite.bbcelite.com/nes/bank_2/subroutine/mt26.html) | 
| 29 | {move to row 7, lower case} | [MT29](https://elite.bbcelite.com/nes/bank_2/subroutine/mt29.html) | 

Here's a list of MT routines that implement the bulk of the jump token functionality. The number of the MT routine corresponds to the jump token that triggers that routine.

| Routine | Function | 
|---|---|
| [MT1](https://elite.bbcelite.com/6502sp/main/subroutine/mt1.html) | Switch to ALL CAPS when printing extended tokens | 
| [MT2](https://elite.bbcelite.com/6502sp/main/subroutine/mt2.html) | Switch to Sentence Case when printing extended tokens | 
| [MT5](https://elite.bbcelite.com/6502sp/main/subroutine/mt5.html) | Switch to extended tokens | 
| [MT6](https://elite.bbcelite.com/6502sp/main/subroutine/mt6.html) | Switch to standard tokens in Sentence Case | 
| [MT8](https://elite.bbcelite.com/6502sp/main/subroutine/mt8.html) | Tab to column 6 and start a new word when printing extended tokens | 
| [MT9](https://elite.bbcelite.com/6502sp/main/subroutine/mt9.html) | Clear the screen and set the current view type to 1 | 
| [MT13](https://elite.bbcelite.com/6502sp/main/subroutine/mt13.html) | Switch to lower case when printing extended tokens | 
| [MT14](https://elite.bbcelite.com/6502sp/main/subroutine/mt14.html) | Switch to justified text when printing extended tokens | 
| [MT15](https://elite.bbcelite.com/6502sp/main/subroutine/mt15.html) | Switch to left-aligned text when printing extended tokens | 
| [MT16](https://elite.bbcelite.com/6502sp/main/subroutine/mt16.html) | Print the character in variable DTW7 | 
| [MT17](https://elite.bbcelite.com/6502sp/main/subroutine/mt17.html) | Print the selected system's adjective, e.g. Lavian for Lave | 
| [MT18](https://elite.bbcelite.com/6502sp/main/subroutine/mt18.html) | Print a random 1-8 letter word in Sentence Case | 
| [MT19](https://elite.bbcelite.com/6502sp/main/subroutine/mt19.html) | Capitalise the next letter | 
| [MT23](https://elite.bbcelite.com/6502sp/main/subroutine/mt23.html) | Move to row 10, switch to white text, and switch to lower case when printing extended tokens | 
| [MT26](https://elite.bbcelite.com/6502sp/main/subroutine/mt26.html) | Fetch a line of text from the keyboard | 
| [MT27](https://elite.bbcelite.com/6502sp/main/subroutine/mt27.html) | Print the captain's name during mission briefings | 
| [MT28](https://elite.bbcelite.com/6502sp/main/subroutine/mt28.html) | Print the location hint during the mission 1 briefing | 
| [MT29](https://elite.bbcelite.com/6502sp/main/subroutine/mt29.html) | Move to row 6, switch to white text, and switch to lower case when printing extended tokens | 

The MT routines use a number of extended print flags to store the current text state. The best way to work out what each flag does is to read the relevant variable's header in the source. They are as follows:

| Location | Function | Set by | 
|---|---|---|
| [DTW1](https://elite.bbcelite.com/6502sp/main/variable/dtw1.html) | A mask for applying the lower case part of Sentence Case to extended text tokens | MT1, MT2, MT13 | 
| [DTW2](https://elite.bbcelite.com/6502sp/main/variable/dtw2.html) | A flag that indicates whether we are currently printing a word | CLYNS, DASC, MT8, TTX66 | 
| [DTW3](https://elite.bbcelite.com/6502sp/main/variable/dtw3.html) | A flag for switching between standard and extended text tokens | MT5, MT6 | 
| [DTW4](https://elite.bbcelite.com/6502sp/main/variable/dtw4.html) | Flags that govern how justified extended text tokens are printed | MT14, MT15, MESS | 
| [DTW5](https://elite.bbcelite.com/6502sp/main/variable/dtw5.html) | The size of the justified text buffer at BUF | DASC, MESS, MT14, MT15, MT17 | 
| [DTW6](https://elite.bbcelite.com/6502sp/main/variable/dtw6.html) | A flag to denote whether printing in lower case is enabled for extended text tokens | MT1, MT2, MT13 | 
| [DTW7](https://elite.bbcelite.com/6502sp/main/subroutine/mt16.html) | Contains the character printed by MT16 | CATS | 
| [DTW8](https://elite.bbcelite.com/6502sp/main/variable/dtw8.html) | A mask for capitalising the next letter in an extended text token | DASC, MT19 |

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/extended_text_tokens.html](https://elite.bbcelite.com/deep_dives/extended_text_tokens.html)*
