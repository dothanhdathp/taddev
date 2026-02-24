# Linux Alsa

> Advanced Linux Sound Architecture

## Công cụ

Bộ công cụ __ALSA__ là bộ công cụ có sẵn trong hệ thống __Ubuntu/Linux__

- [aplay](linux-alsa-aplay.md) : Trình phát chơi nhạc cơ bản
- [amixer](linux-alsa-amixer.md) : ???
- [arecord](linux-alsa-arecord.md) : Trình ghi âm

##### Thông tin

- `aplay -l`: Danh sách __*Playback Devices*__
- `aplay -L`: Danh sách __*PCM devices*__

##### Phát lại

- Phát lại đơn giản:

```bash

```

### arecord

#### Mô tả

`arecord` là một máy ghi âm dòng lệnh cho trình điều khiển __ALSA SoundCard__. Nó hỗ trợ một số định dạng tệp và nhiều âm thanh với nhiều thiết bị.Nếu ghi lại với các mẫu chế độ xen kẽ, tệp sẽ tự động chia trước khi tệp 2GB.

??? note "arecord full help"
    ```txt
    arecord [OPTION]... [FILE]...
    ```

    ```txt
    -h, --help              help
        --version           print current version
    -l, --list-devices      list all soundcards and digital audio devices
    -L, --list-pcms         list device names
    -D, --device=NAME       select PCM by name
    -q, --quiet             quiet mode
    -t, --file-type TYPE    file type (voc, wav, raw or au)
    -c, --channels=#        channels
    -f, --format=FORMAT     sample format (case insensitive)
    -r, --rate=#            sample rate
    -d, --duration=#        interrupt after # seconds
    -s, --samples=#         interrupt after # samples per channel
    -M, --mmap              mmap stream
    -N, --nonblock          nonblocking mode
    -F, --period-time=#     distance between interrupts is # microseconds
    -B, --buffer-time=#     buffer duration is # microseconds
        --period-size=#     distance between interrupts is # frames
        --buffer-size=#     buffer duration is # frames
    -A, --avail-min=#       min available space for wakeup is # microseconds
    -R, --start-delay=#     delay for automatic PCM start is # microseconds
                            (relative to buffer size if <= 0)
    -T, --stop-delay=#      delay for automatic PCM stop is # microseconds from xrun
    -v, --verbose           show PCM structure and setup (accumulative)
    -V, --vumeter=TYPE      enable VU meter (TYPE: mono or stereo)
    -I, --separate-channels one file for each channel
    -i, --interactive       allow interactive operation from stdin
    -m, --chmap=ch1,ch2,..  Give the channel map to override or follow
        --disable-resample  disable automatic rate resample
        --disable-channels  disable automatic channel conversions
        --disable-format    disable automatic format conversions
        --disable-softvol   disable software volume control (softvol)
        --test-position     test ring buffer position
        --test-coef=#       test coefficient for ring buffer position (default 8)
                            expression for validation is: coef * (buffer_size / 2)
        --test-nowait       do not wait for ring buffer - eats whole CPU
        --max-file-time=#   start another output file when the old file has recorded
                            for this many seconds
        --process-id-file   write the process ID here
        --use-strftime      apply the strftime facility to the output file name
        --dump-hw-params    dump hw_params of the device
        --fatal-errors      treat all errors as fatal
    ```

    ```txt
    Recognized sample formats are: S8 U8 S16_LE S16_BE U16_LE U16_BE S24_LE S24_BE U24_LE U24_BE S32_LE S32_BE U32_LE U32_BE FLOAT_LE FLOAT_BE FLOAT64_LE FLOAT64_BE IEC958_SUBFRAME_LE IEC958_SUBFRAME_BE MU_LAW A_LAW IMA_ADPCM MPEG GSM S20_LE S20_BE U20_LE U20_BE SPECIAL S24_3LE S24_3BE U24_3LE U24_3BE S20_3LE S20_3BE U20_3LE U20_3BE S18_3LE S18_3BE U18_3LE U18_3BE G723_24 G723_24_1B G723_40 G723_40_1B DSD_U8 DSD_U16_LE DSD_U32_LE DSD_U16_BE DSD_U32_BE
    Some of these may not be available on selected hardware
    The available format shortcuts are:
    -f cd (16 bit little endian, 44100, stereo)
    -f cdr (16 bit big endian, 44100, stereo)
    -f dat (16 bit little endian, 48000, stereo)
    ```

#### Ví dụ

##### lấy thông tin

- `arecord -h`: hiển thị bảng 
- `arecord -l`: hiển thị danh sách các thiết bị âm thanh khả dụng cho ghi âm.
- `arecord -L`: hiển thị danh sách các PCM được sử dụng cho ghi âm.

##### Ghi âm

```bash
arecord -d 10 -f cd -t wav myrecording.wav
```

- `-d 10`: dừng thu sau 10 giây
- `-f cd`: ghi âm theo chất lượng CD _(16 bit little endian, 44100, stereo)_
- `-f cd`: ghi âm theo chất lượng CD _(16 bit little endian, 44100, stereo)_
- `-t wav`: loại tệp là `wav`
- `myrecording.wav`: Tên tệp

### alsamixer

### amixer

## Reference

- [wikipedia](https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture)