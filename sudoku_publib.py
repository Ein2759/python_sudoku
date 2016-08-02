# coding=utf-8
#=== pyt268104 home work ===
# 20160627
#import math
#import numpy as np
#v1.1
class Num:
    arealoop=[[1,3,1,3],[1,3,4,6],[1,3,7,9],
              [4,6,1,3],[4,6,4,6],[4,6,7,9],
              [7,9,1,3],[7,9,4,6],[7,9,7,9]              
              ]
    areacode=0
    chkno=[]
    no=0
    pos=00
    status = 0 #0:user edit ,1:is mask can no edit
    chkfg=0
    
    def __init__(self, pos, no, status):
        self.pos=pos
        self.no=no
        self.status = status
        self.chkfg=0
        self.chkno=[1,2,3,4,5,6,7,8,9]
        
    def setpos(self,pos):
        px=eval(str(pos)[1])
        py=eval(str(pos)[0])
        if 1<= px <=9:
            if 1<= py <=9:
                #self.pos = pos
                if 1<=py<=3:
                    if 1<=px<=3:
                        self.areacode=1
                    elif 4<=px<=6:
                        self.areacode=2
                    elif 7<=px<=9:
                        self.areacode=3
                        
                elif 4<=py<=6:
                    if 1<=px<=3:
                        self.areacode=4
                    elif 4<=px<=6:
                        self.areacode=5
                    elif 7<=px<=9:
                        self.areacode=6
                    
                elif 7<=py<=9:
                    if 1<=px<=3:
                        self.areacode=7
                    elif 4<=px<=6:
                        self.areacode=8
                    elif 7<=px<=9:
                        self.areacode=9

    def maskno(self,no):
        if self.status==1:#mask no 
            self.no=no
        
    def setno(self,no):
        if self.status==0:#user edit no
            self.no = no

    def scanchk(self,xx):
        self.chkfg=0
        fg1=0
        fg2=0
        fg3=0
        fg1=self.area_scanchk(xx)
        fg2=self.col_scanchk(xx)
        fg3=self.row_scanchk(xx)
        self.chkfg|=fg1 or fg2 or fg3        
        pass
    
    def area_scanchk(self,xx):
        fg=0
        #py=int(self.pos/10)
        #px=self.pos%10
        self.setpos(self.pos)
        xacode=self.areacode
        y1,y2,x1,x2 = self.arealoop[self.areacode-1]
        y,x = (y1-1),(x1-1)        
        for y in range(y1-1,y2):
            for x in range(x1-1,x2):
                tt=(y+1)*10+x+1
                if tt!=self.pos:
                    nn = xx[y][x].no
                    if nn in self.chkno:
                        self.chkno.remove(nn)
                        
                    if nn!=0:
                        if nn==self.no:
                            fg=1# fthe game check fail
        return fg
        pass        

    def col_scanchk(self,xx):#col y 列
        fg=0
        #px=eval(str(pos)[1])#row
        py=eval(str(self.pos)[0])#col
        y=py-1
        for x in range(1-1,9):
            tt=(y+1)*10+x+1
            if tt!=self.pos:                
                nn = xx[y][x].no
                if nn in self.chkno:
                    self.chkno.remove(nn)
                if nn!=0:
                    if nn==self.no:
                        fg=1# fthe game check fail
                        
        return fg            
        pass

    def row_scanchk(self,xx):#row x 行
        fg=0
        px=eval(str(self.pos)[1])#row
        #py=eval(str(pos)[0])#col
        x=px-1
        #print("x=",x)
        for y in range(1-1,9):
            #print("y=",y)
            tt=(y+1)*10+x+1
            if tt!=self.pos:         
                nn = xx[y][x].no            
                if nn in self.chkno:
                    self.chkno.remove(nn)
                if nn!=0:
                    if nn==self.no:
                        fg=1# fthe game check fail        
        return fg
        pass

class sudoku_dataarray:
    gname=""
    sudokudat = []
    chkfg=0
    runfg=0 
    def __init__(self,name):
        self.gname = name
        self.sudokudat = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                pos = (i+1)*10+(j+1)
                self.sudokudat[i][j] = Num(pos,0,0)                
        self.chkfg=0
        self.runfg=0
        pass

    def showsudoku(self):              
        #self.chkfg=0
        #print()
        print("="*15,"sudoku data","="*15)
        for i in range(9):
            for j in range(9):
                
                if self.sudokudat[i][j].status==1:
                    print("($%1s)"%(self.sudokudat[i][j].no),end="")#mask 
                else:    
                    print("[%2s]"%(self.sudokudat[i][j].no),end="")#free edit
                    #self.sudokudat[i][j].scanchk(self.sudokudat)
                    #self.chkfg+=self.sudokudat[i][j].chkfg

                if j in (2,5):
                    print("||",end="")
            print()
            if i in (2,5):
                print(("="*12)+"||"+("="*12)+"||"+("="*12))
        
        print("="*42)
        pass
    
    def checksudoku(self):             
        self.chkfg=0
        self.runfg=0
        for i in range(9):
            for j in range(9):
                if self.sudokudat[i][j].status==0:
                    self.sudokudat[i][j].scanchk(self.sudokudat)
                    self.chkfg|=self.sudokudat[i][j].chkfg
                    if self.sudokudat[i][j].no==0:
                        self.runfg+=1
                    
        #return self.chkfg

    def setsudoku_col(self,nn,ll):
        tt=0
        for j in range(9):
            self.sudokudat[nn-1][j].no=ll[tt]
            if ll[tt]!=0:
                self.sudokudat[nn-1][j].status=1 # mask data  
            else:
                self.sudokudat[nn-1][j].status=0 # user data
            tt+=1        
        pass

    def setsudoku_plan(self,tab):
        tt=0
        for i in range(9):
            for j in range(9):
                self.sudokudat[i][j].no = tab[i][j]
                nn =  tab[i][j]
                if self.sudokudat[i][j].no!=0:
                    self.sudokudat[i][j].status=1 # mask data 
                else:
                    self.sudokudat[i][j].status=0 # user data
                stt=self.sudokudat[i][j].status
                self.sudokudat[i][j].chkno=[1,2,3,4,5,6,7,8,9]
                pp = (i+1)*10+(j+1)
                self.sudokudat[i][j].setpos(pp)

#xx = [[0 for i in range(9)] for j in range(9)]    
#split the pos by col and row   
#k1=eval(str(s)[0])
#k2=eval(str(s)[1])
