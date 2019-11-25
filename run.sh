#! /bin/sh
#
# run.sh
# Copyright (C) 2019 yuengdelahoz <yuengdelahoz@tensorbook>
#
# Distributed under terms of the MIT license.
#


#v4l2-ctl -v width=1920,height=1080,pixelformat=BGR3
v4l2-ctl --set-fmt-video=width=1920,height=1080,pixelformat=YUYV
python3 visualizer.py
