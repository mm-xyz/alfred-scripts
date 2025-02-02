# Alfred Workflow Scripts | Alfred 工作流程腳本集

[English](#english) | [中文](#中文)

## English

### Table of Contents
- [get_preview_info](#get_preview_info) - Web Preview Information Generator

This repository contains a collection of useful Alfred workflow scripts designed to enhance daily productivity.

### Scripts Overview

#### [get_preview_info](./get_preview_info/README.md)
A Python script that generates Hugo blog preview cards from web pages. It automatically extracts titles, descriptions, and preview images using Open Graph tags.

## 中文

### 目錄
- [get_preview_info](#get_preview_info) - 網頁預覽資訊生成器

這個倉庫收集了一系列實用的 Alfred 工作流程腳本，目的是提升日常工作效率。

### 腳本概覽

#### [get_preview_info](./get_preview_info/README.md)
一個 Python 腳本，用於生成 Hugo 部落格的預覽卡片。它能自動從網頁中提取標題、描述和預覽圖片，支援 Open Graph 標籤。

## 腳本列表

### 1. get_preview_info.py
一個用於獲取網頁預覽資訊的 Python 腳本，可以：
- 抓取網頁的標題、描述和預覽圖片
- 自動生成 Hugo 部落格的預覽卡片 shortcode
- 支援 Open Graph 標籤解析

## 安裝需求

- Python 3.x
- pip3（Python 套件管理器）

### 必要的 Python 套件：
```bash
pip3 install requests beautifulsoup4 pyOpenSSL
```

## 使用方法

### get_preview_info.py

1. 確保腳本具有執行權限：
```bash
chmod +x get_preview_info.py
```

2. 在 Alfred 工作流程中使用：
- 將腳本加入到 Alfred 工作流程中
- 設定輸入參數為目標網址
- 輸出將生成一個包含網頁資訊的 Hugo shortcode

輸出格式示例：
```
{{< blog-preview-card 
    url="網址"
    title="網頁標題"
    description="網頁描述"
    image="預覽圖片網址"
    date="當前日期"
>}}
```

## 注意事項

- 腳本會自動處理 SSL 證書相關的警告
- 包含適當的錯誤處理和用戶提示
- 支援現代網頁標準和 meta 標籤

## 貢獻

歡迎提交 Pull Requests 來改進現有腳本或新增新的實用工作流程腳本。

## 授權

MIT License
