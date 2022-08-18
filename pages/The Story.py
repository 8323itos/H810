import streamlit as st
from PIL import Image

st.markdown("# Sustaina Honey Story")

image = Image.open('flower.jpg')

st.image(image, caption='hana',use_column_width=True)


st.markdown(
    """
    Sustaina Honey is from just the idea our labs.
    
    We are surveying vegetation in Japan by Honey DNA analysis and could know rich biodiversity. 
    
    But, We have not been able to inform the public extensively about this.
    
    So, how about enjoying the honey with DNArepot. 
    We can make people aware of the importance of biodiversity through honey,
    and know lots of delicious, quality honey.
    
    Enjoy our Sustaina Honey and share our biodiversity!👋
    
  
""")