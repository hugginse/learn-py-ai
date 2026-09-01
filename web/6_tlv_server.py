import asyncio
from typing import Dict

from .tlv05 import MSG_QUEUE
from .tlv05 import TLVPool

CLIENT_POOL: Dict[str, asyncio.StreamWriter] = dict()

async def client_logic_worker():
    """"
    全局逻辑队列处理协程（独立后台线程）
    专门消费消息队列，执行业务逻辑，不阻塞网络IO
    """

    print("业务逻辑处理协程启动成功")
    while True:
        # 阻塞获取队列消息
        msg_info = await MSG_QUEUE.get()
        client_addr = msg_info["client_addr"]
        msg_type = msg_info["msg_type"]
        msg_body = msg_info["body"]
        