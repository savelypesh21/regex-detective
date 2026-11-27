"""Визуальная версия Regex-детектива на Streamlit."""
import streamlit as st
from rounds import ROUNDS, run_self_tests

st.set_page_config(page_title="Regex-детектив", page_icon="🕵️", layout="centered")
run_self_tests()

if "round_index" not in st.session_state:
    st.session_state.round_index = 0
if "solved" not in st.session_state:
    st.session_state.solved = set()
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "feedback" not in st.session_state:
    st.session_state.feedback = None

st.markdown("""
<style>
.stApp {background: linear-gradient(145deg, #101827, #1b2638);}
.block-container {max-width: 850px; padding-top: 2rem;}
.case-card {background: #202d40; border: 1px solid #40516a;
padding: 22px; border-radius: 16px; margin: 12px 0;}
.small-label {color: #9fb2ca; font-size: 0.78rem; letter-spacing: 2px;}
</style>
""", unsafe_allow_html=True)

st.title("🕵️ REGEX-ДЕТЕКТИВ")
st.caption("Расследование, в котором главная улика — твоё регулярное выражение.")

total = len(ROUNDS)
idx = st.session_state.round_index
completed = len(st.session_state.solved)
st.progress(completed / total, text=f"Получено улик: {completed} из {total}")

if idx >= total:
    st.success("🎉 ДЕЛО РАСКРЫТО! Вы собрали все улики.")
    st.balloons()
    for i in range(total):
        st.write(f"🔎 {ROUNDS[i].clue}")
    if st.button("Начать расследование заново"):
        st.session_state.round_index = 0
        st.session_state.solved = set()
        st.session_state.feedback = None
        st.session_state.show_hint = False
        st.rerun()
    st.stop()

current = ROUNDS[idx]
st.markdown(f"### {current.chapter}")
st.markdown(f"## Дело № {idx + 1}. {current.title}")

with st.container(border=True):
    st.markdown("**ЗАДАНИЕ**")
    st.write(current.task)
    st.markdown("**ПРИМЕРЫ И ОЖИДАЕМЫЙ РЕЗУЛЬТАТ**")
    st.code(current.examples, language="text")

pattern = st.text_input(
    "Введи регулярное выражение",
    placeholder=r"Например: [A-Z]{2}-\d{3}",
    key=f"pattern_{idx}",
)

col1, col2 = st.columns(2)
with col1:
    check_clicked = st.button("🔍 Проверить выражение", use_container_width=True)
with col2:
    hint_clicked = st.button("💡 Подсказка", use_container_width=True)

if hint_clicked:
    st.session_state.show_hint = True
if st.session_state.show_hint:
    st.info(current.hint)

if check_clicked:
    if not pattern:
        st.session_state.feedback = (False, "Сначала введи регулярное выражение.")
    else:
        st.session_state.feedback = current.check(pattern)

if st.session_state.feedback:
    success, message = st.session_state.feedback
    if success:
        st.success("✅ Отлично! " + message)
        st.markdown(f"### 🔎 {current.clue}")
        st.session_state.solved.add(idx)
        if st.button("Перейти к следующему делу", type="primary"):
            st.session_state.round_index += 1
            st.session_state.feedback = None
            st.session_state.show_hint = False
            st.rerun()
    else:
        st.error("❌ " + message)
        st.caption("Исправь шаблон и нажми «Проверить выражение» ещё раз.")

st.divider()
st.caption("Regex-детектив · Командный проект на Python")
