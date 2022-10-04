HW2 BMP 格式圖檔調整亮度與直方圖等化(分成3個檔案的版本)
==================================

* bmp_reader.py >> 延續HW1用來讀取BMP的資料
* hw2_LogT.py >> 增強暗部
* hw2_HistEqliz.py >> 增強亮部
* hw2_PowerLawT.py >> 直方圖等化
* 輸出結果都在output資料夾(如果沒有須自行創建)

1. Log transformation
```python
if __name__ == "__main__":
    # 取得logarithm.bmp的資料
    log_bmp = GetBMPData('logarithm.bmp')
    file_header = log_bmp.file_header
    info_header = log_bmp.info_header
    image_rgb = log_bmp.rgb_quad
    image_data = log_bmp.image_data
    image_create("log", "output/log.bmp", 1)
```
2. Power-Law transformation
```python
if __name__ == "__main__":
    # 取得power_law.bmp的資料
    power_law_bmp = GetBMPData('power_law.bmp')
    file_header = power_law_bmp.file_header
    info_header = power_law_bmp.info_header
    image_rgb = power_law_bmp.rgb_quad
    image_data = power_law_bmp.image_data
    image_create("power law","output/powerlaw.bmp", 1, 5)
```
3. Histogram Equalization
```python
if __name__ == "__main__":
    # 取得power_law.bmp的資料
    hist_eq_bmp = GetBMPData('HistogramEQ.bmp')
    file_header = hist_eq_bmp.file_header
    info_header = hist_eq_bmp.info_header
    image_rgb = hist_eq_bmp.rgb_quad
    image_data = hist_eq_bmp.image_data
    output_image_data = image_create("histogram equalization","output/hist_eqliz.bmp") 
```