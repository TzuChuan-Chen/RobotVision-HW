HW2 BMP 格式圖檔調整亮度與直方圖等化
==================================

* bmp_graylevel_TF.py >> 以HW1的bmp_rgbquad.py來修改，可以對圖片做簡單的 Gray Level Transformations
* bmp_reader.py >> 延續HW1用來讀取BMP的資料
* 輸出結果都在output資料夾(如果沒有須自行創建)

1. Image negatives (additional)
```python
    log_bmp = GetBMPData('logarithm.bmp')
    file_header = log_bmp.file_header
    info_header = log_bmp.info_header
    image_rgb = log_bmp.rgb_quad
    image_data = log_bmp.image_data
    image_create("negatives","output/negatives.bmp", 1) 
```
2. Log transformation
```python
    log_bmp = GetBMPData('logarithm.bmp')
    file_header = log_bmp.file_header
    info_header = log_bmp.info_header
    image_rgb = log_bmp.rgb_quad
    image_data = log_bmp.image_data
    image_create("log", "output/log.bmp", 1)
```
3. Power-Law transformation
```python
    power_law_bmp = GetBMPData('power_law.bmp')
    file_header = power_law_bmp.file_header
    info_header = power_law_bmp.info_header
    image_rgb = power_law_bmp.rgb_quad
    image_data = power_law_bmp.image_data
    image_create("power law","output/powerlaw.bmp", 1, 5)
```
4. Histogram Equalization
```python
    power_law_bmp = GetBMPData('HistogramEQ.bmp')
    file_header = power_law_bmp.file_header
    info_header = power_law_bmp.info_header
    image_rgb = power_law_bmp.rgb_quad
    image_data = power_law_bmp.image_data
    image_create("histogram equalization","output/histogram_equalization.bmp") 
```