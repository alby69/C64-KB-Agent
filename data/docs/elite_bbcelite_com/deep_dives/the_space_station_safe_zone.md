---
title: The space station safe zone
source_url: https://elite.bbcelite.com/deep_dives/the_space_station_safe_zone.html
category: deep-dive
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# The space station safe zone

## Details of the calculations behind the space station safe zone

The space station safe zone extends for quite a distance around the station, and there's nothing quite like seeing that familiar "S" dashboard icon at the end of a long, pirate-heavy trade run:

![The safe zone icon in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/safe_zone.png) 

						But how does Elite work out where the space station is, and where its all-important safe zone starts? Let's take a look at the calculations. (Note that the following applies to all 6502 versions of Elite apart from the NES version; see the [SpawnSpaceStation](https://elite.bbcelite.com/nes/bank_0/subroutine/spawnspacestation.html) routine for details of how the NES implements the safe zone.)

The calculations for the safe zone are done in [part 14 of the main flight loop](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_14_of_16.html), using the [MAS1](https://elite.bbcelite.com/cassette/main/subroutine/mas1.html) routine to add the nosev orientation vector to the coordinates of the planet's centre. This part of the main loop also spawns the station when we enter the safe zone, making sure to position the space station's slot so that it's facing the planet. The code cleverly combines the distance checks with the spawning logic, so if we do need to spawn the station, most of the station's ship data is already set up for us.

First, some definitions:

- The planet is spawned with a radius r of (96 0), and let's call the coordinate of the planet's centre (planet_x, planet_y, planet_z).
- nosev is a vector that points from the planet centre towards a fixed point on the surface that spins around as the planet pitches and yaws.
- As nosev is one of the orthonormal orientation vectors, it is a unit vector with a length of (96 0).

At ship scale we tend to interpret the unit vector length as representing 96.0, but in this case we are adding nosev_x_lo to x_lo (for example), so nosev does indeed represent a vector of length (96 0). Given that r is also (96 0), this means that nosev is a vector from the planet's centre to a point on the planet's surface.

If the planet centre is at (planet_x, planet_y, planet_z), then if we double nosev and add it to the centre, like this:

[ planet_x ] [ nosev_x ] [ planet_y ] + 2 * [ nosev_y ] [ planet_z ] [ nosev_z ]

then the result is a point high above the planet's surface - specifically, it's at an altitude of r above the planet's surface. This point spins around with the planet, so over time it traces out an orbit surrounding the planet, like an electron around a nucleus, at a distance of 2r from the planet's centre, and r from the planet's surface. We use this point as the current location of the space station.

The main flight loop checks whether our ship is within a distance of (192 0) of this point along all three axes (that's a distance of 2r). If we are close enough to the point, then we are close enough to the station to be in the safe zone, at which point we spawn the space station by calling the [NWSPS](https://elite.bbcelite.com/cassette/main/subroutine/nwsps.html) routine. This flips the direction of the nosev vector so that it points towards the planet's centre, which means the station's slot also points to the planet's centre when it is spawned.

This is why the station doesn't always appear when you are the same distance from the planet - sometimes you have to get really close, and other times it appears quite far out. It all depends on when the station passes near enough to our ship as it orbits round the planet.

Specifically, if nosev were pointing directly at us when the test were done, then the station would be spawned when we were 3r above the planet surface, and if it were pointing away from us, it would spawn when we were on the planet's surface (though in practice you wouldn't get this close to the planet without being close enough to spawn way before then).

It's worth noting that once the space station is spawned, it stays at the same coordinates in space and does not rotate around the planet along with the planet's nosev. So the orbiting point that we use in the above calculation isn't strictly the space station's location, it's just used to give us a point in the correct orbit.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ planet_x ]       [ nosev_x ]
  [ planet_y ] + 2 * [ nosev_y ]
  [ planet_z ]       [ nosev_z ]
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_space_station_safe_zone.html](https://elite.bbcelite.com/deep_dives/the_space_station_safe_zone.html)*
