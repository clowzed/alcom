<div align = "center">
<h1>ALCOM</h1>
</div>
<div align = "center">
<h3>Comments aligner for assembler</h3>
</div>

#### Code factor
[![CodeFactor](https://www.codefactor.io/repository/github/clowzed/alcom/badge)](https://www.codefactor.io/repository/github/clowzed/alcom)
<br>

### Platforms
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
<br>

### Packet info
[![Downloads](https://pepy.tech/badge/alcom)](https://pepy.tech/project/alcom)
[![Downloads](https://pepy.tech/badge/alcom/month)](https://pepy.tech/project/alcom)
[![Downloads](https://pepy.tech/badge/alcom/week)](https://pepy.tech/project/alcom)

<div align="center"><h1>Installation</h1></div>

### From [`PyPi`](https://pypi.python.org/pypi/alcom)
```bash
py -m pip install alcom
pip3 install alcom
```


<div align="center"><h1>Usage</h1></div>

#### CLI Options
| short | long                      | description                | help                                                           |
|-------|---------------------------|----------------------------|----------------------------------------------------------------|
| -f    | --file                    | Sets filename for aligning | If not setted it will align all files in directory recursively |
| -nbc  | --align_no_blank_comments | Lave no blank comments     | If not setted no splitters would be placed after codeline      |

#### Running
```bash
alcom
alcom -f asmfile.asm
alcom -f asmfile.asm -nbc
```


<div align="center"><h1>Example</h1></div>

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

<div align="center"><h1>Tips</h1></div>

## VS Code
To add auto aligning after save:
- Add `Run on Save` extension
- Press `ctrl` + `P` and search for `Preferences: Open Workspace Settings (JSON)`
- Add code below into the opened file and save
```json
{
    "emeraldwalk.runonsave": {
        "commands": [
            {
                "match": ".asm",
                "cmd": "alcom -nbc"
            }
        ]
    }
}
```
- You are done!

## TODO
- [❌] Add marging options
- [❌] Issue that comments separator cam be placed in strings 