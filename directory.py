from pathlib import Path

# Absolute Path
# C:\Program File\Microsoft

# Relative Path
# /usr/local/bin

# path = Path("ecommerce")
# print(path.exists())
# print(path.mkdir())     #creates a directory and returns  none
# print(path.rmdir())     #removes a directory

path = Path()

print(path.glob('*'))  # search for all files,all directories and current path
print(path.glob('*.*'))  # gets the files in current directory
print(path.glob('*.py'))  # gets all the .py files

for file in path.glob('*.py'):
    print(file)
