import asyncio
from typing import Dict

from tlv_tools import MSG_QUEUE, TLVPool

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

        # ========================== 自定义业务逻辑处理 ==========================
        print(f"【业务处理】客户端 {client_addr} 消息类型: {msg_type}, 消息内容: {msg_body}")
        # 根据消息id分发不同的业务
        if msg_type == 1:
            resp_body = f"【聊天回执】已收到消息： {msg_body}"

        elif msg_type == 2:
            resp_body = f"【心跳回执】已收到心跳消息： {msg_body}"

        else:
            resp_body = f"【未知消息】消息类型: {msg_type}"
        # =====================================================================
        
        # 封装响应消息, 并发送协程
        if client_addr in CLIENT_POOL:
            resp_pkg = TLVPool.encode(msg_type, resp_body)
            writer = CLIENT_POOL[client_addr]
            writer.write(resp_pkg)
            await writer.drain()

        # 标记队列任务完成
        MSG_QUEUE.task_done()

async def client_handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """
    单个客户端连接总调度协程
    """
    client_addr = f"{writer.get_extra_info('peername')}"
    CLIENT_POOL[client_addr] = writer
    print(f"新客户端接入：{client_addr}, 当前在线客户端数：{len(CLIENT_POOL)}")

    # 客户端私有缓冲区：永久保存半包数据，直至数据接收完整
    recv_buffer = b""

    try:
        while True:
            # 异步接收数据，单词最大4096字节
            recv_data = await reader.read(4096)
            if not recv_data:
                break # 客户端主动断开连接

            # 累加数据到缓冲区（保留上次半包数据）
            recv_buffer += recv_data

            # TLV解析： 获取完整消息列表和剩余半包数据
            full_msgs, recv_buffer = TLVPool.decode(recv_buffer)

            # 完整消息全部投入逻辑队列，交由后台协程处理
            for msg in full_msgs:
                msg["client_addr"] = client_addr
                await MSG_QUEUE.put(msg)  # 阻塞等待队列可用

    except Exception as e:
        print(f"客户端 {client_addr} 连接异常: {e}")
    finally:
        # 连接断开, 清理资源
        del CLIENT_POOL[client_addr]
        writer.close()
        await writer.wait_closed()
        print(f"客户端{client_addr}已断开, 当前在线:{len(CLIENT_POOL)}")

async def main():
    # 启动后台业务逻辑协程（常驻运行）
    asyncio.create_task(client_logic_worker())

    # 启动TLV-TCP服务
    server = await asyncio.start_server(
        client_handle,
        host="0.0.0.0",
        port=8888
    )

    print("【工业级TLV全双工TCP服务启动成功】")
    print("服务监听端口: 8888 | 协议格式: T(2B)+L(2B)+V(NB)")

    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())