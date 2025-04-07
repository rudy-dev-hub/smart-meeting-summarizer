import streamlit as st
from transcription.whisper_transcriber import transcribe_audio
from summarization.gpt_summarizer import generate_summary_and_actions
import tempfile

st.set_page_config(page_title="Smart Meeting Summarizer")

st.title("🎙️ Smart Meeting Summarizer")

uploaded_file = st.file_uploader("Upload audio/video", type=["mp3", "wav", "m4a", "mp4"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    with st.spinner("Transcribing with Whisper..."):
        transcript = transcribe_audio(temp_path)
    st.text_area("Transcript", transcript, height=300)

    with st.spinner("Generating Summary and Action Items..."):
        output = generate_summary_and_actions(transcript)
    st.markdown(output)
