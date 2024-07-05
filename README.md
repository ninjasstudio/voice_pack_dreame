# GLaDOS Voice Pack for Dreame Vacuum Robots

Uses voice generation by [15.ai](https://15.ai/).

MD5 sum of the prepackaged `voice_pack.tar.gz`:  
`44faf8e593f91a28714e6ffb4e594619`

Works at least with `L10 Pro`, `Z10 Pro`, `W10`, and `D9`.

## Installation

1. In Valetudo go to "Robot Settings" -> "Misc Settings"
1. Enter the following information in the "Voice packs" section:
    - URL: `https://github.com/ninjasstudio/voice_pack_dreame/raw/main/voice_pack.tar.gz`
    - Language Code: `GLADOS`
    - Hash: `44faf8e593f91a28714e6ffb4e594619`
    - File size: `3595868` byte
1. Click "Set Voice Pack"

Interestingly on my L10 Pro running `Valetudo 2022.03.0` the .tar.gz doesn't seem to work and the newly created folder `/data/personalized_voice/GLADOS` stays empty.
However, the language code is set correctly in Valetudo and manually copying the files into the right directory works:

```
git clone https://github.com/ninjasstudio/voice_pack_dreame
scp voice_pack_dreame/output/* root@<YOUR_ROBOT_ADDRESS>:/data/personalized_voice/GLADOS
```

-----
Thanks to https://github.com/ccoors/dreame_voice_packs for the inspiration and the list of sounds and 15.ai for the voice generation.
