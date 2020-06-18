""" Get Live Records of COVID-19 """

__auth__ = 'ABHINAV BILWANKAR'

from covid import Covid
c = Covid()
print()
print('\n\n\t\t\t\t ','='*28)
print('\t\t\t\t | '," COVID-19 Live Tracker ",'  |')
print('\t\t\t\t ','='*28,'\n')


heading = '[ Get to Know Status of COVID-19 by choosing below numbers: ]'
print('-'*60)
print(heading)
print('-'*60)

L = ['Press <1> To get know by Country ID                        ||',
     'Press <2> To get know by Country Name                      ||',
     'Press <3> To get know Total Active Cases World-Wide        ||',
     'Press <4> To get know Total Confirmed Cases World-Wide     ||',
     'Press <5> To get know Total Deaths World-Wide              ||',
     'Press <6> To get know Total Recovered World-Wide           ||',
     'Press <7> To get know List of Countries World-Wide         ||',
     'Press <0> To get know Credits                              ||']
print('\n','='*60)

for options in L:
     print('||',options)
print('='*60)

try:
     choose = int(input('\nPlease, Choose any number to get know about COVID-19\n>>> '))

     
## Data by Country ID:
     if choose == 1:
          C_ID = input('\nPlease, provide Country ID: ')
          data = c.get_status_by_country_id(C_ID)
          for k,v in data.items():
               print('{}: {}'.format(k,v))
               
## Data by Country Name:        
     elif choose == 2:
          C_Name = input('\nPlease, provide Country Name: ')
          data = c.get_status_by_country_name(C_Name)
          for k,v in data.items():
               print('{}: {}'.format(k,v))
               
## Active Cases:
     elif choose == 3:
          print(f'\nTotal Active Cases World Wide: {c.get_total_active_cases()}')

## Confirmed Cases: 
     elif choose == 4:
          print(f'\nTotal Confirmed Cases World Wide: {c.get_total_confirmed_cases()}')

## Death Cases:
     elif choose == 5:
          print(f'\nTotal Deaths World Wide: {c.get_total_deaths()}')

## Recovered Cases:
     elif choose == 6:
          print(f'\nTotal Recovered World Wide: {c.get_total_recovered()}')

## Countries:
     elif choose == 7:
          data = c.list_countries()
          n = 0
          for c_names in data:
               n += 1
               print(n,c_names['name'])
          print('\nNumber of Countries Affected: ',n)
          

## Credit for COVID Python Library:
     elif choose == 0:
          print('\nAuthor of Python COVID Library: {}'.format(c.source))
          
     else:
          print('Please, Select Number from given Numbers')
except:
     print()
     print('\t','!'*49)
     print('\t','|  OOPs Something Went Wrong...                 |\n\t |  Sorry, Please Try Again after some time...   |')
     print('\t','!'*49)

message = ' STAY HOME | STAY SAFE '

print('\n\n\t\t\t\t ','='*28)
print('\t\t\t\t|| Author: ',__auth__,'||')
print('\t\t\t\t ','='*28)

print('\n\n\n\n',message.center(120,'@'))
