# 書籍資料庫搜索工具

這是一個簡單的 Alfred 工作流程腳本，用於快速搜索 CSV 格式的書籍資料庫。

## 功能

- 根據輸入的關鍵詞在 CSV 文件中搜索相符合的書籍標題
- 支援部分匹配和不區分大小寫的搜索
- 直接從 Alfred 工作流程中調用，迅速得到結果

## 使用方法

1. 在 Alfred 中設置此腳本作為工作流程
2. 配置工作流程參數:
   - 第一個參數: CSV 資料庫文件的路徑
   - 第二個參數: 搜索關鍵詞

## 技術細節

此腳本使用 Python 3 開發，並依賴以下標準庫:
- `csv`: 用於讀取 CSV 文件
- `sys`: 用於接收命令行參數
- `os`: 用於檢查文件是否存在

## 示例

```bash
python search_books.py books_database.csv "哈利波特"
```

## 運作原理

1. 通過 Python 腳本查詢 CSV 文件中包含關鍵詞的書籍
2. 對每個匹配結果，使用 macOS 的 osascript 顯示系統通知
3. 通知標題設為「匹配書名」，內容為匹配到的書籍標題

### 流程圖

```mermaid
graph TD
    A[用戶輸入查詢詞] --> B[Python腳本搜索CSV文件]
    B --> C{是否找到匹配?}
    C -->|是| D[遍歷每個匹配結果]
    C -->|否| E[結束,無結果]
    D --> F[顯示系統通知]
    F --> G[通知顯示匹配書名]
    G --> H[處理下一個結果]
    H -->|有更多結果| D
    H -->|無更多結果| I[結束流程]
```

## 自定義建議

- 可替換 CSV 文件路徑以指向您自己的書籍數據庫
- 可修改通知標題或格式以符合個人偏好
- 可增加更多處理邏輯，如點擊通知後的操作

## 備註

- CSV 文件的第一列應該包含書籍標題
- 確保 CSV 文件使用 UTF-8 編碼以正確處理各種語言的書籍標題

## 在Finder中顯示文件增強功能

### 最佳解決方案：使用Alfred選單直接選擇並打開文件

這個方案將搜索結果顯示為Alfred選單，讓您可以直接選擇要打開的文件：

#### 1. 修改Python腳本，輸出Alfred可識別的JSON格式

首先，創建一個新的Python腳本 `search_books_alfred.py`：

```python
import csv
import sys
import os
import json

def search_books(filename, query):
    matches = []
    base_dir = "/Users/marslo/pCloud Drive"  # 設置基礎目錄
    
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if query.lower() in row[0].lower():
                    # 獲取書名
                    title = row[0]
                    
                    # 獲取路徑（如果有）
                    if len(row) > 1:
                        path = row[1]
                        # 如果是相對路徑，轉換為絕對路徑
                        if not path.startswith('/'):
                            path = os.path.join(base_dir, path)
                    else:
                        path = ""
                    
                    # 添加到結果集
                    matches.append({
                        "title": title,
                        "subtitle": path,
                        "arg": path,
                        "icon": {"type": "fileicon", "path": path} if os.path.exists(path) else {"type": "default"}
                    })
    else:
        print(f"File not found: {filename}", file=sys.stderr)
    
    # 返回Alfred可讀取的JSON格式
    result = {"items": matches}
    return json.dumps(result)

if __name__ == "__main__":
    filename = sys.argv[1]
    query = sys.argv[2]
    
    print(search_books(filename, query))
```

#### 2. 在Alfred中設置工作流程

1. 創建一個新的Alfred工作流程
2. 添加一個「Script Filter」輸入項
3. 在腳本框中輸入：

```bash
python3 "/Users/marslo/GithubRepo_mm-xyz/alfred-scripts/find_books_in_database/search_books_alfred.py" "/Users/marslo/Library/Mobile Documents/com~apple~Numbers/Documents/files_and_folders.csv" "{query}"
```

4. 設置「With Output As」選項為「Alfred JSON」
5. 添加一個「Open File」動作，並連接到腳本過濾器
6. 在「Open File」動作中，選擇「From Input」選項

#### 3. 使用方式

1. 在Alfred中輸入您的關鍵詞啟動工作流程
2. Alfred將顯示匹配的書籍列表，包含書名和路徑
3. 使用上下箭頭選擇您要打開的書籍
4. 按Enter即可在Finder中顯示該文件

#### 4. 完整工作流程設置

```
[輸入項] Script Filter:
   - 輸入: {query}
   - 腳本: python3 "/path/to/search_books_alfred.py" "/path/to/csv" "{query}"
   - With Output As: Alfred JSON
     |
     V
[動作項] Open File:
   - File(s): {query}
```

使用此方案的優點:

1. 直接在Alfred界面中顯示搜索結果列表，更加直觀
2. 每個結果項目包含書名和路徑信息
3. 可以使用箭頭鍵瀏覽多個結果
4. 選擇後直接在Finder中打開文件
5. 避免了通知系統的限制
6. 支持顯示文件圖標，更易識別文件類型

這個方法利用了Alfred的內建功能，比依賴macOS通知系統更可靠，同時提供了更好的用戶體驗。
