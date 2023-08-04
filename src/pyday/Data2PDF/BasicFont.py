import sys
sys.path.append('..')
from ..basic import config

# 引入字體 
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 寫入字體
for name, path in config.font_ttf.items():
    pdfmetrics.registerFont(TTFont(name, path))

Basis_Font = [ # 5, 6
        [ [ "Title_TC", "Title_SC" ], [ "Noto_Sans_TC_Bold", "Noto_Sans_SC_Bold" ] , 1, 18, 24 ],
        [ [ "SubTitle_TC", "SubTitle_SC" ], [ "Noto_Sans_TC_Bold", "Noto_Sans_SC_Bold" ] , 0, 16, 22 ],
        [ [ "SubTilte2_TC", "SubTilte2_SC" ], [ "Noto_Sans_TC_Bold", "Noto_Sans_SC_Bold "], 0, 16, 22, 16*2 ],
        [ [ "Content_TC", "Content_SC" ], [ "Noto_Sans_TC_Bold", "Noto_Sans_SC_Bold "], 0, 12, 20 ],
        [ [ "Content2_TC", "Content2_SC" ], [ "Noto_Sans_TC_Bold", "Noto_Sans_SC_Bold "], 0, 12, 20, 16*2 ],
    ]

# [ ["Content2_TC"], ["Noto_Sans_TC_Bold"], "TA_LEFT", 12, 20, 16*2 ],
# [ "Content3_TC", "Noto_Sans_TC_Bold", "TA_LEFT", 12, 20, 16*2 ]

# TA_LEFT = 0
# TA_CENTER = 1
# TA_RIGHT = 2
# TA_JUSTIFY = 4

Basis_Img = None
Basis_Table = None

