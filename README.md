# py-tts-sonic-the-hedgehog-2023

This project provides a TTS layer for [The Murder of Sonic the Hedgehog by Sega](https://en.wikipedia.org/wiki/The_Murder_of_Sonic_the_Hedgehog).

This app has been tested on Ubuntu 22.04

## Usage

1. Install espeak and dependencies. `sudo apt install espeak ffmpeg libespeak1`
2. Install dependencies. `pip install -r requirements.txt`
3. Open the game to the loading screen.
![loading screen](./loading_screen.png)
[Art by sega](https://en.wikipedia.org/wiki/The_Murder_of_Sonic_the_Hedgehog)
4. Run `main.py`. Set the `DEBUG` env variable to `true` to see how the app reads text.
5. The app will let you know when it has found the window.
6. Play as normal.

