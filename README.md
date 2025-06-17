# 简单网页爬虫项目

这是一个基于Python的简单网页爬虫项目，适合初学者学习和使用。

## 功能特点

- 🚀 简单易用的爬虫框架
- 🛡️ 内置请求限制和异常处理
- 📊 支持数据导出为CSV格式
- 🎯 提供示例和自定义爬取功能
- 🔧 可扩展的设计

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 运行爬虫

```bash
python scraper.py
```

### 2. 选择功能

程序提供两种模式：

1. **示例模式**：爬取名言网站 http://quotes.toscrape.com/
2. **自定义模式**：输入任意网址和CSS选择器进行爬取

### 3. 查看结果

- 爬取的数据会显示在控制台
- 示例模式会自动保存为 `quotes.csv` 文件

## 代码结构

```
simple-scraper/
├── scraper.py          # 主程序文件
├── requirements.txt    # 依赖包列表
├── README.md          # 说明文档
└── quotes.csv         # 输出文件（运行后生成）
```

## 主要类和方法

### SimpleScraper 类

- `get_page(url, delay=1)`: 获取网页内容
- `parse_html(html)`: 解析HTML
- `scrape_quotes()`: 示例爬取功能
- `save_to_csv(data, filename)`: 保存数据到CSV
- `scrape_custom_site(url, selector)`: 通用爬取功能

## 使用示例

### 基本用法

```python
from scraper import SimpleScraper

# 创建爬虫实例
scraper = SimpleScraper()

# 爬取网页
html = scraper.get_page("https://example.com")
soup = scraper.parse_html(html)

# 提取数据
titles = soup.find_all('h1')
for title in titles:
    print(title.get_text())
```

### 自定义爬取

```python
# 爬取特定元素
results = scraper.scrape_custom_site(
    url="https://example.com",
    selector="h2.title"
)

for result in results:
    print(result['text'])
```

## 注意事项

1. **遵守robots.txt**：爬取前请检查目标网站的robots.txt文件
2. **控制频率**：程序内置1秒延时，避免过于频繁的请求
3. **异常处理**：网络请求可能失败，程序已包含基本异常处理
4. **编码问题**：程序会自动检测网页编码
5. **合法使用**：请确保爬取行为符合相关法律法规

## 扩展功能

你可以根据需要添加以下功能：

- 支持更多数据格式（JSON、Excel）
- 添加数据库存储
- 支持JavaScript渲染页面（Selenium）
- 添加代理支持
- 实现并发爬取

## 常见问题

### Q: 为什么无法访问某些网站？
A: 可能是网站有反爬虫机制，可以尝试：
- 修改User-Agent
- 增加请求延时
- 使用代理IP

### Q: 如何处理动态加载的内容？
A: 当前版本只支持静态HTML，动态内容需要使用Selenium等工具

### Q: 如何提取更复杂的数据？
A: 可以学习更多BeautifulSoup的选择器语法和方法

## 学习资源

- [BeautifulSoup 官方文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests 官方文档](https://docs.python-requests.org/)
- [CSS 选择器教程](https://www.w3schools.com/css/css_selectors.asp)

## 许可证

本项目仅供学习使用，请在法律允许范围内使用。
