import os 
import subprocess

font_name = 'Woodbine'

def get_cwd():
    cwd = os.getcwd()
    print("     Current Working Directory: ", cwd)

try:
    print("\n**** Running Fontmake ******************************\n")
    get_cwd()
    subprocess.call(['fontmake', '-g', 'sources/Woodbine.glyphs', '-o', 'variable',])
except:
    print("Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")

print("\n**** Moving fonts to fonts directory *******************\n")
get_cwd()
subprocess.call(['cp', 'variable_ttf/Woodbine-VF.ttf', 'fonts/',])
print("     [+] Done")

print("\n**** Removing build directories  ***********************\n")
get_cwd()
subprocess.call(['rm', '-rf', 'variable_ttf', 'master_ufo',])
print("     [+] Done")

os.chdir("fonts")
print("\n**** Run: ttfautohint  *********************************\n")
get_cwd()
subprocess.call(['ttfautohint', '-I', 'Woodbine-VF.ttf', 'Woodbine-VF-Fix.ttf'])
subprocess.call(['cp', 'Woodbine-VF-Fix.ttf', 'Woodbine-VF.ttf'])
subprocess.call(['rm', '-rf', 'Woodbine-VF-Fix.ttf'])
print("     [+] Done")

os.chdir("..")
print("\n**** Run: gftools  **************************************\n")
get_cwd()
# subprocess.call(['gftools', 'fix-dsgi', 'fonts/Staatliches-Regular.ttf', '--autofix'])

