import re


# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def filter_text(text):
    return re.sub(r'\b\w*абв\w*\b', '', text)


# print(filter_text('абва тест абва тест рабва тест крабва'))
