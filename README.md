![部署状态](https://img.shields.io/badge/部署-在线成功-brightgreen)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
# 电商商品智能替换系统

## 项目简介
基于机器学习的电商库存预警和商品替代推荐系统，帮助电商企业减少缺货损失。

## 项目位置
C:/Users/27248/ecommerce_stock_system

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 在Jupyter中运行分析
```python
# 在Jupyter中运行
import sys
sys.path.append('./src')

from data_loader import load_sales_data, load_product_data

# 加载数据
sales_df = load_sales_data()
products_df = load_product_data()

print('数据加载成功!')
```

### 3. 打开分析笔记本
运行: notebooks/01_data_analysis.ipynb

## 项目结构
```
ecommerce_stock_system/
├── data/              # 数据文件
│   ├── sales_data.csv
│   └── product_data.csv
├── notebooks/         # Jupyter分析笔记本
│   └── 01_data_analysis.ipynb
├── src/              # Python源代码
│   ├── data_loader.py
│   └── feature_engine.py
├── reports/          # 分析报告
├── requirements.txt  # 依赖包
└── README.md         # 项目说明
```

## 功能特性
- 缺货风险预测
- 智能商品推荐
- 实时库存监控
- 多级风险预警

## 技术栈## 🌐 在线演示

[![Streamlit App](https://ecommerce-stock-system-nwxpappw3rruv6majw8grp2.streamlit.app/)](你的部署链接)

现场体验所有功能：https://你的应用名称.streamlit.app
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook


