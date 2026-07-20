---
title: Market item prices and availability
source_url: https://elite.bbcelite.com/deep_dives/market_item_prices_and_availability.html
category: deep-dive
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Market item prices and availability

## The algorithms behind the generation of each system's cargo market

The prices and availability of the market items displayed in the Buy Cargo screen are calculated using a couple of complex formulae, which take a base value for each item, mix in a couple of economic variables, and blend it all with a bit of random behaviour. The result is the heart of Elite's trading system, where canny traders can make a killing (while the rest of us can't seem to get a break).

Here, for example, is a typical set of market prices and availability at Lave:

![The Market Price screen in BBC Micro Elite](https://elite.bbcelite.com/images/cassette/market_prices.png) 

						So how are these figures calculated? Let's start by looking at the formula for prices, and then availability.

## Market item prices

													 ------------------

						This is the formula for an item's price, which is implemented as an 8-bit calculation by the [TT151](https://elite.bbcelite.com/cassette/main/subroutine/tt151.html) routine:

price = (base_price + (random AND mask) + economy * economic_factor) * 4

The resulting price is 10 times the displayed price, so we can show it to one decimal place. The individual items in the calculation are as follows:

- The item's base_price is byte #0 in the market prices table at QQ23, so it's 19 for food, 20 for textiles, 235 for narcotics and so on.
- Each time we arrive in a new system, a random number is generated and stored in location QQ26, and this is shown as "random" in the calculation above.
- The item's mask is byte #3 in the market prices table at QQ23, so it's &01 for food, &03 for textiles, &78 for narcotics and so on. The more set bits there are in this mask, and the higher their position in this byte, the larger the price fluctuations for this commodity, as the random number is AND'd with the mask. So narcotics will vary wildly in price, while food and textiles will be relatively stable.
- The economy for a system is given in a 3-bit value, from 0 to 7, that is stored in QQ28. This value is described in more detail in routine TT24, but this is the range of values:
								QQ28 Economy type 0 Rich Industrial 1 Average Industrial 2 Poor Industrial 3 Mainly Industrial 4 Mainly Agricultural 5 Rich Agricultural 6 Average Agricultural 7 Poor Agricultural 
- The economic_factor is stored in bits 0-4 of byte #1 in the market prices table at QQ23, and its sign is in bit 7, so it's -2 for food, -1 for textiles, +8 for narcotics and so on. Negative factors show products that tend to be cheaper than average in agricultural economies but closer to average in rich industrial ones, while positive factors are more expensive in poor agricultural systems than rich industrial ones - so food is cheaper in poor agricultural systems while narcotics are very expensive, and it's the other way round in rich industrial systems, where narcotics are closer to the average price, but food is pricier.
- The units for this item (i.e. tonnes, grams or kilograms) are given by bits 5-6 of byte #1 in the market prices table at QQ23.

## Market item availability

													 ------------------------

						The availability of each item is also calculated using a formula, this time in the [GVL](https://elite.bbcelite.com/cassette/main/subroutine/gvl.html) routine. Again it is performed as an 8-bit calculation:

```
  quantity = (base_quantity + (random AND mask) - economy * economic_factor)
             mod 64
```
						If the result of the above is less than 0, then the available quantity is set to 0. The resulting availability is stored in the [AVL](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) table.

The item's base_availability is byte #2 in the market prices table at [QQ23](https://elite.bbcelite.com/cassette/main/variable/qq23.html), so it's 6 for food, 10 for textiles, 8 for narcotics and so on. The other variables are described above.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
price = (base_price + (random AND mask) + economy * economic_factor) * 4
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
quantity = (base_quantity + (random AND mask) - economy * economic_factor)
             mod 64
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/market_item_prices_and_availability.html](https://elite.bbcelite.com/deep_dives/market_item_prices_and_availability.html)*
