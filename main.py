from app.rag import answer_question
from app.pdf_loader import load_pdf_text

pdf_path = "data/Generative_AI_and_Techniques.pdf"
document = load_pdf_text(pdf_path)

question = "What is this document mainly about?"

answer = answer_question(document, question)

print("----- ANSWER -----")
print(answer)
