from moviepy.editor import VideoFileClip
import os


def split_video_for_shorts(file_path, clip_duration=30):
    video = VideoFileClip(file_path)
    total_duration = int(video.duration)
    filename, _ = os.path.splitext(os.path.basename(file_path))

    output_folder = f"{filename}_shorts"
    os.makedirs(output_folder, exist_ok=True)

    total_clips = (total_duration + clip_duration - 1) // clip_duration

    for i in range(total_clips):
        start = i * clip_duration
        # Если это последний кусок — режем точно до конца
        if i == total_clips - 1:
            end = video.duration
        else:
            end = min(start + clip_duration, total_duration)

        output_filename = f"{i + 1:03}.mp4"
        output_path = os.path.join(output_folder, output_filename)

        # Нарезка и сохранение
        video.subclip(start, end).write_videofile(output_path, codec="libx264", audio_codec="aac", logger=None)

        print(f"🔪 Нарезка: {output_filename} ({start:.2f}–{end:.2f} сек)")

    print(f"\n✅ Готово! Файлы сохранены в: {output_folder}")


# Пример вызова
split_video_for_shorts(r"D:\RENDER\PremierePro\demons_shorts_full.mp4")
