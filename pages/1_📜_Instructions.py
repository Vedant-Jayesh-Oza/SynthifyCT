import streamlit as st

st.set_page_config(page_icon="chart_with_upwards_trend", page_title="SynthifyCT", layout="centered")

st.subheader('Instructions')

st.write(
    """
    1. Upload the data in CSV format you want to generate data on - you can try with [auto-mpg.csv](https://drive.google.com/file/d/1iwH3VUWOvlyNw1a4K0r1E05gnc9ZHCVR/view?usp=sharing).

    2. Mention the column names as they are in the dataframe (include every column you want to generate data on). 

    3. Mention the target column (required to mention **one** column). For example, say 'origin' column of auto-mpg dataset.
    """
)

st.subheader('Precautions: ')

st.write(
    '''
    1. Please mention atleast one target/label column. 
    '''
)

st.subheader('Note:')

st.write(
    '''
    1. This data generation technique uses GANs for generating data and each time new data is uploaded, GAN model is trained on the new data and the quality of generated data depends on this training.

    2. Ideally for achieving best results, GAN model should be tuned each time but even without it, can achieve satisfactory results.

    3. Generated data is statistically similar to the original data and not a replica or copy of it.

    4. For more info, do visit the references in the About page. 
    '''
)
