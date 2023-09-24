#跟命令有關的模組
#就我現在的能力，這個比較好表達，還請見諒

#sys：待查詢
#可以提供command-line argumentsb(命令列參數)的模組

#sys.argv

import sys
print(sys.argv[1])

#如果在終端機打：python 跟命令有關的模組.py David John Tom 會輸出第一個值：David

import sys
print(sys.argv[0])

#同上述終端機打入內容，這次會輸出：跟命令有關的模組.py
#這表示sys.argv是從我們在終端機打「python」之後開始算(0) => 可以取得的參數資料範圍：檔案名稱+所有指令列的參數。