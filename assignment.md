# Assignment: Evaluate a Jev Service (e.g., LLM-Based Classification)

## Objective

Build a small service that imitates Jev's typed evaluation API, then compare it with Jev on a labeled dataset.

The goal is not to reproduce Jev internally. We want to see how you research an unfamiliar API, design a reliable dataset, implement a compatible service, and evaluate the results.

## Tasks

### 1. Create a dataset

Create a dataset containing at least **20 labeled examples** suitable for testing Jev.

You are encouraged to explore existing public datasets, such as those on Hugging Face, instead of inventing every example yourself. Cite the dataset and explain how you selected or adapted its examples.

Requirements:

- Include at least one classification task, such as intent routing or sentiment.
- Include at least one boolean or rubric-based evaluation task.
- Store the expected answer for every example.
- Explain where the examples and labels came from.
- Do not use Jev's own output as ground truth.

### 2. Build a Jev-compatible service

Implement an HTTP service backed by a general-purpose model, such as GPT.

The service should match Jev's API as closely as practical:

- Accept a shared `state` and multiple named `questions`.
- Support the Jev question types used in your dataset.
- Return a typed answer and confidence for every question.
- Validate malformed requests and return useful errors.

Document any intentional differences from Jev.

### 3. Evaluate both services

Run the same dataset against Jev and your implementation. Compare them using accuracy or another suitable quality metric.

## Submission

Submit your work in a GitHub repository with clear instructions for running it.
