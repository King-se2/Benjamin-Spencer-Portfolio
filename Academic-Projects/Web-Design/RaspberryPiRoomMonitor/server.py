# Simple demo of the VL53L1X distance sensor.
# Will print the sensed range/distance every second.
import socket
import encodings
import time
import board
import adafruit_vl53l1x
import datetime


HOST = '127.0.0.1' #Fill in with local host of PI
PORT = 10370

i2c = board.I2C()  # uses board.SCL and board.SDA

vl53 = adafruit_vl53l1x.VL53L1X(i2c)

# OPTIONAL: can set non-default values
vl53.distance_mode = 1
vl53.timing_budget = 100

vl53.start_ranging()

def is_person(data):
    if data<863:
        return True
    else:
        return False

def send_data():
    with conn:
            print('Connected by', addr)
            data = conn.recv(1024).decode('ascii')

            if str(data) == "Data":
                print("Sending Data")

                my_data = datetime.datetime.now() #Sends DateTime to client

                encoded_data = my_data.encode('ascii')

                conn.sendall(encoded_data)

            if str(data) == "Quit":
                print("shutting down server")
                

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server waiting for client to connect")
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
    while True:
        if vl53.data_ready:
            data = is_person(vl53.distance)
            print("Distance: {} cm".format(vl53.distance))
            vl53.clear_interrupt()
            time.sleep(1.0)
            if data:
                send_data()
