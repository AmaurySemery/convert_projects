import os
import time
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import subprocess

def convert_video_to_audio(video_path, audio_path):
    try:
        # Convertir les fichiers MKV en MP4
        if video_path.lower().endswith(".mkv"):
            mp4_path = os.path.splitext(video_path)[0] + ".mp4"
            try:
                subprocess.run(
                    [
                        "ffmpeg",
                        "-i", video_path,
                        "-c:v", "libx264",
                        "-crf", "23",
                        "-c:a", "aac",
                        "-strict", "experimental",
                        "-b:a", "192k",
                        "-ac", "2",
                        mp4_path
                    ],
                    check=True
                )
                video_path = mp4_path
                print(f"Conversion réussie : {video_path}")
            except subprocess.CalledProcessError as e:
                print(f"Erreur lors de la conversion : {e}")
            except FileNotFoundError:
                print("ffmpeg n'est pas installé ou n'est pas accessible dans le PATH.")
        else:
            print("Le fichier n'est pas un fichier MKV.")

        # Charger la vidéo
        video_clip = VideoFileClip(video_path)

        # Extraire l'audio
        audio_clip = video_clip.audio

        # Normaliser le chemin du fichier audio
        audio_path = os.path.abspath(audio_path)

        # Sauvegarder l'audio
        audio_clip.write_audiofile(audio_path)

        audio_clip.close()
        video_clip.close()

        # Attendre quelques secondes pour s'assurer que la conversion vidéo en audio est terminée
        time.sleep(5)

        # Supprimer le fichier vidéo d'origine
        os.remove(video_path)
    except:
        print("convert_video_to_audio fail")
        pass

def process_videos_in_folder(folder_path):
    # Parcourir tous les fichiers du dossier
    for filename in os.listdir(folder_path):
        if filename.endswith((".mkv", ".mp4")):
            video_path = os.path.join(folder_path, filename)

            # Déterminer le chemin pour l'audio et l'audio compressé
            audio_path = os.path.splitext(video_path)[0] + ".mp3"
            compressed_audio_path = os.path.splitext(video_path)[0] + "_compressed.mp3"

            # Conversion vidéo vers audio
            convert_video_to_audio(video_path, audio_path)

            print(f"Conversion, compression et suppression terminées pour {filename}")

if __name__ == "__main__":
    # Spécifiez le chemin du dossier contenant les vidéos
    videos_folder_path = "C:/Users/amaur/Videos/test"

    # Traiter toutes les vidéos dans le dossier
    process_videos_in_folder(videos_folder_path)

    print("Toutes les conversions et compressions sont terminées.")
