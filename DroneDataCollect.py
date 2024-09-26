from djitellopy import tello
import KeyPressModule as kp
import cv2
import time

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

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
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): yv = me.land()
    elif kp.getKey("e"): yv = me.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]

def handScan():
    speed = 15

    me.send_rc_control(speed, 0, 0, 0)
    sleep(2)
    me.send_rc_control(0,0,0, speed)
    sleep(2)
    me.send_rc_control(-speed, 0, 0, 0)
    sleep(2)
    me.send_rc_control(0, 0, 0, -speed)
    sleep(2)
    me.send_rc_control(-speed, 0, 0, 0)
    sleep(2)
    me.send_rc_control(-speed, 0, 0, 0)
    sleep(2)
    me.send_rc_control(0, 0, 0, -speed)
    sleep(2)
    me.send_rc_control(-speed, 0, 0, 0)
    sleep(2)
    me.send_rc_control(speed, 0, 0, 0)
    sleep(2)
    me.send_rc_control(0, 0, 0, speed)
    sleep(2)
    me.send_rc_control(speed, 0, 0, 0)
    sleep(2)
    me.send_rc_control(0, 0, 0, speed)
    sleep(2)

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    if kp.getKey("g"): handScan()

    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)






