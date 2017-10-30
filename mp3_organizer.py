import os, shutil
from mutagen.easyid3 import EasyID3


# PATHS
file_path = "/Users/yannickleroux/Downloads/"

nudisco = "/Users/yannickleroux/Music/MUSIC/INDIE\ ROCK\ POP\ ELECTRO/Nu\ Disco\
 2017/".replace('\\', '')

deephouse = "/Users/yannickleroux/Music/MUSIC/DANCE\ HOUSE\ ELECTRO/Deep\
 House/Deep\ House\ 2017/".replace('\\', '')

house = "/Users/yannickleroux/Music/MUSIC/DANCE\ HOUSE\ ELECTRO/House/House\
 2017/".replace('\\', '')

techhouse = "/Users/yannickleroux/Music/MUSIC/DANCE\ HOUSE\ ELECTRO/Tech\
 House/Tech\ House\ 2017/".replace('\\', '')

chillout = "/Users/yannickleroux/Music/MUSIC/AMBIANCE/Chill\ Out\
 2017/".replace('\\', '')

discoedits = "/Users/yannickleroux/Music/MUSIC/70\'s\ 80\'s/DISCO/DISCO\
 EDITS/" .replace('\\', '')


# create a list of all files in the download folder
files = os.listdir(file_path)
files.sort()


def move_file(f,dst):
    '''
    helper function
    Ask user confirmation first and then move the file to the dst path 
    '''
    confirm = input('Do you want to move {0} to {1} ? (y/n) (trash) (quit) -- '.format(f,dst))
    if confirm == 'y':
        shutil.move(src,dst+f)
    if confirm == 'trash':
        shutil.move(src,"/Users/yannickleroux/.Trash/" + f)
    if confirm == 'quit':
        exit()



for f in files:
    if f.endswith(".mp3"): # I'm only intersted in mp3s
        src = file_path + f

        # cree un dict avec les tag ID3 
        audio = EasyID3(src)
        
        # test si contient un tag genre sinon on passe
        try:
            genre = audio['genre'][0]
        except:
            continue
        
        if genre == 'Nu Disco':
            move_file(f,nudisco)

        elif genre == 'Deep House':
            move_file(f,deephouse)

        elif genre == 'House':
            move_file(f,house)
            
        elif genre == 'Tech House':
            move_file(f,techhouse)

        elif genre == 'Chill Out':
            move_file(f,chillout)


