import streamlit as st
import pandas as pd
import numpy as np
import statistics
from sklearn.ensemble import RandomForestClassifier
#st.write('# Simple Level of Depression Prediction App')
#st.sidebar.header('User Input')
#st.sidebar.subheader('Rate the extent to which the pair of traits applies to you, even if one characteristic applies more strongly than the other')
#st.sidebar.subheader('1:Disagree strongly; 5: Agree strongly')
st.write('# Dự đoán nguy cơ trầm cảm dựa trên tính cách')
st.sidebar.header('Thông tin người dùng')
st.sidebar.subheader('Bạn hãy chọn một số bên cạnh mỗi câu để chỉ mức độ mà bạn đồng ý hoặc không đồng ý với tuyên bố đó')
st.sidebar.subheader('1: Không đồng ý mạnh mẽ; 5: Đồng ý mạnh mẽ')

def user_input():
    a1 = st.sidebar.slider('Hướng ngoại, nhiệt tình (Extraverted, enthusiastic)', 1, 5, 2)
    a2 = st.sidebar.slider('Hay phán đoán, gây gổ (Critical, quarrelsome)', 1, 5, 5)
    a3 = st.sidebar.slider('Có thể được trông cậy, có tính kỉ luật (Dependable, self-disciplined)', 1, 5, 2)
    a4 = st.sidebar.slider('Lo lắng, dễ nổi nóng (Anxious, easily upset)', 1, 5, 2)
    a5 = st.sidebar.slider('Sẵn sàng trải nghiệm, phức tạp (Open to new experiences, complex)', 1, 5, 2)
    a6 = st.sidebar.slider('Kín đáo, im lặng (Reserved, quiet)', 1, 5, 2)
    a7 = st.sidebar.slider('Cảm thông, ấm áp (Sympathetic, warm)', 1, 5, 2)
    a8 = st.sidebar.slider('Bừa bộn, vô tư (Disorganized, careless)', 1, 5, 2)
    a9 = st.sidebar.slider('Bình tĩnh, tâm lí ổn định (Calm, emotionally stable)', 1, 5, 2)
    a10 = st.sidebar.slider('Thông thường, không sáng tạo (Conventional, uncreative)', 1, 5, 2)

    liO = [1,2,3,4,5,6,7]
    liO_reversed = liO[::-1]
    reversed_num2 = liO_reversed[a2-1]
    reversed_num4 = liO_reversed[a4-1]
    reversed_num6 = liO_reversed[a6-1]
    reversed_num8 = liO_reversed[a8-1]
    reversed_num10 = liO_reversed[a10-1]

    grp1 = [int(a1),reversed_num6]
    grp2 = [int(a7),reversed_num2]
    grp3 = [int(a3),reversed_num8]
    grp4 = [int(a9),reversed_num4]
    grp5 = [int(a5),reversed_num10]

    data ={'EX':statistics.mean(grp1),
            'AG' :statistics.mean(grp2),
            'CON':statistics.mean(grp3),
            'ES' :statistics.mean(grp4),
            'OP' :statistics.mean(grp5)          }
    features = pd.DataFrame(data, index=[0])
    return features

df1 = user_input()
st.write(df1)

EX = 'EX: Extraversion-Hướng ngoại'
AG = 'AG: Agreeableness-Tính dễ chịu '
CON = 'CON: Conscientiousness- Nhận thức'
ES = 'ES: Emotional Stability- Ổn định tâm lí'
OP = 'OP: Openness to Experiences- Rộng mở với trải nghiệm mới'
liOS = [EX,AG,CON,ES,OP]

if st.checkbox('Show explanation-Giải thích thuật ngữ'):
    liOS


#def user_input_features():
    #EX = st.sidebar.slider('EX', 1, 5, 2)
    #AG = st.sidebar.slider('AG', 1, 5, 2)
    #CON = st.sidebar.slider('CON', 1, 5, 2)
    #ES = st.sidebar.slider('ES', 1, 5, 2)
    #OP = st.sidebar.slider('OP', 1, 5, 2)
    #data = {'EX': int(EX),
     #       'AG': int(AG),
    #        'CON': int(CON),
   #         'ES': int(ES),
  #          'OP': int(OP)}
 #   features = pd.DataFrame(data, index=[0])
 #   return features

#df1 = user_input_features()
#st.write(df1)

df =pd.read_csv("C:/ISEF/KHAO_SAT_tipi - Form Responses 1.csv") 
df.drop(['Timestamp','SUM','Unnamed: 24','Hãy ghi ít nhất 3 câu tâm trạng của bạn bây giờ ( ít nhất 50 từ)','Score','ĐỀ MỤC 1','ĐỀ MỤC 2','ĐỀ MỤC 3','ĐỀ MỤC 4','ĐỀ MỤC 5','ĐỀ MỤC 6','ĐỀ MỤC 7','ĐỀ MỤC 8','ĐỀ MỤC 9','ĐỀ MỤC 10','ĐỀ MỤC 11','ĐỀ MỤC 12','ĐỀ MỤC 13','ĐỀ MỤC 14','ĐỀ MỤC 15','ĐỀ MỤC 16','ĐỀ MỤC 17','ĐỀ MỤC 18','ĐỀ MỤC 19','ĐỀ MỤC 20','ĐỀ MỤC 21','REVERSED R2','REVERSED R4','REVERSED R6','REVERSED R8','REVERSED R10','Hướng ngoại, nhiệt tình (Extraverted, enthusiastic.)','Hay phán đoán, gây gổ (Critical, quarrelsome.)','Có thể được trông cậy, có tính kỉ luật (Dependable, self-disciplined.)','Lo lắng, dễ nổi nóng (Anxious, easily upset.)','Sẵn sàng trải nghiệm, phức tạp (Open to new experiences, complex.)','Kín đáo, im lặng (Reserved, quiet.)','Cảm thông, ấm áp (Sympathetic, warm.)','Bừa bộn, vô tư (Disorganized, careless.)','Bình tĩnh, tâm lí ổn định (Calm, emotionally stable.)','Thông thường, không sáng tạo (Conventional, uncreative.)'], axis=1, inplace=True)
X = df[['EX','AG','CON','ES','OP']]
Y = df['LABEL']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df1)
prediction_proba = clf.predict_proba(df1)

st.subheader('Mã số của mức độ nguy cơ')
st.write(df.LABEL.unique())


st.subheader('Dự đoán')
st.write(prediction)

st.subheader('Xác suất dự đoán')
st.write(prediction_proba)