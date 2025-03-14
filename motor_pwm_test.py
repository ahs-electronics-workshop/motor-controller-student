import time
import board
import pwmio
from adafruit_motor import motor

PWM_PIN_A1 = board.D10  # pick any pwm pins on their own channels
PWM_PIN_A2 = board.D9
PWM_PIN_B1 = board.D7  # pick any pwm pins on their own channels
PWM_PIN_B2 = board.D8

# DC motor setup
pwm_a1 = pwmio.PWMOut(PWM_PIN_A1, frequency=50)
pwm_a2 = pwmio.PWMOut(PWM_PIN_A2, frequency=50)
motor1 = motor.DCMotor(pwm_a1, pwm_a2)

pwm_b1 = pwmio.PWMOut(PWM_PIN_B1, frequency=50)
pwm_b2 = pwmio.PWMOut(PWM_PIN_B2, frequency=50)
motor2 = motor.DCMotor(pwm_b1, pwm_b2)

print("***DC motor test***")

print("Forwards slow")
motor1.throttle = 0.5
motor2.throttle = 0.5
print("-- throttle:", motor1.throttle)
time.sleep(1)

print("Stop")
motor1.throttle = 0
motor2.throttle = 0
print("-- throttle:", motor1.throttle)
time.sleep(1)

print("Forwards")
motor1.throttle = 1.0
motor2.throttle = 1.0
print("-- throttle:", motor1.throttle)
time.sleep(1)

print("Stop")
motor1.throttle = 0
motor2.throttle = 0
print("-- throttle:", motor1.throttle)
time.sleep(1)

print("Backwards")
motor1.throttle = -1.0
motor2.throttle = -1.0
print("-- throttle:", motor1.throttle)
time.sleep(1)

print("Stop")
motor1.throttle = 0
motor2.throttle = 0
print("--throttle:", motor1.throttle)
time.sleep(1)

print("Backwards slow")
motor1.throttle = -0.5
motor2.throttle = -0.5
print("--throttle:", motor1.throttle)
time.sleep(1)

print("Stop")
motor1.throttle = 0
motor2.throttle = 0
print("-- throttle:", motor1.throttle)
time.sleep(1)

print("Spin freely")
motor1.throttle = None
motor2.throttle = None

print("--throttle:", motor1.throttle)

print("***Motor test is complete***")