---
id: src-rs232silversurfer-h
type: source
title: 'Source Summary: rs232silversurfer.h'
aliases:
- rs232silversurfer.h
- rs232silversurfer_h.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/rs232silversurfer_h.md
  sha256: 9e538610bd9cbaa73070c2ac95252f55c191a90836adb1748a3fc61b00d4cf7a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: rs232silversurfer.h

**Raw Source File**: `data/docs/codebase_c64_org/base/rs232silversurfer_h.md`
**SHA256**: `9e538610bd9cbaa73070c2ac95252f55c191a90836adb1748a3fc61b00d4cf7a`

## Summary



# rs232silversurfer.h

base:rs232silversurfer.h

                # rs232silversurfer.h

```
/*
* rs232silversurfer.h
*
* Groepaz/Hitmen, 16.12.2001
*
* This defines for the SilverSurver (16c550 UART) what Ullrichs rs232 module
* defines for the Swithlink/Turbo232
*
* this driver operates in polling mode only atm !
*
*/
#ifndef _RS232silversurfer_H
#define _RS232silversurfer_H
/*****************************************************************************/
/*                   Data              ...
