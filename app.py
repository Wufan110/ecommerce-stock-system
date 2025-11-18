import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import sys
import os

# 设置页面
st.set_page_config(
    page_title="电商库存智能管理系统",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 应用标题
st.title("📊 电商库存智能管理系统")
st.markdown("---")

# 侧边栏导航
st.sidebar.title("导航菜单")
page = st.sidebar.selectbox(
    "选择功能页面",
    ["仪表板概览", "库存监控", "商品推荐", "预测分析", "数据探索"]
)

# 模拟数据加载函数
def load_sample_data():
    """生成示例数据用于演示"""
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', '2024-03-20', freq='D')
    
    data = {
        'date': dates,
        'product_id': np.random.choice(['P001', 'P002', 'P003', 'P004', 'P005'], len(dates)),
        'product_name': np.random.choice(['商品A', '商品B', '商品C', '商品D', '商品E'], len(dates)),
        'category': np.random.choice(['电子产品', '家居用品', '服装', '食品', '图书'], len(dates)),
        'sales': np.random.randint(10, 100, len(dates)),
        'stock': np.random.randint(0, 200, len(dates)),
        'price': np.random.uniform(10, 500, len(dates)).round(2)
    }
    
    return pd.DataFrame(data)

# 各页面内容
if page == "仪表板概览":
    st.header("📈 业务概览仪表板")
    
    # 加载数据
    df = load_sample_data()
    
    # KPI指标
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("总销售额", f"¥{df['sales'].sum() * df['price'].mean():,.0f}")
    
    with col2:
        st.metric("平均库存", f"{df['stock'].mean():.0f}件")
    
    with col3:
        st.metric("商品种类", f"{df['product_id'].nunique()}种")
    
    with col4:
        st.metric("缺货风险", "12%", "-3%")
    
    # 销售趋势图
    st.subheader("销售趋势")
    daily_sales = df.groupby('date')['sales'].sum()
    fig, ax = plt.subplots(figsize=(10, 4))
    daily_sales.plot(ax=ax, color='skyblue', linewidth=2)
    ax.set_title('每日销售趋势')
    ax.set_ylabel('销售量')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif page == "库存监控":
    st.header("📦 库存监控预警")
    
    df = load_sample_data()
    
    # 识别低库存商品
    latest_stock = df.groupby('product_name')['stock'].last().reset_index()
    low_stock = latest_stock[latest_stock['stock'] < 50]
    
    st.subheader("🔴 低库存预警商品")
    if not low_stock.empty:
        st.dataframe(low_stock)
    else:
        st.success("🎉 当前无低库存风险商品")

elif page == "商品推荐":
    st.header("🎯 智能商品推荐")
    
    st.info("基于销售数据和库存情况的智能推荐系统")
    
    # 模拟推荐结果
    recommendations = [
        {"商品": "商品A", "推荐理由": "高销量低库存", "行动": "立即补货"},
        {"商品": "商品C", "推荐理由": "库存积压严重", "行动": "促销活动"},
        {"商品": "商品E", "推荐理由": "季节性需求增长", "行动": "增加库存"}
    ]
    
    for rec in recommendations:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{rec['商品']}** - {rec['推荐理由']}")
            with col2:
                st.button(rec['行动'], key=rec['商品'])

elif page == "预测分析":
    st.header("🔮 销售预测分析")
    
    st.warning("⚠️ 预测模型加载中...")
    
    # 简单的趋势预测
    df = load_sample_data()
    future_dates = pd.date_range('2024-03-21', '2024-03-30', freq='D')
    
    st.subheader("未来10天销售预测")
    prediction_data = {
        '日期': future_dates,
        '预测销量': np.random.randint(80, 120, len(future_dates))
    }
    pred_df = pd.DataFrame(prediction_data)
    st.line_chart(pred_df.set_index('日期')['预测销量'])

elif page == "数据探索":
    st.header("🔍 数据探索分析")
    
    df = load_sample_data()
    
    st.subheader("原始数据预览")
    st.dataframe(df.head(20))
    
    st.subheader("数据统计")
    st.write(df.describe())

# 页脚
st.markdown("---")
st.markdown("© 2024 电商库存智能管理系统 | 基于Streamlit构建")