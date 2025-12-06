from astral.sun import sun
from astral import LocationInfo
import time
import pygame
import datetime

city = LocationInfo("Ankara", "Turkey", "Europe/Istanbul", 39.9334, 32.8597)
sun = sun(city.observer, date=datetime.date.today(), tzinfo=city.timezone)
sunrise = sun['sunrise'].strftime("%H:%M:%S")

music="Time.mp3"
Date= True
print(f"Sunrise: {sunrise}")
repeat="y"
while repeat == "y":
    while Date:
        clock=datetime.datetime.now().strftime("%H:%M:%S")
        print(clock)
        if sunrise == clock:
            print("Wake Up")
            pygame.mixer.init()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()
            Temp=0
            while Temp!=30:
                print(f"{30 - Temp} seconds for the music to stop")
                time.sleep(1)
                Temp=Temp+1
            pygame.mixer.music.stop()
            Date = False
        time.sleep(1)
    repeat="a"
    while repeat != "n" and repeat != "y":
        repeat=input("Would you like to play again? (y/n)")
        repeat=repeat.lower()
        if repeat != "y" and repeat != "n":
            print("Please enter either 'y' or 'n'")
        if repeat == "y":
            Date = True

print("Goodbye")
