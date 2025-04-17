# Still Under Development
import yt_dlp

# YouTube video URL
url = "https://youtu.be/P3cuFDs3vgA?si=EghUTaaAb0Cz867R"

# yt-dlp download options
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'outtmpl': '%(title)s.%(ext)s',  # Save as video title
    'merge_output_format': 'mp4',    # Output file format
    'noplaylist': True,              # Only single video
    'quiet': False,                  # Show logs
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',     # Final format
    }],
}

# Start downloading
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
