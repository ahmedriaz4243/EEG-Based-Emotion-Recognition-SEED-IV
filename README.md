# Project: Emotion Recognition using EEG based Data DEED IV.

This Python project aims to predict emotions in individuals based on EEG-based data. The project utilizes transfer **learning techniques** , including **EEGITNET**  , to build a predictive model.

### Getting Started
These instructions will guide you on how to set up the project on your local machine for development and testing purposes.

### Prerequisites
To run this project, you'll need Python 3.x, GPU and the following libraries installed:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* pickle
* mne
* tensorflow-addons

###### You can install these libraries using the following command:

pip install pandas numpy matplotlib seaborn scikit-learn pickle

### Project Structure
The project is organized as follows:

- tl_helper.py : All helper function to read and explore the data files.
- bci_ml_cross_subject_eeg_itnet.py: Implemented simple Base model for cross subject classifcation.
- bci_tl_cross_subject_eeg_itnet.py: Implemented transfer learning for cross subject classifcation.
- bci_ml_within_subject_eeg_itnet.py: Implemented simple Base model for within subject classifcation
- bci_tl_within_subject_eeg_itnet.py: Implemented transfer learning for within subject classifcation

* Usage
To run the project, simply execute the relevant file. This will preprocess the data, extract relevant features, train the model with EEGITNET, and evaluate the model's performance.

Make sure to include all the necessary details to help users understand the project and its functionality.

### Dataset Acknowledgements

The following data is used in this study. To utilize the dataset, simply request to authors, download it and adjust the file paths according to your setup.

I would like to express my gratitude to the authors and contributors of the SEED_IV dataset for making it publicly available. The dataset informattion can be found at the following link:

[SEED IV Dataset](https://bcmi.sjtu.edu.cn/home/seed/seed-iv.html#)

Please cite the dataset using the following reference:

Wei-Long Zheng, Wei Liu, Yifei Lu, Bao-Liang Lu, and Andrzej Cichocki, EmotionMeter: A Multimodal Framework for Recognizing Human Emotions. IEEE Transactions on Cybernetics, Volume: 49, Issue: 3, March 2019, Pages: 1110-1122, DOI: 10.1109/TCYB.2018.2797176

<pre>
```bibtex
@ARTICLE{8283814, author={W. Zheng and W. Liu and Y. Lu and B. Lu and A. Cichocki}, journal={IEEE Transactions on Cybernetics},
 title={EmotionMeter: A Multimodal Framework for Recognizing Human Emotions}, year={2018}, volume={}, number={}, pages={1-13}, 
 keywords={Electroencephalography;Emotion recognition;Electrodes;Feature extraction;Human computer interaction;Biological neural networks;
 Brain modeling;Affective brain-computer interactions;deep learning;EEG;emotion recognition;eye movements;multimodal deep neural networks},
 doi={10.1109/TCYB.2018.2797176}, ISSN={2168-2267},}
```
</pre>

If you use the EEGITNet model in your research and found it helpful, please cite the following paper:

<pre>
```bibtex
@article{Salami_2022,
	doi = {10.1109/access.2022.3161489},
	url = {https://doi.org/10.1109%2Faccess.2022.3161489},
	year = 2022,
	publisher = {Institute of Electrical and Electronics Engineers ({IEEE})},
	volume = {10},
	pages = {36672--36685},
	author = {Abbas Salami and Javier Andreu-Perez and Helge Gillmeister},
	title = {{EEG}-{ITNet}: An Explainable Inception Temporal Convolutional Network for Motor Imagery Classification}, 
	journal = {{IEEE} Access}
}
```
</pre>


If you use the EEGNet model in your research and found it helpful, please cite the following paper:

<pre>
```bibtex
@article{Lawhern2018,
  author={Vernon J Lawhern and Amelia J Solon and Nicholas R Waytowich and Stephen M Gordon and Chou P Hung and Brent J Lance},
  title={EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces},
  journal={Journal of Neural Engineering},
  volume={15},
  number={5},
  pages={056013},
  url={http://stacks.iop.org/1741-2552/15/i=5/a=056013},
  year={2018}
}
```
</pre>
