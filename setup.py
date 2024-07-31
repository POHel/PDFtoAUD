import os
import sys

print('Created by SKATT')
print('''
	 ▄█▀▀▀█▄████▀▀▀██████▀▀██▀▀██████▀   ▀███▀███▀▀▀██▄
	▄██    ▀█ ██    ▀██▀   ██   ▀███       █   ██   ▀██▄
	▀███▄     ██   █       ██     ██       █   ██   ▄██
	  ▀█████▄ ██████       ██     ██       █   ███████
	▄     ▀██ ██   █  ▄    ██     ██       █   ██
	██     ██ ██     ▄█    ██     ██▄     ▄█   ██
	█▀█████▀▄██████████  ▄████▄    ▀██████▀▀ ▄████▄
''')
print('installing modules...')
os.system('pip install pypdf')
os.system('pip install text-to-speech')
os.system('pip install colorama')
try:
	import main
except:
	sys.exit()