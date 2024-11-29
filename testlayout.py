import streamlit as st

# CSS untuk memusatkan konten
st.markdown("""
    <style>
    .centered-content {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh; /* Memastikan konten berada di tengah viewport */
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Konten yang akan dipusatkan
st.markdown("""
    <div class="centered-content">
        <div>
            <h1>Selamat Datang!</h1>
            <p>Ini adalah konten yang dipusatkan tanpa kolom.</p>
            <button onclick="alert('Tombol diklik!')">Klik Saya</button>
        </div>
    </div>
""", unsafe_allow_html=True)
