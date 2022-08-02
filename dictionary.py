district={
    'Kowloon City':{
        'Whampoa':['A','B','C','D','E'],
        'Mong Kok':['F','G','H','I'],
        'Tsim Sha Tsui':['J','K','L',],
        'Sham Shui Po':['M','N','O'],
        'Yau Tsim Mong':['P','Q','R']
    },
    'Hong Kong Island':{
        'the Central':['S','T','U','W','X'],
        'Causeway Bay':['Y','Z','A'],
        'Cyberport':['B','C','D','E']
    }
}
for i in district['Kowloon City']:
	print(i)

for i in district['Kowloon City']['Whampoa']:
	print(i)