from kivymd. app import MDApp
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy import platform
kv = """

if platform == "android": 
    from android. permissions import request_permissions, Permission 
    request_permissions([Permission.READ_EXTERNAL_STORAGE])
  

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
        try:
            self.FM = MDFileManager(select_path=self.selpath)
            self.FM.show(os.path.expanduser("/"))

        except:
            pass
        
    def selpath(self, path):
        toast(str(path))
        
if __name__ == "__main__":
    App().run()