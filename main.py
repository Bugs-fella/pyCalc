
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("main.kv")

class MyLayout(BoxLayout):
    
    def btn_press(self, instance):
        symbols = ["-", "*", ".", "/", "+", "C", "=", "x"]
        input = self.ids.input.text
        orig = instance.font_size
        anim = Animation(font_size=int(orig * 2), d=.1, t="out_elastic")
        anim += Animation(font_size=orig, d=.1, t="out_elastic")
        if instance.text not in symbols:
            self.ids.input.text += instance.text

        else:
            if instance.text == "C":
                self.ids.input.text = ""

            elif instance.text == "x":
                self.ids.input.text = self.ids.input.text[:-1]
            
            elif instance.text == "=":
                try:
                    soln = str(eval(str(input)))
                    self.ids.output.text = soln
                except:
                    self.ids.output.text = "SYNTAX ERROR"

            elif (len(input) > 0) and (instance.text in symbols) and (input[-1] not in symbols):
                self.ids.input.text += instance.text
        anim.start(instance)

class CornelCalc(App):
    def build(self):
        self.icon = "icon.png"
        return MyLayout()

if __name__ == '__main__':
    CornelCalc().run()
