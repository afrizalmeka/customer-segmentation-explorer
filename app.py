"""
app.py - Customer Segmentation Explorer (Sesi 15 - Mini Project).

Kelompokkan pelanggan berdasarkan pendapatan tahunan dan spending score
memakai K-Means (Sesi 11). Fitur utama: slider jumlah cluster (K) yang
mengubah visualisasi secara REAL-TIME.

Jalankan dengan:
    streamlit run app.py
"""
import sqlite3

import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans

st.title("Customer Segmentation Explorer")
st.write("Kelompokkan pelanggan berdasarkan pendapatan tahunan dan spending score, memakai K-Means yang dipelajari di Sesi 11. Geser slider K untuk lihat perubahan cluster secara langsung.")

DB_PATH = "riwayat_segmentasi.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS eksplorasi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jumlah_cluster INTEGER,
            inertia REAL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()

df = pd.read_csv("mall_customers.csv")
X = df[["Annual_Income_k", "Spending_Score"]]

st.write("### Pilih Jumlah Cluster")
k = st.slider("Jumlah Cluster (K)", min_value=2, max_value=8, value=5)

# Setiap kali slider digeser, Streamlit menjalankan ulang seluruh skrip,
# termasuk baris ini - jadi model otomatis dilatih ulang dengan K baru,
# menghasilkan efek "real-time" tanpa kode tambahan apapun.
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X)

st.write("### Visualisasi Cluster")
st.scatter_chart(df, x="Annual_Income_k", y="Spending_Score", color="cluster")

st.write("### Ringkasan per Cluster")
st.write("Rata-rata pendapatan dan spending score untuk tiap cluster:")
ringkasan = df.groupby("cluster")[["Annual_Income_k", "Spending_Score"]].mean()
st.dataframe(ringkasan)

if st.button("Simpan Eksplorasi Ini"):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO eksplorasi (jumlah_cluster, inertia) VALUES (?, ?)",
        (k, kmeans.inertia_),
    )
    conn.commit()
    conn.close()
    st.success(f"Tersimpan: K={k}")

st.write("### Riwayat Eksplorasi")
conn = sqlite3.connect(DB_PATH)
riwayat_df = pd.read_sql_query("SELECT * FROM eksplorasi ORDER BY id DESC", conn)
conn.close()
st.dataframe(riwayat_df)
