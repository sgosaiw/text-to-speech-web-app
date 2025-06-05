import streamlit as st
import asyncio
import edge_tts

# Set title
st.title("🗣️ Advanced Text-to-Speech Generator")

# Input text
text = st.text_area("Paste your text here:", height=300)

# Voice options
voices = {
    "Male - GuyNeural": "en-US-GuyNeural",
    "Female - JennyNeural": "en-US-JennyNeural",
    "Female - AriaNeural": "en-US-AriaNeural",
    "Male - BrandonNeural": "en-US-BrandonNeural"
}

# Voice selection
voice_selection = st.selectbox("Select Voice", list(voices.keys()))

# Speed selection
speed_options = {
    "Slow (-50%)": "-50%",
    "Normal (0%)": "0%",
    "Fast (+50%)": "+50%",
    "Very Fast (+100%)": "+100%"
}
speed_selection = st.selectbox("Select Speaking Speed", list(speed_options.keys()))

# Output format selection
format_options = ["mp3", "wav", "m4a"]
output_format = st.selectbox("Select Output Format", format_options)

# Button
if st.button("Convert to Speech"):
    if text.strip() == "":
        st.error("Please paste some text first!")
    else:
        output_file = f"speech_output.{output_format}"
        
        async def generate_tts():
            communicate = edge_tts.Communicate(
                text, 
                voices[voice_selection], 
                rate=speed_options[speed_selection]
            )
            await communicate.save(output_file)
        
        asyncio.run(generate_tts())
        
        st.success(f"Speech generated successfully as {output_format}!")

        with open(output_file, "rb") as audio_file:
            st.download_button(
                label=f"Download {output_format.upper()}",
                data=audio_file,
                file_name=output_file,
                mime=f"audio/{output_format}"
            )

