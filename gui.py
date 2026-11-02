import streamlit as st
from library_managment import books

book_instance = books()

tab1, tab2 = st.tabs(["Add","view"])

with tab1:
    st.header("add new books")
    book_name = st.text_input("Enter Book Name")
    author_name = st.text_input("enter Author_name")
    price = st.text_input("enter Price")
    type = st.text_input("enter the book's type")
    published_year = st.text_input("enter published year")
    if st.button("add new book"):
        book_instance.post(book_name=book_name, author_name=author_name, price=price,type=type, published_year = published_year)
        st.success("new book added successfully..!")
with tab2:
    st.header("view book details")
    records = book_instance.get()
    # print(records)
    if records:
        st.table(records)
    else:
        st.warning("no book details found")