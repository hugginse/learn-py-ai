import asyncio
import aiohttp

# 限定最大并发协程数：3
sem = asyncio.Semaphore(3)

async def crawl_page(session, url):
    # 占用一个并发席位，超出数量则阻塞等待
    async with sem:
        async with session.get(url) as resp:
            html = await resp.text()
            print(f"{url} 页面字节大小： {len(html)}")

async def main():
    async with aiohttp.ClientSession() as session:
        # 8个相同链接, 最多同时3个并发请求
        url_list = ["https://www.baidu.com"] * 8
        tasks = [crawl_page(session, url) for url in url_list]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())