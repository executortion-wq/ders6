from flask import Flask, request, render_template_string

app = Flask(__name__)

# STATE (sunucuda tutuluyor)
favorites = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Favoriler</title>
</head>
<body>
    <h2>Favoriler Sitesi</h2>
    <p>Burhan İnce</p>

    <form method="POST">
        <input type="text" name="item" placeholder="Favori ekle" required>
        <button type="submit">Ekle</button>
    </form>

    <h3>Favoriler</h3>
    <ul>
        {% for f in favorites %}
            <li>{{ f }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        item = request.form.get("item")
        favorites.append(item)
    return render_template_string(HTML, favorites=favorites)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
