import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def convert_video_to_audio(video_path, audio_path):
    # Charger la vidéo
    video_clip = VideoFileClip(video_path)
    
    # Extraire l'audio
    audio_clip = video_clip.audio
    
    # Sauvegarder l'audio
    audio_clip.write_audiofile(audio_path)

def compress_audio(input_audio_path, output_audio_path):
    # Charger l'audio
    audio = AudioSegment.from_file(input_audio_path)
    
    # Compresser sans perte de qualité
    compressed_audio = audio.export(output_audio_path, format="mp3", bitrate="320k")

def process_videos_in_folder(folder_path):
    # Parcourir tous les fichiers du dossier
    for filename in os.listdir(folder_path):
        if filename.endswith(".mkv") or filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)

            # Déterminer le chemin pour l'audio et l'audio compressé
            audio_path = os.path.splitext(video_path)[0] + ".mp3"
            compressed_audio_path = os.path.splitext(video_path)[0] + "_compressed.mp3"

            # Conversion vidéo vers audio
            convert_video_to_audio(video_path, audio_path)

            # Compression audio sans perte de qualité
            compress_audio(audio_path, compressed_audio_path)

            # Supprimer le fichier audio non compressé si nécessaire
            os.remove(audio_path)

            print(f"Conversion et compression terminées pour {filename}")

if __name__ == "__main__":
    # Spécifiez le chemin du dossier contenant les vidéos
    videos_folder_path = "chemin/vers/votre/dossier/videos"

    # Traiter toutes les vidéos dans le dossier
    process_videos_in_folder(videos_folder_path)

    print("Toutes les conversions et compressions sont terminées.")
