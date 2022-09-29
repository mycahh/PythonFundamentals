try:
    archive = open('./FileHandling/test.txt', 'r', encoding='utf8')
    ### read = archive.read() ### READ ALL
    ### read = archive.read(3) ### FIRST THREE CHARACTER
    ## firstLine = archive.readline() # FIRST LINE
    ##secondLine = archive.readline() # SECOND LINE
    ## print(f'{firstLine} and {secondLine}')

    ## for linea in archive: # Iter
    ##    print(linea)


    ## allLines = archive.readlines() ## Save it as List
    ## print(f'{allLines} - type{type(allLines)}')

except Exception as e:
    print(e)
finally:
    archive.close()
    ### archive.write('Peter') ### ERROR
    print('Done...')