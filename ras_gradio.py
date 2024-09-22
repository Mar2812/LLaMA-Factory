import gradio as gr
import requests
import json
from openai import OpenAI
llm_url = "http://0.0.0.0:4922/v1"
# 修改后的多轮对话函数，改为调用RAG API
def chat_multiple(message, history, session_id="123", temperature=0.0):
    client = OpenAI(api_key="0",base_url=llm_url)
    messages = [{"role": "user", "content": message}]
    result = client.chat.completions.create(messages=messages, model="/data2/machao/qwen/Qwen2.5-7B-Instruct")
    return result.choices[0].message.content

def create_gradio():
    with gr.Blocks() as demo:
        with gr.Tab("对话测试"):
            markdown_display = gr.Markdown('''
                这是女王小鑫鑫的聊天界面\n
            ''')
            # 创建 ChatInterface 调用 chat_multiple
            gr.ChatInterface(chat_multiple, fill_height=False)
    return demo


def run_gradio(server_name, server_port):
    """运行UI"""
    demo = create_gradio()
    demo.launch(share=True, server_name=server_name, server_port=server_port)


if __name__ == '__main__':
    run_gradio("0.0.0.0", 12800)
