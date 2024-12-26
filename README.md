# Calculating-a-student-s-GPA-with-Python
You can use this code to classify students based on their GPA.

# توضیحات به‌روز شده به زبان فارسی:
مرتب‌سازی دانشجویان بر اساس معدل (GPA):

در بخش نمایش خلاصه معدل‌ها، لیست دانشجویان با استفاده از تابع sorted بر اساس معدل آنها مرتب می‌شود.
از پارامتر key برای مشخص کردن کلید مرتب‌سازی استفاده شده است (در اینجا، gpa).
برای مرتب‌سازی نزولی (بالاترین معدل در ابتدا)، از reverse=True استفاده شده است.
تابع calculate_gpa:

مسئول دریافت نمرات از کاربر و محاسبه معدل است.
نمرات معتبر به یک لیست اضافه شده و در پایان میانگین آنها به‌عنوان معدل برگردانده می‌شود.
تابع main:

نام دانشجو و معدل او را دریافت کرده و اطلاعات دانشجو را در یک لیست ذخیره می‌کند.
پس از پایان ورود اطلاعات، خلاصه‌ای از دانشجویان و معدل‌های آنها به ترتیب نزولی نمایش داده می‌شود.
# Updated Explanation in English:
Sorting Students by GPA:

In the summary section, the list of students is sorted by their GPA using the sorted function.
The key parameter specifies the field to sort by (in this case, gpa).
To sort in descending order (highest GPA first), reverse=True is used.
Function calculate_gpa:

Handles receiving grades from the user and calculating the GPA.
Valid grades are added to a list, and their average is calculated and returned as the GPA.
Function main:

Receives student names and GPAs, storing them in a list.
After input is complete, a summary of students and their GPAs is displayed in descending order.
# Güncellenmiş Açıklamalar Türkçe:
GPA'ye Göre Öğrencilerin Sıralanması:

Özet bölümünde, öğrencilerin listesi sorted fonksiyonu kullanılarak GPA'lerine göre sıralanır.
key parametresi, sıralama yapılacak alanı belirtir (bu durumda gpa).
Azalan düzende sıralamak için (en yüksek GPA ilk sırada), reverse=True kullanılmıştır.
calculate_gpa Fonksiyonu:

Kullanıcıdan notları alır ve GPA hesaplamasını yapar.
Geçerli notlar bir listeye eklenir ve bu notların ortalaması GPA olarak döndürülür.
main Fonksiyonu:

Öğrencilerin adlarını ve GPA'lerini alır, bunları bir listede saklar.
Giriş tamamlandıktan sonra, öğrencilerin ve GPA'lerinin özeti azalan düzende gösterilir.
