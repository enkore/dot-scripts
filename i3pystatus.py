#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

from . import Status

status = Status(standalone=True)

status.register("clock",
    format="%a %-d %b %X KW%V",)

status.register("load")

status.register("backlight",
    format="{brightness}/{max_brightness}",)

status.register("temp",
    format="{temp:.0f}°C",)

# Fan speed
status.register("regex",
    regex="speed:\s+([0-9]+)\nlevel:\s+([a-zA-Z0-9]+)",
    file="/proc/acpi/ibm/fan",
    format="{0}",).move(1).move(2)

status.register("battery",
#    format="{status}/{consumption:.2f}W {percentage:.2f}% [{percentage_design:.2f}%] {remaining_hm}",
#     format="{status} {percentage:.1f}% {percentage_design:.1f}% {remaining_hm}",
    format="{status}{percentage:.1f}% {remaining_hm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    },)

status.register("runwatch",
    name="DHCP",
    path="/var/run/dhclient*.pid",)

status.register("network",
    interface="eth0",
    format_up="{v4cidr}",)

status.register("wireless",
    interface="wlan0",
    format_up="{essid} {quality:03.0f}%",)

# It's never full anyway, so I don't need that ATM
status.register(False, "disk",
    path="/",
    format="{used}/{total}G [{avail}G]",)

status.register("pulseaudio",
    format="♪{volume}",)

status.register("mpd",
    format="{title}{status}{album}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },)

from i3pystatus.parcel import DHL, UPS

#status.register("parcel",
#    instance=DHL("04681615604503"),
#    name="cam",)

status.run()
