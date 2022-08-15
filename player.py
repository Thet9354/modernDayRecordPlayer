#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.IN)

DEVICE_ID="YOUR_DEVICE_ID"
CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"

while True:
  
  musicUrl = " "
  
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id=='555341117139'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:5W3UniuRMkHHIpaiQo1hAW'])
                sleep(2)
                musicUrl = "spotify:track:5W3UniuRMkHHIpaiQo1hAW"
                sleep(2)
                if(musicUrl == "spotify:track:5W3UniuRMkHHIpaiQo1hAW"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                
            elif (id=='969050486368'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4IO8X9W69dIQe0EC5ALXhq'])
                sleep(2)
                musicUrl = "spotify:track:4IO8X9W69dIQe0EC5ALXhq"
                sleep(2)
                if(musicUrl == "spotify:track:4IO8X9W69dIQe0EC5ALXhq"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                    
            elif (id=='692528477827'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:VaLvJ0RenpXUIAC52d'])
                sleep(2)
                musicUrl = "spotify:track:VaLvJ0RenpXUIAC52d"
                sleep(2)
                if(musicUrl == "spotify:track:VaLvJ0RenpXUIAC52d"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                    
            elif (id=='14438276707'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1fewSx2d5KIZ04wsooEBOz'])
                sleep(2)
                musicUrl = "spotify:track:1fewSx2d5KIZ04wsooEBOz"
                sleep(2)
                if(musicUrl == "spotify:track:1fewSx2d5KIZ04wsooEBOz"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                    
           elif (id=='556784023100'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3F5CgOj3wFlRv51JsHbxhe'])
                sleep(2)
                musicUrl = "spotify:track:3F5CgOj3wFlRv51JsHbxhe"
                sleep(2)
                if(musicUrl == "spotify:track:3F5CgOj3wFlRv51JsHbxhe"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                    
          elif (id=='692880865007'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:22I3h5AOENlH4CqXJsEbFR'])
                sleep(2)
                musicUrl = "spotify:track:22I3h5AOENlH4CqXJsEbFR"
                sleep(2)
                if(musicUrl == "spotify:track:22I3h5AOENlH4CqXJsEbFR"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                    
          elif (id=='419630347982'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4PhsKqMdgMEUSstTDAmMpg'])
                sleep(2)
                musicUrl = "spotify:track:4PhsKqMdgMEUSstTDAmMpg"
                sleep(2)
                if(musicUrl == "spotify:track:4PhsKqMdgMEUSstTDAmMpg"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                    
          elif (id=='418305013272'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1Bqxj0aH5KewYHKUg1IdrF'])
                sleep(2)
                musicUrl = "spotify:track:1Bqxj0aH5KewYHKUg1IdrF"
                sleep(2)
                if(musicUrl == "spotify:track:1Bqxj0aH5KewYHKUg1IdrF"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                    
           elif (id=='213790750442'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1cKHdTo9u0ZymJdPGSh6nq'])
                sleep(2)
                musicUrl = "spotify:track:1cKHdTo9u0ZymJdPGSh6nq"
                sleep(2)
                if(musicUrl == "spotify:track:1cKHdTo9u0ZymJdPGSh6nq"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)
                    
           elif (id=='1037099136668'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3JsydWaf2Ev4ehaLUjj3SY'])
                sleep(2)
                musicUrl = "spotify:track:3JsydWaf2Ev4ehaLUjj3SY"
                sleep(2)
                if(musicUrl == "spotify:track:3JsydWaf2Ev4ehaLUjj3SY"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID) 
                    
           elif (id=='1046529771865'):
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3yWF3DqFBNLvf7s4C7mKUm'])
                sleep(2)
                musicUrl = "spotify:track:3yWF3DqFBNLvf7s4C7mKUm"
                sleep(2)
                if(musicUrl == "spotify:track:3yWF3DqFBNLvf7s4C7mKUm"):
                  while (GPIO.input(16) == False):
                    print("Continue")
                  else:
                    print("Pausing Music")
                    sp.pause_playback(device_id=DEVICE_ID)         
                
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
