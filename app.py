import streamlit as st
from dputils import scrape as sc
import pandas as pd

def dataExtractor(item,pg_num):
    all_data = []
    for i in range(1,pg_num+1):
        url=f"https://www.amazon.in/s?k={item}&ref=nb_sb_noss&page={i}"
        soup = sc.get_webpage_data(url)
        target = {
            'tag':'div',
            'attrs': {
                'class':"s-main-slot s-result-list s-search-results sg-row"
            }
        }
        items = {'tag':'div','attrs':{'class' :'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'}}
        title = {'tag':'h2','attrs':{'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}}
        price = {'tag':'span','attrs':{'class':'a-price'}}
        output = sc.extract_many(soup,target=target, items=items, title=title, price=price)
        all_data.extend(output)
    df = pd.DataFrame(all_data)
    return df

st.sidebar.header('About Project')
st.sidebar.text('This is based on E-commerce web scraper')
st.header("Amazon Data Extractor")
st.subheader('This is a project for data extraction')


item = st.text_input('Enter the item name')
pg_num = st.number_input('Enter the page number',min_value=3, max_value=100, value=5)
btn = st.button('Click to extract')
if item and pg_num and btn:
    data = dataExtractor(item,pg_num)
    st.table(data)
