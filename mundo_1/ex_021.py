'''
Desafio 021

Faça um programa em Python que 
abra e reproduza o áudio de um 
arquivo MP3.
'''


import miniaudio

stream = miniaudio.stream_file("/storage/emulated/0/Download/pycode/curso_de_python/python_mundo_1/ex_021.mp3")
device = miniaudio.PlaybackDevice()
device.start(stream)
input("Pressione Enter para parar...")

