# -*-coding:utf8;-*-
"""
The MIT License (MIT)

Copyright (c) 2021 sl4awrapper https://github.com/guangrei

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import time
try:
    import androidhelper as sl4a
except ImportError:
    import android as sl4a


class Sl4aWrapper():
    """
    sl4a function wrapper
    """

    def __init__(self):
        self.droid = sl4a.Android()
    """
  sl4a speech recognition and text to speech wrapper
  """

    def listen(self, msg="please speak now!", lang="en-Us", model=None):
        while True:
            ret = self.droid.recognizeSpeech(msg, lang, model)
            if ret.result != None:
                break
            else:
                pass
        return ret.result

    def speak(self, word):
        self.droid.ttsSpeak(word)
        while self.droid.ttsIsSpeaking().result:
            pass
        time.sleep(1)
    """
   sl4a spinner progress wrapper
  """

    def sprogress_start(self, title, message):
        self.droid.dialogCreateSpinnerProgress(title, message)
        self.droid.dialogShow()

    def sprogress_end(self):
        self.droid.dialogDismiss()
