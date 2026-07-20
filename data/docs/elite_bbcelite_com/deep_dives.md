---
title: Index of all deep dive articles
source_url: https://elite.bbcelite.com/deep_dives/
category: source-code
topics:
- basic
- graphics
- assembly
- sprite programming
- input handling
- sound generation
difficulty: beginner
language: mixed
hardware:
- CIA
- SID
- CPU
- VIC-II
- KERNAL
- BASIC ROM
related:
- sid-registers
- sound-programming
- vic-ii-registers
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- sprite-programming
- raster-interrupts
- cia-registers
scraped_at: '2026-07-20'
---

# Index of all deep dive articles

This site contains over 130 deep dive articles that explain how Elite weaves its magic. If you want to learn how Elite works under the hood, then this is the place for you.

See the [quick start guide](https://elite.bbcelite.com/about_site/quick_start_guide.html) for some recommended starting points, or check out the following index of all the deep dive articles and jump straight in. The articles are presented in an order that makes sense for those wanting to unravel the inner workings of Elite, so if you're wondering where to start, I recommend simply working your way down the list.

Most articles apply to all the 6502 versions of Elite, but where this isn't the case, the relevant versions are shown. Version-specific dives are grouped towards the end.

## Software archaeology

													 --------------------

						- [The Elite source code family tree](https://elite.bbcelite.com/the_elite_source_code_family_tree.html)- Tracing the development history of 6502 Elite from the BBC Micro to the NES
- [Building Commodore 64 Elite from the source disk](https://elite.bbcelite.com/building_commodore_64_elite_from_the_source_disk.html)- How to build Commodore 64 Elite from the original BBC Micro source disk [C64]
- [Building Apple II Elite from the source disk](https://elite.bbcelite.com/building_apple_ii_elite_from_the_source_disk.html)- How to build Apple II Elite from the original BBC Micro source disk [Apple]

## The main game loop

													 ------------------

						- [Program flow of the main game loop](https://elite.bbcelite.com/program_flow_of_the_main_game_loop.html)- The sequence of events in the main game loop and the main flight loop
- [Scheduling tasks with the main loop counter](https://elite.bbcelite.com/scheduling_tasks_with_the_main_loop_counter.html)- How the main loop counter controls what we do and when we do it
- [Splitting the main loop in the NES version](https://elite.bbcelite.com/splitting_the_main_loop_in_the_nes_version.html)- How the main flight loop is split and shared with the combat demo [NES]

## Simulating the universe

													 -----------------------

						- [Galaxy and system seeds](https://elite.bbcelite.com/galaxy_and_system_seeds.html)- How system data is extracted from the galaxy and system seeds
- [Generating system data](https://elite.bbcelite.com/generating_system_data.html)- The algorithms behind the procedural generation of system data
- [Generating system names](https://elite.bbcelite.com/generating_system_names.html)- Producing system names from twisted seeds and two-letter tokens
- [Twisting the system seeds](https://elite.bbcelite.com/twisting_the_system_seeds.html)- How the system seeds are twisted to produce entire galaxies of stars
- [Market item prices and availability](https://elite.bbcelite.com/market_item_prices_and_availability.html)- The algorithms behind the generation of each system's cargo market

## Simulating the local bubble

													 ---------------------------

						- [The local bubble of universe](https://elite.bbcelite.com/the_local_bubble_of_universe.html)- The data structures used to simulate the universe around our ship
- [A sense of scale](https://elite.bbcelite.com/a_sense_of_scale.html)- Space is big, but just how large are the star systems in 8-bit Elite?
- [The space station safe zone](https://elite.bbcelite.com/the_space_station_safe_zone.html)- Details of the calculations behind the space station safe zone

## Ship data

													 ---------

						- [Ship blueprints](https://elite.bbcelite.com/ship_blueprints.html)- Specifications for all the different types of ship in the universe
- [Comparing ship specifications](https://elite.bbcelite.com/comparing_ship_specifications.html)- A detailed comparison of in-game statistics for the different ships in Elite
- [Ship data blocks](https://elite.bbcelite.com/ship_data_blocks.html)- Storing data for each of the ships in the local bubble of universe
- [The elusive Cougar](https://elite.bbcelite.com/the_elusive_cougar.html)- Vanishingly rare... but just how rare is the mysterious Cougar? [6502SP, C64, Master, NES]

## Moving and rotating in space

													 ----------------------------

						- [Pitching and rolling](https://elite.bbcelite.com/pitching_and_rolling.html)- Applying our pitch and roll to another ship's orientation in space
- [Pitching and rolling by a fixed angle](https://elite.bbcelite.com/pitching_and_rolling_by_a_fixed_angle.html)- How other ships manage to pitch and roll in space
- [Program flow of the ship-moving routine](https://elite.bbcelite.com/program_flow_of_the_ship-moving_routine.html)- A breakdown of the routine that moves the entire universe around us
- [Rotating the universe](https://elite.bbcelite.com/rotating_the_universe.html)- What happens to the rest of the universe when we rotate our ship?
- [Orientation vectors](https://elite.bbcelite.com/orientation_vectors.html)- The three vectors that determine a ship's orientation in space
- [Tidying orthonormal vectors](https://elite.bbcelite.com/tidying_orthonormal_vectors.html)- Making the orientation vectors orthonormal, and why this matters
- [Flipping axes between space views](https://elite.bbcelite.com/flipping_axes_between_space_views.html)- Details of how the different space views are implemented

## Docking and docking computers

													 -----------------------------

						- [Docking checks](https://elite.bbcelite.com/docking_checks.html)- The checks that determine whether we are docking... or just crashing
- [The docking computer](https://elite.bbcelite.com/the_docking_computer.html)- How the docking computer steers us home in the enhanced versions of Elite [Disc, 6502SP, C64, Apple, Master, NES, Elite-A]

## Tactics and combat

													 ------------------

						- [Combat rank](https://elite.bbcelite.com/combat_rank.html)- The long, long road from Harmless to Elite
- [In the crosshairs](https://elite.bbcelite.com/in_the_crosshairs.html)- How the game knows whether an enemy is being hit by our laser fire
- [Program flow of the tactics routine](https://elite.bbcelite.com/program_flow_of_the_tactics_routine.html)- How ships and missiles work out attack patterns... or how to run away
- [Advanced tactics with the NEWB flags](https://elite.bbcelite.com/advanced_tactics_with_the_newb_flags.html)- How the enhanced versions of Elite give their ships a bit more personality [Disc, 6502SP, C64, Apple, Master, NES, Elite-A]
- [Aggression and hostility in ship tactics](https://elite.bbcelite.com/aggression_and_hostility_in_ship_tactics.html)- Why some ships are peaceful traders while others seem hell-bent on revenge

## The scanner and dashboard

													 -------------------------

						- [The 3D scanner](https://elite.bbcelite.com/the_3d_scanner.html)- The maths behind Elite's famous 3D elliptical scanner
- [The dashboard indicators](https://elite.bbcelite.com/the_dashboard_indicators.html)- How the bar-based dashboard indicators display their data

## The split-screen mode

													 ---------------------

						- [The split-screen mode in BBC Micro Elite](https://elite.bbcelite.com/the_split-screen_mode.html)- Elite's famous split-screen mode, dissected and explained in detail [Cassette, Disc, 6502SP, Master, Elite-A]
- [The split-screen mode in Commodore 64 Elite](https://elite.bbcelite.com/the_split-screen_mode_commodore_64.html)- How the VIC-II makes it easy to implement the Commodore version's split screen [C64]
- [The split-screen mode in NES Elite](https://elite.bbcelite.com/the_split-screen_mode_nes.html)- How the NES version implements a split-screen mode without hardware timers [NES]

## Drawing pixels

													 --------------

						- [Drawing monochrome pixels on the BBC Micro](https://elite.bbcelite.com/drawing_monochrome_pixels_in_mode_4.html)- Poking screen memory to display monochrome pixels in the space view [Cassette, Disc, Elite-A]
- [Drawing colour pixels on the BBC Micro](https://elite.bbcelite.com/drawing_colour_pixels_in_mode_5.html)- Poking screen memory to display colour pixels in the dashboard view [Cassette, Disc, 6502SP, Master, Elite-A]
- [Drawing pixels in the Electron version](https://elite.bbcelite.com/drawing_pixels_in_the_electron_version.html)- Poking pixels into screen memory in the Acorn Electron version of Elite [Electron]
- [Drawing pixels in the Commodore 64 version](https://elite.bbcelite.com/drawing_pixels_in_the_commodore_64_version.html)- Updating the bitmap screen in the Commodore 64 version of Elite [C64]
- [Drawing pixels in the Apple II version](https://elite.bbcelite.com/drawing_pixels_in_the_apple_ii_version.html)- Working with the Apple II's unique high-resolution graphics mode [Apple]
- [Drawing pixels in the NES version](https://elite.bbcelite.com/drawing_pixels_in_the_nes_version.html)- How the NES version pokes pixels into the console's tile-based screen [NES]
- [Extended screen coordinates](https://elite.bbcelite.com/extended_screen_coordinates.html)- The extended 16-bit screen coordinate system behind the space view

## Drawing text

													 ------------

						- [Drawing text](https://elite.bbcelite.com/drawing_text.html)- How Elite draws text on-screen by poking character bitmaps directly into screen memory [Cassette, Disc, Electron, 6502SP, C64, Apple, Master, Elite-A]
- [Fonts in NES Elite](https://elite.bbcelite.com/fonts_in_nes_elite.html)- The three different fonts used in the Nintendo version of Elite [NES]

## Drawing lines

													 -------------

						- [Elite's line-drawing algorithm](https://elite.bbcelite.com/elites_line-drawing_algorithm.html)- The main line-drawing algorithm used to draw non-horizontal lines
- [Line-clipping](https://elite.bbcelite.com/line-clipping.html)- Efficiently clipping an extended line to the part that's on-screen
- [Drawing lines in the NES version](https://elite.bbcelite.com/drawing_lines_in_the_nes_version.html)- Using tiles as stepping stones when drawing lines on the NES [NES]

## Drawing ships

													 -------------

						- [Drawing ships](https://elite.bbcelite.com/drawing_ships.html)- The main routine for drawing 3D wireframe ships in space
- [Back-face culling](https://elite.bbcelite.com/back-face_culling.html)- How Elite draws solid-looking 3D ships by only drawing visible faces
- [Calculating vertex coordinates](https://elite.bbcelite.com/calculating_vertex_coordinates.html)- Determining whether a ship's vertex is visible or hidden from us
- [Flicker-free ship drawing](https://elite.bbcelite.com/flicker-free_ship_drawing.html)- How the BBC Master and Apple II versions reduce flicker when drawing ships [Apple, Master]
- [Backporting the flicker-free algorithm](https://elite.bbcelite.com/backporting_the_flicker-free_algorithm.html)- Applying the BBC Master's flicker-free ship-drawing algorithm to the other versions [Cassette, Disc, Electron, 6502SP, C64, Elite-A]

## Drawing circles and ellipses

													 ----------------------------

						- [Drawing circles](https://elite.bbcelite.com/drawing_circles.html)- The routines that draw planets and the hyperspace and docking tunnels
- [The ball line heap](https://elite.bbcelite.com/the_ball_line_heap.html)- How we remember the lines used to draw circles so they can be redrawn [Cassette, Disc, Electron, 6502SP, C64, Apple, Master, Elite-A]
- [Drawing ellipses](https://elite.bbcelite.com/drawing_ellipses.html)- How Elite draws ellipses for the planet's crater, meridian and equator

## Drawing planets

													 ---------------

						- [Drawing craters](https://elite.bbcelite.com/drawing_craters.html)- The algorithms behind the huge craters of planets like Diso
- [Drawing meridians and equators](https://elite.bbcelite.com/drawing_meridians_and_equators.html)- The algorithms behind the meridians and equators of planets like Lave
- [Drawing Saturn on the loading screen](https://elite.bbcelite.com/drawing_saturn_on_the_loading_screen.html)- How the loader draws the dot-based Saturn in Elite's epic loading screen [Cassette, Disc, Electron, 6502SP, Master, Elite-A]

## Drawing suns and explosions

													 ---------------------------

						- [Drawing the sun](https://elite.bbcelite.com/drawing_the_sun.html)- Drawing and storing the sun, and the systems on the Short-range Chart [Cassette, Disc, 6502SP, C64, Apple, Master, NES, Elite-A]
- [Drawing explosion clouds](https://elite.bbcelite.com/drawing_explosion_clouds.html)- Drawing and storing explosion clouds for ships whose luck runs out...

## Drawing stardust

													 ----------------

						- [Stardust in the front view](https://elite.bbcelite.com/stardust_in_the_front_view.html)- The algorithms behind the stardust particles in the front view
- [Stardust in the side views](https://elite.bbcelite.com/stardust_in_the_side_views.html)- The algorithms behind the stardust particles in the side views

## Missions

													 --------

						- [The Constrictor mission](https://elite.bbcelite.com/the_constrictor_mission.html)- Hunting high and low for the stolen Constrictor [Disc, 6502SP, C64, Apple, Master, NES, Elite-A]
- [The Thargoid Plans mission](https://elite.bbcelite.com/the_thargoid_plans_mission.html)- Evading the Thargoid threat in the depths of the third galaxy [Disc, 6502SP, C64, Apple, Master, NES, Elite-A]
- [The Trumbles mission](https://elite.bbcelite.com/the_trumbles_mission.html)- Furry fun in the Commodore 64 and NES versions of Elite [C64, NES]

## Text

													 ----

						- [Printing text tokens](https://elite.bbcelite.com/printing_text_tokens.html)- Printing recursive text tokens, two-letter tokens and control codes
- [Extended text tokens](https://elite.bbcelite.com/extended_text_tokens.html)- The extended text token system in the enhanced versions of Elite [Disc, 6502SP, C64, Apple, Master, NES, Elite-A]
- [Extended system descriptions](https://elite.bbcelite.com/extended_system_descriptions.html)- The famous "goat soup" algorithm that generates those strange and wonderful system descriptions [Disc, 6502SP, C64, Apple, Master, NES, Elite-A]
- [Printing decimal numbers](https://elite.bbcelite.com/printing_decimal_numbers.html)- How to print big decimal numbers with decimal points and padding
- [Multi-language support in NES Elite](https://elite.bbcelite.com/multi-language_support_in_nes_elite.html)- How the NES version supports English, German and French text [NES]

## Sound and music

													 ---------------

						- [Sound effects in Commodore 64 Elite](https://elite.bbcelite.com/sound_effects_in_commodore_64_elite.html)- Making the most of the SID sound synthesiser [C64]
- [Sound effects in Apple II Elite](https://elite.bbcelite.com/sound_effects_in_apple_ii_elite.html)- Attempting to make game sounds from a single, solitary click [Apple]
- [Sound effects in NES Elite](https://elite.bbcelite.com/sound_effects_in_nes_elite.html)- The largest set of sound effects in all the 6502 Elites [NES]
- [Music in Commodore 64 Elite](https://elite.bbcelite.com/music_in_commodore_64_elite.html)- The music driver behind the iconic Blue Danube and the catchy Elite Theme [C64]
- [Music in NES Elite](https://elite.bbcelite.com/music_in_nes_elite.html)- How David Whittaker's music module plays The Blue Danube [NES]

## Keyboards, joysticks and controllers

													 ------------------------------------

						- [The key logger](https://elite.bbcelite.com/the_key_logger.html)- Supporting concurrent in-flight key presses using a key logger
- [Reading the Commodore 64 keyboard matrix](https://elite.bbcelite.com/reading_the_commodore_64_keyboard_matrix.html)- Scanning the Commodore 64 keyboard without using the operating system [C64]
- [Bolting NES controllers onto the key logger](https://elite.bbcelite.com/bolting_nes_controllers_onto_the_key_logger.html)- How the NES version simulates a joystick and keyboard [NES]
- [Working with the Apple II keyboard](https://elite.bbcelite.com/working_with_the_apple_ii_keyboard.html)- Trying to implement a game-ready key logger, one key press at a time [Apple]

## Maths

													 -----

						- [Adding sign-magnitude numbers](https://elite.bbcelite.com/adding_sign-magnitude_numbers.html)- Doing basic arithmetic with sign-magnitude numbers
- [Calculating square roots](https://elite.bbcelite.com/calculating_square_roots.html)- The algorithm behind the square root routine
- [Shift-and-add multiplication](https://elite.bbcelite.com/shift-and-add_multiplication.html)- The main algorithm behind Elite's many multiplication routines
- [Multiplication and division using logarithms](https://elite.bbcelite.com/multiplication_and_division_using_logarithms.html)- Faster multiplication and division routines by using logarithm lookup tables [6502SP, C64, Apple, Master, NES]
- [Shift-and-subtract division](https://elite.bbcelite.com/shift-and-subtract_division.html)- The main algorithm behind Elite's many division routines
- [The sine, cosine and arctan tables](https://elite.bbcelite.com/the_sine_cosine_and_arctan_tables.html)- The lookup tables used for the planet-drawing trigonometric functions
- [Generating random numbers](https://elite.bbcelite.com/generating_random_numbers.html)- The algorithm behind Elite's random number generation routines

## Saving and loading

													 ------------------

						- [Commander save files](https://elite.bbcelite.com/commander_save_files.html)- A description of each and every byte in the saved commander file
- [The competition code](https://elite.bbcelite.com/the_competition_code.html)- All the information that's hidden in the Elite competition code [Cassette, Disc, Electron, 6502SP, C64, Apple]

## Demonstration modes

													 -------------------

						- [The Elite Demonstration Disc](https://elite.bbcelite.com/the_elite_demonstration_disc.html)- The secrets of Acornsoft's self-playing demo for the BBC Micro [Cassette, Disc]
- [Code changes in the Demonstration Disc](https://elite.bbcelite.com/code_changes_in_the_demonstration_disc.html)- The differences between the cassette version and the demonstration disc [Cassette, Disc]
- [The 6502 Second Processor demo mode](https://elite.bbcelite.com/6502sp_demo_mode.html)- All about the Star Wars-esque scroll text in the Tube-based version of Elite [6502SP]
- [The NES combat demo](https://elite.bbcelite.com/the_nes_combat_demo.html)- How the scroll text and combat practice works [NES]
- [Auto-playing the NES combat demo](https://elite.bbcelite.com/auto-playing_the_combat_demo.html)- The magic of watching Elite playing itself [NES]

## Memory maps

													 -----------

						- [BBC Micro cassette Elite memory map](https://elite.bbcelite.com/the_elite_memory_map.html)- Memory usage in the classic version of Elite, where space is really tight [Cassette]
- [BBC Micro disc Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_disc.html)- Memory usage in the enhanced disc version [Disc, Elite-A]
- [Acorn Electron Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_electron.html)- Memory usage in the smallest and most basic version of Elite [Electron]
- [6502 Second Processor Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_6502sp.html)- Memory usage in the colour version of Elite [6502SP]
- [Commodore 64 Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_commodore_64.html)- Memory usage in the musical version of Elite [C64]
- [Apple II Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_apple_ii.html)- Memory usage in the flicker-free version of Elite [Apple]
- [BBC Master Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_master.html)- Memory usage in the smoothest version of Elite [Master]
- [NES Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_nes.html)- Memory usage in the only console-based version of Elite [NES]

## BBC Micro disc Elite

													 --------------------

						- [Swapping between the docked and flight code](https://elite.bbcelite.com/docked_and_flight_code.html)- Using a disc drive to swap out the game binaries when launching and docking [Disc]
- [Ship blueprints in the BBC Micro disc version](https://elite.bbcelite.com/ship_blueprints_in_the_disc_version.html)- How the BBC Micro disc version loads its ship blueprints into memory [Disc]

## 6502 Second Processor Elite

													 ---------------------------

						- [6502 Second Processor Tube communication](https://elite.bbcelite.com/6502sp_tube_communication.html)- How the 6502 Second Processor version of Elite talks over the Tube [6502SP]
- [The TINA hook](https://elite.bbcelite.com/the_tina_hook.html)- Adding your own custom code to the 6502 Second Processor version using TINA [6502SP]
- [Secrets of the Executive version](https://elite.bbcelite.com/secrets_of_the_executive_version.html)- Infinite jumps, retro-futuristic fonts, speech support... and Pizzasoft? [6502SP]

## Commodore 64 Elite

													 ------------------

						- [Colouring the Commodore 64 bitmap screen](https://elite.bbcelite.com/colouring_the_commodore_64_bitmap_screen.html)- Adding a distinctive dash of colour to the Commodore 64 dashboard [C64]
- [Sprite usage in Commodore 64 Elite](https://elite.bbcelite.com/sprite_usage_in_commodore_64_elite.html)- Laser crosshairs, colourful explosions and lots of cuddly, furry Trumbles [C64]
- [Developing Commodore 64 Elite on a BBC Micro](https://elite.bbcelite.com/developing_commodore_64_elite_on_a_bbc_micro.html)- Sending Elite between 8-bit machines with the Programmer's Development System [C64]

## Apple II Elite

													 --------------

						- [File operations with embedded Apple DOS](https://elite.bbcelite.com/file_operations_with_embedded_apple_dos.html)- Saving and loading commander files with a customised version of DOS 3.3 [Apple]
- [Developing Apple II Elite on a BBC Micro](https://elite.bbcelite.com/developing_apple_ii_elite_on_a_bbc_micro.html)- Clues about the remote development of the Apple II version of Elite [Apple]

## NES Elite

													 ---------

						- [Comparing NES Elite with the other versions](https://elite.bbcelite.com/comparing_nes_elite_with_the_other_versions.html)- The features that make NES Elite so unique [NES]
- [Understanding the NES for Elite](https://elite.bbcelite.com/understanding_the_nes_for_elite.html)- The NES architecture and how it applies to Elite [NES]
- [Splitting NES Elite across multiple ROM banks](https://elite.bbcelite.com/splitting_nes_elite_across_multiple_rom_banks.html)- Details of the MMC1 controller and the 128K game ROM [NES]
- [The pattern and nametable buffers](https://elite.bbcelite.com/pattern_and_nametable_buffers.html)- How the NES version achieves its beautifully smooth wireframe graphics [NES]
- [Bitplanes in NES Elite](https://elite.bbcelite.com/bitplanes_in_nes_elite.html)- Squeezing two patterns into one tile using separate bitplanes [NES]
- [Drawing vector graphics using NES tiles](https://elite.bbcelite.com/drawing_vector_graphics_using_nes_tiles.html)- The art of the impossible: vector graphics on the NES [NES]
- [Views and view types in NES Elite](https://elite.bbcelite.com/views_and_view_types_in_nes_elite.html)- Configuring all the different views in the console version [NES]
- [Image and data compression](https://elite.bbcelite.com/image_and_data_compression.html)- How images and data are compressed in NES Elite [NES]
- [Displaying two-layer images](https://elite.bbcelite.com/displaying_two-layer_images.html)- The beautiful pixel art of the commander and system images [NES]
- [Sprite usage in NES Elite](https://elite.bbcelite.com/sprite_usage_in_nes_elite.html)- Stardust, scanners, images, crosshairs and more [NES]

## Elite-A

													 -------

						- [Making room for the modifications in Elite-A](https://elite.bbcelite.com/elite-a_making_room_for_the_modifications.html)- How Angus Duggan found enough spare memory for Elite-A's modifications [Elite-A]
- [Buying and flying ships in Elite-A](https://elite.bbcelite.com/elite-a_buying_and_flying_ships.html)- What it's like to save up for and fly your dream ship in Elite-A [Elite-A]
- [Ship blueprints in Elite-A](https://elite.bbcelite.com/elite-a_ship_blueprints.html)- The enhanced logic behind Elite-A's sophisticated ship blueprints system [Elite-A]
- [The Encyclopedia Galactica](https://elite.bbcelite.com/elite-a_the_encyclopedia_galactica.html)- Inside the encyclopedia, Elite-A's most recognisable modification [Elite-A]
- [The I.F.F. system](https://elite.bbcelite.com/elite-a_the_iff_system.html)- Friend or foe? Adding ship information to the 3D scanner [Elite-A]
- [Fixing ship positions](https://elite.bbcelite.com/elite-a_fixing_ship_positions.html)- Why Elite spawns certain ships in certain places, and how Elite-A fixes this [Elite-A]
- [Special cargo missions](https://elite.bbcelite.com/elite-a_special_cargo_missions.html)- Procedurally generating delivery missions and tracking progress [Elite-A]
- [Delta 14B joystick support](https://elite.bbcelite.com/elite-a_delta_14b_joystick_support.html)- All the controls of Elite in one single handset - the future is here! [Elite-A]
- [Tube communication in Elite-A](https://elite.bbcelite.com/elite-a_tube_communication.html)- How the 6502 Second Processor version of Elite-A talks over the Tube [Elite-A]
- [The original Elite-A source files](https://elite.bbcelite.com/elite-a_the_original_source_files.html)- How the original Elite-A source was written, edited and compiled [Elite-A]

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/](https://elite.bbcelite.com/deep_dives/)*
