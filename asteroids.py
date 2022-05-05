import pyglet

window_width = 1000
window_height = 1000

# nastaveni okna
window = pyglet.window.Window(width = window_width, height = window_height)

# nacteni obrazku a ulozeni do promenne img
img = pyglet.image.load('spaceship2.png')



# definice tridy Spaceship a jejich metod
class Spaceship:
    # pri inicializaci objektu mu jako atribut "sprite" nastavim pyglet.sprite obrazek, se kterym budu pomoci metod manipulovat
    def __init__(self, image):
        self.sprite = pyglet.sprite.Sprite(image)

    # metoda pro ovladani lodi
    def tick(self, t):
        self.sprite.x = self.sprite.x + t
        self.sprite.y = self.sprite.y + t
        #print(self, t)

    # metoda pro vykresleni
    def draw(self):
        window.clear()
        self.sprite.draw()

#    def process_keys(text):
#        print(text)

 
    
# vytvoreni objektu "spaceship" tridy Spaceship
spaceship_tonik = Spaceship(img)



# kazdou 1/30 vteriny volam metodu tick a dava ji argument - uplynuly cas od posledniho spusteni teto funkce
pyglet.clock.schedule_interval(spaceship_tonik.tick, 1/30)





# registrace textu a prekresleni - spousti metody pri danem eventu
window.push_handlers(
#    on_text=Spaceship.process_text,
    on_draw=spaceship_tonik.draw,
#    on_key_press=spaceship_tonik
)

# spusteni pygletu
pyglet.app.run()