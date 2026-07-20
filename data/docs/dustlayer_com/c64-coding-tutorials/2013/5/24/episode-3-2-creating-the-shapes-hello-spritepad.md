---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad
category: tutorial
topics:
- sprite programming
- basic
- assembly
- graphics
difficulty: beginner
language: mixed
hardware:
- SID
- KERNAL
- CIA
- VIC-II
- CPU
related:
- sound-programming
- music-player
- raster-interrupts
- vic-ii-registers
- sprite-programming
- sid-registers
- keyboard-handling
- kernal-routines
- joystick-reading
- cia-registers
- memory-map
scraped_at: '2026-07-20'
---


# 

# Episode 3-2: Creating the Shapes - Hello SpritePad

**Synopsis:** Creating C64 Sprites - especially on Mac - is not trivial. Here is an easy way to circumvent the problem with non-existing C64 Tools on Mac - we will simply run a Windows tool! 

**Download via  dust:** $ dust tutorials (select 'spritro') 

**Github Repository:**

[Spritro Source Code on Github](https://github.com/actraiser/dust-tutorial-c64-spritro)

- [Episode 3-1: Spritro - An Intro with a Sprite](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite)
- **Episode 3-2: Creating the Shapes - Hello SpritePad**
- [Episode 3-3: Loading Shapes and grasping Symbols](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols)
- [Episode 3-4: Flying the Space Ship off Course](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course)
- [Episode 3-5: Taking Command of the Ship Controls](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls)
- [Episode 3-6: Custom Character Sets - Hello CharPad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad)
- [Episode 3-7: Creating Pseudo Timers for Color Cycle](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle)
- [Episode 3-8: If the SID doesn't fit, use a bigger Hammer](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer)
- [Episode 3-9: Greetings, Acknowledgments and Links](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-9-greetings-acknowledgments-and-links)

### Creating Sprite Shapes on Mac OSX using a Windows Program

For moving Sprites over the screen we need Sprite Shapes which is the common term for one single frame of an animated Sprite. For this we want to use some good software - unfortunately such software does not exist on Mac OSX! However, we can use Wine - the Windows Emulator - to run SpritePad on Mac. SpritePad is a free Windows program which comes with everything we need to create Sprite Shapes for our intro.

### Getting Windows programs on Mac the easy way

We need to install Wine, however, as with many large open source projects, this can be very painful. Fortunately there are already solutions which install and configure everything you need to run Windows-Programs on a Mac using One-Click installers. The easiest I found is WineBottler. Just [download it on the official site](http://winebottler.kronenberg.org/).  Open the .dmg and drag the Wine and the WineBottler application to the */Application*-Folder. Then run WineBottler for the first time - it will set up some directories and with that you are good to go. 

### Running SpritePad on Mac

[Download SpritePad](http://csdb.dk/release/?id=100657) and unzip it to a folder of your choice. The clean way would be to put it under *~/Wine Files/drive_c/Program Files *which is the directory set up by WineBottler when it was run for the first time but really every other directory works as well. Double-Click on *SpritePad.exe* and after a short time you should see the User Interface - let's start! 

### What do we want to achieve?

For our little intro we need to animate and move a Sprite from right to left. I went for the traditional space ship but as a matter of fact I am no way skilled to draw and animate a good-looking sprite myself.

Luckily, SpritePad comes with some pre-bundled examples which include a number of Shapes - in modern environments you would probably call those files spritesheets. We will use one as basis and modify it to our liking. Let's load the [Uridium](http://www.lemon64.com/?game_id=2766) spritesheet which is located in the* /examples* directory of the unzipped SpritePad project. The good thing about using this particular sheet is that it already comes with a great Sprite - the famous Manta Class Space Ship from the game Uridium.

Our ship is supposed to fly into the screen from the right - go all the way to the left to disappear behind the side border before it shows up again on the opposite side.

Let's prepare our Spritesheet using SpritePad now. Click on *File->Open *then select the *Examples* folder and load the Uridium Spritesheet named *Uridium.spd*. If you don't want to do the work, just load the Sprites.spr which came with the Spritro Sources.

- This Uridium-Spritesheet contains 128 different Shapes. When you scroll a bit down using the right side scrollbar you will find the Manta Space Ship and all of its animations. 

### SpritePad 101

Let's quickly run through some of the buttons and boxes on SpritePad. Lots of the stuff should make sense to you when you read all other articles on Dustlayer.com. In the top left you have the 12x21 grid with double wide Pixels which is typical for a Multicolor Sprite. If you turn off Multicolor by using the checkbox below you will see that the grid changes to the standard 24x21 Layout but it also affects instantly the colors of course. As you remember Standard Sprites only have one common Background color stored in $D021 and one individual Foreground Color while in Multicolor mode we gain two extra colors and lose half of the horizontal resolution.

SpritePad will automatically adapt the options palette in the GUI. In Multicolor Mode a Sprite is displayed in the 12x21 Grid and we have four colors to choose from. When clearing the Multicolor checkbox, we have only two color options available. The Background Color and the individual Sprite Color stays as it is the same in both color modes but the two Multicolors disappeared and the Sprite in all editing and preview window changes accordingly - that is very convenient.

SpritePad comes with a simple Animator Tool to check whether our different Shapes will make a fluent animation when the they are played back continuously. To test this, just select the a number of sprite shapes with your mouse, then select the *Animator...*-Option unter Tools or hit the Short-Cut Button at the very right in the tool bar.

For example, select all Shapes from Frame 72 to Frame 87 - the Frame Number is displayed below the the small preview window between the Grid and the Spritesheet Window.  After you open the Animator you simply click on the *Play* Icon, that is the one facing to the right. The animation plays backs. 


**Looks great, doesn't it? **You can change Animation Speed and whether the Animation will repeat or go back and forth. This behavior of course is not exported with your Sprite Data but must be programmed ourselves later. To get back to the SpriteEditor you must first close the Animator-Tool by the way.

### Building our Sprite Shapes

Sprite Pad has a few more interesting options but for our intro we will only use existing frames without really modifying them.

The Space Ship is already there and you played back the animation a minute ago. We will Simply use the 16 already completed frames from 72 to 87. Since our Ship will just fly from right to left, that is all we need - case closed. Let's delete the rows below that animation by selecting everything and then hitting DEL on the keyboard.

Finally we want to delete all the Frames from 0 to 71 in the Spritesheet. Then we cut and paste the remaining 16 Ship Frames to the top of the spritesheet matrix. Once this is copied we can safely change the number of Frames from 128 to 16. This makes sure that only the shapes for the ship animation are saved into the output file.

**Our work is done! ** We would save the spritesheet as sprites.spr and put it in our resources folder of the Spritro project but of course it is already there when you downloaded the sources from Github or using DUST. Play a bit with the Sprite Editor though and change individual frames to get a feel for SpritePad. It's a great tool!

### The SpritePad Format

To further work with our Sprites in the actual C64 code we need to know how the Spritepad format is organized. It is in fact not hard to grasp but changed over the last couple of versions. The release I use is 1.8.1 downloaded at [CSDB](http://csdb.dk/release/?id=100657). The files have the extension .SPR, in the */example* folder of SpritePad they actually have the extension .SPD which seems to be for historic reasons. 

Anyways, the .SPR file starts with a header of three Bytes that determine the three shared colors. It does not matter if you only use Standard Mode sprites by the way, there will always be three bytes at the beginning of a .spr file reserved to store three bytes of information, thus in Standard Mode two of those Bytes are Zero.

After that header all the sprite shapes are following one by one. They consist of 63 Bytes of the actual Sprite Data plus 1 Byte which holds the the Information whether a Sprite is MultiColor or in Standard Mode plus the color code of the individual Sprite Color.

To get a better feeling for the data we look at the first 67 Bytes of our sprites.spr supplied with the Spritro sources. After the three initial Bytes for the shared colors we can basically see the first frame of the Manta Space Ship in the binary code - well with good imagination that is or by using some coloring like I used below in the picture. 

The first three Bytes are $00, $0B and $01 which correspond to Background Color, MultiColor 1 and MultiColor 2. We defined those colors in the SpritePad application. Since it is a MultiColor Sprite the next 252 Bit-Pairs define the source for the color information for each individual pair of pixels. In Standard Mode you would only work with $00 and $FF values of course but in Multicolor we have four different states, hence sources for color information. Read corresponding articles in the knowledge base if you need to recap on this.

Finally we reach Byte 64. The low Nibble stores the individual color Black in this particular case - therefore it is $00 - and the high Nibble of that Byte indicates by the most significant Bit set that this Sprite uses Multicolor Mode. For Standard Mode, Bit#7 of Byte 64 would have been set to low by SpritePad.

**Here is a drawing for a quick overview of the just explained properties of the format. **

When we load the Spritesheet into our program we must consider that the first three bytes are color information and that all the shapes follow afterwards. When loading the data into our program we can either parse the first three bytes or just skip them and put the color information manually into the appropriate registers. The latter is actually what I did.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad)*


### Collegamenti e Riferimenti Hardware
- **$D021 (Background Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d021).
