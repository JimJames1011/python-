#案例介绍
#JSON数据格式的转换
import json

from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

data=[{"name":"Jim","age":19}]
#通过json.dumps(data)方法把python数据转化成了json数据
data=json.dumps(data)
#通过json.dumps(data)方法把json数据转化成了python数据
data=json.loads(data)
print(data)

#pyecharts模块
#基础折线图
from pyecharts.charts import Line

#得到折线图对象
line=Line()
#添加x轴数据
line.add_xaxis(["China",'America','Italy'])
#添加y轴数据
line.add_yaxis('Gdp',[30,20,10])
#生成图表
line.render()

#设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_top="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()

#数据处理
f_us=open("D:/America.txt","r",encoding="UTF-8")
us_data=f_us.read()
#去掉不符合JSON规范的开头
us_data=us_data.replace("jsonp_162933_6364(","")
#去掉不符合JSON规范的结尾
us_data=us_data[:-2]
#JSOn转Python字典
us_dict=json.loads(us_data)