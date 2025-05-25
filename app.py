import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Data Upload
df = pd.read_csv("customers.csv")

st.title("Müşteri Segmentasyonu ve Kişiselleştirilmiş Kampanya Paneli")

# --- Sidebar Logo ---
logo = Image.open("logo.jpg")
st.sidebar.image(logo, use_container_width=True)

# --- Data Preparation for Segmentation  ---
X = df[["total_spent", "num_transactions"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method ile en uygun küme sayısını bulma
def plot_elbow(X):
    distortions = []
    K = range(1, 10)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)
    fig, ax = plt.subplots()
    ax.plot(K, distortions, 'bx-')
    ax.set_xlabel('Küme Sayısı')
    ax.set_ylabel('Inertia')
    ax.set_title('Elbow Yöntemi')
    st.pyplot(fig)

with st.expander("Elbow Yöntemi ile Küme Sayısı Seçimi"):
    plot_elbow(X_scaled)

# Elbow (default 4)
n_clusters = st.sidebar.slider("Küme (Segment) Sayısı", 2, 8, 4)
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
df['segment'] = kmeans.fit_predict(X_scaled)

# --- Sidebar Filters ---
min_age, max_age = int(df.age.min()), int(df.age.max())
age_range = st.sidebar.slider("Yaş Aralığı", min_age, max_age, (min_age, max_age))
gender = st.sidebar.multiselect("Cinsiyet", options=df.gender.unique(), default=list(df.gender.unique()))
spend_min, spend_max = int(df.total_spent.min()), int(df.total_spent.max())
spend_range = st.sidebar.slider("Harcama Aralığı", spend_min, spend_max, (spend_min, spend_max))
segment_options = st.sidebar.multiselect("Segment Seçimi", options=sorted(df.segment.unique()), default=list(sorted(df.segment.unique())))

# --- Filtration ---
filtered = df[
    (df.age.between(*age_range)) &
    (df.gender.isin(gender)) &
    (df.total_spent.between(*spend_range)) &
    (df.segment.isin(segment_options))
]

st.subheader("Filtrelenmiş Müşteri Tablosu")
st.dataframe(filtered)

# --- Visualization ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Segmentlere Göre Harcama Dağılımı**")
    fig1, ax1 = plt.subplots()
    sns.barplot(x="segment", y="total_spent", data=filtered, estimator=np.mean, ax=ax1)
    st.pyplot(fig1)

with col2:
    st.markdown("**Yaşa Göre Müşteri Segmentasyonu**")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x="age", y="total_spent", hue="segment", data=filtered, palette="tab10", ax=ax2)
    st.pyplot(fig2)

st.markdown("**Zaman İçindeki Harcama Eğilimleri**")
filtered['last_purchase_date'] = pd.to_datetime(filtered['last_purchase_date'])
trend = filtered.groupby('last_purchase_date')['total_spent'].sum().reset_index()
fig3, ax3 = plt.subplots()
ax3.plot(trend['last_purchase_date'], trend['total_spent'], marker='o')
ax3.set_xlabel('Tarih', fontsize=10)
ax3.set_ylabel('Toplam Harcama', fontsize=10)
plt.xticks(rotation=45, fontsize=8)
plt.yticks(fontsize=8)
fig3.tight_layout()
st.pyplot(fig3)

# --- Customer Detail and Campaign Recommendation ---
st.subheader("Müşteri Detayları ve Kampanya Önerisi")
selected_customer = st.selectbox("Bir müşteri seçin", filtered['name'])
customer_row = filtered[filtered['name'] == selected_customer].iloc[0]
st.write(customer_row)

# Simple campaign proposal logic
segment_campaigns = {
    0: "%10 indirim kuponu!",
    1: "Ücretsiz kargo fırsatı!",
    2: "Sadakat puanı kazanın!",
    3: "Yeni sezon ürünlerinde özel teklif!",
    4: "Kişiye özel sürpriz!",
    5: "Arkadaşını getir, ikinize de hediye!",
    6: "VIP müşteri avantajları!",
    7: "Sınırlı süreli kampanya!"
}
campaign = segment_campaigns.get(customer_row['segment'], "Özel kampanya!")
st.info(f"Önerilen Kampanya: {campaign}")

# --- Sidebar: New customer add ---
st.sidebar.markdown("---")
st.sidebar.header("Yeni Müşteri Ekle")
if st.sidebar.checkbox("Yeni müşteri ekle" ):
    with st.sidebar.form("new_customer_form"):
        new_id = int(df['customer_id'].max()) + 1
        name = st.text_input("Ad Soyad")
        age = st.number_input("Yaş", min_value=18, max_value=100, value=30)
        gender = st.selectbox("Cinsiyet", options=["Female", "Male"])
        total_spent = st.number_input("Toplam Harcama", min_value=0, value=1000)
        num_transactions = st.number_input("Alışveriş Sayısı", min_value=1, value=1)
        last_purchase_date = st.date_input("Son Alışveriş Tarihi")
        preferred_category = st.text_input("Tercih Edilen Kategori")
        submitted = st.form_submit_button("Ekle")
        if submitted:
            new_row = {
                "customer_id": new_id,
                "name": name,
                "age": age,
                "gender": gender,
                "total_spent": total_spent,
                "num_transactions": num_transactions,
                "last_purchase_date": last_purchase_date,
                "preferred_category": preferred_category
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv("customers.csv", index=False)
            st.success(f"Yeni müşteri eklendi: {name}")
            # Refresh olmadan güncel tabloyu göster
            st.session_state['df'] = df

# --- Sidebar: Add New Purchase to Existing Customer ---
st.sidebar.markdown("---")
st.sidebar.header("Mevcut Müşteriye Yeni Alışveriş Ekle")
if st.sidebar.checkbox("Yeni alışveriş ekle"):
    with st.sidebar.form("add_purchase_form"):
        customer_name = st.selectbox("Müşteri Seç", options=df['name'].unique())
        category = st.text_input("Kategori")
        amount = st.number_input("Harcama Tutarı", min_value=0, value=100)
        date = st.date_input("Alışveriş Tarihi")
        submitted2 = st.form_submit_button("Ekle")
        if submitted2:
            idx = df[df['name'] == customer_name].index[-1]
            df.at[idx, 'total_spent'] += amount
            df.at[idx, 'num_transactions'] += 1
            df.at[idx, 'last_purchase_date'] = date
            df.at[idx, 'preferred_category'] = category
            df.to_csv("customers.csv", index=False)
            st.success(f"{customer_name} için yeni alışveriş eklendi.")
            st.session_state['df'] = df

# --- Sidebar: Remove Customer ---
st.sidebar.markdown("---")
st.sidebar.header("Müşteri Sil")
if st.sidebar.checkbox("Müşteri sil" ):
    with st.sidebar.form("delete_customer_form"):
        del_customer = st.selectbox("Silinecek Müşteri", options=df['name'].unique())
        confirm = st.checkbox(f"{del_customer} adlı müşteriyi silmek istediğinize emin misiniz?")
        submitted3 = st.form_submit_button("Sil")
        if submitted3 and confirm:
            df = df[df['name'] != del_customer].reset_index(drop=True)
            df.to_csv("customers.csv", index=False)
            st.success(f"{del_customer} başarıyla silindi.")
            st.session_state['df'] = df

# --- DataFrame update ---
if 'df' in st.session_state:
    df = st.session_state['df']
