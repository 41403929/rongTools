from pyecharts.charts import Map,Geo
from pyecharts import options
import numpy as np
import pandas as pd
 
df = pd.read_csv('./datas.csv')
datas = df.iloc[:,1]
country = df.iloc[:,0]

map_version = {}  #定义空字典
for i in range(len(country)):
    name = country[i]   #国家名
    data = datas[i]   #该国家疫情人数
    if name in map_version:
        map_version[name] = int(data)  + map_version[name]
    else:
        map_version[name] = int(data)  #将国家和人数以键值对的形式传入字典
 
element = list(map_version.items())
# rgb(135,206,250)
map = Map(options.InitOpts(bg_color="#fff",page_title='World Apple Production by Country')).\
    add(series_name="World Apple Production by Country",  #名称
        data_pair=element,   #传入数据
        is_map_symbol_show=False,  #不显示标记
        maptype='world',   #地图类型
        )
#设置全局配置项
map.set_global_opts(visualmap_opts=options.VisualMapOpts(
                        max_=10000000,
                        is_piecewise=True,
                        pieces=[
                            {"min": 10000000,                   "color": "#4E9674"},
                            {"min": 1000000, "max": 9999999,    "color": "#38C4A1"},
                            {"min": 100000, "max": 999999,      "color": "#86D9CA"},
                            {"min": 10000, "max": 99999,        "color": "#C3EDE5"},
                            {"min": 10,"max": 9999,             "color": "#EAF7FA"},]))
#设置系列配置项
map.set_series_opts(label_opts=options.LabelOpts(is_show=False))  #不显示国家名
map.render('map.html')  #命名并保存
print(country) 
# 第一种
# "color": "#ff00cc"
# "color": "#ff66cc"
# "color": "#ff99cc"
# "color": "#ffcccc"
# "color": "#ffffcc"
# 第二种
# "color": "#ff0099"
# "color": "#ff6699"
# "color": "#ff9999"
# "color": "#ffcc99"
# "color": "#ffff99"
# 第三种
# "color": "#ff0066"
# "color": "#ff6666"
# "color": "#ff9966"
# "color": "#ffcc66"
# "color": "#ffff66"
# 第四种
# "color": "#4E9674"
# "color": "#38C4A1"
# "color": "#86D9CA"
# "color": "#C3EDE5"
# "color": "#EAF7FA"
