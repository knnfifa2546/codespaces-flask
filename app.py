from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORSHEADERS'] = 'Content-Type'


books=[
    {"id":1,"title":"Messi1","author":"Messi Dad"},
    {"id":2,"title":"Messi2","author":"Messi Dad"},
    {"id":3,"title":"Messi3","author":"Messi Dad"}
]
@app.route("/")
def Greet():
    return "<p>Welcome to Book Management Systems</p>"

@app.route("/books",methods=["GET"])
def getall_books():
    return jsonify({"books":books})

@app.route("/books/<int:book_id>",methods=["GET"])
def get_book(book_id):
    book =  next(( b for b in books if b["id"]==book_id ),None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}),404

@app.route("/books",methods=["POST"])
def create_book():
    data = request.get_json()
    new_book={
        "id":len(books)+1,
        "title":data["title"],
        "author":data["author"]
    }
    books.append(new_book)
    return jsonify(new_book),201

@app.route("/books/<int:book_id>",methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"]==book_id),None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}),404




@app.route("/books/<int:book_id>",methods=["DELETE"])
def delete_book(book_id):
    book = next((b for b in books if b["id"]==book_id),None)
    if book:
        books.remove(book)
        return jsonify({"message":"Book deleted successfully"}),200
    else:
        return jsonify({"error":"Book not found"}),40

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
