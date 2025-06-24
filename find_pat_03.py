import streamlit as st
import re
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Find DNA Pattern",
    layout="wide",
    initial_sidebar_state="auto"
)

col1, col2 = st.columns([1,3])
# with col1:
#     st.image(image)
with col2:
    st.title("Find Pattern in Sequence")

# Inputs
fasta = st.text_area("Enter the sequence", "AGGCCGGGCACCCGGTCGAATTCAGGAAACCGGCCAGCGAATTCTCAACCGGGTCCTTAGAATTCTTGCCGGAGGTCACTGCGTCTCAAGAATTCATACCCGGCCGGGCGAATTCTGGGCCTGTGCCGGACTCACACACCAGCACCAACAACCAGGGGGTGGGATATTGCATCAGGAAAAGCTCCACTCTGGGTGGAACCTGCTTTTCAACCTCATTGGGTGTGTCACCGCCCAGTGGGTTCACCTTGCCCGCTGCCT")
pattern1 = st.text_input("Enter the first pattern", "CCGG")
pattern2 = st.text_input("Enter the second pattern", "GAATTC")

patterns = [pattern1,pattern2]

# st.write(patterns)

p_pos = []
all_pats = []
if st.button("Find the Patterns"):

    for i in range(0,len(patterns)):
        # st.write(i)
        pos_all =[]
        for match in re.finditer(patterns[i], fasta):
            pos_all.append(match.start())
        # st.write(f'PosPat: {patterns[i]}: {str(pos_all)}')

        data = {
        'id': i,
        'sequence': patterns[i],
        'index': pos_all
        }
        all_pats.append(data)

    # df = pd.DataFrame(data)
    st.dataframe(all_pats, use_container_width=True)
