---
id: src-3d-rotation
type: source
title: 'Source Summary: 3D Rotation'
aliases:
- 3D Rotation
- 3d_rotation.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/3d_rotation.md
  sha256: 57fcf3282356e7eaa55cd03612c42a9bdedb727c43f9505617d62f3410915dc7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 3D Rotation

**Raw Source File**: `data/docs/codebase_c64_org/base/3d_rotation.md`
**SHA256**: `57fcf3282356e7eaa55cd03612c42a9bdedb727c43f9505617d62f3410915dc7`

## Summary



# 3D Rotation

### Table of Contents

# 3D Rotation

By Oswald/Resource and Bitbreaker/Oxyron/Nuance

Derived from the rotation in one plane, these are the basic equations to rotate a point defined with its x, y, z coordinates around all 3 axises:

Rotation about the x axis:

x' = x

y' = cos(xangle) * y - sin(xangle) * z

z' = sin(xangle) * y + cos(xangle) * z

Rotation about the y axis:

x' = cos(yangle) * x + sin(yangle) * z

y' = y

z' = -sin(yangle) * x + cos(yangle) * z

Rotation about t...
