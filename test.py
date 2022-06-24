import os
import shutil

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import matplotlib_fname, get_cachedir, rc


font_path = './NanumGothicCoding.ttf'
fonts_dir = os.path.join(os.path.dirname(matplotlib_fname()), 'fonts', 'ttf')
target_fonts_path = os.path.join(fonts_dir, font_path)

# 여기는 한번만 실행 하면 됨.
if not os.path.isfile(target_fonts_path):
    font_cache_dir = get_cachedir()
    shutil.rmtree(font_cache_dir)
    shutil.copyfile(font_path, target_fonts_path)
    fontlist = fm.findSystemFonts(fontpaths=os.getcwd(), fontext='ttf')

if True:
    font_name = fm.FontProperties(fname=target_fonts_path).get_name()
    rc('font', family=font_name)

    plt.scatter([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
    plt.title('타이틀 입니다.')
    plt.xlabel('X축 라벨')
    plt.ylabel('Y축 라벨')
    plt.grid(True)
    plt.show()
