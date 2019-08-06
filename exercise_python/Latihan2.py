CatName = []

while True:
    print('Enter your cat name\'s number ' + str(len(CatName)) + \
          ' (Or enter nothing to break).')
    cat = input('> ')
    CatName = CatName + [cat]

    if cat == '':
        break

print('You have ' + str(len(CatName)-1) + ' cat. They are: ')
for name in CatName:
    print('   ' + name)