import struct
import asyncio
from asyncio import Queue

# 全局业务消息队列： IO协程生产消息，逻辑协程消费消息
MSG_QUEUE = Queue(maxsize=1000)

class TLVPool:
    # T=2字节, L=2字节, 头部固定4字节
    HEADER_LEN = 4

    @classmethod
    def encode(cls, msg_type: int, body: str) -> bytes:
        '''
        TLV消息打包: 对外发送完整数据包
        : param msg_type: 消息ID(T)
        : param body: 业务消息内容(V)
        : return: 二进制TLV数据包
        '''
        body_bytes = body.encode('utf-8')
        body_len = len(body_bytes)
        # 网络字节序打包： 2字节消息类型 + 2字节消息长度
        header = struct.pack("!HH", msg_type, body_len)
        return header + body_bytes

    @classmethod
    def decode(cls, buffer: bytes) -> tuple[list[dict], bytes]:
        '''
        TLV消息解包: 处理缓冲区数据，解析完整消息，返回未用完的半包数据
        : param buffer: 累计接收的缓冲区原始字节
        : return: 完整消息列表，剩余半包残留
        '''
        messages = []
        # 循环解析，支持一次多条消息+半包残留
        while len(buffer) >= cls.HEADER_LEN:
            # 解析头部, 获取消息体长度
            msg_type, body_len = struct.unpack("!HH", buffer[:cls.HEADER_LEN])
            total_pkg_len = cls.HEADER_LEN + body_len

            # 数据不完整，直接退出，保留当前所有数据等待下次接收
            if len(buffer) < total_pkg_len:
                break

            # 截取完整消息体
            body_data = buffer[cls.HEADER_LEN:total_pkg_len].decode('utf-8')
            messages.append({
                "msg_type": msg_type,
                "body": body_data,
                "body_len": body_len,
            })

            # 截断已解析数据，保留剩余字节继续解析
            buffer = buffer[total_pkg_len:]
        return messages, buffer
    