# 3.10.8 64-bit
from flask import Flask, render_template, request
import pickle

enc_dict = {
    "Almonds": 0, "Amaranth leaves": 1, "Amaranth seed, Black": 2, "Anise seeds": 3, "Apple": 4, "Apricot, dried": 5, 
    "Arecanut dried": 6, "Asafoetida": 7, "Ash gourd": 8, "Avocado": 9, "Bajra": 10, "Bamboo shoot, tender": 11, "Banana": 12, 
    "Barley": 13, "Basil seeds": 14, "Beef, chops": 15, "Beet greens": 16, "Beetroot": 17, "Bengal gram, dal": 18, "Bengal gram, whole": 19, 
    "Bitter gourd": 20, "Black cumin (Kalonji)": 21, "Black gram, whole": 22, "Blackberry fruit": 23, "Blackcurrants": 24, "Bottle gourd": 25, 
    "Brinjal": 26, "Broad beans": 27, "Brown Rice": 28, "Brussels sprouts": 29, "Bulgar wheat": 30, "Butter": 31, "Cabbage Chinese": 32, 
    "Cabbage, green": 33, "Capsicum": 34, "Cardamom, green": 35, "Carrot": 36, "Cashew nut": 37, "Cat fish": 38, "Catla": 39, "Cauliflower": 40, 
    "Cauliflower, leaves": 41, "Celery stalk": 42, "Cheese": 43, "Cherries red": 44, "Chia seeds": 45, "Chicken, breast,": 46, "Chicken, leg, skinless": 47, 
    "Chicken, liver": 48, "Chicken, thigh,": 49, "Cho-Cho- Marrow": 50, "Clam": 51, "Cloves": 52, "Cluster beans": 53, "Coconut dry": 54, "Coconut fresh": 55, 
    "Coconut water": 56, "Colocasia leaves, green": 57, "Coriander seeds": 58, "Cow pea, brown": 59, "Cow pea, white": 60, "Crab": 61, "Cucumber": 62, "Cumin seeds": 63, 
    "Curry leaves": 64, "Custard apple": 65, "Dates, dry": 66, "Drumstick leaves": 67, "Egg white, raw": 68, "Egg, whole, raw": 69, "Egg, yolk, raw": 70, "Fenugreek leaves": 71, 
    "Fenugreek seeds": 72, "Fig": 73, "Flax seeds": 74, "French beans": 75, "Garlic": 76, "Ghee": 77, "Gingelly seeds": 78, "Ginger, fresh": 79, "Goat": 80, "Grapes": 81, 
    "Green chillies": 82, "Green gram dal": 83, "Green gram, whole": 84, "Ground nut": 85, "Guava": 86, "Horse gram, whole": 87, "Jack fruit": 88, "Jaggery cane": 89, "Jowar": 90,
    "Khoa": 91, "Knol-Khol": 92, "Kovai": 93, "Ladies finger": 94, "Lentil dal": 95, "Lettuce": 96, "Linseeds": 97, "Litchi": 98, "Lobster": 99, 
    "Mackerel": 100, "Mango": 101, "Matha": 102, "Milk, whole (Buffalo)": 103, "Milk, whole, cow": 104, "Mint leaves": 105, "Musk melon": 106, 
    "Mustard leaves": 107, "Nutmeg": 108, "Oil": 109, "Onion": 110, "Orange": 111, "Oyster": 112, "Paneer": 113, "Papaya": 114, "Parsley": 115, 
    "Parwar": 116, "Peach": 117, "Pear": 118, "Peas, dry": 119, "Peas,fresh": 120, "Pepper, black": 121, "Pine seed": 122, "Pineapple": 123, 
    "Pistachio nuts": 124, "Plantain stem": 125, "Plum": 126, "Pomegranate": 127, "Pomfret": 128, "Poppy seeds": 129, "Pork, chops": 130, "Pork, shoulder": 131, 
    "Potato brown": 132, "Pumpkin": 133, "Quinoa": 134, "Radish leaves": 135, "Radish,white": 136, "Ragi": 137, "Raisins, black": 138, "Rajma, red": 139, 
    "Red chillies": 140, "Red gram, dal": 141, "Red gram, whole": 142, "Refined flour": 143, "Rice flakes": 146, "Rice Parboiled": 144, "Rice Raw milled": 145, 
    "Ridge gourd": 147, "Salmon": 148, "Sapota": 149, "Sardine": 150, "Shark": 151, "Sheep, chops": 152, "Sheep, shoulder": 153, "Silver fish": 154, "Snake gourd": 155, 
    "Soy milk": 156, "Soya bean, brown": 157, "Spinach": 158, "Squid": 159, "Strawberry": 160, "Sugarcane, juice": 161, "Sunflower seeds": 162, "Sweet lime": 163, 
    "Sweet potato (brown)": 164, "Tapioca": 165, "Tiger prawns": 166, "Tofu": 167, "Tomato": 168, "Tuna": 169, "Turmeric powder": 170, "Walnut": 171, "Watermelon": 172, 
    "Wheat flour": 173, "Wheat semolina": 174, "Wheat vermicelli": 175, "Wheat whole": 176, "Wood apple": 177, "Yam": 178, "Zucchini, green": 179
    }

model = pickle.load(open("model.pkl", "rb"))
app = Flask(__name__)

@app.route("/")
def front_page():
    return render_template("front_page.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    if request.method == "POST":
        ingredients = request.form.getlist("ingredient[]")
        quantities = request.form.getlist("quantity[]")

        calorie = 0
        predicted_calories = []
        for encoded_ingredient, quantity in zip(ingredients, quantities):
            if quantity:
                quantity = float(quantity)
            else:
                quantity = 0
            if encoded_ingredient:  # Check if ingredient is not empty
                pre_cal = model.predict([[enc_dict.get(encoded_ingredient), quantity]])[0]
                predicted_calories.append(pre_cal)
                calorie += pre_cal
            else:
                predicted_calories.append(0)
        return render_template("calorie.html", calorie=calorie)
    else:
        return "<html><body><h1>ERROR!</h1></body></html>"


if __name__ == "__main__":
    app.run(debug=True)