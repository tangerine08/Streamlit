# home.py
import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Waspada Phising",
)

st.sidebar.markdown("# Home")

col1, col2, col3 = st.columns([5,1,4])
with col1:
    st.markdown ("<h1 style='vertical-align:middle;margin-top:100'> Penipuan Online di Indonesia dan Pencegahannya </h1>", unsafe_allow_html=True)
    st.write('<div style="text-align: justify;vertical-align:middle;padding-right:100"> Di era serba digital sekarang ini, banyak aktifitas yang bisa dilakukan secara online dan memberikan kemudahan , namun ada juga pihak tidak bertanggung jawab melakukan hal negatif, mulai dari pemalsuan, penipuan terencana, pengatasnamaan dan juga yang paling sering terjadi adalah pencurian data. Cari tahu lebih lanjut terkait kejahatan siber yang sering terjadi di Indonesia dalam website ini. </div>', unsafe_allow_html=True)

with col2:
    st.write()
with col3:
    st.image('phising.png')

if st.button('Let\'s Go!'):
       #st.write ('Mestinya konten infografis akan muncul di luar kolom seperti di bawah')
        st.markdown ("<h1 style='text-align:center;'> 5 Jenis Penipuan Online </h1>", unsafe_allow_html=True)
        st.image('infografis-1.png')
        st.markdown('''
<ul>
    <li><strong>Phising</strong>
    <p style='text-align:justify;'> Berasal dari bahasa Inggris fishing (memancing), phising berarti memancing informasi pribadi seperti User ID, password dan data-data sensitif lainnya dengan menyamar sebagai orang atau organisasi yang berwenang melalui sebuah email, telepon atau pesan teks. Data-data tersebut kemudian akan digunakan untuk melakukan tindakan negatif lainnya seperti mencuri dengan menggunakan identitas korban, meretas sistem komputer, hingga tindakan lainnya yang merugikan dari sisi keamanan. </p>
    </li>
    <li><strong>Social Engineering</strong>
    <p style='text-align:justify;'> Penipuan online berbasis rekayasa sosial (social engineering) akan membuat pelaku kejahatan siber bisa mengontrol akun milik korban melalui data pribadi korban yang didapatkan secara cuma-cuma dari korban itu sendiri. Hal ini bisa dicapai dengan memanipulasi psikologi korban, alih-alih persoalan teknis. Misalnya, orang yang serakah rentan menjadi korban kejahatan siber, meskipun apa yang dilakukan si pelaku sebenarnya hanya menelepon korban sembari berbohong kalau dia menang undian. </p>
    </li>
</ul>
<p style='text-align:justify;'> Menurut Head of IT Governance Risk and Compliance Information Security GoPay, Genesha Saputra, Ada tiga pilar di information security, yaitu people, process, technology. Diantara ketiga pilar ini, sudah diakui di seluruh dunia bahwa people merupakan weakest link atau rantai terlemah dari keamanan informasi. “Magis ini, atau manipulasi psikologis, memang hanya ada satu cara yang efektif, yaitu edukasi.”''', unsafe_allow_html=True)
