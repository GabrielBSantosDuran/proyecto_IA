from asyncore import write
import csv 

with open('repos.csv', 'w') as csvfile:
    fieldnames=['repoId','title','categorias','stars']
    write= csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    write.writeheader()
    write.writerow({'repoId':'1',
                    'title':'Avenger Age of Ultron',
                   'categorias': 'Accion',
                   'stars': '8000'})
    write.writerow({'repoId':'2',
                    'title':'Hotel Transilvania',
                   'categorias': 'Animada',
                   'stars': '8050'})
    write.writerow({'repoId':'3',
                    'title':'Star Wars Rogue One',
                   'categorias': 'Ciencia Ficcion',
                   'stars': '7500'})
    write.writerow({'repoId':'4',
                    'title':'Saw',
                   'categorias': 'Terror',
                   'stars': '9000'})
    write.writerow({'repoId':'5',
                    'title':'Spiderman no Way Home',
                   'categorias': 'Accion',
                   'stars': '11000'})

    