import streamlit as st
import base64

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    c = st.container()
    c.write(html, unsafe_allow_html=True)

render_svg(open("issue/default.svg").read())