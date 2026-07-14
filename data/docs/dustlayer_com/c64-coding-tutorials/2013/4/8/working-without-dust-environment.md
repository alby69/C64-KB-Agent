---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/4/8/working-without-dust-environment
category: tutorial
topics:
- assembly
- basic
difficulty: beginner
language: mixed
hardware:
- KERNAL
- CIA
related:
- kernal-routines
- keyboard-handling
- joystick-reading
- cia-registers
- memory-map
scraped_at: '2026-07-14'
---

# 

# Episode 1-2: Working without DUST environment

**Topics:** Maybe you are on Windows or Linux or the DUST setup for some reason did not work out. Here is some information how to work with the tutorial code provided on dustlayer.com.

- [Episode 1-1: Introduction to DUST - the Mac tool for C64 development](http://dustlayer.com/c64-coding-tutorials/2013/2/10/dust-c64-command-line-tool)
- **Episode 1-2: working without DUST environment**

### The point of using DUST

DUST is a problem solver for Mac OSX users. It takes care of setting up various tools to ease C64 cross-development. It follows a setup which is compliant with what I use to learn Machine Language and it is also the setup which will run code from dustlayer.com.

If you want to work with the tutorials on dustlayer.com but have a system environment not compatible to install DUST you can of course set up everything required yourself.

### Mandatory Tools

**ACME Cross Assembler  **

You will need the ACME cross assembler. There are of course other cross assemblers but I use this one. I have not tried others so I don't know if they are better but then again I am too lazy to evaluate assemblers when ACME works just fine.[Download ACME](https://sourceforge.net/projects/acme-crossass/)

**A C64 Emulator  **

Probably any C64 Emulator will do but I use Vice which is available on many systems. [Download Vice](http://sourceforge.net/projects/vice-emu/)

**Git**

Git is a command line client to download projects from a git repository. It's basically a version control system. I host all tutorials on [github.com](http://github.com/actraiser) which is great way to distribute source code. You need git to download tutorials code, every tutorial on dustlayer.com will have the download information on top of each article. You don't need to sign up on github.com if all you want is to download the code for the tutorials.[Download Git](http://git-scm.com/downloads)

That's all what is mandatory - everything else provided by DUST is sugar on top like pre-configured IDEs, build scripts, additional command line tools etc.

### Running dustlayer tutorial code

Here is an example workflow which should work out of the box when all tools above are set up by you.

The *open* command does not exist on Windows - run the hello_world.prg by double clicking it in the Explorer. It should be associated with the C64 emulator of your choice.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/4/8/working-without-dust-environment](https://dustlayer.com/c64-coding-tutorials/2013/4/8/working-without-dust-environment)*
