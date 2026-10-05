---
id: src-decoding-bitstreams
type: source
title: 'Source Summary: Decoding bitstreams for fun and profit'
aliases:
- Decoding bitstreams for fun and profit
- decoding_bitstreams.md
tags:
- sprite programming
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/decoding_bitstreams.md
  sha256: 47569eeca375cfd1cf9602bb88cf4825b8526e5582bcb31d8142970124a0be5e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Decoding bitstreams for fun and profit

**Raw Source File**: `data/docs/codebase_c64_org/base/decoding_bitstreams.md`
**SHA256**: `47569eeca375cfd1cf9602bb88cf4825b8526e5582bcb31d8142970124a0be5e`

## Summary



# Decoding bitstreams for fun and profit

### Table of Contents

# Decoding bitstreams for fun and profit

by lft

This article describes a technique for extracting bitfields from a long sequence of bytes stored in RAM.

As an example application, consider a scroller where the text is a string of 5-bit character codes. The entire text could then be stored as a bitstream, from which you read five bits at a time. But you might save some space if you represent, say, the eight most common characte...
