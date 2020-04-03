#!/bin/python
import sys
import os

def printUsage():
    print("""Usage: backlight <op> <value>
    <op> can be + (add), - (subtract) or = (set)
    <value> is in percentage (min = 0, max = 100)

Example:
    Set brightness to 50% of max brightness:
        backlight = 50
    Lower brightness by 5% of max brightness:
        backlight - 5
    Raise brightness by 25% of max brightness:
        backlight + 25
    Use max brightness:
        backlight = 100
    Put the screen in complete dark:
        backlight = 0

Note:
    * The operator and value MUST be separated by a space, i.e: "+5" or "=10"
    is invalid. This constraint will be relaxed later.
    * The result of a change is clamped to the range [0, 100] (e.g: current
    brightness is 5% and you subtract 10% out of it, the result will be 0%
    instead of -5%)""")
    exit()

def readFile(path):
    with open(path, "r") as f:
        return f.read()

def writeFile(path, data):
    with open(path, "w") as f:
        f.write(data)


brightnessPath = "/sys/class/backlight/intel_backlight/brightness"
maxBrightnessPath = "/sys/class/backlight/intel_backlight/max_brightness"

currentBrightness = int(readFile(brightnessPath))
maxBrightness = int(readFile(maxBrightnessPath))
currentBrightnessRatio = currentBrightness / maxBrightness

if len(sys.argv) == 1:
    print(round(currentBrightnessRatio * 100))
    exit()
if len(sys.argv) != 3:
    printUsage()

operator = sys.argv[1]
try:
    change = float(sys.argv[2]) / 100
except ValueError:
    printUsage()

if operator == '+':
    newBrightnessRatio = min(1, currentBrightnessRatio + change)
elif operator == '-':
    newBrightnessRatio = max(0, currentBrightnessRatio - change)
elif operator == '=':
    newBrightnessRatio = min(1, change)
else:
    printUsage()

newBrightness = int(newBrightnessRatio * maxBrightness)
writeFile(brightnessPath, str(newBrightness))