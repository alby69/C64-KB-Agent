---
id: src-reading-the-error-channel-of-a-disk-drive
type: source
title: 'Source Summary: Reading the error channel of a disk drive'
aliases:
- Reading the error channel of a disk drive
- reading_the_error_channel_of_a_disk_drive.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/reading_the_error_channel_of_a_disk_drive.md
  sha256: 17d865a4239922781c35cc17d66617594cd8b8c43d90da1d45d331c89d7d8fe4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Reading the error channel of a disk drive

**Raw Source File**: `data/docs/codebase_c64_org/base/reading_the_error_channel_of_a_disk_drive.md`
**SHA256**: `17d865a4239922781c35cc17d66617594cd8b8c43d90da1d45d331c89d7d8fe4`

## Summary




# Reading the error channel of a disk drive

# Reading the error channel of a disk drive

A simple example on how to read the error channel of a disk drive and print the error string to screen.

The error string has a very simple format: error number, error string, track, sector

A small warning: Both the BASIC and the Assembler versions will deadlock if the device is not present.

Examples:

00, OK,00,00 (no error)

21, READ ERROR,18,00 (read error on track 18, sector 0)

BASIC code like you...
