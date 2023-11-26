from kivymd. app import MDApp
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
kv = """

Screen:
    
    AnchorLayout:
        MDFillRoundFlatButton:
            text:"open"
            padding: "20dp"
            on_press:
                app.open()

"""

class App(MDApp):
    def build(self):
        return Builder.load_string(kv)
        
    def open(self):
        self.FM = MDFileManager(select_path=self.selpath)
        self.FM.show(os.path.expanduser("/"))
        
    def selpath(self, path):
        toast(str(path))
        
if __name__ == "__main__":
    App().run()