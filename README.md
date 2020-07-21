[![CodeFactor](https://www.codefactor.io/repository/github/youngmeatboy/alcom/badge/master)](https://www.codefactor.io/repository/github/youngmeatboy/alcom/overview/master)
# ALCOM
# Comments aligner for asm (MASM)


# Installation
```bash
pip install alcom
pip3 install alcom
```
# Usage
```bash
alcom
alcom -f asmfile.asm
```
# Example
### Before
```asm
.MODEL TINY  ;set memory model
.DOSSEG
.DATA
        MSG DB "Hello, World!", 0Dh, 0Ah, '$'; message
.CODE
.STARTUP
        MOV AH, 09h ; moves 09h into ah
        MOV DX, OFFSET MSG
        INT 21h           ;run int 21h
        MOV AH, 4Ch
        INT 21h      ;exit
END
```
### After
```asm
.MODEL TINY                                                      ;    set memory model
.DOSSEG                                                          ;    
.DATA                                                            ;    
        MSG DB "Hello, World!", 0Dh, 0Ah, '$'                    ;    message
.CODE                                                            ;    
.STARTUP                                                         ;    
        MOV AH, 09h                                              ;    moves 09h into ah
        MOV DX, OFFSET MSG                                       ;    
        INT 21h                                                  ;    run int 21h
        MOV AH, 4Ch                                              ;    
        INT 21h                                                  ;    exit
END                                                              ;    

```
