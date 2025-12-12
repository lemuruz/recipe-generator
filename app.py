

from flask import Flask, render_template, request
import ollama

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    recipe = None

    if request.method == "POST":

        ingredients = request.form["ingredients"]

        prompt = f"""
        Now you are a professional chef. Create a recipe using these ingredients: {ingredients}.
        Then tell me the 
        
        1.required equipment
        2.ingredients list measured in grams or kg
        3.step-by-step instruction
        4.estimated cooking time
        """

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}],
        )

        recipe = response["message"]["content"]
        # print(recipe)
    return render_template("index.html",recipe=recipe)
    
if __name__ == "__main__":
    app.run(debug=True)