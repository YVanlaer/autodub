from pathlib import Path

from moviepy.editor import VideoFileClip


def extract_audio(
    input_mp4: Path,
    output_mp3: Path,
) -> None:
    video_clip = VideoFileClip(str(input_mp4))

    audio_clip = video_clip.audio

    audio_clip.write_audiofile(str(output_mp3))

    audio_clip.close()
    video_clip.close()


if __name__ == "__main__":
    mp4_file = Path(r"..\..\data\examples\meatthezoo.mp4")
    mp3_file = Path(r"..\..\data\examples\audio.mp3")

    extract_audio(mp4_file, mp3_file)
