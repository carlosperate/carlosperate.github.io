Title: LightUp Alarm
Slug: LightUpPi-Alarm
page-order: 2
carousel: 1


This is a Clock Alarm System for the Raspberry Pi. It has sunrise lighting, coffee machine control, physical snooze button, and an Android companion app.

The system is made of two complementary projects:

**LightUpPi Alarm**: The Alarm system running on a Raspberry Pi. It controls all the hardware triggered for the alarm alert, and provides multiple ways to interface with the system (command line, web front and server back-end).

**LightUpDroid Alarm**: An Android alarm application that connects to the LightUpPi Alarm server to synchronise phone alarms. It is capable to keep and trigger its local alarms without a connection to the LightUpPi Alarm system.


## LightUpPi

It has been modularised into the following packages:

* __LightUpAlarm__: Completely independent Python package to manage alarms (create, edit, and delete alarms; can also run a callback on alarm alert).
* __LightUpHardware__: Controls external hardware to complement the alarm alert, in this case it controls the room lights, mains socket switch, and snooze functionality from a physical button.
* __LightUpServer__: Creates an HTTP server to interface with the LightUpAlarm system using a web interface or JSON (used in the LightUpDroid Android app).
* __LightUpWeb__: Front-end web interface for the LightUpServer. 

Additionally, an Android application can be used to interface with the LightUpPi Alarm system. For more information about this app please visit its repository: [LightUpDrop Alarm](http://github.com/carlosperate/LightUpDroid-Alarm)


### Installing LightUpPi Alarm

This application has been been develop to run a Raspberry Pi with Python 2.7. The project currently aims to maintain compatibility with Python 3. 

Install the dependencies described below. Then download this repository, by clicking [here][2] or running the following in the command line:

```
git clone git://github.com/carlosperate/LightUpPi-Alarm.git
```


#### Software Dependencies
You can see the project Python dependencies on the [requirements.txt][3] file.

More information about specific dependencies can be found in each package README:
* LightUpAlarm [README][4]
* LightUpServer [README][5]
* LightUpHardware [README][6]


### Hardware Dependencies
This project uses the following hardware in addition to the Raspberry Pi:
* [Pimoroni Unicorn Hat][8] for the lamp light
* [Belkin Wemo Switch][9] for the coffee machine control
* [Philips Hue][10] for the room light control

Note that the LightUpAlarm package can be used independently as an alarm system software and does not require any additional hardware to run.


### Running LightUpPi Alarm

There are two different ways to run LightUpPi Alarm:

1. Using the command line using, by launching the application with the `-c` flag:

    ```
    python main.py -c
    ```
    
    Instructions about how to use the CLI can be found in the LightUpAlarm package [README][4].
    
    <img src="http://carlosperate.github.com/LightUpPi-Alarm/images/screenshot_cli_1.png" alt="CLI interface" width="75%">

2. Using the web interface only, designed to run on a headless system, by launching the program with the `-s` flag:

    ```
    python main.py -s
    ```
    
    And then pointing your browser to the following adddress: ` http://raspberrypi.local/LightUpPi ` or using the [LightUpDroid][1] app.

    <img src="http://carlosperate.github.com/LightUpPi-Alarm/images/screenshot_web_1.png" alt="Web Interface" width="75%">


## LightUpDroid

This is an Android companion app for the [LightUpPi Alarm](http://github.com/carlosperate/LightUpPi-Alarm).

It is an Android alarm app that synchronizes to the alarms running in the `LightUpPi Alarm` Raspberry Pi system.

It is based on the [Alarm Clock](http://github.com/klinker41/alarm-clock) app by Jacob Klinker, which in turn is a modification of the official Android Open Source Project [DeskClock](http://android.googlesource.com/platform/packages/apps/DeskClock/) (updated for backwards compatibility).

<img src="http://raw.githubusercontent.com/carlosperate/LightUpDroid-Alarm/master/screenshots/clock.png" alt="Clock Screen" width="24%">
<img src="http://raw.githubusercontent.com/carlosperate/LightUpDroid-Alarm/master/screenshots/alarms.png" alt="Alarms Screen" width="24%">
<img src="http://raw.githubusercontent.com/carlosperate/LightUpDroid-Alarm/master/screenshots/timepicker.png" alt="Timepicker Screen" width="24%">
<img src="http://raw.githubusercontent.com/carlosperate/LightUpDroid-Alarm/master/screenshots/settings.png" alt="Settings Screen" width="24%">

## License

This project is licensed under The MIT License (MIT), a copy of which can be found in the [LICENSE][7] file.

[1]: http://github.com/carlosperate/LightUpDroid-Alarm
[2]: http://github.com/carlosperate/LightUpPi-Alarm/archive/master.zip
[3]: http://github.com/carlosperate/LightUpPi-Alarm/blob/master/requirements.txt
[4]: http://github.com/carlosperate/LightUpPi-Alarm/blob/master/LightUpAlarm/README.md
[5]: http://github.com/carlosperate/LightUpPi-Alarm/blob/master/LightUpServer/README.md
[6]: http://github.com/carlosperate/LightUpPi-Alarm/blob/master/LightUpHardware/README.md
[7]: http://raw.githubusercontent.com/carlosperate/LightUpPi-Alarm/master/LICENSE
[8]: http://shop.pimoroni.com/products/unicorn-hat
[9]: http://www.belkin.com/uk/p/P-F7C027/
[10]: http://www.philips.co.uk/c-p/8718291797098/hue-personal-wireless-lighting
