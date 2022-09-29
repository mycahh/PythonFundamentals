from CustomWith import CustomWith

with CustomWith('./FileHandling/test.txt') as archive:
    print(archive.read())