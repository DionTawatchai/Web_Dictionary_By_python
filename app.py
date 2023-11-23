# Python (Flask)
from xml.dom import Node
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# ตัวอย่างข้อมูลใน array
dictionary = {
    "apple": ["1", "apple", "แอปเปิล", "noun"],
    "banana": ["2", "banana", "กล้วย", "noun"],
    "cat": ["3", "cat", "แมว", "noun"],
    "egg": ["4", "dance", "	เต้นรำ", "verb"],
    "dog": ["5", "eraser", "ยางลบ", "noun"],
    "flower":["6","flower","ดอกไม้","noun"],
    "good":["7","good","ดี","adjective"],
    "hair":["8","hair","ผม","noun"],
    "ice":["9","ice","น้ำแข็ง","noun"],
    "jar":["10","jar","โอ่ง","noun"],
    "king":["11","king","พระราชา","noun"],
    "listen":["12","listen","	ฟัง","verb"],
    "milk":["13","milk","นม","noun"],
    "name":["14","name","ชื่อ","noun"],
    "open":["15","open","เปิด","verb"],
    "park":["16","park","สวนสาธารณะ","noun"],
    "queen":["17","queen","ราชินี","noun"],
    "ring":["18","ring","แหวน","noun"],
    "salad":["19","salad","สลัดผัก","noun"],
    "tree":["20","tree","ต้นไม้","noun"]
}
dic1 = dictionary

app.secret_key = 'your_secret_key'  # ใส่คีย์ที่คุณเลือก

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        search_term = request.args.get("searchN")

        if search_term in dictionary:
            keys = list(dictionary.keys())
            current_index = keys.index(search_term.lower())

            # เก็บค่า index เพื่อให้ใช้ใน next และ previous
            session['current_index'] = current_index

            return render_template('index.html', number=current_index, name=search_term, Dic=dictionary, data=search_term)
        else:
            return render_template('index.html', name='', Dic=dictionary, data='')
    else:
        return render_template('index.html', name='', Dic=dictionary, data='')


@app.route('/clear_data_pn', methods=['POST'])
def clear_data_pn():
    # เพิ่มโค้ดที่จะล้างข้อมูลที่เกี่ยวกับการค้นหา
    session.pop('current_index', None)  # ลบค่า current_index ใน session

    # เช็คว่ามี parameter 'search' มั้ย ถ้ามีให้ล้างค่าใน input ด้วย
    search_term = request.form.get('search', '')
    if search_term:
        return redirect(url_for('pn', search=''))
    else:
        return redirect(url_for('pn'))
    
@app.route('/clear_data', methods=['POST'])
def clear_data():
    # เพิ่มโค้ดที่จะล้างข้อมูลที่เกี่ยวกับการค้นหา
    session.pop('current_index', None)  # ลบค่า current_index ใน session

    # เช็คว่ามี parameter 'search' มั้ย ถ้ามีให้ล้างค่าใน input ด้วย
    search_term = request.form.get('searchN', '')
    if search_term:
        return redirect(url_for('index', searchN=''))
    else:
        return redirect(url_for('index'))

@app.route('/add_word', methods=['GET', 'POST'])
def add_word():
    KB_KEY_number = request.args.get('number')
    KB_KEY_Vocub = request.args.get('englishWord')
    KB_Thai_word = request.args.get('thaiWord')
    KB_Type = request.args.get('wordType')
    key = KB_KEY_Vocub.lower()  # ทำให้เป็น lowercase เพื่อป้องกันปัญหา case-sensitive
    value_list = [KB_KEY_number, KB_KEY_Vocub, KB_Thai_word, KB_Type]
    dictionary[key] = value_list
    return redirect(url_for('index'))


@app.route('/delete_word', methods=['GET', 'POST'])
def delete_word():
    KB_KEY_Vocub = request.args.get('englishWord')

    # ตรวจสอบว่าคำศัพท์อยู่ใน Dictionary หรือไม่
    if KB_KEY_Vocub.lower() in dictionary:
        del dictionary[KB_KEY_Vocub.lower()]
        print("Deleted:", KB_KEY_Vocub)
    else:
        print("Key not found in Dictionary")

    return redirect(url_for('index'))


@app.route('/delete_word_inlist', methods=['GET', 'POST'])
def delete_word_inlist():
    KB_KEY_Vocub = request.form.get('englishWord', '')

    # ตรวจสอบว่าคำศัพท์อยู่ใน Dictionary หรือไม่
    if KB_KEY_Vocub.lower() in dictionary:
        del dictionary[KB_KEY_Vocub.lower()]
        print("Deleted:", KB_KEY_Vocub)
        return redirect(url_for('index'))
    else:
        print("Key not found in Dictionary")
        return render_template('error.html', message='คำศัพท์ไม่พบใน Dictionary')


@app.route('/edit_word', methods=['GET', 'POST'])
def edit_word():
    KB_KEY_number = request.args.get('number')
    KB_KEY_Vocub = request.args.get('englishWord')
    KB_Thai_word = request.args.get('thaiWord')
    KB_Type = request.args.get('wordType')
    key = KB_KEY_Vocub.lower()
    value_list = [KB_KEY_number, KB_KEY_Vocub, KB_Thai_word, KB_Type]
    dictionary[key] = value_list
    return redirect(url_for('index'))


@app.route('/edit_word_inlist', methods=['GET', 'POST'])
def edit_word_inlist():
    KB_KEY_number = request.args.get('number')
    KB_KEY_Vocub = request.args.get('englishWord')
    KB_Thai_word = request.args.get('thaiWord')
    KB_Type = request.args.get('wordType')
    key = KB_KEY_Vocub.lower()
    value_list = [KB_KEY_number, KB_KEY_Vocub, KB_Thai_word, KB_Type]
    dictionary[key] = value_list
    return redirect(url_for('index'))


@app.route('/next_or_previous_word', methods=['GET', 'POST'])
def next_or_previous_word():
    search_term = request.args.get("search")
    action = request.args.get("action")

    if search_term:
        keys = list(dictionary.keys())
        current_index = keys.index(search_term.lower())

        if action == "next" and current_index < len(keys) - 1:
            next_index = current_index + 1
            next_word = keys[next_index]
            session['current_index'] = next_index
            return render_template('pn.html', Dic=dictionary, next_or_previous_word=next_word)

        elif action == "previous" and current_index > 0:
            previous_index = current_index - 1
            previous_word = keys[previous_index]
            session['current_index'] = previous_index
            return render_template('pn.html', Dic=dictionary, next_or_previous_word=previous_word)

    return render_template('pn.html', Dic=dictionary, next_or_previous_word=search_term)

@app.route('/pn')
def pn():
    return render_template("pn.html", Dic=dictionary, next_word=None)


@app.route('/profile')
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)
