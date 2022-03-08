import time
import asyncio

def download_page(url) :
    time.sleep(1) # 페이지를 다운로드
    #html 분석
    print("complete download:", url)
    
def main() :
    download_page("url_1")
    download_page("url_2")
    download_page("url_3")
    download_page("url_4")
    download_page("url_5")

print(f"stated at {time.strftime('%X')}")
main()
print(f"finish at {time.strftime('%X')}")


async def download_page(url) :
    await asyncio.sleep(1) # 페이지를 다운로드
    #html 분석
    print("complete download:", url)
    
async def main() :
    await asyncio.gather(
        download_page("url_1"),
        download_page("url_2"),
        download_page("url_3"),
        download_page("url_4"),
        download_page("url_5")
    )    

print(f"stated at {time.strftime('%X')}")
asyncio.run(main())
print(f"finish at {time.strftime('%X')}")