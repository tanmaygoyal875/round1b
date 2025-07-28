# Adobe Hackathon Round 1B - Persona-Driven Intelligence

## 🔍 Task

Extract and rank sections from 3–10 PDFs based on a given persona and job-to-be-done.

## 📁 Input

- input/persona.txt → Line 1 = Persona, Line 2 = Job
- input/docs/ → Place 3–10 PDF documents here

## 📤 Output

- output/round1b_output.json → Top ranked sections

## 🐳 Docker Commands

## Step 1: Making img

```
docker build --platform linux/amd64 -t adobehack:round1b .
```

## Step 2: Compiling n Runing

```
docker run --rm   -v "$PWD/input:/app/input"   -v "$PWD/output:/app/output"   --network none   adobehack:round1b
```
