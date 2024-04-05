# Beverbord
# Lente van Haastrecht, Jasmijn Rodenburg, Tibbe Dinjens
#PO informatica 5VA periode 3 2024
import pygame, random, tkinter
import tkinter.messagebox


# -----------------Globale variabelen----------------

#coordinaten van de vakjes:
vakjes = [[135, 537], [230, 540], [278, 541], [323, 540], [371, 541], [414, 541],[468, 542], [517, 541], [566, 537], [616, 515], [658, 478], [690, 437], [707, 390], [719, 342], [721, 285], [713, 227], [695, 182], [670, 141],[624, 95], [559, 63], [504, 62], [455, 62], [412, 62], [365,62], [317, 61],[275, 63], [231, 64], [180, 85], [146, 112], [118, 149], [98, 190],[88, 242], [90, 299], [98, 350], [123, 389], [152, 428], [189, 457],[236, 469], [280, 471], [322, 471], [370, 470], [417, 468], [469, 470],[523, 469], [567, 462], [611, 423], [640, 371], [649, 323], [649, 273],[635, 228], [599, 176], [551, 143], [486, 141], [422, 137], [367, 137],[318, 137], [270, 137], [227, 144], [176, 191], [158, 270], [170, 328],[195, 367], [238, 388], [403, 295]]

#pion posities, beurt en worp op 0 zetten:
posities = [0,0]
beurt = 0
worp = 0

#bord afbeelding:
bord = pygame.image.load("canvas (1).png")

#-----------------Pygame initialisatie---------------

#pygame instaleren
pygame.init()

#afmetingen van het spelscherm instellen en het spelscherm maken
WINDOW_SIZE = [800,600]
screen = pygame.display.set_mode(WINDOW_SIZE)

#Titel van het spelscherm instellen:
pygame.display.set_caption("Beversbord")

#oneindige loop zodat het spel kan blijven lopen
done = False

#pygame Clock object om de verversingssnelheid van het scherm te beheren
clock = pygame.time.Clock()


#---------------Hoofdloop van het programma---------------------------

while not done:
  
  # --- Check gebeurtenissen en werk de admiraal bij ---
  
  for event in pygame.event.get(): 
    #doorloop alle gebeurtenissen sinds de vorige schermupdate
    
    if event.type == pygame.QUIT: #gebeurtenis: het kruisje is aangeklikt
      done = True #We zetten done op True, zodat de loop stopt
    elif event.type == pygame.KEYDOWN:
      #er is een toets ingedrukt, we kijken welke en ondernemen actie
      if event.key == pygame.K_SPACE: #spatie
        print ("Knop: Spatie")

        worp = random.randint(1,6) #Random getal tussen 1 en 6 als dobbelsteen

        posities[beurt] += worp #verzet de pion die aan de beurt is
        
        #Is de pion op een speciaal vakje? Dan doe iets...
        #vakje 1
        if posities[beurt] == 1 :
          tkinter.messagebox.showinfo("1 gegooid? :(", "aww arme jij, je mag 1 vakje vooruit als troost")
          posities[beurt] = 2 
        #vakje 5
        elif posities[beurt] == 5 :
          tkinter.messagebox.showinfo("oopsie-daisy", "Oh nee! Je stapt op een stapel losse boomstronken en je rolt helemaal door naar 10")
          posities[beurt] = 10
        #vakje 9
        elif posities[beurt] == 9:
          tkinter.messagebox.showinfo("pas op, otters", "Je ziet een pas op otters bord en wordt bang, ren terug naar vakje 3 :0")
          posities[beurt] = 3
        #vakje 38
        elif posities[beurt] == 38:
          tkinter.messagebox.showinfo("Auwie :(", "Je struikelt over een losse tak. Auw! Ga naar het ziekenhuis op vakje 34")
          posities[beurt] = 34
        #vakje 45
        elif posities[beurt] == 45 :
          tkinter.messagebox.showinfo("arm bevertje :/", "Je wordt aangevallen door een otter! Gelukkig heeft het beverdorp een goede therapeut. Hij zegt dat je een ronde moet overslaan voor een therapie sessie, na deze traumatische ervaring. Heb je al eerder therapie gevolgd? Ga dan ook een stap naar achter voor elke extra sessie")
          posities[beurt] = 44
        #vakje 57
        elif posities[beurt] == 57 :
          tkinter.messagebox.showinfo("OH NEE!!", " De dam is doorgebroken! Je wordt door het water terug gespoelt naar vakje 26")
          posities[beurt] = 26
        
        #pion voorbij het laatste vakje? Dan valt die van het bord af :/
        #Daarom moet ie precies op vakje 63 vallen:
        if posities[beurt] >= 63:
          posities[beurt] = 63
          #Nog niet gewonnen? geef beurt door aan de volgende speler:
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

  screen.fill((255,255,255))#witte achtergrond

  bordrect = bord.get_rect() #vraag afmetingen van het bordplaatje op
  screen.blit(bord, bordrect) #teken het bord op het volgende screen:

  #teken pionnen als gekleurde cirkels 
  speler0_x = vakjes[posities[0]][0]; #x-coordinaat pion speler 0
  speler0_y = vakjes[posities[0]][1]; #y-coordinaat pion speler 0
  kleur0 = (51, 51, 255) #blauw
  pygame.draw.circle(screen, kleur0, (speler0_x, speler0_y), 10) #speler 0
  
  speler1_x = vakjes[posities[1]][0]; #x-coordinaat pion speler 1
  speler1_y = vakjes[posities[1]][1]; #y-coordinaat pion speler 1
  kleur1 = (255, 26, 117) #echt mooie barbie roze
  pygame.draw.circle(screen, kleur1, (speler1_x, speler1_y), 10) #speler 1

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

  
  # --- Update de graphics voor de volgende schermupdate (nog buiten beeld) ---

  clock.tick(60) #zet de limiet op 60 frames per seconde
  pygame.display.flip() #ververst het beeldscherm


#--------------------Afsluiting----------------------
pygame.quit()#pygame en het gamevenster afsluiten