#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C as I2C
import time
import os

ACCEL_GYRO_ADD = 0x6b
MAG_ADD = 0x1e
PITCH_MSB = 0x19
PITCH_LSB = 0x18
ROLL_MSB = 0x1b
ROLL_LSB = 0x1a
YAW_MSB = 0x1d
YAW_LSB = 0x1c
ACC_X_MSB = 0x29
ACC_X_LSB = 0x28
ACC_Y_MSB = 0x2b
ACC_Y_LSB = 0x2a
ACC_Z_MSB = 0x2d
ACC_Z_LSB = 0x2c
MAG_X_MSB = 0x29
MAG_X_LSB = 0x28
MAG_Y_MSB = 0x2b
MAG_Y_LSB = 0x2a
MAG_Z_MSB = 0x2d
MAG_Z_LSB = 0x2c

#Accerometer and gyroscope output data resolution register
CTRL_REG1_G = 0x10

#Magnetometer operation mode register
CTRL_REG3_M = 0x22

#IMU class for Sparkfun LSM9DS1 9-axis IMU
class IMU(object)

   #constructor
   def __init__(self)
      
      #Assign the accelerometer and gyroscope device address, and magnetometer device address
      self.accel_gyro_add = I2C(ACCEL_GYRO_ADD)
      self.mag_add = I2C(MAG_ADD)
      
      #create lists of accelerometer, gyro, and magnetometer registers 
      acc_x = [ACC_X_MSB, ACC_X_LSB]
      acc_y = [ACC_Y_MSB, ACC_Y_LSB]
      acc_z = [ACC_Z_MSB, ACC_Z_LSB]
      pitch = [PITCH_MSB, PITCH_LSB]
      roll = [ROLL_MSB, ROLL_LSB]
      yaw = [YAW_MSB, YAW_LSB]
      mag_x = [MAG_X_MSB, MAG_X_LSB]
      mag_y = [MAG_Y_MSB, MAG_Y_LSB]
      mag_z = [MAG_Z_MSB, MAG_Z_LSB]

      #dump registers into parent lists
      self.accel = [acc_x, acc_y, acc_z]
      self.gyro = [pitch, roll, yaw]
      self.mag = [mag_x, mag_y, mag_z]

      #set accelerometer and gyroscope data rate
      I2C.write8(self.accel_gyro_addr, CTRL_REG1_G, 0xc0) #0xc0 is 952 Hz

   #Method to read accelerometer data
#   def read_accel(self)
      #
#initialize IMU

#set accelerometer and gyroscope data rate
#I2C.write8(accgy, 0x10, 0xc0) #0xc0 is 952 Hz
#I2C.write8(accgy, 0x20, 0xc0) 

#set high resolution mode for accelerometer
#I2C.write8(accgy, 0x21, 0x80)

#set continuous FIFO mode
#I2C.write8(accgy, 0x2E, 0xc0)

#while True:

   #print (I2C.readS

   #read pitch data
#   print "Pitch rate = "
#   print ((I2C.readS8(accgy, pitch_high) << 8) | I2C.readS8(accgy, pitch_low)) / 133.747
   
   #read roll data
#   print "Roll rate = "
#   print ((I2C.readS8(accgy, roll_high) << 8) | I2C.readS8(accgy, roll_low)) / 133.747

   #read yaw data
#   print "Yaw rate = "
#   print ((I2C.readS8(accgy, yaw_high) << 8) | I2C.readS8(accgy, yaw_low)) / 133.747

   #read x data
#   print "x linear rate = "
#   print -1 * ((I2C.readS8(accgy, x_axis_high) << 8) | I2C.readS8(accgy, x_axis_low)) / 16536.0

   #read y data
#   print "y linear rate = "
#   print -1 * ((I2C.readS8(accgy, y_axis_high) << 8) | I2C.readS8(accgy, y_axis_low)) / 16536.0

   #read z data
#   print "z linear rate = "
   #trying this out. data * 3.3 V / 65536 (16 bits)
#   print -1 * ((I2C.readS8(accgy, z_axis_high) << 8) | I2C.readS8(accgy, z_axis_low)) / 16536.0

   #delay for 100 ms
#   time.sleep(.1)
   
   #clear screen
#   os.system('clear')
