---
title: base:syntax_highligthing_acme_vim [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Asyntax_highligthing_acme_vim
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware: []
related: []
scraped_at: '2026-07-20'
---

# base:syntax_highligthing_acme_vim [Codebase64 wiki]

base:syntax_highligthing_acme_vim

                ### Syntax highlighting for ACME in vim

by Bitbreaker/Nuance^Metalvotze

first, you need some rules that do the highlighting for you, that will be placed in ~./vim/syntax/acme.vim → [acme_vim.tar.gz](https://codebase.c64.org/lib/exe/fetch.php?media=base:acme_vim.tar.gz)

in .vimrc you need then to append the following line to automatically highlight .asm files:

autocmd BufNewFile,BufRead *.asm set syntax=acme.vim

base/syntax_highligthing_acme_vim.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
autocmd BufNewFile,BufRead *.asm set syntax=acme.vim
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asyntax_highligthing_acme_vim](https://codebase.c64.org/doku.php?id=base%3Asyntax_highligthing_acme_vim)*
