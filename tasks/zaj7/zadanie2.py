import requests
from IPython.display import HTML
from multiprocessing.pool import Pool
import bs4

if __name__ == '__main__':
    N = 10
    p = Pool(N)
    address = "http://194.29.175.134:4444"
    headers = {
                "uname": "foo",
                "password":"bar"
                }
    cookie = requests.post(address+"/login", params=headers, allow_redirects=False)
    print(cookie.cookies)
    resp = requests.get(address+"/237931237970", cookies=cookie.cookies)
    bs = bs4.BeautifulSoup(resp.text)

    """
        dwie kolejny in: wueue_in 0- do przetworzenia,
            quote out - juz przetworzone
        jeden proces przerabia
        w glownym procesie przerzucamy

        1 proces wrzuca linki do queue in
        drugi z quoue out parsuje i wrzuca do queue in
        """