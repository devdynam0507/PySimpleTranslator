from py_translator import Translator
import asyncio
import threading
import time

LANG = ['ko', 'en']

thread = None #Current waiting task queue thread

def get_lang(index):
    return LANG[index]

def translate(dest, text):
    t = Translator()
    return t.translate(text=text, dest=dest).text

# class Test(object):
#
#     def callback(self, text):
#         print("callback: " + text)
#
# word = ['d', 'a', 'c', 'adawdaw', 'adwada']
#
# for value in word:
#     t = Test()
#     t = TranslatorThread('ko', value, t)
#     t.start()