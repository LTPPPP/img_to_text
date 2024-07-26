import requests
from bs4 import BeautifulSoup


def fetch_web_data(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)

    # Kiểm tra nếu yêu cầu thành công
    if response.status_code == 200:
        # Phân tích cú pháp HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trích xuất thông tin, ví dụ: tiêu đề trang
        title = soup.title.string
        print(f"Title of the page: {title}")

        # Trích xuất tất cả các liên kết (anchor tags)
        links = soup.find_all('a')
        for link in links:
            print(f"Link text: {link.text}, URL: {link.get('href')}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


# URL ví dụ để kiểm tra
url = 'https://chatgpt.com/c/262414a4-7a50-4fa8-8403-1b5b80f47099'
fetch_web_data(url)
