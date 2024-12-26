# Calculating-a-student-s-GPA-with-Python
You can use this code to classify students based on their GPA.


# Code Explanation in English:
Function calculate_gpa:

This function handles receiving grades from the user and calculating the GPA.
Grades are stored in a list, and if a negative grade is entered, an error message is displayed.
Invalid inputs (like text or non-numeric values) are handled, and the user is prompted again.
Finally, if valid grades are entered, the GPA is calculated and returned; otherwise, an appropriate message is displayed to the user.
Function main:

This is the main part of the program and performs the following tasks:
Gets the student's name from the user and ensures it is not empty.
Calls the calculate_gpa function to compute the student's GPA.
Stores student names and their GPAs in a list.
Provides options for the user to continue or exit.
At the end, it prints a summary of all students' GPAs.
Program Execution (__name__ == "__main__"):

If the file is run directly, the main function is executed. This ensures the program does not execute unintentionally if imported as a module.

# Kod Açıklamaları Türkçe:
calculate_gpa Fonksiyonu:

Bu fonksiyon, kullanıcıdan notları alır ve GPA (ortalama) hesaplamasını yapar.
Notlar bir listeye kaydedilir ve negatif bir not girildiğinde hata mesajı gösterilir.
Geçersiz girişler (örneğin metin veya sayı olmayan değerler) yönetilir ve kullanıcıdan tekrar giriş yapması istenir.
Son olarak, eğer geçerli notlar girilmişse GPA hesaplanır ve döndürülür; aksi takdirde uygun bir mesaj gösterilir.
main Fonksiyonu:

Programın ana kısmıdır ve şu görevleri yerine getirir:
Kullanıcıdan öğrencinin adını alır ve adın boş olmadığını kontrol eder.
Öğrencinin GPA'sını hesaplamak için calculate_gpa fonksiyonunu çağırır.
Öğrenci isimlerini ve GPA'larını bir listede saklar.
Kullanıcıya devam etmek veya çıkış yapmak için seçenekler sunar.
Sonunda, tüm öğrencilerin GPA'larının bir özeti yazdırılır.
Programın Çalıştırılması (__name__ == "__main__"):

Eğer dosya doğrudan çalıştırılırsa, main fonksiyonu çağrılır. Bu yapı, programın bir modül olarak kullanılması durumunda istem dışı çalışmasını engeller.

# توضیحات کد به زبان فارسی:
تابع calculate_gpa:

این تابع مسئول دریافت نمرات از کاربر و محاسبه معدل (GPA) است.
نمرات در یک لیست ذخیره می‌شوند و اگر نمره‌ای منفی وارد شود، پیام خطا نمایش داده می‌شود.
اگر ورودی نامعتبر باشد (مانند متن یا نماد غیرعددی)، خطا مدیریت شده و دوباره ورودی درخواست می‌شود.
در نهایت، اگر نمرات معتبر وارد شده باشند، معدل محاسبه و برگردانده می‌شود؛ در غیر این صورت پیام مناسبی به کاربر نشان داده می‌شود.
تابع main:

این تابع، بخش اصلی کد را مدیریت می‌کند و شامل موارد زیر است:
گرفتن نام دانشجو از کاربر و بررسی اینکه نام خالی نباشد.
فراخوانی تابع calculate_gpa برای محاسبه معدل دانشجو.
ذخیره اطلاعات دانشجویان و معدل‌های آنها در یک لیست.
نمایش پیام ادامه یا خروج برای کاربر.
در پایان، یک خلاصه از معدل تمام دانشجویان چاپ می‌شود.
اجرای برنامه (__name__ == "__main__"):

اگر فایل به صورت مستقیم اجرا شود، تابع main اجرا می‌شود. این ساختار تضمین می‌کند که برنامه به صورت ماژول استفاده نشود.
