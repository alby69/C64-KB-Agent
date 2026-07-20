---
title: Rotate byte and perform an action on each bit set to 1
source_url: https://codebase.c64.org/doku.php?id=base%3Arotate_byte_and_act_on_1-bits
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
related: []
scraped_at: '2026-07-20'
---

# Rotate byte and perform an action on each bit set to 1

# Rotate byte and perform an action on each bit set to 1

Invented by Hoogo. Written by Frantic.

Sometimes you've got a byte value and for each bit you want to perform some action if the bit is set to 1 and do nothing, or something else, if the bit is set to 0. Hoogo came up with [a nice way of doing that on CSDb](http://csdb.dk/forums/?roomid=11&topicid=115488#115562) which doesn't clobber any registers except for the status register.

asl pattern bcc no_action inc pattern ;Perform action here ... no_action:

This works fine because ASL always shifts in a 0 as the new lsb in the byte and the INC, which changes the lsb to 1, is only executed if a 1 was shifted out into the carry flag by the ASL instruction.

In some circumstances it might be a better optimization to use 0 as flag for “take action” instead of 1, because then the INC will only be needed when no action is to be taken, but whether that is desirable obviously depend on a number of factors.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`no_action`** (unknown): Perform action here

```assembly
asl pattern
	bcc no_action
	inc pattern
	;Perform action here
	...
no_action:
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Arotate_byte_and_act_on_1-bits](https://codebase.c64.org/doku.php?id=base%3Arotate_byte_and_act_on_1-bits)*
