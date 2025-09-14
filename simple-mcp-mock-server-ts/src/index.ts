import express, { Request, Response } from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

const PORT = 8000;

// 定义接口请求体类型
interface MCPRequest {
  tool: string;
  input: unknown;
}

interface UserInfo {
  id: string;
  name: string;
  email: string;
}

app.post("/mcp", (req: Request<{}, {}, MCPRequest>, res: Response) => {
  const { tool, input } = req.body;

  if (tool === "getUserInfo") {
    // 返回模拟的用户信息数据
    const data: UserInfo = {
      id: "user-123",
      name: "张三",
      email: "zhangsan@example.com",
    };
    return res.json({ tool, data });
  }

  res.status(400).json({ error: "未知工具请求" });
});

app.listen(PORT, () => {
  console.log(`简单MCP Mock服务器（TypeScript版）已启动，监听端口${PORT}`);
});
