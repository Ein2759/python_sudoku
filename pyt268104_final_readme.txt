pyt268104 廖恆德 python期末作業 20160724
主題: 數獨
1說明:
	專題由三個檔案組成
	pyt268104_sudoku.py	--主程式
	sudoku_publib.py	--class Num and Class sudoku_dataarray 
	sudoku_tablex1.py   	--題庫(demo_1)Easy ,(demo_2)Normal,(demo_3)Hard
	需置於同一目錄下

2執行啟動:
	python3 pyt268104_sudoku.py
	啟動後 預置 demo,demo1,demo2 3個遊戲庫資料(keyin 3 whill list)        
3操作:
=== Easy Sudoku Game V1.0 pyt268104 Handel ===
*** System Command ***
[1]Level Select (L1:Easy,L2:Normal,L3:Hard) 	: 設定 Level
[2]Game code by LEVEL(1..10)		   	: 設定題目序號
[3]Show Game Buffer and Status 			: 顯示目前開啟的遊戲數急狀態名稱
[4]select play Game				: 選擇緩衝區中的數獨題目
[?]List Menu					: 顯示指令提示
[H]Help info show				: 顯示 版本紀錄
[Q]quit						: 結束離開
*** Game Command *** 
[N]Add a New Game				: 增加 遊戲庫資料 
[D]Delete a Game				: 刪除 遊戲庫資料
[L]Load Game Data[from level,gcode]		: 於選定的遊戲庫資料載入指定的題目
[P]Print Game data array			: 顯示遊戲庫的資料現況
[K]key in a data to Game			: 輸入 (pos,Num) 
[C]check the Game by Pass			: 檢查遊戲狀態 (playing , Fail , Pass)

範例:
===0 is [ demo,(Easy_1) ] === ##顯示 (buffer index)  [名稱,(等級_題目序號)]
=============== sudoku data ===============
[ 0][ 0]($9)||[ 0]($4)[ 0]||($1)($7)[ 0]   ## ($ Num) 為題目不可更改
[ 0][ 0]($1)||[ 0]($2)[ 0]||[ 0]($3)[ 0]   ## [  Num] 為user 寫入欄位
[ 0]($4)($6)||[ 0][ 0]($5)||($8)[ 0][ 0]
============||============||============
($6)[ 0]($3)||($7)[ 0][ 0]||[ 0][ 0][ 0]
($8)($2)[ 0]||[ 0][ 0][ 0]||[ 0][ 0]($4)
[ 0][ 0][ 0]||($5)($8)[ 0]||($6)[ 0]($3)
============||============||============
($5)($7)[ 0]||[ 0][ 0]($8)||($9)[ 0][ 0]
[ 0]($1)[ 0]||($2)[ 0][ 0]||[ 0]($8)($5)
($3)[ 0][ 0]||[ 0]($5)($1)||[ 0][ 0][ 0]
==========================================
