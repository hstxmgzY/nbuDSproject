# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from random import randint
from math import radians, cos, sin, asin, sqrt

'''准备数据'''
places = {
    '山东': [117.000923, 36.675807],
    '河北': [115.48333, 38.03333],
    '吉林': [125.35000, 43.88333],
    '黑龙江': [127.63333, 47.75000],
    '辽宁': [123.38333, 41.80000],
    '内蒙古': [111.670801, 41.818311],
    '新疆': [87.68333, 43.76667],
    '甘肃': [103.73333, 36.03333],
    '宁夏': [106.26667, 37.46667],
    '山西': [112.53333, 37.86667],
    '陕西': [108.95000, 34.26667],
    '河南': [113.65000, 34.76667],
    '安徽': [117.283042, 31.86119],
    '江苏': [119.78333, 32.05000],
    '浙江': [120.20000, 30.26667],
    '福建': [118.30000, 26.08333],
    '广东': [113.23333, 23.16667],
    '江西': [115.90000, 28.68333],
    '海南': [110.35000, 20.01667],
    '广西': [108.320004, 22.82402],
    '贵州': [106.71667, 26.56667],
    '湖南': [113.00000, 28.21667],
    '湖北': [114.298572, 30.584355],
    '四川': [104.06667, 30.66667],
    '云南': [102.73333, 25.05000],
    '西藏': [91.00000, 30.60000],
    '青海': [96.75000, 36.56667],
    '天津': [117.20000, 39.13333],
    '上海': [121.55333, 31.20000],
    '重庆': [106.45000, 29.56667],
    '北京': [116.41667, 39.91667],
    '台湾': [121.30, 25.03],
    '香港': [114.10000, 22.20000],
    '澳门': [113.50000, 22.20000],
}
logs = []
lats = []
names = []
for k, v in places.items():
    names.append(k)
    logs.append(v[0])
    lats.append(v[1])

'''将各个地点进行编号，并放入利用字典保存'''
rood = []
place_num = {}    # key = 地点 value=编号 的字典
num_place = {}    # key = 编号 value=地点 的字典
num = 0
for k in places.keys():
    place_num[k] = num
    num_place[num] = k
    num = num + 1

'''随机生成点之间的路线'''
for i in range(0, num):
    list1 = []
    for j in range(0, num):
        if i > j:  #创造对称矩阵
            list1.append(rood[j][i])
        else:
            list1.append(0)
    if i != num - 1:
        list1[randint(i+1,num-1)]=1  #每一个点都随机找一个点相连(若相连，矩阵置一)
    rood.append(list1)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

'''画图三部曲  '''
'''1.构建若干个trace'''
traces = []
traces.append(
    go.Scattermapbox(
        mode="markers", #点
        text=names,
        lon=logs,
        lat=lats,
        marker={'size': 10},
        # marker_color='red'
    )
)
'''增加地点之间的路径'''
for i in range(0, num):
    for j in range(i,num):
        if rood[i][j] == 1:   #若两点相连，则往列表内加入一条红色连线(trace)
            traces.append(
            go.Scattermapbox(
                mode="lines",
                text=[num_place[i], num_place[j]],
                lon=[places[num_place[i]][0], places[num_place[j]][0]],
                lat=[places[num_place[i]][1], places[num_place[j]][1]],
                marker={'size': 5},
                marker_color='red'
                )
            )
'''画图三部曲  2.figure数据列表展示的样式'''
fig = go.Figure(data=traces)
fig.update_layout(
    margin={'l': 3, 't': 3, 'b': 3, 'r': 3}, #边缘距离
    mapbox={
        'center': {'lon': places['浙江'][0], 'lat': places['浙江'][1]},  #图中心在浙江这里
        'style': "stamen-terrain",
        'zoom': 3  #放大倍数
    },
)
'''画图三部曲  3.使用dash.Dash构建app'''
graph = dcc.Graph(  # 2
    id='example-graph',
    figure=fig  # 地图从这里传入
)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1(id="title", children="中国地图"),  # 1
    html.Div(id='graph',
        children=dcc.Graph(  # 2
        id='example-graph',
        figure=fig  # 地图从这里传入
    )),
    html.Div(id="div", children="")  # 3
])
'''根据经纬度计算两地之间的距离'''
def geodistance(list1,list2):
    lng1, lat1 = list1[0],list1[1]
    lng2, lat2 = list2[0],list2[1]
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]) # 经纬度转换成弧度
    dlon = lng2-lng1
    dlat = lat2-lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance = 2*asin(sqrt(a)) * 6371 * 1000  #地球平均半径，6371km
    distance = round(distance/1000, 3)
    return distance

'''计算图中各点之间的距离'''
distance = []   # 表示最开始两点距离，若不可达，距离为无穷（用10000000表示）
for i in range(0, num):
    list1 = []
    for j in range(0, num):
        if rood[i][j] == 1:
            list1.append(geodistance(places[num_place[i]],places[num_place[j]]))
        elif i == j:
            list1.append(0)
        else:
            list1.append(10000000)
    distance.append(list1)

'''利用Floyd算法来计算最短路径'''
path=[]
for i in range(0, num):  # 初始化全-1 的path矩阵
    list1 = []
    for j in range(0, num):
        list1.append(-1)
    path.append(list1)
for k in range(0, num):
    for i in range(0, num):
        for j in range(0, num):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                path[i][j] = k
'''得到 distanc矩阵表示两点最短距离和path矩阵表示最短距离的路径'''

'''根据path列表来寻找最短路'''
trace1 = []    # 存放最短路径的列表，连线用黄色表示
def printroad(x,y,path):
    place1 = num_place[x]
    place2 = num_place[y]
    if path[x][y] == -1:
        trace1.append(
            go.Scattermapbox(   # 路径的样式
                mode="lines",
                text=[place1, place2],
                lon=[places[place1][0], places[place2][0]],
                lat=[places[place1][1], places[place2][1]],
                marker={'size': 5},
                marker_color = 'yellow'
            )
        )
        return
    else:
        mid = path[x][y]
        printroad(x, mid, path)
        printroad(mid, y, path)

# 实现最短路径算法
def solve_shortest_path():
    print("两点之间的最短路为：")  # 读出两点之间的最短路
    print(distance[place_num[points_name[0]]][place_num[points_name[1]]])
    global trace1
    trace1 = []
    printroad(place_num[points_name[0]], place_num[points_name[1]], path)   # 获得两点之间最短路径
    return None


two_points = []  # 需要选择两个点
points_name = []
SELECTED = ""

def selectPoint(point, double_points, text):
    if len(double_points) == 1 and double_points[0] == point:
        return
    else:
        double_points.append(point)
        points_name.append(text)
        print("Points you selected:{}".format(point))

'''dash地图创建好后，点击响应'''
@app.callback(
    [Output('div', 'children'), Output('graph', 'children')],
    [Input('example-graph', 'clickData')])

def display_click_data(clickData):
    global two_points, SELECTED,points_name,graph
    if clickData:
        point_dict = clickData['points'][0]
        lon = point_dict['lon']
        lat = point_dict['lat']
        text = point_dict['text']
        selectPoint([lon, lat], two_points, text)
        SELECTED += "{}:({},{})   ".format(text, lon, lat)
        MSG = "您选择了" + SELECTED

        if len(two_points) == 2:
            solve_shortest_path()  # 最短路算法实现函数

            two_points = []
            points_name = []
            SELECTED = ""

            global trace1
            fig = go.Figure(data=traces + trace1)
            fig.update_layout(
                margin={'l': 3, 't': 3, 'b': 3, 'r': 3},
                mapbox={
                    'center': {'lon': places['浙江'][0], 'lat': places['浙江'][1]},
                    'style': "stamen-terrain",
                    'zoom': 3
                },
            )
            graph = dcc.Graph(  # 2
                id='example-graph',
                figure=fig  # 地图从这里传入
            )
        return MSG, graph
    else:
        return "请选择两个点", graph


if __name__ == '__main__':
    app.run_server(debug=True, port=8056)








