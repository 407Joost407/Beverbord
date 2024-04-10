# Beverbord
# Lente van Haastrecht, Jasmijn Rodenburg, Tibbe Dinjens
# PO informatica 5VA periode 3 2024
import pygame, random, tkinter
import tkinter.messagebox

# -- Alle graphics voor het spel --
def graphics():
  screen.fill((255,255,255))#witte achtergrond

  bordrect = bord.get_rect() #afmetingen van het bordplaatje opvragen
  screen.blit(bord, bordrect) #teken het bord op het volgende screen:

  #teken pionnen als gekleurde cirkels op de coordinaten van de vakjes waar ze staan:
  speler0_x = vakjes[posities[0]][0]; #x-coordinaat pion speler 0
  speler0_y = vakjes[posities[0]][1]; #y-coordinaat pion speler 0
  kleur0 = (51, 51, 255) #blauw
  pygame.draw.circle(screen, kleur0, (speler0_x, speler0_y), 10) #teken speler 0

  speler1_x = vakjes[posities[1]][0]; #x-coordinaat pion speler 1
  speler1_y = vakjes[posities[1]][1]; #y-coordinaat pion speler 1
  kleur1 = (255, 26, 117) #echt mooie barbie roze
  pygame.draw.circle(screen, kleur1, (speler1_x, speler1_y), 10) #teken speler 1

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

#pion posities, beurt en worp op 0 zetten:
posities = [0,0]
beurt = 0

#dobbelsteenworp:
worp = 0   

#bord afbeelding:
bord = pygame.image.load("beverbord.png")

#Voor speciale vakjes:
beurtOverslaan = [False, False]
therapie = [0,0] 

#-----------------Pygame initialisatie---------------

#pygame instaleren
pygame.init()
pygame.mixer.init()

#afmetingen van het spelscherm instellen en het spelscherm maken
WINDOW_SIZE = [800,600]
screen = pygame.display.set_mode(WINDOW_SIZE)

#Titel van het spelscherm instellen:
pygame.display.set_caption("Beversbord")

#oneindige loop zodat het spel kan blijven lopen
done = False

#pygame Clock object om de verversingssnelheid van het scherm te beheren
clock = pygame.time.Clock()


#---------------Hoofdloop van het programma----------
top = tkinter.Tk()
top.withdraw()



while not done:
  # --- Graphics aanroepen ---
  graphics()
  # --- Check gebeurtenissen en werk de admiraal bij ---
  
  for event in pygame.event.get(): 
    #doorloop alle gebeurtenissen sinds de vorige schermupdate
    
    if event.type == pygame.QUIT: #gebeurtenis: het kruisje is aangeklikt
      answer = tkinter.messagebox.askyesno("Beverbord", "Weet je zeker dat je wilt stoppen?")
      if answer == True :
        done = True #We zetten done op True, zodat de loop stopt
    elif event.type == pygame.KEYDOWN:
      #er is een toets ingedrukt, we kijken welke en ondernemen actie
      if event.key == pygame.K_SPACE: #spatie
        print ("Knop: Spatie")
        graphics()
        if beurtOverslaan[beurt] == True:
          worp = 0
          beurtOverslaan[beurt] = False
        else:
          worp = random.randint(1,6) #Random getal als dobbelsteen
          posities[beurt] += worp #verzet de pion die aan de beurt is
          
        #Is de pion op een speciaal vakje? Dan doe iets...
        #Zelfde vakje als je tegenstander:
        
        if posities[0] == posities[1]:
          #battle
          tkinter.messagebox.showinfo("Battle","Je bent op hetzelfde vakje als je tegenspeler belandt. Gooien! Hoogste speler mag het vakje houden.")
          worp1 = random.randint(1,6) #aanvaller
          worp2 = random.randint(1,6) #verdediger
          print("speler", beurt + 1, "valt de andere speler aan met", worp1, "\nEr wordt verdedigt met", worp2)
          if worp1 <= worp2:
            posities[beurt] -= 1
          else:
            if beurt == 0:
              posities[1] -= 1
            else:
              posities[0] -= 1
          tkinter.messagebox.showinfo("Battle","De verliezer moet 1 vakje achteruit.")

        #Is de pion op een speciaal vakje? Dan doe iets...
        #vakje 1
        elif posities[beurt] == 1 :
          tkinter.messagebox.showinfo("1 gegooid? :(", "aww arme jij, je mag 1 vakje vooruit als troost")
          posities[beurt] = 2 
          print("vakje 1\n", "speler", beurt +1)
        #vakje 5
        elif posities[beurt] == 5 :
          tkinter.messagebox.showinfo("oopsie-daisy", "Oh nee! Je stapt op een stapel losse boomstronken en je rolt helemaal door naar 10")
          posities[beurt] = 10
          print("vakje 5\n", "speler", beurt +1)
        #vakje 9
        elif posities[beurt] == 9:
          tkinter.messagebox.showinfo("pas op, otters", "Je ziet een pas op otters bord en wordt bang, ren terug naar vakje 3 :0")
          posities[beurt] = 3
          print("vakje 9\n", "speler", beurt +1)
        #vakje 13
        elif posities[beurt] == 13:
          tkinter.messagebox.showinfo("ottergeluk","Met een beetje ottergeluk mag je naar nummer 13. Als je 3 gooit mag je er heen, anders komen de otters je terug naar de start slepen. Druk op ok om opnieuw te gooien.")
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
          print("vakje 13\n", "speler", beurt +1)
        #vakje 19
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
          print("vakje 19\n", "speler", beurt +1)
        #vakje 23
        elif posities[beurt] == 23: 
          tkinter.messagebox.showinfo("Paddenstoelen", "Je eet een paddenstoel, een magische paddenstoel. Het voelt alsof je in de wolken bent, of ben je dat ook. Als je weer bij bewustzijn bent sta je ineens op vakje 40, maar je was zo lang in de wolken dat je volgende beurt is vergaan.")
          beurtOverslaan[beurt] = True
          posities[beurt] = 40
          print("vakje 23\n", "speler", beurt +1)
        #vakje 32
        elif posities[beurt]== 32:

          tkinter.messagebox.showinfo("Otter uitdaging","Een groep tiener otters dagen je uit voor een potje dammen. Gooien! ")
          pygame.time.delay(3000)
          worps = random.randint(1,6)
          print(worps)
          if worps == 1 or 3 or 5:
            tkinter.messagebox.showinfo("oneven","Je hebt een oneven getal gegooit. Je hebt verloren, de otters lachen zo hard dat je stiekem een vakje vooruit kan gaan.")
            pygame.time.delay(3000)
            posities[beurt] += 1
          else:

            tkinter.messagebox.showinfo("even","Je hebt een even getal gegooit. Je hebt gewonnen, de otters kunnen niet tegen hun verlies en worden boos. Ga 1 vakje terug en verstop je in de bosjes.")
            pygame.time.delay(3000)
            posities[beurt] -= 1
          print("vakje 32\n", "speler", beurt +1)
        #vakje 38
        elif posities[beurt] == 38:
          tkinter.messagebox.showinfo("Auwie :(", "Je struikelt over een losse tak. Auw! Ga naar het ziekenhuis op vakje 34")
          posities[beurt] = 34
          print("vakje 38\n", "speler", beurt +1)
        #vakje 45
        elif posities[beurt] == 45 :
          tkinter.messagebox.showinfo("arm bevertje :/", "Je wordt aangevallen door een otter! Gelukkig heeft het beverdorp een goede therapeut. Hij zegt dat je een ronde moet overslaan voor een therapie sessie, na deze traumatische ervaring. Heb je al eerder therapie gevolgd? Ga dan ook een stap naar achter voor elke extra sessie")
          therapie[beurt] = therapie[beurt] + 1
          posities[beurt] -= therapie[beurt] - 1
          beurtOverslaan = True
          print("vakje 45\n", "speler", beurt +1)
        #vakje 57
        elif posities[beurt] == 57 :
          tkinter.messagebox.showinfo("OH NEE!!", " De dam is doorgebroken! Je wordt door het water terug gespoelt naar vakje 26")
          posities[beurt] = 26
          print("vakje 57\n", "speler", beurt +1)
        #vakje 58
        elif posities[beurt] == 58:
          tkinter.messagebox.showinfo("Dammen", "Je bent tussen twee dammen ingevallen. De klim naar boven zal je je volgende beurt kosten.")
          beurtOverslaan[beurt] = True
          print("vakje 58\n", "speler", beurt +1)

        
        #pion moet precies op vakje 63 vallen:
        if posities[beurt] >= 63:
          posities[beurt] = 63
          tkinter.messagebox.showinfo("WHOOO", "GEWONNEN, JA HOOR WE HEBBEN EEN WINNAAR! GEFELICITEERD! DIE OTTERS ZULLEN ONS NOOIT VERSLAAN! :)") 
          done = True
        elif worp == 6 :
          tkinter.messagebox.showinfo("6", "Lets gooo je hebt 6 gegooiddd, nu mag je nog een keer gooien")
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



  
  #deze staan in functie bovenaan de code
  
  # --- Update de graphics voor de volgende schermupdate (nog buiten beeld) ---

  clock.tick(60) #zet de limiet op 60 frames per seconde
  pygame.display.flip() #ververst het beeldscherm


#--------------------Afsluiting----------------------
pygame.quit()#pygame en het gamevenster afsluiten