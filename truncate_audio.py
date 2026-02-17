import os
import numpy as np
import scipy.io.wavfile as wav

def truncate_wav(input_path, output_path, max_duration_sec=120):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    try:
        print(f"Reading {input_path}...")
        rate, data = wav.read(input_path)
        
        # Calculate max samples
        max_samples = int(rate * max_duration_sec)
        
        # Determine duration
        original_frames = data.shape[0]
        original_duration = original_frames / rate
        
        if original_frames > max_samples:
            truncated_data = data[:max_samples]
            new_duration = max_samples / rate
            print(f"Truncating from {original_duration:.2f}s to {new_duration:.2f}s")
        else:
            truncated_data = data
            print(f"File is already short enough ({original_duration:.2f}s). Copying.")

        # Save
        wav.write(output_path, rate, truncated_data)
        print(f"Saved truncated file to: {output_path}")
            
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))
outputs_dir = os.path.join(base_dir, 'outputs')

study_in = os.path.join(outputs_dir, 'study_song_long.wav')
phone_in = os.path.join(outputs_dir, 'phone_song_long.wav')

study_out = os.path.join(outputs_dir, 'study_song_preview.wav')
phone_out = os.path.join(outputs_dir, 'phone_song_preview.wav')

# Run truncation
truncate_wav(study_in, study_out)
truncate_wav(phone_in, phone_out)
