"""
练习: HTTP请求

描述：
本练习帮助您学习如何使用requests库发送HTTP请求并处理响应。
注意：运行此练习前，请确保已安装requests库（pip install requests）。

请补全下面的函数，实现发送HTTP请求并处理响应的功能。
"""
import requests

def get_website_content(url):
    """
    发送GET请求获取网页内容
    
    参数:
    - url: 目标网站URL
    
    返回:
    - 包含响应信息的字典: 
      {
        'status_code': HTTP状态码,
        'content': 响应内容文本,
        'headers': 响应头部信息
      }
    """
    # 请在下方编写代码
    # 使用requests.get()发送GET请求
    # 返回包含状态码、内容和头部信息的字典
    response = requests.get(url)
    return {
        'status_code': response.status_code,
        'content': response.text,
        'headers': dict(response.headers)
    }
    pass

def post_data(url, data):
    """
    发送POST请求提交数据
    
    参数:
    - url: 目标网站URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典:
      {
        'status_code': HTTP状态码,
        'response_json': 响应的JSON数据(如果有),
        'success': 请求是否成功(状态码为2xx)
      }
    """
    # 请在下方编写代码
    # 使用requests.post()发送POST请求
    # 返回包含状态码、响应JSON和成功标志的字典
    response = requests.post(url, data=data)
    return {
        'status_code': response.status_code,
        'response_json': response.json() if response.headers.get('Content-Type', '').startswith('application/json') else None,
        'success': 200 <= response.status_code < 300
    }
    pass