# 2310717302005 ธวัชชัย ธีรปกรณ์ Project Web_Dictionary_By_python
Web Application Dictionary Create By Flask Python Freamwork
## Assignment 4: Project
โปรเจคนี้พัฒนาโดย นาย ธวัชชัย ธีรปกรณ์
โปรเจค Web Application โดย ใช้ Flask Python Freamwork

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




    



1. กหด
   
    1.6

4. dvxdv


    1.6

5. 
    1.6




6. 



