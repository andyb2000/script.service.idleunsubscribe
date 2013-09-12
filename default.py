import xbmc,time, xbmcgui

# idle time in minutes
IDLE_TIME_MIN = 60
s = 1
while True:
	# do an initial sleep to let things settle first
	xbmc.sleep(5000)
	if (xbmc.Player().isPlaying()):
		# get idle time
		it = xbmc.getGlobalIdleTime()
		#calculate sleep time in msec
		s = ((IDLE_TIME_MIN * 60) - it ) * 1000
		# sleep for IDLE_TIME_MIN if playing
		if (xbmc.Player().isPlaying()): s = IDLE_TIME_MIN * 60 * 1000
		print("idleunsubscribe: Playback running, I'm going to idle for %d ms" % s)
		if (s > 0): xbmc.sleep(s)
		print("idleunsubscribe: back from sleep, display dialog")
		# xbmcgui.Dialog().ok("Idle Timer", "IDLE: Press a key on the remote to avoid sleep")
		xbmc.executebuiltin('Notification(Idle Timer,IDLE: Press a key on the remote to avoid sleep,20000)')
		# wait another 30 seconds to give them a chance
		it = xbmc.getGlobalIdleTime()
		print("idleunsubscribe: Checking first idletime %d " % it)
		ncount = 1
		while it > 20:
			xbmc.sleep(1000)
			it = xbmc.getGlobalIdleTime()
			print("idleunsubscribe: Checking for idletime %d " % it)
			if ncount > 30:
				break
			else:
				ncount += 1
		# gotham only
		#    if (s < 10000): yes = xbmcgui.Dialog().yesno("Idle Timer", "IDLE: Press a key on the remote to avoid sleep", autoclose = 30000)
		# unsubscribe
		print('idleunsubscribe: Stopping playback')
		xbmc.executebuiltin('PlayerControl(Stop)')
		print('idleunsubscribe: Playback stopped')
	else:
		xbmc.sleep(5000)
		print('idleunsubscribe: Loop without playback')
