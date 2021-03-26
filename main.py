import streamlit as st
import pandas as pd 

df = pd.read_excel("articlelinks.xlsx")
df = df.dropna(subset=["标题"])
st.dataframe(df)

platform = st.radio("Which platform?",
            ('微信', '知乎', '科学网', '少数派', 'medium'))
keyword = st.text_input("搜索关键词", "Roam")

df1 = df[df['标题'].str.contains(keyword)]
df1 = df1.dropna(subset=[platform]).reset_index()[['标题', platform]]
choice = st.radio("Select the one you want to include:", df1[['标题']])
if st.button("Get Link!"):
    df_result = df1[df1['标题'].str.match(choice)]
    link = df_result.iloc[0, 1]
    output_str = f"[{choice}]({link})"
    st.write(output_str)
