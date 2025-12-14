import streamlit as st
import pandas as pd
import os

st.title("Admin Feedback Dashboard")

if os.path.exists("reviews.csv") and os.path.getsize("reviews.csv") > 0:
    df = pd.read_csv("reviews.csv")

    st.subheader("All User Reviews")
    st.dataframe(df)

    avg_rating = df["rating"].mean()
    st.write(f"Average Rating: {avg_rating:.2f}")

    if avg_rating >= 4:
        action = "Maintain service quality and continue current practices."
    elif avg_rating >= 3:
        action = "Identify improvement areas and address customer concerns."
    else:
        action = "Immediate action required to improve customer experience."

    st.write("Suggested Action:", action)
else:
    st.info("No reviews available yet.")
