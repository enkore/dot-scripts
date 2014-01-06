#!/usr/bin/env python
# coding=utf-8

import subprocess
import os
import os.path

from i3pystatus import Status, IntervalModule, Module

status = Status(standalone=True)

class RestartReminder(IntervalModule):
    settings = required = ()

    def run(self):
        if os.path.exists("/lib/modules/" + os.uname().release):
            self.output = None
        else:
            self.output = {
                "full_text": "\uF201 Reboot required!",
                "color": "#FF0000",
            }

class ShutdownButton(Module):
    output = {
        "full_text": "\uF3A9",
    }

    def on_leftclick(self):
        import subprocess
        subprocess.Popen(["dmenu_runstate"])

status.register("clock",
    format="%a %-d %b %X KW%V",)

status.register(ShutdownButton())

status.register(RestartReminder())

status.register("load",
    format="{avg1} {avg5} {avg15}")

status.register("backlight",
    format="{brightness}/{max_brightness}",)

status.register("temp",
    format="{temp:.0f}°C",)

status.register("regex", 
    regex="speed:\s+([0-9]+)\nlevel:\s+([a-zA-Z0-9]+)",
    file="/proc/acpi/ibm/fan",
    format="{0}",).move(1).move(2)

status.register("battery",
    format="{status}[ with {consumption:.2f}W] {percentage:.2f}% [{percentage_design:.2f}%] {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "CHR": "Charging",
        "DIS": "Discharging",
        "FULL": "Battery full",
    })

status.register("runwatch",
    name="DHCP",
    path="/var/run/dhclient*.pid",)

status.register("network",
    interface="eth0",
    format_up="\uF0E8 eth0: {v4cidr}",
    format_down="\uF0E8")

status.register("wireless",
    interface="wlan0",
    format_up="\uF35C {essid} {quality:03.0f}%",
    format_down="\uF35C")

status.register("disk",
    path="/",
    format="{used}/{total}G → {avail}G",)

status.register("mem",
    format="{used_mem}/{total_mem}M [{percent_used_mem}%]")

status.register("pulseaudio",
    format="{muted} {db} dB",
    muted="\uF026",
    unmuted="♪")

status.register("mpd",
    format="{status} [{artist} / {album} / ]{title}[ {song_elapsed:%l %m:%S}[/{song_length:%m:%S}]]",
    status={
        "pause": "\uF04C",
        "play": "\uF04B",
        "stop": "\uF04D",
    },)

status.register("weather",
    location_code="GMXX0051",
    format="\uF0C2 {current_temp} {humidity}%")

# See s_short.py
import s_parcel
s_parcel.register(status)

status.run()
