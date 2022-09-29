try:
    archive = open('./FileHandling/test.txt', 'r', encoding='utf8')
    CopyArchive = open('./FileHandling/CopyTest.txt', 'w', encoding='utf8')

    CopyArchive.write(archive.read())
except Exception as e:
    print(e)
finally:
    archive.close()
    ### archive.write('Peter') ### ERROR
    print('Done...')