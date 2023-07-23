import os 

# __file__ = "."
basedir = os.path.abspath(os.path.dirname(__file__))

font_path = os.path.join(basedir,"font")
Noto_Sans_TC = os.path.join(font_path, "Noto_Sans_TC")
Noto_Sans_SC = os.path.join(font_path, "Noto_Sans_SC")

font_otf = {
    "Noto_Sans_TC_Black" : os.path.join(Noto_Sans_TC, "NotoSansTC-Black.otf"),
    "Noto_Sans_TC_Bold" : os.path.join(Noto_Sans_TC, "NotoSansTC-Bold.otf"),
    "Noto_Sans_TC_Light" : os.path.join(Noto_Sans_TC, "NotoSansTC-Light.otf"),
    "Noto_Sans_TC_Medium" : os.path.join(Noto_Sans_TC, "NotoSansTC-Medium.otf"),
    "Noto_Sans_TC_Regular" : os.path.join(Noto_Sans_TC, "NotoSansTC-Regular.otf"),
    "Noto_Sans_TC_Thin" : os.path.join(Noto_Sans_TC, "NotoSansTC-Thin.otf"),
    
    "Noto_Sans_SC_Black" : os.path.join(Noto_Sans_SC, "NotoSansSC-Black.otf"),
    "Noto_Sans_SC_Bold" : os.path.join(Noto_Sans_SC, "NotoSansSC-Bold.otf"),
    "Noto_Sans_SC_Light" : os.path.join(Noto_Sans_SC, "NotoSansSC-Light.otf"),
    "Noto_Sans_SC_Medium" : os.path.join(Noto_Sans_SC, "NotoSansSC-Medium.otf"),
    "Noto_Sans_SC_Regular" : os.path.join(Noto_Sans_SC, "NotoSansSC-Regular.otf"),
    "Noto_Sans_SC_Thin" : os.path.join(Noto_Sans_SC, "NotoSansSC-Thin.otf")
}

font_ttf = {
    "Noto_Sans_TC_Black" : os.path.join(Noto_Sans_TC, "NotoSansTC-Black.ttf"),
    "Noto_Sans_TC_Bold" : os.path.join(Noto_Sans_TC, "NotoSansTC-Bold.ttf"),
    "Noto_Sans_TC_Light" : os.path.join(Noto_Sans_TC, "NotoSansTC-Light.ttf"),
    "Noto_Sans_TC_Medium" : os.path.join(Noto_Sans_TC, "NotoSansTC-Medium.ttf"),
    "Noto_Sans_TC_Regular" : os.path.join(Noto_Sans_TC, "NotoSansTC-Regular.ttf"),
    "Noto_Sans_TC_Thin" : os.path.join(Noto_Sans_TC, "NotoSansTC-Thin.ttf"),
    
    "Noto_Sans_SC_Black" : os.path.join(Noto_Sans_SC, "NotoSansSC-Black.ttf"),
    "Noto_Sans_SC_Bold" : os.path.join(Noto_Sans_SC, "NotoSansSC-Bold.ttf"),
    "Noto_Sans_SC_Light" : os.path.join(Noto_Sans_SC, "NotoSansSC-Light.ttf"),
    "Noto_Sans_SC_Medium" : os.path.join(Noto_Sans_SC, "NotoSansSC-Medium.ttf"),
    "Noto_Sans_SC_Regular" : os.path.join(Noto_Sans_SC, "NotoSansSC-Regular.ttf"),
    "Noto_Sans_SC_Thin" : os.path.join(Noto_Sans_SC, "NotoSansSC-Thin.ttf")
}