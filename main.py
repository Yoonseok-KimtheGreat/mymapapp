import streamlit as st
import folium
from streamlit_folium import folium_static

# 페이지 기본 정보
st.title("도쿄 관광 명소 추천 지도 🇯🇵")
st.markdown("한국인에게 인기 있는 도쿄의 관광지 3곳과 주변 맛집을 소개합니다.")

# 도쿄 중심 좌표
tokyo_center = [35.682839, 139.759455]

# 지도 생성
m = folium.Map(location=tokyo_center, zoom_start=12)

# 관광지 데이터
locations = [
    {
        "name": "시부야 스크램블 교차로",
        "coords": [35.6595, 139.7005],
        "desc": "도쿄의 상징적인 번화가. 젊음의 중심지.",
        "food": {
            "name": "우오가시 니혼이치 스시",
            "coords": [35.6597, 139.7012],
            "desc": "서서 먹는 신선한 초밥 체험"
        }
    },
    {
        "name": "아사쿠사 센소지",
        "coords": [35.7148, 139.7967],
        "desc": "도쿄에서 가장 오래된 절. 일본 전통문화 체험.",
        "food": {
            "name": "아사쿠사 멘치",
            "coords": [35.7145, 139.7958],
            "desc": "고로케 스타일의 인기 간식"
        }
    },
    {
        "name": "하라주쿠 메이지신궁",
        "coords": [35.6764, 139.6993],
        "desc": "도심 속 자연과 평온함이 공존하는 신사.",
        "food": {
            "name": "말차 스탠드 마루니",
            "coords": [35.6701, 139.7025],
            "desc": "진한 우지말차와 디저트"
        }
    }
]

# 마커 추가
for place in locations:
    folium.Marker(
        location=place["coords"],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

    folium.Marker(
        location=place["food"]["coords"],
        popup=f"<b>{place['food']['name']}</b><br>{place['food']['desc']}",
        icon=folium.Icon(color='green', icon='cutlery', prefix='fa')
    ).add_to(m)

# 지도 출력
folium_static(m)
