# COGS 18 Final Project
### Glenda Utsler

[![lite-badge](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/UGlenda/COGS18)

Glenda Utsler final project for COGS 18, University of California San Diego (UCSD).

## About this Project

##### The goal of this project is to implement C.R.U.D. operations (Create, Read, Update, Delete) using Python and Jupyter Notebook. The data that this project focuses on are of musical scores. It will be adapted after submission for other key tabs-- specifically, for the Kalimba; a handheld percussion instrument originating from Zimbabwe.

##### The inspiration for this project comes from a personal need for managing a collection of music charts. The needs that this project addresses are as follows:

    Tests with Imported Music Database Collection
    Create, Read, Update, Delete music_list Features
    Sort Feature (General Queries)
    Song Randomizer
    Ability to Delete All Info (to start over with an empty database)
    CRUD.py, SongRandomizerClass.py

### How to Run the Project

*Required Packages*
- pandas
- pytest
- jupyter

run the following in terminal to install if the packages above respectively:
\
``` pip install pandas ```
\
``` pip install pytest ```
\
``` pip install jupyter ```

*Running the Program*
1. Extract the project.
2. In terminal / command line, navigate to the project directory.
3. Type ```jupyter notebook``` then press enter to display the project in a browser.
4. Open the Glenda_Utsler_COGS18_Final_Project.ipynb file.
5. Reload and run all cells.

*Testing the Program*
1. There are three (3) test cases. These cases can be found in the project folder under "*/modules/".
2. Navigate to this directory in terminal, then run ```pytest``` to see the output.

### Next Steps

    Add a transcribing feature to simplify sheet music into letter and number notation for the kalimba.

## Work Used

### DataBase Test Credit
#### MusicNet Dataset, by Gupta, Sparsh
##### Music from the Dataset is sourced from Isabella Stewart Gardner Museum, the European Archive, and Musopen.

https://www.kaggle.com/datasets/imsparsh/musicnet-dataset/

https://storage.googleapis.com/kagglesdsdata/datasets/1167622/1956211/musicnet_metadata.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231211%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231211T043119Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=0d1cb8311f7ba6ff75ed2b7af006927f588979aafe2b2d12a6d869291d382aecbe00e387f6df45b2ea92f0a9e8478a44a7f12006fc7163efb76e5800741b841c273955a25108c3144abac75b13b02f2ee155383087e6c22ac3bd72184ff4f36a052177871b6af3df7bcc026d400e201bd0b6529bbd69d43707ee0936b279babf01516d9e89ec133fef7cc55667440f6de7917a9455fe233e3fad7d520854c82edc733deaa568410517ea2e3c916379bfec3f1a0e08966e0d87cc89bc7495a159efe7361db663aec5960d21e1c40c1b7598b8c53e9b2b419d0406634cc63b64cc49457df235f9eef7ff9fa9b1d84a2502865884ee7464fed56e675c9e32c745f4