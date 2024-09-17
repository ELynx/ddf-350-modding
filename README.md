# DumboRC DDF-350 Transmitter firmware modding

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FELynx%2Fddf-350-modding&count_bg=%237FD2C6&title_bg=%23555555&icon=furrynetwork.svg&icon_color=%237FD2C6&title=Page+views&edge_flat=false)](https://hits.seeyoufarm.com)

## Current supported version - 1.1.3

## What this does

### Quick Program MIX toggle

[![Video demonstration of quick on/off feature](https://img.youtube.com/vi/AhQe9XWsPlI/hqdefault.jpg)](https://www.youtube.com/embed/AhQe9XWsPlI)

### New Program MIX mode - multiplicative mixing

[![Video demonstration of multiply feature](https://img.youtube.com/vi/MkXmJsyX0sQ/hqdefault.jpg)](https://www.youtube.com/embed/MkXmJsyX0sQ?start=20)

### Features

1. Gives you configurable quick ways to turn Program MIX 1 and 2 on and off without menu diving.
1. Gives you a new way of using Program MIX 1 and 2 by scaling / multiplying channels
1. Cleans up some English translation to my taste and to get rid of scrolling.
1. Clears up some German translation to best of my German knowledge to get rid of terrible amounts of scrolling.
1. Adds main screen battery level "circle" calibration for 4 NiMh batteries in addition to original options for 4 AA and 2/3S LiPo.
    * Range is 4.0 volts 0% to 5.6 volts 100%.
    * Also lowered voltage alarm lowest setting to 4.1 volts.

I am now into RC crawlers, and I have a crawler with four-wheel steering (4ws). This mod expresses my desire to be able to turn 4ws (and Crab) on and off without kilometer of menus. It replaces Timer, IMO not a huge loss on crawler community.

Remember, this mod allows you to do 4ws, but you need to configure your mixes. Also, you can configure anything else you want.

## How to install

⚠️ Important note: remote is **very** picky about USB cables. Even when cable work as Data cable for phone, PC, etc., remote may *not* work with it. ⚠️

Symptoms are "USB device error", device flash drive not appearing. Try different cables, one by one, until one of them works.

⚠️ Important note: always start patching with fresh 1.1.3 firmware file. Do not reuse files changed by previous mod releases. ⚠️

☑️ Note: turn off "Trigger priming" unless you need it. When it is on unexpectedly, it can cause a lot of confusion. ☑️

### Video version (step by step, but less nuanced)

[![Video demonstration](https://img.youtube.com/vi/8Tg5iURBdxE/hqdefault.jpg)](https://youtu.be/8Tg5iURBdxE)

### Text version (more nuances, read this if you have troubles)

1. Download and unpack firmware version 1.1.3 from official DumboRC site [here](https://www.dumborc.com/?page_id=930).
    * ⚠️ Always apply patch to **clean original** binary. ⚠️
        * Applying patch on top of previously patched binary _will_ result in glitches.
    * This mod will work **ONLY** with 1.1.3 download.
1. Back up the official files.
    * When 1.1.2 was released, 1.1.1 was removed. Same with 1.1.3 and 1.1.2. And you may need original firmware, so do yourself and others a favor and keep a copy.
1. Download very good tool named LunarIPS [here](https://fusoya.eludevisibility.org/lips).
    * This is because I _cannot_ distribute official firmware, but I _can_ [distribute my rom hacks](https://en.wikipedia.org/wiki/ROM_hacking#Distribution).
1. Download the latest `.ips` file.
    * Visit [latest release](https://github.com/ELynx/ddf-350-modding/releases/latest)
    * Find "Assets" under text description
    * Download `.ips` file
1. Using LunarIPS apply my "Romack" to clean fresh official 1.1.3 binary file.
    * LunarIPS modifies binary file "in place". Make sure to not override your backup.
    * Make sure you are applying it to the .bin file, and not the .zip
    * If (when) you do not see the .bin file in LunarIPS, change the filter inside it to `all files / *.*`
1. Flash the modified binary file as described in official instruction. To summarize it here, purely for your convenience:
    * Take out batteries from your remote.
    * Connect your remote to computer using USB cable _with data capabilities_.
       * ⚠️ It is **very** picky, not every cable will work. Try several until you find one.
    * Press and hold CH3 and CH4 buttons, then turn on the remote with power button.
    * Screen will flash "black", you will hear the chime. You can release the buttons now.
    * On your computer, you will see new USB flash drive appearing.
    * Run official .bat file to flash the image.
        * Manual copying does _not_ work, Windows creates "System Volume Information" and this throw process off. Official script takes care of that.
    * After bat file is complete, "Safe Eject" the flash drive.
    * Unplug the transmitter.
    * Plug the transmitter back, or insert batteries.
    * Turn transmitter on, new firmware fill flash automatically and you should see changes.
1. ☑️ Make sure to turn off "Trigger priming" unless you specifically need it.
    * It appears that trigger priming is "on" for some of the people by default.
    * It turns on ProgMIX 1 when you increase throttle.
    * By default, ProgMIXes mix CH1 and CH2, so you get very unexpected cross-talk between steering and throttle.
1. Enjoy! Drop a star on this repo, "watch" it for future updates. These numbers mean a lot to me, letting me know that I should not only to all this, but share with the community.
1. If this was useful, consider Ko-Fi or GitHub Sponsorship (one-time or monthly).

## Four-wheel steering setup

[![Video demonstration](https://img.youtube.com/vi/32zv6zOlYxQ/hqdefault.jpg)](https://youtu.be/32zv6zOlYxQ)

## SW-7 as throttle limit setup

[![Video demonstration](https://img.youtube.com/vi/C1-xoKf7d_Y/hqdefault.jpg)](https://youtu.be/C1-xoKf7d_Y)

## How to uninstall

1. Flash original firmware of your choice.

## Known limitations

1. Program MIX menu does not update "live" when you press the toggle buttons.
    * It updates if you change page back and forth, though.
    * I _maybe_ will look into this in future, but I do not want to break stuff "just because", or delay releases forever.
1. Desktop icon is Timer, and not something cool.
    * I know . Annoys me as well. I am working on graphical changes, but cannot figure graphical format yet.
    * As above, it is better so than broken or never.
1. Timer is gone.
    * Yes, this mod took its place.
    * I _crawl_ so does not affect me :3
1. 4 NiMh 4.0V as 0% is not optimal.
    * I aligned it with 4 AA and with lowest alarm voltage.
1. Program MIX multiplier is "funky" with VR knobs.
    * Yes, I know. But when I made a test version that was logically sound, it was visually difficult to understand.
    * Unless I think of something radically different or get a lot of inspiration, I will not spend more time on this.

## Safety, warranty, responsibility

I provide no guarantees of safety and I am not responsible if you break something.

I do my best and test everything on my own only transmitter, so I have "skin in the game". But I cannot predict everything and every situation.

Just to keep it cool, do not do this day before important drives.

## How I did this, how I do this myself

### Translations

With a help of stochastic parrot, I made some Python scripts to dump and insert UTF-8 strings. Of course, some are too short, some are not recognized and some are wrongly offset, but process is pretty smooth.

I highly recommend making a "translation" file, or modifying existing ones compared to changing raw binaries. You lose track of what is where quickly, and as I experience it with update, have to reinvent the wheel.

Current EN translation is 98% OK by me. DE translation is modified to get rid of scrolling, all your suggestions are welcome. I presume CN is very good. If you want to improve FR, make an issue, offer your help, we will work it out.

### Logic

With porting to 1.1.3 I finally started to publish my Ghidra projects publicly. With those, you can follow on my changes, or do yours, _collaboratively_.

It is still not Git-based, since Git replaces common server storage. As such, if you want to do something, let me know in the issues, I will make sure to upload my latest changes and take a break to allow your changes to pass.

You will need Ghidra (search engine of your choice is your friend). I use Ghidra 11.1.2.

You will need to set up `./ghidra_repositories` folder of this repo as `ghidra.repositories.dir` in `server.conf`.

You can set up user name as `user.name` / `VMARGS=-Duser.name=` in `launch.properties`.

I run server in `console` mode without any auth^2.

From there on, do a local "check-out" of project of interest, and follow the usual Ghidra SRE flow.

I export modified .bin file and flash it with standard procedure. In case of broken firmware recovery is possible, just follow standard flashing procedure.

I assume that if you want to mod firmwares and use Ghidra you know what you are doing.

## Your translation is bad / your choice of words is bad / there is a better term

Works for me :3

Jokes aside, I am open to suggestions. My goal was to get rid of scrolling, because scrolling gave me perceivable headache. Plus, couple of outdated terms that just need to go.

If you want to be helpful, look at the "Issues" page. Join existing issues there, or make a new one. Please add a *picture* of place you want to change, and clear writing you want to see there.

## Legals

I am not associated or affiliated with DumboRC, Radiolink or other commercial companies.

They in no way or shape endorse this, or involved in this. Likewise, Transmitter and it‘s firmware are their property and distribution.

I only distribute my changes to firmware, and I do this because changes are done by me.
