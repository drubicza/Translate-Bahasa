import os
import sys
import time
import requests
import json

merah  = '\x1b[1;91m'
lime   = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru   = '\x1b[1;94m'
ungu   = '\x1b[1;95m'
blue   = '\x1b[1;96m'
putih  = '\x1b[1;97m'
tutup  = '\x1b[0m'

try:
    data = open('jangan_di_rename_ntar_error.json')
    kimak = json.loads(data.read())
    me = kimak['nama']
    ur = kimak['url']
except IOError:
    exit(tutup + '[' + merah + '!' + tutup + '] Terjadi kesalahan' + tutup)

logos = '\x1b[0m\n +-+-+-+-+-+-+-+-+-+- \n |\x1b[1;91mT\x1b[0m|\x1b[1;91mr\x1b[0m|\x1b[1;91ma\x1b[0m|\x1b[1;91mn\x1b[0m|\x1b[1;91ms\x1b[0m|\x1b[1;91ml\x1b[0m|\x1b[1;91ma\x1b[0m|\x1b[1;91mt\x1b[0m|\x1b[1;91me\x1b[0m \n +-+-+-+-+-+-+-+-+-+-\n \x1b[0mAuthor \x1b[1;94m' + me + '\n \x1b[0mGithub \x1b[1;94m' + ur + '\n' + tutup
indonesia = 'id'
inggris = 'en'
api = 'trnsl.1.1.20190811T093056Z.c49ad2b84a78db90.3c8791321fcf6ba39a3a12ce331dd5ff7e5271eb'

def pilih():
    os.system('clear')
    print logos
    print tutup + '[' + lime + '1' + tutup + '] Indonesia - English'
    print tutup + '[' + lime + '2' + tutup + '] English - Indonesia'
    print tutup + '[' + merah + '0' + tutup + '] Exit'
    print
    cok = raw_input(lime + 'Choose language' + tutup + '> ')
    if cok == '':
        exit(tutup + '[' + merah + '!' + tutup + '] Please input' + tutup)
    elif cok in ('1', '01'):
        indonesia()
    elif cok in ('2', '02'):
        english()
    else:
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)


def indonesia():
    os.system('clear')
    print logos
    print tutup + ' [' + lime + 'Indonesia - English' + tutup + ' ]' + tutup
    print
    ids = raw_input(blue + 'Masukkan teks' + tutup + ' : ')
    if ids == '':
        exit(tutup + '[' + merah + '!' + tutup + '] Please input' + tutup)
    else:
        print tutup + 'Translate to english ...\n'
        time.sleep(1)
        r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=' + api + '&text=' + str(ids) + '&lang=en')
        s = json.loads(r.text)
        done = s['text']
        print blue + 'English ' + tutup + ':' + tutup
        print tutup + str(done)
        lagi = raw_input(tutup + '\nAgain [y/n]? : ')
        if lagi == 'y':
            indonesia()
        elif lagi == 'n':
            pilih()
        else:
            exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)


def english():
    os.system('clear')
    print logos
    print tutup + ' [' + lime + 'English - Indonesia' + tutup + ' ]' + tutup
    print
    ids = raw_input(blue + 'Enter the text' + tutup + ' : ')
    if ids == '':
        exit(tutup + '[' + merah + '!' + tutup + '] Please input' + tutup)
    else:
        print tutup + 'Translate to indonesia ...\n'
        time.sleep(1)
        r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=' + api + '&text=' + str(ids) + '&lang=id')
        s = json.loads(r.text)
        done = s['text']
        print blue + 'Indonesia ' + tutup + ':' + tutup
        print tutup + str(done)
        lagi = raw_input(tutup + '\nAgain [y/n]? : ')
        if lagi == 'y':
            english()
        elif lagi == 'n':
            pilih()
        else:
            exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)


if __name__ == '__main__':
    pilih()
