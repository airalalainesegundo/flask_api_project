from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Item One", "description": "This is item one."},
    {"id": 2, "name": "Item Two", "description": "This is item two."},
]

# Home route (returns JSON)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

# Get all items (renders HTML)
@app.route('/items', methods=['GET'])
def get_items():
    return render_template("items.html", items=items)

# Get specific item by ID (JSON)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Add a new item (Form Submission)
@app.route('/items', methods=['POST'])
def add_item():
    data = request.form
    if not data.get("name") or not data.get("description"):
        return jsonify({"error": "Name and description are required"}), 400
    
    new_item = {
        "id": len(items) + 1,
        "name": data["name"],
        "description": data["description"]
    }
    items.append(new_item)
    return redirect(url_for("get_items"))  # Redirects to item list page

# Run the app
if __name__ == '__main__':
    app.run(debug=True)