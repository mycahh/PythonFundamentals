try:
    archive = open('./FileHandling/test.txt', 'w', encoding='utf8')
    archive.write('Hello World\n')
    archive.write('éter')
except Exception as e:
    print(e)
finally:
    archive.close()
    ### archive.write('Peter') ### ERROR
    print('Done...')