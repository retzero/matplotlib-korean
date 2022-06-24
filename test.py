import os
import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


font_path = './NanumGothicCoding.ttf'
if not os.path.isfile(font_path):
    print('No font file found')
    sys.exit(0)
font_name = fm.FontProperties(fname=font_path).get_name()

font_files = fm.findSystemFonts(fontpaths=[os.getcwd()])
for font_file in font_files:
    fm.fontManager.addfont(font_file)
plt.rcParams['font.family'] = font_name

# 테스트
if True:
    time_list = [18.1, 6.3, 7.2, 5.5]
    labels = ['08시', '09시', '10시', '11시']

    plt.title('타이틀 입니다.')
    plt.xlabel('X축 라벨')
    plt.ylabel('Y축 ')
    plt.pie(time_list, labels=labels, startangle=120)
    plt.show()
