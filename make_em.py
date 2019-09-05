import os
import subprocess

path = 'c'

files = []
# r=root, d=directories, f = files

bzList = []
for r, d, f in os.walk(path):
    for file in f:
         if 'fuzz' in r or 'em' in r or 'tools' in r:
            continue
         if '.c' in file:
            fullname = os.path.join(r, file)
            #/bin/obj/[PADZONDER/c/maar/EM/].bc
            os.system('mkdir -p bin/obj/{}'.format(r.replace("c/", 'em/')))
           
            bzName = "bin/obj/{}".format(fullname.replace("c/", 'em/', 1).replace('.cc', '.bc').replace('.c', '.bc'))

            bzList.append(bzName)
         
            os.system('emcc -Ic/include {} -o {}'.format(fullname,bzName))

print("COMPILING NOW")
bzs = ' '.join(bzList)
args = ['echo', "\"" + bzs + "\"", '-o',  "brotli.js"]
os.system("echo " + bzs)
os.system("mkdir -p bin/js")
os.system("emcc -Ic/include --bind c/em/bindings.cc " + bzs +  ' -o ' +  "bin/js/brotli.js" )