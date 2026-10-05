---
id: src-double-irq-explained
type: source
title: 'Source Summary: Double IRQ explained'
aliases:
- Double IRQ explained
- double_irq_explained.md
tags:
- sprite programming
- basic
- graphics
- assembly
- raster interrupts
sources:
- path: data/docs/codebase_c64_org/base/double_irq_explained.md
  sha256: 87f22b5b90b1978431efd8b5ae158dd09d6f37dee944451ede20e1f4b2349ce4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Double IRQ explained

**Raw Source File**: `data/docs/codebase_c64_org/base/double_irq_explained.md`
**SHA256**: `87f22b5b90b1978431efd8b5ae158dd09d6f37dee944451ede20e1f4b2349ce4`

## Summary




# Double IRQ explained

### Table of Contents

# Double IRQ explained

Writing a raster interrupt routine on the Commodore 64, stabilised using the double interrupt technique

Author: Wouter Bovelander
Date: july 2015
Location: [http://www.thehilander.nl](http://www.thehilander.nl)

### Introduction

There are many reasons why you would want to split the Commodore 64's screen into different parts, each part doing something independently from the other. You may want to have each part use a dif...
