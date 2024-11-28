tree_tall = input("받고 싶은 트리의 키는?")

for x in range(int (tree_tall)):
    for y in range(int (tree_tall)):

        if (int(tree_tall)-x <= y+1):
            if(y+1 == int(tree_tall)):
                print("*")
            else:
                print("*",end = " ")

        else:
            print(end = " ")



print("""------------------------------------------------------------
                          Happy CristMas!!!
------------------------------------------------------------""")


end = input("")


                

            





            
        
            
        
