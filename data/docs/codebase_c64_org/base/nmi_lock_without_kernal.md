---
title: NMI Lock Without Kernal
source_url: https://codebase.c64.org/doku.php?id=base%3Anmi_lock_without_kernal
category: reference
topics:
- assembly
difficulty: advanced
language: assembly
hardware:
- KERNAL
- CIA
related:
- keyboard-handling
- memory-map
- joystick-reading
- kernal-routines
- cia-registers
scraped_at: '2026-07-20'
---

# NMI Lock Without Kernal

base:nmi_lock_without_kernal

                # NMI Lock Without Kernal

Modification of the example given at [NMI lock](https://codebase.c64.org/doku.php?id=base:nmi_lock). The NMI is locked without using kernal routines and without using RAM at $0318/$0319.

; 'Disable NMI' without using kernal and $0318/$0319 by Sokrates sei ;; switch off interrupt lda #$35 ;; all RAM except D000-Dfff sta $01 ;; write to $FFFA/$FFFB now possible lda #<nmiRoutine ;; change nmi vector to nmiRoutine sta $FFFA lda #>nmiRoutine sta $FFFB lda #$00 ;; stop Timer A sta $DD0E sta $DD04 ;; set Timer A to 0, after starting sta $DD05 ;; NMI will occur immediately lda #$81 sta $DD0D ;; set Timer A as source for NMI lda #$01 sta $DD0E ;; start Timer A -> NMI ;; from here on NMI is disabled ... nmiRoutine rti ;; exit interrupt not acknowledged

base/nmi_lock_without_kernal.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
; 'Disable NMI' without using kernal and $0318/$0319 by Sokrates

  sei  ;; switch off interrupt
  lda #$35 ;; all RAM except D000-Dfff 
  sta $01  ;; write to $FFFA/$FFFB now possible
  lda #<nmiRoutine ;; change nmi vector to nmiRoutine
  sta $FFFA		     
  lda #>nmiRoutine
  sta $FFFB 			
  lda #$00  ;; stop Timer A
  sta $DD0E 
  sta $DD04 ;; set Timer A to 0, after starting
  sta $DD05 ;; NMI will occur immediately
  lda #$81  
  sta $DD0D ;; set Timer A as source for NMI 
  lda #$01  
  sta $DD0E ;; start Timer A -> NMI
  ;; from here on NMI is disabled
  ...

nmiRoutine
  rti ;; exit interrupt not acknowledged
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Anmi_lock_without_kernal](https://codebase.c64.org/doku.php?id=base%3Anmi_lock_without_kernal)*
