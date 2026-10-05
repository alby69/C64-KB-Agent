---
id: src-syntax-highligthing-acme-vim
type: source
title: 'Source Summary: base:syntax_highligthing_acme_vim [Codebase64 wiki]'
aliases:
- base:syntax_highligthing_acme_vim [Codebase64 wiki]
- syntax_highligthing_acme_vim.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/syntax_highligthing_acme_vim.md
  sha256: 0a43b5f7e50c2e51caa746549bb462bf44e58e4f837e4de49bb7bd2ce6937b3e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:syntax_highligthing_acme_vim [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/syntax_highligthing_acme_vim.md`
**SHA256**: `0a43b5f7e50c2e51caa746549bb462bf44e58e4f837e4de49bb7bd2ce6937b3e`

## Summary



# base:syntax_highligthing_acme_vim [Codebase64 wiki]

base:syntax_highligthing_acme_vim

                ### Syntax highlighting for ACME in vim

by Bitbreaker/Nuance^Metalvotze

first, you need some rules that do the highlighting for you, that will be placed in ~./vim/syntax/acme.vim → [acme_vim.tar.gz](https://codebase.c64.org/lib/exe/fetch.php?media=base:acme_vim.tar.gz)

in .vimrc you need then to append the following line to automatically highlight .asm files:

autocmd BufNewFile,BufRead...
