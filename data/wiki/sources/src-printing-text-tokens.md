---
id: src-printing-text-tokens
type: source
title: 'Source Summary: Printing text tokens'
aliases:
- Printing text tokens
- printing_text_tokens.md
tags:
- basic
- assembly
- graphics
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/printing_text_tokens.md
  sha256: 6e09e70732dd60d77a1825ffae45277273d64259aa9724e5e59c213f54ec45a1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Printing text tokens

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/printing_text_tokens.md`
**SHA256**: `6e09e70732dd60d77a1825ffae45277273d64259aa9724e5e59c213f54ec45a1`

## Summary



# Printing text tokens

## Printing recursive text tokens, two-letter tokens and control codes

There are lots of routines that print text in Elite, covering everything from the formatting of huge decimal numbers to printing individual spaces. For example, the Status Mode screen uses a whole range of those routines to print our commander's status:

![The Status Mode screen in the BBC Micro disc version of Elite](https://elite.bbcelite.com/images/disc/status_mode.png) 

Under the hood, the game...
