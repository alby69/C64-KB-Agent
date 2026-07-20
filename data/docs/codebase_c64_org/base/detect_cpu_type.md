---
title: base:detect_cpu_type [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Adetect_cpu_type
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
related: []
scraped_at: '2026-07-20'
---

# base:detect_cpu_type [Codebase64 wiki]

base:detect_cpu_type

                ```
; ---------------------------------------------------------------------------
; Subroutine to detect an 816. Returns
;
;   - carry clear and 0 in A for a NMOS 6502 CPU
;   - carry set and 1 in A for CMOS 6502 CPUs
;   - carry set and 2 in A for a 65816
;
; This function uses a $1A opcode which is a INA on the 816 and C02, and
; ignored (interpreted as a NOP) on a NMOS 6502. Detection of the 65816 is
; done by the xba instruction which is a NOP on the 65C02s.
GetCPU:	lda	#0
      	inc	a	      	; .byte $1a
      	cmp	#1
       	bcc    	@L9
; This is at least a 65C02, check for a 65816
      	xba		    	; .byte $eb, put $01 in B accu
      	dec	a     		; .byte $3a, A=$00 if 65C02
       	xba    	       	       	; .byte $eb, get $01 back if 65816
       	inc    	a      	       	; .byte $1a, make $01/$02
@L9:	rts
```
Ullrich von Bassewitz uz@musoftware.de

base/detect_cpu_type.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
; ---------------------------------------------------------------------------
; Subroutine to detect an 816. Returns
;
;   - carry clear and 0 in A for a NMOS 6502 CPU
;   - carry set and 1 in A for CMOS 6502 CPUs
;   - carry set and 2 in A for a 65816
;
; This function uses a $1A opcode which is a INA on the 816 and C02, and
; ignored (interpreted as a NOP) on a NMOS 6502. Detection of the 65816 is
; done by the xba instruction which is a NOP on the 65C02s.

GetCPU:	lda	#0
      	inc	a	      	; .byte $1a
      	cmp	#1
       	bcc    	@L9

; This is at least a 65C02, check for a 65816

      	xba		    	; .byte $eb, put $01 in B accu
      	dec	a     		; .byte $3a, A=$00 if 65C02
       	xba    	       	       	; .byte $eb, get $01 back if 65816
       	inc    	a      	       	; .byte $1a, make $01/$02
@L9:	rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adetect_cpu_type](https://codebase.c64.org/doku.php?id=base%3Adetect_cpu_type)*
