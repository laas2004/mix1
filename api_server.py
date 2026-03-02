# from flask import Flask, request, jsonify
# import os

# from ui_layer.query_wrapper import ask_question
# from ui_layer.ingest_wrapper import ingest_pdf
# from ui_layer.auth import check_admin_password

# app = Flask(__name__)

# UPLOAD_FOLDER = "data/pdfs"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # =========================
# # QUERY ENDPOINT
# # =========================
# @app.route("/query", methods=["POST"])
# def query():
#     try:
#         data = request.json
#         question = data.get("query") or data.get("question")

#         if not question:
#             return jsonify({"error": "No question provided"}), 400

#         raw_output = ask_question(question)

#         # If wrapper returns plain text
#         if isinstance(raw_output, str):
#             return jsonify({
#                 "answer": raw_output,
#                 "sections": [],
#                 "citations": []
#             })

#         # If wrapper returns structured
#         return jsonify({
#             "answer": raw_output.get("answer", ""),
#             "sections": raw_output.get("sections", []),
#             "citations": raw_output.get("citations", [])
#         })

#     except Exception as e:
#         print("Query error:", str(e))
#         return jsonify({"error": str(e)}), 500


# # =========================
# # ADMIN UPLOAD
# # =========================
# @app.route("/api/admin/upload", methods=["POST"])
# def upload():
#     try:
#         files = request.files.getlist("file")

#         if not files:
#             return jsonify({"success": False, "error": "No files uploaded"}), 400

#         saved_files = []

#         for file in files:
#             path = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(path)
#             saved_files.append(file.filename)

#         return jsonify({
#             "success": True,
#             "files": saved_files
#         })

#     except Exception as e:
#         return jsonify({"success": False, "error": str(e)}), 500


# # =========================
# # ADMIN INGEST
# # =========================
# # new addn
# from datetime import datetime

# @app.route('/api/admin/ingest', methods=['POST'])
# def ingest_documents():
#     global pipeline_status

#     try:
#         pipeline_status["running"] = True
#         pipeline_status["message"] = "Processing documents..."

#         from ui_layer.ingest_wrapper import ingest_pdf

#         output = ingest_pdf()

#         pipeline_status["running"] = False
#         pipeline_status["last_run"] = datetime.now().isoformat()
#         pipeline_status["message"] = "Ingestion completed"

#         return {
#             "success": True,
#             "logs": output
#         }

#     except Exception as e:
#         pipeline_status["running"] = False
#         pipeline_status["message"] = "Failed"

#         import traceback
#         print(traceback.format_exc())

#         return {"success": False, "error": str(e)}, 500
# @app.route('/api/pipeline/status', methods=['GET'])
# def pipeline_status_route():
#     return pipeline_status

# # @app.route('/api/admin/ingest', methods=['POST'])
# # def ingest_documents():
# #     try:
# #         from ui_layer.ingest_wrapper import ingest_pdf

# #         output = ingest_pdf()

# #         return {
# #             "success": True,
# #             "message": "Ingestion completed",
# #             "logs": output
# #         }

# #     except Exception as e:
# #         import traceback
# #         print(traceback.format_exc())

# #         return {
# #             "success": False,
# #             "error": str(e)
# #         }, 500
#         # new addn
# pipeline_status = {
#     "running": False,
#     "last_run": None,
#     "message": "Idle"
# }



# if __name__ == "__main__":
#     app.run(port=5000, debug=True)






# trust this 
# from flask import Flask, request, jsonify
# from datetime import datetime
# import threading
# import os

# from ui_layer.ingest_wrapper import ingest_pdf
# from ui_layer.query_wrapper import ask_question  # <--- important

# app = Flask(__name__)

# UPLOAD_FOLDER = "data/pdfs"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# pipeline_status = {
#     "running": False,
#     "last_run": None,
#     "message": "Idle"
# }

# # =========================
# # QUERY ENDPOINT
# # =========================
# @app.route("/query", methods=["POST"])
# def query():
#     try:
#         data = request.json
#         question = data.get("query") or data.get("question")

#         if not question:
#             return jsonify({"error": "No question provided"}), 400

#         raw_output = ask_question(question)

#         # If wrapper returns plain text
#         if isinstance(raw_output, str):
#             return jsonify({
#                 "answer": raw_output,
#                 "sections": [],
#                 "citations": []
#             })

#         # If wrapper returns structured
#         return jsonify({
#             "answer": raw_output.get("answer", ""),
#             "sections": raw_output.get("sections", []),
#             "citations": raw_output.get("citations", [])
#         })

#     except Exception as e:
#         print("Query error:", str(e))
#         return jsonify({"error": str(e)}), 500
# # =========================
# # ADMIN UPLOAD 
# # =========================
# @app.route("/api/admin/upload", methods=["POST"])
# def upload():
#     try:
#         files = request.files.getlist("file")
#         if not files:
#             return jsonify({"success": False, "error": "No files uploaded"}), 400
#         saved_files = []
#         for file in files:
#             path = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(path)
#             saved_files.append(file.filename)
#         return jsonify({
#             "success": True,
#             "files": saved_files
#         })
#     except Exception as e:
#         return jsonify({"success": False, "error": str(e)}), 500


# # =========================
# # Admin ingest endpoint
# # =========================
# # new addn
# from datetime import datetime

# @app.route('/api/admin/ingest', methods=['POST'])
# def ingest_documents():
#     global pipeline_status
#     try:
#         pipeline_status["running"] = True
#         pipeline_status["message"] = "Processing documents..."

#         from ui_layer.ingest_wrapper import ingest_pdf
#         output = ingest_pdf()

#         pipeline_status["running"] = False
#         pipeline_status["last_run"] = datetime.now().isoformat()
#         pipeline_status["message"] = "Ingestion completed"

#         return {
#             "success": True,
#             "logs": output
#         }

#     except Exception as e:
#         pipeline_status["running"] = False
#         pipeline_status["message"] = "Failed"

#         import traceback
#         print(traceback.format_exc())

#         return {"success": False, "error": str(e)}, 500


# @app.route('/api/pipeline/status', methods=['GET'])
# def pipeline_status_route():
#     return pipeline_status


# # @app.route('/api/admin/ingest', methods=['POST'])
# # def ingest_documents():
# #     try:
# #         from ui_layer.ingest_wrapper import ingest_pdf
# #         output = ingest_pdf()
# #         return {
# #             "success": True,
# #             "message": "Ingestion completed",
# #             "logs": output
# #         }
# #     except Exception as e:
# #         import traceback
# #         print(traceback.format_exc())
# #         return {
# #             "success": False,
# #             "error": str(e)
# #         }, 500


# # new addn
# pipeline_status = {
#     "running": False,
#     "last_run": None,
#     "message": "Idle"
# }

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)


# trust the below code to work cuz it does
# from flask import Flask, request, jsonify
# from datetime import datetime
# import threading
# import os

# from ui_layer.ingest_wrapper import ingest_pdf
# from ui_layer.query_wrapper import ask_question

# app = Flask(__name__)

# UPLOAD_FOLDER = "data/pdfs"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # ------------------------
# # Pipeline status tracker
# # ------------------------
# pipeline_status = {
#     "running": False,
#     "last_run": None,
#     "message": "Idle"
# }

# # =========================
# # QUERY ENDPOINT
# # =========================
# @app.route("/query", methods=["POST"])
# def query():
#     try:
#         data = request.json
#         question = data.get("query") or data.get("question")

#         if not question:
#             return jsonify({"error": "No question provided"}), 400

#         raw_output = ask_question(question)

#         # If wrapper returns plain text
#         if isinstance(raw_output, str):
#             return jsonify({
#                 "answer": raw_output,
#                 "sections": [],
#                 "citations": []
#             })

#         # If wrapper returns structured
#         return jsonify({
#             "answer": raw_output.get("answer", ""),
#             "sections": raw_output.get("sections", []),
#             "citations": raw_output.get("citations", [])
#         })

#     except Exception as e:
#         print("Query error:", str(e))
#         return jsonify({"error": str(e)}), 500

# # =========================
# # ADMIN UPLOAD ENDPOINT
# # =========================
# @app.route("/api/admin/upload", methods=["POST"])
# def upload():
#     try:
#         files = request.files.getlist("file")
#         if not files:
#             return jsonify({"success": False, "error": "No files uploaded"}), 400

#         saved_files = []
#         for file in files:
#             path = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(path)
#             saved_files.append(file.filename)

#         return jsonify({
#             "success": True,
#             "files": saved_files,
#             "message": f"Uploaded: {', '.join(saved_files)}"
#         })
#     except Exception as e:
#         return jsonify({"success": False, "error": str(e)}), 500

# # =========================
# # ADMIN INGEST ENDPOINT (ASYNC)
# # =========================
# @app.route('/api/admin/ingest', methods=['POST'])
# def ingest_documents_async():
#     global pipeline_status

#     def run_ingest():
#         try:
#             pipeline_status["running"] = True
#             pipeline_status["message"] = "Processing documents..."

#             # Run actual ingestion
#             output = ingest_pdf()

#             pipeline_status["message"] = "Ingestion completed"
#         except Exception as e:
#             pipeline_status["message"] = f"Failed: {str(e)}"
#         finally:
#             pipeline_status["running"] = False
#             pipeline_status["last_run"] = datetime.now().isoformat()

#     # Start ingestion in a separate thread
#     threading.Thread(target=run_ingest).start()

#     # Immediately return to UI
#     return {"success": True, "message": "Ingestion started"}

# # =========================
# # PIPELINE STATUS ENDPOINT
# # =========================
# @app.route('/api/pipeline/status', methods=['GET'])
# def pipeline_status_route():
#     return pipeline_status

# # =========================
# # MAIN
# # =========================
# if __name__ == "__main__":
#     # threaded=True allows status GET requests while ingestion runs
#     app.run(port=5000, debug=True, threaded=True)



from flask import Flask, request, jsonify, send_file
from datetime import datetime
import threading
import os
import tempfile

from flask_cors import CORS

from ui_layer.ingest_wrapper import ingest_pdf
from ui_layer.query_wrapper import ask_question

from faster_whisper import WhisperModel
from gtts import gTTS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "data/pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ------------------------
# Pipeline status tracker
# ------------------------
pipeline_status = {
    "running": False,
    "last_run": None,
    "message": "Idle",
    "logs": [],
    "current_file": None
}

# =========================
# LOAD WHISPER MODEL
# =========================
print("Loading Whisper model...")
whisper_model = WhisperModel("base", compute_type="int8")
print("Whisper loaded")

# =========================
# QUERY
# =========================
@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.json
        question = data.get("query") or data.get("question")

        if not question:
            return jsonify({"error": "No question provided"}), 400

        raw_output = ask_question(question)

        if isinstance(raw_output, str):
            return jsonify({
                "answer": raw_output,
                "sections": [],
                "citations": []
            })

        return jsonify({
            "answer": raw_output.get("answer", ""),
            "sections": raw_output.get("sections", []),
            "citations": raw_output.get("citations", [])
        })

    except Exception as e:
        print("Query error:", str(e))
        return jsonify({"error": str(e)}), 500

# =========================
# SPEECH TO TEXT
# =========================
@app.route("/api/speech-to-text", methods=["POST"])
def speech_to_text():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "No audio file"}), 400

        audio_file = request.files["audio"]

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            audio_file.save(tmp.name)
            segments, _ = whisper_model.transcribe(tmp.name)

        text = " ".join([seg.text for seg in segments])
        os.remove(tmp.name)

        return jsonify({"text": text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =========================
# TEXT TO SPEECH
# =========================
@app.route("/api/text-to-speech", methods=["POST"])
def text_to_speech():
    try:
        data = request.json
        text = data.get("text")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        tts = gTTS(text=text)

        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(tmp_file.name)

        return send_file(tmp_file.name, mimetype="audio/mpeg")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =========================
# ADMIN UPLOAD
# =========================
@app.route("/api/admin/upload", methods=["POST"])
def upload():
    try:
        files = request.files.getlist("file")
        if not files:
            return jsonify({"success": False, "error": "No files uploaded"}), 400

        saved_files = []
        for file in files:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            saved_files.append(file.filename)

        pipeline_status["logs"].append(f"Uploaded {len(saved_files)} file(s)")

        return jsonify({
            "success": True,
            "files": saved_files,
            "message": f"Uploaded: {', '.join(saved_files)}"
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# =========================
# INGEST
# =========================
@app.route('/api/admin/ingest', methods=['POST'])
def ingest_documents_async():
    global pipeline_status

    def run_ingest():
        try:
            pipeline_status["running"] = True
            pipeline_status["logs"].append("Starting ingestion...")
            pipeline_status["message"] = "Processing documents"

            ingest_pdf()

            pipeline_status["logs"].append("Ingestion completed successfully")
            pipeline_status["message"] = "Completed"

        except Exception as e:
            pipeline_status["logs"].append(f"Failed: {str(e)}")
            pipeline_status["message"] = "Failed"

        finally:
            pipeline_status["running"] = False
            pipeline_status["last_run"] = datetime.now().isoformat()

    threading.Thread(target=run_ingest).start()

    return {"success": True, "message": "Ingestion started"}

# =========================
# STATUS
# =========================
@app.route('/api/pipeline/status', methods=['GET'])
def pipeline_status_route():
    return jsonify(pipeline_status)

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app.run(port=5000, debug=False, threaded=True)