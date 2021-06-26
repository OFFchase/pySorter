

import os
import shutil
import sys


def sortDirectory(directory, func=shutil.copy):

    if not os.path.isdir(directory):
        return 1

    for root, dirs, files in os.walk(directory):
        for file in files:

            name, ext = os.path.splitext(file)
            ext = ext[1:]

            if not os.path.exists(os.path.join("Sorted", ext)):
                os.makedirs(os.path.join("Sorted", ext))

            if os.path.exists(os.path.join("Sorted", ext, file)):
                count = 1
                for newFile in os.listdir(os.path.join("Sorted", ext, '')):
                    if name == "_".join(newFile.split('.')[0].split('_')[:-1]):
                        count += 1
                Sortedfile = name+'_'+str(count)+'.'+ext
            else:
                Sortedfile = file
            print('File:', os.path.join(root, file), '->', os.path.join("Sorted", ext, Sortedfile))
            func(os.path.join(root, file), os.path.join("Sorted", ext, Sortedfile))

    return 0


def main():

    functionDict = {
        'm': shutil.move,
        'c': shutil.copy,
    }
    flag = shutil.copy
    if len(sys.argv) == 3:
        if sys.argv[2].lower()[0] in functionDict:
            flag = functionDict[sys.argv[2].lower()[0]]
        else:
            print("Unsupported 3rd argument. Use 'm'ove or 'c'opy")
            return 1

    elif len(sys.argv) == 1 or len(sys.argv) > 3:
        print("Wrong amount of arguments. Only 2 arguments supported: [path function]")
        return 1

    return sortDirectory(sys.argv[1], flag)


if __name__ == '__main__':
    main()


def someCode():
    iAmGoodProgrammer = "Hello world"
    upperLimit = 10*24+4
    for x in range(upperLimit):
        print(iAmGoodProgrammer, str(x))

    return 1























