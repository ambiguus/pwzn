import requests
from IPython.display import HTML
from multiprocessing.pool import ThreadPool
import time
import hashlib

def process(request_range):
    address = "http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-a"
    headers = {
                    "Range": "bytes={}-{}".format(*request_range)
                }
    return requests.get(address, headers=headers)

if __name__ == '__main__':
    N = 1
    p = ThreadPool(N)
    data = []
    collected=""
    resp = requests.head("http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-a")
    resp_len = int(resp.headers['Content-Length'])
    step = int(resp_len/(N))
    request_range = []
    for ii in range(0, resp_len, step):
        request_range.append((ii, min(resp_len, ii+step-1)))
    try:
        start = time.monotonic()
        result = p.map(process,request_range)
        for r in result:
            data.append(r.content)
            collected = b"".join([r.content])
        print(time.monotonic() - start)
    finally:
        p.close()
        p.join()
    hash = hashlib.md5()
    hash.update(collected)
    print(hash.hexdigest())