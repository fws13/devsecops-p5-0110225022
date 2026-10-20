from flask import Flask, jsonify, request
from app.services import NoteService
from app.validators import validate_note

service = NoteService()


def create_app():
    app = Flask(__name__)

    @app.route("/notes", methods=["GET"])
    def list_notes():
        return jsonify([n.to_dict() for n in service.list_all()])

    @app.route("/notes", methods=["POST"])
    def add_note():
        data = request.get_json(silent=True)
        valid, error = validate_note(data)
        if not valid:
            return jsonify({"error": error}), 400
        note = service.create(data["title"].strip(), data["content"].strip())
        return jsonify(note.to_dict()), 201

    @app.route("/notes/<int:note_id>", methods=["GET"])
    def get_note(note_id):
        note = service.get(note_id)
        if note is None:
            return jsonify({"error": "Catatan tidak ditemukan"}), 404
        return jsonify(note.to_dict())

    @app.route("/notes/<int:note_id>", methods=["DELETE"])
    def delete_note(note_id):
        if service.delete(note_id):
            return jsonify({"message": "Dihapus"}), 200
        return jsonify({"error": "Catatan tidak ditemukan"}), 404

    @app.route("/summaries", methods=["GET"])
    def summaries():
        return jsonify(service.summaries())

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000)
