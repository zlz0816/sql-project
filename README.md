# sql-project
# SQL智辅 · Python版
基于 FastAPI 开发的 SQL 智能辅助工具，前后端一体化，可直接部署使用。

## 项目简介
本项目是一个轻量级 SQL 辅助工具，提供 Web 可视化界面与 API 服务，适合学习、演示与简单业务场景使用。

## 项目结构
├── app/│ ├── api/ # 后端接口路由│ └── static/ # 前端静态页面（HTML/CSS/JS）├── main.py # 程序入口└── requirements.txt # 依赖包列表

## 环境依赖
- Python 3.8+
- fastapi
- uvicorn
- pydantic

## 本地运行
1. 安装依赖
```bash
pip install -r requirements.txt
启动服务
bash
运行
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
