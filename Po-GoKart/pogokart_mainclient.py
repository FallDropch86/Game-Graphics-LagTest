from ursina import *
from ursina.shaders import *
import sqlite3

dbcon = sqlite3.connect('Client-PlrStats.db')
dbcursor = dbcon.cursor()

dbcursor.execute('''CREATE TABLE IF NOT EXISTS CLIENTPLAYER_STATS
(UserName   TEXT        NULL,
XP          INT         NULL,
PFP         BLOB        NULL)''')

ColumnAlrdyExsts = dbcursor.fetchone()

print("Player database connected successfully!")

app = Ursina()
window.borderless = False

Music = Audio("Musics/Dimension - Creo.mp3", loop=True)
Music.play()

camera.position = (1074, 360, -44)
camera.rotation_x +=15
camera.rotation_y -=90

def playMenu():
    playBtn.disable()
    GameInfoBtn.disable()
    Gobackbtn.enable()
    foodsplash.enable()
    airtime.enable()
    timechase.enable()
    foodsplash.enable()
    fiveplrrace.enable()
    GameModeSelectTxt.enable()
    MainMenuTitle.disable()
    camera.animate('position', (500, 360, -175), duration=0.4)
    camera.animate('rotation_x', camera.rotation_x + 5, duration=0.4)

def GoBacktoMenu():
    global Pogocitytrackbtnconf
    global floatingspaceconf
    global rockystuntconf
    global freezeridingconf
    global drydesertsconf
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()
    strtrkartbtn.disable()
    btrstrtrsbtn.disable()
    pogonoob1btn.disable()
    pogobtr1btn.disable()
    pogonoob2btn.disable()
    pogobtr2btn.disable()
    pogovip1btn.disable()
    pogolux1btn.disable()
    pogovip2btn.disable()
    pogolux2btn.disable()
    pogohyperturboplusbtn.disable()
    Pogocitytrackbtnconf = False
    floatingspaceconf = False
    rockystuntconf = False
    freezeridingconf = False
    drydesertsconf = False
    global fiveplrraceconf
    global timechaseconf
    global foodsplashconf
    global airtimeconf
    fiveplrraceconf = False
    timechaseconf = False
    foodsplashconf = False
    airtimeconf = False
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf
    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    playBtn.enable()
    GameInfoBtn.enable()
    Gobackbtn.disable()
    Drydeserts.disable()
    GameInfo.disable()
    foodsplash.disable()
    airtime.disable()
    timechase.disable()
    MapSelectTxt.disable()
    floatingspace.disable()
    rockystunt.disable()
    foodsplash.disable()
    freezeriding.disable()
    fiveplrrace.disable()
    KartSelectTxt.disable()
    MainMenuTitle.enable()
    Pogocitytrackbtn.disable()
    GameModeSelectTxt.disable()
    slctkartBtn.disable()
    camera.animate('position', (1074, 360, -44), duration=0.4)
    camera.animate('rotation_x', camera.rotation_x - 5, duration=0.4)

Gobackbtn = Button(icon="UI/Buttons/gobackbtn.png", scale=(0.2, 0.15), on_click=GoBacktoMenu)
Gobackbtn.position = (-0.76, 0.4)
Gobackbtn.disable()

usrnmtxtbox = InputField(scale=(0.6, 0.1))
usrnmtxtbox.position = (0.425, -0.412)

def SaveUsrname():
    dbcursor.execute("SELECT COUNT(*) FROM CLIENTPLAYER_STATS")
    reccheckresult = dbcursor.fetchone()[0]
    if reccheckresult is not None and reccheckresult == 0:
        dbcursor.execute(f"INSERT INTO CLIENTPLAYER_STATS (UserName) VALUES ('{usrnmtxtbox.text}')");
        dbcon.commit()
        print("Successfully registered player username!")
    elif reccheckresult is not None and reccheckresult > 0:
        dbcursor.execute(f'''UPDATE CLIENTPLAYER_STATS SET UserName = '{usrnmtxtbox.text}' WHERE rowid = 1''')
        dbcon.commit()
        print("Successfully edited player username!")
    else:
        print("Error while trying to register or edit a username")

saveusrnmbtn = Button(icon="UI/Buttons/SaveUsername.png", scale=(0.1, 0.1), on_click=SaveUsrname)
saveusrnmbtn.position = (0.06, -0.412)

global Pogocitytrackbtnconf
global floatingspaceconf
global rockystuntconf
global freezeridingconf
global drydesertsconf

Pogocitytrackbtnconf = False
floatingspaceconf = False
rockystuntconf = False
freezeridingconf = False
drydesertsconf = False

def Pogocitytrackbtnconffunc():
    global Pogocitytrackbtnconf
    Pogocitytrackbtnconf = True
    KartSelectTxt.enable()
    MapSelectTxt.disable()
    strtrkartbtn.enable()
    btrstrtrsbtn.enable()
    pogonoob1btn.enable()
    pogobtr1btn.enable()
    pogonoob2btn.enable()
    pogobtr2btn.enable()
    pogovip1btn.enable()
    pogolux1btn.enable()
    pogovip2btn.enable()
    pogolux2btn.enable()
    pogohyperturboplusbtn.enable()
    Pogocitytrackbtn.disable()
    freezeriding.disable()
    floatingspace.disable()
    rockystunt.disable()
    Drydeserts.disable()

def floatingspaceconffunc():
    global floatingspaceconf
    floatingspaceconf = True
    KartSelectTxt.enable()
    MapSelectTxt.disable()
    strtrkartbtn.enable()
    btrstrtrsbtn.enable()
    pogonoob1btn.enable()
    pogobtr1btn.enable()
    pogonoob2btn.enable()
    pogobtr2btn.enable()
    pogovip1btn.enable()
    pogolux1btn.enable()
    pogovip2btn.enable()
    pogolux2btn.enable()
    pogohyperturboplusbtn.enable()
    Pogocitytrackbtn.disable()
    freezeriding.disable()
    floatingspace.disable()
    rockystunt.disable()
    Drydeserts.disable()

def rockystuntconffunc():
    global rockystuntconf
    rockystuntconf = True
    KartSelectTxt.enable()
    MapSelectTxt.disable()
    Pogocitytrackbtn.disable()
    strtrkartbtn.enable()
    btrstrtrsbtn.enable()
    pogonoob1btn.enable()
    pogobtr1btn.enable()
    pogonoob2btn.enable()
    pogobtr2btn.enable()
    pogovip1btn.enable()
    pogolux1btn.enable()
    pogovip2btn.enable()
    pogolux2btn.enable()
    pogohyperturboplusbtn.enable()
    freezeriding.disable()
    floatingspace.disable()
    rockystunt.disable()
    Drydeserts.disable()

def freezeridingconffunc():
    global freezeridingconf
    freezeridingconf = True
    KartSelectTxt.enable()
    MapSelectTxt.disable()
    strtrkartbtn.enable()
    btrstrtrsbtn.enable()
    pogonoob1btn.enable()
    pogobtr1btn.enable()
    pogonoob2btn.enable()
    pogobtr2btn.enable()
    pogovip1btn.enable()
    pogolux1btn.enable()
    pogovip2btn.enable()
    pogolux2btn.enable()
    pogohyperturboplusbtn.enable()
    Pogocitytrackbtn.disable()
    freezeriding.disable()
    floatingspace.disable()
    rockystunt.disable()
    Drydeserts.disable()

def drydesertsconffunc():
    global drydesertsconf
    drydesertsconf = True
    KartSelectTxt.enable()
    MapSelectTxt.disable()
    Pogocitytrackbtn.disable()
    strtrkartbtn.enable()
    btrstrtrsbtn.enable()
    pogonoob1btn.enable()
    pogobtr1btn.enable()
    pogonoob2btn.enable()
    pogobtr2btn.enable()
    pogovip1btn.enable()
    pogolux1btn.enable()
    pogovip2btn.enable()
    pogolux2btn.enable()
    pogohyperturboplusbtn.enable()
    freezeriding.disable()
    floatingspace.disable()
    rockystunt.disable()
    Drydeserts.disable()

Pogocitytrackbtn = Button(icon="UI/Buttons/Po-Go City track", scale=(0.2, 0.75), on_click=Pogocitytrackbtnconffunc)
Pogocitytrackbtn.position = (-0.7, -0.1)
Pogocitytrackbtn.disable()

floatingspace = Button(icon="UI/Buttons/floating space.png", scale=(0.2, 0.75), on_click=floatingspaceconffunc)
floatingspace.position = (-0.46, -0.1)
floatingspace.disable()

rockystunt = Button(icon="UI/Buttons/rockystunt.png", scale=(0.2, 0.75), on_click=rockystuntconffunc)
rockystunt.position = (-0.22, -0.1)
rockystunt.disable()

freezeriding = Button(icon="UI/Buttons/freezeriding.png", scale=(0.67, 0.24), on_click=freezeridingconffunc)
freezeriding.position = (0.28, 0.17)
freezeriding.disable()

Drydeserts = Button(icon="UI/Buttons/Drydeserts.png", scale=(0.67, 0.24), on_click=drydesertsconffunc)
Drydeserts.position = (0.28, -0.17)
Drydeserts.disable()

GameModeSelectTxt = Button(icon="UI/Image labels/GameModeSelect.png", scale=(0.35, 0.14))
GameModeSelectTxt.position = (-0.3, 0.35)
GameModeSelectTxt.disable()

global fiveplrraceconf
global timechaseconf
global foodsplashconf
global airtimeconf

fiveplrraceconf = False
timechaseconf = False
foodsplashconf = False
airtimeconf = False

def fiveplrraceconffunc():
    global fiveplrraceconf
    fiveplrraceconf = True
    GameModeSelectTxt.disable()
    fiveplrrace.disable()
    Pogocitytrackbtn.enable()
    freezeriding.enable()
    floatingspace.enable()
    Drydeserts.enable()
    timechase.disable()
    rockystunt.enable()
    foodsplash.disable()
    airtime.disable()
    MapSelectTxt.enable()

def timechaseconffunc():
    global timechaseconf
    timechaseconf = True
    GameModeSelectTxt.disable()
    fiveplrrace.disable()
    Pogocitytrackbtn.enable()
    freezeriding.enable()
    Drydeserts.enable()
    timechase.disable()
    floatingspace.enable()
    rockystunt.enable()
    foodsplash.disable()
    airtime.disable()
    MapSelectTxt.enable()

def foodsplashconffunc():
    global foodsplashconf
    foodsplashconf = True
    GameModeSelectTxt.disable()
    fiveplrrace.disable()
    freezeriding.enable()
    timechase.disable()
    floatingspace.enable()
    rockystunt.enable()
    Drydeserts.enable()
    Pogocitytrackbtn.enable()
    foodsplash.disable()
    airtime.disable()
    MapSelectTxt.enable()

def airtimeconffunc():
    global airtimeconf
    airtimeconf = True
    GameModeSelectTxt.disable()
    fiveplrrace.disable()
    timechase.disable()
    freezeriding.enable()
    Pogocitytrackbtn.enable()
    Drydeserts.enable()
    floatingspace.enable()
    rockystunt.enable()
    foodsplash.disable()
    airtime.disable()
    MapSelectTxt.enable()

fiveplrrace = Button(icon="UI/Buttons/5 player race.png", scale=(0.4, 0.4), on_click=fiveplrraceconffunc)
fiveplrrace.position = (-0.65, -0.05)
fiveplrrace.disable()

timechase = Button(icon="UI/Buttons/timechase.png", scale=(0.4, 0.4), on_click=timechaseconffunc)
timechase.position = (-0.22, -0.05)
timechase.disable()

foodsplash = Button(icon="UI/Buttons/foodsplash.png", scale=(0.4, 0.4), on_click=foodsplashconffunc)
foodsplash.position = (0.21, -0.05)
foodsplash.disable()

airtime = Button(icon="UI/Buttons/airtime.png", scale=(0.4, 0.4), on_click=airtimeconffunc)
airtime.position = (0.64, -0.05)
airtime.disable()

MapSelectTxt = Button(icon="UI/Image labels/MapselectTxt.png", scale=(0.35, 0.14))
MapSelectTxt.position = (-0.3, 0.35)
MapSelectTxt.disable()

KartSelectTxt = Button(icon="UI/Image labels/KartSelectTxt.png", scale=(0.25, 0.14))
KartSelectTxt.position = (-0.3, 0.35)
KartSelectTxt.disable()

def FullScreenToggleFunc():
    if window.fullscreen == False:
        window.fullscreen = True
    else:
        window.fullscreen = False

fullscreentoggle = Button(icon="UI/Buttons/flscrntoggle.png", scale=(0.26, 0.16), on_click=FullScreenToggleFunc)
fullscreentoggle.position = (0.69, 0.4)

playBtn = Button(icon="UI/Buttons/playButton.png", scale=(0.13, 0.13), on_click=playMenu)
playBtn.position = (-0.100, -0.05)

def GameExit():
    application.quit()

ExitGameBtn = Button(icon="UI/Buttons/ExitGameBtn.png", scale=(0.13, 0.13), on_click=GameExit)
ExitGameBtn.position = (0.805, -0.412)

GameInfo = Button(icon="UI/Image labels/Gameinfo.png", scale=(1.1, 0.69))
GameInfo.position = (0,0)
GameInfo.disable()

def gameinfo():
    GameInfoBtn.disable()
    playBtn.disable()
    MainMenuTitle.disable()
    GameInfo.enable()
    Gobackbtn.enable()
    camera.animate('position', (500, 360, -175), duration=0.6)
    camera.animate('rotation_x', camera.rotation_x + 5, duration=0.6)

GameInfoBtn = Button(icon="UI/Buttons/GameInfoBtn.png", scale=(0.13, 0.13), on_click=gameinfo)
GameInfoBtn.position = (0.100, -0.05)

MainMenuTitle = Button(icon="UI/image labels/MainMenuGameTitle.png", scale=(0.41, 0.29))
MainMenuTitle.position = (-0.0005,0.33)

BuildVersionTxt = Text(text="Dev Build v2.0 - 22nd September 2023, 4:05:23 P.M.", scale=0.75, color=color.black)
BuildVersionTxt.position = (-0.88, -0.47)

global strtrkartconf
global btrstrtrsconf
global pogonoob1conf
global pogobtr1conf
global pogonoob2conf
global pogobtr2conf
global pogovip1conf
global pogolux1conf
global pogovip2conf
global pogolux2conf
global pogohyperturboplusconf

strtrkartconf = False
btrstrtrsconf = False
pogonoob1conf = False
pogobtr1conf = False
pogonoob2conf = False
pogobtr2conf = False
pogovip1conf = False
pogolux1conf = False
pogovip2conf = False
pogolux2conf = False
pogohyperturboplusconf = False

def showstrtrkartmenu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = True
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.enable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()

strtrkartbtn = Button(icon="UI/Buttons/Starter Kart.png", scale=(0.1, 0.1), on_click=showstrtrkartmenu)
strtrkartbtn.position = (-0.8, -0.41)
strtrkartbtn.disable()

strtrkart = Entity(model=r"Karts/Actual Kart/Starter Kart.glb", scale=2.4, shader=lit_with_shadows_shader)
strtrkart.position = (-80, 132, -220)
strtrkart.rotation_y += 225
strtrkart.disable()

def showbtrstrtrsmenu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = True
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.enable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()

btrstrtrsbtn = Button(icon="UI/Buttons/Better Starters.png", scale=(0.1, 0.1), on_click=showbtrstrtrsmenu)
btrstrtrsbtn.position = (-0.69, -0.41)
btrstrtrsbtn.disable()

btrstrtrs = Entity(model=r"Karts/Actual Kart/Better Starters.glb", scale=2.4, shader=lit_with_shadows_shader)
btrstrtrs.position = (-90, 132, -245)
btrstrtrs.rotation_y += 225
btrstrtrs.disable()

def showpogonoob1menu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = True
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.enable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()

pogonoob1btn = Button(icon="UI/Buttons/POGOnoob-1.png", scale=(0.1, 0.1), on_click=showpogonoob1menu)
pogonoob1btn.position = (-0.58, -0.41)
pogonoob1btn.disable()

pogonoob1 = Entity(model=r"Karts/Actual Kart/POGOnoob-1.glb", scale=3.1, shader=lit_with_shadows_shader)
pogonoob1.position = (83, 132, -160)
pogonoob1.rotation_y += 225
pogonoob1.disable()

def showpogobtr1menu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = True
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.enable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()

pogobtr1btn = Button(icon="UI/Buttons/POGObtr-1.png", scale=(0.1, 0.1), on_click=showpogobtr1menu)
pogobtr1btn.position = (-0.47, -0.41)
pogobtr1btn.disable()

pogobtr1 = Entity(model=r"Karts/Actual Kart/POGObtr-1.glb", scale=2.4, shader=lit_with_shadows_shader)
pogobtr1.position = (-10, 132, -186)
pogobtr1.rotation_y += 225
pogobtr1.disable()

def showpogonoob2menu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = True
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.enable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()

pogonoob2btn = Button(icon="UI/Buttons/POGOnoob-2.png", scale=(0.1, 0.1), on_click=showpogonoob2menu)
pogonoob2btn.position = (-0.36, -0.41)
pogonoob2btn.disable()

pogonoob2 = Entity(model=r"Karts/Actual Kart/POGOnoob-2.glb", scale=2.4, shader=lit_with_shadows_shader)
pogonoob2.position = (-78, 132, -227)
pogonoob2.rotation_y += 225
pogonoob2.disable()

def showpogobtr2menu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = True
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.enable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()

pogobtr2btn = Button(icon="UI/Buttons/POGObtr-2.png", scale=(0.1, 0.1), on_click=showpogobtr2menu)
pogobtr2btn.position = (-0.25, -0.41)
pogobtr2btn.disable()

pogobtr2 = Entity(model=r"Karts/Actual Kart/POGObtr-2.glb", scale=2.9, shader=lit_with_shadows_shader)
pogobtr2.position = (-8, 132, -157)
pogobtr2.rotation_y += 225
pogobtr2.disable()

def showpogovip1menu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = True
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.enable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()

pogovip1btn = Button(icon="UI/Buttons/POGOvip-1.png", scale=(0.1, 0.1), on_click=showpogovip1menu)
pogovip1btn.position = (-0.14, -0.41)
pogovip1btn.disable()

pogovip1 = Entity(model=r"Karts/Actual Kart/POGOvip-1.glb", scale=8.4, shader=lit_with_shadows_shader)
pogovip1.position = (-80, 132, -237)
pogovip1.rotation_y += 225
pogovip1.disable()

pogovip1frontwheel = Entity(model=r"Karts/Kart wheels/front wheels/POGOvip-1 front wheels.glb", scale=1.2, shader=lit_with_shadows_shader, parent=pogovip1)
pogovip1frontwheel.rotation_y += 180
pogovip1frontwheel.position = (17.2, 0, -10)

pogovip1rearwheel = Entity(model=r"Karts/Kart wheels/rear wheels/POGOvip-1 back wheels.glb", scale=1.2, shader=lit_with_shadows_shader, parent=pogovip1)
pogovip1rearwheel.rotation_y += 180
pogovip1rearwheel.position = (20, 0, -10)

def showpogolux1menu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = True
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.enable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.disable()

pogolux1btn = Button(icon="UI/Buttons/POGOlux-1.png", scale=(0.1, 0.1), on_click=showpogolux1menu)
pogolux1btn.position = (-0.8, -0.30)
pogolux1btn.disable()

pogolux1 = Entity(model=r"Karts/Actual Kart/POGOlux-1.glb", scale=6.9, shader=lit_with_shadows_shader)
pogolux1.position = (-140, 132, -277)
pogolux1.rotation_y += 225
pogolux1.disable()

def showpogovip2menu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = True
    pogolux2conf = False
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.enable()
    pogolux2.disable()
    pogohyperturboplus.disable()

pogovip2btn = Button(icon="UI/Buttons/POGOvip-2.png", scale=(0.1, 0.1), on_click=showpogovip2menu)
pogovip2btn.position = (-0.69, -0.30)
pogovip2btn.disable()

pogovip2 = Entity(model=r"Karts/Actual Kart/POGOvip-2.glb", scale=10, shader=lit_with_shadows_shader)
pogovip2.position = (-290, 132, 120)
pogovip2.rotation_y += -45
pogovip2.disable()

pogovip2frontwheel = Entity(model=r"Karts/Kart wheels/front wheels/POGOvip-2 wheels front.glb", scale=1.2, shader=lit_with_shadows_shader, parent=pogovip2)
pogovip2frontwheel.rotation_y += 180
pogovip2frontwheel.position = (-8.65, 0, -89)

pogovip2rearwheel = Entity(model=r"Karts/Kart wheels/rear wheels/POGOvip-2 wheels back.glb", scale=1.2, shader=lit_with_shadows_shader, parent=pogovip2)
pogovip2rearwheel.rotation_y += 180
pogovip2rearwheel.position = (-8.32, 0, -70.5)

def showpogolux2menu():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = True
    pogohyperturboplusconf = False
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.enable()
    pogohyperturboplus.disable()

pogolux2btn = Button(icon="UI/Buttons/POGOlux-2.png", scale=(0.1, 0.1), on_click=showpogolux2menu)
pogolux2btn.position = (-0.58, -0.30)
pogolux2btn.disable()

pogolux2 = Entity(model=r"Karts/Actual Kart/POGOlux-2.glb", scale=4.5, shader=lit_with_shadows_shader)
pogolux2.position = (50, 132, -398)
pogolux2.rotation_y += 140
pogolux2.disable()

def showpogohypertubroplus():
    slctkartBtn.enable()
    global strtrkartconf
    global btrstrtrsconf
    global pogonoob1conf
    global pogobtr1conf
    global pogonoob2conf
    global pogobtr2conf
    global pogovip1conf
    global pogolux1conf
    global pogovip2conf
    global pogolux2conf
    global pogohyperturboplusconf

    strtrkartconf = False
    btrstrtrsconf = False
    pogonoob1conf = False
    pogobtr1conf = False
    pogonoob2conf = False
    pogobtr2conf = False
    pogovip1conf = False
    pogolux1conf = False
    pogovip2conf = False
    pogolux2conf = False
    pogohyperturboplusconf = True
    strtrkart.disable()
    btrstrtrs.disable()
    pogonoob1.disable()
    pogobtr1.disable()
    pogonoob2.disable()
    pogobtr2.disable()
    pogovip1.disable()
    pogolux1.disable()
    pogovip2.disable()
    pogolux2.disable()
    pogohyperturboplus.enable()

pogohyperturboplusbtn = Button(icon="UI/Buttons/POGO-HyperTurboPlus.png", scale=(0.1, 0.1), on_click=showpogohypertubroplus)
pogohyperturboplusbtn.position = (-0.47, -0.30)
pogohyperturboplusbtn.disable()

pogohyperturboplus = Entity(model=r"Karts/Actual Kart/POGO-HyperTurboPlus.glb", scale=2.8, shader=lit_with_shadows_shader)
pogohyperturboplus.position = (-118, 132, -284)
pogohyperturboplus.rotation_y += -45
pogohyperturboplus.disable()

slctkartBtn = Button(icon="UI/Buttons/Select this kart!.png", scale=(0.26, 0.2))
slctkartBtn.position = (0.6,-0.2)
slctkartBtn.disable()

sun = DirectionalLight()
sun.look_at(Vec3(0.5,-1,-2))

Sky().texture = "Sky/MainMenuMap.jpg"

MainMenuMap = Entity(model=r"Maps/Main Menu map.glb", scale=2, shader=lit_with_shadows_shader)

def update():
    camera.x += held_keys["s"] * 0.8
    camera.x -= held_keys["w"] * 0.8
    camera.y += held_keys["e"] * 0.5
    camera.y -= held_keys["q"] * 0.5
    camera.z += held_keys["d"] * 0.5
    camera.z -= held_keys["a"] * 0.5

app.run()
