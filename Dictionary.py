dictionary =  {}
    
print('Would you like to add something to your dictionary?')
print('Type "1" if you want to, and "2" if you do not want to.')
a = input()
if a != '1':
    exit()
else:
    while a == '1' or a == '2' or a == '3' or a == '4' :
        if a == '1':
            print("Type '1' if you want to add anything to your dictionary")
            print("Type '2' if you want to delete something from your dicionary")
            print("Type '3' if you want to see your dictionary")
            print("Type '4' if you want to search  definition of word in your dictionary")
            b = input()
            if b == '1':
                print('Please, write any word: ')
                c = input()
                print('Now write definition of that word: ')
                d = input()
                dictionary.update({c: d})
                print('Would you like to go back to menu?')
                print('\n')
                print("Type '1' if you'd like to, and '2' if you wouldn't like to")
                a = input()
            if b == '2':
                print('Write a word that you want to delete from your dictionary')
                e = input()
                if e in dictionary:
                    del(dictionary[e])
                    print('Done!')
                    print('\n')
                else:
                    print("There is no ", e, " in your dictionary")
                    print('Would you like go back to menu?')
                    print('\n')
                    print("Type '1' if you'd like to, and '2' if you wouldn't like to")
                    a = input()
            if b == '3':
                for key in dictionary:
                    print(key, dictionary[key])
                print('Would you like go back to menu?')
                print('\n')
                print("Type '1' if you'd like to, and '2' if you wouldn't like to")
                a = input()
            if b == '4':
                print("Write a word whose definition you would like to see")
                f = input()
                if f in dictionary:
                    print(dictionary[f])
                else:
                    print("There's no ",' " ', f, " ' ", " in your dictionary")
                    print('Would you like go back to menu?')
                    print('\n')
                    print("Type '1' if you'd like to, and '2' if you wouldn't like to")
                    a = input()
                           
                
        
            
                
                                    

