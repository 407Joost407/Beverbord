# Ganzenbord - Tibbe Dinjens
import pygame, random, time, tkinter
import tkinter.messagebox
# from tkinter import messagebox

def graphics():
  screen.fill((255,255,255))#witte achtergrond

  bordrect = bord.get_rect() #vraag afmetingen (rectangle) van het bordplaatje op
  screen.blit(bord, bordrect) #teken het bord op het volgende screen:

  #teken pionnen als gekleurde cirkels op de coordinaten van de vakjes waar ze staan:
  speler0_x = vakjes[posities[0]][0]; #x-coordinaat pion speler 0
  speler0_y = vakjes[posities[0]][1]; #y-coordinaat pion speler 0
  kleur0 = (51, 51, 255) #blauw
  pygame.draw.circle(screen, kleur0, (speler0_x, speler0_y), 10) #teken cirkel als pion speler 0

  speler1_x = vakjes[posities[1]][0]; #x-coordinaat pion speler 1
  speler1_y = vakjes[posities[1]][1]; #y-coordinaat pion speler 1
  kleur1 = (255, 26, 117) #echt mooie barbie roze
  pygame.draw.circle(screen, kleur1, (speler1_x, speler1_y), 10) #teken cirkel als pion speler 1\

  #we tekenen wat tekst op het scherm
  #Kies het standaardfont en een lettergrootte (30):
  myfont = pygame.font.SysFont(None, 30)

  #teken de laatste worp op het scherm:
  text = "Laatste worp: " + str(worp)
  label = myfont.render(text,1, (0,0,0))
  screen.blit(label, (350,365))

  #teken de speler die aan de beurt is op het scherm:
  text = "Aan de beurt: " + str(beurt + 1)
  label = myfont.render(text,1, (0,0,0))
  screen.blit(label, (350,390))
# -----------------Globale variabelen----------------

#coordinaten van de vakjes:
vakjes = [[135, 537], [230, 540], [278, 541], [323, 540], [371, 541], [414, 541],[468, 542], [517, 541], [566, 537], [616, 515], [658, 478], [690, 437], [707, 390], [719, 342], [721, 285], [713, 227], [695, 182], [670, 141],[624, 95], [559, 63], [504, 62], [455, 62], [412, 62], [365,62], [317, 61],[275, 63], [231, 64], [180, 85], [146, 112], [118, 149], [98, 190],[88, 242], [90, 299], [98, 350], [123, 389], [152, 428], [189, 457],[236, 469], [280, 471], [322, 471], [370, 470], [417, 468], [469, 470],[523, 469], [567, 462], [611, 423], [640, 371], [649, 323], [649, 273],[635, 228], [599, 176], [551, 143], [486, 141], [422, 137], [367, 137],[318, 137], [270, 137], [227, 144], [176, 191], [158, 270], [170, 328],[195, 367], [238, 388], [403, 295]]

#pion posities
posities = [0,0]

#wie is aan de beurt?
beurt = 0

#dobbelsteenworp:
worp = 0   
#bord afbeelding:
bord = pygame.image.load("canvas (1).png")

#-----------------Pygame initialisatie---------------

#pygame instaleren
pygame.init()

#afmetingen van het spelscherm instellen (in pixels [breedte, hoogte])
#daarna het spelscherm maken (en opslaan in een variabele screen)
WINDOW_SIZE = [800,600]
screen = pygame.display.set_mode(WINDOW_SIZE)

#Titel van het spelscherm instellen:
pygame.display.set_caption("Beversbord")

#oneindige loop zodat het spel blijft lopen totdat er op het kruisje
#geklikt wordt om af te sluiten. (deze zet dan done op True)
done = False

#pygame Clock object die nodig is om de verversingssnelheid 
#(framerate) van het scherm te beheren
clock = pygame.time.Clock()


#---------------Hoofdloop van het programma----------
top = tkinter.Tk()
top.withdraw()
while not done:
  
  # --- Check gebeurtenissen (zoals muiskliks) en werk de admiraal bij ---
  
  for event in pygame.event.get(): #doorloop alle gebeurtenissen sinds de vorige schermupdate
    
    if event.type == pygame.QUIT: #gebeurtenis: het kruisje is aangeklikt
      done = True #het spel moet eindigen dus we zetten done op True, zodat de loop straks stopt
    elif event.type == pygame.KEYDOWN:
      #er is een toets ingedrukt, we kijken welke en ondernemen actie
      if event.key == pygame.K_SPACE: #spatie
        print ("Knop: Spatie")

        worp = random.randint(1,6) #Random getal tussen 1 en 6 als dobbelsteen
        posities[beurt] += worp #verzet de pion die op dit moment aan de beurt is
        if posities[beurt] == 13:
          tkinter.messagebox.showinfo("ottergeluk","Je staat nu op nummer 13, dit is een ongeluksgetal. De otters komen je terug naar de start slepen als je geen drie gooit. Druk op ok om opnieuw te gooien.")
          pygame.time.delay(3000)
          worps = random.randint(1,6)
          if worps == 3:
            tkinter.messagebox.showinfo("3 gegooit","Je hebt 3 gegooit en bent de otters net ontsnapt. Je mag blijven staan.")
            pygame.time.delay(3000)
            posities[beurt] += 0
          else:
            tkinter.messagebox.showinfo("geen 3 gegooit","AH OH, je hebt geen 3 gegooit de otters slepen je helemaal terug naar de start.")
            pygame.time.delay(3000)
            posities[beurt] -= 13
        elif posities[beurt] == 19:
          
          tkinter.messagebox.showinfo("dam"," Damn. Je bent een dam tegengekomen. Als je 6 gooit, mag je de dam over en mag je naar vakje 51")
          pygame.time.delay(3000)
          worps = random.randint(1,6)
          if worps == 6:
            
            tkinter.messagebox.showinfo("6 gegooit","Hoera je hebt 6 gegooit je kan nu over de dam helemaal naar vakje 51.")
            pygame.time.delay(3000)
            posities[beurt] += 32
          else:
            
            tkinter.messagebox.showinfo("geen 6 gegooit","Womp Womp, je hebt geen 6 gegooit. Je mag dus niet over de dam heen en blijft staan op vakje 19.")
            pygame.time.delay(3000)
            posities[beurt] += 0
        elif posities[beurt]== 32:
          
          tkinter.messagebox.showinfo("Otter uitdaging","Een groep kinder otters dagen je uit voor een potje dammen. Gooien! ")
          pygame.time.delay(3000)
          worps = random.randint(1,6)
          print(worps)
          if worps == 1 or 3 or 5:
            tkinter.messagebox.showinfo("oneven","Je hebt een oneven getal gegooit. Je hebt verloren, de otters lachen zo hard dat je stiekem een vakje vooruit kan gaan")
            pygame.time.delay(3000)
            posities[beurt] +=1
          else:
            
            tkinter.messagebox.showinfo("even","Je hebt een even getal gegooit. Je hebt gewonnen, de otters kunnen niet tegen hun verlies en worden boos. Ga 1 vakje terug en verstop je in de bosjes.")
            pygame.time.delay(3000)
            posities[beurt] -=1
        #pion voorbij het laatste vakje? Dan valt die van het bord af :/
        #Daarom moet ie precies op vakje 63 vallen:
        if posities[beurt] >= 63:
          posities[beurt] = 63
        #heeft de speler nog niet gewonnen? geef dan de beurt door aan de volgende speler
        else:
            
          if beurt == 0:
            beurt = 1
          else:
            beurt = 0
        
  
      elif event.key == pygame.K_BACKSPACE: #backspace
        print("Knop: Backspace")
        #om een nieuw spel te starten, moeten de spelerposities weer op 0 zetten.
        #En we geven de beurt weer aan speler 0.
        beurt = 0
        posities = [0,0]

  # --- Teken de graphics voor de volgende schermupdate (nog buiten beeld) ---

  graphics()

  
  # --- Update de graphics voor de volgende schermupdate (nog buiten beeld) ---

  clock.tick(60) #zet de limiet op 60 frames per seconde
  pygame.display.flip() #ververst het beeldscherm


#--------------------Afsluiting----------------------
pygame.quit()#pygame en het gamevenster afsluiten