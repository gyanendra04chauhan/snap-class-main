import streamlit as st

from supabase import create_client, client

supabase:client = create_client(
    st.secrets["supabase_url"],
    st.secrets["supabase_key"]
)