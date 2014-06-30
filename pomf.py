#!/usr/bin/env python2
import requests
import subprocess
import random
import glob
import os
import sys
from time import sleep

class pomf:
    def __init__(self):
        self.generateName()
        self.takeScreenshot()
        self.uploadedUrl = "http://a.pomf.se/%s" % self.uploadScreenshot()['files'][0]['url']
        self.clipboardThatShit()
        self.removeImages()
        print(self.uploadedUrl)

    def takeScreenshot(self):
        subprocess.check_output(['scrot', self.fileName])
        return True

    def generateName(self):
        self.fileName = "/tmp/pomf-py-%d.png"%random.randint(10000, 99999)
        return True

    def uploadScreenshot(self):
        self.uploadRequest = requests.post("http://pomf.se/upload.php", files={'files[]': open(self.fileName, 'rb')})
        return self.uploadRequest.json()

    def clipboardThatShit(self):
        lol = subprocess.Popen(['xsel', '-psbi'], stdin=subprocess.PIPE)
        lol.communicate(input=self.uploadedUrl)
        return True

    def removeImages(self):
        files = glob.glob('/tmp/pomf-py-*.png')
        for xd in files:
            os.remove(xd)
        return True

if __name__ == "__main__":
    pomf()