# DumboRC DDF-350 Transmitter firmware modding

## What this does

[![Video demonstration](https://img.youtube.com/vi/AhQe9XWsPlI/hqdefault.jpg)](https://www.youtube.com/embed/AhQe9XWsPlI)

In text format:

1. Gives you configurable quick ways to turn Program MIX 1 and 2 on and off without menu diving.

2. Cleans up some English translation to my taste and to get rid of scrolling.

3. "Clears up" some German translation to best of my German knowledge to get rid of terrible amounts of scrolling.

I am now into RC crawlers, and I have a crawler with four-wheel steering (4ws). This mod expresses my desire to be able to turn 4ws (and Crab) on and off without kilometer of menus. It replaces Timer, IMO not a huge loss on crawler community.

Remember, this mod allows you to do 4ws, but you need to configure your mixes. Also, you can configure anything else you want.

## How to install

[![Video demonstration](https://img.youtube.com/vi/8Tg5iURBdxE/hqdefault.jpg)](https://youtu.be/8Tg5iURBdxE)

In text format:

1. Download and unpack firmware version 1.1.2 from official DumboRC site [here](https://www.dumborc.com/?page_id=930).

    * This mod will work ONLY with 1.1.2 download.
    * I will update it to best of my ability, supporting me will tell that it is useful and very likely speed this up.

2. Back up the official 1.1.2 files. When 1.1.2 was released, 1.1.1 was removed. And you need official 1.1.2 firmware, so do yourself and others a favor and keep a copy.

3. Download very good tool named LunarIPS [here](https://fusoya.eludevisibility.org/lips).

    * This is because I _cannot_ distribute official firmware, but I _can_ [distribute my rom hacks](https://en.wikipedia.org/wiki/ROM_hacking#Distribution).

4. Download the `DDF_V1.1.2 0.0.3mix.ips` file. Chances you are reading this on GitHub. This file should be visible in the listing nearby.

    * Try [this link](https://github.com/ELynx/ddf-350-modding/raw/main/DDF_V1.1.2%200.0.3mix.ips)
    * If for some reason this does not work, go to the file in repository, then find and click "Download raw file".

5. Using LunarIPS apply my "Romack" to clean fresh official 1.1.2 binary file.

    * LunarIPS modifies binary file "in place". Make sure to not override your backup.
    * Make sure you are applying it to the .bin file, and not the .zip
    * If (when) you do not see the .bin file in LunarIPS, change the filter inside it to `all files / *.*`

6. Flash the modified binary file as described in official instruction. To summarize it here, purely for your convenience:

    * Take out batteries from your remote.
    * Connect your remote to computer using USB cable _with data capabilities_.
    * Press and hold CH3 and CH4 buttons, then turn on the remote with power button.
    * Screen will flash "black", you will hear the chime. You can release the buttons now.
    * On your computer, you will see new USB flash drive appearing.
    * Run official .bat file to flash the image.
        * Manual copying does _not_ work, Windows creates "System Volume Information" and this throw process off. Official script takes care of that.
    * After bat file is complete, "Safe Eject" the flash drive.
    * Unplug the transmitter.
    * Plug the transmitter back, or insert batteries.
    * Turn transmitter on, new firmware fill flash automatically and you should see changes.

7. Enjoy! Drop a star on this repo, "watch" it for future updates. These numbers mean a lot to me, letting me know that I should not only to all this, but share with the community.

## Four-wheel steering setup

[![Video demonstration](https://img.youtube.com/vi/32zv6zOlYxQ/hqdefault.jpg)](https://youtu.be/32zv6zOlYxQ)

## How to uninstall

1. Flash stock firmware of your choice.

## Known limitations

1. Program MIX menu does not update "live" when you press the toggle buttons.
    * It updates if you change page back and forth, though.
    * I _maybe_ will look into this in future, but I do not want to break stuff "just because", or delay release forever.

2. Desktop icon is Timer, and not something cool.
    * I know . Annoys me as well. I am working on graphical changes, but cannot figure graphical format yet.
    * As above, it is better so than broken or never.

3. Timer is gone.
    * Yes, this mod took its place.
    * I _crawl_ so does not affect me :3

## Safety, warranty, responsibility

I provide no guarantees of safety and I am not responsible if you break something.

I do my best and test everything on my own only transmitter, so I have "skin in the game". But I cannot predict everything and every situation.

Just to keep it cool, do not do this day before important drives.

## How I did this, how I do this myself

Coming. There is so much writing I can do in one sitting. If you are a dev and want to do something similar, "watch" this repo for updates.

In short, .bin file is ARM Cortex 32-bit LE. Ghidra or other tool of your choice does the rest. As of time of writing, there are no checks on flashed firmware, flash at your heart's content.

I also have a "memdump" firmware version where buttons change memory address and content is displayed on screen. I plan to make this a permanent feature and plug it to CN language, but if you need it sooner ping me, we can work it out.

## Your translation is bad / your choice of words is bad / there is a better term

Works for me :3

Jokes aside, I am open to suggestions. My goal was to get rid of scrolling, because scrolling gave me perceivable headache.

Consider these restrictions:

* I can make text only shorter or same length.
* Umlauts and other addons "cost" twice more as regular letters (they take two bytes).
* Hieroglyphs "cost" 3 and more.

If you want to be helpful, look at the "Issues" page. Join existing issues there, or make a new one. Please add a *picture* of place you want to change, and clear writing you want to see there.

If you _really really_ want if fixed and fast, go to [hexed.it](https://hexed.it), load .bin file into it, and search for text you want to do. Remember [strings are null terminated](https://en.wikipedia.org/wiki/Null-terminated_string).

## Legals

I am not associated or affiliated with DumboRC, Radiolink or other commercial companies.

They in no way or shape endorse this, or involved in this. Likewise, Transmitter and it‘s firmware are their property and distribution.

I only distribute my changes to firmware, and I do this because changes are done by me.
