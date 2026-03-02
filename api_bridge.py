# from flask import Flask, request, jsonify
# from ui_layer.query_wrapper import ask_question

# app = Flask(__name__)

# @app.route("/query", methods=["POST"])
# def query():
#     try:
#         data = request.json
#         question = data.get("question")

#         if not question:
#             return jsonify({"error": "No question provided"}), 400

#         answer = ask_question(question)

#         return jsonify({
#             "answer": answer,
#             "sources": []
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(port=5000, debug=True)

from flask import Flask, request, jsonify
from ui_layer.query_wrapper import ask_question

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.json
        question = data.get("query") or data.get("question")

        if not question:
            return jsonify({"error": "No question provided"}), 400

        # Call your RAG pipeline
        response = ask_question(question)

        # EXPECTED response from pipeline:
        # {
        #   "answer": "...",
        #   "sections": [...]
        # }

        answer = response.get("answer", "")
        sections = response.get("sections", [])

        return jsonify({
            "answer": answer,
            "sections": sections,
            "citations": [s.get("citation") for s in sections if s.get("citation")]
        })

    except Exception as e:
        print("Query error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
