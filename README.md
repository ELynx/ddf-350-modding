# DumboRC DDF-350 Transmitter firmware modding

## ℹ️ Current supported firmware version - 1.1.5 ℹ️

## ℹ️ Current mod version - 0.7.0 ℹ️

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FELynx%2Fddf-350-modding&count_bg=%237FD2C6&title_bg=%23555555&icon=furrynetwork.svg&icon_color=%237FD2C6&title=Page+views&edge_flat=false)](https://hits.seeyoufarm.com)

## Versions 0.7.x targeting long-term firmware release 1.1.5

### Version 0.7.0

Improved translations for EN and DE:
* No scrolling.
* Reduces ambiguity.

Transmitter battery display option for four NiMh cells:
* Range 0% at 4.0 Volts to 100% at 5.6 Volts.
* Lower possible transmitter voltage alarm setting down to 4.1 Volts.

<details>
<summary>Previous versions</summary>

[![Version 0.6.0](https://img.youtube.com/vi/W_R5PePB6ME/hqdefault.jpg)](https://www.youtube.com/embed/W_R5PePB6ME)

[![Version 0.0.4](https://img.youtube.com/vi/AhQe9XWsPlI/hqdefault.jpg)](https://www.youtube.com/embed/AhQe9XWsPlI)

</details>

## How to install

⚠️ Important note: transmitter is **very** specific with USB cables. Even when USB cable works as a data cable for phone, PC, etc., it may *not* work with transmitter. ⚠️

Symptoms include "USB device error", device flash drive not appearing. Try different cables, one by one, until one of them works.

⚠️ Remove batteries from transmitter before doing upgrades. ⚠️

### ⚠️ Upgrading from firmware versions lower than 1.1.5, stock or modded ⚠️

If your current firmware version is lower than 1.1.5, stock or modded, you need **ONCE** to update to stock version 1.1.5.

Process depends on your current version, and I will leave explanation to official video and website.

[![Official 1.1.5 installation guide on YouTube](https://img.youtube.com/vi/NK6ea4CEv3U/hqdefault.jpg)](https://www.youtube.com/embed/NK6ea4CEv3U)

[Official DumboRC site with firmware for DDF-350](https://www.dumborc.com/?page_id=930)

Once you successfully updated to 1.1.5, return here. You will not need to go through whole boot update process.

### Upgrading 1.1.5 stock <-> mod or upgrading versions of mod

⚠️ Important note: always start patching with clean original 1.1.5 firmware file `DDF.bin`. Do not reuse files changed by previous mod releases. ⚠️

1. Start with 1.1.5 firmware file `DDF.bin`
    * You should already have it on hand after initial upgrade to stock 1.1.5.
    * ⚠️ Always apply patch to **clean original** binary. ⚠️
        * Applying patch on top of previously patched binary _will_ result in glitches.
    * This mod will work **ONLY** with 1.1.5 download.
1. Back up the official 1.1.5 files.
    * DumboRC removes previous versions of firmware from their website. If you ever want to go back to some specific version, or if I am lagging behind on supported version, your only legitimate source of original files is your backup.
1. Download very good tool named LunarIPS [here](https://fusoya.eludevisibility.org/lips).
    * This is because I _cannot_ distribute official firmware, but I _can_ [distribute my rom hacks](https://en.wikipedia.org/wiki/ROM_hacking#Distribution).
1. Download the latest `.ips` file.
    * Visit [latest release](https://github.com/ELynx/ddf-350-modding/releases/latest)
    * Find "Assets" under text description
    * Download `.ips` file
1. Using LunarIPS apply my "Romhack" to clean fresh official 1.1.5 binary file.
    * LunarIPS modifies binary file "in place". Make sure to not override your backup.
    * Make sure you are applying it to the .bin file, and not the .zip.
    * Make sure you are applying it to the firmware file, and not any of the *boot* files.
    * If (when) you do not see the .bin file in LunarIPS, change the filter inside it to `all files / *.*`
1. Flash the modified binary file as described in official instruction. To summarize it here, purely for your convenience:
    * ⚠️ Take out batteries from your transmitter. ⚠️
    * Connect your transmitter to computer using USB cable _with data capabilities_.
       * ⚠️ It is **very** specific, not every cable will work. Try several until you find one.
    * Press and hold CH3 and CH4 buttons, then turn on the transmitter with power button.
    * Screen will flash "black", you will hear the chime. You can release the buttons now.
    * On your computer, you will see new USB flash drive appearing.
    * Run official .bat file to flash the image.
        * Manual copying does _not_ work, Windows creates "System Volume Information" and this throw process off. Official script takes care of that.
    * After bat file is complete, "Safe Eject" the flash drive.
    * Unplug the transmitter.
    * Plug the transmitter back, or insert batteries.
    * Turn transmitter on, new firmware fill flash automatically and you should see changes.
1. Enjoy! Drop a star on this repo, "watch" it for future updates. These numbers mean a lot to me, letting me know that I should not only to all this, but share with the community.
1. If this was useful, consider Ko-Fi or GitHub Sponsorship (one-time or monthly).

## Known limitations

1. Four NiMh 0% at 4.0V as is not optimal.
    * I aligned it with 4 AA and with lowest alarm voltage.
    * I suspect transmitter will not work below 4.0 volts anyway.
    * I suspect lowest value is set by bootloader to 4.1 volts, and I will *not* mess with bootloader (the part that makes transmitter start).

## Safety, warranty, responsibility

I provide no guarantees of safety and I am not responsible if you break something.

I do my best and test everything on my own only transmitter, so I have "skin in the game". But I cannot predict everything and every situation.

Just to keep it cool, do not do this day before important drives.

## How I did this, how I do this myself

### Translations

With a help of ChatGPT, I made some Python scripts to dump and insert UTF-8 strings. Of course, some are too short, some are not recognized and some are wrongly offset, but process is pretty smooth.

I highly recommend making a "translation" file, or modifying existing ones compared to changing raw binaries. You lose track of what is where quickly, and as I experience it with update, have to reinvent the wheel.

Current EN translation is 98% OK by me. DE translation is modified to get rid of scrolling, all your suggestions are welcome. I presume CN is very good. If you want to improve FR, make an issue, offer your help, we will work it out.

### Logic

With porting to 1.1.3 I finally started to publish my Ghidra projects publicly. With those, you can follow on my changes, or do yours, _collaboratively_.

It is still not Git-based, since Git replaces common server storage. As such, if you want to do something, let me know in the issues, I will make sure to upload my latest changes and take a break to allow your changes to pass.

You will need Ghidra. I use [Ghidra 11.2 Public](https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_11.2_build)

You will need to set up `./ghidra_repositories` folder of this repo as `ghidra.repositories.dir` in `server/server.conf`.

You will need to disable authentication in `server/server.conf`.

* Find `wrapper.app.parameter.1=-a0`, comment the line with `#`, change `.2` to `.1` on next parameter.

* For me it now looks like
```
#wrapper.app.parameter.1=-a0
wrapper.app.parameter.1=${ghidra.repositories.dir}
```

You can set up user name as `user.name` / `VMARGS=-Duser.name=` in `support/launch.properties`. Or by default your username is OS user name.

Add your username to `ghidra_repositories/users` of this repo, like `YourName:*:*`. I will be honored to not be alone there.

I run server in `console` mode, since I do not intend to use it as actual network server.

Once server is running, start Ghidra tool itself.

Click "File", "New project", "Shared Project", Server Name "127.0.0.1" (I presume you run server locally in console), "Existing Repository", "ddf-350-113".

Select folder to store files locally.

To start editing, RMB .bin file and do "Check Out".

After you did some changes and want to make a save, do "Check In...".

Once you are done want want to share changes back, do "Undo Checkout". Then close Ghidra, then stop Ghidra server with `Ctrl-C`.

After that commit all files in git, push.

To test the changes, export .bin file as "Raw Binary" to `translation` folder. If you want translations, use `input.bin`, otherwise just use `DDF.bin`.

To add translations to `input.bin` run `import_strings.py`.

Run `update.bat` that is just verbose translated official update script. Process is as usual.

If you flashed garbage, just flash working version again.

## Your translation is bad / your choice of words is bad / there is a better term

Works for me :3

Jokes aside, I am open to suggestions. My goal was to get rid of scrolling, because scrolling gave me perceivable headache. Plus couple of outdated terms that just need to go.

If you want to be helpful, look at the "Issues" page. Join existing issues there, or make a new one. Please add a *picture* of place you want to change, and clear writing you want to see there.

## Legals

I am not associated or affiliated with DUMBORC, RadioLink or other commercial companies.

They in no way or shape endorse this, or involved in this. Likewise, Transmitter and it's firmware are their property and distribution.

I only distribute my changes to firmware, and I do this because changes are done by me.
