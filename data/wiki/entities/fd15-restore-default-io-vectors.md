---
id: fd15-restore-default-io-vectors
type: entity
title: restore default I/O vectors
aliases:
- restore default I/O vectors
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd15-restore-default-io-vectors.md
  sha256: ad9e3559d62ce75beb3ab16aa633549959929073010a0ba4937a9a5b7930f465
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fd15-restore-default-io-vectors
---

# restore default I/O vectors



# $FD15 — restore default I/O vectors

## Disassemblatura
```assembly
.FD15  A2 30    LDX #$30   ; pointer to vector table low byte
.FD17  A0 FD    LDY #$FD   ; pointer to vector table high byte
.FD19  18       CLC   ; flag set vectors
```


## Commenti

### Original Disassembly (—)
- **$FD15**: pointer to vector table low byte
- **$FD17**: pointer to vector table high byte
- **$FD19**: flag set vectors

### Commodore-64-intern-Buch (Commodore)
- **$FD15**: LOW- und HIGH-Byte des
- **$FD17**: Zeigers auf Tabelle $FD30
- **$FD19**: Flag für 'Vektoren setzen'
- **$FD1A**: LOW- und HIGH-Byte
- **$FD1C**: des Zeigers setzen
- **$FD1E**: Zeiger setzen (16 Vektoren)
- **$FD20**: Wert aus Tabelle holen
- **$FD23**: C=1 holen,C=0 setzen
- **$FD25**: Tabellenwert holen
- **$FD27**: Tabellenwert setzen
- **$FD29**: Wert in Tabelle ablegen
- **$FD2C**: Zähler vermindern
- **$FD2D**: Fertig? nein: nächster Wert
- **$FD2F**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$FD15**: low  FD30
- **$FD17**: high FD30

### Magnus Nyman (Magnus Nyman)
- **$FD15**: $fd30 - table of KERNAL vectors
- **$FD17**: Clear carry to SET values.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fd15-restore-default-io-vectors]]
