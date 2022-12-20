Intro to Machine Learning
=========================

Machine learning is a branch of artificial intelligence that enables algorithms to automatically learn from data without being explicitly programmed.Its practitioners train algorithms to identify patterns in data and to make decisions with minimal human intervention.

Machine learning is used when:

- The rules cannot be coded in to arrive at the outcome. eg: Recognizing emails as spam or not.
- We want to scale for huge datasets. eg: Recognizing spam or not for millions of emails.

The key component of a machine learning process is the training. How do you train machines? Think of how you teach children to recognise objects. So, if you want him/her to recognise cats, you show him/her photos of cats, or real cats and she soon starts knowing which is a cat; and that a dog is not a cat. 

The examples you show are like feeding input data (image of cat or dog) with output (which is cat, and which is dog) into a machine during a training process. The output is the program that will recognise cats and dogs. A good machine learning system always learns from experience and updates the program to improve the performance.  

The followings are a few more examples in machine learning:

- Recognizing patterns:
    - Facial identities or facial expressions
    - Handwritten or spoken words
    - Tumour detection from medical images

- Generating patterns:
    - Generating images or motion sequences

- Recognizing anomalies:
    - Dizziness detection of drivers
    - Unusual patterns of sensor readings in a nuclear power plant

- Predictions:
    - Future stock prices or currency exchange rates
    - Traffic volume forecasting

There are 3 major types of learning that can be used to develop ML models. 

**Supervised learning** - 
Supervised learning is simply a formalization of the idea of learning from examples. The algorithm is fed data with labels to learn from it. In supervised learning, the learner (typically, a computer program) is provided with two sets of data, a training set and a test set. The idea is for the learner to learn from a set of labeled examples in the training set so that it can identify unlabeled examples in the test set with the highest possible accuracy. That is, the goal of the learner is to develop a rule, a program, or a procedure that estimates outcomes of new examples (in the test set) by analyzing the examples it has been given. There are two kinds of supervised learning, ``Classification`` when the label data is categorical or class, and ``Regression`` when expected outcomes are numerical values.

**Unsupervised learning** - 
This type of algorithm trains and learns from input data without labelled response. There will not be any pre-existing labels and human intervention is also less. It is mostly used in exploratory analysis as it can automatically identify the structure in data. Cluster analysis is the most popular example of unsupervised learning.

**Reinforcement learning** - 
This model is used in making a sequence of decisions. It is learning by interacting with the environment. It is based on the observation that intelligent agents tend to repeat the action that are rewarded for and refrain from action that are punished for. It can be said that it is a trial-and-error method in finding the best outcome based on experience.

**Deep Learning** is a more specialised type of machine learning enabling significant advancement over traditional ML. So, while in conventional machine learning, we extract the features from data and feed it to the system whereas in deep learning, algorithms are capable of extracting features. 
