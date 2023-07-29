import streamlit as st

@st.cache_data(ttl=60)
def get_map():
    import json
    with open('map.json') as f:
        return json.load(f)

st.write("# COC屏蔽词转换")

mapping = get_map()

def clear_text():
    st.session_state["text"] = ""


input = st.text_area("输入", key='text', placeholder='部落战，大家加油！', max_chars=1024)

cols = st.columns(6)

with cols[-2]:
    st.button("清空", on_click=clear_text)

with cols[-1]:
    submit = st.button("提交")

st.write('输出(最右边可以一键复制)')

if submit:
    text = st.session_state["text"]
    for k, v in mapping.items():
        text = text.replace(k, v)
    st.markdown('<style> code span {white-space: normal}</style>', unsafe_allow_html=True)
    st.code(text)
