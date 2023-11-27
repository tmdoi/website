import time
import datetime
import serial
import ambient

am_v = ambient.Ambient(6273x,'e806320c61cf328x')
# am_i = ambient.Ambient(6273x,'5b1f13e2de2e09cx')
# am_w = ambient.Ambient(6273x,'e0f03ae39a9fcc5x')

#Class for acquiring data_データを取得するためのクラス
class GetData:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0',115200,timeout=None)
        print('Port Open')
        print("")
    def GetData(self):
        #Acquire data from sensors_センサからのデータを取得
        v_string="Sent data"
        self.ser.write(f"{v_string}\n".encode())
        print("Wait data from microbit")

        line = self.ser.readline()
        print("Recieve data")
        line_So=eval(line)
        data_watt,data_voltage,data_current = line_So
        print(data_watt, data_voltage, data_current)
        print("")

        return data_watt,data_voltage,data_current

def amSend(am, data):

    # Send data to Ambient_Ambientにデータを送信
    r = am.send(data)
    print(data)

GD = GetData()

# Time interval to acquire data_データを取得する時間間隔
# 6 for a 1-hour experiment, 30 for a 1-week experiment
# １時間実験なら 6、１週間実験なら 30を設定
interval = 6

while(True):
    try:
        start_time = time.time()#Record processing start time_処理開始時間を記録
        dt_now = datetime.datetime.now()#Time acquisition for recording_記録用の時間取得
        dt_now_arranged = dt_now.strftime('%Y/%m/%d %H:%M:%S.%f')#タイムスタンプの形式変換
        data_watt,data_voltage,data_current = GD.GetData() #Time stamp format conversion_データ取得
        dic_v = {"d1":data_voltage}
        dic_i = {"d1":data_current}
        dic_w = {"d1":data_watt}

        amSend(am_v,dic_v)
        # amSend(am_i,dic_i)
        # amSend(am_w,dic_w)

        pro_time = time.time() - start_time #Calculate time spent processing_処理にかかった時間を計算
        wait_time = interval - pro_time ##Calculate time to adjust interval to acquire data_データを取得する間隔を調整する時間を計算
        print(f'Interval {interval}: ProcessingTime {pro_time}, Wait_time {wait_time}')
        print("")
        time.sleep(wait_time) #Time Adjustment_時間調整

    except Exception as e:
        print(e)

ser.close()
