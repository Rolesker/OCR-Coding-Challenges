def print_song(starting_num):
    for i in range(2,starting_num+1)[::-1]:
        print(str(i)+" green bottles sitting on the wall \n"+str(i)+" green bottles sitting on the wall \nAnd if one green bottle should accidentally fall \nThere'll be "+str(i-1)+" green bottles sitting on the wall \n")
    print("1 green bottle sitting on the wall \n1 green bottle sitting on the wall \nAnd if one green bottle should accidentally fall \nThere'll be no green bottles sitting on the wall")
print_song(3)