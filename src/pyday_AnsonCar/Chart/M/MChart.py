import matplotlib
from matplotlib.font_manager import FontManager
# matplotlib.rc("font",family='Heiti TC')

class MChart:
    def __int__(self):
        self.setfont("Heiti TC")

    def font(self):
        mpl_fonts = set(f.name for f in FontManager().ttflist)
        print('all font list get from matplotlib.font_manager:')
        for f in sorted(mpl_fonts):
            print('\t' + f)

    def setfont(self, font):
        matplotlib.rc("font",family=font)

    def outputPhoto(self,name):
        self.savefig(name)