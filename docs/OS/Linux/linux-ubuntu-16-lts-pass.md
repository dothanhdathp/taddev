# Change Sudo Password

## Đổi mật khẩu

Đổi mật khẩu bằng lệnh:

```bash
sudo passwd
```

Nhưng ở bước này sẽ có yêu cầu kiểm tra về độ dài và ký tự. Không thể cài đặt `<SPACE>` cho mật khẩu. (Mình thích cài đặt này trên các máy thử nghiệm).

Có điều vãn còn một vấn đề, lệnh đó có thể yêu cầu quyền sửa cho root không chính thức nên để chắc chắn nên dùng lệnh:

```bash
sudo passwd $user
```

## Bỏ qua kiểm tra

Sử dụng lệnh sau vào sửa đổi tệp cấu hình:

```bash
sudo nano /etc/pam.d/common-password
```

```text title="/etc/pam.d/common-password"
#
# /etc/pam.d/common-password - password-related modules common to all services
#
# This file is included from other service-specific PAM config files,
# and should contain a list of modules that define the services to be
# used to change user passwords.  The default is pam_unix.

# Explanation of pam_unix options:
#
# The "sha512" option enables salted SHA512 passwords.  Without this option,
# the default is Unix crypt.  Prior releases used the option "md5".
#
# The "obscure" option replaces the old `OBSCURE_CHECKS_ENAB' option in
# login.defs.
#
# See the pam_unix manpage for other options.

# As of pam 1.0.1-6, this file is managed by pam-auth-update by default.
# To take advantage of this, it is recommended that you configure any
# local modules either before or after the default block, and use
# pam-auth-update to manage selection of other modules.  See
# pam-auth-update(8) for details.

# here are the per-package modules (the "Primary" block)
password        [success=1 default=ignore]      pam_unix.so obscure sha512
# here's the fallback if no module succeeds
password        requisite                       pam_deny.so
# prime the stack with a positive return value if there isn't one already;
# this avoids us returning an error just because nothing sets a success code
# since the modules above will each just jump around
password        required                        pam_permit.so
# and here are more per-package modules (the "Additional" block)
password        optional        pam_gnome_keyring.so
# end of pam-auth-update config
```

Từ đây có hai cách:

Hướng dẫn __*Stack Overflow*__ nói rằng chỉ cần sửa: 

=== "From"
    ```text
    password        [success=1 default=ignore]   pam_unix.so obscure sha512
    ```
=== "To"
    ```text
    password        [success=1 default=ignore]   pam_unix.so obscure sha512 minlen=1
    ```

Nhưng mình làm sai dòng, thế là:

=== "From"
    ```text
    password        requisite                       pam_deny.so
    ```
=== "To"
    ```text
    password        requisite                       pam_deny.so minlen=1
    ```

Nhưng mà vẫn thành công. Thế thôi kệ đi.