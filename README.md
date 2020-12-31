# myEasyOCR
WIP, the goal is to automate images to text translation for foreigner friends

### Download EasyOCR
You will need to download EasyOCR from github
https://github.com/JaidedAI/EasyOCR
<br><br>
### Usage
Copy the link address by right-clicking the image
<br><br>
And input the following in cmd/shell at the directory where the python file at:
```
python main.py [paste your image url here (without sqaure braskets)]
```
<br>
In the first run, it should download the corresponding `cn_tra` model for reading Traditional Chinese automatically.
<br>
If not, please find the model at EasyOCR page and put it into the module's model folder manually.
