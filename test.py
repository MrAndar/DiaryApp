import streamlit as st


with st.form("Add a new Entry", clear_on_submit=True):
    st.title("Add a new diary entry")

    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("Enter date")
    with col2:
        time = st.time_input("Enter time")

    title = st.text_input("Entry title")
    entry = st.text_area("Enter diary entry:")
    submitted = st.form_submit_button("Save")

    if submitted:
        # Saving files
        filepath = f"entries/{date} - {str(time).replace(":", "-")} - {title}.txt"
        with open(filepath, "w") as file:
            file.write(entry)
        st.success("File saved successfully!")
