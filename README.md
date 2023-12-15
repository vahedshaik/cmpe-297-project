# CMPE 297 - Deep Learning Special Topics Project
_____________________________________________________________________________________________________________________________________________
**Team Spartan**
Abdul Vahed Shaik
_____________________________________________________________________________________________________________________________________________

# **Lingua Vertex: Language modeling with vertex ai**

The daily use of data for a variety of objectives, including marketing, business, sentiment analysis, election prediction, and communication has increased rapidly.
1. Text Classification, Sentiment Analysis
2. Summarization

**Classifying Emotions through Custom Training using Vertex AI.**
I successfully accomplished emotion classification by fine-tuning a pretrained BERT model. Additionally, I automated all essential steps of the machine learning system, including data collection, model deployment, and serving, utilizing GCP and Vertex AI.

**Dataset**
Emotion from Hugging Face Datasets: The dataset comprises labels across various classes, representing Twitter messages associated with six fundamental emotions: anger, fear, joy, love, sadness, and surprise..

**GCP and Vertex AI**
**Objective**: My aim is to perform custom training on a pre-trained PyTorch model based on BERT, fine-tuning it with different hyperparameter values, and deploying it within the Vertex AI pipeline for emotion classification.

Vertex AI serves as an integrated MLOps platform, empowering data scientists and ML engineers to enhance experimentation, accelerate deployment, and confidently manage models. It facilitates the swift building, deployment, and scaling of ML models through a unified AI platform that combines pre-trained capabilities and customizable tools.

It functions as an AI platform facilitating the creation of a comprehensive ML application by seamlessly incorporating various Google Cloud services. Vertex AI offers distinctive features, including:

1. A unified user interface spanning the entire ML workflow.
2. End-to-end integration for both data and AI processes.
3. Pre-trained APIs catering to vision, video, natural language, and more.
4. Compatibility with all major open-source frameworks.

For projects involving extensive datasets and models, the most efficient approach is constructing a training pipeline using Vertex AI. The training job on Vertex AI involves packaging the code and establishing a training pipeline to coordinate the execution of the training process. The process entails three key steps:

	a)Packaging the training code as a Python source distribution and submitting the training job to Vertex AI.
 	b)Hyperparameter Tuning Job - Throughout the fine-tuning process of the BERT model, I conducted experiments involving key hyperparameters 	such as learning rate and weight decay. The outcomes of these trials, along with details about the best-performing model, are presented 		below.

![image](https://github.com/vahedshaik/cmpe-297-project/assets/112588672/7d05226b-83b2-4a9d-8555-a5fc8ed6863a)

	c)Finally deploying the best model to an endpoint on Vertex AI.

 Following the fine-tuning of the BERT model, we deploy its predictions on the Streamlit application through the utilization of Google Cloud's 'aiplatform' library.

	*Displayed below is a screenshot of the model, showcasing predictions specifically for the emotion of Joy:

<img width="446" alt="Screen Shot 2023-12-15 at 7 49 48 AM" src="https://github.com/vahedshaik/cmpe-297-project/assets/112588672/79ba56d3-4d1a-461c-9871-f6b11837f1aa">

	*Displayed below is a screenshot of the model, showcasing predictions specifically for the emotion of fear:
 
 <img width="401" alt="Screen Shot 2023-12-15 at 7 50 54 AM" src="https://github.com/vahedshaik/cmpe-297-project/assets/112588672/4d499a78-6c2a-4b7b-8198-8dfedcdb6e50">

 *Displayed below is a screenshot of the model, showcasing predictions specifically for the emotion of anger:

 <img width="448" alt="Screen Shot 2023-12-15 at 7 51 35 AM" src="https://github.com/vahedshaik/cmpe-297-project/assets/112588672/ec140bf4-4bbe-402c-a909-9ac42e5ec9de">

 **TensorBoard logs capturing the fine-tuning process of the BERT model locally, including accuracy, training loss, and validation loss, are shown below:**

 <img width="499" alt="Screen Shot 2023-12-15 at 7 52 53 AM" src="https://github.com/vahedshaik/cmpe-297-project/assets/112588672/562b2b7a-76e2-4510-8178-ca7f8b856f44">

_____________________________________________________________________________________________________________________________________________
**References:**
 https://huggingface.co/datasets/emotion

 https://github.com/nlpunibo/Question-Answering-SQUAD

 https://huggingface.co/transformers/

 https://huggingface.co/human-centered-summarization/financial-summarization-pegasus

 


 



