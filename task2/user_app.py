import streamlit as st
import pandas as pd
import os

st.title("User Feedback Dashboard")

rating = st.selectbox("Select your rating (1–5)", [1, 2, 3, 4, 5])
review = st.text_area("Write your review")

if st.button("Submit Feedback"):
    if review.strip() == "":
        st.warning("Please write a review before submitting.")
    else:
        if os.path.exists("reviews.csv") and os.path.getsize("reviews.csv") > 0:
            df = pd.read_csv("reviews.csv")
        else:
            df = pd.DataFrame(columns=["rating", "review", "ai_response"])

        ai_response = "Thank you for your feedback! We appreciate your input."

        new_row = {
            "rating": rating,
            "review": review,
            "ai_response": ai_response
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv("reviews.csv", index=False)

        st.success("Feedback submitted successfully!")
        st.write("AI Response:", ai_response)
