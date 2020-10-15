from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.widget import Widget
from PIL import Image
import PIL 
import shutil

Image.LOAD_TRUNCATED_IMAGES = True
import sqlite3
#import serial
from settingsjson import settings_json

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480') 

Builder.load_file('kvs/recycle.kv')
Builder.load_file('kvs/main_kv.kv')
Builder.load_file('kvs/second.kv')
Builder.load_file('kvs/Add.kv')
Builder.load_file('kvs/Remove.kv')
Builder.load_file('kvs/Choose.kv')
Builder.load_file('kvs/new.kv')
Builder.load_file('kvs/file.kv')
Builder.load_file('kvs/stone.kv')
conn = sqlite3.connect('database/Gemstone.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE CLIENTS
#             ([Id] INTEGER PRIMARY KEY,[Name] text, [Hardness] integer, [Transparency] text, [min. Refraction] float, [Birefringence] float, [Dispersion] float, [Pleochronism] text, [Sensitivity to heat] integer,[Critical angle] text, [HFW-UT] text, [Polishing recommendation] text, [other] text, [link] text)''')
          
#conn.commit()

#Builder.load_file('pys/Add.py')
#gemstore = JsonStore('selection/gemStore.json')

# c = conn.cursor()
# c.execute('''SELECT COUNT(*) FROM Gems''')
# nStones=c.fetchall()[0][0]
# print(nStones)
# conn.commit()


    


GemSetting = JsonStore('GemSetting.json')
Gstore = JsonStore('selection/gems.json')

#nStones= int(Gstore.get('nData')['Num'])
Speed=0
SSpeed=0
count = 0
LabelBase.register(name="Roboto",
fn_regular="sources/Roboto-Regular.ttf",
fn_bold="sources/Roboto-Bold.ttf",
fn_italic="sources/Roboto-Italic.ttf",
fn_bolditalic="sources/Roboto-BoldItalic.ttf")

Sel= 'selection/giphy.gif'
Background = StringProperty()
pathx = "StringProperty()"

class RV(RecycleView):
    
    def __init__(self, **kwargs):
        c = conn.cursor()
        c.execute('''SELECT * FROM Gems''')
        Ast=c.fetchall()
        print("ABCD")
        c = conn.cursor()
        c.execute('''SELECT COUNT(*) FROM Gems''')
        nStones=c.fetchall()[0][0]
        print(nStones)
        conn.commit()
        if nStones%2==1:
            Ast.append(((0, '', '', '', '', '', '', '', '', '', '', '', '', 'S1.gif')))
            nStones=nStones+1
        print(Ast)
        
        
        super(RV, self).__init__(**kwargs)
        #self.data = [{'text': str(x)} for x in range(10)]
        #self.data = [{'id':str(x),'myIM': gemstore.get(str(x))['loc']} for x in range(nStones)]
        self.data = [{'id1':Ast[2*x][0],'id2':Ast[2*x+1][0],'loc1': "database/"+Ast[2*x][13],'loc2': "database/"+Ast[2*x+1][13]} for x in range(int(nStones/2))]
        print(self.data)
        conn.commit()
class Stone:
    name = "GEM"
    image_loc = ''
    def _init_(self, name):
        self.name = name
    def change_name(self,new_name):
        self.name = new_name

class RVScreen(Screen):
    pass

class WidgetApp(App):
    label_a = StringProperty()
    label_a = "6.jpg"
    #GemSetting.put('Background',BC='6.jpg')
    def build(self):
       Background= self.config.get('example', 'pathexample')
       self.settings_cls = SettingsWithSidebar
       setting = self.config.get('example', 'boolexample')
       
       return kv
   
    def build_config(self, config):
        config.setdefaults('example',{
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option2',
            'stringexample': 'some_string',
            'pathexample': '/sources/backgrounds/img.jpg'})
    
    def build_settings(self, settings):
        settings.add_json_panel('Personalize', self.config,data = settings_json)
   
       

 
class MainWindow(Screen):
    BC=StringProperty()
    BC=GemSetting.get('Background')['BC']
    print("BC TRANSFERED")
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        def my_callback(dt):
            global count
            count += 1
            if count == 2:
                print ('Last call of my callback, bye bye !')
                return False
            
            try:
                # arduino = serial.Serial('/dev/tty.usbmodem1421', 9600)
                a=5
            except:
                print ("Failed to connect")
        
            print ('My callback is called',dt)
            self.ids.pgb.value=count
            self.ids.rpmval.text=str(count)
            #print(self.ids.pgb.value)
            
        Clock.schedule_interval(my_callback, 3)
   
    
    def btn_clk_mot(self):
        
        if self.btn_mot_py.background_normal=='sources/images/iconfinder_Stop1Normal_22944.png':
            #print("b is greater than a")
            self.btn_mot_py.background_normal='sources/images/iconfinder_Stop1NormalRed_22947.png'
        else: 
            self.btn_mot_py.background_normal='sources/images/iconfinder_Stop1Normal_22944.png'
    
    def btn_clk_pump(self):
        print('PRESSED')
        
        if self.btn_pump_py.background_normal=='sources/images/iconfinder_Stop1Normal_22944.png':
           # print("b is greater than a")
            self.btn_pump_py.background_normal='sources/images/iconfinder_Stop1NormalRed_22947.png'
        else: 
            self.btn_pump_py.background_normal='sources/images/iconfinder_Stop1Normal_22944.png'
           # print("b is greater than a")
              
class SecondWindow(Screen):
    def btn_B1_clk(self):
        #Gstore.put('Sel',ID=str(self.manager.s),Loc=Gstore.get(self.manager.s)['loc'])
        #self.ids.S1.ids.my.text=Gstore.get('toSet')['Loc']
        self.manager.ids.S1.ids.my.text=Gstore.get('toSet')['Loc']
        self.manager.current='main'
 
class Add(Screen):
    pass

class New(Screen):
    def SaveDatabase(self):
        print("Saved file")
        if self.name_py.text=="":
        
            print("Name Cant be empty")
            
            
        conn = sqlite3.connect('database/Gemstone.db')
        c = conn.cursor()
        insert_stmt = ("INSERT INTO Gems(Name, Hardness, Transparency,minRefraction, Birefringence,Dispersion,Pleochronism,ThermalSensitivity,CriticalAngle,HFW_UT,Polishing ,other,link)"
                       "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)")
        data = (self.name_py.text, self.hardness.text, self.transparency.text, self.minRefraction.text, self.birefringence.text, self.dispersion.text, self.pleochronism.text, self.thermalSensitivity.text, self.criticalAngle.text, self.mLG.text, self.polishing.text, self.others.text,self.name_py.text+".gif" )

        #try:
        # Executing the SQL command
        c.execute(insert_stmt, data)
        
        # Commit your changes in the database
        conn.commit()
        print("Data inserted")  
        
        
        #except:
        # Rolling back in case of error
        #conn.rollback()
        shutil.copy2( self.selGem.source,"database/"+self.name_py.text+'.gif')
        self.name_py.text="" 
        self.hardness.text="" 
        self.transparency.text=""
        self.minRefraction.text=""
        self.birefringence.text=""
        self.dispersion.text=""
        self.pleochronism.text=""
        self.thermalSensitivity.text=""
        self.criticalAngle.text=""
        self.mLG.text=""
        self.polishing.text=""
        self.others.text=""
        self.selGem.source="database/Choose.gif"
       # GemAPP.recreate()
        

class Filechooser(Screen): 
    def select(self, *args): 
        try: self.label.text = args[1][0]
        except: pass
        
        try: self.selGem.source=args[1][0]
        except: pass
       # self.my.text= args[1][0]
       # self.selGem.source=args[1][0]
      #  im1 = Image.open(args[1][0])  
      #  im1 = im1.save("geeks.gif") 
        #shutil.copy2( args[1][0],'geeks.gif')
    def sel(self):
        print(self.root.manager.ids)
        
              
        
class Stone(Screen):
    pass       
                    

class Remove(Screen):
    pass 

class Choose(Screen):
    
    def Choosen(self,path):
        print(path[0])
        pathx=path
        #print(pathx)
        Gstore.put('pathpass',ID='Choosen',Loc=pathx)
        self.ids.image.source = path[0]
        
    def SelChoosen(self):
        print(Gstore.get('pathpass')['Loc'])


class WindowManager(ScreenManager):
    s= StringProperty()
    
    def sel(self,messa):
       # print(self.ids.new.ids.SelGem.source)
        self.ids.new.ids.SelGem.source=messa
        
    
   

    def go_to_Sel(self,messa):
       
       if(messa!=0):
            c = conn.cursor()
            c.execute('''SELECT * FROM Gems WHERE Id= ?''',(int(messa),))
            a= c.fetchall()
            print(a[0][13])
            conn.commit()
            self.ids.stone.ids.SelGem.source='database/'+a[0][13]
            self.ids.stone.ids.name.text=a[0][1]
            self.ids.stone.ids.hardness.text=str(a[0][2])
            self.ids.stone.ids.transparency.text=str(a[0][3])
            self.ids.stone.ids.minRefraction.text=str(a[0][4])
            self.ids.stone.ids.birefringence.text=str(a[0][5])
            self.ids.stone.ids.dispersion.text=str(a[0][6])
            self.ids.stone.ids.pleochronism.text=str(a[0][7])
            self.ids.stone.ids.thermalSensitivity.text=str(a[0][8])
            self.ids.stone.ids.criticalAngle.text=str(a[0][9])
            self.ids.stone.ids.mLG.text=str(a[0][10])
            self.ids.stone.ids.polishing.text=str(a[0][11])
            self.ids.stone.ids.others.text=str(a[0][12])
            self.current='stone'
     
        

class RecycleViewRow(BoxLayout):
    id1=ObjectProperty()
    id2=ObjectProperty()
    loc1=StringProperty()
    loc2=StringProperty()
    
kv=Builder.load_file("kvs/A.kv")
 
if __name__ == "__main__":
    GemAPP=WidgetApp()
    GemAPP.run()
   
    
