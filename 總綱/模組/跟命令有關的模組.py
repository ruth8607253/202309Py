#跟命令有關的模組
#就我現在的能力，這個比較好表達，還請見諒

#sys：系統相關的參數&函式
#可以提供command-line argumentsb(命令列參數)的模組

#sys.argv
#常用在快速互動的程式。

"""import sys
print(sys.argv[1])"""

#如果在終端機打：python 跟命令有關的模組.py David John Tom 會輸出第一個值：David

import sys
#print(sys.argv[0])

#同上述終端機打入內容，這次會輸出：跟命令有關的模組.py
#這表示sys.argv是從我們在終端機打「python」之後開始算(0) => 可以取得的參數資料範圍：檔案名稱+所有指令列的參數。

#sys預設是以「空白分辨斷句」如果希望輸入全名，可以用""框起來
"""import sys
print(sys.argv[1])"""
#在終端機打入內容：python 跟命令有關的模組.py "David Malon" John Tom，可以獲得完整姓名

#限制輸入者回答範圍的方法1：try
"""try:
    print(sys.argv[1])
except IndexError:
    print("Too few arguments.")"""

#限制輸入者回答範圍的方法2：len
"""if len(sys.argv) < 3:
    print("Too few arguments.")
else:
    print(sys.argv[1])"""


#實用小範例：輸入股票代號就能查即時報價。
import sys
import twstock
#在終端機打$ twstock -s 0050(或其他股票代號，可以1~多個同時輸入)
#在終端機打$ twstock -b 0050(或其他股票代號，可以1~多個同時輸入)：判斷是否適合買入