import pandas as pd
import streamlit as st

from app.utils import get_history

st.set_page_config(page_title="Prediction History", layout="wide")
st.title("📊 Prediction History")

history_df = get_history()

if history_df.empty:
    st.info("No prediction history found yet.")
else:
    search_term = st.text_input("Search by state or crop")
    if search_term:
        history_df = history_df[history_df.apply(lambda row: search_term.lower() in str(row["state"]).lower() or search_term.lower() in str(row["crop"]).lower(), axis=1)]

    history_df = history_df.sort_values(by="id", ascending=False)
    st.dataframe(history_df, use_container_width=True)

    csv = history_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "prediction_history.csv", "text/csv")
