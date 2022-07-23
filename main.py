import datetime
import pyglet
from time import sleep

# time_now = datetime.datetime.now()
music = pyglet.resource.media('music.mp3')
print('день')
day = input()
print('час')
hour = input()
print('минуты')
minutes = input()
while True:
    time_now = datetime.datetime.now()
    if str(time_now.hour)==hour and str(time_now.minute)==minutes and str(time_now.day)==day:23
        music.play()
        break
    sleep(1)
pyglet.app.run()
