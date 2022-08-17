import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Honey Report",
    page_icon="👋",
)

st.write("# DNA metabarcoding to evaluate biodiversity! 👋")

st.markdown(
    """
    Sustaina Honey is analyzed by DNA analysis provided by Bio-Insight.
    Out labs succeeded in developing DNA metabarcoding for plants and 
    now offers our proprietary analytical method. 
    
    **👈 Select a Sample-ID from the sidebar** to see your honey's DNA report.
    ### Want to know more?
    - Check out [bioinsight.co.jp](https://bioinsight.co.jp/)
  
"""
)


#データの読み込み
input_book = pd.ExcelFile('はちみつデータ.xlsx')
input_sheet_name = input_book.sheet_names
input_sheet_df = input_book.parse(input_sheet_name[0])


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'どのサンプルを表示しますか。検体名を選択してください',
    set(input_sheet_df['検体名'])
)


selected_id_df = input_sheet_df[input_sheet_df.検体名 == add_selectbox]
selected_id_df = selected_id_df.drop('検体名',axis = 1)
st.write("Here's the name of Genus:")
st.bar_chart(selected_id_df, x= 'Genus' ,y = 'DNA比率')
st.write("Here's the name of Species:")
st.bar_chart(selected_id_df, x= 'Species' ,y = 'DNA比率')
st.write("Honey DNA Data-table:")
st.write(selected_id_df)


# Adding code so we can have map default to the center of the data
st.write("The place of Honey extraction:")
input_sheet_df2 = input_book.parse(input_sheet_name[1])
input_sheet_df2 = input_sheet_df2.loc[:,('検体ID','緯度','経度')]
df_new = input_sheet_df2.rename(columns={'緯度': 'lat','経度':'lon'})
df_new = df_new.dropna()
df_new = df_new[df_new.検体ID == add_selectbox ]

st.map(df_new)





