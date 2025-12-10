import asyncio
import time
from django.http import HttpResponse
import httpx


# --------- Função ASSÍNCRONA ---------
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


# --------- Função SÍNCRONA ---------
def http_call_sync():
    for num in range(1, 6):
        time.sleep(1)  # CORRETO para função síncrona
        print(num)

    r = httpx.get("https://httpbin.org/")
    print(r)


# --------- VIEW ASSÍNCRONA ---------
async def async_view(request):
    # roda a função http_call_async sem travar a view
    asyncio.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


# --------- VIEW SÍNCRONA ---------
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")
