import asyncio
import aiohttp
from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

MCP_SERVER_URL = "http://localhost:8000/mcp"

agent = Agent(name="Assistant", instructions="You are a helpful assistant.")

async def call_mock_tool():
    async with aiohttp.ClientSession() as session:
        # 发送请求调用mock MCP服务器的工具
        async with session.post(MCP_SERVER_URL, json={"tool": "getUserInfo", "input": {}}) as resp:
            return await resp.json()

async def main():
    # 调用MCP mock工具接口
    mock_response = await call_mock_tool()
    print("Mock MCP响应:", mock_response)

    # 这里可以结合agent调用OpenAI聊天，模拟OpenAI调工具场景
    response = await Runner.run(agent, "请告诉我用户的信息")
    print("OpenAI响应:", response)

if __name__ == "__main__":
    asyncio.run(main())
