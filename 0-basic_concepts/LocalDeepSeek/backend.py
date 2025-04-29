# backend.py
import os
import requests
from typing import Generator
from rich import print
import json

class DeepSeekChatter:
    def __init__(self, 
                 api_base: str = "http://localhost:8110/v1",
                 model: str = "./DeepSeek-R1-Distill-Qwen-1.5B",
                 #model="./DeepSeek-R1-Distill-Qwen-7B",
                 max_tokens: int = 1024):
        self.api_base = api_base
        self.model = model
        self.max_tokens = max_tokens
        self.session = requests.Session()
        self._print_banner()

    def _print_banner(self):
        """打印启动横幅"""
        print("[bold green]\nDeepSeek 对话系统已启动![/bold green]")
        print(f"[dim]模型: {os.path.basename(self.model)}[/dim]")
        print("[dim]输入 'exit' 退出，输入 'reset' 清空对话历史[/dim]\n")

    def _generate_stream(self, messages: list) -> Generator[str, None, None]:
        """流式响应生成器"""
        response = self.session.post(
            f"{self.api_base}/chat/completions",
            json={
                "model": self.model,
                "messages": messages,
                "temperature": 0.3,
                "max_tokens": self.max_tokens,
                "stream": True
            },
            stream=True,
            timeout=30
        )
        response.raise_for_status()
        
        for chunk in response.iter_lines():
            chunk = chunk.decode().strip()  # Add whitespace stripping
            if not chunk:  # Skip empty lines
                continue
            try:
                if chunk.startswith("data: "):
                    json_str = chunk[6:]  # Get content after "data: "
                    if json_str == "[DONE]":  # Handle stream end marker
                        break
                    data = json.loads(json_str)
                    if content := data["choices"][0]["delta"].get("content"):
                        yield content
            except json.JSONDecodeError:
                print(f"[red]警告: 无效JSON数据块: {chunk}[/red]")  # Add error logging
                continue

    def chat_loop(self):
        """对话主循环"""
        history = []
        while True:
            try:
                print("[bold cyan]您 > [/bold cyan]", end="")
                user_input = input().strip()
                
                if user_input.lower() == 'exit':
                    print("[yellow]聊天结束[/yellow]")
                    break
                if user_input.lower() == 'reset':
                    history = []
                    print("[green]历史已重置[/green]")
                    continue
                if not user_input:
                    continue
                
                # 添加用户消息到历史
                history.append({"role": "user", "content": user_input})
                
                # 流式输出响应
                print("[bold magenta]原神玩家sunsky > [/bold magenta]", end="")
                full_response = []
                for chunk in self._generate_stream(history):
                    print(chunk, end="", flush=True)
                    full_response.append(chunk)
                
                # 添加模型响应到历史
                history.append({"role": "assistant", "content": "".join(full_response)})
                print("\n")
                
            except KeyboardInterrupt:
                print("\n[yellow]已中断当前生成[/yellow]")
            except Exception as e:
                print(f"[red]错误: {str(e)}[/red]")
                break

if __name__ == "__main__":
    # 初始化（参数与start.sh匹配）
    chatter = DeepSeekChatter(
        model="./DeepSeek-R1-Distill-Qwen-1.5B",
        #model="./DeepSeek-R1-Distill-Qwen-7B",
        max_tokens=1024
    )
    chatter.chat_loop()