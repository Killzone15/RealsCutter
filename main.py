from moviepy.editor import VideoFileClip
import os


def split_video_for_shorts(file_path, clip_duration=32):
    video = VideoFileClip(file_path)
    total_duration = int(video.duration)
    filename, _ = os.path.splitext(os.path.basename(file_path))

    output_folder = f"{filename}_shorts"
    os.makedirs(output_folder, exist_ok=True)

    total_clips = (total_duration + clip_duration - 1) // clip_duration

    for i in range(total_clips):
        start = i * clip_duration
        end = min(start + clip_duration, total_duration)

        # Применяем прямое использование ffmpeg для нарезки
        output_filename = f"{i + 1:03}.mp4"
        output_path = os.path.join(output_folder, output_filename)

        # Используем метод ffmpeg для нарезки
        video.subclip(start, end).write_videofile(output_path, codec="libx264", audio_codec="aac", logger=None)

        print(f"🔪 Нарезка: {output_filename} ({start}–{end} сек)")

    print(f"\n✅ Готово! Файлы сохранены в: {output_folder}")


# Пример вызова
split_video_for_shorts(r"D:\RENDER\PremierePro\demons_shorts_full.mp4")
