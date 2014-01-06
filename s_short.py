#!/usr/bin/env python
# coding=utf-8

import subprocess

from i3pystatus import Status, Module

class ShutdownButton(Module):
    output = {
        "full_text": "\uF3A9",
    }

    def on_leftclick(self):
        import subprocess
        subprocess.Popen(["dmenu_runstate"])

status = Status(standalone=True)

status.register("clock",
    format="%a %-d %b %X KW%V",)

status.register(ShutdownButton())

status.register("load")

status.register("backlight",
    format="{brightness}/{max_brightness}",)

status.register("temp",
    format="{temp:.0f}°C",)

status.register("regex", 
    regex="speed:\s+([0-9]+)\nlevel:\s+([a-zA-Z0-9]+)",
    file="/proc/acpi/ibm/fan",
    format="{0}",).move(1).move(2)

status.register("battery",
    format="{status}{percentage:.1f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    alert_format_body="",
    status={
        "DIS": "\uF215",
        "CHR": "\uF211",
        "FULL": "\uF213",
    },)

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

status.register(False, "disk",
    path="/",
    format="{used}/{total}G [{avail}G]",)

status.register("pulseaudio",
    format="{muted} {db} dB",
    muted="\uF026",
    unmuted="♪")

# That module contains a dict of parcels and a helper to register them, looks like that:
#
#from i3pystatus.parcel import DHL, UPS
#
#def register(status, **kwargs):
#    for name, tracker in items.items():
#        status.register("parcel",
#            instance=tracker,
#            name=name,
#            **kwargs
#        )
#
#items = {
#    "some_parcel": DHL("idnumber"),
#}

#import s_parcel
#s_parcel.register(status)

status.register("mpd",
    format="{title}{status}",
   status={
        "pause": "\uF04C",
        "play": "\uF04B",
        "stop": "\uF04D",
    },

status.register("weather",
    location_code="GMXX0051",
    format="\uF0C2 {current_temp} {humidity}%"))

status.run()
