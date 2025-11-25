# \[Tool\] FFmpeg

Chuyển đổi video

## To FLAC

=== "MP4 to FLAC"
    ```bash
    ffmpeg -i input.mp4 -vn -c:a flac output.flac
    ```
=== "WEBM to FLAC"
    ```bash
    ffmpeg -i input.webm -vn -c:a flac output.flac
    ```