from asyncore import write
import csv 

with open('users.csv', 'w') as csvfile:
    fieldnames=['userId','username','name']
    write= csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    write.writeheader()
    write.writerow({'userId': '1',
                   'username': 'Sakenita',
                   'name': 'Sara Arias'})
    write.writerow({'userId': '2',
                   'username': 'Siodor',
                   'name': 'Andre Salas Aguilar'})
    write.writerow({'userId': '3',
                   'username': 'Frost',
                   'name': 'Gabriel Santos'})
    write.writerow({'userId': '4',
                   'username': 'N64RX',
                   'name': 'Ramiro Gonzales'})
    write.writerow({'userId': '5',
                   'username': 'Prueba',
                   'name': 'Ramiro Teran'})
    write.writerow({'userId': '6',
                   'username': 'alfonzo',
                   'name': 'Alfonzo Gonzales'})
    write.writerow({'userId': '7',
                   'username': 'LA',
                   'name': 'Larry'})
    write.writerow({'userId': '8',
                   'username': 'Bigboss',
                   'name': 'Solid Snake'})
    write.writerow({'userId': '9',
                   'username': 'andres',
                   'name': 'Andres Gonzales'})    
    