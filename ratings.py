from asyncore import write
import csv 

with open('ratings.csv', 'w') as csvfile:
    fieldnames=['userId','repoId','rating']
    write= csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    write.writeheader()
    write.writerow({'userId':'1',
                    'repoId':'1',
                    'rating':'2'})
    write.writerow({'userId':'2',
                    'repoId':'2',
                    'rating':'3'})
    write.writerow({'userId':'1',
                    'repoId':'3',
                    'rating':'4'})
    write.writerow({'userId':'1',
                    'repoId':'4',
                    'rating':'5'})
    write.writerow({'userId':'1',
                    'repoId':'5',
                    'rating':'3'})
    write.writerow({'userId':'3',
                    'repoId':'2',
                    'rating':'4'})
    write.writerow({'userId':'4',
                    'repoId':'3',
                    'rating':'2'})
    
    
    
       
    