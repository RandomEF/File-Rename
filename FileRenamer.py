import os
import glob

useMenu = False
path = "C:\\Users\\eshan\\Music\\Music\\Deltarune\\Chapter 2\\"
fileName = "1.*"
resultFileName = "*"


def Rename():
    global fileName
    global resultFileName
    global path
    oldName = path + fileName
    files = glob.glob(oldName)
    splitName = fileName.split("*")
    splitResultName = resultFileName.split("*")
    diff = [x for x in splitName if x not in splitResultName]
    for file in files:
        name = [file.removeprefix(path)]
        for x in diff:
            for elem in name:
                temp = elem.split(x)
                skipped = 0
                for i in range(len(temp)):
                    if temp[i] == "":
                        skipped += 1
                        continue
                    name.insert(name.index(elem) + i, temp[i])
                del name[name.index(elem) + i + 1 - skipped]
                name[name.index(elem)] = elem.split(x)
        name = name[0]
        for i in range(name.count("")):
            name.remove("")
        newName = path + "".join(name)
        os.rename(file, newName)


def Menu():
    pass


def main():
    if useMenu:
        Menu()
    else:
        Rename()


if __name__ == '__main__':
    main()
