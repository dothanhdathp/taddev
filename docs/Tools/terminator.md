# Terminator

- Công cụ thay cho _**terminal**_ mặc định.
- Công cụ này cũng cho phép thay đổi font chữ và màu sắc, nhìn dễ chịu hơn nhiều.

## Cấu hình

Để sao chép cấu hình, có thể sao chép tệp tại `$HOME/.config/terminator/config`. Sao chép tệp này sang máy khác để lấy lại cấu hình. Nội dung tệp như sau:

```text
[global_config]
  suppress_multiple_term_dialog = True
[keybindings]
  switch_to_tab_1 = <Alt>1
  switch_to_tab_2 = <Alt>2
  switch_to_tab_3 = <Alt>3
  switch_to_tab_4 = <Alt>4
  switch_to_tab_5 = <Alt>5
  switch_to_tab_6 = <Alt>6
  switch_to_tab_7 = <Alt>7
  switch_to_tab_8 = <Alt>8
  switch_to_tab_9 = <Alt>9
[profiles]
  [[default]]
    background_color = "#1e2428"
    background_darkness = 0.9
    foreground_color = "#ffffff"
    palette = "#073642:#dc322f:#2ec27e:#b58900:#0066ff:#d33682:#2aa198:#eee8d5:#002b36:#cb4b16:#586e75:#657b83:#839496:#6c71c4:#93a1a1:#fdf6e3"
    title_transmit_fg_color = "#6cffc1"
    title_transmit_bg_color = "#222b30"
    title_receive_bg_color = "#a51d2d"
    title_inactive_fg_color = "#bde6fb"
    title_inactive_bg_color = "#222b30"
    title_use_system_font = False
[layouts]
  [[default]]
    [[[window0]]]
      type = Window
      parent = ""
    [[[child1]]]
      type = Terminal
      parent = window0
      profile = default
[plugins]
```