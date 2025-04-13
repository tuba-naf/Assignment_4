import streamlit as st
import json
import os
from datetime import datetime

# ---------- Constants ----------
BLOG_FILE = "blog_posts.json"
BANNER_DIR = "user_banner"  # Directory to save user-uploaded banners

# Ensure the directory exists to save the banner
if not os.path.exists(BANNER_DIR):
    os.makedirs(BANNER_DIR)

# ---------- Helper Functions ----------
def load_posts():
    if os.path.exists(BLOG_FILE):
        with open(BLOG_FILE, "r") as f:
            return json.load(f)
    return []

def save_post(title, content):
    posts = load_posts()
    post = {
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%B %d, %Y %H:%M")
    }
    posts.append(post)
    with open(BLOG_FILE, "w") as f:
        json.dump(posts, f, indent=4)

def delete_all_posts():
    if os.path.exists(BLOG_FILE):
        os.remove(BLOG_FILE)

# ---------- App Configuration ----------
st.set_page_config(page_title="📝 My Blog", layout="centered")

# ---------- Header with Banner ----------
# File uploader to upload banner image
uploaded_banner = st.file_uploader("Upload your banner image", type=["png", "jpg", "jpeg"])

if uploaded_banner is not None:
    # Save the uploaded image to the banner directory
    with open(os.path.join(BANNER_DIR, "user_banner.png"), "wb") as f:
        f.write(uploaded_banner.getbuffer())
    # Display the uploaded image
    st.image(uploaded_banner, use_container_width=True)
else:
    # If no banner image is uploaded, display the default one
    banner_path = os.path.join(BANNER_DIR, "user_banner.png")
    if os.path.exists(banner_path):
        st.image(banner_path, use_container_width=True)  # Display custom banner if uploaded
    else:
        # Default banner image
        st.markdown("""
            <div style="text-align: center;">
                <img src="https://via.placeholder.com/800x150.png?text=Welcome+to+My+Blog" alt="Blog Banner" width="100%" />
            </div>
        """, unsafe_allow_html=True)

# ---------- Sidebar Profile ----------
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=120)  # Replace with your image
    st.markdown("""
        ### 👋 Hello, I'm Tuba Nafees
        _A passionate writer and tech enthusiast._
        ---
    """)
    menu = st.radio("📌 Navigate", ["🏠 Home", "➕ Add New Post", "📞 Contact"])

# ---------- Footer ----------
def footer():
    st.markdown("""
        <footer style="text-align:center; padding: 20px;">
            <p style="color: gray;">Made with ❤️ in Streamlit | &copy; 2025 Your Blog</p>
        </footer>
    """, unsafe_allow_html=True)

# ---------- Home Page - Display Posts ----------
if menu == "🏠 Home":
    st.subheader("📚 Recent Posts")

    posts = load_posts()
    if posts:
        for post in reversed(posts):
            with st.expander(f"📖 {post['title']} — *{post['date']}*"):
                st.markdown(post["content"], unsafe_allow_html=True)
    else:
        st.info("No posts yet. Go to 'Add New Post' to get started!")

# ---------- Add Post Page - Create New Post ----------
elif menu == "➕ Add New Post":
    st.subheader("✍️ Write a New Blog Post")

    title = st.text_input("📌 Post Title", max_chars=100, placeholder="e.g. My Coding Journey")
    content = st.text_area("📝 Post Content (Markdown supported)", height=250)

    st.markdown("#### 👀 Preview")
    if content:
        st.markdown(content)

    if st.button("🚀 Publish Post"):
        if title and content:
            save_post(title, content)
            st.success("✅ Post published successfully!")
            st.balloons()
        else:
            st.warning("Please enter both a title and content.")

# ---------- Contact Page - Contact Form ----------
elif menu == "📞 Contact":
    st.subheader("📬 Contact Me")

    with st.form(key='contact_form'):
        name = st.text_input("Your Name", max_chars=100)
        email = st.text_input("Your Email", max_chars=100)
        message = st.text_area("Your Message", height=150)

        submit_button = st.form_submit_button(label='Send Message')

    if submit_button:
        if name and email and message:
            st.success("✅ Your message has been sent successfully!")
            # Here, you could integrate an email API to send the message.
        else:
            st.warning("Please fill out all fields.")

# ---------- Footer ----------
footer()
