import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

def prepare_product_features(df_products):
    """准备商品特征用于相似度计算"""
    features_df = df_products.copy()
    
    # 对分类变量进行编码
    categorical_columns = ['Category', 'Brand']
    encoders = {}
    
    for col in categorical_columns:
        le = LabelEncoder()
        features_df[col + '_encoded'] = le.fit_transform(features_df[col].fillna('Unknown'))
        encoders[col] = le
    
    # 选择数值特征
    feature_columns = ['Price', 'Category_encoded', 'Brand_encoded']
    
    # 标准化数值特征
    scaler = StandardScaler()
    product_features = scaler.fit_transform(features_df[feature_columns])
    
    return product_features, features_df, scaler, encoders

def create_similarity_matrix(df_products):
    """创建商品相似度矩阵"""
    product_features, features_df, scaler, encoders = prepare_product_features(df_products)
    
    # 计算余弦相似度
    similarity_matrix = cosine_similarity(product_features)
    
    # 转换为DataFrame
    similarity_df = pd.DataFrame(
        similarity_matrix, 
        index=df_products['StockCode'], 
        columns=df_products['StockCode']
    )
    
    print("✅ 商品相似度矩阵创建完成")
    return similarity_df

def prepare_stock_features(df_sales):
    """准备库存预测特征"""
    # 按商品聚合特征
    product_features = []
    
    for product_id in df_sales['StockCode'].unique():
        product_data = df_sales[df_sales['StockCode'] == product_id]
        
        features = {
            'ProductID': product_id,
            '总销量': product_data['Quantity'].sum(),
            '平均价格': product_data['UnitPrice'].mean(),
            '销售天数': (product_data['InvoiceDate'].max() - product_data['InvoiceDate'].min()).days + 1,
            '日均销量': product_data['Quantity'].sum() / 365,  # 简化计算
            '缺货率': product_data['IsOutOfStock'].mean(),
            '最近库存': product_data['StockQuantity'].iloc[-1]
        }
        
        product_features.append(features)
    
    features_df = pd.DataFrame(product_features)
    features_df = features_df.set_index('ProductID')
    
    # 创建预测标签
    features_df['预计售罄天数'] = features_df['最近库存'] / (features_df['日均销量'] + 0.1)
    features_df['未来7天缺货风险'] = (features_df['预计售罄天数'] <= 7).astype(int)
    
    return features_df
