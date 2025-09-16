import streamlit as st
import random

# Danh sách món ăn (tên, link ảnh, địa chỉ)
foods = [
    {
        "name": "Phở Bò",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Pho-Beef-Noodles-2008.jpg",
        "address": "24 Lý Quốc Sư, Hà Nội"
    },
    {
        "name": "Bún Chả",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/04/Bun_cha_Hanoi.JPG",
        "address": "34 Hàng Mành, Hà Nội"
    },
    {
        "name": "Cơm Tấm",
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Com_tam_suon_bi_cha.jpg",
        "address": "Quận 1, TP.HCM"
    },
    {
        "name": "Mì Quảng",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Mi_quang.jpg",
        "address": "Đà Nẵng"
    }
]

# Chọn 1 món ăn ngẫu nhiên
food = random.choice(foods)

# Hiển thị trên Streamlit
st.title("🍜 Gợi ý món ăn hôm nay")

st.subheader(food["name"])
st.image(food["image"], use_column_width=True)
st.write(f"📍 Địa chỉ: {food['address']}")
