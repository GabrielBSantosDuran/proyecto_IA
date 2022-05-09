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
    
    
    