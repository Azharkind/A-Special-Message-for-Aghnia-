import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie

# --- FUNGSI UNTUK MEMUAT ANIMASI (Tidak perlu diubah) ---
def load_lottieurl(url: str):
    """
    Mengambil file JSON animasi Lottie dari URL.
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- PENGATURAN HALAMAN WEB ---
st.set_page_config(
    page_title="FOR YOU AGHNIA AURA FASYA!",
    page_icon="💌",
    layout="centered"
)

# --- MEMORI UNTUK MENYIMPAN PROGRES PESAN ---
if 'pesan_idx' not in st.session_state:
    st.session_state.pesan_idx = 0

# --- DAFTAR PESAN SEMANGAT KAMU ---
pesan_semangat = [
    "Lagi hectic sama tugas atau praktikum yaa? Wajar banget kokk, Aku juga gitu soalnya....😆",
    "Tapi, aku yakin Kak Aghniaa Pasti bisa ngelewatin semuanya!✨",
    "Setiap usaha dan waktu yang Kakak luangin itu nggak akan pernah sia-sia lhoo💐.",
    "Jangan lupa istirahat yang cukup dan jaga kesehatan juga yaaa. Itu yang paling penting!🌞",
    "Pokoknya... SEMANGAT TERUS KAK! Kamu keren banget! 🔥",
    "SEMANGATTT KULIAHHNYAA...🤗",
]

# --- JUDUL DAN HEADER ---
st.title("💌 A Message for Aghnia!")
st.markdown("---")

# Menampilkan animasi di bagian atas
lottie_url = "https://assets10.lottiefiles.com/packages/lf20_j7s3s1im.json"
lottie_json = load_lottieurl(lottie_url)
if lottie_json:
    st.lottie(lottie_json, speed=1, height=250, key="initial_animation")

st.header("Haii Makasi Banyak Udah Nyempetin Buat Baca😊")
st.write("Dibaca pelan-pelan yaaa...")
st.markdown("---")

# --- LOGIKA TOMBOL INTERAKTIF BARU ---

# Cek apakah masih ada pesan yang bisa ditampilkan
if st.session_state.pesan_idx < len(pesan_semangat):
    
    # Tampilkan pesan sesuai urutan
    current_pesan = pesan_semangat[st.session_state.pesan_idx]
    st.info(f"**Pesan ke-{st.session_state.pesan_idx + 1}:**\n\n_{current_pesan}_")
    
    # Buat tombol "Lanjut"
    if st.button("Lanjut Baca →", key=f"next_{st.session_state.pesan_idx}"):
        st.toast('Next... ✨', icon='💌')
        
        st.session_state.pesan_idx += 1
        st.rerun()

# Jika semua pesan sudah ditampilkan
else:
    st.success("Yess! Semua pesan berhasil tersampaikan!")
    st.header("Keep Shining yaaa, Kak! 🌟")
    st.balloons()
    
    if st.button("Mau Baca Lagi?"):
        time.sleep(1)
        
        st.session_state.pesan_idx = 0
        st.rerun()

st.markdown("---")
st.write("From Kindiii")