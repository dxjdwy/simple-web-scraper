#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import csv
import os

class SimpleScraper:
    def __init__(self):
        self.session = requests.Session()
        # 设置请求头，模拟浏览器访问
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_page(self, url, delay=1):
        """
        获取网页内容
        """
        try:
            print(f"正在访问: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()  # 检查响应状态
            response.encoding = response.apparent_encoding  # 自动检测编码
            
            # 添加延时，避免频繁请求
            time.sleep(delay)
            
            return response.text
        except requests.RequestException as e:
            print(f"请求失败: {e}")
            return None
    
    def parse_html(self, html):
        """
        解析HTML内容
        """
        if not html:
            return None
        
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    def scrape_quotes(self):
        """
        示例：爬取名言网站 http://quotes.toscrape.com/
        """
        base_url = "http://quotes.toscrape.com"
        quotes_data = []
        page = 1
        
        while True:
            url = f"{base_url}/page/{page}/"
            html = self.get_page(url)
            
            if not html:
                break
                
            soup = self.parse_html(html)
            quotes = soup.find_all('div', class_='quote')
            
            if not quotes:
                print("没有更多内容了")
                break
            
            for quote in quotes:
                text = quote.find('span', class_='text').get_text()
                author = quote.find('small', class_='author').get_text()
                tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
                
                quotes_data.append({
                    'text': text,
                    'author': author,
                    'tags': ', '.join(tags)
                })
                
                print(f"作者: {author}")
                print(f"名言: {text}")
                print(f"标签: {', '.join(tags)}")
                print("-" * 50)
            
            page += 1
            
            # 限制爬取页数，避免过度请求
            if page > 3:
                break
        
        return quotes_data
    
    def save_to_csv(self, data, filename="quotes.csv"):
        """
        保存数据到CSV文件
        """
        if not data:
            print("没有数据可保存")
            return
            
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['text', 'author', 'tags']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in data:
                writer.writerow(row)
                
        print(f"数据已保存到 {filename}")
    
    def scrape_custom_site(self, url, selector):
        """
        通用爬取函数
        url: 目标网址
        selector: CSS选择器
        """
        html = self.get_page(url)
        if not html:
            return []
            
        soup = self.parse_html(html)
        elements = soup.select(selector)
        
        results = []
        for element in elements:
            results.append({
                'text': element.get_text().strip(),
                'html': str(element)
            })
            
        return results

def main():
    """
    主函数
    """
    scraper = SimpleScraper()
    
    print("=== 简单网页爬虫 ===")
    print("1. 爬取名言网站示例")
    print("2. 自定义爬取")
    
    choice = input("请选择 (1/2): ").strip()
    
    if choice == "1":
        print("\n开始爬取名言网站...")
        quotes = scraper.scrape_quotes()
        scraper.save_to_csv(quotes)
        
    elif choice == "2":
        url = input("请输入网址: ").strip()
        selector = input("请输入CSS选择器 (例如: h1, .title, #content): ").strip()
        
        print(f"\n开始爬取 {url}...")
        results = scraper.scrape_custom_site(url, selector)
        
        if results:
            print(f"\n找到 {len(results)} 个元素:")
            for i, result in enumerate(results[:10], 1):  # 只显示前10个
                print(f"{i}. {result['text'][:100]}...")
        else:
            print("没有找到匹配的元素")
    
    else:
        print("无效选择")

if __name__ == "__main__":
    main()
