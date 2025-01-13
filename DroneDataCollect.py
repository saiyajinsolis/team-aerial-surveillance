from djitellopy import tello
import KeyPressModule as kp
import cv2
import time

testConnection = False
controlDrone = True

kp.init()
me = tello.Tello()
me.connect()
me.streamon()
print(me.get_battery())
global img

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speedI

    if kp.getKey("q"): me.land()
    elif kp.getKey("e"): me.takeoff()

    print(f"Current Speed: {speed}")

    if kp.getKey('p'):
        print("Image Captured")
        cv2.imwrite(f'./Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]

def handScan():
    speed = 15

    me.send_rc_control(speed, 0, 0, 0)
    time.sleep(2)
    me.send_rc_control(0,0,0, speed)
    time.sleep(2)
    me.send_rc_control(-speed, 0, 0, 0)
    time.sleep(2)
    me.send_rc_control(0, 0, 0, -speed)
    time.sleep(2)
    me.send_rc_control(-speed, 0, 0, 0)
    time.sleep(2)
    me.send_rc_control(-speed, 0, 0, 0)
    time.sleep(2)
    me.send_rc_control(0, 0, 0, -speed)
    time.sleep(2)
    me.send_rc_control(-speed, 0, 0, 0)
    time.sleep(2)
    me.send_rc_control(speed, 0, 0, 0)
    time.sleep(2)
    me.send_rc_control(0, 0, 0, speed)
    time.sleep(2)
    me.send_rc_control(speed, 0, 0, 0)
    time.sleep(2)
    me.send_rc_control(0, 0, 0, speed)
    time.sleep(2)

while controlDrone:
    vals = getKeyboardInput()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    
    if kp.getKey("b"): 
        testConnection = True

    while testConnection:
        print(me.get_battery())
        if kp.getKey("b"): 
            testConnection = False

    # if kp.getKey("g"): handScan()

   
    # cv2.imshow("Image", img)
    # cv2.waitKey(1)w






