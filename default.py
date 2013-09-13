import xbmc, time, xbmcgui, xbmcaddon

# idle time in minutes
settings = xbmcaddon.Addon(id='script.service.idleunsubscribe')
IDLE_TIME_MIN = int(settings.getSetting("idletime"))
print("idleunsubscribe: Loaded idletime from settings: %d" % IDLE_TIME_MIN)
if not IDLE_TIME_MIN: IDLE_TIME_MIN = 60
s = 1
while True:
	# do an initial sleep to let things settle first
	xbmc.sleep(5000)
	if (xbmc.Player().isPlaying()):
		# get idle time
		it = xbmc.getGlobalIdleTime()
		s = IDLE_TIME_MIN * 60 * 1000
		print("idleunsubscribe: Playback running, I'm going to idle for %d ms" % s)
		timer = 0
		while timer < s:
			print("idleunsubscribe: count %d ms < %d ms" % (timer, s))
			it = xbmc.getGlobalIdleTime()
			if (xbmc.Player().isPlaying()):
				print("idleunsubscribe: Playback still taking place")
				if (it < 3):
					print("idleunsubscribe: Idle timer less than 3 seconds (%d), reset timer" % it)
					xbmc.sleep(5000)
					timer = 0
				else:
					print("idleunsubscribe: Idle timer greater than 60 seconds")
			else:
				print("idleunsubscribe: Player no longer playing, break called")
				break
			xbmc.sleep(1000)
			timer += 1000

		if (xbmc.Player().isPlaying()):
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
			# unsubscribe
			print('idleunsubscribe: Stopping playback')
			xbmc.executebuiltin('PlayerControl(Stop)')
			print('idleunsubscribe: Playback stopped')
	else:
		xbmc.sleep(5000)
		print('idleunsubscribe: Loop without playback')
