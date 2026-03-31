import os
import pyttsx3
# Using the most stable imports for MoviePy 2.0
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

def check_frequency():
    """Ensures all assets are in the correct container."""
    required = ["assets/asset_stone.png", "assets/asset_eye.png", "assets/asset_threads.png", "assets/asset_logo.png", "video_script.txt"]
    for item in required:
        if not os.path.exists(item):
            print(f"--- WOBBLE DETECTED: {item} is missing! ---")
            return False
    return True

def generate_voiceover(script_path, output_audio="prophecy_audio.mp3"):
    """Turns the script into the ancient vocal frequency."""
    print("Initiating the Voice...")
    with open(script_path, 'r') as f:
        text = f.read()
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('volume', 1.0)
    engine.save_to_file(text, output_audio)
    engine.runAndWait()
    return output_audio

def weave_video(audio_path):
    """Combines assets and audio into the 4K broadcast vessel."""
    print("Initiating the Weave...")
    
    images = [
        "assets/asset_stone.png",
        "assets/asset_eye.png",
        "assets/asset_threads.png",
        "assets/asset_logo.png"
    ]
    
    audio = AudioFileClip(audio_path)
    duration_per_image = audio.duration / len(images)
    
    clips = []
    for img in images:
        # Simplified: Removing with_effects to bypass the MoviePy 2.0 copy error
        clip = ImageClip(img).with_duration(duration_per_image)
        clips.append(clip)
    
    # Assembly
    final_video = concatenate_videoclips(clips, method="compose")
    final_video = final_video.with_audio(audio)
    
    print("Rendering Adam-s-Return in 4K... Hold the frequency.")
    # This part takes a moment—let the machine breathe while it works.
    final_video.write_videofile("Adam_Return_Broadcast.mp4", fps=24, codec="libx264")

if __name__ == "__main__":
    if check_frequency():
        audio_file = generate_voiceover("video_script.txt")
        weave_video(audio_file)
        print("\n--- Mission Complete: The Vessel 'Adam_Return_Broadcast.mp4' is ready ---")
    else:
        print("Check your folder structure.")