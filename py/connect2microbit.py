# serial '/dev/tty.usbmodem11102'
import serial
import matplotlib.pyplot as plt
import numpy as np

# シリアルポートとボーレートを設定
ser = serial.Serial('/dev/tty.usbmodem11102', 115200)

# データを格納する配列を初期化
vals = np.full(800, 300)

# プロットを初期化
plt.ion()
fig, ax = plt.subplots()
plot_line, = ax.plot(vals)

while True:
    # シリアルポートからデータを読み取る
    if ser.in_waiting:
        data_line = ser.readline().strip()
        try:
            val = float(data_line)
        except ValueError:
            continue  # 変換できない場合は次のループに進む

        # データを配列に追加
        vals = np.roll(vals, -1)
        vals[-1] = val

        # プロットを更新
        plot_line.set_ydata(vals)
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        plt.pause(0.01)

# シリアルポートを閉じる
ser.close()
