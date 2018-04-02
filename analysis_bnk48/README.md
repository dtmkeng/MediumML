# BNK48 analytic
สำหรับคนที่จะลองไปรันเองก็เปลี่ยนไฟล์ growth.json กับ reaction.json โดยไปโหลดข้อมูลได้จาก
https://www.iqueuez.com/app/bnk48/facebook/1/2018-3-25/2018-4-1/total_fans/line_chart
ดึงไฟล์ได้จากตัว network ที่รับเข้ามา 
จากนั้นก็ทำการรันไฟล์ evaluate.js ก่อน โดยแก้ date ใน evaluate ให้ตรงกับที่โหลดมาทำการแก้ตัวแปร arg ให้เป็นทำ reaction และ growth 
ในส่วนของ analy.py ก็จะเรียกไฟล์ growth_Cleaned.json กับ reaction_Cleaned.json output ออกมาเป็นค่า coefficiency หรือจะแก้โมเดลยังไงก็แล้วแต่
