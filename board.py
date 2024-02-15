import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import random
# import time

# 宣告變數
player_board = 0
oppnent_board = 1
player_air_1 = 2
player_air_2 = 3
player_air_3 = 4
player_air_4 = 5
oppnent_air_1 = 6
oppnent_air_2 = 7
oppnent_air_3 = 8
oppnent_air_4 = 9
empty_board = 10
last_1 = 11
last_8 = 18
x = np.zeros((19, 19, 19))
x[:, :, empty_board] = 1

# 計算陣列裡的實際位置
def trans_pos(num_x, num_y):
    return 19 - num_y, num_x - 1

# print棋盤陣列
def print_board(s, e):
    for i in range(s, e):
        print(f'board {i}')
        for j in range(0, 19):
            for k in range(0, 19):
                print(int(x[j][k][i]), end = " ")
            print()
        print()

# main
# 創建一個21x21的棋盤，並將所有的值設為0.5
board = np.full((21, 21), 0.5)
# 創建一個咖啡色的色彩映射
colors = ["saddlebrown", "saddlebrown"]
cmap = LinearSegmentedColormap.from_list("mycmap", colors)

# 畫出棋盤
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(board, cmap=cmap, extent=[0, 20, 0, 20])

# 畫出格線
for i in range(1, 20):
    ax.axhline(i, xmin=0.05, xmax=0.95, color='black', zorder=1)
    ax.axvline(i, ymin=0.05, ymax=0.95, color='black', zorder=1)

ax.scatter(4, 4, s=50, c='black', zorder=1)
ax.scatter(4, 10, s=50, c='black', zorder=1)
ax.scatter(4, 16, s=50, c='black', zorder=1)
ax.scatter(10, 4, s=50, c='black', zorder=1)
ax.scatter(10, 10, s=50, c='black', zorder=1)
ax.scatter(10, 16, s=50, c='black', zorder=1)
ax.scatter(16, 4, s=50, c='black', zorder=1)
ax.scatter(16, 10, s=50, c='black', zorder=1)
ax.scatter(16, 16, s=50, c='black', zorder=1)

# 設定軸的範圍
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

# 隱藏x軸和y軸的刻度
ax.set_xticks([])
ax.set_yticks([])

# 定義棋子的顏色，開始時為黑色
color = ['black']

# 定義棋子的位置
positions = []

# 定義滑鼠點擊事件的回調函數
def onclick(event):
    color = ['black']
    ix, iy = event.xdata, event.ydata
    # print(f'x = {ix}, y = {iy}')

    # 計算最近的交叉點
    nearest_x = round(ix)
    nearest_y = round(iy)

    # 只有當滑鼠點擊的位置在中間的19x19的範圍內，並且該位置沒有棋子時，才畫出棋子
    if 1 <= nearest_x <= 19 and 1 <= nearest_y <= 19 and (nearest_x, nearest_y) not in positions:
        ax.scatter(nearest_x, nearest_y, s=400, c=color[0], zorder=2)
        fig.canvas.draw()

        # 將該位置添加到棋子的位置列表中
        print(f'x = {nearest_x}, y = {nearest_y}')
        positions.append((nearest_x, nearest_y))
        nearest_x, nearest_y = trans_pos(nearest_x, nearest_y)
        x[nearest_x][nearest_y][player_board] = 1


        plt.pause(1)

        # 如果是黑棋，則隨機選擇一個還沒下過的位置下白棋
        if color[0] == 'black':
            random_x = random.randint(1, 19)
            random_y = random.randint(1, 19)
            if (random_x, random_y) not in positions:
                ax.scatter(random_x, random_y, s=400, c='white', zorder=2)
                fig.canvas.draw()
                print(f'x = {random_x}, y = {random_y}')
                positions.append((random_x, random_y))
                random_x, random_y = trans_pos(random_x, random_y)
                x[random_x][random_y][oppnent_board] = 1

        print("player")
        print_board(player_board, player_board + 1)
        print("opponent")
        print_board(oppnent_board, oppnent_board + 1)
        # 交換棋子的顏色
        # color[0] = 'white' if color[0] == 'black' else 'black'

# 連接滑鼠點擊事件和回調函數
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# 顯示棋盤
plt.show()
