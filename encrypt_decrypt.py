import pyAesCrypt
import os
import pyfiglet
from colorama import *

figl = pyfiglet.figlet_format('Fayl SHIFR', font='slant')
print(figl)

def encryption(file, password):

    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size
    )

    print(Fore.GREEN+'[Fayl {str(os.path.splitext(file)[0])} shifrlandi')

    os.remove(file)

def decryption(file, password):

    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    print(Fore.GREEN+f'[Fayl {str(os.path.splitext(file)[0])} shifrdan olindi')

    os.remove(file)


def fayllar_boyicha_sayr(dir, password):
    for nomi in os.listdir(dir):
        path = os.path.join(dir, nomi)

        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)

        else:
            fayllar_boyicha_dec(path, password)

def fayllar_boyicha_dec(dir, password):
    for nomi in os.listdir(dir):
        path = os.path.join(dir, nomi)

        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)

        else:
            fayllar_boyicha_dec(path, password)

if __name__ == '__main__':
    try:
        tanla = int(input(Fore.MAGENTA+'Encrypt[1] Decrypt[0] : '))
    except:
        pass


    if tanla == 1:
        password = input(Fore.GREEN+'Shifr parolini kiriting: ')
        toffol = input(Fore.GREEN+'Shifrlamoqchi bolgan faylingizni yolini kiriting: ')
        fayllar_boyicha_sayr(toffol, password)
    elif tanla == 0:
        password = input(Fore.GREEN+'Shifr parolini kiriting: ')
        toffol = input(Fore.GREEN+'Shifrlamoqchi bolgan faylingizni yolini kiriting: ')
        fayllar_boyicha_dec(toffol, password)
    else:
        x = input(Fore.RED+'Dasturda xatolik!!!')

    y = input('Dastur yakunlash uchun ETERni bosing!!!')


