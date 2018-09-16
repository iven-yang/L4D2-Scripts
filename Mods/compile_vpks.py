import os
from subprocess import Popen

filenames= os.listdir(".")

results = []
for filename in filenames:
    # Get all folders except the git folder and vpk output folder
    if os.path.isdir(os.path.join(os.path.abspath("."), filename)) and filename != '.git':
        results.append(filename)

vpk_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Left 4 Dead 2\bin\vpk.exe'

for result in results:
    p=Popen(['vpk.exe', result], executable=vpk_dir)
    p.communicate()

print('Packaging VPKs complete')
