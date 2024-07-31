import os
import sys
import time
import text_to_speech
import pypdf
from pypdf import PdfReader as PR


print('Created by SKATT')
print('''
	---------------------------------------------------------------
	 _____  _____  ______ _               _    _ _____ _____ ____  
	|  __ \|  __ \|  ____| |         /\  | |  | |  __ \_   _/ __ \ 
	| |__) | |  | | |__  | |_ ___   /  \ | |  | | |  | || || |  | |
	|  ___/| |  | |  __| | __/ _ \ / /\ \| |  | | |  | || || |  | |
	| |    | |__| | |    | || (_) / ____ \ |__| | |__| || || |__| |
	|_|    |_____/|_|     \__\___/_/    \_\____/|_____/_____\____/ 
	
	---------------------------------------------------------------
''')                                                                                                                               
try:
	answ = input('''
	[1] Скопировать текст из .pdf файла
	[2] Озвучить .pdf файл
	--> ''')
	pdf = input('Введите название файла без расширения: ')
	name = pdf

	def read_pdf():
		reader = PR(f'{name}.pdf')
		num_pag = len(reader.pages)
		page = reader.pages[0]
		text = page.extract_text()
		return text

	def aud():
		from text_to_speech import save
		aud_text = read_pdf()
		language = 'ru'
		output_file = f'{name}.mp3'
		print('Please wait...')
		save(aud_text, language, file=output_file)

	PDFtext = read_pdf()

	if answ == '1':
		print(read_pdf())
		pdf = open(f'{name}.txt', 'w')
		pdf.write(PDFtext)
		pdf.close()
		print(f'Файл {name}.txt сохранён!')

	elif answ == '2':
		aud()
		print('Готово!')
		print(f'Файл {name}.mp3 создан!')
		
	else:
		print('Возникла ошибка!')
		sys.exit()

except KeyboardInterrupt:
    print(f"\n[!] Exiting...")
    sys.exit()