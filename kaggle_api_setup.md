## Install kaggle API<br>
``` !pip install kaggle```<br>

## Upload kaggle.json<br>
```from google.colab import files```<br>
```uploaded = files.upload() ```<br>

## Move it into Kaggle Source Directory<br>
``` !mkdir -p ~/.kaggle```<br>
``` !cp kaggle.json ~/.kaggle/```<br>
``` !chmod 600 ~/.kaggle/kaggle.json ```

## List All Datasets<br>
``` !kaggle datasets list```

## Download a particular dataset<br>
``` !kaggle datasets download -d dataset_name```
