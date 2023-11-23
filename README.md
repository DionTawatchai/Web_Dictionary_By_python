# 2310717302005 ธวัชชัย ธีรปกรณ์ Project Web_Dictionary_By_python
Web Application Dictionary Create By Flask Python Freamwork
## Assignment 4: Project
โปรเจคนี้พัฒนาโดย นาย ธวัชชัย ธีรปกรณ์
โปรเจค Web Application โดย ใช้ Flask Python Freamwork

อธิบายแนวคิดในการสร้างโปรแกรม

Flask Python Freamwork จะใช้หลักการของ (MTV) โดยโปรเจตนี้จะใช้แค่ Templete และ Views

- Model ==> คือ เป็นส่วนที่รับผิดชอบในการจัดเก็บและจัดการข้อมูล รวมถึงการประมวลผลของแอปพลิเคชัน , Model จะเป็นโค้ดที่เชื่อมโยงกับฐานข้อมูลและจัดการกับข้อมูล.

- Templete ==> คือ จะเขียนเป็น Layout.html ไว้ เพื่อ สืบทอดไปหน้าต่อไปที่ต้องการ ยกตัวอย่างของโปรเจคคือ สร้าง layout.html ไว้เพื่อสืบทอดไปยัง index.html และ pn.html เพื่อสะดวกต่อการแก้ไข

- Views ==> คือ การประมวลผลและจัดการกับข้อมูลที่จะถูกแสดงในหน้าเว็บ, View รับข้อมูลจาก Model และส่งไปยัง Template เพื่อแสดงผล. ยกตัวอย่างใน project คือ app.py เพื่อรับส่งค่าเพื่อ ไปแสดง index.html และ pn.html

โดย โปรเจคจะมี Page ที่สนใจอยู่ 2 หน้า

1. index.html ==> เพื่อแสดงคำศัพท์ มีปุ่มในการ Edit Delete และ Search
2. pn.html ==> เพื่อเอาไว้ใช้ใน Fucntion การค้นหาแบบ Next และ Previous
3. layout.html ==> เพื่อเอาไว้ใช้เป็น layout เพื่อให้ index.html และ pn.html ไว้สืบทอด
4. app.py ==> เป็น python file เพื่อจะเก็บ Code ในการสั่งการในการรับและส่ง ข้อมูลเพื่อไปแสดงหน้า index.htm และ pn.html

จากโจทย์
1. โปรแกรมพจนานุกรม เก็บคำศัพท์เบื้องต้นอย่างน้อย 20 คำ
   
    1.1 จากภาพ ชื่อไฟล์ app.py คือไฟล์ที่ทำการสั่งการต่างๆ
   

    1.2 โดยจะเก็บคำศัพท์ 20 คำ เป็นรูปแบบ Dictionary
![Number1_Code](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/ed3e75f7-2222-446d-ba0c-99110f15d2b2)


    1.3 จากภาพ เป็นหน้า web page ที่ทำการแสดงคำศัพท์
![Number1_Web](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/4370d422-54b0-4803-b092-48a4a9ed013b)

    1.4 จากภาพ Code ที่แสดงหน้าคำศัพท์ โดยใช้ Flask python Freeamwork สั่งให้ เส้นทาง route ไปยังหน้า Page index.html ผ่าน Fuction def index()
![index_code](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/18b59273-ecd1-40d0-ac12-081c3f1413e7)



    1.5 จากCode แสดงการ ใช้ Lopp for เพื่อเรียกคำศัพท์มาแสดงจาก Dictionary ในหน้า indec.html


Code

    <table class="table">
      <thead>
        <tr>
            <th>Number</th>
            <th>English Word</th>
            <th>Thai Word</th>
            <th>Type</th>
            <th>EDIT and DELETE</th>
        </tr>
        {% for key, value_list in Dic.items() %}
        <tr>
            <th>{{ value_list[0] }}</th>
            <th>{{ value_list[1] }}</th>
            <th>{{ value_list[2] }}</th>
            <th>{{ value_list[3] }}</th>
            <th>
                <div class="btn-group">
                    <button class="btn btn-warning mr-3" data-toggle="modal" data-target="#editWordModal" name="{{ value_list[1] }}">แก้ไขคำศัพท์</button>
                    <form action="{{ url_for('delete_word_inlist') }}" method="post">
                        <input type="hidden" name="englishWord" value="{{ value_list[1] }}">
                        <button type="submit" class="btn btn-danger">ลบคำศัพท์</button>
                    </form>
                </div>
            </th>
        </tr>
        {% endfor %}


2. จากโจทย์ แต่ละคำศัพท์ที่เก็บประกอบไปด้วย คำศัพท์ภาษาอังกฤษ คำแปลภาษาไทย และชนิดของคำ
   
    2.1 เก็บคำศัพท์ 20 คำ เป็นรูปแบบ Dictionary ที่เก็บประกอบไปด้วย คำศัพท์ภาษาอังกฤษ คำแปลภาษาไทย และชนิดของคำ
   
Code

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

3. จากโจทย์ โปรแกรมเป็นแบบ Console App (Command-Line) หรือ Window App ก็ได้

   - เพิ่มเติม คะแนนเสริม (5 คะแนน)
      
      - หากโปรแกรมเป็น Mobile App หรือ Web App
    
      - ในที่นี้ ได้เลือก พัฒนาเป็น Web App

4. จากโจทย์ ใช้โครงสร้างข้อมูลที่เหมาะสมในการรองรับ CRUD operations

    - Create (สร้าง): การสร้างข้อมูลใหม่และเพิ่มข้อมูลลงในระบบ
  

![1700740622427](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/e8be10f1-2131-46d5-9ef7-364d2a3670cd)


![1700740645539](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/9591d537-e346-48a8-abf1-67aa39cc8d13)


![1700740707844](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/5baf32d5-cc12-4812-a688-88dd6156209f)


![1700740724995](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/b07f55ba-a2d6-429f-86c2-4e1561134b0a)


Code app.py เพื่อรับค่าและไปเพิ่มใน Arrays ==> Dictionary

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

Code index.html เมื่อกดปุ่มเพิ่มคำศัพท์จะมี pop up เป็น Modal เพื่อเป็น Form ให้กรอก และ เพื่อส่งค่าไปยัง app.py เพื่อเรียกใช้ฟังก์ชั่น add_word

      <!-- เพิ่ม Modal ที่มี id="addWordModal" -->
      <div class="modal fade" id="addWordModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
              <div class="modal-content">
                  <div class="modal-header">
                      <h5 class="modal-title" id="exampleModalLabel">เพิ่มคำศัพท์</h5>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                      </button>
                  </div>
                  <div class="modal-body">
                      <form action="{{url_for('add_word')}}" method="GET">
                          <div class="form-group">
                              <label for="number">ลำดับ:</label>
                              <input type="text" name="number" class="form-control">
                          </div>
                          <div class="form-group">
                              <label for="englishWord">คำศัพท์ภาษาอังกฤษ:</label>
                              <input type="text" name="englishWord" class="form-control">
                          </div>
                        <div class="form-group">
                              <label for="thaiWord">คำศัพท์ภาษาไทย:</label>
                              <input type="text" name="thaiWord" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="wordType">ประเภท:</label>
                        <input type="text" name="wordType" class="form-control">
                    </div>
                    <button type="submit" class="btn btn-success">บันทึก</button>
                      </form>
                  </div>
              </div>
          </div>
      </div>

<button class="btn btn-success" data-toggle="modal" data-target="#addWordModal">เพิ่มคำศัพท์</button>





         







5. 
    1.6




6. 



