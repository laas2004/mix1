# import streamlit as st
# import os
# import hashlib

# from app.pdf_loader import load_pdf_text
# from app.rag import answer_question

# # ----------------------------------
# # Streamlit page config
# # ----------------------------------
# st.set_page_config(page_title="AI Document Q&A", layout="centered")

# st.title("📄 PRAGYA LEGAL AGENT")
# st.write("Upload a PDF and ask questions grounded in the document.")

# # ----------------------------------
# # Session state initialization
# # ----------------------------------
# if "vector_ready" not in st.session_state:
#     st.session_state.vector_ready = False

# if "last_pdf_hash" not in st.session_state:
#     st.session_state.last_pdf_hash = None

# # ----------------------------------
# # Helper: cache path from file hash
# # ----------------------------------


# def get_cache_path(file_path):
#     with open(file_path, "rb") as f:
#         file_hash = hashlib.md5(f.read()).hexdigest()
#     return f"data/cache/{file_hash}.pkl", file_hash


# # ----------------------------------
# # PDF upload
# # ----------------------------------
# uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# if uploaded_file:
#     os.makedirs("data/docs", exist_ok=True)
#     os.makedirs("data/cache", exist_ok=True)

#     pdf_path = os.path.join("data/docs", uploaded_file.name)

#     # Save uploaded PDF
#     with open(pdf_path, "wb") as f:
#         f.write(uploaded_file.read())

#     cache_path, pdf_hash = get_cache_path(pdf_path)

#     # NEW PDF → reset vectors
#     if st.session_state.last_pdf_hash != pdf_hash:
#         st.session_state.vector_ready = False
#         st.session_state.last_pdf_hash = pdf_hash

#     st.success("PDF uploaded successfully ✅")

#     # ----------------------------------
#     # Read PDF ONCE
#     # ----------------------------------
#     with st.spinner("Reading PDF..."):
#         document = load_pdf_text(pdf_path)

#     # ----------------------------------
#     # Question input
#     # ----------------------------------
#     question = st.text_input("Ask a question about the document")

#     if question:
#         with st.spinner("Thinking..."):
#             answer, context, evaluation = answer_question(
#                 document=document,
#                 question=question,
#                 cache_path=cache_path
#             )

#             st.session_state.vector_ready = True

#         # ----------------------------------
#         # Display output
#         # ----------------------------------
#         st.subheader("Answer")
#         st.write(answer)

#         with st.expander("Retrieved Context"):
#             st.write(context)

#         with st.expander("Evaluation"):
#             st.json(evaluation)

# v2
# import streamlit as st
# import os

# from ui_layer.auth import check_admin_password
# from ui_layer.ingest_wrapper import ingest_pdf
# from ui_layer.query_wrapper import ask_question

# st.set_page_config(page_title="PRAGYA LEGAL AGENT", layout="centered")
# st.title("📄 PRAGYA LEGAL AGENT")

# # ----------------------------
# # Role selection
# # ----------------------------
# role = st.selectbox(
#     "Select your role",
#     ["Employee", "Junior HR", "Admin"]
# )

# # ----------------------------
# # ADMIN PANEL
# # ----------------------------
# if role == "Admin":
#     password = st.text_input("Admin password", type="password")

#     if not check_admin_password(password):
#         st.warning("Admin access required")
#         st.stop()

#     st.success("Admin authenticated ✅")

#     uploaded_files = st.file_uploader(
#         "Upload PDFs",
#         type=["pdf"],
#         accept_multiple_files=True
#     )

#     if uploaded_files:
#         os.makedirs("data/pdfs", exist_ok=True)

#         for file in uploaded_files:
#             path = os.path.join("data/pdfs", file.name)

#             with open(path, "wb") as f:
#                 f.write(file.read())

#             with st.spinner(f"Ingesting {file.name}..."):
#                 ingest_pdf(path)

#         st.success("Documents ingested successfully 🎯")

# # ----------------------------
# # QUERY SECTION (ALL ROLES)
# # ----------------------------
# st.divider()
# st.subheader("Ask a question")

# question = st.text_input("Your question")

# if question:
#     with st.spinner("Querying knowledge base..."):
#         raw_output = ask_question(question)

#     # Remove terminal-only prompts
#     lines_to_remove = [
#         "RAG system ready. Type 'exit' to quit.",
#         "Ask a question (or 'exit'):"
#     ]

#     clean_output = raw_output
#     for line in lines_to_remove:
#         clean_output = clean_output.replace(line, "").strip()

#     st.markdown(
#         f"""
# {clean_output}

# """,
#         unsafe_allow_html=False
#     )

# v3-v2 works fine if this doesn't, only change is admin panel
import streamlit as st
import os

from ui_layer.auth import check_admin_password
from ui_layer.ingest_wrapper import ingest_pdf
from ui_layer.query_wrapper import ask_question

st.set_page_config(page_title="PRAGYA LEGAL AGENT", layout="centered")
st.title("📄 PRAGYA LEGAL AGENT")

# ----------------------------
# Role selection
# ----------------------------
role = st.selectbox(
    "Select your role",
    ["Employee", "Junior HR", "Admin"]
)

# ----------------------------
# ADMIN PANEL
# ----------------------------
if role == "Admin":
    password = st.text_input("Admin password", type="password")

    if not check_admin_password(password):
        st.warning("Admin access required")
        st.stop()

    st.success("Admin authenticated ✅")

    # ----------------------------
    # Upload Section
    # ----------------------------
    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        os.makedirs("data/pdfs", exist_ok=True)

        for file in uploaded_files:
            path = os.path.join("data/pdfs", file.name)

            with open(path, "wb") as f:
                f.write(file.read())

        st.success("Files uploaded successfully 📁")

    # ----------------------------
    # Ingestion Button
    # ----------------------------
    if st.button("Run Ingestion"):
        with st.spinner("Running ingestion pipeline..."):
            try:
                output = ingest_pdf()
                st.success("Ingestion completed successfully 🎯")
                st.text_area("Ingestion Logs", output, height=300)

            except Exception as e:
                st.error("Ingestion failed ❌")
                st.text_area("Error Details", str(e), height=300)

# ----------------------------
# QUERY SECTION (ALL ROLES)
# ----------------------------
st.divider()
st.subheader("Ask a question")

question = st.text_input("Your question")

if question:
    with st.spinner("Querying knowledge base..."):
        raw_output = ask_question(question)

    # Remove terminal-only prompts
    lines_to_remove = [
        "RAG system ready. Type 'exit' to quit.",
        "Ask a question (or 'exit'):"
    ]

    clean_output = raw_output
    for line in lines_to_remove:
        clean_output = clean_output.replace(line, "").strip()

    st.markdown(
        f"""
{clean_output}

""",
        unsafe_allow_html=False
    )