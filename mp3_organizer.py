import os, shutil
from mutagen.easyid3 import EasyID3


# PATHS
file_path = "/Users/yannickleroux/Downloads/"

nudisco = "/Users/yannickleroux/Music/MUSIC/INDIE\ ROCK\ POP\ ELECTRO/Nu\ Disco\
 2018/".replace('\\', '')

deephouse = "/Users/yannickleroux/Music/MUSIC/DANCE\ HOUSE\ ELECTRO/Deep\
 House/Deep\ House\ 2018/".replace('\\', '')

house = "/Users/yannickleroux/Music/MUSIC/DANCE\ HOUSE\ ELECTRO/House/House\
 2018/".replace('\\', '')

techhouse = "/Users/yannickleroux/Music/MUSIC/DANCE\ HOUSE\ ELECTRO/Tech\
 House/Tech\ House\ 2018/".replace('\\', '')

chillout = "/Users/yannickleroux/Music/MUSIC/AMBIANCE/Chill\ Out\
 2018/".replace('\\', '')

discoedits = "/Users/yannickleroux/Music/MUSIC/70\'s\ 80\'s/DISCO/DISCO\
 EDITS/".replace('\\', '')

eighties = "/Users/yannickleroux/Music/MUSIC/70\'s\ 80\'s/80\'s/".replace('\\', '')

disco = "/Users/yannickleroux/Music/MUSIC/70\'s\ 80\'s/DISCO/".replace('\\', '')

dancefloor = "/Users/yannickleroux/Music/MUSIC/DANCE\ HOUSE\ ELECTRO/2018\
 Download/".replace('\\', '')

hiphop = "/Users/yannickleroux/Music/MUSIC/RAP\ R\ N\ B/2018\ rap/".replace('\\', '')

acapella = "/Users/yannickleroux/Music/MUSIC/ACAPELLAS/".replace('\\','')

varietes_inter = "/Users/yannickleroux/Music/MUSIC/VARIETE\ INTERNATIONALE/2018".replace('\\','')

soul = "/Users/yannickleroux/Music/MUSIC/SOUL/".replace('\\', '')

jazz = "/Users/yannickleroux/Music/MUSIC/JAZZ\ ANNEES\ 30\ CROONER/".replace('\\', '')

france = "/Users/yannickleroux/Music/MUSIC/VARIETE\ FRANCAISE/".replace('\\', '')


# create a list of all files in the download folder
files = os.listdir(file_path)
files.sort()


def move_file(f,dst):
    '''
    helper function
    Ask user confirmation first and then move the file to the dst path
    '''
    confirm = input('Do you want to move {0} to {1} ? (y/n) (t=trash, dh=deephouse etc) or (quit) -- '.format(f,dst))
    if confirm == 'y':
        shutil.move(src,dst+f)
    if confirm == 't':
        shutil.move(src,"/Users/yannickleroux/.Trash/" + f)
    if confirm == 'quit':
        exit()

    if confirm == 'dh':
        shutil.move(src, deephouse + f )

    if confirm == 'h':
        shutil.move(src, house + f )

    if confirm == 'th':
        shutil.move(src, techhouse + f )

    if confirm == 'nd':
        shutil.move(src, nudisco + f )

    if confirm == 'co':
        shutil.move(src, chillout + f )

    if confirm == 'df':
        shutil.move(src, dancefloor + f )

    if confirm == 'soul':
        shutil.move(src, soul + f )

    if confirm == 'jazz':
        shutil.move(src, jazz + f )


    print ('**')
    print ('**')



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

        if genre =='Indie Dance / Nu Disco' or genre == 'Nu Disco':
            move_file(f,nudisco)

        elif genre == 'Deep House':
            move_file(f,deephouse)

        elif genre == 'House':
            move_file(f,house)

        elif genre == 'Tech House':
            move_file(f,techhouse)

        elif genre == 'Chill Out':
            move_file(f,chillout)

        elif genre in ['Dance','Future House']:
            move_file(f,dancefloor)

        elif genre =='Pop':
            move_file(f, varietes_inter)

        elif genre =='Acapella':
            move_file(f,acapella)

        elif genre =='80\'s':
            move_file(f,eighties)

        elif genre =='Soul':
            move_file(f,soul)

        elif genre =='Disco':
            move_file(f,disco)

        elif genre =='Variété Française':
            move_file(f,france)

        elif genre =='Disco Edits':
            move_file(f,discoedits)

        elif genre =='Jazz':
            move_file(f,jazz)

        elif genre =='Hip Hop':
            move_file(f,hiphop)



