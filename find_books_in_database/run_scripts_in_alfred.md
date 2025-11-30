# Alfred 中執行書籍搜索腳本指南

## 腳本說明

這個 shell 腳本用於在 Alfred 工作流程中執行書籍搜索功能，並以通知方式顯示結果。

## 配置步驟

1. 打開 Alfred 偏好設置
2. 創建新的工作流程 (Workflow)
3. 添加"Script Filter"或"Run Script"動作
4. 將下方腳本貼入腳本區域

## 腳本代碼

```bash
python3 "//Users/marslo/GithubRepo_mm-xyz/alfred-scripts/find_books_in_database/search_books.py" "/Users/marslo/Library/Mobile Documents/com~apple~Numbers/Documents/files_and_folders.csv" "{query}" | while IFS= read -r line; do
    osascript -e "display notification \"$line\" with title \"匹配書名\""
done
```

## 運作原理

1. 通過 Python 腳本查詢 CSV 文件中包含關鍵詞的書籍
2. 對每個匹配結果，使用 macOS 的 osascript 顯示系統通知
3. 通知標題設為「匹配書名」，內容為匹配到的書籍標題

## 自定義建議

- 可替換 CSV 文件路徑以指向您自己的書籍數據庫
- 可修改通知標題或格式以符合個人偏好
- 可增加更多處理邏輯，如點擊通知後的操作