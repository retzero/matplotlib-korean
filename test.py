import os
import shutil

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import matplotlib_fname, get_cachedir, rc

# 이 부분은 한번만 실행 해 주면 됨.
font_path = './NanumGothicCoding.ttf'
target_font_path = os.path.join(fonts_dir, font_path)
if not os.path.isfile(target_font_path):
    fonts_dir = os.path.join(os.path.dirname(matplotlib_fname()), 'fonts', 'ttf')
    shutil.copyfile(font_path, target_font_path)
    shutil.rmtree(get_cachedir())

fontlist = fm.findSystemFonts(fontpaths=os.getcwd(), fontext='ttf')

if True:
    font_name = fm.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    plt.scatter([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
    plt.title('타이틀 입니다.')
    plt.xlabel('X축 라벨')
    plt.ylabel('Y축 라벨')
    plt.grid(True)
    plt.show()
