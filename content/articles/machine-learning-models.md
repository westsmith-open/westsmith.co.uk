description: A practical guide to machine learning models — from classical techniques to LLMs. What each model type does, when to use it, and why reaching for an LLM every time is often the wrong call.
title: Machine Learning Models: A Practical Guide | Westsmith
author: Daniel Ball, founder of Westsmith

# Machine Learning Models

<img src="/static/images/articles/models.png" alt="Machine learning models overview">

## Introduction

In this article, we will demystify the term **model** and explore the evolving landscape of machine learning tools. We will also cover the difference between classical models and modern LLMs and show you the tradeoffs between running models locally, in the cloud or via an API.

Picking the right ML tool for the job is where we want to get to at the end, instead of plugging everything into a ChatGPT terminal. If you're a software developer, system architect or tech-curious builder wondering how to integrate ML wisely, this is for you.

There is also a heavy focus on examples in **Python**. If you don't know Python, do still read on — hopefully you'll get inspired to learn it as well as discovering the underpinnings of modern AI.

### Resources / TLDR

**Communities**

- [Kaggle](https://www.kaggle.com/) — The largest AI and ML community
- [Hugging Face](https://huggingface.co/) — The platform where the machine learning community collaborates on models, datasets and applications

**Tools**

- [Open Router Models](https://openrouter.ai/models) — Access any hosted LLM model from one interface
- [Github Models](https://docs.github.com/en/github-models) — Find and experiment with AI models for free
- [Jupyter](https://jupyter.org/) — ML engineers and data scientists use this to write Python code that interfaces with ML models
- [PyTorch](https://pytorch.org/), [TensorFlow](https://www.tensorflow.org/) and [JAX](https://docs.jax.dev/en/latest/) — The backbone of modern AI
- [scikit-learn](https://scikit-learn.org/) — Python library for building most types of ML model

**Learning**

- [W3Schools Machine Learning course](https://www.w3schools.com/python/python_ml_getting_started.asp)
- [Google Machine Learning Education](https://developers.google.com/machine-learning)
- [StatQuest YouTube channel](https://www.youtube.com/@statquest) — The best beginner-friendly ML YouTube channel
- Free ML courses from [Harvard](https://pll.harvard.edu/course/machine-learning-and-ai-python), [IBM](https://www.coursera.org/learn/machine-learning-with-python) and [FreeCodeCamp](https://www.freecodecamp.org/learn/machine-learning-with-python/)

## What is a Model?

In Machine Learning, a **model** refers to a mathematical construct trained to make decisions or predictions based on input data. Once you've trained or created a model, you can use it to create new data or predictions from an input it's never seen before.

GPT, Gemini and Claude are examples of **Large Language Models** and are perhaps the most well-known type of ML model by the general public. However, these are very extreme examples and represent the high end in a spectrum of model complexity.

Before AI became known for chatbots and image generators, professionals who dealt with data (such as data scientists) used — and still do use — a variety of machine learning models to make predictions, detect patterns or sort information. These models were usually small, focused and trained on structured data like spreadsheets or databases.

## Types of ML Models

### 1. Linear Models — The Straight-Line Thinker

<img src="/static/images/articles/linear.png" alt="Linear Model" style="width: 300px;">

Draws a line or curve through data points to spot trends and make predictions.

- **Used for**: Forecasting sales, predicting prices
- **Strength**: Simple, fast, easy to interpret
- **Weakness**: Can't handle complex relationships

---

### 2. Decision Trees — The Flowchart Brain

<img src="/static/images/articles/decision_tree.png" alt="Decision Tree" style="width: 300px;">

Asks a series of yes/no questions to make a decision.

- **Used for**: Loan approval, medical diagnoses
- **Strength**: Easy to understand and explain
- **Weakness**: Can overfit and make decisions that don't generalise

---

### 3. Random Forests — The Crowd of Flowcharts

<img src="/static/images/articles/random_forest.png" alt="Random Forest" style="width: 300px;">

Builds many decision trees and combines their answers to improve accuracy.

- **Used for**: Risk scoring, product recommendations
- **Strength**: More accurate and robust
- **Weakness**: Harder to explain decisions

---

### 4. Clustering Models — The Natural Group Finder

<img src="/static/images/articles/clustering.png" alt="Clustering Models" style="width: 300px;">

Groups similar things together without knowing the labels ahead of time.

- **Used for**: Customer segments, user behaviour patterns
- **Strength**: Great for discovery
- **Weakness**: Can be sensitive to noise or unclear groups

---

### 5. Naive Bayes — The Probability Calculator

<img src="/static/images/articles/bayes.png" alt="Bayes" style="width: 300px;">

Makes predictions based on how likely something is, given past data.

- **Used for**: Spam filters, topic classification
- **Strength**: Very fast
- **Weakness**: Can oversimplify complex problems

---

### 6. Support Vector Machines (SVMs) — The Border Drawer

<img src="/static/images/articles/svm.png" alt="SVM" style="width: 300px;">

Draws the best dividing line between different categories in your data.

- **Used for**: Image classification, face detection
- **Strength**: Precise with clean data
- **Weakness**: Not great with lots of messy or overlapping data

---

### 7. Neural Networks — The Brain-Inspired Pattern Learner

<img src="/static/images/articles/neural.png" alt="Neural Network" style="width: 300px;">

Mathematical models inspired by biological neural networks, consisting of interconnected nodes organised in layers that process and transform input data.

- **Used for**: Pattern recognition, classification, prediction
- **Strength**: Can learn complex relationships
- **Weakness**: Need careful tuning, can be unstable

---

### 8. Deep Learning — The Advanced Pattern Master

<img src="/static/images/articles/deep.png" alt="Deep Learning" style="width: 200px;">

Deep learning refers to neural networks with many layers. These additional layers allow the network to learn increasingly complex features from data automatically. LLM models such as GPT and Gemini fall into this category.

- **Used for**: Computer vision, language models, speech recognition
- **Strength**: Learns complex patterns automatically, state-of-the-art performance
- **Weakness**: Needs massive data/compute, complex to train, black box behaviour

### Summary

| Model Type | Example Use Case | Can it Handle Complex Data? | Needs Lots of Data? | Easy to Understand? |
| --- | --- | --- | --- | --- |
| Linear Model | Predicting house prices | No | No | Yes |
| Decision Tree | Loan approval | Some | No | Yes |
| Random Forest | Fraud detection | Yes | Medium | Kind of |
| Clustering | Market segmentation | Some | Medium | Sometimes |
| Naive Bayes | Spam detection | No | No | Yes |
| SVM | Face detection | Yes | Medium | No |
| Neural Network | Voice or image recognition | Yes | Yes | No |
| Deep Learning (Transformers, CNNs) | Language, vision, etc. | Yes | Yes (lots) | Very hard |

## Choosing the Right Model for the Job

### If your data is structured (tables, numbers, categories):

**Use classical ML models** like Logistic Regression, Decision Trees / Random Forests, or XGBoost / LightGBM.

**Examples:**
- Predicting churn from customer data
- Scoring leads in a CRM
- Classifying transactions as fraud or not

✅ Fast — ✅ Explainable — ✅ Can run locally — ❌ Not great for messy or unstructured input

> If the data fits in a spreadsheet, you probably don't need a neural net.

### If your input is text and the output is a simple label:

**Use smaller NLP models** (not full LLMs) like RoBERTa, DistilBERT or fastText.

**Examples:**
- Categorising support tickets
- Sentiment analysis
- Spam detection

✅ Lightweight and fast — ✅ More accurate than old-school methods — ❌ Doesn't generate language, just classifies

> You don't need ChatGPT to decide if a tweet is angry or not.

### If you're working with images or video:

**Use vision models** like ResNet / MobileNet / EfficientNet (classification), YOLO / Detectron2 (object detection), or CLIP / BLIP (image + text tasks).

✅ Purpose-built and efficient — ✅ Can run on phones or edge devices — ❌ Needs labelled image data to train

### If your input is audio or speech:

**Use audio models** like Whisper (speech-to-text), wav2vec2 (speech recognition), or TTS models.

✅ Highly accurate models available open-source — ✅ Works well offline — ❌ Audio data can be large and tricky to process

### If you need language generation, summarisation or reasoning:

**Now you're in LLM territory**: GPT-4 / Claude / Gemini via commercial APIs, or LLaMA / Mistral / Phi as open-source options.

**Examples:**
- Summarising a legal document
- Explaining code
- Writing email drafts or documentation
- Chatbots with memory and logic

✅ Extremely powerful — ✅ Very general-purpose — ❌ Can be expensive — ❌ May hallucinate — ❌ Overkill for small classification tasks

> Use LLMs for jobs that involve language reasoning.

### Decision Table

| Task Type | Recommended Model Type | Example Tool |
| --- | --- | --- |
| Predict from tabular data | Decision Tree | XGBoost, LightGBM |
| Classify short texts | NLP | DistilBERT, fastText |
| Summarise/generate text | LLM | GPT, Claude, Mistral |
| Understand images | CNN | YOLO, ResNet, BLIP |
| Transcribe speech | ASR | Whisper |
| Group similar users | K-means Clustering | Scikit-learn |
| Detect sentiment in reviews | NLP | RoBERTa |
| Write SEO blog posts | LLM | GPT-4, Claude |

### Final Advice: Use the Smallest Model That Works

You wouldn't call a rocket scientist to fix a leaky tap — and you shouldn't call an LLM when a few `if` statements would do.

But sometimes LLMs are the right call. If the task involves nuance, ambiguity or creativity, or if you need a prototype right now and tokens are cheap, go ahead. Just know there's a whole toolbox behind it and sometimes a hammer really is better than a sledgehammer.

## The LLM-ification of Everything (and why it's a Problem)

Large Language Models are incredibly capable — they can summarise, classify, generate, reason and write code. Given that power, it's no surprise that many developers now reach for LLMs as the default tool for every ML problem.

But just because you _can_ use an LLM doesn't mean you _should_.

### Why Everyone's Using LLMs for Everything

- **Low barrier to entry** — You don't need to collect data, train anything or understand ML theory. Just write a prompt and get results.
- **One tool for many tasks** — You can classify sentiment, summarise articles, translate languages and chat, all from the same API.
- **Faster prototyping** — Especially for startups and small teams, LLMs let you get a working product today.

### The Problems with Treating LLMs as a Catch-All

**Wasteful overhead** — You're using a billion-parameter model to do what a 5MB model could have done. Classifying tweets as positive or negative? A fine-tuned BERT could do it faster and cheaper.

**Scaling costs** — An LLM call might cost fractions of a cent, but multiply that by millions of users and you're bleeding money. Traditional models are nearly free to run once deployed.

**Latency** — Even the fastest LLMs are slower than traditional models. A call to a hosted LLM takes 200ms–1s+. A local scikit-learn model returns results in milliseconds.

**Loss of specialisation** — LLMs are generalists. A fine-tuned fraud detection model trained on your data will almost always beat an LLM trying to "reason" its way to a result.

**Skills atrophy** — When LLMs become a catch-all, developers stop learning about classical ML, statistics and feature engineering. That's dangerous in regulated, high-stakes or performance-sensitive environments.

### A Better Approach: Use LLMs for What They're Great At

Use LLMs for language understanding, generation and reasoning. Use traditional models when you want speed, predictable output, privacy, simplicity or cost-efficiency.

A good architecture might look like:
1. Use LLMs at the edge to route or clean messy data
2. Pass that to a lightweight classifier or ranking model
3. Return a response that's fast, traceable and explainable

## How to Access and Run Models

### Commercial APIs

The easiest route is to use models via APIs:

- Anthropic's Claude
- OpenAI's GPT-4o
- Google's Gemini

✅ Fastest time to value — ✅ Extremely powerful models — ⚠️ Black-box — ⚠️ Pay-per-use, costs can scale fast

### Hosting Locally

Running smaller models like Phi-3-mini or Gemma 2B on a laptop is increasingly feasible via tools like [Ollama](https://ollama.com/) or [LM Studio](https://lmstudio.ai/).

✅ Full privacy — ✅ Free after setup — ⚠️ Limited power

### Hourly Cloud Compute

Platforms like [RunPod](https://www.runpod.io/) and [LambdaLabs](https://lambda.ai/) let you spin up a GPU machine by the hour.

✅ On-demand power — ✅ No hardware investment — ⚠️ Pay-as-you-go can become expensive

### Enterprise ML Platforms

Platforms like [Amazon SageMaker](https://aws.amazon.com/sagemaker/) and [MLFlow](https://mlflow.org/) provide integrated environments for model development, deployment and management at enterprise scale.

✅ End-to-end ML workflow management — ✅ Built-in security and governance — ⚠️ Requires enterprise licensing

## Acquiring Models from Hugging Face

Hugging Face hosts a wide range of machine learning models, especially those built with PyTorch, TensorFlow and JAX. All models are free or open source, but you will need to provide the compute resource to run them.

| Model Type | Hosted on Hugging Face? | Notes |
| --- | --- | --- |
| Transformers (LLMs) | ✅ Yes | Hugging Face's core focus (e.g. GPT-style, BERT, LLaMA) |
| CNNs for vision | ✅ Yes | Models like ResNet, YOLO and CLIP |
| Audio models | ✅ Yes | Whisper, wav2vec2, TTS |
| Small/efficient LMs (SLMs) | ✅ Yes | e.g. DistilBERT, TinyLLaMA, Phi-3 |
| Embeddings / vector models | ✅ Yes | Sentence Transformers |
| Classical ML via sklearn | ⚠️ Limited | A few examples, mostly for education |
| XGBoost / LightGBM | ⚠️ Rare | Not commonly hosted |
| Rule-based or statistical models | 🚫 Not really | Usually too simple to share as models |
