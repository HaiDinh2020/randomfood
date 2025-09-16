import streamlit as st
import random

# Danh sách món ăn (tên, link ảnh, địa chỉ)
foods = [
    {
        "name": "Phở Bò",
        "image": "https://pholyquocsu.vn/wp-content/uploads/2019/09/p1.jpg",
        "address": "24 Lý Quốc Sư, Hà Nội"
    },
    {
        "name": "Bún Chả",
        "image": "https://statics.vinpearl.com/bun-cha-ha-noi-2_1688011803.jpg",
        "address": "34 Hàng Mành, Hà Nội"
    },
    {
        "name": "Cơm Tấm",
        "image": "https://statics.vinpearl.com/com-tam-ha-noi-1_1692527283.jpg",
        "address": "Quận 1, TP.HCM"
    },
    {
        "name": "Mì Quảng",
        "image": "https://static.vinwonders.com/production/mi-quang-ha-noi-3.jpg",
        "address": "Đà Nẵng"
    }
]

# Chọn 1 món ăn ngẫu nhiên
food = random.choice(foods)

# Hiển thị trên Streamlit
st.title("🍜 Gợi ý món ăn hôm nay")

st.subheader(food["name"])
st.image(food["image"], use_container_width =True)
st.write(f"📍 Địa chỉ: {food['address']}")
