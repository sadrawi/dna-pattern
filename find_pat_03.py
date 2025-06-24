import streamlit as st
import re
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="i3L AI System",
    layout="wide",
    initial_sidebar_state="auto"
)

image = Image.open('i3l_logo.png')

col1, col2 = st.columns([1,3])
with col1:
    st.image(image)
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
all_ind = []
if st.button("Find the Patterns"):

    for i in range(0,len(patterns)):
        # st.write(i)
        pos_all =[]
        for match in re.finditer(patterns[i], fasta):
            pos_all.append(match.start())
        # st.write(f'PosPat: {patterns[i]}: {str(pos_all)}')

        data = {
        # 'id': i,
        'sequence': patterns[i],
        'index': pos_all
        }
        all_pats.append(data)

    # df = pd.DataFrame(data)
    st.dataframe(all_pats, use_container_width=True)

    print(all_pats)
    # for j in range(0,len(all_pats)):

    #     all_ind.append(tuple(all_pats[j]['index']))
    # # st.write(all_pats[0]['index'])
    # st.write(all_ind)

    # for j in range(0,len(all_pats)):
    #     print(all_pats['index'])
    # st.write(len(all_pats))
    # # if match1:
    # for i in range(0,len(pos_all1)-1):
    #     p_pos.append((pos_all1[i],pos_all1[i+1]))
    # # st.write(f'Paired: {str(p_pos)}')
    # for i in range(0,len(p_pos)):
    #     l_pair.append(p_pos[i][1]-p_pos[i][0])
    #     s_pair.append(fasta[p_pos[i][0]:p_pos[i][1]])
    # # st.write(f'Segment: {s_pair}')
    # # st.write(f'Segment Length: {l_pair}')

    # data = {
    # 'Sequence': s_pair,
    # 'Length': tuple(l_pair)
    # }

    # # Create DataFrame
    # df = pd.DataFrame(data)

    # # Reorder columns and sort
    # s_df = df[['Sequence', 'Length']].sort_values(
    #     by='Length', ascending=False).reset_index(drop=True)

    # # Display the DataFrame
    # # st.dataframe(s_df, use_container_width=True)
    # st.write(s_df)


