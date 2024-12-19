# 3.10.8 64-bit
from flask import Flask, render_template, request, send_file
import pickle
import pdfkit

enc_dict = {
    'Aamchur': 0, 'Agathi leaves': 1, 'Almond': 2, 'Amaranth leaves': 3, 'Amaranth leaves-Red': 4, 'Amaranth seed, Black': 5, 
    'Amaranth spinosus-green': 6, 'Amarnath leaves green': 7, 'Anise seeds': 8, 'Apple ': 9, 'Apricot, dried': 10, 'Arbi': 11, 'Arbi leaves': 12, 
    'Arecanut dried': 13, 'Arugula leaves': 14, 'Asafoetida': 15, 'Ash gourd': 16, 'Avocado': 17, 'Baby corn': 19, 'Baby Potato': 18, 'Bajra': 20, 
    'Bamboo shoot, tender': 21, 'Banana': 22, 'Barley ': 23, 'Basil seeds': 24, 'Basmati Rice': 25, 'Bathua leaves': 26, 'Bay Leaf': 27, 'Beans': 28, 
    'Beef, chops': 29, 'Beet greens': 30, 'Beetroot': 31, 'Bengal gram': 32, 'Bengal gram, dal': 33, 'Betelleaves': 34, 'Bitter gourd': 35, 
    'Black bean': 35, 'Black Cardamom': 38, 'Black cumin (Kalonji)': 36, 'Black Gram': 39, 'Black gram flour ': 37, 'Black pepper': 40, 'Blackberry fruit': 41, 
    'Blackcurrants': 42, 'Bottle gourd': 43, 'Brinjal': 44, 'Broad beans': 45, 'Broccoli': 46, 'Brown Rice': 47, 'Brown sugar': 48, 
    'Brussels sprouts': 49, 'Buckwheat flour': 50, 'Buffalo milk': 50, 'Bulgar wheat': 51, 'Bulgur': 52, 'Butter': 53, 'Cabbage': 54, 
    'Cabbage Chinese': 55, 'Cabbage, green': 56, 'Cabbage-violet': 57, 'Capsicum': 58, 'Cardamom, green': 59, 'Carom seeds': 60, 'Carrot': 61, 
    'Cashewnut': 62, 'Cat fish': 63, 'Catla': 64, 'Cauliflower': 65, 'Cauliflower leaves': 66, 'Cauliflower null': 67, 'Cauliflower, leaves': 68, 
    'Celery stalk': 69, 'Chaat masala': 70, 'Chai masala': 71, 'Chayote': 72, 'Cheese': 73, 'Cherries red': 74, 'Cherry': 75, 'Chia seeds': 76, 
    'Chicken': 77, 'Chicken, breast': 78, 'Chicken, leg, skinless': 79, 'Chicken, liver': 80, 'Chicken, thigh': 81, 'Chickpeas': 82, 'Chilli Flakes': 83, 
    'Chilli sauce': 84, 'Chillies': 85, 'Cho-Cho- Marrow': 86, 'Cinnamon': 87, 'Clam': 88, 'Clove ': 89, 'Cluster beans': 90, 'Coconut': 91, 
    'Coconut dry': 92, 'Coconut fresh': 93, 'Coconut water': 94, 'Colocasia leaves, green': 95, 'Coriander leaves': 96, 'Coriander powder': 97, 
    'Coriander seed': 98, 'Corn flour': 99, 'Corn kernels': 100, 'Cow milk': 101, 'Cow pea, brown': 102, 'Cow pea, white': 103, 'Crab': 104, 
    'Cucumber': 105, 'Cumin Powder': 106, 'Cumin Seeds': 107, 'Curd': 108, 'Curry leaves': 109, 'Custard apple': 110, 'Dates': 111, 'Dates, dry': 112, 
    'Dill leaves': 113, 'Dried tea leaves': 114, 'Drumstick': 115, 'Drumstick leaves': 116, 'Dry Maize': 117, 'Dry Mango powder': 118, 'Dry mint': 119, 
    'Egg': 120, 'Egg white, raw': 121, 'Egg, whole, raw': 122, 'Egg, yolk, raw': 123, 'Fenugreek leaves': 124, 'Fenugreek seeds': 125, 
    'Field bean, black': 126, 'Field bean, brown': 127, 'Field bean, white': 128, 'Fig': 129, 'Finger Millet': 130, 'Flattened Rice': 131, 
    'Flax seeds': 132, 'French Beans': 133, 'Fresh coconut': 134, 'Fresh cream': 135, 'Fresh turmeric': 136, 'Garlic': 137, 'Garlic-kashmir': 138, 
    'Ghee': 139, 'Gingelly seeds': 140, 'Ginger': 141, 'Ginger Garlic Chilli Paste null': 142, 'Ginger Garlic paste': 143, 'Ginger, fresh': 144, 
    'Goat': 145, 'Gooseberry': 146, 'Gram flour': 147, 'Grapes': 148, 'Grated coconut': 149, 'Green Apple': 150, 'Green Cardamom': 151, 'Green chickpeas': 152, 
    'Green chilli': 153, 'Green Gram': 155, 'Green gram dal': 156, 'Green gram spilt': 154, 'Green gram spilt-skinless': 157, 'Green gram, whole': 158, 
    'Green pumpkin': 159, 'Green tamato': 160, 'Green zucchini': 161, 'Ground Cardamom': 162, 'Ground nut': 163, 'Ground nut oil': 164, 'Guava': 165, 
    'Honey': 166, 'Horse gram, whole': 167, 'Hung Crud': 168, 'Idli rice': 169, 'Ivy gourd': 170, 'Jack fruit': 171, 'Jaggery': 172, 'Jaggery cane': 173, 
    'Jalapeno': 174, 'Jowar': 175, 'Khoa': 176, 'Kidney beans': 177, 'Knol-Khol': 178, 'Kovai': 179, 'Ladies finger': 180, 'Lemon juice': 181, 
    'Lentil dal': 182, 'Lettuce': 183, 'Lime': 184, 'Linseeds': 185, 'Litchi': 186, 'Lobster': 187, 'Lotus termeric': 188, 'Mace Blade': 189, 
    'Mackerel': 190, 'Makke ka atta': 191, 'Malabar spinach': 192, 'Mango': 193, 'Matha': 194, 'Milk': 195, 'Milk, whole (Buffalo)': 196, 
    'Milk, whole, cow': 197, 'Mint Chutney': 198, 'Mint Leaves': 199, 'Mint leaves': 200, 'Mushroom': 201, 'Musk melon': 202, 'Mustard leaves': 203, 
    'Mustard oil': 204, 'Mustard Sauce': 207, 'Mustard Seed': 208, 'Nutmeg': 205, 'Oil': 206, 'Okra': 209, 'Olive oil': 210, 'Onion': 211, 'Orange': 212, 
    'Orange Carrot': 213, 'Orange juice': 214, 'Oregano': 215, 'Oyster': 216, 'Palm Fruit': 217, 'Paneer': 218, 'Papaya': 219, 'Parsley': 220, 
    'Parwar': 221, 'Pav bhaji masala': 222, 'Peach': 223, 'Peanuts': 224, 'Pear': 225, 'Peas, dry': 226, 'Peas, fresh': 227, 'Pepper, black': 228, 
    'Pepper, white': 229, 'Pigeon pea ': 230, 'Pigeon peas (Fresh)': 231, 'Pigeon peas split': 232, 'Pine seed': 233, 'Pineapple': 234, 'Pippali': 235, 
    'Pistachio': 236, 'Plantain (stem)': 237, 'Plum': 238, 'Pomegranate': 239, 'Pomfret': 240, 'Poopy seed': 241, 'Pork, chops': 242, 
    'Pork, shoulder': 243, 'Potato': 244, 'Potato brown skin': 245, 'Puffed rice ': 246, 'Pumpkin': 247, 'Quinao': 248, 'Radish': 249, 
    'Radish leaves': 250, 'Radish, white': 251, 'Ragi': 252, 'Ragi flour': 253, 'Raisins, black': 254, 'Rajma, red': 255, 'Raw Mango': 256, 
    'Red Capsicum': 257, 'Red Chilli (Dry)': 258, 'Red gram, dal': 259, 'Red gram, whole': 260, 'Red lentil': 261, 'Red snapper': 262, 
    'Refined flour': 263, 'Rice': 264, 'Rice flour': 265, 'Rice Parboiled': 266, 'Rice Raw milled': 269, 'Ridge gourd': 267, 'Rose petal': 268, 
    'Rosemary leaves': 270, 'Saffron': 271, 'Salmon': 272, 'Salt ': 273, 'Sapota': 274, 'Sardine': 275, 'Semolina': 276, 'Sesame kala': 277, 
    'Sesame white': 278, 'Shark': 279, 'Sheep, chops': 280, 'Sheep, shoulder': 281, 'Silver fish': 282, 'Snake Gourd (long-pale green)': 283, 
    'Soonth powder': 284, 'Soy milk': 285, 'Soya bean, brown': 286, 'Soya sauce': 287, 'Spinach': 288, 'Spring onion': 289, 'Squid': 290, 
    'Star Anise': 290, 'Strawberry': 291, 'Sugar': 292, 'Sugarcane, juice': 293, 'Sunflower seeds': 294, 'Sweet corn': 295, 'Sweet lime': 296, 
    'Sweet potato': 297, 'Tamarind': 298, 'Tamarind chutney': 299, 'Tamato sauce': 300, 'Tapioca': 301, 'Tiger prawns': 302, 'Tinda': 303, 
    'Tindora': 304, 'Tofu': 305, 'Tomato': 306, 'Tuna': 307, 'Turmeric powder': 308, 'Turnip': 309, 'Walnut': 310, 'Water chesnut': 311, 
    'Watermelon': 312, 'Wheat Flour': 313, 'Wheat semolina': 314, 'Wheat Vermicelli': 315, 'Wheat Whole': 316, 'Wood apple': 319, 'Yam': 317, 
    'Yellow capsicum': 318, 'Yellow Zucchini': 320, 'Zucchini, green': 321
    }

model = pickle.load(open("model.pkl", "rb"))  
app = Flask(__name__)        

@app.route("/")
def front_page():
    return render_template("front_page.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    if request.method == "POST":
        ingredients = request.form.getlist("ingredient[]")
        quantities = request.form.getlist("quantity[]")

        total_calories = 0
        items_with_calories = []
        item_names = []
        item_quantities = []

        for ingredient, quantity in zip(ingredients, quantities):
            if quantity:
                quantity = float(quantity)
            else:
                quantity = 0
            if ingredient in enc_dict:  # Check if the ingredient exists in the dictionary
                encoded_ingredient = enc_dict[ingredient]  # Retrieve the encoded value
                cal = round(float(model.predict([[encoded_ingredient, quantity]])[0]), 2)
                total_calories += cal
                items_with_calories.append((ingredient, quantity, cal))
                item_names.append(ingredient)
                item_quantities.append(quantity)

        return render_template("calorie.html", items=items_with_calories, total_calories=total_calories, item_names=item_names, item_quantities=item_quantities)
    else:
        return "<html><body><h1>ERROR!</h1></body></html>"
    
@app.route("/download")
def download():
    html_file = "C:\\Users\\Dhruv Gandhi\\Desktop\\Dhruv Gandhi\\CS Chatbot\\Calorie Tracking\\templates\\calorie.html"  # Replace with the actual path to your HTML file
    pdf_file = "calorie.pdf"  # Name for the generated PDF file
    
    # Specify path to wkhtmltopdf executable
    config = pdfkit.configuration(wkhtmltopdf="/path/to/wkhtmltopdf")
    
    # Convert HTML to PDF
    pdfkit.from_file(html_file, pdf_file, configuration=config)
    
    # Serve the generated PDF file for download
    return send_file(pdf_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)