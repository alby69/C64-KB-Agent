---
id: src-sending-a-command-to-a-disk-drive
type: source
title: 'Source Summary: Sending a command to a disk drive, the easy way'
aliases:
- Sending a command to a disk drive, the easy way
- sending_a_command_to_a_disk_drive.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sending_a_command_to_a_disk_drive.md
  sha256: a137aa3ffaee77a67766c7e244d15507c679b728a868eb3d93f8e8f07e472463
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sending a command to a disk drive, the easy way

**Raw Source File**: `data/docs/codebase_c64_org/base/sending_a_command_to_a_disk_drive.md`
**SHA256**: `a137aa3ffaee77a67766c7e244d15507c679b728a868eb3d93f8e8f07e472463`

## Summary




# Sending a command to a disk drive, the easy way

base:sending_a_command_to_a_disk_drive

                # Sending a command to a disk drive, the easy way

The easiest way of sending a command to the disk drive is by simply using the command string as filename when calling OPEN.

BASIC code:

OPEN 15,8,15,"I":CLOSE 15

Assembler code:

```
        LDA #cmd_end-cmd
        LDX #<cmd
        LDY #>cmd
        JSR $FFBD     ; call SETNAM
        LDA #$0F      ; file number 15
        LDX $BA  ...
