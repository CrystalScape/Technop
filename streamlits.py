import streamlit as st
st.image('logo2.png')
topik = ['info' , 'transformer' , 'NLP' , 'thinklab' , 'Developer']
cols1 , cols2 = st.columns(2,gap = 'small')
with cols1 : 
    st.write("Perhatian ini hanya di Gunakan sebagai Promosi atau bisa di sebut Demo , Program asli lebih compleks lagi Dan pastikan perhatikan ketika mengetik Huruf Besar Kecil nya")
tops = ' , '.join(topik)
to = f'''Topik Yang tersedia : \n {tops}'''
with cols2 : 
    st.write(to)
prom = st.chat_input("ketik info atau Developer")
if prom :
    with st.chat_message("You") :
        st.write(prom)
    with st.chat_message("Thinkfy"):
        split_proms = prom.split()
        for i in range(len(split_proms)):
            if split_proms[i] in topik : 
                kon_awal = True
                if kon_awal : 
                    topiks = split_proms[i]
                else : topiks = None
        if topiks in split_proms and 'info' in split_proms: 
            info = '''Thinkfy adalah product kecerdasan Buatan ThinkLab yang di develop oleh Yudo Nidlom firmansyah
            Yudo Pertama kali membuat chatbot ini pada tahun 2022 lalu , tepatnya bulan desember 2022
            chatbot ini di buat manual tanpa bantuan hungging face / ChatGPT , jadi Pertama Yudo melakukan
            sebuah Riset Untuk membuat Arsitektur Neural Netwok Transformer terbaik selain Untuk Arsitektur Neural Network ,
            Yudo juga melakukan Riset Untuk menambah fitur lain yaitu : '''
            st.image('logo.png')
            st.title('Thinkfy')
            st.write(info)
            st.write('''
                    - Text to Image (membuat text caption / cerita dari gambar) 
                    - Prediksi dari dataset input dengan Linear Regresi (adalah termasuk perhitungan Statistika)
                    - Klasifikasi emosi dari Text sehingga akan muncul Stiker sebagai Ekspresi 
                    - memory untuk mengingat caht 
                    - Diskusi Dengan Dataset 
                    - Prediksi Dolar (Time Series)
                    - Chat biasa 
                    - Deepfake (sedang di riset)
                    - mengerjakan soal matematika
                    - pengujian dataset dengan ML algorithm yang tersedia
                    - Reinforcment akurasi nya dengan algoritma Deep MAB
                     ''')
        elif topiks in split_proms and 'Developer' in split_proms:
            st.title('Profile Developer')
            col1 , col2 = st.columns(2,gap='small')
            with col1:
                st.image('profil.jpg')
                prop1 = '''Yudo Nidlom Firmansyah adalah seorang anak laki laki yang lahir pada 
                tahun 2003 bulan agustus tanggal 4 , memiliki hobi :'''
                st.write(prop1)
                st.write('''
                         - Membaca buku 
                         - ngoding 
                         - riset dan eksperimen 
                         - sains
                         ''')
            with col2:
                st.title('Yudo Nidlom Firmansyah')
                prop = '''umur 20th 
                saat ini masih Mahasiswa 
                Status : Privacy! 
                posisi : Developer , anggota , Pemilik , Engginer'''
                st.write(prop)
                st.title("PLANING")
                plan = '''
                - Melakukan penelitian terhadap Advance Deep Reinforcmen Learning untuk membuat 
                algoritma Deep Reinforcmen learning Baru bernama ACTGA
                - Meneliti untuk mengembangkan Computer vision Untuk masalah simulasi Robot di Pygame
                - meneliti untuk mengembangkan algoritma AlphaZero untuk mengatasi masalah permainan Game papan
                - Meneliti CV , NLP , RL , untuk pengembangan project virtual RA
                '''
                st.write(plan)
        elif topiks in split_proms and 'transformer' in split_proms:
            colu1 , colu2 = st.columns(2 , gap = 'small')
            with colu1 : 
                st.image('transfor.jpg')
            t = '''
            adalah sebuah Arsitektur neural network yang Biasa di gunakan untuk menyelesaikan masalah NLP
            yang di perkenalkan pada tahun 2017 oleh google sebagai model NN Translasi
            lalu seiring berjalan nya waktu Transformer berkembang bisa di gunakan untuk berbagai hal 
            Contoh : NLP, CV , RL , Prediksi \n Transformer memiliki Anatomi : 
            '''
            st.write(t)
            st.write("""
                     - Attention (Multihead dan Scale dot Product)
                     - Positional enc / dec
                     - enc layer 
                     - encoder
                     - dec layer
                     - decoder layer
                     - Transformer Block
                     """)
            with colu2:
                st.title('TRANSFORMERS NLP')
        elif topiks in split_proms and 'NLP' in split_proms:
            st.title("Natural Language Procecing")
            means = '''
            NLP adalah sebuah program yang dimana program tersebut akan belajar memahami 
            bahasa manusia sehingga bisa menyelesaikan masalah Seperti : 
            '''
            st.write(means)
            st.write('''
                     - Translasi 
                     - image to text 
                     - chatbot
                     - text clasifikasi
                     ''')
        elif topiks in split_proms and 'thinklab' in split_proms :
            st.image('lab.png')
            st.write('''ThinkLab adalah sebuah product utama kecerdasan buatan yang di Develop oleh
                     Yudo Nidlom Firmansyah juga , ThinkLab memiliki banyak product yang telah di kembangkan 
                     atau sedang masa pengembangan , thinkLab sendiri dibuat untuk membantu memudahkan 
                     orang orang dalam menyelesaikan pekerjaan nya , Beberapa product yang sedang di kembangkan : 
                     ''')
            st.write('''
                     - ThinkFy (chatbot)
                     - ImThink (pengenalan objek / deteksi objek)
                     - ROBSIM (simulasi kecerdasan buatan untuk robot atau simulasi lain)
                     - GiThink (pengembangan Algoritma Alphazero)
                     - ActGA (nama untuk project riset penggabungan Algoritma RL)
                     - MuThink (Music Generator)
                     - MaThs (project untuk membuat Framework / module untuk matematika dan fisika)
                     - ScyT (Project riset untuk mengembangkan kecerdasan buatan untuk masalah pengamanan)''')