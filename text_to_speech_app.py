import streamlit as st
import edge_tts
import asyncio
import tempfile
import os

# Set page configuration
st.set_page_config(
    page_title="Advanced Text-to-Speech",
    page_icon="🗣️",
    layout="wide"
)

# Custom title with some styling
st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>🗣️ Advanced Text-to-Speech Generator</h1>
<p style='text-align: center; font-size: 1.1em;'>Generate high-quality speech from text using Microsoft Edge TTS</p>
<hr>
""", unsafe_allow_html=True)

# Define robust voice options
# Included a few popular ones
VOICES = {
    "🇺🇸 Male - Guy (Neural)": "en-US-GuyNeural",
    "🇺🇸 Female - Jenny (Neural)": "en-US-JennyNeural",
    "🇺🇸 Female - Aria (Neural)": "en-US-AriaNeural",
    "🇺🇸 Male - Brandon (Neural)": "en-US-BrandonNeural",
    "🇬🇧 Female - Sonia (Neural)": "en-GB-SoniaNeural",
    "🇬🇧 Male - Ryan (Neural)": "en-GB-RyanNeural",
}

def main():
    # --- Sidebar Controls ---
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Voice Selection
        st.subheader("Voice Settings")
        voice_label = st.selectbox("Select Voice", list(VOICES.keys()), index=1)
        voice_key = VOICES[voice_label]
        
        # Speed Selection
        st.subheader("Audio Settings")
        speed_val = st.slider("Rate (Speed)", -50, 100, 0, format="%d%%")
        rate_str = f"{'+' if speed_val >= 0 else ''}{speed_val}%"
        
        # Pitch Selection
        pitch_val = st.slider("Pitch", -50, 50, 0, format="%dHz")
        pitch_str = f"{'+' if pitch_val >= 0 else ''}{pitch_val}Hz"
        
        # Format Selection
        st.subheader("Output")
        output_format = st.radio("Format", ["mp3", "wav"], horizontal=True)
    
    # --- Main Content ---
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📜 Input Text")
        text = st.text_area("Type or paste your text here...", height=350, placeholder="Hello! This is a test of the text-to-speech system.")
        
        generate_btn = st.button("🔊 Generate Speech", type="primary", use_container_width=True)

    with col2:
        st.subheader("🎧 Output")
        
        if generate_btn:
            if not text.strip():
                st.warning("⚠️ Please enter some text first!")
            else:
                try:
                    with st.spinner("Generating audio..."):
                        # Create a temporary file
                        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_format}") as tmp_file:
                            tmp_path = tmp_file.name
                        
                        # Run async generation
                        async def generate():
                            # Reverted to plain text communication as per user request
                            # (Known issue: minor audio cutoff at start)
                            communicate = edge_tts.Communicate(text, voice_key, rate=rate_str, pitch=pitch_str)
                            await communicate.save(tmp_path)
                        
                        asyncio.run(generate())
                        
                        # Read file data into memory for persistence
                        with open(tmp_path, "rb") as f:
                            audio_bytes = f.read()
                        
                        # Store in session state
                        st.session_state['audio_data'] = audio_bytes
                        st.session_state['audio_format'] = output_format
                        st.session_state['success_message'] = "✅ Generation Complete!"
                        
                        # Clean up temp file
                        try:
                            os.remove(tmp_path)
                        except:
                            pass

                except Exception as e:
                    st.error(f"❌ Error generating speech: {str(e)}")
        
        # Check session state to render output (PERSISTENT across reruns)
        if 'audio_data' in st.session_state:
            st.success(st.session_state.get('success_message', "Ready"))
            
            fmt = st.session_state['audio_format']
            st.audio(st.session_state['audio_data'], format=f"audio/{fmt}")
            
            st.download_button(
                label=f"⬇️ Download {fmt.upper()}",
                data=st.session_state['audio_data'],
                file_name=f"speech.{fmt}",
                mime=f"audio/{fmt}",
                use_container_width=True
            )
        elif not generate_btn and 'audio_data' not in st.session_state:
            st.info("👈 Adjust settings in the sidebar and click 'Generate Speech' to start.")

if __name__ == "__main__":
    main()

