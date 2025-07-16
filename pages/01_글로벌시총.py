import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd

# 페이지 설정
st.set_page_config(layout="wide")
st.title("글로벌 시가총액 상위 기업 주가 변동")

# 상위 기업 티커 (예시)
# 실제 상위 기업 리스트는 변동될 수 있으며, 정확한 리스트는 수동으로 업데이트해야 합니다.
top_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Amazon": "AMZN",
    "Alphabet (GOOGL)": "GOOGL",
    "Alphabet (GOOG)": "GOOG",
    "Meta Platforms": "META",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK-B",
    "Eli Lilly": "LLY",
    "TSMC": "TSM",
    "JPMorgan Chase": "JPM"
}

# 날짜 설정
end_date = datetime.now()
start_date = end_date - timedelta(days=3*365) # 최근 3년

# 사이드바에서 기업 선택
selected_company_name = st.sidebar.selectbox("기업을 선택하세요:", list(top_companies.keys()))
selected_ticker = top_companies[selected_company_name]

st.sidebar.markdown(f"선택된 기업: **{selected_company_name} ({selected_ticker})**")
st.sidebar.markdown(f"데이터 기간: **{start_date.strftime('%Y-%m-%d')}** 부터 **{end_date.strftime('%Y-%m-%d')}** 까지")

# 주가 데이터 가져오기
@st.cache_data
def get_stock_data(ticker, start, end):
    try:
        data = yf.download(ticker, start=start, end=end)
        return data
    except Exception as e:
        st.error(f"주가 데이터를 가져오는 중 오류가 발생했습니다: {e}")
        return pd.DataFrame() # 빈 데이터프레임 반환

stock_data = get_stock_data(selected_ticker, start_date, end_date)

if not stock_data.empty:
    st.subheader(f"{selected_company_name} ({selected_ticker}) 최근 3년간 주가 변동")

    # Plotly 그래프 생성
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='종가'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Open'], mode='lines', name='시작가', opacity=0.7))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['High'], mode='lines', name='고가', opacity=0.7))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Low'], mode='lines', name='저가', opacity=0.7))

    fig.update_layout(
        title=f'{selected_company_name} 주가 추이',
        xaxis_title='날짜',
        yaxis_title='주가 (USD)',
        hovermode="x unified",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    # 추가 정보 표시
    st.subheader("데이터 요약")
    st.write(stock_data.describe())

    st.subheader("최근 데이터 미리보기")
    st.write(stock_data.tail())

else:
    st.warning("선택하신 기업의 주가 데이터를 가져올 수 없습니다. 티커를 확인하거나 나중에 다시 시도해주세요.")

st.markdown("---")
st.markdown("이 애플리케이션은 yfinance를 사용하여 데이터를 가져오고 Plotly로 그래프를 시각화합니다.")
