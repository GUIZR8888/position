'''
streamlit多页面程序的入口文件
'''
import streamlit as st
st.title("智能ai互动界面")
col,col1,col2 = st.columns(3)
# 语言大模型应用程序功能入口
with col:
    st.image("https://aigc-files.bigmodel.cn/api/cogview/202410301549353839071934c849cc_0.png", use_column_width=True)
    flag = st.button("智能对话",use_container_width=True)
    if flag:
        st.switch_page("pages/huiyan.py")
# 文生图大模型应用程序入口
with col1:
    st.image("https://aigc-files.bigmodel.cn/api/cogview/202410301549353839071934c849cc_0.png", use_column_width=True)
    flag = st.button("智能绘图",use_container_width=True)
    if flag:
        st.switch_page("pages/textToImage.py")

# 岗位问答系统
with col2:
    st.image("https://aigc-files.bigmodel.cn/api/cogview/202410301549353839071934c849cc_0.png", use_column_width=True)
    flag = st.button("boos助手",use_container_width=True)
    if flag:
        st.switch_page("pages/job-ai.py")

