# DumboRC DDF-350 Transmitter firmware modding

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FELynx%2Fddf-350-modding&count_bg=%237FD2C6&title_bg=%23555555&icon=furrynetwork.svg&icon_color=%237FD2C6&title=Page+views&edge_flat=false)](https://hits.seeyoufarm.com)

## What this does

[![Video demonstration of quick on/off feature](https://img.youtube.com/vi/AhQe9XWsPlI/hqdefault.jpg)](https://www.youtube.com/embed/AhQe9XWsPlI)

[![Video demonstration of multiply feature](https://img.youtube.com/vi/MkXmJsyX0sQ/hqdefault.jpg)](https://www.youtube.com/embed/MkXmJsyX0sQ?start=20)

In text format:

1. Gives you configurable quick ways to turn Program MIX 1 and 2 on and off without menu diving.
1. Gives you new way of using Program MIX 1 and 2 by scaling / multiplying channels
1. Cleans up some English translation to my taste and to get rid of scrolling.
1. "Clears up" some German translation to best of my German knowledge to get rid of terrible amounts of scrolling.
1. Adds main screen battery level "circle" calibration for 4 NiMh batteries in addition to original options for 4 AA and 2/3S LiPo.
    * Range is 3.6 volts 0% to 5.6 volts 100%.
    * Also lowered voltage alarm lowest setting to 4.1 volts.

I am now into RC crawlers, and I have a crawler with four-wheel steering (4ws). This mod expresses my desire to be able to turn 4ws (and Crab) on and off without kilometer of menus. It replaces Timer, IMO not a huge loss on crawler community.

Remember, this mod allows you to do 4ws, but you need to configure your mixes. Also, you can configure anything else you want.

## How to install

⚠️ Important note: remote is **very** picky about USB cables. Even when cable work as Data cable for phone, PC, etc., remote may *not* work with it. ⚠️

Symptoms are "USB device error", device flash drive not appearing. Try different cables, one by one, until one of them works.

[![Video demonstration](https://img.youtube.com/vi/8Tg5iURBdxE/hqdefault.jpg)](https://youtu.be/8Tg5iURBdxE)

In text format:

1. Download and unpack firmware version 1.1.2 from official DumboRC site [here](https://www.dumborc.com/?page_id=930).
    * ⚠️ Always apply patch to clean original binary ⚠️
        * Applying patch on top of previously patched binary _will_ result in glitches.
    * This mod will work ONLY with 1.1.2 download.
        * I will update it to best of my ability, supporting me will tell that it is useful and very likely speed this up.
1. Back up the official 1.1.2 files. When 1.1.2 was released, 1.1.1 was removed. And you need official 1.1.2 firmware, so do yourself and others a favor and keep a copy.
1. Download very good tool named LunarIPS [here](https://fusoya.eludevisibility.org/lips).
    * This is because I _cannot_ distribute official firmware, but I _can_ [distribute my rom hacks](https://en.wikipedia.org/wiki/ROM_hacking#Distribution).
1. Download the latest `.ips` file.
    * Visit [latest release](https://github.com/ELynx/ddf-350-modding/releases/latest)
    * Find "Assets" under text description
    * Download `.ips` file
1. Using LunarIPS apply my "Romack" to clean fresh official 1.1.2 binary file.
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
1. ⚠️ Make sure to turn off "Trigger priming" unless you specifically need it.
    * It appears that trigger priming is "on" for some of the people by default.
    * It turns on ProgMIX 1 when you increase throttle.
    * By default ProgMIXes mix CH1 and CH2, so you get very unexpected cross-talk between steering and throttle.
1. Enjoy! Drop a star on this repo, "watch" it for future updates. These numbers mean a lot to me, letting me know that I should not only to all this, but share with the community.

## Four-wheel steering setup

[![Video demonstration](https://img.youtube.com/vi/32zv6zOlYxQ/hqdefault.jpg)](https://youtu.be/32zv6zOlYxQ)

## SW-7 as throttle limit setup

[![Video demonstration](https://img.youtube.com/vi/TODO/hqdefault.jpg)](https://youtu.be/TODO)

## How to uninstall

1. Flash stock firmware of your choice.

## Known limitations

1. Program MIX menu does not update "live" when you press the toggle buttons.
    * It updates if you change page back and forth, though.
    * I _maybe_ will look into this in future, but I do not want to break stuff "just because", or delay release forever.
1. Desktop icon is Timer, and not something cool.
    * I know . Annoys me as well. I am working on graphical changes, but cannot figure graphical format yet.
    * As above, it is better so than broken or never.
1. Timer is gone.
    * Yes, this mod took its place.
    * I _crawl_ so does not affect me :3
1. NiMh 0% voltage is too low.
    * Chime in at #6 and suggest your voltages.
1. Program MIX multipler is "funky" with VR knobs.
    * Yes, I know. But no one told me they are interested in having this better beside single comment with no follow-up. Chine in at #3.

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

Jokes aside, I am open to suggestions. My goal was to get rid of scrolling, because scrolling gave me perceivable headache. Plus couple of outdated terms that just need to go.

If you want to be helpful, look at the "Issues" page. Join existing issues there, or make a new one. Please add a *picture* of place you want to change, and clear writing you want to see there.

If you _really really_ want if fixed and fast, go to [hexed.it](https://hexed.it), load .bin file into it, and search for text you want to do. Remember [strings are null terminated](https://en.wikipedia.org/wiki/Null-terminated_string).

## Legals

I am not associated or affiliated with DumboRC, Radiolink or other commercial companies.

They in no way or shape endorse this, or involved in this. Likewise, Transmitter and it‘s firmware are their property and distribution.

I only distribute my changes to firmware, and I do this because changes are done by me.
