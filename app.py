from ollama import Client
import streamlit as st
import markdown

st.title("AI Code Review Bot")
api_key = st.text_input("Enter your Ollama API Key: ")

client = Client(host="https://ollama.com", headers={"Authorization":api_key})
    
def generate_review(code_text):
    
    msg=[
         {"role": "system", "content": (
            "You are a senior code reviewer. "
            "Provide structured feedback in Markdown format with these sections:\n"
            "## Bugs & Errors\n"
            "## Style & Formatting\n"
            "## Performance Issues\n"
            "## Security Concerns\n"
            "## Suggestions & Improvements\n"
        )},
        {"role": "user", "content": f"Review the following code:\n\n{code_text}"}
        ]

    response = client.chat(model="qwen3-coder:480b-cloud", messages=msg)
    return response["message"]["content"]

st.set_page_config(page_title="AI Code Review Bot", layout="wide")
st.write("Upload a code file and get an instant review powered by Ollama Cloud.")

file = st.file_uploader("Upload a code file", type=["py", "js", "java", "cpp", "ts", "go"])

if file is not None:

    code_text = file.read().decode("utf-8")
    with st.expander("📄 View Uploaded Code"):
        st.code(code_text, language=file.name.split(".")[-1])

    if st.button("🔍 Run Code Review"):
        with st.spinner("Reviewing your code... please wait ⏳"):
            review = generate_review(code_text)
            
        review_html = markdown.markdown(review, extensions=["fenced_code", "tables"])
        
        dark_css = """
        <style>
            body {
                background-color: #1e1e1e;
                color: #e6e6e6;
                font-family: Arial, sans-serif;
                line-height: 1.6;
                padding: 20px;
            }
            h1, h2, h3 {
                color: #4fc3f7;
                border-bottom: 1px solid #333;
                padding-bottom: 4px;
            }
            ul {
                margin-left: 20px;
            }
            li {
                margin: 6px 0;
            }
            code {
                background: #2d2d2d;
                color: #f8f8f2;
                padding: 2px 5px;
                border-radius: 4px;
                font-family: monospace;
            }
            pre {
                background: #2d2d2d;
                color: #f8f8f2;
                padding: 10px;
                border-radius: 6px;
                overflow-x: auto;
            }
            a { color: #80cbc4; }
        </style>
        """

        st.markdown("## 📝 Code Review Report")
        st.components.v1.html(
            f"<html><head>{dark_css}</head><body>{review_html}</body></html>",
            height=600,
            scrolling=True
        )

        full_html = f"<html><head>{dark_css}</head><body>{review_html}</body></html>"
        st.download_button(
            label="⬇️ Download Review Report (Dark HTML)",
            data=full_html,
            file_name="code_review_report_dark.html",
            mime="text/html"
        )
