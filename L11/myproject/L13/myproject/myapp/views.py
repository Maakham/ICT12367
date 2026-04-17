from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person
from django.db.models import Q

# Create your views here.
def index(request):
    # 1. ดึงข้อมูลประชากรทั้งหมดมาก่อน (กรณีที่ยังไม่ได้ค้นหา)
    all_Person = Person.objects.all()

    # 2. รับค่าคำค้นหาจากช่องค้นหา (name="q")
    query = request.GET.get('q')

    # 3. ตรวจสอบว่ามีคำค้นหาถูกพิมพ์ส่งมาหรือไม่
    if query:
        # ถ้ามีคำค้นหา ให้นำ all_Person มากรองข้อมูลเฉพาะคนที่ชื่อตรงกับคำค้นหา
        all_Person = all_Person.filter(Q(name__icontains=query) | Q(age__icontains=query))

    # 4. ส่งข้อมูลไปแสดงผลที่ template (ถ้าไม่มี query ก็จะแสดงทั้งหมดตามข้อ 1)
    return render(request, "index.html", {"all_person": all_Person})

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age = request.POST.get("age")

        # บันทึกข้อมูลลงฐานข้อมูล
        person = Person.objects.create(
            name = name,
            age = age
        )

        # เปลี่ยนเส้นทางไปหน้าแรก
        return redirect("/")
    else:
        # แสดงฟอร์ม
        return render(request, "form.html")

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age = request.POST.get("age")

        # บันทึกข้อมูลลงฐานข้อมูล
        person.name = name
        person.age = age
        person.save()

        # เปลี่ยนเส้นทางไปหน้าแรก
        return redirect("/")
    else:
        # แสดงฟอร์ม
        return render(request, "edit.html", {"person": person})

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")
