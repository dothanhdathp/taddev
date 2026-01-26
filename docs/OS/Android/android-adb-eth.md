# \[Android\] ADB ETH

> Android __adb__ an __ethernet__

## Connect

## Read Pass

=== "Cũ"
    ```bash
    cat /data/misc/wifi/wpa_supplicant.conf
    ```
=== "Mới"
    ```bash
    cat /data/misc/apexdata/com.android.wifi/WifiConfigStore.xml
    ```

    Đọc từ trên xuống lấy __*WifiConfiguration*__

    ```text
    <WifiConfiguration>
    <string name="ConfigKey">&quot;tot_home2G_12f&quot;WPA_PSK</string>
    <string name="SSID">&quot;tot_home2G_12f&quot;</string>
    <string name="PreSharedKey">&quot;74200075&quot;</string>
    ```