print("=== Kaloria.kz — жеке тамақ есебі жүйесі ===")

kunlik_norma = 2200.0
tamak_atauy = input("Тамақтың атауы: ").strip()
energiya = float(input("Оның калория мөлшері (ккал): "))

qaldyk = kunlik_norma - energiya

print(f"{tamak_atauy} тағамы: {energiya:.1f} ккал")
print(f"Күндік лимит: {kunlik_norma:.1f} ккал | Қалғаны: {qaldyk:.1f} ккал")

if energiya >= 600:
    print("⚠️ Бұл тағам жоғары калориялы!")
elif energiya < 250:
    print("✅ Бұл тағам жеңіл және пайдалы.")
else:
    print("ℹ️ Орташа калория мөлшері.")

print("\n=== Ас тізімі мен деректер ===")
menu_list = ["сорпа", "ботқа", "жұмыртқа", "ботқа", "салат"]

unik_menu = set(menu_list)

tamaktanu_kuni = ("таңғы ас", "түскі ас", "кешкі ас")

print("Толық тізім:", menu_list)
print("Қайталанусыз:", unik_menu)
print("Тамақтану кезеңдері:", tamaktanu_kuni)

print("\n=== Іздеу және мәтінмен жұмыс ===")

izdeu = input("Қай тағамды тексереміз? ").lower()
bar_tamaktar = [t.lower() for t in menu_list]

if izdeu in bar_tamaktar:
    print(f"✅ '{izdeu.capitalize()}' мәзірде бар.")
else:
    print(f"❌ '{izdeu.capitalize()}' мәзірде табылмады.")

spisok = ", ".join(menu_list)
spisok = spisok.replace("ботқа", "сүзбелі ботқа")
print("Жаңартылған мәзір:", spisok)

print("\n=== Kaloria.kz мәзір жүйесі ===")

kaloria_db = {
    "сорпа": 230,
    "ботқа": 310,
    "салат": 150
}

for at, kcal in kaloria_db.items():
    print(f"{at.capitalize()} → {kcal} ккал")

while True:
    print("\n🔹 Негізгі мәзір:")
    print("1 — Тағам қосу")
    print("2 — Бар мәзірді көру")
    print("3 — Жалпы калорияны санау")
    print("4 — Ең калориялы тағамды табу")
    print("0 — Шығу")

    tauda = input("Таңдау енгізіңіз: ").strip()

    if tauda == "1":
        at = input("Жаңа тағамның атауы: ").lower()
        kcal = float(input("Калория мөлшері: "))
        kaloria_db[at] = kcal
        print(f"✅ '{at.capitalize()}' қосылды ({kcal} ккал).")

    elif tauda == "2":
        print("\nҚазіргі мәзір:")
        for a, k in kaloria_db.items():
            print(f"- {a.capitalize()} : {k} ккал")

    elif tauda == "3":
        barlygy = sum(kaloria_db.values())
        print(f"Барлық тағамдардың жиынтық калориясы: {barlygy} ккал")
        if barlygy > kunlik_norma:
            print("⚠️ Күндік норма асып кетті!")
        else:
            print("✅ Норма ішінде қалдыңыз.")

    elif tauda == "4":
        max_food = max(kaloria_db, key=kaloria_db.get)
        print(f"🍕 Ең калориялы тағам: {max_food.capitalize()} ({kaloria_db[max_food]} ккал)")

    elif tauda == "0":
        print("Бағдарлама жабылды. Kaloria.kz таңдағаныңызға рақмет! 🥑")
        break

    else:
        print("Қате таңдау! Қайта енгізіңіз.")
