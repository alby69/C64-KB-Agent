---
title: Highscore detection
source_url: https://codebase.c64.org/doku.php?id=base%3Ahigh_score_detection
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-20'
---

# Highscore detection

base:high_score_detection

                # Highscore detection

When I was coding games, like Bomb Chase 2007, etc. I wanted to add a high score detection routine. This example below shows how the high score detection works using 6 chars on screen, when using number chars on a game screen. :)

```
                        lda playerscore+0
			sec
			lda hiscore1+5
			sbc playerscore+5
			lda hiscore1+4
			sbc playerscore+4
			lda hiscore1+3
			sbc playerscore+3
			lda hiscore1+2
			sbc playerscore+2
			lda hiscore1+1
			sbc playerscore+1
			lda hiscore1+0
			sbc playerscore+0
			bpl nohiscore
                        jmp newhiscore
nohiscore:              ;Rest of program
newhiscore:             ;Rest of program 
```
base/high_score_detection.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`nohiscore`** (unknown): No description available
- **`newhiscore`** (unknown): No description available

```assembly
lda playerscore+0
			sec
			lda hiscore1+5
			sbc playerscore+5
			lda hiscore1+4
			sbc playerscore+4
			lda hiscore1+3
			sbc playerscore+3
			lda hiscore1+2
			sbc playerscore+2
			lda hiscore1+1
			sbc playerscore+1
			lda hiscore1+0
			sbc playerscore+0
			bpl nohiscore
                        jmp newhiscore

nohiscore:              ;Rest of program

newhiscore:             ;Rest of program
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ahigh_score_detection](https://codebase.c64.org/doku.php?id=base%3Ahigh_score_detection)*
