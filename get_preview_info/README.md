# get_preview_info

[English](#english) | [中文](#中文)

## English

### Description
A Python script that generates Hugo link preview cards from web pages. It automatically extracts titles, descriptions, and preview images using Open Graph tags.

### Requirements
- Python 3.x
- pip3 (Python Package Manager)

### Required Python Packages
```bash
pip3 install requests beautifulsoup4 pyOpenSSL
```

### Usage

1. Ensure the script has execution permissions:
```bash
chmod +x get_preview_info.py
```

2. In Alfred Workflow:
- Add the script to your Alfred workflow
- Set the input parameter as the target URL
- The output will generate a Hugo shortcode containing webpage information

Example output:
```
{{< link-preview-card 
    url="target_url"
    title="webpage_title"
    description="webpage_description"
    image="preview_image_url"
    date="current_date"
>}}
```

### Notes
- Automatically handles SSL certificate warnings
- Includes proper error handling and user prompts
- Supports modern web standards and meta tags

## 中文

### 描述
這是一個用於生成 Hugo 連結預覽卡片的 Python 腳本。它能自動從網頁中提取標題、描述和預覽圖片，並支援 Open Graph 標籤解析。

### 系統需求
- Python 3.x
- pip3（Python 套件管理器）

### 必要的 Python 套件
```bash
pip3 install requests beautifulsoup4 pyOpenSSL
```

### 使用方法

1. 確保腳本具有執行權限：
```bash
chmod +x get_preview_info.py
```

2. 在 Alfred 工作流程中使用：
- 將腳本加入到您的 Alfred 工作流程中
- 設定輸入參數為目標網址
- 輸出將生成一個包含網頁資訊的 Hugo shortcode

輸出格式範例：
```
{{< link-preview-card 
    url="目標網址"
    title="網頁標題"
    description="網頁描述"
    image="預覽圖片網址"
    date="當前日期"
>}}
```

### 注意事項
- 自動處理 SSL 證書相關的警告
- 包含適當的錯誤處理和使用者提示
- 支援現代網頁標準和 meta 標籤 