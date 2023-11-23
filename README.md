# 2310717302005 ธวัชชัย ธีรปกรณ์ Project Web_Dictionary_By_python
Web Application Dictionary Create By Flask Python Freamwork
## Assignment 4: Project
โปรเจคนี้พัฒนาโดย นาย ธวัชชัย ธีรปกรณ์
โปรเจค Web Application โดย ใช้ Flask Python Freamwork

อธิบายแนวคิดในการสร้างโปรแกรม

Flask Python Freamwork จะใช้หลักการของ (MTV) โดยโปรเจตนี้จะใช้แค่ Templete และ Views 

ซึ่งเป็น web Application 

และพัฒนาให้มี Function Next และ Previous

- Model ==> คือ เป็นส่วนที่รับผิดชอบในการจัดเก็บและจัดการข้อมูล รวมถึงการประมวลผลของแอปพลิเคชัน , Model จะเป็นโค้ดที่เชื่อมโยงกับฐานข้อมูลและจัดการกับข้อมูล.

- Templete ==> คือ จะเขียนเป็น Layout.html ไว้ เพื่อ สืบทอดไปหน้าต่อไปที่ต้องการ ยกตัวอย่างของโปรเจคคือ สร้าง layout.html ไว้เพื่อสืบทอดไปยัง index.html และ pn.html เพื่อสะดวกต่อการแก้ไข

- Views ==> คือ การประมวลผลและจัดการกับข้อมูลที่จะถูกแสดงในหน้าเว็บ, View รับข้อมูลจาก Model และส่งไปยัง Template เพื่อแสดงผล. ยกตัวอย่างใน project คือ app.py เพื่อรับส่งค่าเพื่อ ไปแสดง index.html และ pn.html

โดย โปรเจคจะมี Page ที่สนใจอยู่ 2 หน้า

1. index.html ==> เพื่อแสดงคำศัพท์ มีปุ่มในการ Edit Delete และ Search
2. pn.html ==> เพื่อเอาไว้ใช้ใน Fucntion การค้นหาแบบ Next และ Previous
3. layout.html ==> เพื่อเอาไว้ใช้เป็น layout เพื่อให้ index.html และ pn.html ไว้สืบทอด
4. app.py ==> เป็น python file เพื่อจะเก็บ Code ในการสั่งการในการรับและส่ง ข้อมูลเพื่อไปแสดงหน้า index.htm และ pn.html
5. การตกแต่งจะใช้ bootstrap5 ในการช่วยตกแต่ง
#

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
        
#

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

#

3. จากโจทย์ โปรแกรมเป็นแบบ Console App (Command-Line) หรือ Window App ก็ได้

   - เพิ่มเติม คะแนนเสริม (5 คะแนน)
      
      - หากโปรแกรมเป็น Mobile App หรือ Web App
    
      - ในที่นี้ ได้เลือก พัฒนาเป็น Web App

#

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

 ##     

   - Read (อ่าน): การอ่านหรือดึงข้อมูลจากระบบ เช่น การดึงข้อมูลจากฐานข้อมูลเพื่อแสดงผลบนหน้าเว็บหรือแอปพลิเคชัน.

![1700740924018](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/d9f4ada5-766c-4dfd-b683-44f1b3ae40d5)

![1700740943044](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/45f32376-1bd3-47c6-98c8-e5ddd6f8c95c)

![1700740956604](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/706655a0-da2b-4344-8923-e5e0425daeeb)

![1700740965547](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/fae6275f-8950-406b-85e4-a2bd0b48a148)

![1700740924018](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/d9f4ada5-766c-4dfd-b683-44f1b3ae40d5)



Code app.py เพื่อรับค่าและไปดึงข้อมูลใน Arrays ==> Dictionary โดยใช้ key เพื่อหา จากนั้นส่งค่ากลับไปยัง index.html

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

Code index.html เมื่อใส่ ข้อมูลในช่อง input Search แล้วกดปุ่ม จะขึ้น คำศัพท์ คำแปล ชนิดของข้อมูล เพื่อส่งไปยัง app.py

    <div class="container mt-5">
       <h1 class="mb-4">Dictionary</h1>
       <form action="{{url_for('index')}}" method="GET">
           <div class="form-group">
               <label for="search">Search:</label>
               <input type="text" name="searchN" class="form-control" placeholder="Enter a word..."><br>
               <input type="submit" value="ค้นหาคำศัพท์" class="btn btn-primary">
            
           </div>
       </form>
       <form action="{{url_for('clear_data')}}" method="POST">
           <input type="hidden" name="searchN" value="{{ next_or_previous_word }}">
           <input type="submit" value="ล้างข้อมูล" class="btn btn-warning">
       </form>

##

   - Update (อัปเดต): การปรับปรุงหรือแก้ไขข้อมูลที่มีอยู่ในระบบ เช่น การแก้ไขข้อมูลในฐานข้อมูล.


![1700740829323](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/037aaa67-67d1-4fc0-bd43-48d3c938d7f1)


![1700740876517](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/d8a70ba8-e27c-4118-82b5-87da9491e8b4)


![1700740894996](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/6ebc9fae-d567-4d55-a93d-9e68db78c64e)


![1700740909876](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/381346d9-ba88-4fc2-8803-e486ddfb0fb2)



Code app.py เพื่อรับค่าและไปแก้ไขข้อมูลใน Arrays ==> Dictionary โดยใช้ key เพื่อหา จากนั้นส่งค่ากลับไปยัง index.html

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


Code index.html เมื่อใส่ ข้อมูลในช่อง input edit แล้วกดปุ่ม จะขึ้น คำศัพท์ คำแปล ชนิดของข้อมูล ที่แก้ไข เพื่อส่งไปยัง app.py เพื่อเรียกใช้ฟังก์ชั่น edit_word

   
      <!-- เพิ่ม Modal ที่มี id="editWordModal" -->
      <div class="modal fade" id="editWordModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
              <div class="modal-content">
                  <div class="modal-header">
                      <h5 class="modal-title" id="exampleModalLabel">แก้ไขคำศัพท์</h5>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                      </button>
                  </div>
                  <div class="modal-body">
                      <!-- เพิ่มเนื้อหา Modal ที่นี่ -->
                      <!-- ตัวอย่าง: -->
                      <form action="{{url_for('edit_word')}}" method="GET">
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
                          <button type="submit" class="btn btn-info">บันทึก</button>
                      </form>
                  </div>
              </div>
          </div>
      </div>
      <button class="btn btn-info" data-toggle="modal" data-target="#editWordModal">แก้ไขคำศัพท์</button>









##
     
   - Delete (ลบ): การลบข้อมูลที่มีอยู่จากระบบ เช่น การลบบันทึกที่ไม่ต้องการออกจากฐานข้อมูล.


![1700740744763](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/6ca11925-a531-4ae7-8f0d-780ec8b78f91)

   
![1700740774260](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/b2d78f10-1081-4264-a087-c410374d0f0c)



![1700740799579](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/1fc00d84-d2d9-44db-9c28-aa46b5f04939)



![1700740816516](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/db7fee1a-41ec-49cd-a209-fa6271f829db)




Code app.py เพื่อรับค่าและไปลบข้อมูลใน Arrays ==> Dictionary โดยใช้ key เพื่อหา จากนั้นส่งค่ากลับไปยัง index.html

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
        r   eturn render_template('error.html', message='คำศัพท์ไม่พบใน Dictionary')





Code index.html เมื่อใส่ ข้อมูลในช่อง input Delete หรือกดปุ่มลบจามRow ของคำศัพท์ แล้วกดปุ่ม ข้อมูลจะถูก ส่งไปยัง app.py เพื่อเรียกใช้ delete_word


     <!-- เพิ่ม Modal ที่มี id="DeleteWordModal" -->
      <div class="modal fade" id="DeleteWordModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
              <div class="modal-content">
                  <div class="modal-header">
                      <h5 class="modal-title" id="exampleModalLabel">ลบคำศัพท์</h5>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                      </button>
                  </div>
                  <div class="modal-body">
                      <!-- เพิ่มเนื้อหา Modal ที่นี่ -->
                      <!-- ตัวอย่าง: -->
                      <form action="{{url_for('delete_word')}}" method="GET">
                          <div class="form-group">
                              <label for="englishWord">คำศัพท์ภาษาอังกฤษที่ต้องการลบ:</label>
                              <input type="text" name="englishWord" class="form-control">
                          </div>
                          <button type="submit" class="btn btn-success">ลบคำศัพท์</button>
                      </form>
                  </div>
              </div>
          </div>
      </div>
      <button class="btn btn-danger" data-toggle="modal" data-target="#DeleteWordModal">ลบคำศัพท์</button> 


#

5. จากโจทย์ คะแนนเสริม (10 คะแนน)

หากนักศึกษาเลือกใช้โครงสร้างข้อมูลที่รองรับการค้นหาที่ไม่เป็นแบบ Linear แต่ยังรองรับ Next และ Previous เพื่อดูข้อมูลตัวถัดไปหรือก่อนหน้าได้ด้วย


![1700741062770](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/afb85424-c048-4f1a-86ea-3b937824f475)


![1700741081986](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/4c735447-6d55-4a6d-88b9-8b03e91bedce)



![1700741108163](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/300ce9a5-a1c6-4951-be67-eb23413f49a7)


![1700741125636](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/06da2527-d88b-43c4-ac0e-83485b491102)


![1700741139500](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/a71a921e-1e1b-4803-8671-4439a02cc506)


![1700741166434](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/54b9ba43-7bdd-47d1-8746-0a54cd60d2d9)

![1700741181603](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/ff9d897e-4e33-4d0c-a23c-15902d80e260)


![1700741197531](https://github.com/DionTawatchai/Web_Dictionary_By_python/assets/150526207/d4658f82-fc56-4ab3-881f-d422661b6d36)




Code app.py เพื่อรับค่าและไปดึงข้อมูลใน Arrays ==> Dictionary โดยใช้ key เพื่อหา จากนั้นส่งค่ากลับไปยัง pn.html โดยใช้ ฟังก์ชั่น

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
             

Code pn.html เมื่อใส่ ข้อมูลในช่อง input Search แล้วกดปุ่ม next หรือ previous จะขึ้น คำศัพท์ คำแปล ชนิดของข้อมูล ตามการกดปุ่มหน้าหรือหลังคำที่ใส่ลงไป

      {% extends "layout.html" %}
      {% block content %}
      <div class="container mt-5">
          {% if next_or_previous_word %}
              <h2>English Word: <span id="wordDisplay">{{ Dic[next_or_previous_word][1] }}</span></h2>
              <h2>Thai Word: <span id="wordDisplay">{{ Dic[next_or_previous_word][2] }}</span></h2>
              <h2>Type Word: <span id="wordDisplay">{{ Dic[next_or_previous_word][3] }}</span></h2>
          {% else %}
              <h2>Word: <span id="wordDisplay"></span></h2>
          {% endif %}
    
          <form action="{{ url_for('next_or_previous_word') }}" method="GET">
              <div class="form-group">
                  <input type="text" name="search" class="form-control" placeholder="Enter a word..." value="{{ next_or_previous_word }}">
                  <button type="submit" name="action" value="previous" class="btn btn-primary mt-2">Previous Word</button>
                  <button type="submit" name="action" value="next" class="btn btn-success mt-2">Next Word</button>
              </div>
          </form>

          <form action="{{ url_for('clear_data_pn') }}" method="POST">
              <input type="hidden" name="search" value="{{ next_or_previous_word }}">
              <input type="submit" value="Clear Data" class="btn btn-warning">
          </form>

          <table class="table">
              <thead>
                  <tr>
                      <th>Number</th>
                      <th>English Word</th>
                      <th>Thai Word</th>
                      <th>Type</th>
                  </tr>
              </thead>
           <tbody id="tableBody">
                  {% for key, value_list in Dic.items() %}
                      <tr>
                          <td>{{ value_list[0] }}</td>
                          <td>{{ value_list[1] }}</td>
                          <td>{{ value_list[2] }}</td>
                          <td>{{ value_list[3] }}</td>
                      </tr>
                  {% endfor %}
              </tbody>
          </table>
      </div>
      {% endblock %}










# หากผิดพลาดประการใดขออภัยไว้ ณ ที่นี้ด้วย 2310717302005 ธวัชชัย ธีรปกรณ์ Project Web_Dictionary_By_python



