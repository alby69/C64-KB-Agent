---
title: Elite over Econet on the Acorn Archimedes
source_url: https://elite.bbcelite.com/hacks/elite_over_econet_acorn_archimedes.html
category: source-code
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- SID
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Elite over Econet on the Acorn Archimedes

## Joining multiplayer scoreboards from the RISC OS version of Elite

If you are playing Archimedes Elite and want to send scores to a multiplayer scoreboard over Econet, then you only need two things: version 1.14 of Archimedes Elite and the EliteNet application. You can find download links for both of these on the [installing Elite over Econet](https://elite.bbcelite.com/elite_over_econet_installing.html) page.

![The EliteNet application](https://elite.bbcelite.com/images/elite_over_econet/elitenet.png) 

						Once you have both ArcElite and EliteNet installed on your system, you can load Elite as usual, and simply run the EliteNet application alongside, as in the screenshot above. Archimedes Elite already works fine when loaded from an Econet fileserver, so you can install Elite and EliteNet on your network if you want, but this isn't essential; you might find it quicker to load the game from a hard disc.

Configuring EliteNet to point to the scoreboard is pretty simple: you just fill in the configuration window and enable transmissions, and your scores should appear in the scoreboard (though note scores are only transmitted when you are actually in the game). Alternatively you can load an existing configuration from an EliteNet file by double-clicking the file or by dragging it to the application's window or icon bar icon.

You can save the network configuration and the current score as an EliteNet file. You can do this from the icon bar menu. This lets you take a break from playing a multiplayer game, and when you come back, you can reload both your EliteNet score file and your Elite commander file, so you can jump back into the competition without losing your place.

For full instructions on how to configure and use EliteNet, click Menu on the application icon in the Filer and choose Help from the App. '!EliteNet' submenu.

Let's look at how EliteNet works under hood, but first here's some advice on how kills are counted.

## Counting kills in Archimedes Elite

													 ----------------------------------

						Archimedes Elite is similar to BBC Master Elite in that each combat kill awards a variable number of kill points, with more difficult kills giving more points. To make things fair in multiplayer competitions, the BBC Master version reverts to the one-point-per-kill approach of the original BBC Micro version, so everyone is on a level playing field.

To do the same with Archimedes Elite, the EliteNet application observes the game running alongside it, rather than hacking into it (see below for the details). To obtain the combat score, it checks the player's rank twice every second, and if the rank has gone up since the last check, it awards one kill point in the multiplayer scoreboard.

This approach typically works well, but if you manage to kill a second ship within half a second of killing the first, then the second kill might not be recorded. Also, energy bombs in Archimedes Elite only award one kill point, rather than many, as the rank only goes up once for all those kills.

For the rest of this article, let's take a look at exactly how this observing is done.

## Adding scoreboard support to Archimedes Elite

													 ---------------------------------------------

						I haven't disassembled Archimedes Elite, and as quite a bit of it was written in C, I'm not sure I ever will. So if we can't easily hack the transmission routines into the game code, how can we persuade it to send scores to a multiplayer scoreboard over Econet?

The answer is buried inside the !EliteNet application directory, which contains a relocatable module called EliteOverEconet that looks after the whole thing. Indeed, the application is little more than a friendly user interface that sits on top of the module to make it easier to configure, and it's the module itself that does all the hard work. If you want to, it's possible to do away with the desktop application altogether and configure the module purely via star-commands or SWIs.

Relocatable modules are always resident in memory, so the EliteOverEconet module can effectively pull the scores out of the running game and transmit them to the configured Econet scoreboard. It does this in a very hands-off way, by observing the game rather than hacking into it. The module is configured to send score data at a regular interval (every ten seconds by default), and every time that interval elapses, the module checks whether the game is paged into main memory at &8000 (which it will be if it's the currently running task). If the game is paged in, the module fetches the relevant data from within game memory and transmits a data packet to the scoreboard.

These two scheduled tasks (transmit and rank check) are implemented as ticker events using OS_CallEvery. Both event handlers start by checking whether Elite is the currently active task that's paged into application space at address &8000. My first attempt to identify Elite as the current task was fairly rudimentary; it would simply check three specific memory locations within application memory to make sure they matched the Elite binary. But this approach proved unreliable, as OS_ValidateAddress would sometimes confirm that addresses were valid, when they would in fact give an abort on data transfer, thus crashing the whole process.

So the latest version of the module does things more reliably, and without needing to poke around in application space. When the module first starts up, it runs through all the active tasks using TaskManager_EnumerateTasks and looks for the task called "Elite", noting the task handle when it finds it. Then, when the module wants to fetch a value from within the running game, it gets the handle for the currently active task using Wimp_ReadSysInfo, and checks to see if it matches the handle for Elite; if they match then we know Elite is currently paged in at &8000, and we can safely fetch data from within the game as it runs.

This approach works well for all the data except the kill tally and the death count, which aren't directly stored anywhere in the Elite application. Let's look at these in turn.

As mentioned above, Archimedes Elite is like the BBC Master version, in that it awards multiple points for each kill, with more difficult kills awarding more points. To make multiplayer competitions fair, we need all versions to support the one-point-per-kill approach of the original BBC Micro version, including Archimedes Elite. So, independently of the scheduled transmissions mentioned above, the module checks the player's rank twice a second, and if the rank has gone up, it awards one kill point in the multiplayer scoreboard.

The death count is trickier, as the game doesn't keep a track of deaths anywhere. To get around this, the EliteOverEconet module injects two SWI calls into the game binary. The first is a call to the module's Elite_GameOver SWI, which is injected into the code that prints the "GAME OVER" text. This only ever appears when we die, so it's a reliable trigger for counting deaths. Unfortunately the text is actually drawn on every frame, as it's shown in front of the spinning remains of our plucky Cobra, so we can't simply increase the death count in this routine; instead we set a flag to say the SWI has been called, and we inject a second call into the code that prints the copyright message on the title screen. This second injection calls the module's Elite_GameRestart SWI, which checks the flag that gets set by Elite_GameOver. If the flag is set then this second SWI increments the death count before resetting the flag. This ensures that we count one death when the title screen appears, but only if it's being shown following the game over screen.

If you want to find out exactly how this is all done, the source code for the EliteOverEconet module is fully documented. You can find this and the source for the EliteNet application in the [project's repository](https://github.com/markmoxon/elite-over-econet-acorn-archimedes).

To see a full list of star-commands supported by the module, load the module (or run EliteNet), press F12 and enter:

*HELP EL.

The module also supports two SWIs, Elite_GetStatus and Elite_SetStatus. To find out more about these, look at the comments in the SWI_Elite_GetStatus and SWI_Elite_SetStatus routines in the [module's source](https://github.com/markmoxon/elite-over-econet-acorn-archimedes/blob/main/1-source-files/main-sources/EliteOverEconet.arm). You can see these SWIs being used in the application's [!RunImage source](https://github.com/markmoxon/elite-over-econet-acorn-archimedes/blob/main/1-source-files/main-sources/!RunImage.bas) - search for "XElite" to see how they can be called.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*HELP EL.
```



---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_over_econet_acorn_archimedes.html](https://elite.bbcelite.com/hacks/elite_over_econet_acorn_archimedes.html)*
