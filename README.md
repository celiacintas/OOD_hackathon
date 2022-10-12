## Identifying out of distribution samples in healthcare :  skin cancer and malaria as use cases

**Authors: Girmaw Abebe Tadesse & Celia Cintas**

Most machine learning (ML) models assume ideal conditions and rely on the assumption that test/clinical data comes from the same distribution of the training samples. However, this assumption is not satisfied in most real-world applications; in a clinical setting, we can find different hardware devices,  environmental conditions, diverse patient characteristics with different or unknown disease samples.

Recent advances in deep learning have led to breakthroughs in the development of automated medical disease diagnosis. As we observe an increasing interest in these models in the healthcare space, it is crucial to address aspects such as the robustness towards these variations, i.e., input data distribution shifts. Current models tend to make incorrect inferences for test samples from different hardware devices and clinical settings or unknown conditions samples, which are out-of-distribution (OOD) from the training samples. 

In this project we will explore multiple ML solutions to search effective approaches that detect these OOD samples prior to making any decision.  Often the approaches shouldn't require prior knowledge of the OOD samples (e.g., during training) to mimic practical settings. We will validate our OOD detection approach in two use cases: 
- identify samples collected from different protocols.
- detect samples from unknown/new disease classes.  

The solution pipeline mainly consists of  data-preprocessing, model selection and fine-tuning, characterization of in-distribution (ID) samples, quantification for divergence from ID samples and performance evaluation.

 

Two publicly available datasets will be used in the project:

- [**BBBC04**](https://bbbc.broadinstitute.org/BBBC041): Images are in .png or .jpg format. There are 3 sets of images consisting of 1364 images (~80,000 cells) with different researchers having prepared each one: from Brazil (Stefanie Lopes), from Southeast Asia (Benoit Malleret), and time course (Gabriel Rangel). The data consists of two classes of uninfected cells (RBCs and leukocytes) and four classes of infected cells (gametocytes, rings, trophozoites, and schizonts). 

 

- [**ISIC 2019**](https://challenge.isic-archive.com/data/): dataset consists of 25,331 dermoscopic images among eight diagnostic categories: Melanoma, Melanocytic nevus, Basal cell carcinoma, Actinic keratosis, Benign keratosis, Dermatofibroma, Vascular lesion}, and Squamous cell carcinoma. As its test set is not available publicly, we set aside Dermatofibroma (DF) and Vascular lesion (VASC) samples during training, and utilize them as OOD samples of unknown diseases during testing. 


References:

- Zaida, Muhammad, et al. "Out of distribution detection for skin and malaria images." arXiv preprint arXiv:2111.01505 (2021).
- Kim, Hannah, et al. "Out-of-distribution detection in dermatology using input perturbation and subset scanning." 2022 IEEE 19th International Symposium on Biomedical Imaging (ISBI). IEEE, 2022.

 
### Outline

#### Day 1

 - Introduction to computer vision and medical imaging.
   - Introduction to data structures, preprocessing and visualization.
 - Types of machine learning algorithms (Supervised, Unsupervised and Semi-Supervised).
   - Model selection and training (simple One SVM, Isolation Forest). 
   - Types of validations (cross validation, stratified cross-validation, etc).
   - Basic evaluation metrics and performance visualization.
   - Threshold-based metrics (Accuracy, Precision, Recall, Specificity, F-score).
 - Present preliminary results.

#### Day 2

- From traditional models to Deep learning models.
  - Building blocks (AEs & GANs).
- Transfer learning.
- Basic evaluation metrics and performance visualization.
- Present preliminary results.

Day 3 (only half day)

- Tips \& Tricks for efective presentations. 
- Prepare slides with proposed solution and comparisons.
- Discuss lessons learned and limitations of the chosen approach.



