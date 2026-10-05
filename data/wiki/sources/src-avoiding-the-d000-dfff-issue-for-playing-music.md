---
id: src-avoiding-the-d000-dfff-issue-for-playing-music
type: source
title: 'Source Summary: The $D000-$DFFF issues of music code/data'
aliases:
- The $D000-$DFFF issues of music code/data
- avoiding_the_d000-_dfff_issue_for_playing_music.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/avoiding_the_d000-_dfff_issue_for_playing_music.md
  sha256: 9f6c638a530f840d76413688c53aa2a454c031e45121b98dc46bc602b3588f41
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: The $D000-$DFFF issues of music code/data

**Raw Source File**: `data/docs/codebase_c64_org/base/avoiding_the_d000-_dfff_issue_for_playing_music.md`
**SHA256**: `9f6c638a530f840d76413688c53aa2a454c031e45121b98dc46bc602b3588f41`

## Summary



# The $D000-$DFFF issues of music code/data

### Table of Contents

# The $D000-$DFFF issues of music code/data

After reading the tutorial Richard Bayliss submitted on “Playing music at $A000 - $FFFF “behind” kernal”, I thought I'd make out some important points:

# Problem 1

There may be the case where you include a music file that can start at any address BEFORE $D000, and leads to using up memory BETWEEN $D000-$DFFF. For example, a tune stored between $A000-$E757… say, it's a collection o...
