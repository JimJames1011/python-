#地图可视化
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, LabelOpts

map=Map()
data=[("beijing",99),("shangha",199),("hunan",299)]
map.add("地图",data,"china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
            {"min":100,"max":500,"label":"100-500","color":"#990033"},
        ]
    )
)


map.render("map.html")

#柱状图构建
from pyecharts.charts import Bar
bar=Bar()
bar.add_xaxis(["China","America","Italy"])
bar.add_yaxis("GDP",[10,20,30],label_opts=LabelOpts(position="right"))
#反转xy轴
bar.reversal_axis()
bar.render("bar.html")


#基础时间线柱状图绘制
from pyecharts. charts import Bar, Timeline
from pyecharts. options import *
bar1 = Bar()
bar1.add_xaxis(["中国","美","英 "])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts (position="right"))
bar1. reversal_axis()
bar2 = Bar()
bar2.add_xaxis(["中国","美","英"])
bar2.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
timeline = Timeline()
timeline.add(bar1,"2021年GDP")
timeline.add(bar2, "2022年GDP")
# 越过时间线然區
timeline.render("基础槌状图-时间线.html")