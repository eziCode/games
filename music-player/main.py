import pygame
from pygame import mixer
import sys
pygame.init()
pygame.mixer.init()

display = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Meme Soundboard')
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0
count21 = 0
count22 = 0
count23 = 0
count24 = 0
count25 = 0
count26 = 0

programIteration = 1

with open("MusicLog.txt", 'w') as MusicLog:
    MusicLog.write(str(programIteration) + ' Program Run')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    mixer.music.load('anime-wow-sound-effect-mp3cut.mp3')
                    mixer.music.play(-1)
                    count1 += 1
                    if count1 > 1:
                        MusicLog.write('\nThis is my ' + str(count1) + ' time playing the anime wow sound.')
                    else:
                        MusicLog.write('\nJust played anime wow sound effect.\n')
                elif event.key == pygame.K_a:
                    mixer.music.load('daequan-come-here-boy-sound-effect.mp3')
                    mixer.music.play(-1)
                    count2 += 1
                    if count2 > 1:
                        MusicLog.write('\nThis is my ' + str(count2) + ' time playing the daequan sound.')
                    else:
                        MusicLog.write('\nJust played a daequan classic.\n')
                elif event.key == pygame.K_z:
                    mixer.music.load('emotional-damage-meme.mp3')
                    mixer.music.play(-1)
                    count3 += 1
                    if count3 > 1:
                        MusicLog.write('\nThis is my ' + str(count3) + ' time playing the emotional damage sound.')
                    else:
                        MusicLog.write('\nJust played an iconic sound.\n')
                elif event.key == pygame.K_w:
                    mixer.music.load('error_CDOxCYm (1).mp3')
                    mixer.music.play(-1)
                    count4 += 1
                    if count4 > 1:
                        MusicLog.write('\nThis is my ' + str(count4) + ' time playing the error sound.')
                    else:
                        MusicLog.write('\nJust played an error sound.\n')
                elif event.key == pygame.K_s:
                    mixer.music.load('fail-sound-effect.mp3')
                    mixer.music.play(-1)
                    count5 += 1
                    if count5 > 1:
                        MusicLog.write('\nThis is my ' + str(count5) + ' time playing the fail sound.')
                    else:
                        MusicLog.write('\nJust played a fail sound.\n')
                elif event.key == pygame.K_x:
                    mixer.music.load('fart-meme-sound.mp3')
                    mixer.music.play(-1)
                    count6 += 1
                    if count6 > 1:
                        MusicLog.write('\nThis is my ' + str(count6) + ' time playing the fart sound.')
                    else:
                        MusicLog.write('\nJust played a great fart sound.\n')
                elif event.key == pygame.K_e:
                    mixer.music.load('fbi-open-up_dwLhIFf.mp3')
                    mixer.music.play(-1)
                    count7 += 1
                    if count7 > 1:
                        MusicLog.write('\nThis is my ' + str(count7) + ' time playing the fbi open up sound.')
                    else:
                        MusicLog.write('\nThe FBI is here, you better open up.\n')
                elif event.key == pygame.K_d:
                    mixer.music.load('french-meme-song.mp3')
                    mixer.music.play(-1)
                    count8 += 1
                    if count8 > 1:
                        MusicLog.write('\nThis is my ' + str(count8) + ' time playing the relaxing french song.')
                    else:
                        MusicLog.write('\nWho doesn\'t want to listen to french music.\n')
                elif event.key == pygame.K_c:
                    mixer.music.load('gta-san-andreas-ah-shit-here-we-go-again_BWv0Gvc (1).mp3')
                    mixer.music.play(-1)
                    count9 += 1
                    if count9 > 1:
                        MusicLog.write('\nThis is my ' + str(count9) + ' time playing the GTA sound.')
                    else:
                        MusicLog.write('\nWhat fantastic sound effects GTA makes.\n')
                elif event.key == pygame.K_r:
                    mixer.music.load('man-beatboxing-meme-online-audio-converter.mp3')
                    mixer.music.play(-1)
                    count10 += 1
                    if count10 > 1:
                        MusicLog.write('\nThis is my ' + str(count10) + ' time playing the beatboxing sound.')
                    else:
                        MusicLog.write('\nBeatboxing is such a pleasant sound.\n')
                elif event.key == pygame.K_f:
                    mixer.music.load('meme-de-creditos-finales (1).mp3')
                    mixer.music.play(-1)
                    count11 += 1
                    if count11 > 1:
                        MusicLog.write('\nThis is my ' + str(count11) + ' time playing the fail music sound.')
                    else:
                        MusicLog.write('\nWhat an OG sound this is.\n')
                elif event.key == pygame.K_v:
                    mixer.music.load('meme-okay-lets-go.mp3')
                    mixer.music.play(-1)
                    count12 += 1
                    if count12 > 1:
                        MusicLog.write('\nThis is my ' + str(count12) + ' time playing OK lets go sound.')
                    else:
                        MusicLog.write('\nNothing beats this.\n')
                elif event.key == pygame.K_t:
                    mixer.music.load('movie_1_C2K5NH0.mp3')
                    mixer.music.play(-1)
                    count13 += 1
                    if count13 > 1:
                        MusicLog.write('\nThis is my ' + str(count13) + ' time playing the BRUH sound.')
                    else:
                        MusicLog.write('\nBRUH!\n')
                elif event.key == pygame.K_g:
                    mixer.music.load('my-movie-6_0RlWMvM (1).mp3')
                    mixer.music.play(-1)
                    count14 += 1
                    if count14 > 1:
                        MusicLog.write('\nThis is my ' + str(count14) + ' time playing the Russia music sound.')
                    else:
                        MusicLog.write('\nRussian music can not be beat.\n')
                elif event.key == pygame.K_b:
                    mixer.music.load('run-vine-sound-effect.mp3')
                    mixer.music.play(-1)
                    count15 += 1
                    if count15 > 1:
                        MusicLog.write('\nThis is my ' + str(count15) + ' time playing run sound.')
                    else:
                        MusicLog.write('\nYou better run.\n')
                elif event.key == pygame.K_y:
                    mixer.music.load('slumber-that-brother-gone-meme_pXziXJ1.mp3')
                    mixer.music.play(-1)
                    count16 += 1
                    if count16 > 1:
                        MusicLog.write('\nThis is my ' + str(count16) + ' time playing the \'that brother falling\' sound.')
                    else:
                        MusicLog.write('\n\'That brother falling\'. How iconic!\n')
                elif event.key == pygame.K_h:
                    mixer.music.load('spiderman-meme-song.mp3')
                    mixer.music.play(-1)
                    count17 += 1
                    if count17 > 1:
                        MusicLog.write('\nThis is my ' + str(count17) + ' time playing the Spiderman sound.')
                    else:
                        MusicLog.write('\nWho doesn\'t love spiderman?!\n')
                elif event.key == pygame.K_n:
                    mixer.music.load('steve-old-hurt-sound_XKZxUk4.mp3')
                    mixer.music.play(-1)
                    count18 += 1
                    if count18 > 1:
                        MusicLog.write('\nThis is my ' + str(count18) + ' time playing the minecraft injury sound.')
                    else:
                        MusicLog.write('\nMinecraft makes such great sound effects.\n')
                elif event.key == pygame.K_u:
                    mixer.music.load('tf_nemesis (1).mp3')
                    mixer.music.play(-1)
                    count19 += 1
                    if count19 > 1:
                        MusicLog.write('\nThis is my ' + str(count19) + ' time playing the sad music sound.')
                    else:
                        MusicLog.write('\nThis sound is just so sad ;(\n')
                elif event.key == pygame.K_j:
                    mixer.music.load('they-ask-you-how-you-are-and-you-just-have-to-say-that-youre-fine-sound-effect_IgYM1CV (1).mp3')
                    mixer.music.play(-1)
                    count20 += 1
                    if count20 > 1:
                        MusicLog.write('\nThis is my ' + str(count20) + ' time playing the Kardashian sound.')
                    else:
                        MusicLog.write('\nThe Kardashians never cease to make great meme sounds.\n')
                elif event.key == pygame.K_m:
                    mixer.music.load('tmpbxydyrz3.mp3')
                    mixer.music.play(-1)
                    count21 += 1
                    if count21 > 1:
                        MusicLog.write('\nThis is my ' + str(count21) + ' time playing the Snoop Dogg sound.')
                    else:
                        MusicLog.write('\nSnoop Dogg: He smokes a lot and makes great beats.\n')
                elif event.key == pygame.K_i:
                    mixer.music.load('vine-boom-sound-effect_KT89XIq.mp3')
                    mixer.music.play(-1)
                    count22 += 1
                    if count22 > 1:
                        MusicLog.write('\nThis is my ' + str(count22) + ' time playing the boom sound.')
                    else:
                        MusicLog.write('\nBoom!\n')
                elif event.key == pygame.K_k:
                    mixer.music.load('what-are-you-doing-in-my-swamp- (1).mp3')
                    mixer.music.play(-1)
                    count23 += 1
                    if count23 > 1:
                        MusicLog.write('\nThis is my ' + str(count23) + ' time playing the Shrek sound.')
                    else:
                        MusicLog.write('\nHow can anybody hate Shrek?\n')
                elif event.key == pygame.K_o:
                    mixer.music.load('windows-xp-startup_1ph012N.mp3')
                    mixer.music.play(-1)
                    count24 += 1
                    if count24 > 1:
                        MusicLog.write('\nThis is my ' + str(count24) + ' time playing the windows startup sound.')
                    else:
                        MusicLog.write('\nWhat an OG sound\n')
                elif event.key == pygame.K_l:
                    mixer.music.load('y2mate-mp3cut_sRzY6rh (1).mp3')
                    mixer.music.play(-1)
                    count25 += 1
                    if count25 > 1:
                        MusicLog.write('\nThis is my ' + str(count25) + ' time playing the coffin dance song.')
                    else:
                        MusicLog.write('\nThis sound even makes funerals fun\n')
                elif event.key == pygame.K_p:
                    mixer.music.load('y2mate_5gbydy1.mp3')
                    mixer.music.play(-1)
                    count26 += 1
                    if count26 > 1:
                        MusicLog.write('\nThis is my ' + str(count26) + ' time playing the screaming man sound.')
                    else:
                        MusicLog.write('\nThere is nothing better than a screaming man.\n')

            if event.type == pygame.KEYUP:
                pygame.mixer.music.stop()
