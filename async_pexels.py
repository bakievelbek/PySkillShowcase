import time
import httpx
import asyncio

from dotenv import dotenv_values

config = dotenv_values(".env")

start_time = time.time()

"""

Example of synchronous request

"""


async def get_link(query: str, current_page: int):
    headers = {'Authorization': config.get('PEXELS_TOKEN')}
    params = {'query': query, 'per_page': 1, 'page': current_page}
    url = 'https://api.pexels.com/v1/search'

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        if response.status_code == 200:
            res = response.json()
            k = res.get('photos')[0].get('src').get('original')
            print(k)
            return k


async def search_image(query: str, count: int):
    current_page = 0
    images = await asyncio.gather(
        *(get_link(query, count) for count in range(current_page, count)),
        return_exceptions=True
    )

    return images


asyncio.run(search_image('fox', 50))

# Result:
# Time taken: 1.405679702758789 seconds


"""

Example of asynchronous request

"""

for i in range(0, 50):
    response = httpx.request(method='GET',
                             headers={'Authorization': config.get('PEXELS_TOKEN')},
                             url='https://api.pexels.com/v1/search',
                             params={'query': 'fox', 'per_page': 1, 'page': i})
    res = response.json()
    print(res.get('photos')[0].get('src').get('original'))

# Result
# Time taken: 16.580148458480835 seconds


end_time = time.time()
print("Time taken:", end_time - start_time, "seconds")
