# coding=utf-8
#=== pyt268104 home work ===
# 20160627
#import math
#import numpy as np
 
#def fun(a1,a2): 
#   c = np.dot(a1,a2)     
#   return c
import sudoku_tablex1
import sudoku_publib
arealoop=[[1,3,1,3],[1,3,4,6],[1,3,7,9],
          [4,6,1,3],[4,6,4,6],[4,6,7,9],
          [7,9,1,3],[7,9,4,6],[7,9,7,9]              
         ]
level = 1
gcode = 1
pysudokuver = '''
This is Sudoku Game
Desiger: Handel Liao pyt268104
Codeing by Python3.5 
Ver : 1.2 20160725
'''
lev=["Easy","Normal","Hard"]
mtxt = '''
=== Easy Sudoku Game V1.2 pyt268104 Handel ===
*** System Command ***
[1]Level Select (L1:Easy,L2:Normal,L3:Hard)
[2]Game code by LEVEL(1..10)
[3]Show Game Buffer and Status 
[4]select play Game
[?]List Menu
[H]Help info show
[Q]quit
*** Game Command *** 
[N]Add a New Game
[D]Delete a Game
[L]Load Game Data[from level,gcode]
[P]Print Game data array
[K]key in a data to Game
[C]check the Game by Pass
'''

def getsudoku():
    xx = [[0 for i in range(9)] for j in range(9)]
    return xx

def showsudoku(xx):
    print()
    print("="*15,"sudoku data","="*15)
    for i in range(9):
        for j in range(9):
            print("[%2s]"%(xx[i][j]),end="")
            if j in (2,5):
                print("||",end="")
        print()
        if i in (2,5):
            print(("="*12)+"||"+("="*12)+"||"+("="*12))

def setsudoku_area(xx,nn,ll):
    tt=0
    for j in range(9):
        xx[nn-1][j]=ll[tt]
        tt+=1
        
def setsudoku_plan(xx,tab):
    tt=0
    for i in range(9):
        xx[i]=tab[i]

def scanok(yy):#c1: area ,col,raw must be 1 scan 
    for i in range(9):
        for j in range(9):
            if yy.sudokudat[i][j].status == 0:
                yy.sudokudat[i][j].scanchk(yy.sudokudat)
            
    runok=0
    runfail=0
    for i in range(9):
        for j in range(9):
            ll=len(yy.sudokudat[i][j].chkno)
            print("%d%d = %s # %d"%(i+1,j+1,yy.sudokudat[i][j].chkno,ll))
            if yy.sudokudat[i][j].no==0:
                if ll==1:                
                    yy.sudokudat[i][j].no = yy.sudokudat[i][j].chkno[0]
                else:
                    runok+=1

                if ll==0:
                    runfail+=1
                
    return runok,runfail    

def scanok2(yy):#c2: area mabe only 1 scan
    xall=[]
    xpass=[]
    for acode in range(9):
        xall.clear()
        xpass.clear()
        y1,y2,x1,x2 = arealoop[acode]
        y,x = (y1-1),(x1-1)        
        for y in range(y1-1,y2):
            for x in range(x1-1,x2):
                if yy.sudokudat[y][x].no==0 and len(yy.sudokudat[y][x].chkno)>1:
                    for i in yy.sudokudat[y][x].chkno:
                        xall.append(i)
                        
        for i in xall:
            if xall.count(i)==1:
                xpass.append(i)

        if len(xpass)>0:        
            y,x = (y1-1),(x1-1)        
            for y in range(y1-1,y2):
                for x in range(x1-1,x2):
                    if  yy.sudokudat[y][x].no==0 and len(yy.sudokudat[y][x].chkno)>1:
                        for i in xpass:
                            if i in yy.sudokudat[y][x].chkno:
                                yy.sudokudat[y][x].chkno=[]
                                yy.sudokudat[y][x].chkno.append(i)
                                yy.sudokudat[y][x].no=i
                            
    for i in range(9):
        for j in range(9):
            if yy.sudokudat[i][j].status == 0:
                yy.sudokudat[i][j].scanchk(yy.sudokudat)
            
    runok=0
    runfail=0
    for i in range(9):
        for j in range(9):
            ll=len(yy.sudokudat[i][j].chkno)
            print("%d%d = %s # %d"%(i+1,j+1,yy.sudokudat[i][j].chkno,ll))
            if yy.sudokudat[i][j].no==0:
                if ll==1:                
                    yy.sudokudat[i][j].no = yy.sudokudat[i][j].chkno[0]
                else:
                    runok+=1

                if ll==0:
                    runfail+=1
                
    return runok,runfail                             
    pass

def main():
    game=[]
    level = 1
    gcode = 1
    ss="demo"+",("+lev[level-1]+"_"+str(gcode)+")"
    game.append(sudoku_publib.sudoku_dataarray(ss))
    game[0].setsudoku_plan(sudoku_tablex1.demo_1[gcode])
    
    level = 2
    gcode = 1
    ss="demo1"+",("+lev[level-1]+"_"+str(gcode)+")"
    game.append(sudoku_publib.sudoku_dataarray(ss))
    game[1].setsudoku_plan(sudoku_tablex1.demo_2[gcode])
    
    level = 3
    gcode = 1
    ss="demo2"+",("+lev[level-1]+"_"+str(gcode)+")"
    game.append(sudoku_publib.sudoku_dataarray(ss))
    game[2].setsudoku_plan(sudoku_tablex1.demo_3[gcode])

    level = 1
    gcode = 1
    playindex = 0    
    cmm ='?'
    while 1:
        if cmm =='?':
            print(mtxt)            
        elif cmm =='h':
            print(pysudokuver)
        elif cmm == 'q':
            print()
            print("************************")
            print("** Thank You By By    **")
            print("************************")
            print()
            break
        elif cmm == 'n':#add a new Game
            ss = input("input the gmae name:")
            ss+=",("+lev[level-1]+"_"+str(gcode)+")"
            game.append(sudoku_publib.sudoku_dataarray(ss))
            tt=0
            for i in game:
                print("[%d]: %s "%(tt,i.gname))
                tt+=1
            print("Add ok !")
            print()
            
        elif cmm == 'd': #delete
            print("==================")
            tt=0
            for i in game:
                print("[%d]: %s "%(tt,i.gname))
                tt+=1
            nn = eval(input("input index by Delete:"))
            if nn>len(game)-1:
                print("Sorry ! index out of range ")
                print()
            else:
                del game[nn]
                tt=0
                for i in game:
                    print("[%d]: %s "%(tt,i.gname))
                    tt+=1
                if playindex>=len(game):
                    playindex=len(game)-1
                print("delete ok !")
                print()
        elif cmm == 'l':#load data to array 
            if level==1:
                game[playindex].setsudoku_plan(sudoku_tablex1.demo_1[gcode])
            elif level==2:
                game[playindex].setsudoku_plan(sudoku_tablex1.demo_2[gcode])
            elif level==3:
                game[playindex].setsudoku_plan(sudoku_tablex1.demo_3[gcode])
                
            ss1 = game[playindex].gname
            ss = ss1.split(",")[0]
            ss += ",("+lev[level-1]+"_"+str(gcode)+")"
            game[playindex].gname = ss
            print("===%d is [ %s ] ==="%(playindex,game[playindex].gname))
            game[playindex].showsudoku()                
                
        elif cmm == "p":#show data array 
            print()
            print("===%d is [ %s ] ==="%(playindex,game[playindex].gname))
            game[playindex].showsudoku()
            
        elif cmm == "k":#keyin data to array
            cl=2
            while 1:
                xin= input("input game pos(11..99),Num:")
                ll=xin.split(",")
                if len(ll)==2:
                    pos=eval(xin.split(",")[0])
                    nn =eval(xin.split(",")[1])
                    i = int(pos/10)
                    j = pos%10
                    game[playindex].sudokudat[i-1][j-1].setno(nn)
                    game[playindex].showsudoku()  
                else:
                    print("Err input stop keyin ...")
                    break           

            
        elif cmm =='1':
            level = eval(input("(1:Easy,2:Normal,3:Hard)Input Level:"))
            if 0<level<=3:
                print("Level:%d , Gcode:%d "%(level,gcode))
            else:
                print("Error input level Out of range")
                
        elif cmm =='2':
            gcode = eval(input("input gcode:"))
            if 0<gcode<=10:
                print("Level:%d , Gcode:%d "%(level,gcode))
            else:
                print("Error input gcode Out of range")
                
        elif cmm =='4':
            tt=0
            for i in game:
                print("[%d]: %s "%(tt,i.gname))
                tt+=1
            xcm = input("input playindex:")
            if xcm.isdigit():
                nn = eval(xcm)
            else:
                print("Error input must is Number ... ")
                nn = playindex
                
            if nn < len(game):
                playindex = nn
                print("You select game [ %s ]"%(game[playindex].gname))
            else:
                print("Error input index Out of range")
                  
        elif cmm =='3':
            print()
            print("====Game buffer show list ==========")
            print("Level:%d , Gcode:%d "%(level,gcode))
            tt=0
            for i in game:
                print("[%d]: %s "%(tt,i.gname))
                tt+=1
             
            print("Game index = %d is run [ %s ]"%(playindex,game[playindex].gname))
            print()
                    
        elif cmm == "c":#check game pass or fail
            print()
            print("===check the %d is [ %s ] ==="%(playindex,game[playindex].gname))
            game[playindex].showsudoku()
            game[playindex].checksudoku()
            
            if game[playindex].runfg>0:
                print("Some Number must to edit  ...")
            else:
                if game[playindex].chkfg==0:
                    print("************************")
                    print("** This Game Pass ... **")
                    print("************************")
                else:
                    print("This Game Fail !")    
                    print("Try Again ...")
                    
        elif cmm == 'c1':
            runck,runfail = scanok(game[playindex])
            print("have %d will be edit %d is err ... "%(runck,runfail))

        elif cmm == 'c2':
            runck,runfail = scanok2(game[playindex])
            print("have %d will be edit %d is err ... "%(runck,runfail))    
        
        cmm = input("Play (game[%d]-> %s) help(?)Input cmm="%(playindex,game[playindex].gname))

    
 
        
if __name__ == '__main__':
   main()
