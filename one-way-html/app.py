import streamlit as st
import json

st.title("Interactive Canvas with User Input")



# Streamlit과 HTML 간 데이터 연결
@st.fragment
def draw():
    # 상태 저장을 위한 초기화
    if "scale" not in st.session_state:
        st.session_state.scale = 1.0
    if "offsetX" not in st.session_state:
        st.session_state.offsetX = 0
    if "offsetY" not in st.session_state:
        st.session_state.offsetY = 0
    # 사용자 입력 받기
    x = st.number_input("Circle X Position", value=0)
    y = st.number_input("Circle Y Position", value=0)
    angle = st.number_input("Circle Rotation (Degrees)", value=0)

    # 사각형 네 꼭지점 입력 받기
    rect_points = [
        [st.number_input("Rect Point 1 X", value=-10), st.number_input("Rect Point 1 Y", value=-10)],
        [st.number_input("Rect Point 2 X", value=10), st.number_input("Rect Point 2 Y", value=-10)],
        [st.number_input("Rect Point 3 X", value=10), st.number_input("Rect Point 3 Y", value=10)],
        [st.number_input("Rect Point 4 X", value=-10), st.number_input("Rect Point 4 Y", value=10)],
    ]

    # HTML 파일 읽기
    html_code = open("canvas.html").read()

    # JSON으로 데이터 변환
    data = json.dumps({
        "x": x,
        "y": y,
        "angle": angle,
        "rect_points": rect_points,
        "scale": st.session_state.scale,
        "offsetX": st.session_state.offsetX,
        "offsetY": st.session_state.offsetY
    })
    print(data)
    st.components.v1.html(f"""
    {html_code}
    <script>
        const data = {data};  // Python에서 받은 데이터
        updateFromStreamlit(data.x, data.y, data.angle, data.rect_points, data.scale, data.offsetX, data.offsetY);
    </script>
    """, height=600)

draw()
