#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 yuengdelahoz <yuengdelahoz@tensorbook>
#
# Distributed under terms of the MIT license.

"""

"""
import cv2
import traceback
import time

vs = cv2.VideoCapture(2)
# print(vs.getBackendName())
vs.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
ret1 =vs.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
ret2 =vs.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
ret = vs.set(cv2.CAP_PROP_EXPOSURE,100.0)
# gamma = vs.set(cv2.CAP_PROP_GAMMA,50.0)
print(ret)
# time.sleep(2)
# vs.set(3, 1920)
# vs.set(4, 1080)
# vs.set(cv2.CAP_PROP_FPS,20)
while True:
	try:
		ret, frame = vs.read()
		# print('FPS',vs.get(cv2.CAP_PROP_FPS))
		print('CAP_PROP_EXPOSURE',vs.get(cv2.CAP_PROP_EXPOSURE))
		print('GAMMA',vs.get(cv2.CAP_PROP_GAMMA))
		# if ret:
			# print(frame.shape)
		cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
		cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		cv2.imshow("window",frame)
		if cv2.waitKey(1) == ord('q'):
			cv2.destroyAllWindows()
			break
	except KeyboardInterrupt:
		cv2.destroyAllWindows()
		break
	except:
		traceback.print_exc()

