from kivy.uix.actionbar import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.codeinput import TextInput
from kivy.uix.actionbar import Label
from kivy.app import App 
from kivy.uix.actionbar import BoxLayout
from kivy.core.window import Window 
import time
import re

Window.size = (500,700)
class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.display_text: TextInput = TextInput(halign='right',
                      size_hint=(1, 0.15), font_size=64,multiline=False)
        self.add_widget(self.display_text)

        self.calculator_buttons: GridLayout = GridLayout(rows=5, cols=4)

        self.operator_list: list[str] = ['+', '/', '+', '*']

        button_names: list[list] = [["CE","C","<<","/"],
                                    ["7","8" ,"9" ,"*"],
                                    ["4","5" ,"6" ,"-"],
                                    ["1","2" ,"3" ,"+"],
                                    ["+/-","0",".","="]] 

        self.button_dict: dict[str, Button] = {}
        for num, button in enumerate(button_names):
            for button_name in button:
                self.button_dict[button_name] = Button(text=button_name,font_size=32)
                self.button_dict[button_name].bind(state=self.enter_value)
                self.calculator_buttons.add_widget(self.button_dict[button_name])

        self.add_widget(self.calculator_buttons)
        self.display_text.text = '0'

    def enter_value(self, instance, value):
        time.sleep(0.16)
        if value == 'normal':
            match instance.text:
                case '<<':  
                    if self.display_text.text == 'Erorr':
                        pass
                    else:
                        self.display_text.text = self.display_text.text[:-1]
                case 'C':  
                    self.display_text.text = '0'
                case 'CE':  
                    if self.display_text.text[-1] in self.operator_list:
                        pass
                    elif self.display_text.text == 'Erorr':
                        pass
                    else:
                        find = re.findall(r'(\d+/)|(\d+\*)|(\d+\-)|(\d+\+)', self.display_text.text)
                        txt = [list(filter(lambda n: any(n), i))[0] for i in find]
                        self.display_text.text = ''.join(txt)
                        if self.display_text.text == '':
                            self.display_text.text = '0'
                case '+/-':  
                    if self.display_text.text[-1] in self.operator_list:
                        pass
                    elif self.display_text.text == 'Erorr':
                        pass
                    else:
                        if self.display_text.text[0] != '-' and self.display_text.text[0] != '+':
                            self.display_text.text = '+' + self.display_text.text 
                        
                        txt = re.findall(r'[\-,+,*,/]\d+', self.display_text.text)
         
                        test = ''.join(txt[:-1])

                        main = txt[-1]
                        if main[0] == '+':
                            main = '-' + main[1:]
                            self.display_text.text = \
                            self.display_text.text[:(len(self.display_text.text) - len(main))] + main
                        elif main[0] == '-':
                            main = '+' + main[1:]
                            self.display_text.text = \
                            self.display_text.text[:(len(self.display_text.text) - len(main))] + main
                        elif main[0] == '/' or main[0] == '*':
                            if main[1] == '-':
                                main = '+' + main[2:]
                                self.display_text.text = \
                                self.display_text.text[:(len(self.display_text.text) - len(main))+1] + main
                            elif main[1] == '+':
                                main = '-' + main[2:]
                                self.display_text.text = \
                                self.display_text.text[:(len(self.display_text.text) - len(main))+1] + main
                            else:
                                md = list(self.display_text.text[len(self.display_text.text) - len(main):])
                                md.insert(1,'-')
                                self.display_text.text =\
                                self.display_text.text[:(len(self.display_text.text) - len(main))] + ''.join(md)
                case '=':  
                    try:
                        self.display_text.text = str(eval(self.display_text.text))
                    except:
                        self.display_text.text = 'Erorr'
                case '*':  
                    if self.display_text.text == 'Erorr':
                        self.display_text.text = 'Erorr'
                    elif self.display_text.text[-1] == '/':
                        self.display_text.text = self.display_text.text[:-1] + instance.text
                    else:
                        self.display_text.text += instance.text
                case '/':
                    if self.display_text.text == 'Erorr':
                        self.display_text.text = 'Erorr'
                    elif self.display_text.text[-1] == '*':
                        self.display_text.text = self.display_text.text[:-1] + instance.text
                    else:
                        self.display_text.text += instance.text

                case _:
                    if self.display_text.text == '0':
                        self.display_text.text = ''
                        self.display_text.text += instance.text
                    elif self.display_text.text == 'Erorr':
                        self.display_text.text = ''
                        self.display_text.text += instance.text    
                    else:
                        self.display_text.text += instance.text

class Poya_CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    Poya_CalculatorApp().run()

