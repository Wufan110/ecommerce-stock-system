import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generate_sample_data(n_records=2000):
    """生成模拟电商数据"""
    np.random.seed(42)
    random.seed(42)
    
    products = {
        'P001': {'name': 'iPhone 14 Pro', 'category': '电子产品', 'brand': 'Apple', 'price': 7999},
        'P002': {'name': 'iPhone 14', 'category': '电子产品', 'brand': 'Apple', 'price': 5999},
        'P003': {'name': '三星 Galaxy S23', 'category': '电子产品', 'brand': 'Samsung', 'price': 5699},
        'P004': {'name': '小米13', 'category': '电子产品', 'brand': '小米', 'price': 3999},
        'P005': {'name': '华为Mate 50', 'category': '电子产品', 'brand': '华为', 'price': 4999},
        'P006': {'name': 'MacBook Air', 'category': '电子产品', 'brand': 'Apple', 'price': 8999},
        'P007': {'name': 'ThinkPad X1', 'category': '电子产品', 'brand': '联想', 'price': 9999},
        'P008': {'name': '男士休闲裤', 'category': '服装', 'brand': '优衣库', 'price': 199},
        'P009': {'name': '女士针织衫', 'category': '服装', 'brand': 'ZARA', 'price': 299},
        'P010': {'name': '咖啡机', 'category': '家居', 'brand': '德龙', 'price': 1299}
    }
    
    # 生成销售数据
    sales_data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(n_records):
        product_id = random.choice(list(products.keys()))
        product_info = products[product_id]
        quantity = random.randint(1, 3)
        unit_price = product_info['price']
        total_price = quantity * unit_price
        
        days_offset = random.randint(0, 365)
        order_date = start_date + timedelta(days=days_offset)
        
        base_stock = random.randint(20, 100)
        days_from_start = (order_date - start_date).days
        current_stock = max(0, base_stock - int(days_from_start * 0.1) + random.randint(-5, 5))
        
        customer_id = f"C{random.randint(1000, 1999)}"
        country = random.choice(['中国', '美国', '英国', '德国', '日本', '法国'])
        
        sales_data.append({
            'InvoiceNo': f'INV{10000 + i}',
            'StockCode': product_id,
            'Description': product_info['name'],
            'Quantity': quantity,
            'UnitPrice': unit_price,
            'TotalPrice': total_price,
            'InvoiceDate': order_date,
            'CustomerID': customer_id,
            'Country': country,
            'Category': product_info['category'],
            'Brand': product_info['brand'],
            'StockQuantity': current_stock,
            'IsOutOfStock': current_stock == 0
        })
    
    df_sales = pd.DataFrame(sales_data)
    
    # 生成商品数据
    product_attributes = []
    for product_id, info in products.items():
        product_attributes.append({
            'StockCode': product_id,
            'ProductName': info['name'],
            'Category': info['category'],
            'Brand': info['brand'],
            'Price': info['price']
        })
    
    df_products = pd.DataFrame(product_attributes)
    
    print(f"✅ 数据生成完成: {len(df_sales)} 条销售记录, {len(df_products)} 个商品")
    return df_sales, df_products

def load_sales_data():
    """加载销售数据"""
    # 使用绝对路径
    data_path = os.path.join('ecommerce_stock_system', 'data', 'sales_data.csv')
    df = pd.read_csv(data_path, parse_dates=['InvoiceDate'])
    print(f"✅ 销售数据加载成功: {len(df)} 条记录")
    return df

def load_product_data():
    """加载商品数据"""
    # 使用绝对路径
    data_path = os.path.join('ecommerce_stock_system', 'data', 'product_data.csv')
    df = pd.read_csv(data_path)
    print(f"✅ 商品数据加载成功: {len(df)} 个商品")
    return df

def get_data_summary(df_sales, df_products):
    """获取数据摘要"""
    summary = {
        'sales_records': len(df_sales),
        'products_count': len(df_products),
        'date_range': f"{df_sales['InvoiceDate'].min().strftime('%Y-%m-%d')} 至 {df_sales['InvoiceDate'].max().strftime('%Y-%m-%d')}",
        'total_sales': f"￥{df_sales['TotalPrice'].sum():,.0f}",
        'out_of_stock_rate': f"{df_sales['IsOutOfStock'].mean()*100:.1f}%",
        'categories': df_sales['Category'].nunique()
    }
    return summary

# 如果直接运行这个文件，测试数据加载
if __name__ == "__main__":
    sales_df = load_sales_data()
    products_df = load_product_data()
    summary = get_data_summary(sales_df, products_df)
    print("📊 数据摘要:")
    for key, value in summary.items():
        print(f"   {key}: {value}")
