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

with col2:
    st.title("Find Pattern in Sequence")

# Inputs
fasta = st.text_area("Enter the sequence here", "AGGGCACTCAGGAAACCAGCTCAAGTCCTTATTGAGGTCACTGCGTCTCAAATACCCGGGCTGGGCCTGTGACTCACACACCAGCACCAACAACCAGGGGGTGGGATATTGCATCAGGAAAAGCTCCACTCTGGGTGGAACCTGCTTTTCAACCTCATTGGGTGTGTCACCGCCCAGTGGGTTCACCTTGCCCGCTGCCT")
pattern1 = st.text_input("Enter the first pattern", "GGG")
pattern2 = st.text_input("Enter the second pattern", "TCA")

pos_all = []
pos_all2 = []
p_pos = []
l_pair = []
s_pair =[]

if st.button("Find the Patterns"):

    for match in re.finditer(pattern1, fasta):
        pos_all.append(match.start())
    # st.write(f'Pos: {str(pos_all)}')
    
    # if match:
    for i in range(0,len(pos_all)-1):
        p_pos.append((pos_all[i],pos_all[i+1]))
    # st.write(f'Paired: {str(p_pos)}')
    for i in range(0,len(p_pos)):
        l_pair.append(p_pos[i][1]-p_pos[i][0])
        s_pair.append(fasta[p_pos[i][0]:p_pos[i][1]])
    # st.write(f'Segment: {s_pair}')
    # st.write(f'Segment Length: {l_pair}')

    data = {
    'Sequence': s_pair,
    'Length': tuple(l_pair)
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Reorder columns and sort
    s_df = df[['Sequence', 'Length']].sort_values(
        by='Length', ascending=False).reset_index(drop=True)

    # Display the DataFrame
    # st.dataframe(s_df, use_container_width=True)
    st.write(s_df)

    datap3=[]
    for i in range(0,s_df.shape[0]):
        datap2 =[]
        seq2 = []
        # st.write(s_df['Sequence'][i])

        for match in re.finditer(pattern2, s_df['Sequence'][i]):
            datap2.append(match.start())
        
        # st.write(f'Pos: {len(datap2) }')

        if len(datap2)>1:
            
            for k in range(0,len(datap2)-1):
                # st.write(datap2[k])
                seq2.append((s_df['Sequence'][i][datap2[k]+1:datap2[k+1]]))
                # st.write((s_df['Sequence'][i][datap2[k]:datap2[k+1]]))
        # st.write(seq2)


        # for j in range(0,)
        row = {
        'id': i,
        'Sequence': s_df['Sequence'][i],
        'Index': seq2
        }
        datap3.append(row)
        # st.write(row)
    st.write(datap3)

