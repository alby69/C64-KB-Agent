---
id: src-high-score-detection
type: source
title: 'Source Summary: Highscore detection'
aliases:
- Highscore detection
- high_score_detection.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/high_score_detection.md
  sha256: b5a0f309b5ec55808fde2b902f5a2d2fc882470f23ab4569712946f414189518
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Highscore detection

**Raw Source File**: `data/docs/codebase_c64_org/base/high_score_detection.md`
**SHA256**: `b5a0f309b5ec55808fde2b902f5a2d2fc882470f23ab4569712946f414189518`

## Summary



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
			lda h...
